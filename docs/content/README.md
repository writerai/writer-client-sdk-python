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
    organization_id=149675,
)

req = operations.ContentCheckRequest(
    content_request=shared.ContentRequest(
        content='iste',
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
    ),
    team_id=222321,
)

res = s.content.check(req)

if res.processed_content is not None:
    # handle response
```

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
    organization_id=616934,
)

req = operations.ContentCorrectRequest(
    content_request=shared.ContentRequest(
        content='laboriosam',
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
    ),
    x_request_id='hic',
    team_id=902599,
)

res = s.content.correct(req)

if res.correction_response is not None:
    # handle response
```
