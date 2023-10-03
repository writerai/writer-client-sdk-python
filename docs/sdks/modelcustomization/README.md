# ModelCustomization
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
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=486589,
)


res = s.model_customization.create(create_customization_request=shared.CreateCustomizationRequest(
    additional_hyper_parameters=shared.HyperParameters(
        num_virtual_tokens=489382,
    ),
    batch_size=638424,
    description='Synchronised full-range emulation',
    epochs=134365,
    learning_rate=7865.46,
    name='shred',
    prompt_template='technology East',
    training_dataset_file_id='evolve',
    validation_dataset_file_id='fuchsia Gasoline Screen',
), model_id='mobile', organization_id=656256)

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
    organization_id=545907,
)


res = s.model_customization.delete(customization_id='Van', model_id='complexity', organization_id=952479)

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
    organization_id=700347,
)


res = s.model_customization.get(customization_id='Northeast', model_id='Hatchback', organization_id=830636)

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
    organization_id=768578,
)


res = s.model_customization.list(model_id='Northeast', organization_id=257649)

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

