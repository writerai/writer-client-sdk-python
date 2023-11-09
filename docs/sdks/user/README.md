# User
(*user*)

## Overview

Methods related to User

### Available Operations

* [list](#list) - List users

## list

List users

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    api_key="",
    organization_id=768578,
)

req = operations.ListUsersRequest()

res = s.user.list(req)

if res.paginated_result_user_public_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListUsersRequest](../../models/operations/listusersrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ListUsersResponse](../../models/operations/listusersresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |
