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
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=998848,
)

req = operations.AddTermsRequest(
    create_terms_request=shared.CreateTermsRequest(
        fail_handling=shared.CreateTermsRequestFailHandling.VALIDATE_ONLY,
        models=[
            shared.TermCreate(
                approved_term_extension=shared.ApprovedTermExtensionCreate(
                    capitalize=False,
                    fix_case=False,
                    fix_common_mistakes=False,
                ),
                case_sensitive=False,
                description='saepe',
                examples=[
                    shared.TermExampleCreate(
                        example='accusantium',
                        type=shared.TermExampleCreateType.GOOD,
                    ),
                    shared.TermExampleCreate(
                        example='praesentium',
                        type=shared.TermExampleCreateType.BAD,
                    ),
                    shared.TermExampleCreate(
                        example='magni',
                        type=shared.TermExampleCreateType.GOOD,
                    ),
                    shared.TermExampleCreate(
                        example='quo',
                        type=shared.TermExampleCreateType.BAD,
                    ),
                ],
                highlight=False,
                linked_terms=[
                    shared.LinkedTermCreate(
                        linked_term_id=807319,
                        reference='ea',
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=569101,
                        reference='odit',
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=407183,
                        reference='accusantium',
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=69167,
                        reference='maiores',
                    ),
                ],
                mistakes=[
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake='ipsam',
                        pos=shared.TermMistakeCreatePos.VERB,
                        reference='autem',
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake='nam',
                        pos=shared.TermMistakeCreatePos.NOUN,
                        reference='pariatur',
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake='nemo',
                        pos=shared.TermMistakeCreatePos.ADJECTIVE,
                        reference='perferendis',
                    ),
                ],
                pos=shared.TermCreatePos.ADJECTIVE,
                reference='amet',
                tags=[
                    shared.TermTagCreate(
                        tag='cumque',
                    ),
                ],
                term='corporis',
                type=shared.TermCreateType.PENDING,
            ),
        ],
    ),
    team_id=729991,
)

res = s.terminology.add(req)

if res.create_terms_response is not None:
    # handle response
```

## delete

Delete terms

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=749999,
)

req = operations.DeleteTermsRequest(
    x_request_id='dolores',
    ids=[
        521037,
        489549,
    ],
    team_id=54338,
)

res = s.terminology.delete(req)

if res.delete_response is not None:
    # handle response
```

## find

Find terms

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=338985,
)

req = operations.FindTermsRequest(
    limit=199996,
    offset=179490,
    part_of_speech=operations.FindTermsPartOfSpeech.NOUN,
    sort_field=operations.FindTermsSortField.TERM,
    sort_order=operations.FindTermsSortOrder.DESC,
    tags=[
        'dolor',
        'vero',
    ],
    team_id=345352,
    term='hic',
    type=operations.FindTermsType.PENDING,
)

res = s.terminology.find(req)

if res.paginated_result_full_term_with_user is not None:
    # handle response
```

## update

Update terms

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=608253,
)

req = operations.UpdateTermsRequest(
    update_terms_request=shared.UpdateTermsRequest(
        fail_handling=shared.UpdateTermsRequestFailHandling.SKIP,
        models=[
            shared.TermUpdate(
                approved_term_extension=shared.ApprovedTermExtensionCreate(
                    capitalize=False,
                    fix_case=False,
                    fix_common_mistakes=False,
                ),
                case_sensitive=False,
                description='voluptatem',
                examples=[
                    shared.TermExampleCreate(
                        example='consequuntur',
                        type=shared.TermExampleCreateType.BAD,
                    ),
                    shared.TermExampleCreate(
                        example='error',
                        type=shared.TermExampleCreateType.GOOD,
                    ),
                    shared.TermExampleCreate(
                        example='occaecati',
                        type=shared.TermExampleCreateType.BAD,
                    ),
                    shared.TermExampleCreate(
                        example='adipisci',
                        type=shared.TermExampleCreateType.BAD,
                    ),
                ],
                highlight=False,
                id=934214,
                linked_terms=[
                    shared.LinkedTermCreate(
                        linked_term_id=613966,
                        reference='dolorum',
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=535633,
                        reference='pariatur',
                    ),
                ],
                mistakes=[
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake='nobis',
                        pos=shared.TermMistakeCreatePos.ADVERB,
                        reference='delectus',
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake='quaerat',
                        pos=shared.TermMistakeCreatePos.ADVERB,
                        reference='aliquid',
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake='dolorem',
                        pos=shared.TermMistakeCreatePos.NOUN,
                        reference='dolor',
                    ),
                ],
                pos=shared.TermUpdatePos.NOUN,
                tags=[
                    shared.TermTagCreate(
                        tag='hic',
                    ),
                ],
                term='excepturi',
                type=shared.TermUpdateType.PENDING,
            ),
            shared.TermUpdate(
                approved_term_extension=shared.ApprovedTermExtensionCreate(
                    capitalize=False,
                    fix_case=False,
                    fix_common_mistakes=False,
                ),
                case_sensitive=False,
                description='voluptate',
                examples=[
                    shared.TermExampleCreate(
                        example='reiciendis',
                        type=shared.TermExampleCreateType.GOOD,
                    ),
                    shared.TermExampleCreate(
                        example='dolorum',
                        type=shared.TermExampleCreateType.GOOD,
                    ),
                ],
                highlight=False,
                id=85295,
                linked_terms=[
                    shared.LinkedTermCreate(
                        linked_term_id=56418,
                        reference='iure',
                    ),
                ],
                mistakes=[
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake='quaerat',
                        pos=shared.TermMistakeCreatePos.ADJECTIVE,
                        reference='quidem',
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake='voluptatibus',
                        pos=shared.TermMistakeCreatePos.VERB,
                        reference='natus',
                    ),
                ],
                pos=shared.TermUpdatePos.NOUN,
                tags=[
                    shared.TermTagCreate(
                        tag='sit',
                    ),
                    shared.TermTagCreate(
                        tag='fugiat',
                    ),
                    shared.TermTagCreate(
                        tag='ab',
                    ),
                ],
                term='soluta',
                type=shared.TermUpdateType.PENDING,
            ),
            shared.TermUpdate(
                approved_term_extension=shared.ApprovedTermExtensionCreate(
                    capitalize=False,
                    fix_case=False,
                    fix_common_mistakes=False,
                ),
                case_sensitive=False,
                description='iusto',
                examples=[
                    shared.TermExampleCreate(
                        example='dolorum',
                        type=shared.TermExampleCreateType.BAD,
                    ),
                    shared.TermExampleCreate(
                        example='omnis',
                        type=shared.TermExampleCreateType.BAD,
                    ),
                ],
                highlight=False,
                id=714697,
                linked_terms=[
                    shared.LinkedTermCreate(
                        linked_term_id=469497,
                        reference='ipsum',
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=456015,
                        reference='id',
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=906418,
                        reference='eius',
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=137220,
                        reference='perferendis',
                    ),
                ],
                mistakes=[
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake='optio',
                        pos=shared.TermMistakeCreatePos.ADJECTIVE,
                        reference='ad',
                    ),
                ],
                pos=shared.TermUpdatePos.ADJECTIVE,
                tags=[
                    shared.TermTagCreate(
                        tag='deserunt',
                    ),
                    shared.TermTagCreate(
                        tag='provident',
                    ),
                ],
                term='minima',
                type=shared.TermUpdateType.PENDING,
            ),
        ],
    ),
    x_request_id='totam',
    team_id=628982,
)

res = s.terminology.update(req)

if res.create_terms_response is not None:
    # handle response
```
