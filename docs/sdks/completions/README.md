# Completions
(*completions*)

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
    api_key="",
    organization_id=486589,
)


res = s.completions.create(completion_request=shared.CompletionRequest(
    best_of=1,
    max_tokens=1024,
    min_tokens=1,
    prompt='bluetooth',
    stop=[
        'the',
        'is',
        'and',
    ],
    temperature=0.7,
    top_p=1,
), model_id='Extended', organization_id=134365)

if res.completion_response is not None:
    # handle response
    pass
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
    api_key="",
    organization_id=919503,
)


res = s.completions.create_model_customization_completion(completion_request=shared.CompletionRequest(
    best_of=1,
    max_tokens=1024,
    min_tokens=1,
    prompt='Uruguay',
    stop=[
        'the',
        'is',
        'and',
    ],
    temperature=0.7,
    top_p=1,
), customization_id='streamline', model_id='newton', organization_id=151932)

if res.completion_response is not None:
    # handle response
    pass
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

