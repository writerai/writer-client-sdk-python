import requests as requests_http
from . import utils
from typing import Optional
from writer.models import operations, shared

class Snippet:
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
        
    def delete_snippets(self, request: operations.DeleteSnippetsRequest) -> operations.DeleteSnippetsResponse:
        r"""Delete snippets
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/snippet/organization/{organizationId}/team/{teamId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        http_res = client.request('DELETE', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteSnippetsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeleteResponse])
                res.delete_response = out
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

    def find_snippets(self, request: operations.FindSnippetsRequest) -> operations.FindSnippetsResponse:
        r"""Find snippets
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/snippet/organization/{organizationId}/team/{teamId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FindSnippetsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PaginatedResultSnippetWithUser])
                res.paginated_result_snippet_with_user = out
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

    def update_snippets(self, request: operations.UpdateSnippetsRequest) -> operations.UpdateSnippetsResponse:
        r"""Update snippets
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/snippet/organization/{organizationId}/team/{teamId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateSnippetsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.SnippetWithUser]])
                res.snippet_with_users = out
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

    