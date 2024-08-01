# Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | 
**node_type** | **str** |  | 
**is_folder** | **bool** |  | 
**is_file** | **bool** |  | 
**is_locked** | **bool** |  | [optional] [default to False]
**modified_at** | **datetime** |  | 
**modified_by_user** | [**UserInfo**](UserInfo.md) |  | 
**created_at** | **datetime** |  | 
**created_by_user** | [**UserInfo**](UserInfo.md) |  | 
**parent_id** | **str** |  | [optional] 
**is_link** | **bool** |  | [optional] 
**is_favorite** | **bool** |  | [optional] 
**content** | [**ContentInfo**](ContentInfo.md) |  | [optional] 
**aspect_names** | **list[str]** |  | [optional] 
**properties** | **object** |  | [optional] 
**allowable_operations** | **list[str]** |  | [optional] 
**path** | [**PathInfo**](PathInfo.md) |  | [optional] 
**permissions** | [**PermissionsInfo**](PermissionsInfo.md) |  | [optional] 
**definition** | [**Definition**](Definition.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

