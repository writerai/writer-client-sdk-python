from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import draft as shared_draft
from ..shared import failresponse as shared_failresponse
from ..shared import generatetemplaterequest as shared_generatetemplaterequest
from typing import Optional


@dataclasses.dataclass
class GenerateContentPathParams:
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GenerateContentHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GenerateContentRequest:
    headers: GenerateContentHeaders = dataclasses.field()
    path_params: GenerateContentPathParams = dataclasses.field()
    request: shared_generatetemplaterequest.GenerateTemplateRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class GenerateContentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    draft: Optional[shared_draft.Draft] = dataclasses.field(default=None)
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    