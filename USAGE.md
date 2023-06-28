<!-- Start SDK Example Usage -->
```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=548814,
)


res = s.ai_content_detector.detect(shared.ContentDetectorRequest(
    input='provident',
), 715190)

if res.content_detector_responses is not None:
    # handle response
```
<!-- End SDK Example Usage -->