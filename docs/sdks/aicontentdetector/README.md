# AIContentDetector
(*ai_content_detector*)

## Overview

Methods related to AI Content Detector

### Available Operations

* [detect](#detect) - Content detector api

## detect

Content detector api

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=496531,
)


res = s.ai_content_detector.detect(content_detector_request=writer.ContentDetectorRequest(
    input='<value>',
), organization_id=592237)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `content_detector_request`                                              | [models.ContentDetectorRequest](../../models/contentdetectorrequest.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `organization_id`                                                       | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |


### Response

**[models.DetectContentResponse](../../models/detectcontentresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |
