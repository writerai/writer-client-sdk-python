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
    organization_id=844266,
)


res = s.ai_content_detector.detect(shared.ContentDetectorRequest(
    input='unde',
), 857946)

if res.content_detector_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `content_detector_request`                                                     | [shared.ContentDetectorRequest](../../models/shared/contentdetectorrequest.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `organization_id`                                                              | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |


### Response

**[operations.DetectContentResponse](../../models/operations/detectcontentresponse.md)**

