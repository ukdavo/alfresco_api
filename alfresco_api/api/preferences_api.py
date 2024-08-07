# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services.   # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from alfresco_api.api_client import ApiClient


class PreferencesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_preference(self, person_id, preference_name, **kwargs):  # noqa: E501
        """Get a preference  # noqa: E501

        Gets a specific preference for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_preference(person_id, preference_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str person_id: The identifier of a person. (required)
        :param str preference_name: The name of the preference. (required)
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :return: PreferenceEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_preference_with_http_info(person_id, preference_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_preference_with_http_info(person_id, preference_name, **kwargs)  # noqa: E501
            return data

    def get_preference_with_http_info(self, person_id, preference_name, **kwargs):  # noqa: E501
        """Get a preference  # noqa: E501

        Gets a specific preference for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_preference_with_http_info(person_id, preference_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str person_id: The identifier of a person. (required)
        :param str preference_name: The name of the preference. (required)
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :return: PreferenceEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['person_id', 'preference_name', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_preference" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'person_id' is set
        if ('person_id' not in params or
                params['person_id'] is None):
            raise ValueError("Missing the required parameter `person_id` when calling `get_preference`")  # noqa: E501
        # verify the required parameter 'preference_name' is set
        if ('preference_name' not in params or
                params['preference_name'] is None):
            raise ValueError("Missing the required parameter `preference_name` when calling `get_preference`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'person_id' in params:
            path_params['personId'] = params['person_id']  # noqa: E501
        if 'preference_name' in params:
            path_params['preferenceName'] = params['preference_name']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/people/{personId}/preferences/{preferenceName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PreferenceEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_preferences(self, person_id, **kwargs):  # noqa: E501
        """List preferences  # noqa: E501

        Gets a list of preferences for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. Note that each preference consists of an **id** and a **value**.  The **value** can be of any JSON type.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_preferences(person_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str person_id: The identifier of a person. (required)
        :param int skip_count: The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0. 
        :param int max_items: The maximum number of items to return in the list. If not supplied then the default value is 100. 
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :return: PreferencePaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_preferences_with_http_info(person_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_preferences_with_http_info(person_id, **kwargs)  # noqa: E501
            return data

    def list_preferences_with_http_info(self, person_id, **kwargs):  # noqa: E501
        """List preferences  # noqa: E501

        Gets a list of preferences for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. Note that each preference consists of an **id** and a **value**.  The **value** can be of any JSON type.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_preferences_with_http_info(person_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str person_id: The identifier of a person. (required)
        :param int skip_count: The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0. 
        :param int max_items: The maximum number of items to return in the list. If not supplied then the default value is 100. 
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :return: PreferencePaging
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['person_id', 'skip_count', 'max_items', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_preferences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'person_id' is set
        if ('person_id' not in params or
                params['person_id'] is None):
            raise ValueError("Missing the required parameter `person_id` when calling `list_preferences`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'person_id' in params:
            path_params['personId'] = params['person_id']  # noqa: E501

        query_params = []
        if 'skip_count' in params:
            query_params.append(('skipCount', params['skip_count']))  # noqa: E501
        if 'max_items' in params:
            query_params.append(('maxItems', params['max_items']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/people/{personId}/preferences', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PreferencePaging',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
