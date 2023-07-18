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
    organization_id=110375,
)


res = s.snippet.delete(674752, 'animi', [
    'odit',
    'quo',
], 196582)

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
    organization_id=949572,
)

req = operations.FindSnippetsRequest(
    limit=368725,
    offset=662527,
    search='possimus',
    shortcuts=[
        'quasi',
    ],
    sort_field=operations.FindSnippetsSortField.CREATION_TIME,
    sort_order=operations.FindSnippetsSortOrder.DESC,
    tags=[
        'quasi',
        'reiciendis',
        'voluptatibus',
    ],
    team_id=878194,
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
    organization_id=468651,
)


res = s.snippet.update(509624, [
    shared.SnippetUpdate(
        description='ipsa',
        id='97b0074f-1547-41b5-a6e1-3b99d488e1e9',
        shortcut='veritatis',
        snippet='itaque',
        tags=[
            shared.SnippetTagV2(
                tag='enim',
            ),
            shared.SnippetTagV2(
                tag='consequatur',
            ),
        ],
    ),
    shared.SnippetUpdate(
        description='est',
        id='d2abd442-6980-42d5-82a9-4bb4f63c969e',
        shortcut='sint',
        snippet='officia',
        tags=[
            shared.SnippetTagV2(
                tag='debitis',
            ),
        ],
    ),
    shared.SnippetUpdate(
        description='a',
        id='a77dfb14-cd66-4ae3-95ef-b9ba88f3a669',
        shortcut='omnis',
        snippet='molestiae',
        tags=[
            shared.SnippetTagV2(
                tag='nihil',
            ),
        ],
    ),
    shared.SnippetUpdate(
        description='magnam',
        id='ba4469b6-e214-4195-9890-afa563e2516f',
        shortcut='debitis',
        snippet='eius',
        tags=[
            shared.SnippetTagV2(
                tag='deleniti',
            ),
            shared.SnippetTagV2(
                tag='facilis',
            ),
            shared.SnippetTagV2(
                tag='in',
            ),
            shared.SnippetTagV2(
                tag='architecto',
            ),
        ],
    ),
], 'architecto', 919483)

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

