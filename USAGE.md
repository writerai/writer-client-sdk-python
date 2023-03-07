<!-- Start SDK Example Usage -->
```python
import writer
from writer.models import operations, shared

s = writer.Writer()
   
req = operations.ContentDetectorAPIRequest(
    path_params=operations.ContentDetectorAPIPathParams(
        organization_id=548814,
    ),
    headers=operations.ContentDetectorAPIHeaders(
        authorization="deserunt",
    ),
    request=shared.ContentDetectorRequest(
        input="porro",
    ),
)
    
res = s.ai_content_detector.content_detector_api(req)

if res.content_detector_responses is not None:
    # handle response
```
<!-- End SDK Example Usage -->