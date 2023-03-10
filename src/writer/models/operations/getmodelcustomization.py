from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import modelcustomization as shared_modelcustomization
from typing import Optional


@dataclasses.dataclass
class GetModelCustomizationPathParams:
    customization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customizationId', 'style': 'simple', 'explode': False }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetModelCustomizationHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetModelCustomizationRequest:
    headers: GetModelCustomizationHeaders = dataclasses.field()
    path_params: GetModelCustomizationPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetModelCustomizationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    model_customization: Optional[shared_modelcustomization.ModelCustomization] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    