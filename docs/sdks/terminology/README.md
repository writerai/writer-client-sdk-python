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

s = writer.Writer(
    api_key="",
    organization_id=551477,
)


res = s.terminology.add(create_terms_request=writer.CreateTermsRequest(
    models=[
        writer.TermCreate(
            approved_term_extension=writer.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            examples=[
                writer.TermExampleCreate(
                    example='string',
                    type=writer.TermExampleCreateType.BAD,
                ),
            ],
            linked_terms=[
                writer.LinkedTermCreate(),
            ],
            mistakes=[
                writer.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='string',
                ),
            ],
            tags=[
                writer.TermTagCreate(
                    tag='string',
                ),
            ],
            term='string',
            type=writer.TermCreateType.BANNED,
        ),
    ],
), team_id=623445, organization_id=822001)

if res.create_terms_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `create_terms_request`                                       | [models.CreateTermsRequest](../models/createtermsrequest.md) | :heavy_check_mark:                                           | N/A                                                          |
| `team_id`                                                    | *int*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `organization_id`                                            | *Optional[int]*                                              | :heavy_minus_sign:                                           | N/A                                                          |


### Response

**[models.AddTermsResponse](../../models/addtermsresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.FailResponseError | 400,401,403,404,500      | application/json         |
| models.SDKError          | 400-600                  | */*                      |

## delete

Delete terms

### Example Usage

```python
import writer

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

**[models.DeleteTermsResponse](../../models/deletetermsresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.FailResponseError | 400,401,403,404,500      | application/json         |
| models.SDKError          | 400-600                  | */*                      |

## find

Find terms

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="",
    organization_id=40141,
)

req = writer.FindTermsRequest(
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

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [models.FindTermsRequest](../../models/findtermsrequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |


### Response

**[models.FindTermsResponse](../../models/findtermsresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.FailResponseError | 400,401,403,404,500      | application/json         |
| models.SDKError          | 400-600                  | */*                      |

## update

Update terms

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="",
    organization_id=857478,
)


res = s.terminology.update(update_terms_request=writer.UpdateTermsRequest(
    models=[
        writer.TermUpdate(
            approved_term_extension=writer.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            examples=[
                writer.TermExampleCreate(
                    example='string',
                    type=writer.TermExampleCreateType.GOOD,
                ),
            ],
            id=597129,
            linked_terms=[
                writer.LinkedTermCreate(),
            ],
            mistakes=[
                writer.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='string',
                ),
            ],
            tags=[
                writer.TermTagCreate(
                    tag='string',
                ),
            ],
            term='string',
            type=writer.TermUpdateType.APPROVED,
        ),
    ],
), team_id=344620, x_request_id='string', organization_id=708455)

if res.create_terms_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `update_terms_request`                                       | [models.UpdateTermsRequest](../models/updatetermsrequest.md) | :heavy_check_mark:                                           | N/A                                                          |
| `team_id`                                                    | *int*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `x_request_id`                                               | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `organization_id`                                            | *Optional[int]*                                              | :heavy_minus_sign:                                           | N/A                                                          |


### Response

**[models.UpdateTermsResponse](../../models/updatetermsresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.FailResponseError | 400,401,403,404,500      | application/json         |
| models.SDKError          | 400-600                  | */*                      |
