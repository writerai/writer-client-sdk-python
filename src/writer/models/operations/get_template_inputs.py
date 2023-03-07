from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import templatedetailsresponse as shared_templatedetailsresponse
from typing import Optional


@dataclasses.dataclass
class GetTemplateInputsPathParams:
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    template_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'templateId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTemplateInputsHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTemplateInputsRequest:
    headers: GetTemplateInputsHeaders = dataclasses.field()
    path_params: GetTemplateInputsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetTemplateInputsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    template_details_response: Optional[shared_templatedetailsresponse.TemplateDetailsResponse] = dataclasses.field(default=None)
    