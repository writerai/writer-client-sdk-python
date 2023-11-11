# Models
(*models*)

## Overview

Methods related to Model

### Available Operations

* [list](#list) - List available LLM models

## list

List available LLM models

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="",
    organization_id=768578,
)


res = s.models.list(organization_id=99895)

if res.generation_models_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[models.ListModelsResponse](../../models/listmodelsresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.FailResponseError | 400,401,403,404,500      | application/json         |
| models.SDKError          | 400-600                  | */*                      |
