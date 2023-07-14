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
    organization_id=358152,
)


res = s.model_customization.create(shared.CreateCustomizationRequest(
    additional_hyper_parameters=shared.HyperParameters(
        num_virtual_tokens=128926,
    ),
    batch_size=750686,
    description='enim',
    epochs=607831,
    learning_rate=3637.11,
    name='Velma Batz',
    prompt_template='doloribus',
    training_dataset_file_id='sapiente',
    validation_dataset_file_id='architecto',
), 'mollitia', 208876)

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
    organization_id=635059,
)


res = s.model_customization.delete('consequuntur', 'repellat', 653108)

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
    organization_id=581850,
)


res = s.model_customization.get('numquam', 'commodi', 466311)

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
    organization_id=474697,
)


res = s.model_customization.list('velit', 623510)

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

