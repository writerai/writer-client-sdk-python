# content

## Overview

Methods related to Content

### Available Operations

* [check](#check) - Check your content against your preset styleguide.
* [correct](#correct) - Apply the style guide suggestions directly to your content.

## check

Check your content against your preset styleguide.

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=18789,
)


res = s.content.check(shared.ContentRequest(
    content='ad',
    settings=shared.ContentSettings(
        age_and_family_status=False,
        confidence=False,
        content_safeguards=False,
        disability=False,
        gender_identity_sensitivity=False,
        gender_inclusive_nouns=False,
        gender_inclusive_pronouns=False,
        grammar=False,
        healthy_communication=False,
        passive_voice=False,
        race_ethnicity_nationality_sensitivity=False,
        sexual_orientation_sensitivity=False,
        spelling=False,
        substance_use_sensitivity=False,
        unclear_reference=False,
        wordiness=False,
    ),
), 617636, 149675)

if res.processed_content is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `content_request`                                              | [shared.ContentRequest](../../models/shared/contentrequest.md) | :heavy_check_mark:                                             | N/A                                                            |
| `team_id`                                                      | *int*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `organization_id`                                              | *Optional[int]*                                                | :heavy_minus_sign:                                             | N/A                                                            |


### Response

**[operations.ContentCheckResponse](../../models/operations/contentcheckresponse.md)**


## correct

Apply the style guide suggestions directly to your content.

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=612096,
)


res = s.content.correct(shared.ContentRequest(
    content='dolor',
    settings=shared.ContentSettings(
        age_and_family_status=False,
        confidence=False,
        content_safeguards=False,
        disability=False,
        gender_identity_sensitivity=False,
        gender_inclusive_nouns=False,
        gender_inclusive_pronouns=False,
        grammar=False,
        healthy_communication=False,
        passive_voice=False,
        race_ethnicity_nationality_sensitivity=False,
        sexual_orientation_sensitivity=False,
        spelling=False,
        substance_use_sensitivity=False,
        unclear_reference=False,
        wordiness=False,
    ),
), 616934, 'laboriosam', 943749)

if res.correction_response is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `content_request`                                              | [shared.ContentRequest](../../models/shared/contentrequest.md) | :heavy_check_mark:                                             | N/A                                                            |
| `team_id`                                                      | *int*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `x_request_id`                                                 | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `organization_id`                                              | *Optional[int]*                                                | :heavy_minus_sign:                                             | N/A                                                            |


### Response

**[operations.ContentCorrectResponse](../../models/operations/contentcorrectresponse.md)**

