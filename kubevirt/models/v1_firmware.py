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


class V1Firmware(object):
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
        'bootloader': 'V1Bootloader',
        'serial': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'bootloader': 'bootloader',
        'serial': 'serial',
        'uuid': 'uuid'
    }

    def __init__(self, bootloader=None, serial=None, uuid=None):
        """
        V1Firmware - a model defined in Swagger
        """

        self._bootloader = None
        self._serial = None
        self._uuid = None

        if bootloader is not None:
          self.bootloader = bootloader
        if serial is not None:
          self.serial = serial
        if uuid is not None:
          self.uuid = uuid

    @property
    def bootloader(self):
        """
        Gets the bootloader of this V1Firmware.
        Settings to control the bootloader that is used.

        :return: The bootloader of this V1Firmware.
        :rtype: V1Bootloader
        """
        return self._bootloader

    @bootloader.setter
    def bootloader(self, bootloader):
        """
        Sets the bootloader of this V1Firmware.
        Settings to control the bootloader that is used.

        :param bootloader: The bootloader of this V1Firmware.
        :type: V1Bootloader
        """

        self._bootloader = bootloader

    @property
    def serial(self):
        """
        Gets the serial of this V1Firmware.
        The system-serial-number in SMBIOS

        :return: The serial of this V1Firmware.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this V1Firmware.
        The system-serial-number in SMBIOS

        :param serial: The serial of this V1Firmware.
        :type: str
        """

        self._serial = serial

    @property
    def uuid(self):
        """
        Gets the uuid of this V1Firmware.
        UUID reported by the vmi bios. Defaults to a random generated uid.

        :return: The uuid of this V1Firmware.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this V1Firmware.
        UUID reported by the vmi bios. Defaults to a random generated uid.

        :param uuid: The uuid of this V1Firmware.
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, V1Firmware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
