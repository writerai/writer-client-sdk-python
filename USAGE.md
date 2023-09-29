<!-- Start SDK Example Usage -->


```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=496531,
)


res = s.ai_content_detector.detect(content_detector_request=shared.ContentDetectorRequest(
    input='Bronze Indian',
), organization_id=558689)

if res.content_detector_responses is not None:
    # handle response
```
<!-- End SDK Example Usage -->