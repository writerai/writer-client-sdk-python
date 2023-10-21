<!-- Start SDK Example Usage -->


```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=496531,
)


res = s.ai_content_detector.detect(content_detector_request=shared.ContentDetectorRequest(
    input='string',
), organization_id=592237)

if res.content_detector_responses is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->