# models

## Overview

Methods related to Model

### Available Operations

* [list](#list) - List available LLM models

## list

List available LLM models

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=653108,
)


req = operations.ListModelsRequest()

res = s.models.list(req)

if res.generation_models_response is not None:
    # handle response
```
