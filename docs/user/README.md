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
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=55,
)

req = operations.ListUsersRequest(
    limit=872651,
    offset=311860,
    search='tempora',
    sort_field=operations.ListUsersSortField.CREATION_TIME,
    sort_order=operations.ListUsersSortOrder.DESC,
)

res = s.user.list(req)

if res.paginated_result_user_public_response is not None:
    # handle response
```
