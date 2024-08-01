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

class PathInfo(object):
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
        'elements': 'list[PathElement]',
        'name': 'str',
        'is_complete': 'bool'
    }

    attribute_map = {
        'elements': 'elements',
        'name': 'name',
        'is_complete': 'isComplete'
    }

    def __init__(self, elements=None, name=None, is_complete=None):  # noqa: E501
        """PathInfo - a model defined in Swagger"""  # noqa: E501
        self._elements = None
        self._name = None
        self._is_complete = None
        self.discriminator = None
        if elements is not None:
            self.elements = elements
        if name is not None:
            self.name = name
        if is_complete is not None:
            self.is_complete = is_complete

    @property
    def elements(self):
        """Gets the elements of this PathInfo.  # noqa: E501


        :return: The elements of this PathInfo.  # noqa: E501
        :rtype: list[PathElement]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this PathInfo.


        :param elements: The elements of this PathInfo.  # noqa: E501
        :type: list[PathElement]
        """

        self._elements = elements

    @property
    def name(self):
        """Gets the name of this PathInfo.  # noqa: E501


        :return: The name of this PathInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PathInfo.


        :param name: The name of this PathInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_complete(self):
        """Gets the is_complete of this PathInfo.  # noqa: E501


        :return: The is_complete of this PathInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this PathInfo.


        :param is_complete: The is_complete of this PathInfo.  # noqa: E501
        :type: bool
        """

        self._is_complete = is_complete

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
        if issubclass(PathInfo, dict):
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
        if not isinstance(other, PathInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
