# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit Tests for QuantumPlatformV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.authenticators.bearer_token_authenticator import BearerTokenAuthenticator
import json
import os
import pytest
import re
import responses
import urllib
import ibm_platform_services.quantum_platform_v1 as quantum_platform_v1
from ibm_platform_services.quantum_platform_v1 import *


_base_url = 'https://quantum.cloud.ibm.com'
_service = QuantumPlatformV1(
    authenticator=NoAuthAuthenticator(),
    instance_crn='crn:v1:bluemix:public:quantum-computing:us-east:a/test:instance::',
)
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    operation_path = urllib.parse.unquote(operation_path)
    operation_path = urllib.parse.quote(operation_path, safe='/')
    request_url = _base_url + operation_path
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'
        os.environ['TEST_SERVICE_INSTANCE_CRN'] = 'crn:test'
        os.environ['TEST_SERVICE_API_VERSION'] = '2026-03-15'

        service = QuantumPlatformV1.new_instance(service_name='TEST_SERVICE')

        assert service is not None
        assert isinstance(service, QuantumPlatformV1)
        assert service.instance_crn == 'crn:test'
        assert service.api_version == '2026-03-15'

        del os.environ['TEST_SERVICE_AUTH_TYPE']
        del os.environ['TEST_SERVICE_INSTANCE_CRN']
        del os.environ['TEST_SERVICE_API_VERSION']

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            QuantumPlatformV1.new_instance(service_name='TEST_SERVICE_NOT_FOUND')


class TestHeaders:
    """
    Test Class for Quantum-specific headers
    """

    @responses.activate
    def test_constructor_instance_crn_and_api_version_headers(self):
        """
        list_backends()
        """
        url = preprocess_url('/api/v1/backends')
        responses.add(responses.GET, url, body='{"backends": []}', content_type='application/json', status=200)

        response = _service.list_backends(headers={})

        assert response.status_code == 200
        assert len(responses.calls) == 1
        request_headers = responses.calls[0].request.headers
        assert request_headers['Service-CRN'] == _service.instance_crn
        assert request_headers['IBM-API-Version'] == QuantumPlatformV1.DEFAULT_API_VERSION

    @responses.activate
    def test_per_call_headers_override_constructor_defaults(self):
        """
        list_backends with per-call overrides
        """
        url = preprocess_url('/api/v1/backends')
        responses.add(responses.GET, url, body='{"backends": []}', content_type='application/json', status=200)

        response = _service.list_backends(
            service_crn='crn:override',
            ibm_api_version='2027-01-01',
            headers={},
        )

        assert response.status_code == 200
        request_headers = responses.calls[0].request.headers
        assert request_headers['Service-CRN'] == 'crn:override'
        assert request_headers['IBM-API-Version'] == '2027-01-01'

    def test_missing_crn_raises_value_error(self):
        """
        list_backends without instance CRN
        """
        service = QuantumPlatformV1(authenticator=NoAuthAuthenticator())
        with pytest.raises(ValueError, match='service_crn must be provided'):
            service.list_backends(headers={})

    @responses.activate
    def test_versions_does_not_require_crn(self):
        """
        get_versions()
        """
        url = preprocess_url('/api/v1/versions')
        responses.add(responses.GET, url, body='{"versions": []}', content_type='application/json', status=200)

        service = QuantumPlatformV1(authenticator=NoAuthAuthenticator())
        service.set_service_url(_base_url)
        response = service.get_versions(headers={})

        assert response.status_code == 200
        request_headers = responses.calls[0].request.headers
        assert 'Service-CRN' not in request_headers
        assert 'IBM-API-Version' not in request_headers

    @responses.activate
    def test_eu_url_override(self):
        """
        list_backends with EU URL
        """
        eu_url = 'https://eu-de.quantum.cloud.ibm.com'
        service = QuantumPlatformV1(authenticator=NoAuthAuthenticator(), instance_crn='crn:test')
        service.set_service_url(eu_url)
        responses.add(
            responses.GET,
            eu_url + '/api/v1/backends',
            body='{"backends": []}',
            content_type='application/json',
            status=200,
        )

        response = service.list_backends(headers={})

        assert response.status_code == 200
        assert len(responses.calls) == 1

    @responses.activate
    def test_bearer_token_authenticator_adds_authorization_header(self):
        """
        BearerTokenAuthenticator()
        """
        service = QuantumPlatformV1(authenticator=BearerTokenAuthenticator('test-token'), instance_crn='crn:test')
        service.set_service_url(_base_url)
        url = preprocess_url('/api/v1/backends')
        responses.add(responses.GET, url, body='{"backends": []}', content_type='application/json', status=200)

        response = service.list_backends(headers={})

        assert response.status_code == 200
        assert responses.calls[0].request.headers['Authorization'] == 'Bearer test-token'


