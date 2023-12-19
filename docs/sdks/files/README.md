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

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
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

**[models.DeleteFileResponse](../../models/deletefileresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## get

Get file

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
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

**[models.GetFileResponse](../../models/getfileresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## list

List files

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
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

**[models.ListFilesResponse](../../models/listfilesresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |

## upload

Upload file

### Example Usage

```python
import writer

s = writer.Writer(
    api_key="<YOUR_API_KEY_HERE>",
    organization_id=403654,
)


res = s.files.upload(upload_model_file_request=writer.UploadModelFileRequest(
    file=writer.File(
        content='0x7cbca97eC6'.encode(),
        file_name='plastic_cli.gif',
    ),
), organization_id=360896)

if res.model_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `upload_model_file_request`                                             | [models.UploadModelFileRequest](../../models/uploadmodelfilerequest.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `organization_id`                                                       | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |


### Response

**[models.UploadFileResponse](../../models/uploadfileresponse.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.FailResponse | 400,401,403,404,500 | application/json    |
| models.SDKError     | 4x-5xx              | */*                 |
