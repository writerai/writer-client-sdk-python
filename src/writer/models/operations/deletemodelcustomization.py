from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from typing import Any, Optional


@dataclasses.dataclass
class DeleteModelCustomizationPathParams:
    customization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customizationId', 'style': 'simple', 'explode': False }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteModelCustomizationRequest:
    path_params: DeleteModelCustomizationPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteModelCustomizationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_model_customization_200_application_json_object: Optional[dict[str, Any]] = dataclasses.field(default=None)
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    