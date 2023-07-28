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
    organization_id=301575,
)


res = s.terminology.add(create_terms_request=shared.CreateTermsRequest(
    fail_handling=shared.CreateTermsRequestFailHandling.SKIP,
    models=[
        shared.TermCreate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='labore',
            examples=[
                shared.TermExampleCreate(
                    example='suscipit',
                    type=shared.TermExampleCreateType.BAD,
                ),
                shared.TermExampleCreate(
                    example='nobis',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            highlight=False,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=135474,
                    reference='architecto',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=298282,
                    reference='et',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=569965,
                    reference='ullam',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=590873,
                    reference='quos',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='accusantium',
                    pos=shared.TermMistakeCreatePos.ADVERB,
                    reference='reiciendis',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='mollitia',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='eum',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='dolor',
                    pos=shared.TermMistakeCreatePos.ADJECTIVE,
                    reference='odit',
                ),
            ],
            pos=shared.TermCreatePos.VERB,
            reference='quasi',
            tags=[
                shared.TermTagCreate(
                    tag='doloribus',
                ),
                shared.TermTagCreate(
                    tag='debitis',
                ),
            ],
            term='eius',
            type=shared.TermCreateType.PENDING,
        ),
        shared.TermCreate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='deleniti',
            examples=[
                shared.TermExampleCreate(
                    example='in',
                    type=shared.TermExampleCreateType.GOOD,
                ),
                shared.TermExampleCreate(
                    example='architecto',
                    type=shared.TermExampleCreateType.BAD,
                ),
                shared.TermExampleCreate(
                    example='ullam',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            highlight=False,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=998848,
                    reference='quibusdam',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=149448,
                    reference='saepe',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='accusantium',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='praesentium',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='natus',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='sunt',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='quo',
                    pos=shared.TermMistakeCreatePos.ADJECTIVE,
                    reference='pariatur',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='maxime',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='excepturi',
                ),
            ],
            pos=shared.TermCreatePos.NOUN,
            reference='ea',
            tags=[
                shared.TermTagCreate(
                    tag='ab',
                ),
            ],
            term='maiores',
            type=shared.TermCreateType.PENDING,
        ),
        shared.TermCreate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='ipsam',
            examples=[
                shared.TermExampleCreate(
                    example='autem',
                    type=shared.TermExampleCreateType.BAD,
                ),
                shared.TermExampleCreate(
                    example='eaque',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            highlight=False,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=975522,
                    reference='perferendis',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=855804,
                    reference='amet',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='cumque',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='hic',
                ),
            ],
            pos=shared.TermCreatePos.ADVERB,
            reference='nobis',
            tags=[
                shared.TermTagCreate(
                    tag='quis',
                ),
            ],
            term='totam',
            type=shared.TermCreateType.BANNED,
        ),
    ],
), team_id=54338, organization_id=338985)

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
    organization_id=199996,
)


res = s.terminology.delete(team_id=179490, x_request_id='perferendis', ids=[
    793698,
], organization_id=463451)

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
    organization_id=223924,
)

req = operations.FindTermsRequest(
    limit=874573,
    offset=345352,
    part_of_speech=operations.FindTermsPartOfSpeech.ADJECTIVE,
    sort_field=operations.FindTermsSortField.TYPE,
    sort_order=operations.FindTermsSortOrder.DESC,
    tags=[
        'perspiciatis',
        'voluptatem',
        'porro',
    ],
    team_id=164694,
    term='blanditiis',
    type=operations.FindTermsType.BANNED,
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
    organization_id=50370,
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
            description='adipisci',
            examples=[
                shared.TermExampleCreate(
                    example='earum',
                    type=shared.TermExampleCreateType.GOOD,
                ),
                shared.TermExampleCreate(
                    example='iste',
                    type=shared.TermExampleCreateType.BAD,
                ),
                shared.TermExampleCreate(
                    example='deleniti',
                    type=shared.TermExampleCreateType.BAD,
                ),
                shared.TermExampleCreate(
                    example='provident',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            highlight=False,
            id=730122,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=311945,
                    reference='quos',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=398221,
                    reference='dolorem',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=209843,
                    reference='dolor',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=186193,
                    reference='ipsum',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='excepturi',
                    pos=shared.TermMistakeCreatePos.ADVERB,
                    reference='voluptate',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='dignissimos',
                    pos=shared.TermMistakeCreatePos.ADJECTIVE,
                    reference='amet',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='dolorum',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='veritatis',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='ipsa',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='iure',
                ),
            ],
            pos=shared.TermUpdatePos.VERB,
            tags=[
                shared.TermTagCreate(
                    tag='accusamus',
                ),
                shared.TermTagCreate(
                    tag='quidem',
                ),
            ],
            term='voluptatibus',
            type=shared.TermUpdateType.BANNED,
        ),
        shared.TermUpdate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='natus',
            examples=[
                shared.TermExampleCreate(
                    example='atque',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            highlight=False,
            id=854614,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=743835,
                    reference='dolorum',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='voluptate',
                    pos=shared.TermMistakeCreatePos.ADVERB,
                    reference='deleniti',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='omnis',
                    pos=shared.TermMistakeCreatePos.ADJECTIVE,
                    reference='distinctio',
                ),
            ],
            pos=shared.TermUpdatePos.ADJECTIVE,
            tags=[
                shared.TermTagCreate(
                    tag='ipsum',
                ),
                shared.TermTagCreate(
                    tag='voluptate',
                ),
            ],
            term='id',
            type=shared.TermUpdateType.PENDING,
        ),
        shared.TermUpdate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='eius',
            examples=[
                shared.TermExampleCreate(
                    example='perferendis',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            highlight=False,
            id=758379,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=320017,
                    reference='saepe',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=383464,
                    reference='deserunt',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=588317,
                    reference='minima',
                ),
                shared.LinkedTermCreate(
                    linked_term_id=831049,
                    reference='totam',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='alias',
                    pos=shared.TermMistakeCreatePos.ADJECTIVE,
                    reference='quaerat',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='tempora',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='quod',
                ),
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='officiis',
                    pos=shared.TermMistakeCreatePos.NOUN,
                    reference='dolorum',
                ),
            ],
            pos=shared.TermUpdatePos.ADJECTIVE,
            tags=[
                shared.TermTagCreate(
                    tag='harum',
                ),
                shared.TermTagCreate(
                    tag='iusto',
                ),
            ],
            term='ipsum',
            type=shared.TermUpdateType.PENDING,
        ),
    ],
), team_id=947371, x_request_id='amet', organization_id=730856)

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

