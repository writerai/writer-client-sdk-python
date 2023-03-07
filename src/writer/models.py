import requests as requests_http
from . import utils
from typing import Optional
from writer.models import operations, shared

class Models:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def models(self, request: operations.ModelsRequest) -> operations.ModelsResponse:
        r"""List available LLM models
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/llm/organization/{organizationId}/model', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModelsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GenerationModelsResponse])
                res.generation_models_response = out
        elif http_res.status_code == 400:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out
        elif http_res.status_code == 401:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out
        elif http_res.status_code == 403:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out
        elif http_res.status_code == 404:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out
        elif http_res.status_code == 500:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out

        return res

    