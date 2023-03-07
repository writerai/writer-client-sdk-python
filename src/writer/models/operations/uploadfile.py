from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import modelfile as shared_modelfile
from ..shared import uploadmodelfilerequest as shared_uploadmodelfilerequest
from typing import Optional


@dataclasses.dataclass
class UploadFilePathParams:
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UploadFileHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UploadFileRequest:
    headers: UploadFileHeaders = dataclasses.field()
    path_params: UploadFilePathParams = dataclasses.field()
    request: shared_uploadmodelfilerequest.UploadModelFileRequest = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class UploadFileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    model_file: Optional[shared_modelfile.ModelFile] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    