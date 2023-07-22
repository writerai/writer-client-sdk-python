# files

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
    organization_id=617636,
)


res = s.files.delete('sed', 612096)

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
    organization_id=222321,
)


res = s.files.get('natus', 386489)

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
    organization_id=943749,
)


res = s.files.list(902599)

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
    organization_id=681820,
)


res = s.files.upload(shared.UploadModelFileRequest(
    file=shared.UploadModelFileRequestFile(
        content='in'.encode(),
        file='corporis',
    ),
), 613064)

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

