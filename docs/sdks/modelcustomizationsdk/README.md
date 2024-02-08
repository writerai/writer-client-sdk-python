# ModelCustomizationSDK
(*model_customization*)

## Overview

Methods related to Model Customization

### Available Operations

* [create](#create) - Create model customization
* [delete](#delete) - Delete Model customization
* [get](#get) - Get model customization
* [list](#list) - List model customizations

## create

Create model customization

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=486589,
)


res = s.model_customization.create(create_customization_request=writer.CreateCustomizationRequest(
    name='string',
    training_dataset_file_id='string',
    additional_hyper_parameters=writer.HyperParameters(
        num_virtual_tokens=489382,
    ),
), model_id='string', organization_id=638424)

if res.model_customization is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `create_customization_request`                                                  | [models.CreateCustomizationRequest](../../models/createcustomizationrequest.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `model_id`                                                                      | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `organization_id`                                                               | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |


### Response

**[models.CreateModelCustomizationResponse](../../models/createmodelcustomizationresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## delete

Delete Model customization

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=545907,
)


res = s.model_customization.delete(customization_id='string', model_id='string', organization_id=841399)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `customization_id` | *str*              | :heavy_check_mark: | N/A                |
| `model_id`         | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[models.DeleteModelCustomizationResponse](../../models/deletemodelcustomizationresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## get

Get model customization

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=700347,
)


res = s.model_customization.get(customization_id='string', model_id='string', organization_id=90065)

if res.model_customization is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `customization_id` | *str*              | :heavy_check_mark: | N/A                |
| `model_id`         | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[models.GetModelCustomizationResponse](../../models/getmodelcustomizationresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## list

List model customizations

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=768578,
)


res = s.model_customization.list(model_id='string', organization_id=99895)

if res.customizations_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `model_id`         | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[models.ListModelCustomizationsResponse](../../models/listmodelcustomizationsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |
