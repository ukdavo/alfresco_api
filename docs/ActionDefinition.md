# ActionDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the action definition — used for example when executing an action | 
**name** | **str** | name of the action definition, e.g. \&quot;move\&quot; | [optional] 
**title** | **str** | title of the action definition, e.g. \&quot;Move\&quot; | [optional] 
**description** | **str** | describes the action definition, e.g. \&quot;This will move the matched item to another space.\&quot; | [optional] 
**applicable_types** | **list[str]** | QNames of the types this action applies to | 
**track_status** | **bool** | whether the basic action definition supports action tracking or not | 
**parameter_definitions** | [**list[ActionParameterDefinition]**](ActionParameterDefinition.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

