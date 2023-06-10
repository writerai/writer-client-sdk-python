# ai_content_detector

## Overview

Methods related to AI Content Detector

### Available Operations

* [detect](#detect) - Content detector api

## detect

Content detector api

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=715190,
)

req = operations.DetectContentRequest(
    content_detector_request=shared.ContentDetectorRequest(
        input='quibusdam',
    ),
)

res = s.ai_content_detector.detect(req)

if res.content_detector_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DetectContentRequest](../../models/operations/detectcontentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DetectContentResponse](../../models/operations/detectcontentresponse.md)**

