# co_write

## Overview

Methods related to CoWrite

### Available Operations

* [generate_content](#generate_content) - Generate content using predefined templates
* [list_templates](#list_templates) - Get a list of your existing CoWrite templates

## generate_content

Generate content using predefined templates

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=847252,
)


res = s.co_write.generate_content(generate_template_request=shared.GenerateTemplateRequest(
    inputs=[
        shared.MagicRequestInput(
            name='Sabrina Oberbrunner',
            value=[
                'magnam',
            ],
        ),
    ],
    template_id='debitis',
), team_id=56713, organization_id=963663)

if res.draft is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `generate_template_request`                                                      | [shared.GenerateTemplateRequest](../../models/shared/generatetemplaterequest.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `team_id`                                                                        | *int*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `organization_id`                                                                | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | N/A                                                                              |


### Response

**[operations.GenerateContentResponse](../../models/operations/generatecontentresponse.md)**


## list_templates

Get a list of your existing CoWrite templates

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=272656,
)


res = s.co_write.list_templates(team_id=383441, template_id='molestiae', organization_id=791725)

if res.template_details_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *int*              | :heavy_check_mark: | N/A                |
| `template_id`      | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.ListTemplatesResponse](../../models/operations/listtemplatesresponse.md)**

