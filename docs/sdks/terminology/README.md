# terminology

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
    security=shared.Security(
        api_key="",
    ),
    organization_id=979587,
)


res = s.terminology.add(create_terms_request=shared.CreateTermsRequest(
    fail_handling=shared.CreateTermsRequestFailHandling.ACCUMULATE,
    models=[
        shared.TermCreate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='corporis',
            examples=[
                shared.TermExampleCreate(
                    example='dolore',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            highlight=False,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=118727,
                    reference='harum',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='enim',
                    pos=shared.TermMistakeCreatePos.ADJECTIVE,
                    reference='commodi',
                ),
            ],
            pos=shared.TermCreatePos.ADJECTIVE,
            reference='quae',
            tags=[
                shared.TermTagCreate(
                    tag='ipsum',
                ),
            ],
            term='quidem',
            type=shared.TermCreateType.BANNED,
        ),
    ],
), team_id=566602, organization_id=865103)

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
    security=shared.Security(
        api_key="",
    ),
    organization_id=265389,
)


res = s.terminology.delete(team_id=508969, x_request_id='rem', ids=[
    916723,
], organization_id=93940)

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
    security=shared.Security(
        api_key="",
    ),
    organization_id=921158,
)

req = operations.FindTermsRequest(
    limit=575947,
    offset=83112,
    part_of_speech=operations.FindTermsPartOfSpeech.ADJECTIVE,
    sort_field=operations.FindTermsSortField.CREATION_TIME,
    sort_order=operations.FindTermsSortOrder.ASC,
    tags=[
        'consequatur',
    ],
    team_id=667411,
    term='quibusdam',
    type=operations.FindTermsType.APPROVED,
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
    security=shared.Security(
        api_key="",
    ),
    organization_id=647174,
)


res = s.terminology.update(update_terms_request=shared.UpdateTermsRequest(
    fail_handling=shared.UpdateTermsRequestFailHandling.SKIP,
    models=[
        shared.TermUpdate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='quibusdam',
            examples=[
                shared.TermExampleCreate(
                    example='labore',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            highlight=False,
            id=183191,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=397821,
                    reference='cupiditate',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='quos',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='magni',
                ),
            ],
            pos=shared.TermUpdatePos.ADJECTIVE,
            tags=[
                shared.TermTagCreate(
                    tag='ipsam',
                ),
            ],
            term='alias',
            type=shared.TermUpdateType.APPROVED,
        ),
    ],
), team_id=677817, x_request_id='excepturi', organization_id=270008)

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

