from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import paginatedresult_snippetwithuser as shared_paginatedresult_snippetwithuser
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class FindSnippetsPathParams:
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    
class FindSnippetsSortFieldEnum(str, Enum):
    SHORTCUT = "shortcut"
    CREATION_TIME = "creationTime"
    MODIFICATION_TIME = "modificationTime"

class FindSnippetsSortOrderEnum(str, Enum):
    ASC = "asc"
    DESC = "desc"


@dataclasses.dataclass
class FindSnippetsQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    search: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search', 'style': 'form', 'explode': True }})
    shortcuts: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'shortcuts', 'style': 'form', 'explode': True }})
    sort_field: Optional[FindSnippetsSortFieldEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortField', 'style': 'form', 'explode': True }})
    sort_order: Optional[FindSnippetsSortOrderEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortOrder', 'style': 'form', 'explode': True }})
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tags', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class FindSnippetsHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FindSnippetsRequest:
    headers: FindSnippetsHeaders = dataclasses.field()
    path_params: FindSnippetsPathParams = dataclasses.field()
    query_params: FindSnippetsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class FindSnippetsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    paginated_result_snippet_with_user: Optional[shared_paginatedresult_snippetwithuser.PaginatedResultSnippetWithUser] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    