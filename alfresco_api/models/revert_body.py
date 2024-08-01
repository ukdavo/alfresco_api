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

class RevertBody(object):
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
        'major_version': 'bool',
        'comment': 'str'
    }

    attribute_map = {
        'major_version': 'majorVersion',
        'comment': 'comment'
    }

    def __init__(self, major_version=None, comment=None):  # noqa: E501
        """RevertBody - a model defined in Swagger"""  # noqa: E501
        self._major_version = None
        self._comment = None
        self.discriminator = None
        if major_version is not None:
            self.major_version = major_version
        if comment is not None:
            self.comment = comment

    @property
    def major_version(self):
        """Gets the major_version of this RevertBody.  # noqa: E501


        :return: The major_version of this RevertBody.  # noqa: E501
        :rtype: bool
        """
        return self._major_version

    @major_version.setter
    def major_version(self, major_version):
        """Sets the major_version of this RevertBody.


        :param major_version: The major_version of this RevertBody.  # noqa: E501
        :type: bool
        """

        self._major_version = major_version

    @property
    def comment(self):
        """Gets the comment of this RevertBody.  # noqa: E501


        :return: The comment of this RevertBody.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this RevertBody.


        :param comment: The comment of this RevertBody.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(RevertBody, dict):
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
        if not isinstance(other, RevertBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
