# CoWrite
(*co_write*)

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

s = writer.Writer(
    api_key="",
    organization_id=569932,
)


res = s.co_write.generate_content(generate_template_request=writer.GenerateTemplateRequest(
    inputs=[
        writer.MagicRequestInput(
            name='string',
            value=[
                'string',
            ],
        ),
    ],
    template_id='string',
), team_id=888452, organization_id=926220)

if res.draft is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `generate_template_request`                                            | [models.GenerateTemplateRequest](../models/generatetemplaterequest.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `team_id`                                                              | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `organization_id`                                                      | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |


### Response

**[models.GenerateContentResponse](../../models/generatecontentresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.FailResponseError | 400,401,403,404,500      | application/json         |
| models.SDKError          | 400-600                  | */*                      |

## list_templates

Get a list of your existing CoWrite templates

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="",
    organization_id=380445,
)


res = s.co_write.list_templates(team_id=882866, template_id='string', organization_id=55511)

if res.template_details_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *int*              | :heavy_check_mark: | N/A                |
| `template_id`      | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[models.ListTemplatesResponse](../../models/listtemplatesresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.FailResponseError | 400,401,403,404,500      | application/json         |
| models.SDKError          | 400-600                  | */*                      |
