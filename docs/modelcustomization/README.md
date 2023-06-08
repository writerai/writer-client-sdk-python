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
    organization_id=653140,
)

req = operations.CreateModelCustomizationRequest(
    create_customization_request=shared.CreateCustomizationRequest(
        additional_hyper_parameters=shared.HyperParameters(
            num_virtual_tokens=670638,
        ),
        batch_size=170909,
        description='dolorem',
        epochs=358152,
        learning_rate=1289.26,
        name='Ronnie Mohr',
        prompt_template='excepturi',
        training_dataset_file_id='accusantium',
        validation_dataset_file_id='iure',
    ),
    model_id='culpa',
)

res = s.model_customization.create(req)

if res.model_customization is not None:
    # handle response
```

## delete

Delete Model customization

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=988374,
)

req = operations.DeleteModelCustomizationRequest(
    customization_id='sapiente',
    model_id='architecto',
)

res = s.model_customization.delete(req)

if res.delete_model_customization_200_application_json_object is not None:
    # handle response
```

## get

Get model customization

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=652790,
)

req = operations.GetModelCustomizationRequest(
    customization_id='dolorem',
    model_id='culpa',
)

res = s.model_customization.get(req)

if res.model_customization is not None:
    # handle response
```

## list

List model customizations

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=161309,
)

req = operations.ListModelCustomizationsRequest(
    model_id='repellat',
)

res = s.model_customization.list(req)

if res.customizations_response is not None:
    # handle response
```
