# Content
(*content*)

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

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=935464,
)


res = s.content.check(content_request=writer.ContentRequest(
    content='<value>',
    settings=writer.ContentSettings(
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
), team_id=38270, organization_id=919579)

if res.processed_content is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `content_request`                                       | [models.ContentRequest](../../models/contentrequest.md) | :heavy_check_mark:                                      | N/A                                                     |
| `team_id`                                               | *int*                                                   | :heavy_check_mark:                                      | N/A                                                     |
| `organization_id`                                       | *Optional[int]*                                         | :heavy_minus_sign:                                      | N/A                                                     |


### Response

**[models.ContentCheckResponse](../../models/contentcheckresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## correct

Apply the style guide suggestions directly to your content.

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=501355,
)


res = s.content.correct(content_request=writer.ContentRequest(
    content='<value>',
    settings=writer.ContentSettings(
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
), team_id=31310, x_request_id='<value>', organization_id=383223)

if res.correction_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `content_request`                                       | [models.ContentRequest](../../models/contentrequest.md) | :heavy_check_mark:                                      | N/A                                                     |
| `team_id`                                               | *int*                                                   | :heavy_check_mark:                                      | N/A                                                     |
| `x_request_id`                                          | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `organization_id`                                       | *Optional[int]*                                         | :heavy_minus_sign:                                      | N/A                                                     |


### Response

**[models.ContentCorrectResponse](../../models/contentcorrectresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |
