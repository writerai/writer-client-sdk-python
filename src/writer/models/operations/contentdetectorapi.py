from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import contentdetectorrequest as shared_contentdetectorrequest
from ..shared import contentdetectorresponse as shared_contentdetectorresponse
from ..shared import failresponse as shared_failresponse
from typing import Optional


@dataclasses.dataclass
class ContentDetectorAPIPathParams:
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ContentDetectorAPIHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ContentDetectorAPIRequest:
    headers: ContentDetectorAPIHeaders = dataclasses.field()
    path_params: ContentDetectorAPIPathParams = dataclasses.field()
    request: shared_contentdetectorrequest.ContentDetectorRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ContentDetectorAPIResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    content_detector_responses: Optional[list[shared_contentdetectorresponse.ContentDetectorResponse]] = dataclasses.field(default=None)
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    