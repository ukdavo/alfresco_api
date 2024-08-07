# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services.   # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NetworkQuota(object):
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
        'id': 'str',
        'limit': 'int',
        'usage': 'int'
    }

    attribute_map = {
        'id': 'id',
        'limit': 'limit',
        'usage': 'usage'
    }

    def __init__(self, id=None, limit=None, usage=None):  # noqa: E501
        """NetworkQuota - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._limit = None
        self._usage = None
        self.discriminator = None
        self.id = id
        self.limit = limit
        self.usage = usage

    @property
    def id(self):
        """Gets the id of this NetworkQuota.  # noqa: E501


        :return: The id of this NetworkQuota.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkQuota.


        :param id: The id of this NetworkQuota.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def limit(self):
        """Gets the limit of this NetworkQuota.  # noqa: E501


        :return: The limit of this NetworkQuota.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NetworkQuota.


        :param limit: The limit of this NetworkQuota.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def usage(self):
        """Gets the usage of this NetworkQuota.  # noqa: E501


        :return: The usage of this NetworkQuota.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this NetworkQuota.


        :param usage: The usage of this NetworkQuota.  # noqa: E501
        :type: int
        """
        if usage is None:
            raise ValueError("Invalid value for `usage`, must not be `None`")  # noqa: E501

        self._usage = usage

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
        if issubclass(NetworkQuota, dict):
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
        if not isinstance(other, NetworkQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
