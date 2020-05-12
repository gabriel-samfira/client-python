# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1VirtualMachineInstanceMigrationState(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'abort_requested': 'bool',
        'abort_status': 'str',
        'completed': 'bool',
        'end_timestamp': 'V1Time',
        'failed': 'bool',
        'migration_uid': 'str',
        'source_node': 'str',
        'start_timestamp': 'V1Time',
        'target_direct_migration_node_ports': 'dict(str, int)',
        'target_node': 'str',
        'target_node_address': 'str',
        'target_node_domain_detected': 'bool',
        'target_pod': 'str'
    }

    attribute_map = {
        'abort_requested': 'abortRequested',
        'abort_status': 'abortStatus',
        'completed': 'completed',
        'end_timestamp': 'endTimestamp',
        'failed': 'failed',
        'migration_uid': 'migrationUid',
        'source_node': 'sourceNode',
        'start_timestamp': 'startTimestamp',
        'target_direct_migration_node_ports': 'targetDirectMigrationNodePorts',
        'target_node': 'targetNode',
        'target_node_address': 'targetNodeAddress',
        'target_node_domain_detected': 'targetNodeDomainDetected',
        'target_pod': 'targetPod'
    }

    def __init__(self, abort_requested=None, abort_status=None, completed=None, end_timestamp=None, failed=None, migration_uid=None, source_node=None, start_timestamp=None, target_direct_migration_node_ports=None, target_node=None, target_node_address=None, target_node_domain_detected=None, target_pod=None):
        """
        V1VirtualMachineInstanceMigrationState - a model defined in Swagger
        """

        self._abort_requested = None
        self._abort_status = None
        self._completed = None
        self._end_timestamp = None
        self._failed = None
        self._migration_uid = None
        self._source_node = None
        self._start_timestamp = None
        self._target_direct_migration_node_ports = None
        self._target_node = None
        self._target_node_address = None
        self._target_node_domain_detected = None
        self._target_pod = None

        if abort_requested is not None:
          self.abort_requested = abort_requested
        if abort_status is not None:
          self.abort_status = abort_status
        if completed is not None:
          self.completed = completed
        if end_timestamp is not None:
          self.end_timestamp = end_timestamp
        if failed is not None:
          self.failed = failed
        if migration_uid is not None:
          self.migration_uid = migration_uid
        if source_node is not None:
          self.source_node = source_node
        if start_timestamp is not None:
          self.start_timestamp = start_timestamp
        if target_direct_migration_node_ports is not None:
          self.target_direct_migration_node_ports = target_direct_migration_node_ports
        if target_node is not None:
          self.target_node = target_node
        if target_node_address is not None:
          self.target_node_address = target_node_address
        if target_node_domain_detected is not None:
          self.target_node_domain_detected = target_node_domain_detected
        if target_pod is not None:
          self.target_pod = target_pod

    @property
    def abort_requested(self):
        """
        Gets the abort_requested of this V1VirtualMachineInstanceMigrationState.
        Indicates that the migration has been requested to abort

        :return: The abort_requested of this V1VirtualMachineInstanceMigrationState.
        :rtype: bool
        """
        return self._abort_requested

    @abort_requested.setter
    def abort_requested(self, abort_requested):
        """
        Sets the abort_requested of this V1VirtualMachineInstanceMigrationState.
        Indicates that the migration has been requested to abort

        :param abort_requested: The abort_requested of this V1VirtualMachineInstanceMigrationState.
        :type: bool
        """

        self._abort_requested = abort_requested

    @property
    def abort_status(self):
        """
        Gets the abort_status of this V1VirtualMachineInstanceMigrationState.
        Indicates the final status of the live migration abortion

        :return: The abort_status of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._abort_status

    @abort_status.setter
    def abort_status(self, abort_status):
        """
        Sets the abort_status of this V1VirtualMachineInstanceMigrationState.
        Indicates the final status of the live migration abortion

        :param abort_status: The abort_status of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._abort_status = abort_status

    @property
    def completed(self):
        """
        Gets the completed of this V1VirtualMachineInstanceMigrationState.
        Indicates the migration completed

        :return: The completed of this V1VirtualMachineInstanceMigrationState.
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """
        Sets the completed of this V1VirtualMachineInstanceMigrationState.
        Indicates the migration completed

        :param completed: The completed of this V1VirtualMachineInstanceMigrationState.
        :type: bool
        """

        self._completed = completed

    @property
    def end_timestamp(self):
        """
        Gets the end_timestamp of this V1VirtualMachineInstanceMigrationState.
        The time the migration action ended

        :return: The end_timestamp of this V1VirtualMachineInstanceMigrationState.
        :rtype: V1Time
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this V1VirtualMachineInstanceMigrationState.
        The time the migration action ended

        :param end_timestamp: The end_timestamp of this V1VirtualMachineInstanceMigrationState.
        :type: V1Time
        """

        self._end_timestamp = end_timestamp

    @property
    def failed(self):
        """
        Gets the failed of this V1VirtualMachineInstanceMigrationState.
        Indicates that the migration failed

        :return: The failed of this V1VirtualMachineInstanceMigrationState.
        :rtype: bool
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """
        Sets the failed of this V1VirtualMachineInstanceMigrationState.
        Indicates that the migration failed

        :param failed: The failed of this V1VirtualMachineInstanceMigrationState.
        :type: bool
        """

        self._failed = failed

    @property
    def migration_uid(self):
        """
        Gets the migration_uid of this V1VirtualMachineInstanceMigrationState.
        The VirtualMachineInstanceMigration object associated with this migration

        :return: The migration_uid of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._migration_uid

    @migration_uid.setter
    def migration_uid(self, migration_uid):
        """
        Sets the migration_uid of this V1VirtualMachineInstanceMigrationState.
        The VirtualMachineInstanceMigration object associated with this migration

        :param migration_uid: The migration_uid of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._migration_uid = migration_uid

    @property
    def source_node(self):
        """
        Gets the source_node of this V1VirtualMachineInstanceMigrationState.
        The source node that the VMI originated on

        :return: The source_node of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._source_node

    @source_node.setter
    def source_node(self, source_node):
        """
        Sets the source_node of this V1VirtualMachineInstanceMigrationState.
        The source node that the VMI originated on

        :param source_node: The source_node of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._source_node = source_node

    @property
    def start_timestamp(self):
        """
        Gets the start_timestamp of this V1VirtualMachineInstanceMigrationState.
        The time the migration action began

        :return: The start_timestamp of this V1VirtualMachineInstanceMigrationState.
        :rtype: V1Time
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """
        Sets the start_timestamp of this V1VirtualMachineInstanceMigrationState.
        The time the migration action began

        :param start_timestamp: The start_timestamp of this V1VirtualMachineInstanceMigrationState.
        :type: V1Time
        """

        self._start_timestamp = start_timestamp

    @property
    def target_direct_migration_node_ports(self):
        """
        Gets the target_direct_migration_node_ports of this V1VirtualMachineInstanceMigrationState.
        The list of ports opened for live migration on the destination node

        :return: The target_direct_migration_node_ports of this V1VirtualMachineInstanceMigrationState.
        :rtype: dict(str, int)
        """
        return self._target_direct_migration_node_ports

    @target_direct_migration_node_ports.setter
    def target_direct_migration_node_ports(self, target_direct_migration_node_ports):
        """
        Sets the target_direct_migration_node_ports of this V1VirtualMachineInstanceMigrationState.
        The list of ports opened for live migration on the destination node

        :param target_direct_migration_node_ports: The target_direct_migration_node_ports of this V1VirtualMachineInstanceMigrationState.
        :type: dict(str, int)
        """

        self._target_direct_migration_node_ports = target_direct_migration_node_ports

    @property
    def target_node(self):
        """
        Gets the target_node of this V1VirtualMachineInstanceMigrationState.
        The target node that the VMI is moving to

        :return: The target_node of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._target_node

    @target_node.setter
    def target_node(self, target_node):
        """
        Sets the target_node of this V1VirtualMachineInstanceMigrationState.
        The target node that the VMI is moving to

        :param target_node: The target_node of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._target_node = target_node

    @property
    def target_node_address(self):
        """
        Gets the target_node_address of this V1VirtualMachineInstanceMigrationState.
        The address of the target node to use for the migration

        :return: The target_node_address of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._target_node_address

    @target_node_address.setter
    def target_node_address(self, target_node_address):
        """
        Sets the target_node_address of this V1VirtualMachineInstanceMigrationState.
        The address of the target node to use for the migration

        :param target_node_address: The target_node_address of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._target_node_address = target_node_address

    @property
    def target_node_domain_detected(self):
        """
        Gets the target_node_domain_detected of this V1VirtualMachineInstanceMigrationState.
        The Target Node has seen the Domain Start Event

        :return: The target_node_domain_detected of this V1VirtualMachineInstanceMigrationState.
        :rtype: bool
        """
        return self._target_node_domain_detected

    @target_node_domain_detected.setter
    def target_node_domain_detected(self, target_node_domain_detected):
        """
        Sets the target_node_domain_detected of this V1VirtualMachineInstanceMigrationState.
        The Target Node has seen the Domain Start Event

        :param target_node_domain_detected: The target_node_domain_detected of this V1VirtualMachineInstanceMigrationState.
        :type: bool
        """

        self._target_node_domain_detected = target_node_domain_detected

    @property
    def target_pod(self):
        """
        Gets the target_pod of this V1VirtualMachineInstanceMigrationState.
        The target pod that the VMI is moving to

        :return: The target_pod of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._target_pod

    @target_pod.setter
    def target_pod(self, target_pod):
        """
        Sets the target_pod of this V1VirtualMachineInstanceMigrationState.
        The target pod that the VMI is moving to

        :param target_pod: The target_pod of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._target_pod = target_pod

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1VirtualMachineInstanceMigrationState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
