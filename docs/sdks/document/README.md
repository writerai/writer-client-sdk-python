# document

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
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=756107,
)


res = s.document.get(document_id=576157, team_id=396098, organization_id=592042)

if res.document is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `document_id`      | *int*              | :heavy_check_mark: | N/A                |
| `team_id`          | *int*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDocumentDetailsResponse](../../models/operations/getdocumentdetailsresponse.md)**


## list

List team documents

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=896039,
)

req = operations.ListTeamDocumentsRequest(
    limit=572252,
    offset=638921,
    search='dolor',
    sort_field=operations.ListTeamDocumentsSortField.OPENED_BY_ME_TIME,
    sort_order=operations.ListTeamDocumentsSortOrder.DESC,
    team_id=680056,
)

res = s.document.list(req)

if res.brief_documents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListTeamDocumentsRequest](../../models/operations/listteamdocumentsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListTeamDocumentsResponse](../../models/operations/listteamdocumentsresponse.md)**

