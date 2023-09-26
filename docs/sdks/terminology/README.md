# Terminology

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
    organization_id=480894,
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
            description='harum',
            examples=[
                shared.TermExampleCreate(
                    example='enim',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            highlight=False,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=414263,
                    reference='repudiandae',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='quae',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='quidem',
                ),
            ],
            pos=shared.TermCreatePos.ADVERB,
            reference='excepturi',
            tags=[
                shared.TermTagCreate(
                    tag='pariatur',
                ),
            ],
            term='modi',
            type=shared.TermCreateType.BANNED,
        ),
    ],
), team_id=523248, organization_id=916723)

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
    organization_id=93940,
)


res = s.terminology.delete(team_id=921158, x_request_id='sint', ids=[
    83112,
], organization_id=929297)

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
    organization_id=277718,
)

req = operations.FindTermsRequest(
    limit=318569,
    offset=9356,
    part_of_speech=operations.FindTermsPartOfSpeech.ADVERB,
    sort_field=operations.FindTermsSortField.TYPE,
    sort_order=operations.FindTermsSortOrder.ASC,
    tags=[
        'deserunt',
    ],
    team_id=716327,
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
    organization_id=264730,
)


res = s.terminology.update(update_terms_request=shared.UpdateTermsRequest(
    fail_handling=shared.UpdateTermsRequestFailHandling.ACCUMULATE,
    models=[
        shared.TermUpdate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='aliquid',
            examples=[
                shared.TermExampleCreate(
                    example='cupiditate',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            highlight=False,
            id=20107,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=164940,
                    reference='assumenda',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='ipsam',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='fugit',
                ),
            ],
            pos=shared.TermUpdatePos.ADVERB,
            tags=[
                shared.TermTagCreate(
                    tag='excepturi',
                ),
            ],
            term='tempora',
            type=shared.TermUpdateType.PENDING,
        ),
    ],
), team_id=735194, x_request_id='labore', organization_id=962189)

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

