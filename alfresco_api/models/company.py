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

class Company(object):
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
        'organization': 'str',
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'postcode': 'str',
        'telephone': 'str',
        'fax': 'str',
        'email': 'str'
    }

    attribute_map = {
        'organization': 'organization',
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'postcode': 'postcode',
        'telephone': 'telephone',
        'fax': 'fax',
        'email': 'email'
    }

    def __init__(self, organization=None, address1=None, address2=None, address3=None, postcode=None, telephone=None, fax=None, email=None):  # noqa: E501
        """Company - a model defined in Swagger"""  # noqa: E501
        self._organization = None
        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._postcode = None
        self._telephone = None
        self._fax = None
        self._email = None
        self.discriminator = None
        if organization is not None:
            self.organization = organization
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if address3 is not None:
            self.address3 = address3
        if postcode is not None:
            self.postcode = postcode
        if telephone is not None:
            self.telephone = telephone
        if fax is not None:
            self.fax = fax
        if email is not None:
            self.email = email

    @property
    def organization(self):
        """Gets the organization of this Company.  # noqa: E501


        :return: The organization of this Company.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Company.


        :param organization: The organization of this Company.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def address1(self):
        """Gets the address1 of this Company.  # noqa: E501


        :return: The address1 of this Company.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Company.


        :param address1: The address1 of this Company.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Company.  # noqa: E501


        :return: The address2 of this Company.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Company.


        :param address2: The address2 of this Company.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def address3(self):
        """Gets the address3 of this Company.  # noqa: E501


        :return: The address3 of this Company.  # noqa: E501
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this Company.


        :param address3: The address3 of this Company.  # noqa: E501
        :type: str
        """

        self._address3 = address3

    @property
    def postcode(self):
        """Gets the postcode of this Company.  # noqa: E501


        :return: The postcode of this Company.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this Company.


        :param postcode: The postcode of this Company.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def telephone(self):
        """Gets the telephone of this Company.  # noqa: E501


        :return: The telephone of this Company.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this Company.


        :param telephone: The telephone of this Company.  # noqa: E501
        :type: str
        """

        self._telephone = telephone

    @property
    def fax(self):
        """Gets the fax of this Company.  # noqa: E501


        :return: The fax of this Company.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this Company.


        :param fax: The fax of this Company.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def email(self):
        """Gets the email of this Company.  # noqa: E501


        :return: The email of this Company.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Company.


        :param email: The email of this Company.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(Company, dict):
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
        if not isinstance(other, Company):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
