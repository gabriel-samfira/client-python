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


class V1PITTimer(object):
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
        'present': 'bool',
        'tick_policy': 'str'
    }

    attribute_map = {
        'present': 'present',
        'tick_policy': 'tickPolicy'
    }

    def __init__(self, present=None, tick_policy=None):
        """
        V1PITTimer - a model defined in Swagger
        """

        self._present = None
        self._tick_policy = None

        if present is not None:
          self.present = present
        if tick_policy is not None:
          self.tick_policy = tick_policy

    @property
    def present(self):
        """
        Gets the present of this V1PITTimer.
        Enabled set to false makes sure that the machine type or a preset can't add the timer. Defaults to true.

        :return: The present of this V1PITTimer.
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """
        Sets the present of this V1PITTimer.
        Enabled set to false makes sure that the machine type or a preset can't add the timer. Defaults to true.

        :param present: The present of this V1PITTimer.
        :type: bool
        """

        self._present = present

    @property
    def tick_policy(self):
        """
        Gets the tick_policy of this V1PITTimer.
        TickPolicy determines what happens when QEMU misses a deadline for injecting a tick to the guest. One of \"delay\", \"catchup\", \"discard\".

        :return: The tick_policy of this V1PITTimer.
        :rtype: str
        """
        return self._tick_policy

    @tick_policy.setter
    def tick_policy(self, tick_policy):
        """
        Sets the tick_policy of this V1PITTimer.
        TickPolicy determines what happens when QEMU misses a deadline for injecting a tick to the guest. One of \"delay\", \"catchup\", \"discard\".

        :param tick_policy: The tick_policy of this V1PITTimer.
        :type: str
        """

        self._tick_policy = tick_policy

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
        if not isinstance(other, V1PITTimer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
