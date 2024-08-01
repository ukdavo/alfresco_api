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

class PersonPagingList(object):
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
        'pagination': 'Pagination',
        'entries': 'list[PersonEntry]'
    }

    attribute_map = {
        'pagination': 'pagination',
        'entries': 'entries'
    }

    def __init__(self, pagination=None, entries=None):  # noqa: E501
        """PersonPagingList - a model defined in Swagger"""  # noqa: E501
        self._pagination = None
        self._entries = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if entries is not None:
            self.entries = entries

    @property
    def pagination(self):
        """Gets the pagination of this PersonPagingList.  # noqa: E501


        :return: The pagination of this PersonPagingList.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PersonPagingList.


        :param pagination: The pagination of this PersonPagingList.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def entries(self):
        """Gets the entries of this PersonPagingList.  # noqa: E501


        :return: The entries of this PersonPagingList.  # noqa: E501
        :rtype: list[PersonEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this PersonPagingList.


        :param entries: The entries of this PersonPagingList.  # noqa: E501
        :type: list[PersonEntry]
        """

        self._entries = entries

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
        if issubclass(PersonPagingList, dict):
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
        if not isinstance(other, PersonPagingList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
