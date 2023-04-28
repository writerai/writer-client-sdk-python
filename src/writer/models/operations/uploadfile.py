"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import modelfile as shared_modelfile
from ..shared import uploadmodelfilerequest as shared_uploadmodelfilerequest
from typing import Optional


@dataclasses.dataclass
class UploadFileRequest:
    
    upload_model_file_request: shared_uploadmodelfilerequest.UploadModelFileRequest = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})

    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})

    

@dataclasses.dataclass
class UploadFileResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)

    r"""Bad Request"""
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)

    model_file: Optional[shared_modelfile.ModelFile] = dataclasses.field(default=None)

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    