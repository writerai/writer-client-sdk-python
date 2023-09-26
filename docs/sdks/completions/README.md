# Completions

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
    organization_id=392785,
)


res = s.completions.create(completion_request=shared.CompletionRequest(
    best_of=1,
    frequency_penalty=9255.97,
    logprobs=836079,
    max_tokens=1024,
    min_tokens=1,
    n=71036,
    presence_penalty=3373.96,
    prompt='veritatis',
    stop=[
        'deserunt',
    ],
    temperature=0.7,
    top_p=1,
), model_id='perferendis', organization_id=368241)

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
    organization_id=832620,
)


res = s.completions.create_model_customization_completion(completion_request=shared.CompletionRequest(
    best_of=1,
    frequency_penalty=9571.56,
    logprobs=778157,
    max_tokens=1024,
    min_tokens=1,
    n=140350,
    presence_penalty=8700.13,
    prompt='at',
    stop=[
        'maiores',
    ],
    temperature=0.7,
    top_p=1,
), customization_id='molestiae', model_id='quod', organization_id=800911)

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

