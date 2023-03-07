from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from typing import Optional


@dataclasses.dataclass
class FetchCustomizedModelFilePathParams:
    customization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customizationId', 'style': 'simple', 'explode': False }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FetchCustomizedModelFileHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FetchCustomizedModelFileRequest:
    headers: FetchCustomizedModelFileHeaders = dataclasses.field()
    path_params: FetchCustomizedModelFilePathParams = dataclasses.field()
    

@dataclasses.dataclass
class FetchCustomizedModelFileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    fetch_customized_model_file_200_application_octet_stream_binary_string: Optional[bytes] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    