from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import pagewithsectionresponse as shared_pagewithsectionresponse
from typing import Optional


@dataclasses.dataclass
class PageDetailsRequest:
    page_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'pageId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PageDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    page_with_section_response: Optional[shared_pagewithsectionresponse.PageWithSectionResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    