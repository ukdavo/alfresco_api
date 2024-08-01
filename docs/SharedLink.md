# SharedLink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**node_id** | **str** |  | [optional] 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**modified_at** | **datetime** |  | [optional] 
**modified_by_user** | [**UserInfo**](UserInfo.md) |  | [optional] 
**shared_by_user** | [**UserInfo**](UserInfo.md) |  | [optional] 
**content** | [**ContentInfo**](ContentInfo.md) |  | [optional] 
**allowable_operations** | **list[str]** | The allowable operations for the Quickshare link itself. See allowableOperationsOnTarget for the allowable operations pertaining to the linked content node.  | [optional] 
**allowable_operations_on_target** | **list[str]** | The allowable operations for the content node being shared.  | [optional] 
**is_favorite** | **bool** |  | [optional] 
**properties** | **object** | A subset of the target node&#x27;s properties, system properties and properties already available in the SharedLink are excluded.  | [optional] 
**aspect_names** | **list[str]** |  | [optional] 
**path** | [**PathInfo**](PathInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

