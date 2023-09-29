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
    security=shared.Security(
        api_key="",
    ),
    organization_id=551477,
)


res = s.terminology.add(create_terms_request=shared.CreateTermsRequest(
    fail_handling=shared.CreateTermsRequestFailHandling.VALIDATE_ONLY,
    models=[
        shared.TermCreate(
            approved_term_extension=shared.ApprovedTermExtensionCreate(
                capitalize=False,
                fix_case=False,
                fix_common_mistakes=False,
            ),
            case_sensitive=False,
            description='Optional mobile secured line',
            examples=[
                shared.TermExampleCreate(
                    example='noon bypass Chief',
                    type=shared.TermExampleCreateType.GOOD,
                ),
            ],
            highlight=False,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=753323,
                    reference='Southeast',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='generating payment quantify',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='Urbandale Gasoline',
                ),
            ],
            pos=shared.TermCreatePos.ADVERB,
            reference='methodologies',
            tags=[
                shared.TermTagCreate(
                    tag='Northeast',
                ),
            ],
            term='Pomona auxiliary',
            type=shared.TermCreateType.BANNED,
        ),
    ],
), team_id=739517, organization_id=358325)

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
    security=shared.Security(
        api_key="",
    ),
    organization_id=40141,
)

req = operations.FindTermsRequest(
    limit=326883,
    offset=488098,
    part_of_speech=operations.FindTermsPartOfSpeech.ADJECTIVE,
    sort_field=operations.FindTermsSortField.TYPE,
    sort_order=operations.FindTermsSortOrder.ASC,
    tags=[
        'West',
    ],
    team_id=413686,
    term='Bike generating',
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
    organization_id=857478,
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
            description='Persistent 24/7 focus group',
            examples=[
                shared.TermExampleCreate(
                    example='dock Quality redundant',
                    type=shared.TermExampleCreateType.BAD,
                ),
            ],
            highlight=False,
            id=134151,
            linked_terms=[
                shared.LinkedTermCreate(
                    linked_term_id=54062,
                    reference='mostly',
                ),
            ],
            mistakes=[
                shared.TermMistakeCreate(
                    case_sensitive=False,
                    mistake='dynamic white',
                    pos=shared.TermMistakeCreatePos.VERB,
                    reference='Forward',
                ),
            ],
            pos=shared.TermUpdatePos.ADJECTIVE,
            tags=[
                shared.TermTagCreate(
                    tag='East Baht Quality',
                ),
            ],
            term='Home users Sharable',
            type=shared.TermUpdateType.BANNED,
        ),
    ],
), team_id=439152, x_request_id='Northeast', organization_id=481319)

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

