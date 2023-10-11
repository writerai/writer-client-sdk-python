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
                    example='calculate Toyota noon',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            linked_terms=[
                shared.LinkedTermCreate(),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='Chief',
                ),
            ],
            tags=[
                shared.TermTagCreate(
                    tag='kelvin',
                ),
            ],
            term='lime',
            type=shared.TermCreateType.BANNED,
        ),
    ],
), team_id=623862, organization_id=445859)

if res.create_terms_response is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `create_terms_request`                                                 | [shared.CreateTermsRequest](../../models/shared/createtermsrequest.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `team_id`                                                              | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `organization_id`                                                      | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |


### Response

**[operations.AddTermsResponse](../../models/operations/addtermsresponse.md)**


## delete

Delete terms

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=545907,
)


res = s.terminology.delete(team_id=841399, x_request_id='Designer', ids=[
    386564,
], organization_id=201447)

if res.delete_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *int*              | :heavy_check_mark: | N/A                |
| `x_request_id`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `ids`              | list[*int*]        | :heavy_minus_sign: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DeleteTermsResponse](../../models/operations/deletetermsresponse.md)**


## find

Find terms

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=40141,
)

req = operations.FindTermsRequest(
    tags=[
        'underestimate',
    ],
    team_id=111247,
)

res = s.terminology.find(req)

if res.paginated_result_full_term_with_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.FindTermsRequest](../../models/operations/findtermsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.FindTermsResponse](../../models/operations/findtermsresponse.md)**


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
                    example='Rock',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            id=708455,
            linked_terms=[
                shared.LinkedTermCreate(),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='Metal cheater Islands',
                ),
            ],
            tags=[
                shared.TermTagCreate(
                    tag='withdrawal extend',
                ),
            ],
            term='bifurcated',
            type=shared.TermUpdateType.BANNED,
        ),
    ],
), team_id=789275, x_request_id='syndicate', organization_id=345187)

if res.create_terms_response is not None:
    # handle response
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

