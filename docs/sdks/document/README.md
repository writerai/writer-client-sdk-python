# Document
(*document*)

## Overview

Methods related to document

### Available Operations

* [get](#get) - Get document details
* [list](#list) - List team documents

## get

Get document details

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    api_key="",
    organization_id=700347,
)


res = s.document.get(document_id=90065, team_id=558834, organization_id=844199)

if res.document is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `document_id`      | *int*              | :heavy_check_mark: | N/A                |
| `team_id`          | *int*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDocumentDetailsResponse](../../models/operations/getdocumentdetailsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |

## list

List team documents

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    api_key="",
    organization_id=768578,
)

req = operations.ListTeamDocumentsRequest(
    team_id=99895,
)

res = s.document.list(req)

if res.brief_documents is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListTeamDocumentsRequest](../../models/operations/listteamdocumentsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListTeamDocumentsResponse](../../models/operations/listteamdocumentsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |
