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

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=501762,
)


res = s.download_the_customized_model.fetch_file(customization_id='<value>', model_id='<value>', organization_id=948692)

if res.stream is not None:
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

**[models.FetchCustomizedModelFileResponse](../../models/fetchcustomizedmodelfileresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |
