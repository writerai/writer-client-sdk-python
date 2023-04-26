# billing

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
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=602763,
)


res = s.billing.get_subscription_details()

if res.subscription_public_response_api is not None:
    # handle response
```
