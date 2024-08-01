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

class SiteMembershipRequestBodyCreate(object):
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
        'message': 'str',
        'id': 'str',
        'title': 'str',
        'client': 'str'
    }

    attribute_map = {
        'message': 'message',
        'id': 'id',
        'title': 'title',
        'client': 'client'
    }

    def __init__(self, message=None, id=None, title=None, client=None):  # noqa: E501
        """SiteMembershipRequestBodyCreate - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._id = None
        self._title = None
        self._client = None
        self.discriminator = None
        if message is not None:
            self.message = message
        self.id = id
        if title is not None:
            self.title = title
        if client is not None:
            self.client = client

    @property
    def message(self):
        """Gets the message of this SiteMembershipRequestBodyCreate.  # noqa: E501


        :return: The message of this SiteMembershipRequestBodyCreate.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SiteMembershipRequestBodyCreate.


        :param message: The message of this SiteMembershipRequestBodyCreate.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def id(self):
        """Gets the id of this SiteMembershipRequestBodyCreate.  # noqa: E501


        :return: The id of this SiteMembershipRequestBodyCreate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SiteMembershipRequestBodyCreate.


        :param id: The id of this SiteMembershipRequestBodyCreate.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this SiteMembershipRequestBodyCreate.  # noqa: E501


        :return: The title of this SiteMembershipRequestBodyCreate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SiteMembershipRequestBodyCreate.


        :param title: The title of this SiteMembershipRequestBodyCreate.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def client(self):
        """Gets the client of this SiteMembershipRequestBodyCreate.  # noqa: E501

        Optional client name used when sending an email to the end user, defaults to \"share\" if not provided. **Note:** The client must be registered before this API can send an email. **Note:** This is available in Alfresco 7.0.0 and newer versions.   # noqa: E501

        :return: The client of this SiteMembershipRequestBodyCreate.  # noqa: E501
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this SiteMembershipRequestBodyCreate.

        Optional client name used when sending an email to the end user, defaults to \"share\" if not provided. **Note:** The client must be registered before this API can send an email. **Note:** This is available in Alfresco 7.0.0 and newer versions.   # noqa: E501

        :param client: The client of this SiteMembershipRequestBodyCreate.  # noqa: E501
        :type: str
        """

        self._client = client

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
        if issubclass(SiteMembershipRequestBodyCreate, dict):
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
        if not isinstance(other, SiteMembershipRequestBodyCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
