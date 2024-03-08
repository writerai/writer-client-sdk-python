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

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
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

**[models.PageDetailsResponse](../../models/pagedetailsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## list_pages

List your styleguide pages

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=763372,
)


res = s.styleguide.list_pages(limit=760116, offset=303332, status=writer.QueryParamStatus.LIVE)

if res.paginated_result_page_public_api_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `status`                                                              | [Optional[models.QueryParamStatus]](../../models/queryparamstatus.md) | :heavy_minus_sign:                                                    | N/A                                                                   |


### Response

**[models.ListPagesResponse](../../models/listpagesresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |
