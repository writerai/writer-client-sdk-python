"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from .completionrequest import CompletionRequest
from .completionresponse import CompletionResponse
from typing import Dict, List, Optional


@dataclasses.dataclass
class CreateCompletionRequest:
    completion_request: CompletionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class CreateCompletionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    completion_response: Optional[CompletionResponse] = dataclasses.field(default=None)
    

