import requests as requests_http
from . import utils
from typing import Any, Optional
from writer.models import operations, shared

class Files:
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
        
    def delete_file(self, request: operations.DeleteFileRequest) -> operations.DeleteFileResponse:
        r"""Delete file
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/llm/organization/{organizationId}/file/{fileId}', request.path_params)
        
        
        client = self._client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.delete_file_200_application_json_object = out
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

    def files(self, request: operations.FilesRequest) -> operations.FilesResponse:
        r"""List files
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/llm/organization/{organizationId}/file', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ModelFilesResponse])
                res.model_files_response = out
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

    def get_file(self, request: operations.GetFileRequest) -> operations.GetFileResponse:
        r"""Get file
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/llm/organization/{organizationId}/file/{fileId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ModelFile])
                res.model_file = out
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

    def upload_file(self, request: operations.UploadFileRequest) -> operations.UploadFileResponse:
        r"""Upload file
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/llm/organization/{organizationId}/file', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UploadFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ModelFile])
                res.model_file = out
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

    