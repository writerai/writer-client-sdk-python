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
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=581850,
)


req = operations.DeleteSnippetsRequest(
    x_request_id='numquam',
    ids=[
        'quam',
        'molestiae',
    ],
    team_id=244425,
)

res = s.snippet.delete(req)

if res.delete_response is not None:
    # handle response
```

## find

Find snippets

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=623510,
)


req = operations.FindSnippetsRequest(
    limit=158969,
    offset=338007,
    search='vitae',
    shortcuts=[
        'animi',
        'enim',
        'odit',
    ],
    sort_field=operations.FindSnippetsSortFieldEnum.MODIFICATION_TIME,
    sort_order=operations.FindSnippetsSortOrderEnum.ASC,
    tags=[
        'ipsam',
        'id',
        'possimus',
        'aut',
    ],
    team_id=97101,
)

res = s.snippet.find(req)

if res.paginated_result_snippet_with_user is not None:
    # handle response
```

## update

Update snippets

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=622846,
)


req = operations.UpdateSnippetsRequest(
    request_body=[
        shared.SnippetUpdate(
            description='laborum',
            id='1ffe78f0-97b0-4074-b154-71b5e6e13b99',
            shortcut='pariatur',
            snippet='modi',
            tags=[
                shared.SnippetTagV2(
                    tag='rem',
                ),
                shared.SnippetTagV2(
                    tag='voluptates',
                ),
                shared.SnippetTagV2(
                    tag='quasi',
                ),
            ],
        ),
        shared.SnippetUpdate(
            description='repudiandae',
            id='91e450ad-2abd-4442-a980-2d502a94bb4f',
            shortcut='eum',
            snippet='non',
            tags=[
                shared.SnippetTagV2(
                    tag='sint',
                ),
                shared.SnippetTagV2(
                    tag='aliquid',
                ),
                shared.SnippetTagV2(
                    tag='provident',
                ),
                shared.SnippetTagV2(
                    tag='necessitatibus',
                ),
            ],
        ),
        shared.SnippetUpdate(
            description='sint',
            id='a3efa77d-fb14-4cd6-aae3-95efb9ba88f3',
            shortcut='deserunt',
            snippet='nisi',
            tags=[
                shared.SnippetTagV2(
                    tag='natus',
                ),
                shared.SnippetTagV2(
                    tag='omnis',
                ),
            ],
        ),
        shared.SnippetUpdate(
            description='molestiae',
            id='074ba446-9b6e-4214-9959-890afa563e25',
            shortcut='quasi',
            snippet='iure',
            tags=[
                shared.SnippetTagV2(
                    tag='debitis',
                ),
                shared.SnippetTagV2(
                    tag='eius',
                ),
                shared.SnippetTagV2(
                    tag='maxime',
                ),
                shared.SnippetTagV2(
                    tag='deleniti',
                ),
            ],
        ),
    ],
    x_request_id='facilis',
    team_id=447926,
)

res = s.snippet.update(req)

if res.snippet_with_users is not None:
    # handle response
```
