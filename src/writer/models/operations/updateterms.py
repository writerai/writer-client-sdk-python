"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createtermsresponse as shared_createtermsresponse
from ..shared import updatetermsrequest as shared_updatetermsrequest
from typing import Dict, List, Optional


@dataclasses.dataclass
class UpdateTermsRequest:
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    update_terms_request: shared_updatetermsrequest.UpdateTermsRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Request-ID', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class UpdateTermsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_terms_response: Optional[shared_createtermsresponse.CreateTermsResponse] = dataclasses.field(default=None)
    headers: Optional[Dict[str, List[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

