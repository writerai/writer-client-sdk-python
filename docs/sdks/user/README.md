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

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=768578,
)

req = writer.ListUsersRequest()

res = s.user.list(req)

if res.paginated_result_user_public_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [models.ListUsersRequest](../../models/listusersrequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |


### Response

**[models.ListUsersResponse](../../models/listusersresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 400-600             | */*                 |
