# Terminology
(*terminology*)

## Overview

Methods related to Terminology

### Available Operations

* [add](#add) - Add terms
* [delete](#delete) - Delete terms
* [find](#find) - Find terms
* [update](#update) - Update terms

## add

Add terms

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=551477,
)


res = s.terminology.add(create_terms_request=shared.CreateTermsRequest(
    models=[
        shared.TermCreate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            examples=[
                shared.TermExampleCreate(
                    example='string',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            linked_terms=[
                shared.LinkedTermCreate(),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='string',
                ),
            ],
            tags=[
                shared.TermTagCreate(
                    tag='string',
                ),
            ],
            term='string',
            type=shared.TermCreateType.BANNED,
        ),
    ],
), team_id=623445, organization_id=822001)

if res.create_terms_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `create_terms_request`                                                 | [shared.CreateTermsRequest](../../models/shared/createtermsrequest.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `team_id`                                                              | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `organization_id`                                                      | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |


### Response

**[operations.AddTermsResponse](../../models/operations/addtermsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |

## delete

Delete terms

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    api_key="",
    organization_id=545907,
)


res = s.terminology.delete(team_id=841399, x_request_id='string', ids=[
    698486,
], organization_id=557937)

if res.delete_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *int*              | :heavy_check_mark: | N/A                |
| `x_request_id`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `ids`              | List[*int*]        | :heavy_minus_sign: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DeleteTermsResponse](../../models/operations/deletetermsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |

## find

Find terms

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    api_key="",
    organization_id=40141,
)

req = operations.FindTermsRequest(
    tags=[
        'string',
    ],
    team_id=326883,
)

res = s.terminology.find(req)

if res.paginated_result_full_term_with_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.FindTermsRequest](../../models/operations/findtermsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.FindTermsResponse](../../models/operations/findtermsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |

## update

Update terms

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=857478,
)


res = s.terminology.update(update_terms_request=shared.UpdateTermsRequest(
    models=[
        shared.TermUpdate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            examples=[
                shared.TermExampleCreate(
                    example='string',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            id=597129,
            linked_terms=[
                shared.LinkedTermCreate(),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='string',
                ),
            ],
            tags=[
                shared.TermTagCreate(
                    tag='string',
                ),
            ],
            term='string',
            type=shared.TermUpdateType.APPROVED,
        ),
    ],
), team_id=344620, x_request_id='string', organization_id=708455)

if res.create_terms_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `update_terms_request`                                                 | [shared.UpdateTermsRequest](../../models/shared/updatetermsrequest.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `team_id`                                                              | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `x_request_id`                                                         | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `organization_id`                                                      | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |


### Response

**[operations.UpdateTermsResponse](../../models/operations/updatetermsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |
