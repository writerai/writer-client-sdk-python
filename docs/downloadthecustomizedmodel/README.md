# download_the_customized_model

## Overview

Methods related to Download the customized model

### Available Operations

* [fetch_file](#fetch_file) - Download your fine-tuned model (available only for Palmyra Base and Palmyra Large)

## fetch_file

Download your fine-tuned model (available only for Palmyra Base and Palmyra Large)

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=681820,
)

req = operations.FetchCustomizedModelFileRequest(
    customization_id='in',
    model_id='corporis',
)

res = s.download_the_customized_model.fetch_file(req)

if res.fetch_customized_model_file_200_application_octet_stream_binary_string is not None:
    # handle response
```
