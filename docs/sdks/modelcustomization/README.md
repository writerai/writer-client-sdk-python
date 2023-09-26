# ModelCustomization

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
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=324141,
)


res = s.model_customization.create(create_customization_request=shared.CreateCustomizationRequest(
    additional_hyper_parameters=shared.HyperParameters(
        num_virtual_tokens=617636,
    ),
    batch_size=149675,
    description='iste',
    epochs=222321,
    learning_rate=6169.34,
    name='May Turcotte',
    prompt_template='corporis',
    training_dataset_file_id='iste',
    validation_dataset_file_id='iure',
), model_id='saepe', organization_id=697631)

if res.model_customization is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `create_customization_request`                                                         | [shared.CreateCustomizationRequest](../../models/shared/createcustomizationrequest.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `model_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `organization_id`                                                                      | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.CreateModelCustomizationResponse](../../models/operations/createmodelcustomizationresponse.md)**


## delete

Delete Model customization

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=99280,
)


res = s.model_customization.delete(customization_id='ipsa', model_id='reiciendis', organization_id=666767)

if res.delete_model_customization_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `customization_id` | *str*              | :heavy_check_mark: | N/A                |
| `model_id`         | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DeleteModelCustomizationResponse](../../models/operations/deletemodelcustomizationresponse.md)**


## get

Get model customization

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=653140,
)


res = s.model_customization.get(customization_id='laborum', model_id='dolores', organization_id=210382)

if res.model_customization is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `customization_id` | *str*              | :heavy_check_mark: | N/A                |
| `model_id`         | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetModelCustomizationResponse](../../models/operations/getmodelcustomizationresponse.md)**


## list

List model customizations

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=358152,
)


res = s.model_customization.list(model_id='explicabo', organization_id=750686)

if res.customizations_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `model_id`         | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.ListModelCustomizationsResponse](../../models/operations/listmodelcustomizationsresponse.md)**

