# Snippet
(*snippet*)

## Overview

Methods related to Snippets

### Available Operations

* [delete](#delete) - Delete snippets
* [find](#find) - Find snippets
* [update](#update) - Update snippets

## delete

Delete snippets

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=545907,
)


res = s.snippet.delete(team_id=841399, x_request_id='string', ids=[
    'string',
], organization_id=698486)

if res.delete_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *int*              | :heavy_check_mark: | N/A                |
| `x_request_id`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `ids`              | List[*str*]        | :heavy_minus_sign: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DeleteSnippetsResponse](../../models/operations/deletesnippetsresponse.md)**


## find

Find snippets

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=40141,
)

req = operations.FindSnippetsRequest(
    shortcuts=[
        'string',
    ],
    tags=[
        'string',
    ],
    team_id=326883,
)

res = s.snippet.find(req)

if res.paginated_result_snippet_with_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.FindSnippetsRequest](../../models/operations/findsnippetsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.FindSnippetsResponse](../../models/operations/findsnippetsresponse.md)**


## update

Update snippets

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=857478,
)


res = s.snippet.update(team_id=24555, request_body=[
    shared.SnippetUpdate(
        id='<ID>',
        snippet='string',
        tags=[
            shared.SnippetTagV2(
                tag='string',
            ),
        ],
    ),
], x_request_id='string', organization_id=597129)

if res.snippet_with_users is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `team_id`                                                          | *int*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `request_body`                                                     | List[[shared.SnippetUpdate](../../models/shared/snippetupdate.md)] | :heavy_minus_sign:                                                 | N/A                                                                |
| `x_request_id`                                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `organization_id`                                                  | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |


### Response

**[operations.UpdateSnippetsResponse](../../models/operations/updatesnippetsresponse.md)**

