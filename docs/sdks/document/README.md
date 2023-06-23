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
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=885338,
)

req = operations.GetDocumentDetailsRequest(
    document_id=185636,
    team_id=679880,
)

res = s.document.get(req)

if res.document is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetDocumentDetailsRequest](../../models/operations/getdocumentdetailsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetDocumentDetailsResponse](../../models/operations/getdocumentdetailsresponse.md)**


## list

List team documents

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=952792,
)

req = operations.ListTeamDocumentsRequest(
    limit=456130,
    offset=687488,
    search='iusto',
    sort_field=operations.ListTeamDocumentsSortField.CREATION_TIME,
    sort_order=operations.ListTeamDocumentsSortOrder.DESC,
    team_id=947371,
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

