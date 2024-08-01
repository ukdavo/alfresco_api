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

class ContentInfo(object):
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
        'mime_type': 'str',
        'mime_type_name': 'str',
        'size_in_bytes': 'int',
        'encoding': 'str'
    }

    attribute_map = {
        'mime_type': 'mimeType',
        'mime_type_name': 'mimeTypeName',
        'size_in_bytes': 'sizeInBytes',
        'encoding': 'encoding'
    }

    def __init__(self, mime_type=None, mime_type_name=None, size_in_bytes=None, encoding=None):  # noqa: E501
        """ContentInfo - a model defined in Swagger"""  # noqa: E501
        self._mime_type = None
        self._mime_type_name = None
        self._size_in_bytes = None
        self._encoding = None
        self.discriminator = None
        self.mime_type = mime_type
        if mime_type_name is not None:
            self.mime_type_name = mime_type_name
        if size_in_bytes is not None:
            self.size_in_bytes = size_in_bytes
        if encoding is not None:
            self.encoding = encoding

    @property
    def mime_type(self):
        """Gets the mime_type of this ContentInfo.  # noqa: E501


        :return: The mime_type of this ContentInfo.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this ContentInfo.


        :param mime_type: The mime_type of this ContentInfo.  # noqa: E501
        :type: str
        """
        if mime_type is None:
            raise ValueError("Invalid value for `mime_type`, must not be `None`")  # noqa: E501

        self._mime_type = mime_type

    @property
    def mime_type_name(self):
        """Gets the mime_type_name of this ContentInfo.  # noqa: E501


        :return: The mime_type_name of this ContentInfo.  # noqa: E501
        :rtype: str
        """
        return self._mime_type_name

    @mime_type_name.setter
    def mime_type_name(self, mime_type_name):
        """Sets the mime_type_name of this ContentInfo.


        :param mime_type_name: The mime_type_name of this ContentInfo.  # noqa: E501
        :type: str
        """

        self._mime_type_name = mime_type_name

    @property
    def size_in_bytes(self):
        """Gets the size_in_bytes of this ContentInfo.  # noqa: E501


        :return: The size_in_bytes of this ContentInfo.  # noqa: E501
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """Sets the size_in_bytes of this ContentInfo.


        :param size_in_bytes: The size_in_bytes of this ContentInfo.  # noqa: E501
        :type: int
        """

        self._size_in_bytes = size_in_bytes

    @property
    def encoding(self):
        """Gets the encoding of this ContentInfo.  # noqa: E501


        :return: The encoding of this ContentInfo.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this ContentInfo.


        :param encoding: The encoding of this ContentInfo.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

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
        if issubclass(ContentInfo, dict):
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
        if not isinstance(other, ContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other