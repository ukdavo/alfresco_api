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
from alfresco_api.api.renditions_api import RenditionsApi  # noqa: E501
from alfresco_api.rest import ApiException


class TestRenditionsApi(unittest.TestCase):
    """RenditionsApi unit test stubs"""

    def setUp(self):
        self.api = RenditionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_rendition(self):
        """Test case for create_rendition

        Create rendition  # noqa: E501
        """
        pass

    def test_get_rendition(self):
        """Test case for get_rendition

        Get rendition information  # noqa: E501
        """
        pass

    def test_get_rendition_content(self):
        """Test case for get_rendition_content

        Get rendition content  # noqa: E501
        """
        pass

    def test_list_renditions(self):
        """Test case for list_renditions

        List renditions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
