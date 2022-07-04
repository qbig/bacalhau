package computenode

import (
	"context"
	"fmt"
	"math/rand"
	"strconv"
	"strings"
	"sync"
	"testing"
	"time"

	"github.com/davecgh/go-spew/spew"
	"github.com/filecoin-project/bacalhau/pkg/computenode"
	"github.com/filecoin-project/bacalhau/pkg/executor"
	noop_executor "github.com/filecoin-project/bacalhau/pkg/executor/noop"
	"github.com/filecoin-project/bacalhau/pkg/job"
	_ "github.com/filecoin-project/bacalhau/pkg/logger"
	"github.com/filecoin-project/bacalhau/pkg/resourceusage"
	"github.com/filecoin-project/bacalhau/pkg/system"
	"github.com/filecoin-project/bacalhau/pkg/verifier"
	"github.com/stretchr/testify/assert"
)

func TestJobResourceLimits(t *testing.T) {
	runTest := func(jobResources, jobResourceLimits, defaultJobResourceLimits resourceusage.ResourceUsageConfig, expectedResult bool) {
		computeNode, _, cm := SetupTestNoop(t, computenode.ComputeNodeConfig{
			JobResourceLimit:               jobResourceLimits,
			DefaultJobResourceRequirements: defaultJobResourceLimits,
		}, noop_executor.ExecutorConfig{})
		defer cm.Cleanup()
		job := GetProbeData("")
		job.Spec.Resources = jobResources

		result, err := computeNode.SelectJob(context.Background(), job)
		assert.NoError(t, err)
		assert.Equal(t, expectedResult, result, fmt.Sprintf("the expcted result was %v, but got %v -- %+v vs %+v", expectedResult, result, jobResources, jobResourceLimits))
	}

	// the job is half the limit
	runTest(
		getResources("1", "500Mb"),
		getResources("2", "1Gb"),
		getResources("100m", "100Mb"),
		true,
	)

	// the job is on the limit
	runTest(
		getResources("1", "500Mb"),
		getResources("1", "500Mb"),
		getResources("100m", "100Mb"),
		true,
	)

	// the job is over the limit
	runTest(
		getResources("2", "1Gb"),
		getResources("1", "500Mb"),
		getResources("100m", "100Mb"),
		false,
	)

	// test with fractional CPU
	// the job is less than the limit
	runTest(
		getResources("250m", "200Mb"),
		getResources("1", "500Mb"),
		getResources("100m", "100Mb"),
		true,
	)

	// test when the limit is empty
	runTest(
		getResources("250m", "200Mb"),
		getResources("", ""),
		getResources("100m", "100Mb"),
		true,
	)

	// test when both is empty
	runTest(
		getResources("", ""),
		getResources("", ""),
		getResources("100m", "100Mb"),
		true,
	)

	runTest(
		getResources("", ""),
		getResources("250m", "200Mb"),
		getResources("100m", "100Mb"),
		true,
	)

	runTest(
		getResources("300m", ""),
		getResources("250m", "200Mb"),
		getResources("100m", "100Mb"),
		false,
	)

}

type SeenJobRecord struct {
	Id          string
	CurrentJobs int
	MaxJobs     int
	Start       int64
	End         int64
}

type TotalResourceTestCaseCheck struct {
	name    string
	handler func(seenJobs []SeenJobRecord) (bool, error)
}

type TotalResourceTestCase struct {
	// the total list of jobs to throw at the cluster all at the same time
	jobs        []resourceusage.ResourceUsageConfig
	totalLimits resourceusage.ResourceUsageConfig
	wait        TotalResourceTestCaseCheck
	checkers    []TotalResourceTestCaseCheck
}

