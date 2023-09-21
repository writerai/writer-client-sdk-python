# Files

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
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=537373,
)


res = s.files.delete(file_id='hic', organization_id=758616)

if res.delete_file_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DeleteFileResponse](../../models/operations/deletefileresponse.md)**


## get

Get file

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=521848,
)


res = s.files.get(file_id='beatae', organization_id=414662)

if res.model_file is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetFileResponse](../../models/operations/getfileresponse.md)**


## list

List files

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=473600,
)


res = s.files.list(organization_id=264555)

if res.model_files_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `organization_id`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.ListFilesResponse](../../models/operations/listfilesresponse.md)**


## upload

Upload file

### Example Usage

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=186332,
)


res = s.files.upload(upload_model_file_request=shared.UploadModelFileRequest(
    file=shared.UploadModelFileRequestFile(
        content='impedit'.encode(),
        file='cum',
    ),
), organization_id=456150)

if res.model_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `upload_model_file_request`                                                    | [shared.UploadModelFileRequest](../../models/shared/uploadmodelfilerequest.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `organization_id`                                                              | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |


### Response

**[operations.UploadFileResponse](../../models/operations/uploadfileresponse.md)**

