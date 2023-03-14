from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import paginatedresult_userpublicresponse as shared_paginatedresult_userpublicresponse
from enum import Enum
from typing import Optional

class ListUsersSortFieldEnum(str, Enum):
    ID = "id"
    NAME = "name"
    CREATION_TIME = "creationTime"
    DELETED = "deleted"
    MODIFICATION_TIME = "modificationTime"
    EMAIL = "email"
    LAST_SEEN = "lastSeen"

class ListUsersSortOrderEnum(str, Enum):
    ASC = "asc"
    DESC = "desc"


@dataclasses.dataclass
class ListUsersRequest:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    search: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search', 'style': 'form', 'explode': True }})
    sort_field: Optional[ListUsersSortFieldEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortField', 'style': 'form', 'explode': True }})
    sort_order: Optional[ListUsersSortOrderEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortOrder', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListUsersResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    paginated_result_user_public_response: Optional[shared_paginatedresult_userpublicresponse.PaginatedResultUserPublicResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    