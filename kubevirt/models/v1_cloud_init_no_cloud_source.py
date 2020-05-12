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


class V1CloudInitNoCloudSource(object):
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
        'network_data': 'str',
        'network_data_base64': 'str',
        'network_data_secret_ref': 'V1LocalObjectReference',
        'secret_ref': 'V1LocalObjectReference',
        'user_data': 'str',
        'user_data_base64': 'str'
    }

    attribute_map = {
        'network_data': 'networkData',
        'network_data_base64': 'networkDataBase64',
        'network_data_secret_ref': 'networkDataSecretRef',
        'secret_ref': 'secretRef',
        'user_data': 'userData',
        'user_data_base64': 'userDataBase64'
    }

    def __init__(self, network_data=None, network_data_base64=None, network_data_secret_ref=None, secret_ref=None, user_data=None, user_data_base64=None):
        """
        V1CloudInitNoCloudSource - a model defined in Swagger
        """

        self._network_data = None
        self._network_data_base64 = None
        self._network_data_secret_ref = None
        self._secret_ref = None
        self._user_data = None
        self._user_data_base64 = None

        if network_data is not None:
          self.network_data = network_data
        if network_data_base64 is not None:
          self.network_data_base64 = network_data_base64
        if network_data_secret_ref is not None:
          self.network_data_secret_ref = network_data_secret_ref
        if secret_ref is not None:
          self.secret_ref = secret_ref
        if user_data is not None:
          self.user_data = user_data
        if user_data_base64 is not None:
          self.user_data_base64 = user_data_base64

    @property
    def network_data(self):
        """
        Gets the network_data of this V1CloudInitNoCloudSource.
        NetworkData contains NoCloud inline cloud-init networkdata.

        :return: The network_data of this V1CloudInitNoCloudSource.
        :rtype: str
        """
        return self._network_data

    @network_data.setter
    def network_data(self, network_data):
        """
        Sets the network_data of this V1CloudInitNoCloudSource.
        NetworkData contains NoCloud inline cloud-init networkdata.

        :param network_data: The network_data of this V1CloudInitNoCloudSource.
        :type: str
        """

        self._network_data = network_data

    @property
    def network_data_base64(self):
        """
        Gets the network_data_base64 of this V1CloudInitNoCloudSource.
        NetworkDataBase64 contains NoCloud cloud-init networkdata as a base64 encoded string.

        :return: The network_data_base64 of this V1CloudInitNoCloudSource.
        :rtype: str
        """
        return self._network_data_base64

    @network_data_base64.setter
    def network_data_base64(self, network_data_base64):
        """
        Sets the network_data_base64 of this V1CloudInitNoCloudSource.
        NetworkDataBase64 contains NoCloud cloud-init networkdata as a base64 encoded string.

        :param network_data_base64: The network_data_base64 of this V1CloudInitNoCloudSource.
        :type: str
        """

        self._network_data_base64 = network_data_base64

    @property
    def network_data_secret_ref(self):
        """
        Gets the network_data_secret_ref of this V1CloudInitNoCloudSource.
        NetworkDataSecretRef references a k8s secret that contains NoCloud networkdata.

        :return: The network_data_secret_ref of this V1CloudInitNoCloudSource.
        :rtype: V1LocalObjectReference
        """
        return self._network_data_secret_ref

    @network_data_secret_ref.setter
    def network_data_secret_ref(self, network_data_secret_ref):
        """
        Sets the network_data_secret_ref of this V1CloudInitNoCloudSource.
        NetworkDataSecretRef references a k8s secret that contains NoCloud networkdata.

        :param network_data_secret_ref: The network_data_secret_ref of this V1CloudInitNoCloudSource.
        :type: V1LocalObjectReference
        """

        self._network_data_secret_ref = network_data_secret_ref

    @property
    def secret_ref(self):
        """
        Gets the secret_ref of this V1CloudInitNoCloudSource.
        UserDataSecretRef references a k8s secret that contains NoCloud userdata.

        :return: The secret_ref of this V1CloudInitNoCloudSource.
        :rtype: V1LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """
        Sets the secret_ref of this V1CloudInitNoCloudSource.
        UserDataSecretRef references a k8s secret that contains NoCloud userdata.

        :param secret_ref: The secret_ref of this V1CloudInitNoCloudSource.
        :type: V1LocalObjectReference
        """

        self._secret_ref = secret_ref

    @property
    def user_data(self):
        """
        Gets the user_data of this V1CloudInitNoCloudSource.
        UserData contains NoCloud inline cloud-init userdata.

        :return: The user_data of this V1CloudInitNoCloudSource.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """
        Sets the user_data of this V1CloudInitNoCloudSource.
        UserData contains NoCloud inline cloud-init userdata.

        :param user_data: The user_data of this V1CloudInitNoCloudSource.
        :type: str
        """

        self._user_data = user_data

    @property
    def user_data_base64(self):
        """
        Gets the user_data_base64 of this V1CloudInitNoCloudSource.
        UserDataBase64 contains NoCloud cloud-init userdata as a base64 encoded string.

        :return: The user_data_base64 of this V1CloudInitNoCloudSource.
        :rtype: str
        """
        return self._user_data_base64

    @user_data_base64.setter
    def user_data_base64(self, user_data_base64):
        """
        Sets the user_data_base64 of this V1CloudInitNoCloudSource.
        UserDataBase64 contains NoCloud cloud-init userdata as a base64 encoded string.

        :param user_data_base64: The user_data_base64 of this V1CloudInitNoCloudSource.
        :type: str
        """

        self._user_data_base64 = user_data_base64

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
        if not isinstance(other, V1CloudInitNoCloudSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
