from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import contentrequest as shared_contentrequest
from ..shared import failresponse as shared_failresponse
from ..shared import processedcontent as shared_processedcontent
from typing import Optional


@dataclasses.dataclass
class ContentCheckPathParams:
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ContentCheckHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ContentCheckRequest:
    headers: ContentCheckHeaders = dataclasses.field()
    path_params: ContentCheckPathParams = dataclasses.field()
    request: shared_contentrequest.ContentRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ContentCheckResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    processed_content: Optional[shared_processedcontent.ProcessedContent] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    