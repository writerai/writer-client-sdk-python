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
    security=shared.Security(
        api_key="",
    ),
    organization_id=486589,
)


res = s.completions.create(completion_request=shared.CompletionRequest(
    best_of=1,
    frequency_penalty=4893.82,
    logprobs=638424,
    max_tokens=1024,
    min_tokens=1,
    n=859213,
    presence_penalty=4174.58,
    prompt='South',
    stop=[
        'shred',
    ],
    temperature=0.7,
    top_p=1,
), model_id='abnormally', organization_id=455222)

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
    organization_id=919503,
)


res = s.completions.create_model_customization_completion(completion_request=shared.CompletionRequest(
    best_of=1,
    frequency_penalty=412.97,
    logprobs=951257,
    max_tokens=1024,
    min_tokens=1,
    n=314952,
    presence_penalty=657.2,
    prompt='platforms convergence Bicycle',
    stop=[
        'heavily',
    ],
    temperature=0.7,
    top_p=1,
), customization_id='green', model_id='cum', organization_id=110459)

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

