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
    security=shared.Security(
        api_key="",
    ),
    organization_id=363711,
)


res = s.snippet.delete(team_id=325047, x_request_id='excepturi', ids=[
    'accusantium',
], organization_id=438601)

if res.delete_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *int*              | :heavy_check_mark: | N/A                |
| `x_request_id`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `ids`              | list[*str*]        | :heavy_minus_sign: | N/A                |
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
    security=shared.Security(
        api_key="",
    ),
    organization_id=634274,
)

req = operations.FindSnippetsRequest(
    limit=988374,
    offset=958950,
    search='architecto',
    shortcuts=[
        'mollitia',
    ],
    sort_field=operations.FindSnippetsSortField.SHORTCUT,
    sort_order=operations.FindSnippetsSortOrder.DESC,
    tags=[
        'consequuntur',
    ],
    team_id=995300,
)

res = s.snippet.find(req)

if res.paginated_result_snippet_with_user is not None:
    # handle response
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
    security=shared.Security(
        api_key="",
    ),
    organization_id=653108,
)


res = s.snippet.update(team_id=581850, request_body=[
    shared.SnippetUpdate(
        description='numquam',
        id='67739251-aa52-4c3f-9ad0-19da1ffe78f0',
        shortcut='omnis',
        snippet='voluptate',
        tags=[
            shared.SnippetTagV2(
                tag='cum',
            ),
        ],
    ),
], x_request_id='perferendis', organization_id=39187)

if res.snippet_with_users is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `team_id`                                                          | *int*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `request_body`                                                     | list[[shared.SnippetUpdate](../../models/shared/snippetupdate.md)] | :heavy_minus_sign:                                                 | N/A                                                                |
| `x_request_id`                                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `organization_id`                                                  | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |


### Response

**[operations.UpdateSnippetsResponse](../../models/operations/updatesnippetsresponse.md)**

