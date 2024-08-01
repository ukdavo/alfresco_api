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
from alfresco_api.api.activities_api import ActivitiesApi  # noqa: E501
from alfresco_api.rest import ApiException


class TestActivitiesApi(unittest.TestCase):
    """ActivitiesApi unit test stubs"""

    def setUp(self):
        self.api = ActivitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_activities_for_person(self):
        """Test case for list_activities_for_person

        List activities  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()