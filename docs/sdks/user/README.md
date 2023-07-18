# user

## Overview

Methods related to User

### Available Operations

* [list](#list) - List users

## list

List users

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=679880,
)

req = operations.ListUsersRequest(
    limit=952792,
    offset=456130,
    search='harum',
    sort_field=operations.ListUsersSortField.DELETED,
    sort_order=operations.ListUsersSortOrder.ASC,
)

res = s.user.list(req)

if res.paginated_result_user_public_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListUsersRequest](../../models/operations/listusersrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ListUsersResponse](../../models/operations/listusersresponse.md)**

