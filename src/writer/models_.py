"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from typing import Optional
from writer import models, utils
from writer._hooks import HookContext

class Models:
    r"""Methods related to Model"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def list(self, organization_id: Optional[int] = None) -> models.ListModelsResponse:
        r"""List available LLM models"""
        hook_ctx = HookContext(operation_id='listModels', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = models.ListModelsRequest(
            organization_id=organization_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(models.ListModelsRequest, base_url, '/llm/organization/{organizationId}/model', request, self.sdk_configuration.globals)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('GET', url, params=query_params, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','401','403','404','4XX','500','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        
        res = models.ListModelsResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res, headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[models.GenerationModelsResponse])
                res.generation_models_response = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, models.FailResponse)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise models.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise models.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    