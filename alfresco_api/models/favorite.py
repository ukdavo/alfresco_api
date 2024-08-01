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

class Favorite(object):
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
        'target_guid': 'str',
        'created_at': 'datetime',
        'target': 'object',
        'properties': 'object'
    }

    attribute_map = {
        'target_guid': 'targetGuid',
        'created_at': 'createdAt',
        'target': 'target',
        'properties': 'properties'
    }

    def __init__(self, target_guid=None, created_at=None, target=None, properties=None):  # noqa: E501
        """Favorite - a model defined in Swagger"""  # noqa: E501
        self._target_guid = None
        self._created_at = None
        self._target = None
        self._properties = None
        self.discriminator = None
        self.target_guid = target_guid
        if created_at is not None:
            self.created_at = created_at
        self.target = target
        if properties is not None:
            self.properties = properties

    @property
    def target_guid(self):
        """Gets the target_guid of this Favorite.  # noqa: E501

        The guid of the object that is a favorite.  # noqa: E501

        :return: The target_guid of this Favorite.  # noqa: E501
        :rtype: str
        """
        return self._target_guid

    @target_guid.setter
    def target_guid(self, target_guid):
        """Sets the target_guid of this Favorite.

        The guid of the object that is a favorite.  # noqa: E501

        :param target_guid: The target_guid of this Favorite.  # noqa: E501
        :type: str
        """
        if target_guid is None:
            raise ValueError("Invalid value for `target_guid`, must not be `None`")  # noqa: E501

        self._target_guid = target_guid

    @property
    def created_at(self):
        """Gets the created_at of this Favorite.  # noqa: E501

        The time the object was made a favorite.  # noqa: E501

        :return: The created_at of this Favorite.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Favorite.

        The time the object was made a favorite.  # noqa: E501

        :param created_at: The created_at of this Favorite.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def target(self):
        """Gets the target of this Favorite.  # noqa: E501


        :return: The target of this Favorite.  # noqa: E501
        :rtype: object
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Favorite.


        :param target: The target of this Favorite.  # noqa: E501
        :type: object
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    @property
    def properties(self):
        """Gets the properties of this Favorite.  # noqa: E501

        A subset of the target favorite properties, system properties and properties already available in the target are excluded.  # noqa: E501

        :return: The properties of this Favorite.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Favorite.

        A subset of the target favorite properties, system properties and properties already available in the target are excluded.  # noqa: E501

        :param properties: The properties of this Favorite.  # noqa: E501
        :type: object
        """

        self._properties = properties

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
        if issubclass(Favorite, dict):
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
        if not isinstance(other, Favorite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other