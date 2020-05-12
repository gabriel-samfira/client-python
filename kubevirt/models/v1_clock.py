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


class V1Clock(object):
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
        'timer': 'V1Timer',
        'timezone': 'str',
        'utc': 'V1ClockOffsetUTC'
    }

    attribute_map = {
        'timer': 'timer',
        'timezone': 'timezone',
        'utc': 'utc'
    }

    def __init__(self, timer=None, timezone=None, utc=None):
        """
        V1Clock - a model defined in Swagger
        """

        self._timer = None
        self._timezone = None
        self._utc = None

        if timer is not None:
          self.timer = timer
        if timezone is not None:
          self.timezone = timezone
        if utc is not None:
          self.utc = utc

    @property
    def timer(self):
        """
        Gets the timer of this V1Clock.
        Timer specifies whih timers are attached to the vmi.

        :return: The timer of this V1Clock.
        :rtype: V1Timer
        """
        return self._timer

    @timer.setter
    def timer(self, timer):
        """
        Sets the timer of this V1Clock.
        Timer specifies whih timers are attached to the vmi.

        :param timer: The timer of this V1Clock.
        :type: V1Timer
        """

        self._timer = timer

    @property
    def timezone(self):
        """
        Gets the timezone of this V1Clock.
        Timezone sets the guest clock to the specified timezone. Zone name follows the TZ environment variable format (e.g. 'America/New_York').

        :return: The timezone of this V1Clock.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this V1Clock.
        Timezone sets the guest clock to the specified timezone. Zone name follows the TZ environment variable format (e.g. 'America/New_York').

        :param timezone: The timezone of this V1Clock.
        :type: str
        """

        self._timezone = timezone

    @property
    def utc(self):
        """
        Gets the utc of this V1Clock.
        UTC sets the guest clock to UTC on each boot. If an offset is specified, guest changes to the clock will be kept during reboots and are not reset.

        :return: The utc of this V1Clock.
        :rtype: V1ClockOffsetUTC
        """
        return self._utc

    @utc.setter
    def utc(self, utc):
        """
        Sets the utc of this V1Clock.
        UTC sets the guest clock to UTC on each boot. If an offset is specified, guest changes to the clock will be kept during reboots and are not reset.

        :param utc: The utc of this V1Clock.
        :type: V1ClockOffsetUTC
        """

        self._utc = utc

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
        if not isinstance(other, V1Clock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
