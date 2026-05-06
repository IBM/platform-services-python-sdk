# coding: utf-8

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
IBM Quantum Platform REST API client.

This service exposes the low-level IBM Quantum Platform / Qiskit Runtime REST
endpoints. For Qiskit-native circuits, primitives, sessions, backends, and result
handling, use qiskit-ibm-runtime.

API Version: 2026-03-15
"""

from typing import List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse, read_external_sources
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class QuantumPlatformV1(BaseService):
    """The Quantum Platform V1 service."""

    DEFAULT_SERVICE_URL = 'https://quantum.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'quantum_platform'
    DEFAULT_API_VERSION = '2026-03-15'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'QuantumPlatformV1':
        """
        Return a new client for the Quantum Platform service using the specified
        parameters and external configuration.

        In addition to standard SDK authenticator configuration, this method reads
        QUANTUM_PLATFORM_INSTANCE_CRN and QUANTUM_PLATFORM_API_VERSION from the
        configured environment or credentials file.
        """
        config = read_external_sources(service_name) or {}
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator=authenticator,
            instance_crn=config.get('INSTANCE_CRN'),
            api_version=config.get('API_VERSION') or cls.DEFAULT_API_VERSION,
        )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
        *,
        instance_crn: Optional[str] = None,
        api_version: Optional[str] = None,
    ) -> None:
        """
        Construct a new client for the Quantum Platform service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
        :param str instance_crn: (optional) Default IBM Quantum Platform instance CRN
               to send as the Service-CRN header on CRN-scoped operations.
        :param str api_version: (optional) Default IBM-API-Version header value.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        self.instance_crn = instance_crn
        self.api_version = api_version or self.DEFAULT_API_VERSION

    def set_instance_crn(self, instance_crn: str) -> None:
        """Set the default instance CRN used by CRN-scoped operations."""
        self.instance_crn = instance_crn

    def set_api_version(self, api_version: str) -> None:
        """Set the default IBM-API-Version header used by API-versioned operations."""
        self.api_version = api_version

    def _resolve_instance_crn(self, service_crn: Optional[str], operation_id: str) -> str:
        resolved = service_crn or self.instance_crn
        if not resolved:
            raise ValueError(
                f'service_crn must be provided for {operation_id}, either as a per-call value '
                'or as the service instance_crn default'
            )
        return resolved

    def _encode_path_var(self, value: str) -> str:
        return next(self.encode_path_vars(value))

    def _prepare_headers(
        self,
        operation_id: str,
        *,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        require_crn: bool = True,
        require_api_version: bool = True,
        accept: Optional[str] = 'application/json',
        content_type: Optional[str] = None,
        user_headers: Optional[dict] = None,
    ) -> dict:
        headers = {}
        headers.update(
            get_sdk_headers(
                service_name=self.DEFAULT_SERVICE_NAME,
                service_version='V1',
                operation_id=operation_id,
            )
        )
        if accept:
            headers['Accept'] = accept
        if content_type:
            headers['Content-Type'] = content_type
        if require_crn:
            headers['Service-CRN'] = self._resolve_instance_crn(service_crn, operation_id)
        if require_api_version:
            headers['IBM-API-Version'] = ibm_api_version or self.api_version or self.DEFAULT_API_VERSION
        if user_headers:
            headers.update(user_headers)
        return headers

    def _send_request(
        self,
        operation_id: str,
        method: str,
        url: str,
        *,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        require_crn: bool = True,
        require_api_version: bool = True,
        params: Optional[dict] = None,
        body: Optional[dict] = None,
        accept: Optional[str] = 'application/json',
        content_type: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        user_headers = kwargs.pop('headers', None)
        headers = self._prepare_headers(
            operation_id,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            require_crn=require_crn,
            require_api_version=require_api_version,
            accept=accept,
            content_type=content_type or ('application/json' if body is not None else None),
            user_headers=user_headers,
        )
        data = json.dumps(convert_model(body)) if body is not None else None
        request = self.prepare_request(method=method, url=url, headers=headers, params=params, data=data)
        return self.send(request, **kwargs)

    #########################
    # Versions
    #########################

    def get_versions(
        self,
        *,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """Get supported API versions."""
        return self._send_request(
            'get_versions',
            'GET',
            '/api/v1/versions',
            ibm_api_version=ibm_api_version,
            require_crn=False,
            require_api_version=False,
            **kwargs,
        )

    #########################
    # Jobs
    #########################

    def create_job(
        self,
        body: dict,
        *,
        parent_job_id: Optional[str] = None,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """Invoke a Qiskit Runtime primitive using the raw REST request body."""
        if body is None:
            raise ValueError('body must be provided')
        if parent_job_id:
            headers = kwargs.get('headers') or {}
            headers['Parent-Job-Id'] = parent_job_id
            kwargs['headers'] = headers
        return self._send_request(
            'create_job',
            'POST',
            '/api/v1/jobs',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            body=body,
            **kwargs,
        )

    def list_jobs(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        pending: Optional[bool] = None,
        program: Optional[str] = None,
        backend: Optional[str] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        sort: Optional[str] = None,
        tags: Optional[List[str]] = None,
        session_id: Optional[str] = None,
        exclude_params: Optional[bool] = None,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """List quantum program jobs."""
        params = {
            'limit': limit,
            'offset': offset,
            'pending': pending,
            'program': program,
            'backend': backend,
            'created_after': created_after,
            'created_before': created_before,
            'sort': sort,
            'tags': tags,
            'session_id': session_id,
            'exclude_params': exclude_params,
        }
        return self._send_request(
            'list_jobs',
            'GET',
            '/api/v1/jobs',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params=params,
            **kwargs,
        )

    def get_job(
        self,
        id: str,
        *,
        exclude_params: Optional[bool] = None,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """List details about the specified quantum program job."""
        if id is None:
            raise ValueError('id must be provided')
        url = '/api/v1/jobs/{id}'.format(id=self._encode_path_var(id))
        return self._send_request(
            'get_job',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params={'exclude_params': exclude_params},
            **kwargs,
        )

    def delete_job(
        self,
        id: str,
        *,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """Delete the specified job and its associated data."""
        if id is None:
            raise ValueError('id must be provided')
        url = '/api/v1/jobs/{id}'.format(id=self._encode_path_var(id))
        return self._send_request(
            'delete_job',
            'DELETE',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    def cancel_job_jid(
        self,
        id: str,
        *,
        parent_job_id: Optional[str] = None,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """Cancel the specified job."""
        if id is None:
            raise ValueError('id must be provided')
        if parent_job_id:
            headers = kwargs.get('headers') or {}
            headers['Parent-Job-Id'] = parent_job_id
            kwargs['headers'] = headers
        url = '/api/v1/jobs/{id}/cancel'.format(id=self._encode_path_var(id))
        return self._send_request(
            'cancel_job_jid',
            'POST',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    def get_jog_logs_jid(
        self,
        id: str,
        *,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """List all job logs for the specified job."""
        if id is None:
            raise ValueError('id must be provided')
        url = '/api/v1/jobs/{id}/logs'.format(id=self._encode_path_var(id))
        return self._send_request(
            'get_jog_logs_jid',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            accept='text/plain',
            **kwargs,
        )

    def get_job_metrics_jid(
        self,
        id: str,
        *,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """Get metrics for the specified job."""
        if id is None:
            raise ValueError('id must be provided')
        url = '/api/v1/jobs/{id}/metrics'.format(id=self._encode_path_var(id))
        return self._send_request(
            'get_job_metrics_jid',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    def get_job_results_jid(
        self,
        id: str,
        *,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """Return the final result from the specified job."""
        if id is None:
            raise ValueError('id must be provided')
        url = '/api/v1/jobs/{id}/results'.format(id=self._encode_path_var(id))
        return self._send_request(
            'get_job_results_jid',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    def replace_job_tags(
        self,
        id: str,
        tags: List[str],
        *,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """Replace tags for the specified job."""
        if id is None:
            raise ValueError('id must be provided')
        if tags is None:
            raise ValueError('tags must be provided')
        url = '/api/v1/jobs/{id}/tags'.format(id=self._encode_path_var(id))
        return self._send_request(
            'replace_job_tags',
            'PUT',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            body={'tags': tags},
            **kwargs,
        )

    #########################
    # Backends
    #########################

    def list_backends(
        self,
        *,
        fields: Optional[str] = None,
        service_crn: Optional[str] = None,
        ibm_api_version: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """List backends available to the current instance."""
        return self._send_request(
            'list_backends',
            'GET',
            '/api/v1/backends',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params={'fields': fields},
            **kwargs,
        )

    def get_backend_configuration(
        self,
        backend_name: str,
        *,
        calibration_id: Optional[str] = None,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Get backend configuration."""
        if backend_name is None:
            raise ValueError('backend_name must be provided')
        url = '/api/v1/backends/{backend_name}/configuration'.format(
            backend_name=self._encode_path_var(backend_name)
        )
        return self._send_request(
            'get_backend_configuration',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params={'calibration_id': calibration_id},
            **kwargs,
        )

    def get_backend_defaults(
        self,
        backend_name: str,
        *,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Get backend default settings."""
        if backend_name is None:
            raise ValueError('backend_name must be provided')
        url = '/api/v1/backends/{backend_name}/defaults'.format(backend_name=self._encode_path_var(backend_name))
        return self._send_request(
            'get_backend_defaults',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    def get_backend_properties(
        self,
        backend_name: str,
        *,
        updated_before: Optional[str] = None,
        calibration_id: Optional[str] = None,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Get backend properties."""
        if backend_name is None:
            raise ValueError('backend_name must be provided')
        url = '/api/v1/backends/{backend_name}/properties'.format(backend_name=self._encode_path_var(backend_name))
        return self._send_request(
            'get_backend_properties',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params={'updated_before': updated_before, 'calibration_id': calibration_id},
            **kwargs,
        )

    def get_backend_status(
        self,
        backend_name: str,
        *,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Get backend status."""
        if backend_name is None:
            raise ValueError('backend_name must be provided')
        url = '/api/v1/backends/{backend_name}/status'.format(backend_name=self._encode_path_var(backend_name))
        return self._send_request(
            'get_backend_status',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    #########################
    # Sessions
    #########################

    def create_session(
        self,
        body: Optional[dict] = None,
        *,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Create a job session."""
        return self._send_request(
            'create_session',
            'POST',
            '/api/v1/sessions',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            body=body,
            **kwargs,
        )

    def get_session(self, id: str, *, service_crn=None, ibm_api_version=None, **kwargs) -> DetailedResponse:
        """Get a job session."""
        if id is None:
            raise ValueError('id must be provided')
        url = '/api/v1/sessions/{id}'.format(id=self._encode_path_var(id))
        return self._send_request(
            'get_session',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    def update_session(
        self,
        id: str,
        body: dict,
        *,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Update a job session."""
        if id is None:
            raise ValueError('id must be provided')
        if body is None:
            raise ValueError('body must be provided')
        url = '/api/v1/sessions/{id}'.format(id=self._encode_path_var(id))
        return self._send_request(
            'update_session',
            'PATCH',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            body=body,
            **kwargs,
        )

    def delete_session_close(
        self,
        id: str,
        *,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Close a job session."""
        if id is None:
            raise ValueError('id must be provided')
        url = '/api/v1/sessions/{id}/close'.format(id=self._encode_path_var(id))
        return self._send_request(
            'delete_session_close',
            'DELETE',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    #########################
    # Instances
    #########################

    def get_instance(self, *, service_crn=None, ibm_api_version=None, **kwargs) -> DetailedResponse:
        """Get current instance details."""
        return self._send_request(
            'get_instance',
            'GET',
            '/api/v1/instance',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    def get_instance_configuration(self, *, service_crn=None, ibm_api_version=None, **kwargs) -> DetailedResponse:
        """Get instance configuration."""
        return self._send_request(
            'get_instance_configuration',
            'GET',
            '/api/v1/instances/configuration',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    def replace_instance_configuration(
        self,
        body: dict,
        *,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Update instance configuration."""
        if body is None:
            raise ValueError('body must be provided')
        return self._send_request(
            'replace_instance_configuration',
            'PUT',
            '/api/v1/instances/configuration',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            body=body,
            **kwargs,
        )

    def get_usage(self, *, service_crn=None, ibm_api_version=None, **kwargs) -> DetailedResponse:
        """Get instance usage."""
        return self._send_request(
            'get_usage',
            'GET',
            '/api/v1/instances/usage',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            **kwargs,
        )

    #########################
    # Tags, Accounts, Workloads, Analytics
    #########################

    def list_tags(
        self,
        type: str = 'job',
        search: str = None,
        *,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """List tags."""
        if type is None:
            raise ValueError('type must be provided')
        if search is None:
            raise ValueError('search must be provided')
        return self._send_request(
            'list_tags',
            'GET',
            '/api/v1/tags',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params={'type': type, 'search': search},
            **kwargs,
        )

    def get_account(
        self,
        id: str,
        *,
        plan_id: Optional[str] = None,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Get account configuration."""
        if id is None:
            raise ValueError('id must be provided')
        url = '/api/v1/accounts/{id}'.format(id=self._encode_path_var(id))
        return self._send_request(
            'get_account',
            'GET',
            url,
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params={'plan_id': plan_id},
            **kwargs,
        )

    def find_instance_workloads(
        self,
        *,
        user: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        previous: Optional[str] = None,
        next: Optional[str] = None,
        backend: Optional[str] = None,
        search: Optional[str] = None,
        status: Optional[List[str]] = None,
        mode: Optional[str] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        tags: Optional[List[str]] = None,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """List user instance workloads."""
        params = {
            'user': user,
            'sort': sort,
            'limit': limit,
            'previous': previous,
            'next': next,
            'backend': backend,
            'search': search,
            'status': status,
            'mode': mode,
            'created_after': created_after,
            'created_before': created_before,
            'tags': tags,
        }
        return self._send_request(
            'find_instance_workloads',
            'GET',
            '/api/v1/workloads',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params=params,
            **kwargs,
        )

    def analytics_filters(
        self,
        *,
        instance: Optional[List[str]] = None,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Get usage analytics filters."""
        return self._send_request(
            'analytics_filters',
            'GET',
            '/api/v1/analytics/filters',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params={'instance': instance},
            **kwargs,
        )

    def analytics_usage(
        self,
        *,
        instance: Optional[List[str]] = None,
        interval_start: Optional[str] = None,
        interval_end: Optional[str] = None,
        backend: Optional[List[str]] = None,
        user_id: Optional[List[str]] = None,
        simulators: Optional[bool] = None,
        plan: Optional[List[str]] = None,
        subscription_id: Optional[List[str]] = None,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Get usage analytics."""
        params = {
            'instance': instance,
            'interval_start': interval_start,
            'interval_end': interval_end,
            'backend': backend,
            'user_id': user_id,
            'simulators': simulators,
            'plan': plan,
            'subscription_id': subscription_id,
        }
        return self._send_request(
            'analytics_usage',
            'GET',
            '/api/v1/analytics/usage',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params=params,
            **kwargs,
        )

    def get_usage_analytics_grouped(
        self,
        group_by: str,
        *,
        instance: Optional[List[str]] = None,
        interval_start: Optional[str] = None,
        interval_end: Optional[str] = None,
        backend: Optional[List[str]] = None,
        user_id: Optional[List[str]] = None,
        simulators: Optional[bool] = None,
        plan: Optional[List[str]] = None,
        subscription_id: Optional[List[str]] = None,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Get usage analytics grouped."""
        if group_by is None:
            raise ValueError('group_by must be provided')
        params = {
            'group_by': group_by,
            'instance': instance,
            'interval_start': interval_start,
            'interval_end': interval_end,
            'backend': backend,
            'user_id': user_id,
            'simulators': simulators,
            'plan': plan,
            'subscription_id': subscription_id,
        }
        return self._send_request(
            'get_usage_analytics_grouped',
            'GET',
            '/api/v1/analytics/usage_grouped',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params=params,
            **kwargs,
        )

    def get_usage_analytics_grouped_by_date(
        self,
        group_by: str,
        *,
        instance: Optional[List[str]] = None,
        interval_start: Optional[str] = None,
        interval_end: Optional[str] = None,
        backend: Optional[List[str]] = None,
        user_id: Optional[List[str]] = None,
        simulators: Optional[bool] = None,
        plan: Optional[List[str]] = None,
        subscription_id: Optional[List[str]] = None,
        service_crn=None,
        ibm_api_version=None,
        **kwargs,
    ) -> DetailedResponse:
        """Get usage analytics grouped by date."""
        if group_by is None:
            raise ValueError('group_by must be provided')
        params = {
            'group_by': group_by,
            'instance': instance,
            'interval_start': interval_start,
            'interval_end': interval_end,
            'backend': backend,
            'user_id': user_id,
            'simulators': simulators,
            'plan': plan,
            'subscription_id': subscription_id,
        }
        return self._send_request(
            'get_usage_analytics_grouped_by_date',
            'GET',
            '/api/v1/analytics/usage_grouped_by_date',
            service_crn=service_crn,
            ibm_api_version=ibm_api_version,
            params=params,
            **kwargs,
        )
