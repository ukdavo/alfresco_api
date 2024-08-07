# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services.   # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import alfresco_api
from alfresco_api.api.groups_api import GroupsApi  # noqa: E501
from alfresco_api.rest import ApiException


class TestGroupsApi(unittest.TestCase):
    """GroupsApi unit test stubs"""

    def setUp(self):
        self.api = GroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_group(self):
        """Test case for create_group

        Create a group  # noqa: E501
        """
        pass

    def test_create_group_membership(self):
        """Test case for create_group_membership

        Create a group membership  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Delete a group  # noqa: E501
        """
        pass

    def test_delete_group_membership(self):
        """Test case for delete_group_membership

        Delete a group membership  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        Get group details  # noqa: E501
        """
        pass

    def test_list_group_memberships(self):
        """Test case for list_group_memberships

        List memberships of a group  # noqa: E501
        """
        pass

    def test_list_group_memberships_for_person(self):
        """Test case for list_group_memberships_for_person

        List group memberships  # noqa: E501
        """
        pass

    def test_list_groups(self):
        """Test case for list_groups

        List groups  # noqa: E501
        """
        pass

    def test_update_group(self):
        """Test case for update_group

        Update group details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
