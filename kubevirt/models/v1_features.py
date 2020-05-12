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


class V1Features(object):
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
        'acpi': 'V1FeatureState',
        'apic': 'V1FeatureAPIC',
        'hyperv': 'V1FeatureHyperv',
        'smm': 'V1FeatureState'
    }

    attribute_map = {
        'acpi': 'acpi',
        'apic': 'apic',
        'hyperv': 'hyperv',
        'smm': 'smm'
    }

    def __init__(self, acpi=None, apic=None, hyperv=None, smm=None):
        """
        V1Features - a model defined in Swagger
        """

        self._acpi = None
        self._apic = None
        self._hyperv = None
        self._smm = None

        if acpi is not None:
          self.acpi = acpi
        if apic is not None:
          self.apic = apic
        if hyperv is not None:
          self.hyperv = hyperv
        if smm is not None:
          self.smm = smm

    @property
    def acpi(self):
        """
        Gets the acpi of this V1Features.
        ACPI enables/disables ACPI insidejsondata guest. Defaults to enabled.

        :return: The acpi of this V1Features.
        :rtype: V1FeatureState
        """
        return self._acpi

    @acpi.setter
    def acpi(self, acpi):
        """
        Sets the acpi of this V1Features.
        ACPI enables/disables ACPI insidejsondata guest. Defaults to enabled.

        :param acpi: The acpi of this V1Features.
        :type: V1FeatureState
        """

        self._acpi = acpi

    @property
    def apic(self):
        """
        Gets the apic of this V1Features.
        Defaults to the machine type setting.

        :return: The apic of this V1Features.
        :rtype: V1FeatureAPIC
        """
        return self._apic

    @apic.setter
    def apic(self, apic):
        """
        Sets the apic of this V1Features.
        Defaults to the machine type setting.

        :param apic: The apic of this V1Features.
        :type: V1FeatureAPIC
        """

        self._apic = apic

    @property
    def hyperv(self):
        """
        Gets the hyperv of this V1Features.
        Defaults to the machine type setting.

        :return: The hyperv of this V1Features.
        :rtype: V1FeatureHyperv
        """
        return self._hyperv

    @hyperv.setter
    def hyperv(self, hyperv):
        """
        Sets the hyperv of this V1Features.
        Defaults to the machine type setting.

        :param hyperv: The hyperv of this V1Features.
        :type: V1FeatureHyperv
        """

        self._hyperv = hyperv

    @property
    def smm(self):
        """
        Gets the smm of this V1Features.
        SMM enables/disables System Management Mode. TSEG not yet implemented.

        :return: The smm of this V1Features.
        :rtype: V1FeatureState
        """
        return self._smm

    @smm.setter
    def smm(self, smm):
        """
        Sets the smm of this V1Features.
        SMM enables/disables System Management Mode. TSEG not yet implemented.

        :param smm: The smm of this V1Features.
        :type: V1FeatureState
        """

        self._smm = smm

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
        if not isinstance(other, V1Features):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
