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

class NodeBodyLock(object):
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
        'time_to_expire': 'int',
        'type': 'str',
        'lifetime': 'str'
    }

    attribute_map = {
        'time_to_expire': 'timeToExpire',
        'type': 'type',
        'lifetime': 'lifetime'
    }

    def __init__(self, time_to_expire=None, type='ALLOW_OWNER_CHANGES', lifetime='PERSISTENT'):  # noqa: E501
        """NodeBodyLock - a model defined in Swagger"""  # noqa: E501
        self._time_to_expire = None
        self._type = None
        self._lifetime = None
        self.discriminator = None
        if time_to_expire is not None:
            self.time_to_expire = time_to_expire
        if type is not None:
            self.type = type
        if lifetime is not None:
            self.lifetime = lifetime

    @property
    def time_to_expire(self):
        """Gets the time_to_expire of this NodeBodyLock.  # noqa: E501


        :return: The time_to_expire of this NodeBodyLock.  # noqa: E501
        :rtype: int
        """
        return self._time_to_expire

    @time_to_expire.setter
    def time_to_expire(self, time_to_expire):
        """Sets the time_to_expire of this NodeBodyLock.


        :param time_to_expire: The time_to_expire of this NodeBodyLock.  # noqa: E501
        :type: int
        """

        self._time_to_expire = time_to_expire

    @property
    def type(self):
        """Gets the type of this NodeBodyLock.  # noqa: E501


        :return: The type of this NodeBodyLock.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeBodyLock.


        :param type: The type of this NodeBodyLock.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALLOW_OWNER_CHANGES", "FULL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def lifetime(self):
        """Gets the lifetime of this NodeBodyLock.  # noqa: E501


        :return: The lifetime of this NodeBodyLock.  # noqa: E501
        :rtype: str
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """Sets the lifetime of this NodeBodyLock.


        :param lifetime: The lifetime of this NodeBodyLock.  # noqa: E501
        :type: str
        """
        allowed_values = ["PERSISTENT", "EPHEMERAL"]  # noqa: E501
        if lifetime not in allowed_values:
            raise ValueError(
                "Invalid value for `lifetime` ({0}), must be one of {1}"  # noqa: E501
                .format(lifetime, allowed_values)
            )

        self._lifetime = lifetime

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
        if issubclass(NodeBodyLock, dict):
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
        if not isinstance(other, NodeBodyLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
