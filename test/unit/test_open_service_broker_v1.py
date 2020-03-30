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
import requests
import responses
from platform_services.open_service_broker_v1 import *


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

    #--------------------------------------------------------
    # get_service_instance_state()
    #--------------------------------------------------------
    @responses.activate
    def test_get_service_instance_state_all_params(self):
        # Set up mock
        url = base_url + '/bluemix_v1/service_instances/testString'
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
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_service_instance_state_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_service_instance_state_required_params(self):
        # Set up mock
        url = base_url + '/bluemix_v1/service_instances/testString'
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
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for replace_state
#-----------------------------------------------------------------------------
class TestReplaceState():

    #--------------------------------------------------------
    # replace_state()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_state_all_params(self):
        # Set up mock
        url = base_url + '/bluemix_v1/service_instances/testString'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enabled'] == enabled
        assert req_body['initiator_id'] == initiator_id
        assert req_body['reason_code'] == reason_code


    #--------------------------------------------------------
    # test_replace_state_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_state_required_params(self):
        # Set up mock
        url = base_url + '/bluemix_v1/service_instances/testString'
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
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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

    #--------------------------------------------------------
    # replace_service_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_instance_all_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString'
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
            accepts_incomplete=accepts_incomplete
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
        assert req_body['organization_guid'] == organization_guid
        assert req_body['plan_id'] == plan_id
        assert req_body['service_id'] == service_id
        assert req_body['space_guid'] == space_guid
        assert req_body['context'] == context
        assert req_body['parameters'] == parameters


    #--------------------------------------------------------
    # test_replace_service_instance_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_instance_required_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString'
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
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_service_instance
#-----------------------------------------------------------------------------
class TestUpdateServiceInstance():

    #--------------------------------------------------------
    # update_service_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_update_service_instance_all_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString'
        responses.add(responses.PATCH,
                      url,
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
            accepts_incomplete=accepts_incomplete
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
        assert req_body['service_id'] == service_id
        assert req_body['context'] == context
        assert req_body['parameters'] == parameters
        assert req_body['plan_id'] == plan_id
        assert req_body['previous_values'] == previous_values


    #--------------------------------------------------------
    # test_update_service_instance_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_service_instance_required_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString'
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.update_service_instance(
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_service_instance
#-----------------------------------------------------------------------------
class TestDeleteServiceInstance():

    #--------------------------------------------------------
    # delete_service_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_instance_all_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString'
        responses.add(responses.DELETE,
                      url,
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
            accepts_incomplete=accepts_incomplete
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
        url = base_url + '/v2/service_instances/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        service_id = 'testString'
        plan_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = service.delete_service_instance(
            service_id,
            plan_id,
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'service_id={}'.format(service_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string


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

    #--------------------------------------------------------
    # list_catalog()
    #--------------------------------------------------------
    @responses.activate
    def test_list_catalog_all_params(self):
        # Set up mock
        url = base_url + '/v2/catalog'
        mock_response = '[{}]'
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


    #--------------------------------------------------------
    # test_list_catalog_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_catalog_required_params(self):
        # Set up mock
        url = base_url + '/v2/catalog'
        mock_response = '[{}]'
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

    #--------------------------------------------------------
    # list_last_operation()
    #--------------------------------------------------------
    @responses.activate
    def test_list_last_operation_all_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString/last_operation'
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
            service_id=service_id
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
        url = base_url + '/v2/service_instances/testString/last_operation'
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
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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

    #--------------------------------------------------------
    # replace_service_binding()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_binding_all_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString/service_bindings/testString'
        responses.add(responses.PUT,
                      url,
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['bind_resource'] == bind_resource
        assert req_body['parameters'] == parameters
        assert req_body['plan_id'] == plan_id
        assert req_body['service_id'] == service_id


    #--------------------------------------------------------
    # test_replace_service_binding_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_service_binding_required_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString/service_bindings/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        binding_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = service.replace_service_binding(
            binding_id,
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_service_binding
#-----------------------------------------------------------------------------
class TestDeleteServiceBinding():

    #--------------------------------------------------------
    # delete_service_binding()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_binding_all_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString/service_bindings/testString'
        responses.add(responses.DELETE,
                      url,
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
            service_id
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
    # test_delete_service_binding_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_binding_required_params(self):
        # Set up mock
        url = base_url + '/v2/service_instances/testString/service_bindings/testString'
        responses.add(responses.DELETE,
                      url,
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
            service_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'service_id={}'.format(service_id) in query_string


# endregion
##############################################################################
# End of Service: BindingsAndCredentials
##############################################################################

