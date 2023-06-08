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
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=613064,
)

req = operations.DeleteFileRequest(
    file_id='iure',
)

res = s.files.delete(req)

if res.delete_file_200_application_json_object is not None:
    # handle response
```

## get

Get file

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=902349,
)

req = operations.GetFileRequest(
    file_id='quidem',
)

res = s.files.get(req)

if res.model_file is not None:
    # handle response
```

## list

List files

### Example Usage

```python
import writer
from writer.models import operations

s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=99280,
)

req = operations.ListFilesRequest()

res = s.files.list(req)

if res.model_files_response is not None:
    # handle response
```

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
    organization_id=60225,
)

req = operations.UploadFileRequest(
    upload_model_file_request=shared.UploadModelFileRequest(
        file=shared.UploadModelFileRequestFile(
            content='reiciendis'.encode(),
            file='est',
        ),
    ),
)

res = s.files.upload(req)

if res.model_file is not None:
    # handle response
```
