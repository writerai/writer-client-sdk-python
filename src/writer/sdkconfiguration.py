"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Tuple, Union
from writer import models


SERVERS = [
    'https://enterprise-api.writer.com',
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[models.Security,Callable[[], models.Security]] = None
    server_url: str = ''
    server_idx: int = 0
    globals: Dict[str, Dict[str, Dict[str, Any]]] = field(default_factory=Dict)
    language: str = 'python'
    openapi_doc_version: str = '1.7'
    sdk_version: str = '3.2.1'
    gen_version: str = '2.280.6'
    user_agent: str = 'speakeasy-sdk/python 3.2.1 2.280.6 1.7 writerai'
    retry_config: RetryConfig = None
    _hooks: SDKHooks = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}


    def get_hooks(self) -> SDKHooks:
        return self._hooks
