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

class DeletedNodeBodyRestore(object):
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
        'target_parent_id': 'str',
        'assoc_type': 'str'
    }

    attribute_map = {
        'target_parent_id': 'targetParentId',
        'assoc_type': 'assocType'
    }

    def __init__(self, target_parent_id=None, assoc_type=None):  # noqa: E501
        """DeletedNodeBodyRestore - a model defined in Swagger"""  # noqa: E501
        self._target_parent_id = None
        self._assoc_type = None
        self.discriminator = None
        if target_parent_id is not None:
            self.target_parent_id = target_parent_id
        if assoc_type is not None:
            self.assoc_type = assoc_type

    @property
    def target_parent_id(self):
        """Gets the target_parent_id of this DeletedNodeBodyRestore.  # noqa: E501


        :return: The target_parent_id of this DeletedNodeBodyRestore.  # noqa: E501
        :rtype: str
        """
        return self._target_parent_id

    @target_parent_id.setter
    def target_parent_id(self, target_parent_id):
        """Sets the target_parent_id of this DeletedNodeBodyRestore.


        :param target_parent_id: The target_parent_id of this DeletedNodeBodyRestore.  # noqa: E501
        :type: str
        """

        self._target_parent_id = target_parent_id

    @property
    def assoc_type(self):
        """Gets the assoc_type of this DeletedNodeBodyRestore.  # noqa: E501


        :return: The assoc_type of this DeletedNodeBodyRestore.  # noqa: E501
        :rtype: str
        """
        return self._assoc_type

    @assoc_type.setter
    def assoc_type(self, assoc_type):
        """Sets the assoc_type of this DeletedNodeBodyRestore.


        :param assoc_type: The assoc_type of this DeletedNodeBodyRestore.  # noqa: E501
        :type: str
        """

        self._assoc_type = assoc_type

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
        if issubclass(DeletedNodeBodyRestore, dict):
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
        if not isinstance(other, DeletedNodeBodyRestore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
