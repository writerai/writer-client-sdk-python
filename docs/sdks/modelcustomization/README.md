# model_customization

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
    organization_id=437032,
)


res = s.model_customization.create(create_customization_request=shared.CreateCustomizationRequest(
    additional_hyper_parameters=shared.HyperParameters(
        num_virtual_tokens=902349,
    ),
    batch_size=697631,
    description='architecto',
    epochs=60225,
    learning_rate=9698.1,
    name='Shaun Osinski',
    prompt_template='corporis',
    training_dataset_file_id='explicabo',
    validation_dataset_file_id='nobis',
), model_id='enim', organization_id=607831)

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
    organization_id=363711,
)


res = s.model_customization.delete(customization_id='minima', model_id='excepturi', organization_id=38425)

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
    organization_id=438601,
)


res = s.model_customization.get(customization_id='culpa', model_id='doloribus', organization_id=958950)

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
    organization_id=102044,
)


res = s.model_customization.list(model_id='mollitia', organization_id=208876)

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

