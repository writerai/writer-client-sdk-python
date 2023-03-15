import requests as requests_http
from . import utils
from .ai_content_detector import AIContentDetector
from .billing import Billing
from .completions import Completions
from .content import Content
from .cowrite import CoWrite
from .download_the_customized_model import DownloadTheCustomizedModel
from .files import Files
from .modelcustomization import ModelCustomization
from .models_ import Models
from .snippet import Snippet
from .styleguide import Styleguide
from .terminology import Terminology
from .user import User
from typing import Any
from writer.models import shared

SERVERS = [
	"https://enterprise-api.writer.com",
]

class Writer:
    ai_content_detector: AIContentDetector
    billing: Billing
    co_write: CoWrite
    completions: Completions
    content: Content
    download_the_customized_model: DownloadTheCustomizedModel
    files: Files
    model_customization: ModelCustomization
    models: Models
    snippet: Snippet
    styleguide: Styleguide
    terminology: Terminology
    user: User
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.3.1"
    _gen_version: str = "1.11.2"
    _globals: dict[str, dict[str, dict[str, Any]]]

    def __init__(self,
                 security: shared.Security = None,
                 organization_id: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        self._client = requests_http.Session()
        
        self._globals = {
            "parameters": {
                "queryParam": {
                },
                "pathParam": {
                    "organization_id": organization_id,
                },
            },
        }
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.ai_content_detector = AIContentDetector(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.billing = Billing(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.co_write = CoWrite(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.completions = Completions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.content = Content(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.download_the_customized_model = DownloadTheCustomizedModel(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.files = Files(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.model_customization = ModelCustomization(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.models = Models(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.snippet = Snippet(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.styleguide = Styleguide(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.terminology = Terminology(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
        self.user = User(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version,
            self._globals
        )
        
    