# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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
Unit Tests for OpenServiceBrokerV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.open_service_broker_v1 import *


service = OpenServiceBrokerV1(authenticator=NoAuthAuthenticator())

base_url = 'https://fake'
service.set_service_url(base_url)

##############################################################################
# Start of Service: EnableAndDisableInstances
##############################################################################
# region


class TestGetServiceInstanceState:
    """
    Test Class for get_service_instance_state
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_service_instance_state_all_params(self):
        """
        get_service_instance_state()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.get_service_instance_state(instance_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_get_service_instance_state_value_error(self):
        """
        test_get_service_instance_state_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_service_instance_state(**req_copy)


class TestReplaceServiceInstanceState:
    """
    Test Class for replace_service_instance_state
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_service_instance_state_all_params(self):
        """
        replace_service_instance_state()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'
        enabled = False
        initiator_id = 'null'
        reason_code = 'null'

        # Invoke method
        response = service.replace_service_instance_state(
            instance_id, enabled=enabled, initiator_id=initiator_id, reason_code=reason_code, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enabled'] == False
        assert req_body['initiator_id'] == 'null'
        assert req_body['reason_code'] == 'null'

    @responses.activate
    def test_replace_service_instance_state_required_params(self):
        """
        test_replace_service_instance_state_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.replace_service_instance_state(instance_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_replace_service_instance_state_value_error(self):
        """
        test_replace_service_instance_state_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_service_instance_state(**req_copy)


# endregion
##############################################################################
# End of Service: EnableAndDisableInstances
##############################################################################

##############################################################################
# Start of Service: ResourceInstances
##############################################################################
# region


class TestReplaceServiceInstance:
    """
    Test Class for replace_service_instance
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_service_instance_all_params(self):
        """
        replace_service_instance()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"dashboard_url": "dashboard_url", "operation": "operation"}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['account_id'] = 'null'
        context_model['crn'] = 'null'
        context_model['platform'] = 'null'

        # Set up parameter values
        instance_id = 'testString'
        organization_guid = 'null'
        plan_id = 'null'
        service_id = 'null'
        space_guid = 'null'
        context = context_model
        parameters = {}
        accepts_incomplete = True

        # Invoke method
        response = service.replace_service_instance(
            instance_id,
            organization_guid=organization_guid,
            plan_id=plan_id,
            service_id=service_id,
            space_guid=space_guid,
            context=context,
            parameters=parameters,
            accepts_incomplete=accepts_incomplete,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'accepts_incomplete={}'.format('true' if accepts_incomplete else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['organization_guid'] == 'null'
        assert req_body['plan_id'] == 'null'
        assert req_body['service_id'] == 'null'
        assert req_body['space_guid'] == 'null'
        assert req_body['context'] == context_model
        assert req_body['parameters'] == {}

    @responses.activate
    def test_replace_service_instance_required_params(self):
        """
        test_replace_service_instance_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"dashboard_url": "dashboard_url", "operation": "operation"}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.replace_service_instance(instance_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_replace_service_instance_value_error(self):
        """
        test_replace_service_instance_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"dashboard_url": "dashboard_url", "operation": "operation"}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_service_instance(**req_copy)


class TestUpdateServiceInstance:
    """
    Test Class for update_service_instance
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_service_instance_all_params(self):
        """
        update_service_instance()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"operation": "operation"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['account_id'] = 'null'
        context_model['crn'] = 'null'
        context_model['platform'] = 'null'

        # Set up parameter values
        instance_id = 'testString'
        service_id = 'null'
        context = context_model
        parameters = {}
        plan_id = 'null'
        previous_values = {}
        accepts_incomplete = True

        # Invoke method
        response = service.update_service_instance(
            instance_id,
            service_id=service_id,
            context=context,
            parameters=parameters,
            plan_id=plan_id,
            previous_values=previous_values,
            accepts_incomplete=accepts_incomplete,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'accepts_incomplete={}'.format('true' if accepts_incomplete else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['service_id'] == 'null'
        assert req_body['context'] == context_model
        assert req_body['parameters'] == {}
        assert req_body['plan_id'] == 'null'
        assert req_body['previous_values'] == {}

    @responses.activate
    def test_update_service_instance_required_params(self):
        """
        test_update_service_instance_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"operation": "operation"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.update_service_instance(instance_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_update_service_instance_value_error(self):
        """
        test_update_service_instance_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"operation": "operation"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_service_instance(**req_copy)


class TestDeleteServiceInstance:
    """
    Test Class for delete_service_instance
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_service_instance_all_params(self):
        """
        delete_service_instance()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"operation": "operation"}'
        responses.add(responses.DELETE, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        service_id = 'testString'
        plan_id = 'testString'
        instance_id = 'testString'
        accepts_incomplete = True

        # Invoke method
        response = service.delete_service_instance(
            service_id, plan_id, instance_id, accepts_incomplete=accepts_incomplete, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'service_id={}'.format(service_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'accepts_incomplete={}'.format('true' if accepts_incomplete else 'false') in query_string

    @responses.activate
    def test_delete_service_instance_required_params(self):
        """
        test_delete_service_instance_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"operation": "operation"}'
        responses.add(responses.DELETE, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        service_id = 'testString'
        plan_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = service.delete_service_instance(service_id, plan_id, instance_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'service_id={}'.format(service_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string

    @responses.activate
    def test_delete_service_instance_value_error(self):
        """
        test_delete_service_instance_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"operation": "operation"}'
        responses.add(responses.DELETE, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        service_id = 'testString'
        plan_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "service_id": service_id,
            "plan_id": plan_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_service_instance(**req_copy)


# endregion
##############################################################################
# End of Service: ResourceInstances
##############################################################################

##############################################################################
# Start of Service: Catalog
##############################################################################
# region


class TestListCatalog:
    """
    Test Class for list_catalog
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_catalog_all_params(self):
        """
        list_catalog()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/catalog')
        mock_response = '{"services": [{"bindable": true, "description": "description", "id": "id", "name": "name", "plan_updateable": false, "plans": [{"description": "description", "free": true, "id": "id", "name": "name"}]}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = service.list_catalog()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Catalog
##############################################################################

##############################################################################
# Start of Service: LastOperationAsync
##############################################################################
# region


class TestGetLastOperation:
    """
    Test Class for get_last_operation
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_last_operation_all_params(self):
        """
        get_last_operation()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/last_operation')
        mock_response = '{"description": "description", "state": "state"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'
        operation = 'testString'
        plan_id = 'testString'
        service_id = 'testString'

        # Invoke method
        response = service.get_last_operation(
            instance_id, operation=operation, plan_id=plan_id, service_id=service_id, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'operation={}'.format(operation) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'service_id={}'.format(service_id) in query_string

    @responses.activate
    def test_get_last_operation_required_params(self):
        """
        test_get_last_operation_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/last_operation')
        mock_response = '{"description": "description", "state": "state"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.get_last_operation(instance_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_get_last_operation_value_error(self):
        """
        test_get_last_operation_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/last_operation')
        mock_response = '{"description": "description", "state": "state"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_last_operation(**req_copy)


# endregion
##############################################################################
# End of Service: LastOperationAsync
##############################################################################

##############################################################################
# Start of Service: BindingsAndCredentials
##############################################################################
# region


class TestReplaceServiceBinding:
    """
    Test Class for replace_service_binding
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_service_binding_all_params(self):
        """
        replace_service_binding()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        mock_response = '{"credentials": {"anyKey": "anyValue"}, "syslog_drain_url": "syslog_drain_url", "route_service_url": "route_service_url", "volume_mounts": [{"driver": "driver", "container_dir": "container_dir", "mode": "mode", "device_type": "device_type", "device": "device"}]}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Construct a dict representation of a BindResource model
        bind_resource_model = {}
        bind_resource_model['account_id'] = 'null'
        bind_resource_model['serviceid_crn'] = 'null'
        bind_resource_model['target_crn'] = 'null'
        bind_resource_model['app_guid'] = 'null'
        bind_resource_model['route'] = 'null'

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'
        plan_id = 'null'
        service_id = 'null'
        bind_resource = bind_resource_model
        parameters = {}

        # Invoke method
        response = service.replace_service_binding(
            binding_id,
            instance_id,
            plan_id=plan_id,
            service_id=service_id,
            bind_resource=bind_resource,
            parameters=parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['plan_id'] == 'null'
        assert req_body['service_id'] == 'null'
        assert req_body['bind_resource'] == bind_resource_model
        assert req_body['parameters'] == {}

    @responses.activate
    def test_replace_service_binding_required_params(self):
        """
        test_replace_service_binding_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        mock_response = '{"credentials": {"anyKey": "anyValue"}, "syslog_drain_url": "syslog_drain_url", "route_service_url": "route_service_url", "volume_mounts": [{"driver": "driver", "container_dir": "container_dir", "mode": "mode", "device_type": "device_type", "device": "device"}]}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = service.replace_service_binding(binding_id, instance_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_replace_service_binding_value_error(self):
        """
        test_replace_service_binding_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        mock_response = '{"credentials": {"anyKey": "anyValue"}, "syslog_drain_url": "syslog_drain_url", "route_service_url": "route_service_url", "volume_mounts": [{"driver": "driver", "container_dir": "container_dir", "mode": "mode", "device_type": "device_type", "device": "device"}]}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "binding_id": binding_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_service_binding(**req_copy)


class TestDeleteServiceBinding:
    """
    Test Class for delete_service_binding
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_service_binding_all_params(self):
        """
        delete_service_binding()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        responses.add(responses.DELETE, url, status=200)

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'
        plan_id = 'testString'
        service_id = 'testString'

        # Invoke method
        response = service.delete_service_binding(binding_id, instance_id, plan_id, service_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'service_id={}'.format(service_id) in query_string

    @responses.activate
    def test_delete_service_binding_value_error(self):
        """
        test_delete_service_binding_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        responses.add(responses.DELETE, url, status=200)

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'
        plan_id = 'testString'
        service_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "binding_id": binding_id,
            "instance_id": instance_id,
            "plan_id": plan_id,
            "service_id": service_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_service_binding(**req_copy)


# endregion
##############################################################################
# End of Service: BindingsAndCredentials
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestResp1874644Root:
    """
    Test Class for Resp1874644Root
    """

    def test_resp1874644_root_serialization(self):
        """
        Test serialization/deserialization for Resp1874644Root
        """

        # Construct a json representation of a Resp1874644Root model
        resp1874644_root_model_json = {}
        resp1874644_root_model_json['active'] = True
        resp1874644_root_model_json['enabled'] = True
        resp1874644_root_model_json['last_active'] = 72.5

        # Construct a model instance of Resp1874644Root by calling from_dict on the json representation
        resp1874644_root_model = Resp1874644Root.from_dict(resp1874644_root_model_json)
        assert resp1874644_root_model != False

        # Construct a model instance of Resp1874644Root by calling from_dict on the json representation
        resp1874644_root_model_dict = Resp1874644Root.from_dict(resp1874644_root_model_json).__dict__
        resp1874644_root_model2 = Resp1874644Root(**resp1874644_root_model_dict)

        # Verify the model instances are equivalent
        assert resp1874644_root_model == resp1874644_root_model2

        # Convert model instance back to dict and verify no loss of data
        resp1874644_root_model_json2 = resp1874644_root_model.to_dict()
        assert resp1874644_root_model_json2 == resp1874644_root_model_json


class TestResp1874650Root:
    """
    Test Class for Resp1874650Root
    """

    def test_resp1874650_root_serialization(self):
        """
        Test serialization/deserialization for Resp1874650Root
        """

        # Construct dict forms of any model objects needed in order to build this model.

        plans_model = {}  # Plans
        plans_model['description'] = 'testString'
        plans_model['free'] = True
        plans_model['id'] = 'testString'
        plans_model['name'] = 'testString'

        services_model = {}  # Services
        services_model['bindable'] = True
        services_model['description'] = 'testString'
        services_model['id'] = 'testString'
        services_model['name'] = 'testString'
        services_model['plan_updateable'] = True
        services_model['plans'] = [plans_model]

        # Construct a json representation of a Resp1874650Root model
        resp1874650_root_model_json = {}
        resp1874650_root_model_json['services'] = [services_model]

        # Construct a model instance of Resp1874650Root by calling from_dict on the json representation
        resp1874650_root_model = Resp1874650Root.from_dict(resp1874650_root_model_json)
        assert resp1874650_root_model != False

        # Construct a model instance of Resp1874650Root by calling from_dict on the json representation
        resp1874650_root_model_dict = Resp1874650Root.from_dict(resp1874650_root_model_json).__dict__
        resp1874650_root_model2 = Resp1874650Root(**resp1874650_root_model_dict)

        # Verify the model instances are equivalent
        assert resp1874650_root_model == resp1874650_root_model2

        # Convert model instance back to dict and verify no loss of data
        resp1874650_root_model_json2 = resp1874650_root_model.to_dict()
        assert resp1874650_root_model_json2 == resp1874650_root_model_json


class TestResp2079872Root:
    """
    Test Class for Resp2079872Root
    """

    def test_resp2079872_root_serialization(self):
        """
        Test serialization/deserialization for Resp2079872Root
        """

        # Construct a json representation of a Resp2079872Root model
        resp2079872_root_model_json = {}
        resp2079872_root_model_json['dashboard_url'] = 'testString'
        resp2079872_root_model_json['operation'] = 'testString'

        # Construct a model instance of Resp2079872Root by calling from_dict on the json representation
        resp2079872_root_model = Resp2079872Root.from_dict(resp2079872_root_model_json)
        assert resp2079872_root_model != False

        # Construct a model instance of Resp2079872Root by calling from_dict on the json representation
        resp2079872_root_model_dict = Resp2079872Root.from_dict(resp2079872_root_model_json).__dict__
        resp2079872_root_model2 = Resp2079872Root(**resp2079872_root_model_dict)

        # Verify the model instances are equivalent
        assert resp2079872_root_model == resp2079872_root_model2

        # Convert model instance back to dict and verify no loss of data
        resp2079872_root_model_json2 = resp2079872_root_model.to_dict()
        assert resp2079872_root_model_json2 == resp2079872_root_model_json


class TestResp2079874Root:
    """
    Test Class for Resp2079874Root
    """

    def test_resp2079874_root_serialization(self):
        """
        Test serialization/deserialization for Resp2079874Root
        """

        # Construct a json representation of a Resp2079874Root model
        resp2079874_root_model_json = {}
        resp2079874_root_model_json['operation'] = 'testString'

        # Construct a model instance of Resp2079874Root by calling from_dict on the json representation
        resp2079874_root_model = Resp2079874Root.from_dict(resp2079874_root_model_json)
        assert resp2079874_root_model != False

        # Construct a model instance of Resp2079874Root by calling from_dict on the json representation
        resp2079874_root_model_dict = Resp2079874Root.from_dict(resp2079874_root_model_json).__dict__
        resp2079874_root_model2 = Resp2079874Root(**resp2079874_root_model_dict)

        # Verify the model instances are equivalent
        assert resp2079874_root_model == resp2079874_root_model2

        # Convert model instance back to dict and verify no loss of data
        resp2079874_root_model_json2 = resp2079874_root_model.to_dict()
        assert resp2079874_root_model_json2 == resp2079874_root_model_json


class TestResp2079876Root:
    """
    Test Class for Resp2079876Root
    """

    def test_resp2079876_root_serialization(self):
        """
        Test serialization/deserialization for Resp2079876Root
        """

        # Construct dict forms of any model objects needed in order to build this model.

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['driver'] = 'testString'
        volume_mount_model['container_dir'] = 'testString'
        volume_mount_model['mode'] = 'testString'
        volume_mount_model['device_type'] = 'testString'
        volume_mount_model['device'] = 'testString'

        # Construct a json representation of a Resp2079876Root model
        resp2079876_root_model_json = {}
        resp2079876_root_model_json['credentials'] = {'foo': 'bar'}
        resp2079876_root_model_json['syslog_drain_url'] = 'testString'
        resp2079876_root_model_json['route_service_url'] = 'testString'
        resp2079876_root_model_json['volume_mounts'] = [volume_mount_model]

        # Construct a model instance of Resp2079876Root by calling from_dict on the json representation
        resp2079876_root_model = Resp2079876Root.from_dict(resp2079876_root_model_json)
        assert resp2079876_root_model != False

        # Construct a model instance of Resp2079876Root by calling from_dict on the json representation
        resp2079876_root_model_dict = Resp2079876Root.from_dict(resp2079876_root_model_json).__dict__
        resp2079876_root_model2 = Resp2079876Root(**resp2079876_root_model_dict)

        # Verify the model instances are equivalent
        assert resp2079876_root_model == resp2079876_root_model2

        # Convert model instance back to dict and verify no loss of data
        resp2079876_root_model_json2 = resp2079876_root_model.to_dict()
        assert resp2079876_root_model_json2 == resp2079876_root_model_json


class TestResp2079894Root:
    """
    Test Class for Resp2079894Root
    """

    def test_resp2079894_root_serialization(self):
        """
        Test serialization/deserialization for Resp2079894Root
        """

        # Construct a json representation of a Resp2079894Root model
        resp2079894_root_model_json = {}
        resp2079894_root_model_json['description'] = 'testString'
        resp2079894_root_model_json['state'] = 'testString'

        # Construct a model instance of Resp2079894Root by calling from_dict on the json representation
        resp2079894_root_model = Resp2079894Root.from_dict(resp2079894_root_model_json)
        assert resp2079894_root_model != False

        # Construct a model instance of Resp2079894Root by calling from_dict on the json representation
        resp2079894_root_model_dict = Resp2079894Root.from_dict(resp2079894_root_model_json).__dict__
        resp2079894_root_model2 = Resp2079894Root(**resp2079894_root_model_dict)

        # Verify the model instances are equivalent
        assert resp2079894_root_model == resp2079894_root_model2

        # Convert model instance back to dict and verify no loss of data
        resp2079894_root_model_json2 = resp2079894_root_model.to_dict()
        assert resp2079894_root_model_json2 == resp2079894_root_model_json


class TestResp2448145Root:
    """
    Test Class for Resp2448145Root
    """

    def test_resp2448145_root_serialization(self):
        """
        Test serialization/deserialization for Resp2448145Root
        """

        # Construct a json representation of a Resp2448145Root model
        resp2448145_root_model_json = {}
        resp2448145_root_model_json['active'] = True
        resp2448145_root_model_json['enabled'] = True
        resp2448145_root_model_json['last_active'] = 38

        # Construct a model instance of Resp2448145Root by calling from_dict on the json representation
        resp2448145_root_model = Resp2448145Root.from_dict(resp2448145_root_model_json)
        assert resp2448145_root_model != False

        # Construct a model instance of Resp2448145Root by calling from_dict on the json representation
        resp2448145_root_model_dict = Resp2448145Root.from_dict(resp2448145_root_model_json).__dict__
        resp2448145_root_model2 = Resp2448145Root(**resp2448145_root_model_dict)

        # Verify the model instances are equivalent
        assert resp2448145_root_model == resp2448145_root_model2

        # Convert model instance back to dict and verify no loss of data
        resp2448145_root_model_json2 = resp2448145_root_model.to_dict()
        assert resp2448145_root_model_json2 == resp2448145_root_model_json


class TestBindResource:
    """
    Test Class for BindResource
    """

    def test_bind_resource_serialization(self):
        """
        Test serialization/deserialization for BindResource
        """

        # Construct a json representation of a BindResource model
        bind_resource_model_json = {}
        bind_resource_model_json['account_id'] = 'null'
        bind_resource_model_json['serviceid_crn'] = 'null'
        bind_resource_model_json['target_crn'] = 'null'
        bind_resource_model_json['app_guid'] = 'null'
        bind_resource_model_json['route'] = 'null'

        # Construct a model instance of BindResource by calling from_dict on the json representation
        bind_resource_model = BindResource.from_dict(bind_resource_model_json)
        assert bind_resource_model != False

        # Construct a model instance of BindResource by calling from_dict on the json representation
        bind_resource_model_dict = BindResource.from_dict(bind_resource_model_json).__dict__
        bind_resource_model2 = BindResource(**bind_resource_model_dict)

        # Verify the model instances are equivalent
        assert bind_resource_model == bind_resource_model2

        # Convert model instance back to dict and verify no loss of data
        bind_resource_model_json2 = bind_resource_model.to_dict()
        assert bind_resource_model_json2 == bind_resource_model_json


class TestContext:
    """
    Test Class for Context
    """

    def test_context_serialization(self):
        """
        Test serialization/deserialization for Context
        """

        # Construct a json representation of a Context model
        context_model_json = {}
        context_model_json['account_id'] = 'null'
        context_model_json['crn'] = 'null'
        context_model_json['platform'] = 'null'

        # Construct a model instance of Context by calling from_dict on the json representation
        context_model = Context.from_dict(context_model_json)
        assert context_model != False

        # Construct a model instance of Context by calling from_dict on the json representation
        context_model_dict = Context.from_dict(context_model_json).__dict__
        context_model2 = Context(**context_model_dict)

        # Verify the model instances are equivalent
        assert context_model == context_model2

        # Convert model instance back to dict and verify no loss of data
        context_model_json2 = context_model.to_dict()
        assert context_model_json2 == context_model_json


class TestPlans:
    """
    Test Class for Plans
    """

    def test_plans_serialization(self):
        """
        Test serialization/deserialization for Plans
        """

        # Construct a json representation of a Plans model
        plans_model_json = {}
        plans_model_json['description'] = 'testString'
        plans_model_json['free'] = True
        plans_model_json['id'] = 'testString'
        plans_model_json['name'] = 'testString'

        # Construct a model instance of Plans by calling from_dict on the json representation
        plans_model = Plans.from_dict(plans_model_json)
        assert plans_model != False

        # Construct a model instance of Plans by calling from_dict on the json representation
        plans_model_dict = Plans.from_dict(plans_model_json).__dict__
        plans_model2 = Plans(**plans_model_dict)

        # Verify the model instances are equivalent
        assert plans_model == plans_model2

        # Convert model instance back to dict and verify no loss of data
        plans_model_json2 = plans_model.to_dict()
        assert plans_model_json2 == plans_model_json


class TestServices:
    """
    Test Class for Services
    """

    def test_services_serialization(self):
        """
        Test serialization/deserialization for Services
        """

        # Construct dict forms of any model objects needed in order to build this model.

        plans_model = {}  # Plans
        plans_model['description'] = 'testString'
        plans_model['free'] = True
        plans_model['id'] = 'testString'
        plans_model['name'] = 'testString'

        # Construct a json representation of a Services model
        services_model_json = {}
        services_model_json['bindable'] = True
        services_model_json['description'] = 'testString'
        services_model_json['id'] = 'testString'
        services_model_json['name'] = 'testString'
        services_model_json['plan_updateable'] = True
        services_model_json['plans'] = [plans_model]

        # Construct a model instance of Services by calling from_dict on the json representation
        services_model = Services.from_dict(services_model_json)
        assert services_model != False

        # Construct a model instance of Services by calling from_dict on the json representation
        services_model_dict = Services.from_dict(services_model_json).__dict__
        services_model2 = Services(**services_model_dict)

        # Verify the model instances are equivalent
        assert services_model == services_model2

        # Convert model instance back to dict and verify no loss of data
        services_model_json2 = services_model.to_dict()
        assert services_model_json2 == services_model_json


class TestVolumeMount:
    """
    Test Class for VolumeMount
    """

    def test_volume_mount_serialization(self):
        """
        Test serialization/deserialization for VolumeMount
        """

        # Construct a json representation of a VolumeMount model
        volume_mount_model_json = {}
        volume_mount_model_json['driver'] = 'testString'
        volume_mount_model_json['container_dir'] = 'testString'
        volume_mount_model_json['mode'] = 'testString'
        volume_mount_model_json['device_type'] = 'testString'
        volume_mount_model_json['device'] = 'testString'

        # Construct a model instance of VolumeMount by calling from_dict on the json representation
        volume_mount_model = VolumeMount.from_dict(volume_mount_model_json)
        assert volume_mount_model != False

        # Construct a model instance of VolumeMount by calling from_dict on the json representation
        volume_mount_model_dict = VolumeMount.from_dict(volume_mount_model_json).__dict__
        volume_mount_model2 = VolumeMount(**volume_mount_model_dict)

        # Verify the model instances are equivalent
        assert volume_mount_model == volume_mount_model2

        # Convert model instance back to dict and verify no loss of data
        volume_mount_model_json2 = volume_mount_model.to_dict()
        assert volume_mount_model_json2 == volume_mount_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
