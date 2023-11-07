# Billing
(*.billing*)

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
    api_key="",
    organization_id=850421,
)


res = s.billing.get_subscription_details()

if res.subscription_public_response_api is not None:
    # handle response
    pass
```


### Response

**[operations.GetSubscriptionDetailsResponse](../../models/operations/getsubscriptiondetailsresponse.md)**

