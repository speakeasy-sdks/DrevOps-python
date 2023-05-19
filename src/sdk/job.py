"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations
from typing import Optional

class Job:
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
        
    
    def cancel_job(self, request: operations.CancelJobRequest) -> operations.CancelJobResponse:
        r"""Cancel job
        Cancel job with a given job number.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CancelJobRequest, base_url, '/project/{project-slug}/job/{job-number}/cancel', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CancelJobResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CancelJobMessageResponse])
                res.message_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CancelJobDefaultApplicationJSON])
                res.cancel_job_default_application_json_object = out

        return res

    
    def get_job_artifacts(self, request: operations.GetJobArtifactsRequest) -> operations.GetJobArtifactsResponse:
        r"""Get a job's artifacts
        Returns a job's artifacts.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetJobArtifactsRequest, base_url, '/project/{project-slug}/{job-number}/artifacts', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetJobArtifactsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetJobArtifactsArtifactListResponse])
                res.artifact_list_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetJobArtifactsDefaultApplicationJSON])
                res.get_job_artifacts_default_application_json_object = out

        return res

    
    def get_job_details(self, request: operations.GetJobDetailsRequest) -> operations.GetJobDetailsResponse:
        r"""Get job details
        Returns job details.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetJobDetailsRequest, base_url, '/project/{project-slug}/job/{job-number}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetJobDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetJobDetailsJobDetails])
                res.job_details = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetJobDetailsDefaultApplicationJSON])
                res.get_job_details_default_application_json_object = out

        return res

    
    def get_tests(self, request: operations.GetTestsRequest) -> operations.GetTestsResponse:
        r"""Get test metadata
        Get test metadata for a build. In the rare case where there is more than 250MB of test data on the job, no results will be returned.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetTestsRequest, base_url, '/project/{project-slug}/{job-number}/tests', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTestsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetTestsTestsResponse])
                res.tests_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetTestsDefaultApplicationJSON])
                res.get_tests_default_application_json_object = out

        return res

    