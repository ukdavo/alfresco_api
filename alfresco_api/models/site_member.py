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

class SiteMember(object):
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
        'person': 'Person',
        'role': 'str',
        'is_member_of_group': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'person': 'person',
        'role': 'role',
        'is_member_of_group': 'isMemberOfGroup'
    }

    def __init__(self, id=None, person=None, role=None, is_member_of_group=None):  # noqa: E501
        """SiteMember - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._person = None
        self._role = None
        self._is_member_of_group = None
        self.discriminator = None
        self.id = id
        self.person = person
        self.role = role
        if is_member_of_group is not None:
            self.is_member_of_group = is_member_of_group

    @property
    def id(self):
        """Gets the id of this SiteMember.  # noqa: E501


        :return: The id of this SiteMember.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SiteMember.


        :param id: The id of this SiteMember.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def person(self):
        """Gets the person of this SiteMember.  # noqa: E501


        :return: The person of this SiteMember.  # noqa: E501
        :rtype: Person
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this SiteMember.


        :param person: The person of this SiteMember.  # noqa: E501
        :type: Person
        """
        if person is None:
            raise ValueError("Invalid value for `person`, must not be `None`")  # noqa: E501

        self._person = person

    @property
    def role(self):
        """Gets the role of this SiteMember.  # noqa: E501


        :return: The role of this SiteMember.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this SiteMember.


        :param role: The role of this SiteMember.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["SiteConsumer", "SiteCollaborator", "SiteContributor", "SiteManager"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def is_member_of_group(self):
        """Gets the is_member_of_group of this SiteMember.  # noqa: E501


        :return: The is_member_of_group of this SiteMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_member_of_group

    @is_member_of_group.setter
    def is_member_of_group(self, is_member_of_group):
        """Sets the is_member_of_group of this SiteMember.


        :param is_member_of_group: The is_member_of_group of this SiteMember.  # noqa: E501
        :type: bool
        """

        self._is_member_of_group = is_member_of_group

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
        if issubclass(SiteMember, dict):
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
        if not isinstance(other, SiteMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other