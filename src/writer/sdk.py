import requests as requests_http
from . import utils
from .ai_content_detector import AIContentDetector
from .billing import Billing
from .completions import Completions
from .content import Content
from .cowrite import CoWrite
from .download_the_customized_model import DownloadTheCustomizedModel
from .files import Files
from .fine_tunes import FineTunes
from .models import Models
from .snippet import Snippet
from .styleguide import Styleguide
from .terminology import Terminology
from .user import User

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
    fine_tunes: FineTunes
    models: Models
    snippet: Snippet
    styleguide: Styleguide
    terminology: Terminology
    user: User
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.2.0"
    _gen_version: str = "1.8.6"

    def __init__(self) -> None:
        self._client = requests_http.Session()
        self._security_client = requests_http.Session()
        self._init_sdks()

    def config_server_url(self, server_url: str, params: dict[str, str] = None):
        if params is not None:
            self._server_url = utils.template_url(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    

    def config_client(self, client: requests_http.Session):
        self._client = client
        self._init_sdks()
    
    
    
    def _init_sdks(self):
        self.ai_content_detector = AIContentDetector(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.billing = Billing(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.co_write = CoWrite(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.completions = Completions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.content = Content(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.download_the_customized_model = DownloadTheCustomizedModel(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.files = Files(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.fine_tunes = FineTunes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.models = Models(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.snippet = Snippet(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.styleguide = Styleguide(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.terminology = Terminology(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.user = User(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    