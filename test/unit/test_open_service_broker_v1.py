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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
from ibm_platform_services.open_service_broker_v1 import *


service = OpenServiceBrokerV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://fake'
service.set_service_url(base_url)

##############################################################################
# Start of Service: EnableAndDisableInstances
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_service_instance_state
#-----------------------------------------------------------------------------
class TestGetServiceInstanceState():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_service_instance_state()
    #--------------------------------------------------------
    @responses.activate
    def test_get_service_instance_state_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.get_service_instance_state(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_service_instance_state_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_service_instance_state_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_service_instance_state(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for replace_state
#-----------------------------------------------------------------------------
class TestReplaceState():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # replace_state()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_state_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        enabled = False
        initiator_id = 'null'
        reason_code = 'null'

        # Invoke method
        response = service.replace_state(
            instance_id,
            enabled=enabled,
            initiator_id=initiator_id,
            reason_code=reason_code,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enabled'] == False
        assert req_body['initiator_id'] == 'null'
        assert req_body['reason_code'] == 'null'


    #--------------------------------------------------------
    # test_replace_state_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_state_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.replace_state(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_replace_state_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_state_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/bluemix_v1/service_instances/testString')
        mock_response = '{"active": true, "enabled": false, "last_active": 11}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_state(**req_copy)



# endregion
##############################################################################
# End of Service: EnableAndDisableInstances
##############################################################################

##############################################################################
# Start of Service: ResourceInstances
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for replace_service_instance
#-----------------------------------------------------------------------------
class TestReplaceServiceInstance():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # replace_service_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_instance_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"dashboard_url": "dashboard_url", "operation": "operation"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['account_id'] = 'null'
        context_model['crn'] = 'null'
        context_model['platform'] = 'null'

        # Construct a dict representation of a Parameters model
        parameters_model = {}
        parameters_model['parameter1'] = 38
        parameters_model['parameter2'] = 'null'

        # Set up parameter values
        instance_id = 'testString'
        organization_guid = 'null'
        plan_id = 'null'
        service_id = 'null'
        space_guid = 'null'
        context = [context_model]
        parameters = [parameters_model]
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'accepts_incomplete={}'.format('true' if accepts_incomplete else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['organization_guid'] == 'null'
        assert req_body['plan_id'] == 'null'
        assert req_body['service_id'] == 'null'
        assert req_body['space_guid'] == 'null'
        assert req_body['context'] == [context_model]
        assert req_body['parameters'] == [parameters_model]


    #--------------------------------------------------------
    # test_replace_service_instance_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_instance_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"dashboard_url": "dashboard_url", "operation": "operation"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.replace_service_instance(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_replace_service_instance_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_instance_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '{"dashboard_url": "dashboard_url", "operation": "operation"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_service_instance(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_service_instance
#-----------------------------------------------------------------------------
class TestUpdateServiceInstance():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_service_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_update_service_instance_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '"operation_response"'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['account_id'] = 'null'
        context_model['crn'] = 'null'
        context_model['platform'] = 'null'

        # Construct a dict representation of a Parameters model
        parameters_model = {}
        parameters_model['parameter1'] = 38
        parameters_model['parameter2'] = 'null'

        # Set up parameter values
        instance_id = 'testString'
        service_id = 'null'
        context = [context_model]
        parameters = parameters_model
        plan_id = 'null'
        previous_values = ['testString']
        accepts_incomplete = 'testString'

        # Invoke method
        response = service.update_service_instance(
            instance_id,
            service_id=service_id,
            context=context,
            parameters=parameters,
            plan_id=plan_id,
            previous_values=previous_values,
            accepts_incomplete=accepts_incomplete,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'accepts_incomplete={}'.format(accepts_incomplete) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['service_id'] == 'null'
        assert req_body['context'] == [context_model]
        assert req_body['parameters'] == parameters_model
        assert req_body['plan_id'] == 'null'
        assert req_body['previous_values'] == ['testString']


    #--------------------------------------------------------
    # test_update_service_instance_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_service_instance_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '"operation_response"'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.update_service_instance(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_service_instance_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_service_instance_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '"operation_response"'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_service_instance(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_service_instance
#-----------------------------------------------------------------------------
class TestDeleteServiceInstance():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_service_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_instance_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '"operation_response"'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        service_id = 'testString'
        plan_id = 'testString'
        instance_id = 'testString'
        accepts_incomplete = True

        # Invoke method
        response = service.delete_service_instance(
            service_id,
            plan_id,
            instance_id,
            accepts_incomplete=accepts_incomplete,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'service_id={}'.format(service_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'accepts_incomplete={}'.format('true' if accepts_incomplete else 'false') in query_string


    #--------------------------------------------------------
    # test_delete_service_instance_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_instance_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '"operation_response"'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        service_id = 'testString'
        plan_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = service.delete_service_instance(
            service_id,
            plan_id,
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'service_id={}'.format(service_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string


    #--------------------------------------------------------
    # test_delete_service_instance_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_instance_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString')
        mock_response = '"operation_response"'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
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

#-----------------------------------------------------------------------------
# Test Class for list_catalog
#-----------------------------------------------------------------------------
class TestListCatalog():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_catalog()
    #--------------------------------------------------------
    @responses.activate
    def test_list_catalog_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/catalog')
        mock_response = '[{"bindable": true, "description": "description", "id": "id", "name": "name", "plan_updateable": false, "plans": [{"description": "description", "free": true, "id": "id", "name": "name"}]}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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

#-----------------------------------------------------------------------------
# Test Class for list_last_operation
#-----------------------------------------------------------------------------
class TestListLastOperation():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_last_operation()
    #--------------------------------------------------------
    @responses.activate
    def test_list_last_operation_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/last_operation')
        mock_response = '{"description": "description", "state": "state"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        operation = 'testString'
        plan_id = 'testString'
        service_id = 'testString'

        # Invoke method
        response = service.list_last_operation(
            instance_id,
            operation=operation,
            plan_id=plan_id,
            service_id=service_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'operation={}'.format(operation) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'service_id={}'.format(service_id) in query_string


    #--------------------------------------------------------
    # test_list_last_operation_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_last_operation_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/last_operation')
        mock_response = '{"description": "description", "state": "state"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.list_last_operation(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_last_operation_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_last_operation_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/last_operation')
        mock_response = '{"description": "description", "state": "state"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_last_operation(**req_copy)



# endregion
##############################################################################
# End of Service: LastOperationAsync
##############################################################################

##############################################################################
# Start of Service: BindingsAndCredentials
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for replace_service_binding
#-----------------------------------------------------------------------------
class TestReplaceServiceBinding():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # replace_service_binding()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_binding_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        mock_response = '"operation_response"'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a BindResource model
        bind_resource_model = {}
        bind_resource_model['account_id'] = 'null'
        bind_resource_model['serviceid_crn'] = 'null'
        bind_resource_model['target_crn'] = 'null'

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'
        bind_resource = [bind_resource_model]
        parameters = { 'foo': 'bar' }
        plan_id = 'null'
        service_id = 'null'

        # Invoke method
        response = service.replace_service_binding(
            binding_id,
            instance_id,
            bind_resource=bind_resource,
            parameters=parameters,
            plan_id=plan_id,
            service_id=service_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['bind_resource'] == [bind_resource_model]
        assert req_body['parameters'] == { 'foo': 'bar' }
        assert req_body['plan_id'] == 'null'
        assert req_body['service_id'] == 'null'


    #--------------------------------------------------------
    # test_replace_service_binding_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_binding_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        mock_response = '"operation_response"'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = service.replace_service_binding(
            binding_id,
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_replace_service_binding_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_binding_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        mock_response = '"operation_response"'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "binding_id": binding_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_service_binding(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_service_binding
#-----------------------------------------------------------------------------
class TestDeleteServiceBinding():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_service_binding()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_binding_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        mock_response = '"operation_response"'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'
        plan_id = 'testString'
        service_id = 'testString'

        # Invoke method
        response = service.delete_service_binding(
            binding_id,
            instance_id,
            plan_id,
            service_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'service_id={}'.format(service_id) in query_string


    #--------------------------------------------------------
    # test_delete_service_binding_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_binding_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/service_instances/testString/service_bindings/testString')
        mock_response = '"operation_response"'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
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
#-----------------------------------------------------------------------------
# Test Class for Resp1874644Root
#-----------------------------------------------------------------------------
class TestResp1874644Root():

    #--------------------------------------------------------
    # Test serialization/deserialization for Resp1874644Root
    #--------------------------------------------------------
    def test_resp1874644_root_serialization(self):

        # Construct a json representation of a Resp1874644Root model
        resp1874644_root_model_json = {}
        resp1874644_root_model_json['active'] = True
        resp1874644_root_model_json['enabled'] = True
        resp1874644_root_model_json['last_active'] = 36.0

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

#-----------------------------------------------------------------------------
# Test Class for Resp2079872Root
#-----------------------------------------------------------------------------
class TestResp2079872Root():

    #--------------------------------------------------------
    # Test serialization/deserialization for Resp2079872Root
    #--------------------------------------------------------
    def test_resp2079872_root_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for Resp2079894Root
#-----------------------------------------------------------------------------
class TestResp2079894Root():

    #--------------------------------------------------------
    # Test serialization/deserialization for Resp2079894Root
    #--------------------------------------------------------
    def test_resp2079894_root_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for Resp2448145Root
#-----------------------------------------------------------------------------
class TestResp2448145Root():

    #--------------------------------------------------------
    # Test serialization/deserialization for Resp2448145Root
    #--------------------------------------------------------
    def test_resp2448145_root_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for BindResource
#-----------------------------------------------------------------------------
class TestBindResource():

    #--------------------------------------------------------
    # Test serialization/deserialization for BindResource
    #--------------------------------------------------------
    def test_bind_resource_serialization(self):

        # Construct a json representation of a BindResource model
        bind_resource_model_json = {}
        bind_resource_model_json['account_id'] = 'null'
        bind_resource_model_json['serviceid_crn'] = 'null'
        bind_resource_model_json['target_crn'] = 'null'

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

#-----------------------------------------------------------------------------
# Test Class for Context
#-----------------------------------------------------------------------------
class TestContext():

    #--------------------------------------------------------
    # Test serialization/deserialization for Context
    #--------------------------------------------------------
    def test_context_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for Parameters
#-----------------------------------------------------------------------------
class TestParameters():

    #--------------------------------------------------------
    # Test serialization/deserialization for Parameters
    #--------------------------------------------------------
    def test_parameters_serialization(self):

        # Construct a json representation of a Parameters model
        parameters_model_json = {}
        parameters_model_json['parameter1'] = 38
        parameters_model_json['parameter2'] = 'null'

        # Construct a model instance of Parameters by calling from_dict on the json representation
        parameters_model = Parameters.from_dict(parameters_model_json)
        assert parameters_model != False

        # Construct a model instance of Parameters by calling from_dict on the json representation
        parameters_model_dict = Parameters.from_dict(parameters_model_json).__dict__
        parameters_model2 = Parameters(**parameters_model_dict)

        # Verify the model instances are equivalent
        assert parameters_model == parameters_model2

        # Convert model instance back to dict and verify no loss of data
        parameters_model_json2 = parameters_model.to_dict()
        assert parameters_model_json2 == parameters_model_json

#-----------------------------------------------------------------------------
# Test Class for Plans
#-----------------------------------------------------------------------------
class TestPlans():

    #--------------------------------------------------------
    # Test serialization/deserialization for Plans
    #--------------------------------------------------------
    def test_plans_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for Services
#-----------------------------------------------------------------------------
class TestServices():

    #--------------------------------------------------------
    # Test serialization/deserialization for Services
    #--------------------------------------------------------
    def test_services_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        plans_model = {} # Plans
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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
