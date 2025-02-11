# bacalhau_apiclient
This page is the reference of the Bacalhau REST API. Project docs are available at https://docs.bacalhau.org/. Find more information about Bacalhau at https://github.com/bacalhau-project/bacalhau.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.3.18.post4
- Package version: 0.3.18.post4
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/bacalhau-project/bacalhau](https://github.com/bacalhau-project/bacalhau)

## Requirements.

Python 3.6+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import bacalhau_apiclient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bacalhau_apiclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import bacalhau_apiclient
from bacalhau_apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bacalhau_apiclient.HealthApi(bacalhau_apiclient.ApiClient(configuration))

try:
    # Returns debug information on what the current node is doing.
    api_response = api_instance.api_serverdebug()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->api_serverdebug: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://bootstrap.production.bacalhau.org:1234*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HealthApi* | [**api_serverdebug**](docs/HealthApi.md#api_serverdebug) | **GET** /debug | Returns debug information on what the current node is doing.
*HealthApi* | [**debug**](docs/HealthApi.md#debug) | **GET** /requester/debug | Returns debug information on what the current node is doing.
*JobApi* | [**events**](docs/JobApi.md#events) | **POST** /requester/events | Returns the events related to the job-id passed in the body payload. Useful for troubleshooting.
*JobApi* | [**list**](docs/JobApi.md#list) | **POST** /requester/list | Simply lists jobs.
*JobApi* | [**local_events**](docs/JobApi.md#local_events) | **POST** /requester/local_events | Returns the node&#39;s local events related to the job-id passed in the body payload. Useful for troubleshooting.
*JobApi* | [**results**](docs/JobApi.md#results) | **POST** /requester/results | Returns the results of the job-id specified in the body payload.
*JobApi* | [**states**](docs/JobApi.md#states) | **POST** /requester/states | Returns the state of the job-id specified in the body payload.
*JobApi* | [**submit**](docs/JobApi.md#submit) | **POST** /requester/submit | Submits a new job to the network.
*MiscApi* | [**api_serverversion**](docs/MiscApi.md#api_serverversion) | **POST** /version | Returns the build version running on the server.
*UtilsApi* | [**healthz**](docs/UtilsApi.md#healthz) | **GET** /healthz |
*UtilsApi* | [**id**](docs/UtilsApi.md#id) | **GET** /id | Returns the id of the host node.
*UtilsApi* | [**livez**](docs/UtilsApi.md#livez) | **GET** /livez |
*UtilsApi* | [**logz**](docs/UtilsApi.md#logz) | **GET** /logz |
*UtilsApi* | [**node_info**](docs/UtilsApi.md#node_info) | **GET** /node_info | Returns the info of the node.
*UtilsApi* | [**peers**](docs/UtilsApi.md#peers) | **GET** /peers | Returns the peers connected to the host via the transport layer.
*UtilsApi* | [**readyz**](docs/UtilsApi.md#readyz) | **GET** /readyz |
*UtilsApi* | [**varz**](docs/UtilsApi.md#varz) | **GET** /varz |


## Documentation For Models

 - [BuildVersionInfo](docs/BuildVersionInfo.md)
 - [ComputeNodeInfo](docs/ComputeNodeInfo.md)
 - [Deal](docs/Deal.md)
 - [Engine](docs/Engine.md)
 - [EventsRequest](docs/EventsRequest.md)
 - [EventsResponse](docs/EventsResponse.md)
 - [FreeSpace](docs/FreeSpace.md)
 - [HealthInfo](docs/HealthInfo.md)
 - [Job](docs/Job.md)
 - [JobEvent](docs/JobEvent.md)
 - [JobEventDeal](docs/JobEventDeal.md)
 - [JobEventJobExecutionPlan](docs/JobEventJobExecutionPlan.md)
 - [JobEventRunOutput](docs/JobEventRunOutput.md)
 - [JobEventType](docs/JobEventType.md)
 - [JobExecutionPlan](docs/JobExecutionPlan.md)
 - [JobLocalEvent](docs/JobLocalEvent.md)
 - [JobLocalEventType](docs/JobLocalEventType.md)
 - [JobNodeState](docs/JobNodeState.md)
 - [JobRequester](docs/JobRequester.md)
 - [JobShardState](docs/JobShardState.md)
 - [JobShardStateState](docs/JobShardStateState.md)
 - [JobShardingConfig](docs/JobShardingConfig.md)
 - [JobSpec](docs/JobSpec.md)
 - [JobSpecDocker](docs/JobSpecDocker.md)
 - [JobSpecLanguage](docs/JobSpecLanguage.md)
 - [JobSpecLanguageJobContext](docs/JobSpecLanguageJobContext.md)
 - [JobSpecWasm](docs/JobSpecWasm.md)
 - [JobSpecWasmEntryModule](docs/JobSpecWasmEntryModule.md)
 - [JobState](docs/JobState.md)
 - [JobStateType](docs/JobStateType.md)
 - [JobStatus](docs/JobStatus.md)
 - [JobStatusJobState](docs/JobStatusJobState.md)
 - [LabelSelectorRequirement](docs/LabelSelectorRequirement.md)
 - [LabelSelectorRequirementOperator](docs/LabelSelectorRequirementOperator.md)
 - [ListRequest](docs/ListRequest.md)
 - [ListResponse](docs/ListResponse.md)
 - [LocalEventsRequest](docs/LocalEventsRequest.md)
 - [LocalEventsResponse](docs/LocalEventsResponse.md)
 - [Metadata](docs/Metadata.md)
 - [MountStatus](docs/MountStatus.md)
 - [Network](docs/Network.md)
 - [NetworkConfig](docs/NetworkConfig.md)
 - [NodeInfo](docs/NodeInfo.md)
 - [NodeType](docs/NodeType.md)
 - [PeerAddrInfo](docs/PeerAddrInfo.md)
 - [PublishedResult](docs/PublishedResult.md)
 - [Publisher](docs/Publisher.md)
 - [ResourceUsageConfig](docs/ResourceUsageConfig.md)
 - [ResourceUsageData](docs/ResourceUsageData.md)
 - [ResultsResponse](docs/ResultsResponse.md)
 - [RunCommandResult](docs/RunCommandResult.md)
 - [SelectionOperator](docs/SelectionOperator.md)
 - [Spec](docs/Spec.md)
 - [SpecDeal](docs/SpecDeal.md)
 - [SpecDocker](docs/SpecDocker.md)
 - [SpecEngine](docs/SpecEngine.md)
 - [SpecExecutionPlan](docs/SpecExecutionPlan.md)
 - [SpecNetwork](docs/SpecNetwork.md)
 - [SpecPublisher](docs/SpecPublisher.md)
 - [SpecResources](docs/SpecResources.md)
 - [SpecSharding](docs/SpecSharding.md)
 - [StateRequest](docs/StateRequest.md)
 - [StateResponse](docs/StateResponse.md)
 - [StorageSourceType](docs/StorageSourceType.md)
 - [StorageSpec](docs/StorageSpec.md)
 - [StorageSpecStorageSource](docs/StorageSpecStorageSource.md)
 - [SubmitRequest](docs/SubmitRequest.md)
 - [SubmitResponse](docs/SubmitResponse.md)
 - [VerificationResult](docs/VerificationResult.md)
 - [Verifier](docs/Verifier.md)
 - [VersionRequest](docs/VersionRequest.md)
 - [VersionResponse](docs/VersionResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

team@bacalhau.org
