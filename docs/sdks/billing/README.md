# Billing
(*billing*)

## Overview

Methods related to Billing

### Available Operations

* [get_subscription_details](#get_subscription_details) - Get your organization subscription details

## get_subscription_details

Get your organization subscription details

### Example Usage

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


### Response

**[models.GetSubscriptionDetailsResponse](../../models/getsubscriptiondetailsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |
