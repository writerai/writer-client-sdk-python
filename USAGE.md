<!-- Start SDK Example Usage -->
```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=548814,
)


req = operations.DetectContentRequest(
    content_detector_request=shared.ContentDetectorRequest(
        input="provident",
    ),
)
    
res = s.ai_content_detector.detect(req)

if res.content_detector_responses is not None:
    # handle response
```
<!-- End SDK Example Usage -->