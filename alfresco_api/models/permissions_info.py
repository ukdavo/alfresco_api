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

class PermissionsInfo(object):
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
        'is_inheritance_enabled': 'bool',
        'inherited': 'list[PermissionElement]',
        'locally_set': 'list[PermissionElement]',
        'settable': 'list[str]'
    }

    attribute_map = {
        'is_inheritance_enabled': 'isInheritanceEnabled',
        'inherited': 'inherited',
        'locally_set': 'locallySet',
        'settable': 'settable'
    }

    def __init__(self, is_inheritance_enabled=None, inherited=None, locally_set=None, settable=None):  # noqa: E501
        """PermissionsInfo - a model defined in Swagger"""  # noqa: E501
        self._is_inheritance_enabled = None
        self._inherited = None
        self._locally_set = None
        self._settable = None
        self.discriminator = None
        if is_inheritance_enabled is not None:
            self.is_inheritance_enabled = is_inheritance_enabled
        if inherited is not None:
            self.inherited = inherited
        if locally_set is not None:
            self.locally_set = locally_set
        if settable is not None:
            self.settable = settable

    @property
    def is_inheritance_enabled(self):
        """Gets the is_inheritance_enabled of this PermissionsInfo.  # noqa: E501


        :return: The is_inheritance_enabled of this PermissionsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_inheritance_enabled

    @is_inheritance_enabled.setter
    def is_inheritance_enabled(self, is_inheritance_enabled):
        """Sets the is_inheritance_enabled of this PermissionsInfo.


        :param is_inheritance_enabled: The is_inheritance_enabled of this PermissionsInfo.  # noqa: E501
        :type: bool
        """

        self._is_inheritance_enabled = is_inheritance_enabled

    @property
    def inherited(self):
        """Gets the inherited of this PermissionsInfo.  # noqa: E501


        :return: The inherited of this PermissionsInfo.  # noqa: E501
        :rtype: list[PermissionElement]
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this PermissionsInfo.


        :param inherited: The inherited of this PermissionsInfo.  # noqa: E501
        :type: list[PermissionElement]
        """

        self._inherited = inherited

    @property
    def locally_set(self):
        """Gets the locally_set of this PermissionsInfo.  # noqa: E501


        :return: The locally_set of this PermissionsInfo.  # noqa: E501
        :rtype: list[PermissionElement]
        """
        return self._locally_set

    @locally_set.setter
    def locally_set(self, locally_set):
        """Sets the locally_set of this PermissionsInfo.


        :param locally_set: The locally_set of this PermissionsInfo.  # noqa: E501
        :type: list[PermissionElement]
        """

        self._locally_set = locally_set

    @property
    def settable(self):
        """Gets the settable of this PermissionsInfo.  # noqa: E501


        :return: The settable of this PermissionsInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._settable

    @settable.setter
    def settable(self, settable):
        """Sets the settable of this PermissionsInfo.


        :param settable: The settable of this PermissionsInfo.  # noqa: E501
        :type: list[str]
        """

        self._settable = settable

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
        if issubclass(PermissionsInfo, dict):
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
        if not isinstance(other, PermissionsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
