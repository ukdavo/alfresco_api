# alfresco_api.TagsApi

All URIs are relative to */alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag_for_node**](TagsApi.md#create_tag_for_node) | **POST** /nodes/{nodeId}/tags | Create a tag for a node
[**delete_tag_from_node**](TagsApi.md#delete_tag_from_node) | **DELETE** /nodes/{nodeId}/tags/{tagId} | Delete a tag from a node
[**get_tag**](TagsApi.md#get_tag) | **GET** /tags/{tagId} | Get a tag
[**list_tags**](TagsApi.md#list_tags) | **GET** /tags | List tags
[**list_tags_for_node**](TagsApi.md#list_tags_for_node) | **GET** /nodes/{nodeId}/tags | List tags for a node
[**update_tag**](TagsApi.md#update_tag) | **PUT** /tags/{tagId} | Update a tag

# **create_tag_for_node**
> TagEntry create_tag_for_node(body, node_id, fields=fields)

Create a tag for a node

Creates a tag on the node **nodeId**. You specify the tag in a JSON body like this:  ```JSON {   \"tag\":\"test-tag-1\" } ```  **Note:** You can create more than one tag by specifying a list of tags in the JSON body like this:  ```JSON [   {     \"tag\":\"test-tag-1\"   },   {     \"tag\":\"test-tag-2\"   } ] ``` If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:  ```JSON {   \"list\": {     \"pagination\": {       \"count\": 2,       \"hasMoreItems\": false,       \"totalItems\": 2,       \"skipCount\": 0,       \"maxItems\": 100     },     \"entries\": [       {         \"entry\": {           ...         }       },       {         \"entry\": {          ...         }       }     ]   } } ``` 

### Example
```python
from __future__ import print_function
import time
import alfresco_api
from alfresco_api.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_api.TagsApi(alfresco_api.ApiClient(configuration))
body = alfresco_api.TagBody() # TagBody | The new tag
node_id = 'node_id_example' # str | The identifier of a node.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Create a tag for a node
    api_response = api_instance.create_tag_for_node(body, node_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->create_tag_for_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagBody**](TagBody.md)| The new tag | 
 **node_id** | **str**| The identifier of a node. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**TagEntry**](TagEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_from_node**
> delete_tag_from_node(node_id, tag_id)

Delete a tag from a node

Deletes tag **tagId** from node **nodeId**.

### Example
```python
from __future__ import print_function
import time
import alfresco_api
from alfresco_api.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_api.TagsApi(alfresco_api.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
tag_id = 'tag_id_example' # str | The identifier of a tag.

try:
    # Delete a tag from a node
    api_instance.delete_tag_from_node(node_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->delete_tag_from_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **tag_id** | **str**| The identifier of a tag. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> TagEntry get_tag(tag_id, fields=fields)

Get a tag

Get a specific tag with **tagId**.

### Example
```python
from __future__ import print_function
import time
import alfresco_api
from alfresco_api.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_api.TagsApi(alfresco_api.ApiClient(configuration))
tag_id = 'tag_id_example' # str | The identifier of a tag.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Get a tag
    api_response = api_instance.get_tag(tag_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The identifier of a tag. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**TagEntry**](TagEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> TagPaging list_tags(skip_count=skip_count, max_items=max_items, fields=fields, include=include)

List tags

Gets a list of tags in this repository.  You can use the **include** parameter to return additional **values** information. 

### Example
```python
from __future__ import print_function
import time
import alfresco_api
from alfresco_api.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_api.TagsApi(alfresco_api.ApiClient(configuration))
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
include = ['include_example'] # list[str] | Returns additional information about the tag. The following optional fields can be requested: * count  (optional)

try:
    # List tags
    api_response = api_instance.list_tags(skip_count=skip_count, max_items=max_items, fields=fields, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->list_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **include** | [**list[str]**](str.md)| Returns additional information about the tag. The following optional fields can be requested: * count  | [optional] 

### Return type

[**TagPaging**](TagPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags_for_node**
> TagPaging list_tags_for_node(node_id, skip_count=skip_count, max_items=max_items, fields=fields)

List tags for a node

Gets a list of tags for node **nodeId**.

### Example
```python
from __future__ import print_function
import time
import alfresco_api
from alfresco_api.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_api.TagsApi(alfresco_api.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List tags for a node
    api_response = api_instance.list_tags_for_node(node_id, skip_count=skip_count, max_items=max_items, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->list_tags_for_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**TagPaging**](TagPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> TagEntry update_tag(body, tag_id, fields=fields)

Update a tag

Updates the tag **tagId**.

### Example
```python
from __future__ import print_function
import time
import alfresco_api
from alfresco_api.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_api.TagsApi(alfresco_api.ApiClient(configuration))
body = alfresco_api.TagBody() # TagBody | The updated tag
tag_id = 'tag_id_example' # str | The identifier of a tag.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Update a tag
    api_response = api_instance.update_tag(body, tag_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagBody**](TagBody.md)| The updated tag | 
 **tag_id** | **str**| The identifier of a tag. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**TagEntry**](TagEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

