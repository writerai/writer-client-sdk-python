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
    api_key="",
    organization_id=501762,
)


res = s.download_the_customized_model.fetch_file(customization_id='apology', model_id='Silver', organization_id=432823)

if res.fetch_customized_model_file_200_application_octet_stream_binary_string is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `customization_id` | *str*              | :heavy_check_mark: | N/A                |
| `model_id`         | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.FetchCustomizedModelFileResponse](../../models/operations/fetchcustomizedmodelfileresponse.md)**

