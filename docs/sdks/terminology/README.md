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
    organization_id=904648,
)


res = s.terminology.add(shared.CreateTermsRequest(
    fail_handling=shared.CreateTermsRequestFailHandling.VALIDATE_ONLY,
    models=[
        shared.TermCreate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='consequuntur',
            examples=[
                shared.TermExampleCreate(
                    example='natus',
                    type=shared.TermExampleCreateType.GOOD,
                ),
                shared.TermExampleCreate(
                    example='sunt',
                    type=shared.TermExampleCreateType.BAD,
                ),
                shared.TermExampleCreate(
                    example='illum',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            highlight=False,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=411397,
                    reference='excepturi',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=139972,
                    reference='ea',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=33222,
                    reference='ab',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=982575,
                    reference='quidem',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='voluptate',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='nam',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='eaque',
                    pos=shared.TermMistakeCreatePos.ADJECTIVE,
                    reference='nemo',
                ),
            ],
            pos=shared.TermCreatePos.ADJECTIVE,
            reference='perferendis',
            tags=[
                shared.TermTagCreate(
                    tag='amet',
                ),
                shared.TermTagCreate(
                    tag='aut',
                ),
                shared.TermTagCreate(
                    tag='cumque',
                ),
                shared.TermTagCreate(
                    tag='corporis',
                ),
            ],
            term='hic',
            type=shared.TermCreateType.PENDING,
        ),
    ],
), 749999, 171629)

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
    organization_id=339404,
)


res = s.terminology.delete(521037, 'dignissimos', [
    338985,
], 199996)

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
    organization_id=179490,
)

req = operations.FindTermsRequest(
    limit=18521,
    offset=170986,
    part_of_speech=operations.FindTermsPartOfSpeech.ADJECTIVE,
    sort_field=operations.FindTermsSortField.CREATION_TIME,
    sort_order=operations.FindTermsSortOrder.ASC,
    tags=[
        'nostrum',
        'hic',
        'recusandae',
        'omnis',
    ],
    team_id=704415,
    term='perspiciatis',
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
    organization_id=783645,
)


res = s.terminology.update(shared.UpdateTermsRequest(
    fail_handling=shared.UpdateTermsRequestFailHandling.ACCUMULATE,
    models=[
        shared.TermUpdate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='error',
            examples=[
                shared.TermExampleCreate(
                    example='occaecati',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            highlight=False,
            id=237893,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=934214,
                    reference='modi',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=613966,
                    reference='dolorum',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=535633,
                    reference='pariatur',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=589910,
                    reference='nobis',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='delectus',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='quos',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='aliquid',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='dolorem',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='dolor',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='ipsum',
                ),
            ],
            pos=shared.TermUpdatePos.ADJECTIVE,
            tags=[
                shared.TermTagCreate(
                    tag='cum',
                ),
                shared.TermTagCreate(
                    tag='voluptate',
                ),
                shared.TermTagCreate(
                    tag='dignissimos',
                ),
            ],
            term='reiciendis',
            type=shared.TermUpdateType.APPROVED,
        ),
        shared.TermUpdate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='dolorum',
            examples=[
                shared.TermExampleCreate(
                    example='veritatis',
                    type=shared.TermExampleCreateType.GOOD,
                ),
                shared.TermExampleCreate(
                    example='ipsa',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            highlight=False,
            id=487838,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=881005,
                    reference='quidem',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=976405,
                    reference='voluptas',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='eos',
                    pos=shared.TermMistakeCreatePos.ADVERB,
                    reference='sit',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='fugiat',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='soluta',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='dolorum',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='voluptate',
                ),
            ],
            pos=shared.TermUpdatePos.ADVERB,
            tags=[
                shared.TermTagCreate(
                    tag='omnis',
                ),
                shared.TermTagCreate(
                    tag='necessitatibus',
                ),
                shared.TermTagCreate(
                    tag='distinctio',
                ),
            ],
            term='asperiores',
            type=shared.TermUpdateType.BANNED,
        ),
        shared.TermUpdate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='ipsum',
            examples=[
                shared.TermExampleCreate(
                    example='id',
                    type=shared.TermExampleCreateType.BAD,
                ),
                shared.TermExampleCreate(
                    example='eius',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            highlight=False,
            id=20651,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=758379,
                    reference='accusamus',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='saepe',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='deserunt',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='provident',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='repellendus',
                ),
            ],
            pos=shared.TermUpdatePos.ADVERB,
            tags=[
                shared.TermTagCreate(
                    tag='alias',
                ),
                shared.TermTagCreate(
                    tag='at',
                ),
                shared.TermTagCreate(
                    tag='quaerat',
                ),
            ],
            term='tempora',
            type=shared.TermUpdateType.BANNED,
        ),
    ],
), 798047, 'officiis', 185636)

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