class TestJobs:
    """
    Test Class for job operations
    """

    @responses.activate
    def test_create_job(self):
        """
        create_job()
        """
        url = preprocess_url('/api/v1/jobs')
        responses.add(responses.POST, url, body='{"id": "job-id"}', content_type='application/json', status=201)

        body = {'program_id': 'sampler', 'backend': 'ibm_test', 'params': {'pubs': []}}
        response = _service.create_job(body=body, parent_job_id='parent-id', headers={})

        assert response.status_code == 201
        assert json.loads(str(responses.calls[0].request.body, 'utf-8')) == body
        assert responses.calls[0].request.headers['Parent-Job-Id'] == 'parent-id'

    @responses.activate
    def test_replace_job_tags(self):
        """
        replace_job_tags()
        """
        url = preprocess_url('/api/v1/jobs/job-id/tags')
        responses.add(responses.PUT, url, body='{"tags": ["a"]}', content_type='application/json', status=200)

        response = _service.replace_job_tags('job-id', ['a'], headers={})

        assert response.status_code == 200
        assert json.loads(str(responses.calls[0].request.body, 'utf-8')) == {'tags': ['a']}

    @responses.activate
    def test_job_operation_id_methods(self):
        """
        OpenAPI operationId methods
        """
        responses.add(responses.POST, preprocess_url('/api/v1/jobs/job-id/cancel'), status=204)
        responses.add(
            responses.GET,
            preprocess_url('/api/v1/jobs/job-id/logs'),
            body='logs',
            content_type='text/plain',
            status=200,
        )

        cancel_response = _service.cancel_job_jid('job-id', parent_job_id='parent-id', headers={})
        logs_response = _service.get_jog_logs_jid('job-id', headers={})

        assert cancel_response.status_code == 204
        assert logs_response.status_code == 200
        assert responses.calls[0].request.headers['Parent-Job-Id'] == 'parent-id'
        assert responses.calls[1].request.headers['Accept'] == 'text/plain'

    @responses.activate
    def test_sdk_headers_use_openapi_operation_id(self, monkeypatch):
        """
        get_sdk_headers() receives the OpenAPI operationId.
        """
        operation_ids = []

        def mock_get_sdk_headers(service_name, service_version, operation_id):
            operation_ids.append(operation_id)
            return {}

        monkeypatch.setattr(quantum_platform_v1, 'get_sdk_headers', mock_get_sdk_headers)
        responses.add(responses.POST, preprocess_url('/api/v1/jobs'), body='{}', status=200)

        _service.create_job({'program_id': 'sampler'}, headers={})

        assert operation_ids == ['create_job']

    def test_friendly_aliases_are_not_present(self):
        """
        Friendly method aliases are intentionally not part of the public API.
        """
        friendly_names = [
            'run_job',
            'cancel_job',
            'list_job_logs',
            'list_job_results',
            'get_job_metrics',
            'close_session',
            'update_instance_configuration',
            'get_instance_usage',
            'get_account_configuration',
            'list_workloads',
            'get_analytics_filters',
            'get_usage_analytics',
        ]

        for name in friendly_names:
            assert not hasattr(QuantumPlatformV1, name)


class TestSessionsAndAnalytics:
    """
    Test Class for session and analytics operation details
    """

    @responses.activate
    def test_update_and_delete_session_close_methods(self):
        """
        update_session() and delete_session_close()
        """
        update_url = preprocess_url('/api/v1/sessions/session-id')
        close_url = preprocess_url('/api/v1/sessions/session-id/close')
        responses.add(responses.PATCH, update_url, status=204)
        responses.add(responses.DELETE, close_url, status=204)

        update_response = _service.update_session('session-id', {'accepting_jobs': True}, headers={})
        close_response = _service.delete_session_close('session-id', headers={})

        assert update_response.status_code == 204
        assert close_response.status_code == 204
        assert responses.calls[0].request.method == 'PATCH'
        assert responses.calls[1].request.method == 'DELETE'

    @responses.activate
    def test_grouped_analytics_path_and_query(self):
        """
        get_usage_analytics_grouped()
        """
        url = preprocess_url('/api/v1/analytics/usage_grouped')
        responses.add(responses.GET, url, body='{}', content_type='application/json', status=200)

        response = _service.get_usage_analytics_grouped('backend', instance=['crn:test'], headers={})

        assert response.status_code == 200
        assert 'group_by=backend' in responses.calls[0].request.url
        assert 'instance=crn%3Atest' in responses.calls[0].request.url

    @responses.activate
    def test_other_operation_id_methods(self):
        """
        OpenAPI operationId methods for non-job operations
        """
        responses.add(responses.GET, preprocess_url('/api/v1/accounts/account-id'), body='{}', status=200)
        responses.add(responses.GET, preprocess_url('/api/v1/workloads'), body='{}', status=200)
        responses.add(responses.GET, preprocess_url('/api/v1/analytics/usage'), body='{}', status=200)
        responses.add(responses.GET, preprocess_url('/api/v1/analytics/filters'), body='{}', status=200)
        responses.add(responses.GET, preprocess_url('/api/v1/instances/usage'), body='{}', status=200)

        assert _service.get_account('account-id', headers={}).status_code == 200
        assert _service.find_instance_workloads(headers={}).status_code == 200
        assert _service.analytics_usage(headers={}).status_code == 200
        assert _service.analytics_filters(headers={}).status_code == 200
        assert _service.get_usage(headers={}).status_code == 200
