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
    organization_id=995300,
)


res = s.snippet.delete(653108, 'occaecati', [
    'commodi',
    'quam',
], 474697)

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
    organization_id=244425,
)

req = operations.FindSnippetsRequest(
    limit=623510,
    offset=158969,
    search='quis',
    shortcuts=[
        'laborum',
    ],
    sort_field=operations.FindSnippetsSortField.CREATION_TIME,
    sort_order=operations.FindSnippetsSortOrder.ASC,
    tags=[
        'quo',
    ],
    team_id=196582,
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
    organization_id=949572,
)


res = s.snippet.update(368725, [
    shared.SnippetUpdate(
        description='possimus',
        id='019da1ff-e78f-4097-b007-4f15471b5e6e',
        shortcut='quae',
        snippet='ipsum',
        tags=[
            shared.SnippetTagV2(
                tag='molestias',
            ),
            shared.SnippetTagV2(
                tag='excepturi',
            ),
            shared.SnippetTagV2(
                tag='pariatur',
            ),
        ],
    ),
    shared.SnippetUpdate(
        description='modi',
        id='88e1e91e-450a-4d2a-bd44-269802d502a9',
        shortcut='tempora',
        snippet='facilis',
        tags=[
            shared.SnippetTagV2(
                tag='labore',
            ),
            shared.SnippetTagV2(
                tag='delectus',
            ),
            shared.SnippetTagV2(
                tag='eum',
            ),
        ],
    ),
    shared.SnippetUpdate(
        description='non',
        id='c969e9a3-efa7-47df-b14c-d66ae395efb9',
        shortcut='nam',
        snippet='id',
        tags=[
            shared.SnippetTagV2(
                tag='deleniti',
            ),
            shared.SnippetTagV2(
                tag='sapiente',
            ),
            shared.SnippetTagV2(
                tag='amet',
            ),
        ],
    ),
], 'deserunt', 394869)

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

