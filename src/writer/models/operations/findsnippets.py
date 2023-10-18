"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import paginatedresult_snippetwithuser as shared_paginatedresult_snippetwithuser
from enum import Enum
from typing import Dict, List, Optional

class FindSnippetsSortField(str, Enum):
    SHORTCUT = 'shortcut'
    CREATION_TIME = 'creationTime'
    MODIFICATION_TIME = 'modificationTime'

class FindSnippetsSortOrder(str, Enum):
    ASC = 'asc'
    DESC = 'desc'


@dataclasses.dataclass
class FindSnippetsRequest:
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    search: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search', 'style': 'form', 'explode': True }})
    shortcuts: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'shortcuts', 'style': 'form', 'explode': True }})
    sort_field: Optional[FindSnippetsSortField] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortField', 'style': 'form', 'explode': True }})
    sort_order: Optional[FindSnippetsSortOrder] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortOrder', 'style': 'form', 'explode': True }})
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tags', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class FindSnippetsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    headers: Optional[Dict[str, List[str]]] = dataclasses.field(default=None)
    paginated_result_snippet_with_user: Optional[shared_paginatedresult_snippetwithuser.PaginatedResultSnippetWithUser] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

