# alfresco_api.VersionsApi

All URIs are relative to */alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_version_rendition**](VersionsApi.md#create_version_rendition) | **POST** /nodes/{nodeId}/versions/{versionId}/renditions | Create rendition for a file version
[**delete_version**](VersionsApi.md#delete_version) | **DELETE** /nodes/{nodeId}/versions/{versionId} | Delete a version
[**get_version**](VersionsApi.md#get_version) | **GET** /nodes/{nodeId}/versions/{versionId} | Get version information
[**get_version_content**](VersionsApi.md#get_version_content) | **GET** /nodes/{nodeId}/versions/{versionId}/content | Get version content
[**get_version_rendition**](VersionsApi.md#get_version_rendition) | **GET** /nodes/{nodeId}/versions/{versionId}/renditions/{renditionId} | Get rendition information for a file version
[**get_version_rendition_content**](VersionsApi.md#get_version_rendition_content) | **GET** /nodes/{nodeId}/versions/{versionId}/renditions/{renditionId}/content | Get rendition content for a file version
[**list_version_history**](VersionsApi.md#list_version_history) | **GET** /nodes/{nodeId}/versions | List version history
[**list_version_renditions**](VersionsApi.md#list_version_renditions) | **GET** /nodes/{nodeId}/versions/{versionId}/renditions | List renditions for a file version
[**revert_version**](VersionsApi.md#revert_version) | **POST** /nodes/{nodeId}/versions/{versionId}/revert | Revert a version

# **create_version_rendition**
> create_version_rendition(body, node_id, version_id)

Create rendition for a file version

**Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.  An asynchronous request to create a rendition for version of file **nodeId** and **versionId**.  The version rendition is specified by name **id** in the request body: ```JSON {   \"id\":\"doclib\" } ```   Multiple names may be specified as a comma separated list or using a list format: ```JSON [   {       \"id\": \"doclib\"   },   {       \"id\": \"avatar\"   } ] ``` 

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
api_instance = alfresco_api.VersionsApi(alfresco_api.ApiClient(configuration))
body = alfresco_api.RenditionBodyCreate() # RenditionBodyCreate | The rendition "id".
node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.

try:
    # Create rendition for a file version
    api_instance.create_version_rendition(body, node_id, version_id)
except ApiException as e:
    print("Exception when calling VersionsApi->create_version_rendition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RenditionBodyCreate**](RenditionBodyCreate.md)| The rendition &quot;id&quot;. | 
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> delete_version(node_id, version_id)

Delete a version

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Delete the version identified by **versionId** and **nodeId*.  If the version is successfully deleted then the content and metadata for that versioned node will be deleted and will no longer appear in the version history. This operation cannot be undone.  If the most recent version is deleted the live node will revert to the next most recent version.  We currently do not allow the last version to be deleted. If you wish to clear the history then you can remove the \"cm:versionable\" aspect (via update node) which will also disable versioning. In this case, you can re-enable versioning by adding back the \"cm:versionable\" aspect or using the version params (majorVersion and comment) on a subsequent file content update. 

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
api_instance = alfresco_api.VersionsApi(alfresco_api.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.

try:
    # Delete a version
    api_instance.delete_version(node_id, version_id)
except ApiException as e:
    print("Exception when calling VersionsApi->delete_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> VersionEntry get_version(node_id, version_id)

Get version information

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the version information for **versionId** of file node **nodeId**. 

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
api_instance = alfresco_api.VersionsApi(alfresco_api.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.

try:
    # Get version information
    api_response = api_instance.get_version(node_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 

### Return type

[**VersionEntry**](VersionEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_content**
> str get_version_content(node_id, version_id, attachment=attachment, if_modified_since=if_modified_since, range=range)

Get version content

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the version content for **versionId** of file node **nodeId**. 

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
api_instance = alfresco_api.VersionsApi(alfresco_api.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
attachment = true # bool | **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  (optional) (default to true)
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`.  (optional)
range = 'range_example' # str | The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10.  (optional)

try:
    # Get version content
    api_response = api_instance.get_version_content(node_id, version_id, attachment=attachment, if_modified_since=if_modified_since, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get_version_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **attachment** | **bool**| **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  | [optional] [default to true]
 **if_modified_since** | **datetime**| Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, &#x60;Wed, 09 Mar 2016 16:56:34 GMT&#x60;.  | [optional] 
 **range** | **str**| The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes&#x3D;1-10.  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_rendition**
> RenditionEntry get_version_rendition(node_id, version_id, rendition_id)

Get rendition information for a file version

**Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.  Gets the rendition information for **renditionId** of version of file **nodeId** and **versionId**. 

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
api_instance = alfresco_api.VersionsApi(alfresco_api.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
rendition_id = 'rendition_id_example' # str | The name of a thumbnail rendition, for example *doclib*, or *pdf*.

try:
    # Get rendition information for a file version
    api_response = api_instance.get_version_rendition(node_id, version_id, rendition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get_version_rendition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **rendition_id** | **str**| The name of a thumbnail rendition, for example *doclib*, or *pdf*. | 

### Return type

[**RenditionEntry**](RenditionEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_rendition_content**
> str get_version_rendition_content(node_id, version_id, rendition_id, attachment=attachment, if_modified_since=if_modified_since, range=range, placeholder=placeholder)

Get rendition content for a file version

**Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.  Gets the rendition content for **renditionId** of version of file **nodeId** and **versionId**. 

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
api_instance = alfresco_api.VersionsApi(alfresco_api.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
rendition_id = 'rendition_id_example' # str | The name of a thumbnail rendition, for example *doclib*, or *pdf*.
attachment = true # bool | **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  (optional) (default to true)
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`.  (optional)
range = 'range_example' # str | The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10.  (optional)
placeholder = false # bool | If **true** and there is no rendition for this **nodeId** and **renditionId**, then the placeholder image for the mime type of this rendition is returned, rather than a 404 response.  (optional) (default to false)

try:
    # Get rendition content for a file version
    api_response = api_instance.get_version_rendition_content(node_id, version_id, rendition_id, attachment=attachment, if_modified_since=if_modified_since, range=range, placeholder=placeholder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get_version_rendition_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **rendition_id** | **str**| The name of a thumbnail rendition, for example *doclib*, or *pdf*. | 
 **attachment** | **bool**| **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  | [optional] [default to true]
 **if_modified_since** | **datetime**| Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, &#x60;Wed, 09 Mar 2016 16:56:34 GMT&#x60;.  | [optional] 
 **range** | **str**| The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes&#x3D;1-10.  | [optional] 
 **placeholder** | **bool**| If **true** and there is no rendition for this **nodeId** and **renditionId**, then the placeholder image for the mime type of this rendition is returned, rather than a 404 response.  | [optional] [default to false]

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_version_history**
> VersionPaging list_version_history(node_id, include=include, fields=fields, skip_count=skip_count, max_items=max_items)

List version history

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the version history as an ordered list of versions for the specified **nodeId**.  The list is ordered in descending modified order. So the most recent version is first and the original version is last in the list. 

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
api_instance = alfresco_api.VersionsApi(alfresco_api.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
include = ['include_example'] # list[str] | Returns additional information about the version node. The following optional fields can be requested: * properties * aspectNames  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)

try:
    # List version history
    api_response = api_instance.list_version_history(node_id, include=include, fields=fields, skip_count=skip_count, max_items=max_items)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->list_version_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **include** | [**list[str]**](str.md)| Returns additional information about the version node. The following optional fields can be requested: * properties * aspectNames  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]

### Return type

[**VersionPaging**](VersionPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_version_renditions**
> RenditionPaging list_version_renditions(node_id, version_id, where=where)

List renditions for a file version

**Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.  Gets a list of the rendition information for each rendition of the version of file **nodeId** and **versionId**, including the rendition id.  Each rendition returned has a **status**: CREATED means it is available to view or download, NOT_CREATED means the rendition can be requested.  You can use the **where** parameter to filter the returned renditions by **status**. For example, the following **where** clause will return just the CREATED renditions:  ``` (status='CREATED') ``` 

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
api_instance = alfresco_api.VersionsApi(alfresco_api.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)

try:
    # List renditions for a file version
    api_response = api_instance.list_version_renditions(node_id, version_id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->list_version_renditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 

### Return type

[**RenditionPaging**](RenditionPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_version**
> VersionEntry revert_version(body, node_id, version_id, fields=fields)

Revert a version

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Attempts to revert the version identified by **versionId** and **nodeId** to the live node.  If the node is successfully reverted then the content and metadata for that versioned node will be promoted to the live node and a new version will appear in the version history. 

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
api_instance = alfresco_api.VersionsApi(alfresco_api.ApiClient(configuration))
body = alfresco_api.RevertBody() # RevertBody | Optionally, specify a version comment and whether this should be a major version, or not.
node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Revert a version
    api_response = api_instance.revert_version(body, node_id, version_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->revert_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevertBody**](RevertBody.md)| Optionally, specify a version comment and whether this should be a major version, or not. | 
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**VersionEntry**](VersionEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

