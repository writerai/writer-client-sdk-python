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


res = s.co_write.generate_content(shared.GenerateTemplateRequest(
    inputs=[
        shared.MagicRequestInput(
            name='Doug Hoppe',
            value=[
                'ipsa',
                'delectus',
                'tempora',
                'suscipit',
            ],
        ),
        shared.MagicRequestInput(
            name='Alexandra Schulist',
            value=[
                'nisi',
                'recusandae',
                'temporibus',
            ],
        ),
    ],
    template_id='ab',
), 337396, 87129)

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
    organization_id=648172,
)


res = s.co_write.list_templates(20218, 'ipsam', 832620)

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

