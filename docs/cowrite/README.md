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
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=857946,
)


req = operations.GenerateContentRequest(
    generate_template_request=shared.GenerateTemplateRequest(
        inputs=[
            shared.MagicRequestInput(
                name="Ben Mueller",
                value=[
                    "magnam",
                    "debitis",
                ],
            ),
            shared.MagicRequestInput(
                name="Lucia Goldner",
                value=[
                    "placeat",
                    "voluptatum",
                    "iusto",
                    "excepturi",
                ],
            ),
            shared.MagicRequestInput(
                name="Mrs. Sophie Smith MD",
                value=[
                    "ipsam",
                ],
            ),
        ],
        template_id="repellendus",
    ),
    team_id=957156,
)

res = s.co_write.generate_content(req)

if res.draft is not None:
    # handle response
```

## list_templates

Get a list of your existing CoWrite templates

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=778157,
)


req = operations.ListTemplatesRequest(
    team_id=140350,
    template_id="at",
)

res = s.co_write.list_templates(req)

if res.template_details_response is not None:
    # handle response
```
