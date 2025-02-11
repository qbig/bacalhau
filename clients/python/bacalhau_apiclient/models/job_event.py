# coding: utf-8

"""
    Bacalhau API

    This page is the reference of the Bacalhau REST API. Project docs are available at https://docs.bacalhau.org/. Find more information about Bacalhau at https://github.com/bacalhau-project/bacalhau.  # noqa: E501

    OpenAPI spec version: 0.3.18.post4
    Contact: team@bacalhau.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from bacalhau_apiclient.configuration import Configuration


class JobEvent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'client_id': 'str',
        'deal': 'JobEventDeal',
        'event_name': 'JobEventType',
        'event_time': 'str',
        'execution_id': 'str',
        'job_execution_plan': 'JobEventJobExecutionPlan',
        'job_id': 'str',
        'published_result': 'StorageSpec',
        'run_output': 'JobEventRunOutput',
        'sender_public_key': 'list[int]',
        'shard_index': 'int',
        'source_node_id': 'str',
        'spec': 'JobEventJobExecutionPlan',
        'status': 'str',
        'target_node_id': 'str',
        'verification_proposal': 'list[int]',
        'verification_result': 'VerificationResult'
    }

    attribute_map = {
        'api_version': 'APIVersion',
        'client_id': 'ClientID',
        'deal': 'Deal',
        'event_name': 'EventName',
        'event_time': 'EventTime',
        'execution_id': 'ExecutionID',
        'job_execution_plan': 'JobExecutionPlan',
        'job_id': 'JobID',
        'published_result': 'PublishedResult',
        'run_output': 'RunOutput',
        'sender_public_key': 'SenderPublicKey',
        'shard_index': 'ShardIndex',
        'source_node_id': 'SourceNodeID',
        'spec': 'Spec',
        'status': 'Status',
        'target_node_id': 'TargetNodeID',
        'verification_proposal': 'VerificationProposal',
        'verification_result': 'VerificationResult'
    }

    def __init__(self, api_version=None, client_id=None, deal=None, event_name=None, event_time=None, execution_id=None, job_execution_plan=None, job_id=None, published_result=None, run_output=None, sender_public_key=None, shard_index=None, source_node_id=None, spec=None, status=None, target_node_id=None, verification_proposal=None, verification_result=None, _configuration=None):  # noqa: E501
        """JobEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_version = None
        self._client_id = None
        self._deal = None
        self._event_name = None
        self._event_time = None
        self._execution_id = None
        self._job_execution_plan = None
        self._job_id = None
        self._published_result = None
        self._run_output = None
        self._sender_public_key = None
        self._shard_index = None
        self._source_node_id = None
        self._spec = None
        self._status = None
        self._target_node_id = None
        self._verification_proposal = None
        self._verification_result = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if client_id is not None:
            self.client_id = client_id
        if deal is not None:
            self.deal = deal
        if event_name is not None:
            self.event_name = event_name
        if event_time is not None:
            self.event_time = event_time
        if execution_id is not None:
            self.execution_id = execution_id
        if job_execution_plan is not None:
            self.job_execution_plan = job_execution_plan
        if job_id is not None:
            self.job_id = job_id
        if published_result is not None:
            self.published_result = published_result
        if run_output is not None:
            self.run_output = run_output
        if sender_public_key is not None:
            self.sender_public_key = sender_public_key
        if shard_index is not None:
            self.shard_index = shard_index
        if source_node_id is not None:
            self.source_node_id = source_node_id
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status
        if target_node_id is not None:
            self.target_node_id = target_node_id
        if verification_proposal is not None:
            self.verification_proposal = verification_proposal
        if verification_result is not None:
            self.verification_result = verification_result

    @property
    def api_version(self):
        """Gets the api_version of this JobEvent.  # noqa: E501

        APIVersion of the Job  # noqa: E501

        :return: The api_version of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this JobEvent.

        APIVersion of the Job  # noqa: E501

        :param api_version: The api_version of this JobEvent.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def client_id(self):
        """Gets the client_id of this JobEvent.  # noqa: E501

        optional clientID if this is an externally triggered event (like create job)  # noqa: E501

        :return: The client_id of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this JobEvent.

        optional clientID if this is an externally triggered event (like create job)  # noqa: E501

        :param client_id: The client_id of this JobEvent.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def deal(self):
        """Gets the deal of this JobEvent.  # noqa: E501


        :return: The deal of this JobEvent.  # noqa: E501
        :rtype: JobEventDeal
        """
        return self._deal

    @deal.setter
    def deal(self, deal):
        """Sets the deal of this JobEvent.


        :param deal: The deal of this JobEvent.  # noqa: E501
        :type: JobEventDeal
        """

        self._deal = deal

    @property
    def event_name(self):
        """Gets the event_name of this JobEvent.  # noqa: E501


        :return: The event_name of this JobEvent.  # noqa: E501
        :rtype: JobEventType
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this JobEvent.


        :param event_name: The event_name of this JobEvent.  # noqa: E501
        :type: JobEventType
        """

        self._event_name = event_name

    @property
    def event_time(self):
        """Gets the event_time of this JobEvent.  # noqa: E501


        :return: The event_time of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this JobEvent.


        :param event_time: The event_time of this JobEvent.  # noqa: E501
        :type: str
        """

        self._event_time = event_time

    @property
    def execution_id(self):
        """Gets the execution_id of this JobEvent.  # noqa: E501

        compute execution identifier  # noqa: E501

        :return: The execution_id of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this JobEvent.

        compute execution identifier  # noqa: E501

        :param execution_id: The execution_id of this JobEvent.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def job_execution_plan(self):
        """Gets the job_execution_plan of this JobEvent.  # noqa: E501


        :return: The job_execution_plan of this JobEvent.  # noqa: E501
        :rtype: JobEventJobExecutionPlan
        """
        return self._job_execution_plan

    @job_execution_plan.setter
    def job_execution_plan(self, job_execution_plan):
        """Sets the job_execution_plan of this JobEvent.


        :param job_execution_plan: The job_execution_plan of this JobEvent.  # noqa: E501
        :type: JobEventJobExecutionPlan
        """

        self._job_execution_plan = job_execution_plan

    @property
    def job_id(self):
        """Gets the job_id of this JobEvent.  # noqa: E501


        :return: The job_id of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobEvent.


        :param job_id: The job_id of this JobEvent.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def published_result(self):
        """Gets the published_result of this JobEvent.  # noqa: E501


        :return: The published_result of this JobEvent.  # noqa: E501
        :rtype: StorageSpec
        """
        return self._published_result

    @published_result.setter
    def published_result(self, published_result):
        """Sets the published_result of this JobEvent.


        :param published_result: The published_result of this JobEvent.  # noqa: E501
        :type: StorageSpec
        """

        self._published_result = published_result

    @property
    def run_output(self):
        """Gets the run_output of this JobEvent.  # noqa: E501


        :return: The run_output of this JobEvent.  # noqa: E501
        :rtype: JobEventRunOutput
        """
        return self._run_output

    @run_output.setter
    def run_output(self, run_output):
        """Sets the run_output of this JobEvent.


        :param run_output: The run_output of this JobEvent.  # noqa: E501
        :type: JobEventRunOutput
        """

        self._run_output = run_output

    @property
    def sender_public_key(self):
        """Gets the sender_public_key of this JobEvent.  # noqa: E501


        :return: The sender_public_key of this JobEvent.  # noqa: E501
        :rtype: list[int]
        """
        return self._sender_public_key

    @sender_public_key.setter
    def sender_public_key(self, sender_public_key):
        """Sets the sender_public_key of this JobEvent.


        :param sender_public_key: The sender_public_key of this JobEvent.  # noqa: E501
        :type: list[int]
        """

        self._sender_public_key = sender_public_key

    @property
    def shard_index(self):
        """Gets the shard_index of this JobEvent.  # noqa: E501

        what shard is this event for  # noqa: E501

        :return: The shard_index of this JobEvent.  # noqa: E501
        :rtype: int
        """
        return self._shard_index

    @shard_index.setter
    def shard_index(self, shard_index):
        """Sets the shard_index of this JobEvent.

        what shard is this event for  # noqa: E501

        :param shard_index: The shard_index of this JobEvent.  # noqa: E501
        :type: int
        """

        self._shard_index = shard_index

    @property
    def source_node_id(self):
        """Gets the source_node_id of this JobEvent.  # noqa: E501

        the node that emitted this event  # noqa: E501

        :return: The source_node_id of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        """Sets the source_node_id of this JobEvent.

        the node that emitted this event  # noqa: E501

        :param source_node_id: The source_node_id of this JobEvent.  # noqa: E501
        :type: str
        """

        self._source_node_id = source_node_id

    @property
    def spec(self):
        """Gets the spec of this JobEvent.  # noqa: E501


        :return: The spec of this JobEvent.  # noqa: E501
        :rtype: JobEventJobExecutionPlan
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this JobEvent.


        :param spec: The spec of this JobEvent.  # noqa: E501
        :type: JobEventJobExecutionPlan
        """

        self._spec = spec

    @property
    def status(self):
        """Gets the status of this JobEvent.  # noqa: E501


        :return: The status of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobEvent.


        :param status: The status of this JobEvent.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def target_node_id(self):
        """Gets the target_node_id of this JobEvent.  # noqa: E501

        the node that this event is for e.g. \"AcceptJobBid\" was emitted by Requester but it targeting compute node  # noqa: E501

        :return: The target_node_id of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._target_node_id

    @target_node_id.setter
    def target_node_id(self, target_node_id):
        """Sets the target_node_id of this JobEvent.

        the node that this event is for e.g. \"AcceptJobBid\" was emitted by Requester but it targeting compute node  # noqa: E501

        :param target_node_id: The target_node_id of this JobEvent.  # noqa: E501
        :type: str
        """

        self._target_node_id = target_node_id

    @property
    def verification_proposal(self):
        """Gets the verification_proposal of this JobEvent.  # noqa: E501


        :return: The verification_proposal of this JobEvent.  # noqa: E501
        :rtype: list[int]
        """
        return self._verification_proposal

    @verification_proposal.setter
    def verification_proposal(self, verification_proposal):
        """Sets the verification_proposal of this JobEvent.


        :param verification_proposal: The verification_proposal of this JobEvent.  # noqa: E501
        :type: list[int]
        """

        self._verification_proposal = verification_proposal

    @property
    def verification_result(self):
        """Gets the verification_result of this JobEvent.  # noqa: E501


        :return: The verification_result of this JobEvent.  # noqa: E501
        :rtype: VerificationResult
        """
        return self._verification_result

    @verification_result.setter
    def verification_result(self, verification_result):
        """Sets the verification_result of this JobEvent.


        :param verification_result: The verification_result of this JobEvent.  # noqa: E501
        :type: VerificationResult
        """

        self._verification_result = verification_result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(JobEvent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobEvent):
            return True

        return self.to_dict() != other.to_dict()
