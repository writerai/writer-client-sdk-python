"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from .briefdocuments import BriefDocuments
from enum import Enum
from typing import Dict, List, Optional

class ListTeamDocumentsQueryParamSortField(str, Enum):
    TITLE = 'title'
    CREATION_TIME = 'creationTime'
    MODIFICATION_TIME = 'modificationTime'
    MODIFIED_BY_ME_TIME = 'modifiedByMeTime'
    OPENED_BY_ME_TIME = 'openedByMeTime'

class ListTeamDocumentsQueryParamSortOrder(str, Enum):
    ASC = 'asc'
    DESC = 'desc'


@dataclasses.dataclass
class ListTeamDocumentsRequest:
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    search: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search', 'style': 'form', 'explode': True }})
    sort_field: Optional[ListTeamDocumentsQueryParamSortField] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortField', 'style': 'form', 'explode': True }})
    sort_order: Optional[ListTeamDocumentsQueryParamSortOrder] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortOrder', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class ListTeamDocumentsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    brief_documents: Optional[BriefDocuments] = dataclasses.field(default=None)
    
