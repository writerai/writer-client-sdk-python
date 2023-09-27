# DownloadTheCustomizedModel
(*download_the_customized_model*)

## Overview

Methods related to Download the customized model

### Available Operations

* [fetch_file](#fetch_file) - Download your fine-tuned model (available only for Palmyra Base and Palmyra Large)

## fetch_file

Download your fine-tuned model (available only for Palmyra Base and Palmyra Large)

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=537373,
)


res = s.download_the_customized_model.fetch_file(customization_id='hic', model_id='optio', organization_id=521848)

if res.fetch_customized_model_file_200_application_octet_stream_binary_string is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `customization_id` | *str*              | :heavy_check_mark: | N/A                |
| `model_id`         | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.FetchCustomizedModelFileResponse](../../models/operations/fetchcustomizedmodelfileresponse.md)**

