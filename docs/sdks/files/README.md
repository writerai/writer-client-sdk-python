# Files
(*files*)

## Overview

Methods related to Files

### Available Operations

* [delete](#delete) - Delete file
* [get](#get) - Get file
* [list](#list) - List files
* [upload](#upload) - Upload file

## delete

Delete file

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    api_key="",
    organization_id=545907,
)


res = s.files.delete(file_id='string', organization_id=841399)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DeleteFileResponse](../../models/operations/deletefileresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |

## get

Get file

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    api_key="",
    organization_id=700347,
)


res = s.files.get(file_id='string', organization_id=90065)

if res.model_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetFileResponse](../../models/operations/getfileresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |

## list

List files

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    api_key="",
    organization_id=768578,
)


res = s.files.list(organization_id=99895)

if res.model_files_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.ListFilesResponse](../../models/operations/listfilesresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |

## upload

Upload file

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=403654,
)


res = s.files.upload(upload_model_file_request=shared.UploadModelFileRequest(
    file=shared.File(
        content='0x7cbca97eC6'.encode(),
        file_name='plastic_cli.gif',
    ),
), organization_id=360896)

if res.model_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `upload_model_file_request`                                                    | [shared.UploadModelFileRequest](../../models/shared/uploadmodelfilerequest.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `organization_id`                                                              | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |


### Response

**[operations.UploadFileResponse](../../models/operations/uploadfileresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.FailResponse | 400,401,403,404,500 | application/json    |
| errors.SDKError     | 400-600             | */*                 |
