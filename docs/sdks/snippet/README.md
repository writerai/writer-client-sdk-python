# snippet

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
    organization_id=128926,
)


res = s.snippet.delete(team_id=750686, x_request_id='enim', ids=[
    'omnis',
], organization_id=363711)

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
    organization_id=325047,
)

req = operations.FindSnippetsRequest(
    limit=570197,
    offset=38425,
    search='iure',
    shortcuts=[
        'culpa',
    ],
    sort_field=operations.FindSnippetsSortField.MODIFICATION_TIME,
    sort_order=operations.FindSnippetsSortOrder.DESC,
    tags=[
        'architecto',
    ],
    team_id=652790,
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
    organization_id=208876,
)


res = s.snippet.update(team_id=635059, request_body=[
    shared.SnippetUpdate(
        description='consequuntur',
        id='fa946773-9251-4aa5-ac3f-5ad019da1ffe',
        shortcut='nihil',
        snippet='praesentium',
        tags=[
            shared.SnippetTagV2(
                tag='voluptatibus',
            ),
        ],
    ),
], x_request_id='ipsa', organization_id=604846)

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