func TestTotalResourceLimits(t *testing.T) {

	// for this test we use the transport so the compute_node is calling
	// the executor in a go-routine and we can test what jobs
	// look like over time - this test leave each job running for X seconds
	// and consuming Y resources
	// we will have set a total amount of resources on the compute_node
	// and we want to see that the following things are true:
	//
	//  * all jobs ran eventually (because there is no per job limit and no one job is bigger than the total limit)
	//  * at no time - the total job resource usage exceeds the configured total
	//  * we submit all the jobs at the same time so we prove that compute_nodes "back bid"
	//    * i.e. a job that was seen 20 seconds ago we now have space to run so let's bid on it now
	//
	runTest := func(
		testCase TotalResourceTestCase,
	) {

		epochSeconds := time.Now().Unix()

		seenJobs := []SeenJobRecord{}
		var seenJobsMutex sync.Mutex

		addSeenJob := func(job SeenJobRecord) {
			seenJobsMutex.Lock()
			defer seenJobsMutex.Unlock()
			seenJobs = append(seenJobs, job)
		}

		currentJobCount := 0
		maxJobCount := 0

		_, requestorNode, cm := SetupTestNoop(
			t,
			computenode.ComputeNodeConfig{
				TotalResourceLimit: testCase.totalLimits,
			},

			noop_executor.ExecutorConfig{

				// our function that will "execute the job"
				// record time stamps of start and end
				// sleep for a bit to simulate real work happening
				ExternalHooks: &noop_executor.ExecutorConfigExternalHooks{
					JobHandler: func(ctx context.Context, job *executor.Job) (string, error) {
						currentJobCount++
						if currentJobCount > maxJobCount {
							maxJobCount = currentJobCount
						}
						seenJob := SeenJobRecord{
							Id:          job.ID,
							Start:       time.Now().Unix() - epochSeconds,
							CurrentJobs: currentJobCount,
							MaxJobs:     maxJobCount,
						}
						time.Sleep(time.Second * 1)
						currentJobCount--
						seenJob.End = time.Now().Unix() - epochSeconds
						addSeenJob(seenJob)
						return "", nil
					},
				},
			},
		)
		defer cm.Cleanup()

		for _, jobResources := range testCase.jobs {

			// what the job is doesn't matter - it will only end up
			spec, deal, err := job.ConstructDockerJob(
				executor.EngineNoop,
				verifier.VerifierNoop,
				jobResources.CPU,
				jobResources.Memory,
				[]string{},
				[]string{},
				[]string{},
				[]string{},
				"",
				1,
				[]string{},
			)

			assert.NoError(t, err)
			_, err = requestorNode.Transport.SubmitJob(context.Background(), spec, deal)
			assert.NoError(t, err)

			// sleep a bit here to simulate jobs being sumbmitted over time
			time.Sleep((10 + time.Duration(rand.Intn(10))) * time.Millisecond)
		}

		// wait for all the jobs to have completed
		// we can check the seenJobs because that is easier
		waiter := &system.FunctionWaiter{
			Name:        "wait for jobs",
			MaxAttempts: 10,
			Delay:       time.Second * 1,
			Handler: func() (bool, error) {
				//spew.Dump(seenJobs)
				return testCase.wait.handler(seenJobs)
			},
		}

		err := waiter.Wait()
		assert.NoError(t, err, fmt.Sprintf("there was an error in the wait function: %s", testCase.wait.name))

		if err != nil {
			fmt.Printf("error waiting for jobs to have been seen\n")
			spew.Dump(seenJobs)
		}

		checkOk := true
		failingCheckMessage := ""

		for _, checker := range testCase.checkers {
			innerCheck, err := checker.handler(seenJobs)
			errorMessage := ""
			if err != nil {
				errorMessage = fmt.Sprintf("there was an error in the check function: %s %s", checker.name, err.Error())
			}
			assert.NoError(t, err, errorMessage)
			if !innerCheck {
				checkOk = false
				failingCheckMessage = fmt.Sprintf("there was an fail in the check function: %s", checker.name)
			}
		}

		assert.True(t, checkOk, failingCheckMessage)

		if !checkOk {
			fmt.Printf("error checking results on seen jobs\n")
			spew.Dump(seenJobs)
		}
	}

	waitUntilSeenAllJobs := func(expected int) TotalResourceTestCaseCheck {
		return TotalResourceTestCaseCheck{
			name: fmt.Sprintf("waitUntilSeenAllJobs: %d", expected),
			handler: func(seenJobs []SeenJobRecord) (bool, error) {
				return len(seenJobs) >= expected, nil
			},
		}
	}

	checkMaxJobs := func(max int) TotalResourceTestCaseCheck {
		return TotalResourceTestCaseCheck{
			name: fmt.Sprintf("checkMaxJobs: %d", max),
			handler: func(seenJobs []SeenJobRecord) (bool, error) {
				seenMax := 0
				for _, seenJob := range seenJobs {
					if seenJob.MaxJobs > seenMax {
						seenMax = seenJob.MaxJobs
					}
				}
				return seenMax <= max, nil
			},
		}
	}

	// 2 jobs at a time
	// we should end up with 2 groups of 2 in terms of timing
	// and the highest number of jobs at one time should be 2
	runTest(
		TotalResourceTestCase{
			jobs: getResourcesArray([][]string{
				{"1", "500Mb"},
				{"1", "500Mb"},
				{"1", "500Mb"},
				{"1", "500Mb"},
			}),
			totalLimits: getResources("2", "1Gb"),
			wait:        waitUntilSeenAllJobs(4),
			checkers: []TotalResourceTestCaseCheck{
				// there should only have ever been 2 jobs at one time
				checkMaxJobs(2),
			},
		},
	)

}

func TestDockerResourceLimits(t *testing.T) {

	MEMORY_LIMIT := "100mb"

	computeNode, _, cm := SetupTestDockerIpfs(t, computenode.NewDefaultComputeNodeConfig())
	defer cm.Cleanup()

	result := RunJobGetStdout(t, computeNode, &executor.JobSpec{
		Engine:   executor.EngineDocker,
		Verifier: verifier.VerifierNoop,
		Resources: resourceusage.ResourceUsageConfig{
			CPU:    "100m",
			Memory: MEMORY_LIMIT,
		},
		Docker: executor.JobSpecDocker{
			Image: "ubuntu",
			Entrypoint: []string{
				"bash",
				"-c",
				"grep MemTotal /proc/meminfo | awk '{print $2}'",
			},
		},
	})

	intVar, err := strconv.Atoi(strings.TrimSpace(result))
	assert.NoError(t, err)

	fmt.Printf("memory limit: %d\n", resourceusage.ConvertMemoryString(MEMORY_LIMIT))
	fmt.Printf("result: %d\n", intVar*1024)

	assert.Equal(t, resourceusage.ConvertMemoryString(MEMORY_LIMIT), uint64(intVar*1024), "the container reported memory does not equal the configured limit")
}
