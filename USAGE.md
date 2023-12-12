<!-- Start SDK Example Usage [usage] -->
```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=850421,
)


res = s.billing.get_subscription_details()

if res.subscription_public_response_api is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->