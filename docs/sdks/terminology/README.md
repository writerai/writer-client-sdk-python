# Terminology
(*terminology*)

## Overview

Methods related to Terminology

### Available Operations

* [add](#add) - Add terms
* [delete](#delete) - Delete terms
* [find](#find) - Find terms
* [update](#update) - Update terms

## add

Add terms

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=551477,
)


res = s.terminology.add(create_terms_request=writer.CreateTermsRequest(), team_id=823436, organization_id=554561)

if res.create_terms_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `create_terms_request`                                          | [models.CreateTermsRequest](../../models/createtermsrequest.md) | :heavy_check_mark:                                              | N/A                                                             |
| `team_id`                                                       | *int*                                                           | :heavy_check_mark:                                              | N/A                                                             |
| `organization_id`                                               | *Optional[int]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |


### Response

**[models.AddTermsResponse](../../models/addtermsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## delete

Delete terms

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=545907,
)


res = s.terminology.delete(team_id=841399, x_request_id='<value>', ids=[
    698486,
], organization_id=557937)

if res.delete_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `team_id`          | *int*              | :heavy_check_mark: | N/A                |
| `x_request_id`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `ids`              | List[*int*]        | :heavy_minus_sign: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[models.DeleteTermsResponse](../../models/deletetermsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## find

Find terms

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=40141,
)

req = writer.FindTermsRequest(
    team_id=326883,
)

res = s.terminology.find(req)

if res.paginated_result_full_term_with_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [models.FindTermsRequest](../../models/findtermsrequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |


### Response

**[models.FindTermsResponse](../../models/findtermsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## update

Update terms

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=857478,
)


res = s.terminology.update(update_terms_request=writer.UpdateTermsRequest(), team_id=24555, x_request_id='<value>', organization_id=597129)

if res.create_terms_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `update_terms_request`                                          | [models.UpdateTermsRequest](../../models/updatetermsrequest.md) | :heavy_check_mark:                                              | N/A                                                             |
| `team_id`                                                       | *int*                                                           | :heavy_check_mark:                                              | N/A                                                             |
| `x_request_id`                                                  | *Optional[str]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |
| `organization_id`                                               | *Optional[int]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |


### Response

**[models.UpdateTermsResponse](../../models/updatetermsresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |
