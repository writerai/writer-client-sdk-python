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
        fail_handling="validateOnly",
        models=[
            shared.TermCreate(
                approved_term_extension=shared.ApprovedTermExtensionCreate(
                    capitalize=False,
                    fix_case=False,
                    fix_common_mistakes=False,
                ),
                case_sensitive=False,
                description="saepe",
                examples=[
                    shared.TermExampleCreate(
                        example="accusantium",
                        type="good",
                    ),
                    shared.TermExampleCreate(
                        example="praesentium",
                        type="bad",
                    ),
                    shared.TermExampleCreate(
                        example="magni",
                        type="good",
                    ),
                    shared.TermExampleCreate(
                        example="quo",
                        type="bad",
                    ),
                ],
                highlight=False,
                linked_terms=[
                    shared.LinkedTermCreate(
                        linked_term_id=807319,
                        reference="ea",
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=569101,
                        reference="odit",
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=407183,
                        reference="accusantium",
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=69167,
                        reference="maiores",
                    ),
                ],
                mistakes=[
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake="ipsam",
                        pos="verb",
                        reference="autem",
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake="nam",
                        pos="noun",
                        reference="pariatur",
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake="nemo",
                        pos="adjective",
                        reference="perferendis",
                    ),
                ],
                pos="adjective",
                reference="amet",
                tags=[
                    shared.TermTagCreate(
                        tag="cumque",
                    ),
                ],
                term="corporis",
                type="pending",
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
    x_request_id="dolores",
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
    part_of_speech="noun",
    sort_field="term",
    sort_order="desc",
    tags=[
        "dolor",
        "vero",
    ],
    team_id=345352,
    term="hic",
    type="pending",
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
        fail_handling="skip",
        models=[
            shared.TermUpdate(
                approved_term_extension=shared.ApprovedTermExtensionCreate(
                    capitalize=False,
                    fix_case=False,
                    fix_common_mistakes=False,
                ),
                case_sensitive=False,
                description="voluptatem",
                examples=[
                    shared.TermExampleCreate(
                        example="consequuntur",
                        type="bad",
                    ),
                    shared.TermExampleCreate(
                        example="error",
                        type="good",
                    ),
                    shared.TermExampleCreate(
                        example="occaecati",
                        type="bad",
                    ),
                    shared.TermExampleCreate(
                        example="adipisci",
                        type="bad",
                    ),
                ],
                highlight=False,
                id=934214,
                linked_terms=[
                    shared.LinkedTermCreate(
                        linked_term_id=613966,
                        reference="dolorum",
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=535633,
                        reference="pariatur",
                    ),
                ],
                mistakes=[
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake="nobis",
                        pos="adverb",
                        reference="delectus",
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake="quaerat",
                        pos="adverb",
                        reference="aliquid",
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake="dolorem",
                        pos="noun",
                        reference="dolor",
                    ),
                ],
                pos="noun",
                tags=[
                    shared.TermTagCreate(
                        tag="hic",
                    ),
                ],
                term="excepturi",
                type="pending",
            ),
            shared.TermUpdate(
                approved_term_extension=shared.ApprovedTermExtensionCreate(
                    capitalize=False,
                    fix_case=False,
                    fix_common_mistakes=False,
                ),
                case_sensitive=False,
                description="voluptate",
                examples=[
                    shared.TermExampleCreate(
                        example="reiciendis",
                        type="good",
                    ),
                    shared.TermExampleCreate(
                        example="dolorum",
                        type="good",
                    ),
                ],
                highlight=False,
                id=85295,
                linked_terms=[
                    shared.LinkedTermCreate(
                        linked_term_id=56418,
                        reference="iure",
                    ),
                ],
                mistakes=[
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake="quaerat",
                        pos="adjective",
                        reference="quidem",
                    ),
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake="voluptatibus",
                        pos="verb",
                        reference="natus",
                    ),
                ],
                pos="noun",
                tags=[
                    shared.TermTagCreate(
                        tag="sit",
                    ),
                    shared.TermTagCreate(
                        tag="fugiat",
                    ),
                    shared.TermTagCreate(
                        tag="ab",
                    ),
                ],
                term="soluta",
                type="pending",
            ),
            shared.TermUpdate(
                approved_term_extension=shared.ApprovedTermExtensionCreate(
                    capitalize=False,
                    fix_case=False,
                    fix_common_mistakes=False,
                ),
                case_sensitive=False,
                description="iusto",
                examples=[
                    shared.TermExampleCreate(
                        example="dolorum",
                        type="bad",
                    ),
                    shared.TermExampleCreate(
                        example="omnis",
                        type="bad",
                    ),
                ],
                highlight=False,
                id=714697,
                linked_terms=[
                    shared.LinkedTermCreate(
                        linked_term_id=469497,
                        reference="ipsum",
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=456015,
                        reference="id",
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=906418,
                        reference="eius",
                    ),
                    shared.LinkedTermCreate(
                        linked_term_id=137220,
                        reference="perferendis",
                    ),
                ],
                mistakes=[
                    shared.TermMistakeCreate(
                        case_sensitive=False,
                        mistake="optio",
                        pos="adjective",
                        reference="ad",
                    ),
                ],
                pos="adjective",
                tags=[
                    shared.TermTagCreate(
                        tag="deserunt",
                    ),
                    shared.TermTagCreate(
                        tag="provident",
                    ),
                ],
                term="minima",
                type="pending",
            ),
        ],
    ),
    x_request_id="totam",
    team_id=628982,
)

res = s.terminology.update(req)

if res.create_terms_response is not None:
    # handle response
```
