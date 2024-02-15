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

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=486589,
)


res = s.completions.create(completion_request=writer.CompletionRequest(
    prompt='<value>',
    best_of=1,
    max_tokens=1024,
    min_tokens=1,
    stop=[
        'the',
        'is',
        'and',
    ],
    temperature=0.7,
    top_p=1,
), model_id='<value>', organization_id=489382)

if res.completion_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                     | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `completion_request`                                          | [models.CompletionRequest](../../models/completionrequest.md) | :heavy_check_mark:                                            | N/A                                                           |
| `model_id`                                                    | *str*                                                         | :heavy_check_mark:                                            | N/A                                                           |
| `organization_id`                                             | *Optional[int]*                                               | :heavy_minus_sign:                                            | N/A                                                           |


### Response

**[models.CreateCompletionResponse](../../models/createcompletionresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## create_model_customization_completion

Create completion for LLM customization model

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=919503,
)


res = s.completions.create_model_customization_completion(completion_request=writer.CompletionRequest(
    prompt='<value>',
    best_of=1,
    max_tokens=1024,
    min_tokens=1,
    stop=[
        'the',
        'is',
        'and',
    ],
    temperature=0.7,
    top_p=1,
), customization_id='<value>', model_id='<value>', organization_id=41297)

if res.completion_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                     | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `completion_request`                                          | [models.CompletionRequest](../../models/completionrequest.md) | :heavy_check_mark:                                            | N/A                                                           |
| `customization_id`                                            | *str*                                                         | :heavy_check_mark:                                            | N/A                                                           |
| `model_id`                                                    | *str*                                                         | :heavy_check_mark:                                            | N/A                                                           |
| `organization_id`                                             | *Optional[int]*                                               | :heavy_minus_sign:                                            | N/A                                                           |


### Response

**[models.CreateModelCustomizationCompletionResponse](../../models/createmodelcustomizationcompletionresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |
