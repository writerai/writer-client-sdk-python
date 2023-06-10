# completions

## Overview

Methods related to Completions

### Available Operations

* [create](#create) - Create completion for LLM model
* [create_model_customization_completion](#create_model_customization_completion) - Create completion for LLM customization model

## create

Create completion for LLM model

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=870088,
)

req = operations.CreateCompletionRequest(
    completion_request=shared.CompletionRequest(
        best_of=978619,
        frequency_penalty=4736.08,
        logprobs=799159,
        max_tokens=800911,
        min_tokens=461479,
        n=520478,
        presence_penalty=7805.29,
        prompt='dolorum',
        stop=[
            'nam',
        ],
        temperature=6399.21,
        top_p=5820.2,
    ),
    model_id='fugit',
)

res = s.completions.create(req)

if res.completion_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCompletionRequest](../../models/operations/createcompletionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateCompletionResponse](../../models/operations/createcompletionresponse.md)**


## create_model_customization_completion

Create completion for LLM customization model

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=537373,
)

req = operations.CreateModelCustomizationCompletionRequest(
    completion_request=shared.CompletionRequest(
        best_of=944669,
        frequency_penalty=7586.16,
        logprobs=521848,
        max_tokens=105907,
        min_tokens=414662,
        n=473600,
        presence_penalty=2645.55,
        prompt='qui',
        stop=[
            'cum',
            'esse',
            'ipsum',
            'excepturi',
        ],
        temperature=1352.18,
        top_p=187.89,
    ),
    customization_id='ad',
    model_id='natus',
)

res = s.completions.create_model_customization_completion(req)

if res.completion_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.CreateModelCustomizationCompletionRequest](../../models/operations/createmodelcustomizationcompletionrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.CreateModelCustomizationCompletionResponse](../../models/operations/createmodelcustomizationcompletionresponse.md)**

