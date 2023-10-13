# Styleguide
(*styleguide*)

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
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=700347,
)


res = s.styleguide.get(page_id=90065)

if res.page_with_section_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `page_id`          | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PageDetailsResponse](../../models/operations/pagedetailsresponse.md)**


## list_pages

List your styleguide pages

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=763372,
)


res = s.styleguide.list_pages(limit=760116, offset=303332, status=operations.ListPagesStatus.LIVE)

if res.paginated_result_page_public_api_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `limit`                                                                            | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `offset`                                                                           | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `status`                                                                           | [Optional[operations.ListPagesStatus]](../../models/operations/listpagesstatus.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |


### Response

**[operations.ListPagesResponse](../../models/operations/listpagesresponse.md)**

