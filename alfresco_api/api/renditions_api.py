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


class RenditionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_rendition(self, body, node_id, **kwargs):  # noqa: E501
        """Create rendition  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  An asynchronous request to create a rendition for file **nodeId**.  The rendition is specified by name **id** in the request body: ```JSON {   \"id\":\"doclib\" } ```  Multiple names may be specified as a comma separated list or using a list format: ```JSON [   {      \"id\": \"doclib\"   },   {      \"id\": \"avatar\"   } ] ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_rendition(body, node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RenditionBodyCreate body: The rendition "id". (required)
        :param str node_id: The identifier of a node. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_rendition_with_http_info(body, node_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_rendition_with_http_info(body, node_id, **kwargs)  # noqa: E501
            return data

    def create_rendition_with_http_info(self, body, node_id, **kwargs):  # noqa: E501
        """Create rendition  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  An asynchronous request to create a rendition for file **nodeId**.  The rendition is specified by name **id** in the request body: ```JSON {   \"id\":\"doclib\" } ```  Multiple names may be specified as a comma separated list or using a list format: ```JSON [   {      \"id\": \"doclib\"   },   {      \"id\": \"avatar\"   } ] ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_rendition_with_http_info(body, node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RenditionBodyCreate body: The rendition "id". (required)
        :param str node_id: The identifier of a node. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'node_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_rendition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_rendition`")  # noqa: E501
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params or
                params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `create_rendition`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_id' in params:
            path_params['nodeId'] = params['node_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/nodes/{nodeId}/renditions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_rendition(self, node_id, rendition_id, **kwargs):  # noqa: E501
        """Get rendition information  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the rendition information for **renditionId** of file **nodeId**.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rendition(node_id, rendition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: The identifier of a node. (required)
        :param str rendition_id: The name of a thumbnail rendition, for example *doclib*, or *pdf*. (required)
        :return: RenditionEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rendition_with_http_info(node_id, rendition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rendition_with_http_info(node_id, rendition_id, **kwargs)  # noqa: E501
            return data

    def get_rendition_with_http_info(self, node_id, rendition_id, **kwargs):  # noqa: E501
        """Get rendition information  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the rendition information for **renditionId** of file **nodeId**.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rendition_with_http_info(node_id, rendition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: The identifier of a node. (required)
        :param str rendition_id: The name of a thumbnail rendition, for example *doclib*, or *pdf*. (required)
        :return: RenditionEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_id', 'rendition_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rendition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params or
                params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `get_rendition`")  # noqa: E501
        # verify the required parameter 'rendition_id' is set
        if ('rendition_id' not in params or
                params['rendition_id'] is None):
            raise ValueError("Missing the required parameter `rendition_id` when calling `get_rendition`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_id' in params:
            path_params['nodeId'] = params['node_id']  # noqa: E501
        if 'rendition_id' in params:
            path_params['renditionId'] = params['rendition_id']  # noqa: E501

        query_params = []

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
            '/nodes/{nodeId}/renditions/{renditionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RenditionEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_rendition_content(self, node_id, rendition_id, **kwargs):  # noqa: E501
        """Get rendition content  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the rendition content for **renditionId** of file **nodeId**.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rendition_content(node_id, rendition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: The identifier of a node. (required)
        :param str rendition_id: The name of a thumbnail rendition, for example *doclib*, or *pdf*. (required)
        :param bool attachment: **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response. 
        :param datetime if_modified_since: Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`. 
        :param str range: The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10. 
        :param bool placeholder: If **true** and there is no rendition for this **nodeId** and **renditionId**, then the placeholder image for the mime type of this rendition is returned, rather than a 404 response. 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rendition_content_with_http_info(node_id, rendition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rendition_content_with_http_info(node_id, rendition_id, **kwargs)  # noqa: E501
            return data

    def get_rendition_content_with_http_info(self, node_id, rendition_id, **kwargs):  # noqa: E501
        """Get rendition content  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the rendition content for **renditionId** of file **nodeId**.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rendition_content_with_http_info(node_id, rendition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: The identifier of a node. (required)
        :param str rendition_id: The name of a thumbnail rendition, for example *doclib*, or *pdf*. (required)
        :param bool attachment: **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response. 
        :param datetime if_modified_since: Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`. 
        :param str range: The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10. 
        :param bool placeholder: If **true** and there is no rendition for this **nodeId** and **renditionId**, then the placeholder image for the mime type of this rendition is returned, rather than a 404 response. 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_id', 'rendition_id', 'attachment', 'if_modified_since', 'range', 'placeholder']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rendition_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params or
                params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `get_rendition_content`")  # noqa: E501
        # verify the required parameter 'rendition_id' is set
        if ('rendition_id' not in params or
                params['rendition_id'] is None):
            raise ValueError("Missing the required parameter `rendition_id` when calling `get_rendition_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_id' in params:
            path_params['nodeId'] = params['node_id']  # noqa: E501
        if 'rendition_id' in params:
            path_params['renditionId'] = params['rendition_id']  # noqa: E501

        query_params = []
        if 'attachment' in params:
            query_params.append(('attachment', params['attachment']))  # noqa: E501
        if 'placeholder' in params:
            query_params.append(('placeholder', params['placeholder']))  # noqa: E501

        header_params = {}
        if 'if_modified_since' in params:
            header_params['If-Modified-Since'] = params['if_modified_since']  # noqa: E501
        if 'range' in params:
            header_params['Range'] = params['range']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/nodes/{nodeId}/renditions/{renditionId}/content', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_renditions(self, node_id, **kwargs):  # noqa: E501
        """List renditions  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets a list of the rendition information for each rendition of the the file **nodeId**, including the rendition id.  Each rendition returned has a **status**: CREATED means it is available to view or download, NOT_CREATED means the rendition can be requested.  You can use the **where** parameter to filter the returned renditions by **status**. For example, the following **where** clause will return just the CREATED renditions:  ``` (status='CREATED') ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_renditions(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: The identifier of a node. (required)
        :param str where: A string to restrict the returned objects by using a predicate.
        :return: RenditionPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_renditions_with_http_info(node_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_renditions_with_http_info(node_id, **kwargs)  # noqa: E501
            return data

    def list_renditions_with_http_info(self, node_id, **kwargs):  # noqa: E501
        """List renditions  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets a list of the rendition information for each rendition of the the file **nodeId**, including the rendition id.  Each rendition returned has a **status**: CREATED means it is available to view or download, NOT_CREATED means the rendition can be requested.  You can use the **where** parameter to filter the returned renditions by **status**. For example, the following **where** clause will return just the CREATED renditions:  ``` (status='CREATED') ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_renditions_with_http_info(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: The identifier of a node. (required)
        :param str where: A string to restrict the returned objects by using a predicate.
        :return: RenditionPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_id', 'where']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_renditions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params or
                params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `list_renditions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_id' in params:
            path_params['nodeId'] = params['node_id']  # noqa: E501

        query_params = []
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501

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
            '/nodes/{nodeId}/renditions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RenditionPaging',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
