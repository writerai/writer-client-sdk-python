from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import snippetupdate as shared_snippetupdate
from ..shared import snippetwithuser as shared_snippetwithuser
from typing import Optional


@dataclasses.dataclass
class UpdateSnippetsRequest:
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    request_body: Optional[list[shared_snippetupdate.SnippetUpdate]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Request-ID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateSnippetsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    snippet_with_users: Optional[list[shared_snippetwithuser.SnippetWithUser]] = dataclasses.field(default=None)
    