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
        api_key="",
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

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PageDetailsRequest](../../models/operations/pagedetailsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PageDetailsResponse](../../models/operations/pagedetailsresponse.md)**


## list_pages

List your styleguide pages

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=919483,
)

req = operations.ListPagesRequest(
    limit=352312,
    offset=714242,
    status=operations.ListPagesStatus.LIVE,
)

res = s.styleguide.list_pages(req)

if res.paginated_result_page_public_api_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListPagesRequest](../../models/operations/listpagesrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ListPagesResponse](../../models/operations/listpagesresponse.md)**

