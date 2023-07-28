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
    organization_id=957156,
)


res = s.completions.create(completion_request=shared.CompletionRequest(
    best_of=1,
    frequency_penalty=7781.57,
    logprobs=140350,
    max_tokens=1024,
    min_tokens=1,
    n=870013,
    presence_penalty=8700.88,
    prompt='maiores',
    stop=[
        'quod',
        'quod',
    ],
    temperature=0.7,
    top_p=1,
), model_id='esse', organization_id=520478)

if res.completion_response is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `completion_request`                                                 | [shared.CompletionRequest](../../models/shared/completionrequest.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `model_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `organization_id`                                                    | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |


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
    organization_id=780529,
)


res = s.completions.create_model_customization_completion(completion_request=shared.CompletionRequest(
    best_of=1,
    frequency_penalty=6788.8,
    logprobs=118274,
    max_tokens=1024,
    min_tokens=1,
    n=720633,
    presence_penalty=6399.21,
    prompt='occaecati',
    stop=[
        'deleniti',
    ],
    temperature=0.7,
    top_p=1,
), customization_id='hic', model_id='optio', organization_id=521848)

if res.completion_response is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `completion_request`                                                 | [shared.CompletionRequest](../../models/shared/completionrequest.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `customization_id`                                                   | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `model_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `organization_id`                                                    | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |


### Response

**[operations.CreateModelCustomizationCompletionResponse](../../models/operations/createmodelcustomizationcompletionresponse.md)**

