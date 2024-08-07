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

class Version(object):
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
        'version_comment': 'str',
        'name': 'str',
        'node_type': 'str',
        'is_folder': 'bool',
        'is_file': 'bool',
        'modified_at': 'datetime',
        'modified_by_user': 'UserInfo',
        'content': 'ContentInfo',
        'aspect_names': 'list[str]',
        'properties': 'object'
    }

    attribute_map = {
        'id': 'id',
        'version_comment': 'versionComment',
        'name': 'name',
        'node_type': 'nodeType',
        'is_folder': 'isFolder',
        'is_file': 'isFile',
        'modified_at': 'modifiedAt',
        'modified_by_user': 'modifiedByUser',
        'content': 'content',
        'aspect_names': 'aspectNames',
        'properties': 'properties'
    }

    def __init__(self, id=None, version_comment=None, name=None, node_type=None, is_folder=None, is_file=None, modified_at=None, modified_by_user=None, content=None, aspect_names=None, properties=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version_comment = None
        self._name = None
        self._node_type = None
        self._is_folder = None
        self._is_file = None
        self._modified_at = None
        self._modified_by_user = None
        self._content = None
        self._aspect_names = None
        self._properties = None
        self.discriminator = None
        self.id = id
        if version_comment is not None:
            self.version_comment = version_comment
        self.name = name
        self.node_type = node_type
        self.is_folder = is_folder
        self.is_file = is_file
        self.modified_at = modified_at
        self.modified_by_user = modified_by_user
        if content is not None:
            self.content = content
        if aspect_names is not None:
            self.aspect_names = aspect_names
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Gets the id of this Version.  # noqa: E501


        :return: The id of this Version.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Version.


        :param id: The id of this Version.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def version_comment(self):
        """Gets the version_comment of this Version.  # noqa: E501


        :return: The version_comment of this Version.  # noqa: E501
        :rtype: str
        """
        return self._version_comment

    @version_comment.setter
    def version_comment(self, version_comment):
        """Sets the version_comment of this Version.


        :param version_comment: The version_comment of this Version.  # noqa: E501
        :type: str
        """

        self._version_comment = version_comment

    @property
    def name(self):
        """Gets the name of this Version.  # noqa: E501

        The name must not contain spaces or the following special characters: * \" < > \\ / ? : and |. The character . must not be used at the end of the name.   # noqa: E501

        :return: The name of this Version.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Version.

        The name must not contain spaces or the following special characters: * \" < > \\ / ? : and |. The character . must not be used at the end of the name.   # noqa: E501

        :param name: The name of this Version.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def node_type(self):
        """Gets the node_type of this Version.  # noqa: E501


        :return: The node_type of this Version.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Version.


        :param node_type: The node_type of this Version.  # noqa: E501
        :type: str
        """
        if node_type is None:
            raise ValueError("Invalid value for `node_type`, must not be `None`")  # noqa: E501

        self._node_type = node_type

    @property
    def is_folder(self):
        """Gets the is_folder of this Version.  # noqa: E501


        :return: The is_folder of this Version.  # noqa: E501
        :rtype: bool
        """
        return self._is_folder

    @is_folder.setter
    def is_folder(self, is_folder):
        """Sets the is_folder of this Version.


        :param is_folder: The is_folder of this Version.  # noqa: E501
        :type: bool
        """
        if is_folder is None:
            raise ValueError("Invalid value for `is_folder`, must not be `None`")  # noqa: E501

        self._is_folder = is_folder

    @property
    def is_file(self):
        """Gets the is_file of this Version.  # noqa: E501


        :return: The is_file of this Version.  # noqa: E501
        :rtype: bool
        """
        return self._is_file

    @is_file.setter
    def is_file(self, is_file):
        """Sets the is_file of this Version.


        :param is_file: The is_file of this Version.  # noqa: E501
        :type: bool
        """
        if is_file is None:
            raise ValueError("Invalid value for `is_file`, must not be `None`")  # noqa: E501

        self._is_file = is_file

    @property
    def modified_at(self):
        """Gets the modified_at of this Version.  # noqa: E501


        :return: The modified_at of this Version.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Version.


        :param modified_at: The modified_at of this Version.  # noqa: E501
        :type: datetime
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def modified_by_user(self):
        """Gets the modified_by_user of this Version.  # noqa: E501


        :return: The modified_by_user of this Version.  # noqa: E501
        :rtype: UserInfo
        """
        return self._modified_by_user

    @modified_by_user.setter
    def modified_by_user(self, modified_by_user):
        """Sets the modified_by_user of this Version.


        :param modified_by_user: The modified_by_user of this Version.  # noqa: E501
        :type: UserInfo
        """
        if modified_by_user is None:
            raise ValueError("Invalid value for `modified_by_user`, must not be `None`")  # noqa: E501

        self._modified_by_user = modified_by_user

    @property
    def content(self):
        """Gets the content of this Version.  # noqa: E501


        :return: The content of this Version.  # noqa: E501
        :rtype: ContentInfo
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Version.


        :param content: The content of this Version.  # noqa: E501
        :type: ContentInfo
        """

        self._content = content

    @property
    def aspect_names(self):
        """Gets the aspect_names of this Version.  # noqa: E501


        :return: The aspect_names of this Version.  # noqa: E501
        :rtype: list[str]
        """
        return self._aspect_names

    @aspect_names.setter
    def aspect_names(self, aspect_names):
        """Sets the aspect_names of this Version.


        :param aspect_names: The aspect_names of this Version.  # noqa: E501
        :type: list[str]
        """

        self._aspect_names = aspect_names

    @property
    def properties(self):
        """Gets the properties of this Version.  # noqa: E501


        :return: The properties of this Version.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Version.


        :param properties: The properties of this Version.  # noqa: E501
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
        if issubclass(Version, dict):
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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
