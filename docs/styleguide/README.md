# styleguide

## Overview

Methods related to Styleguide

### Available Operations

* [get](#get) - Page details
* [list_pages](#list_pages) - List your styleguide pages

## get

Page details

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=100226,
)


req = operations.PageDetailsRequest(
    page_id=99569,
)

res = s.styleguide.get(req)

if res.page_with_section_response is not None:
    # handle response
```

## list_pages

List your styleguide pages

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=919483,
)


req = operations.ListPagesRequest(
    limit=352312,
    offset=714242,
    status=operations.ListPagesStatusEnum.LIVE,
)

res = s.styleguide.list_pages(req)

if res.paginated_result_page_public_api_response is not None:
    # handle response
```
