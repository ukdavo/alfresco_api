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

class Group(object):
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
        'display_name': 'str',
        'is_root': 'bool',
        'parent_ids': 'list[str]',
        'zones': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'is_root': 'isRoot',
        'parent_ids': 'parentIds',
        'zones': 'zones'
    }

    def __init__(self, id=None, display_name=None, is_root=True, parent_ids=None, zones=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._display_name = None
        self._is_root = None
        self._parent_ids = None
        self._zones = None
        self.discriminator = None
        self.id = id
        self.display_name = display_name
        self.is_root = is_root
        if parent_ids is not None:
            self.parent_ids = parent_ids
        if zones is not None:
            self.zones = zones

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501


        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.


        :param id: The id of this Group.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this Group.  # noqa: E501


        :return: The display_name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Group.


        :param display_name: The display_name of this Group.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def is_root(self):
        """Gets the is_root of this Group.  # noqa: E501


        :return: The is_root of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._is_root

    @is_root.setter
    def is_root(self, is_root):
        """Sets the is_root of this Group.


        :param is_root: The is_root of this Group.  # noqa: E501
        :type: bool
        """
        if is_root is None:
            raise ValueError("Invalid value for `is_root`, must not be `None`")  # noqa: E501

        self._is_root = is_root

    @property
    def parent_ids(self):
        """Gets the parent_ids of this Group.  # noqa: E501


        :return: The parent_ids of this Group.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_ids

    @parent_ids.setter
    def parent_ids(self, parent_ids):
        """Sets the parent_ids of this Group.


        :param parent_ids: The parent_ids of this Group.  # noqa: E501
        :type: list[str]
        """

        self._parent_ids = parent_ids

    @property
    def zones(self):
        """Gets the zones of this Group.  # noqa: E501


        :return: The zones of this Group.  # noqa: E501
        :rtype: list[str]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this Group.


        :param zones: The zones of this Group.  # noqa: E501
        :type: list[str]
        """

        self._zones = zones

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
        if issubclass(Group, dict):
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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other