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

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from platform_services.resource_controller_v2 import *


service = ResourceControllerV2(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://resource-controller.cloud.ibm.com/v2'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ResourceInstances
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_resource_instances
#-----------------------------------------------------------------------------
class TestListResourceInstances():

    #--------------------------------------------------------
    # list_resource_instances()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_instances_all_params(self):
        # Set up mock
        url = base_url + '/resource_instances'
        mock_response = '{"next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}], "rows_count": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        guid = 'testString'
        name = 'testString'
        resource_group_id = 'testString'
        resource_id = 'testString'
        resource_plan_id = 'testString'
        type = 'testString'
        sub_type = 'testString'
        limit = 'testString'
        updated_from = 'testString'
        updated_to = 'testString'

        # Invoke method
        response = service.list_resource_instances(
            guid=guid,
            name=name,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            resource_plan_id=resource_plan_id,
            type=type,
            sub_type=sub_type,
            limit=limit,
            updated_from=updated_from,
            updated_to=updated_to
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'guid={}'.format(guid) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'resource_plan_id={}'.format(resource_plan_id) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'sub_type={}'.format(sub_type) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'updated_from={}'.format(updated_from) in query_string
        assert 'updated_to={}'.format(updated_to) in query_string


    #--------------------------------------------------------
    # test_list_resource_instances_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_instances_required_params(self):
        # Set up mock
        url = base_url + '/resource_instances'
        mock_response = '{"next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}], "rows_count": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_resource_instances()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_resource_instance
#-----------------------------------------------------------------------------
class TestCreateResourceInstance():

    #--------------------------------------------------------
    # create_resource_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_instance_all_params(self):
        # Set up mock
        url = base_url + '/resource_instances'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'my-instance'
        target = 'bluemix-us-south'
        resource_group = '5c49eabc-f5e8-5881-a37e-2d100a33b3df'
        resource_plan_id = 'cloudant-standard'
        tags = ['testString']
        allow_cleanup = True
        parameters = {}

        # Invoke method
        response = service.create_resource_instance(
            name,
            target,
            resource_group,
            resource_plan_id,
            tags=tags,
            allow_cleanup=allow_cleanup,
            parameters=parameters,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['target'] == target
        assert req_body['resource_group'] == resource_group
        assert req_body['resource_plan_id'] == resource_plan_id
        assert req_body['tags'] == tags
        assert req_body['allow_cleanup'] == allow_cleanup
        assert req_body['parameters'] == parameters


    #--------------------------------------------------------
    # test_create_resource_instance_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_instance_required_params(self):
        # Set up mock
        url = base_url + '/resource_instances'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'my-instance'
        target = 'bluemix-us-south'
        resource_group = '5c49eabc-f5e8-5881-a37e-2d100a33b3df'
        resource_plan_id = 'cloudant-standard'
        tags = ['testString']
        allow_cleanup = True
        parameters = {}

        # Invoke method
        response = service.create_resource_instance(
            name,
            target,
            resource_group,
            resource_plan_id,
            tags=tags,
            allow_cleanup=allow_cleanup,
            parameters=parameters,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['target'] == target
        assert req_body['resource_group'] == resource_group
        assert req_body['resource_plan_id'] == resource_plan_id
        assert req_body['tags'] == tags
        assert req_body['allow_cleanup'] == allow_cleanup
        assert req_body['parameters'] == parameters


#-----------------------------------------------------------------------------
# Test Class for get_resource_instance
#-----------------------------------------------------------------------------
class TestGetResourceInstance():

    #--------------------------------------------------------
    # get_resource_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_instance_all_params(self):
        # Set up mock
        url = base_url + '/resource_instances/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_instance(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_instance_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_instance_required_params(self):
        # Set up mock
        url = base_url + '/resource_instances/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_instance(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_resource_instance
#-----------------------------------------------------------------------------
class TestDeleteResourceInstance():

    #--------------------------------------------------------
    # delete_resource_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_instance_all_params(self):
        # Set up mock
        url = base_url + '/resource_instances/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_instance(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_delete_resource_instance_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_instance_required_params(self):
        # Set up mock
        url = base_url + '/resource_instances/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_instance(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


#-----------------------------------------------------------------------------
# Test Class for update_resource_instance
#-----------------------------------------------------------------------------
class TestUpdateResourceInstance():

    #--------------------------------------------------------
    # update_resource_instance()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_instance_all_params(self):
        # Set up mock
        url = base_url + '/resource_instances/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        name = 'my-new-instance-name'
        parameters = {}
        resource_plan_id = 'a8dff6d3-d287-4668-a81d-c87c55c2656d'
        allow_cleanup = True

        # Invoke method
        response = service.update_resource_instance(
            id,
            name=name,
            parameters=parameters,
            resource_plan_id=resource_plan_id,
            allow_cleanup=allow_cleanup,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['parameters'] == parameters
        assert req_body['resource_plan_id'] == resource_plan_id
        assert req_body['allow_cleanup'] == allow_cleanup


    #--------------------------------------------------------
    # test_update_resource_instance_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_instance_required_params(self):
        # Set up mock
        url = base_url + '/resource_instances/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "resource_id": "resource_id", "resource_plan_id": "resource_plan_id", "target_crn": "target_crn", "state": "state", "type": "type", "sub_type": "sub_type", "allow_cleanup": false, "last_operation": {"mapKey": {"anyKey": "anyValue"}}, "dashboard_url": "dashboard_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00"}], "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        name = 'my-new-instance-name'
        parameters = {}
        resource_plan_id = 'a8dff6d3-d287-4668-a81d-c87c55c2656d'
        allow_cleanup = True

        # Invoke method
        response = service.update_resource_instance(
            id,
            name=name,
            parameters=parameters,
            resource_plan_id=resource_plan_id,
            allow_cleanup=allow_cleanup,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['parameters'] == parameters
        assert req_body['resource_plan_id'] == resource_plan_id
        assert req_body['allow_cleanup'] == allow_cleanup


# endregion
##############################################################################
# End of Service: ResourceInstances
##############################################################################

##############################################################################
# Start of Service: ResourceKeys
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_resource_keys
#-----------------------------------------------------------------------------
class TestListResourceKeys():

    #--------------------------------------------------------
    # list_resource_keys()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_keys_all_params(self):
        # Set up mock
        url = base_url + '/resource_keys'
        mock_response = '{"next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_instance_url": "resource_instance_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}], "rows_count": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        guid = 'testString'
        name = 'testString'
        resource_group_id = 'testString'
        resource_id = 'testString'
        limit = 'testString'
        updated_from = 'testString'
        updated_to = 'testString'

        # Invoke method
        response = service.list_resource_keys(
            guid=guid,
            name=name,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            limit=limit,
            updated_from=updated_from,
            updated_to=updated_to
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'guid={}'.format(guid) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'updated_from={}'.format(updated_from) in query_string
        assert 'updated_to={}'.format(updated_to) in query_string


    #--------------------------------------------------------
    # test_list_resource_keys_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_keys_required_params(self):
        # Set up mock
        url = base_url + '/resource_keys'
        mock_response = '{"next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_instance_url": "resource_instance_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}], "rows_count": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_resource_keys()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_resource_key
#-----------------------------------------------------------------------------
class TestCreateResourceKey():

    #--------------------------------------------------------
    # create_resource_key()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_key_all_params(self):
        # Set up mock
        url = base_url + '/resource_keys'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_instance_url": "resource_instance_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ResourceKeyPostParameters model
        resource_key_post_parameters_model = {}
        resource_key_post_parameters_model['serviceid_crn'] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393' 

        # Set up parameter values
        name = 'my-key'
        source = '25eba2a9-beef-450b-82cf-f5ad5e36c6dd'
        parameters = resource_key_post_parameters_model
        role = 'Writer'

        # Invoke method
        response = service.create_resource_key(
            name,
            source,
            parameters=parameters,
            role=role,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['source'] == source
        assert req_body['parameters'] == parameters
        assert req_body['role'] == role


    #--------------------------------------------------------
    # test_create_resource_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_key_required_params(self):
        # Set up mock
        url = base_url + '/resource_keys'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_instance_url": "resource_instance_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ResourceKeyPostParameters model
        resource_key_post_parameters_model = {}
        resource_key_post_parameters_model['serviceid_crn'] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393' 

        # Set up parameter values
        name = 'my-key'
        source = '25eba2a9-beef-450b-82cf-f5ad5e36c6dd'
        parameters = resource_key_post_parameters_model
        role = 'Writer'

        # Invoke method
        response = service.create_resource_key(
            name,
            source,
            parameters=parameters,
            role=role,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['source'] == source
        assert req_body['parameters'] == parameters
        assert req_body['role'] == role


#-----------------------------------------------------------------------------
# Test Class for get_resource_key
#-----------------------------------------------------------------------------
class TestGetResourceKey():

    #--------------------------------------------------------
    # get_resource_key()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_key_all_params(self):
        # Set up mock
        url = base_url + '/resource_keys/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_instance_url": "resource_instance_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_key_required_params(self):
        # Set up mock
        url = base_url + '/resource_keys/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_instance_url": "resource_instance_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_resource_key
#-----------------------------------------------------------------------------
class TestDeleteResourceKey():

    #--------------------------------------------------------
    # delete_resource_key()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_key_all_params(self):
        # Set up mock
        url = base_url + '/resource_keys/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_resource_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_key_required_params(self):
        # Set up mock
        url = base_url + '/resource_keys/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for update_resource_key
#-----------------------------------------------------------------------------
class TestUpdateResourceKey():

    #--------------------------------------------------------
    # update_resource_key()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_key_all_params(self):
        # Set up mock
        url = base_url + '/resource_keys/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_instance_url": "resource_instance_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        name = 'my-new-key-name'

        # Invoke method
        response = service.update_resource_key(
            id,
            name,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name


    #--------------------------------------------------------
    # test_update_resource_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_key_required_params(self):
        # Set up mock
        url = base_url + '/resource_keys/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_instance_url": "resource_instance_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        name = 'my-new-key-name'

        # Invoke method
        response = service.update_resource_key(
            id,
            name,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name


# endregion
##############################################################################
# End of Service: ResourceKeys
##############################################################################

##############################################################################
# Start of Service: ResourceBindings
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_resource_bindings
#-----------------------------------------------------------------------------
class TestListResourceBindings():

    #--------------------------------------------------------
    # list_resource_bindings()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_bindings_all_params(self):
        # Set up mock
        url = base_url + '/resource_bindings'
        mock_response = '{"next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "target_crn": "target_crn", "region_binding_id": "region_binding_id", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_alias_url": "resource_alias_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}], "rows_count": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        guid = 'testString'
        name = 'testString'
        resource_group_id = 'testString'
        resource_id = 'testString'
        region_binding_id = 'testString'
        limit = 'testString'
        updated_from = 'testString'
        updated_to = 'testString'

        # Invoke method
        response = service.list_resource_bindings(
            guid=guid,
            name=name,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            region_binding_id=region_binding_id,
            limit=limit,
            updated_from=updated_from,
            updated_to=updated_to
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'guid={}'.format(guid) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'region_binding_id={}'.format(region_binding_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'updated_from={}'.format(updated_from) in query_string
        assert 'updated_to={}'.format(updated_to) in query_string


    #--------------------------------------------------------
    # test_list_resource_bindings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_bindings_required_params(self):
        # Set up mock
        url = base_url + '/resource_bindings'
        mock_response = '{"next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "target_crn": "target_crn", "region_binding_id": "region_binding_id", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_alias_url": "resource_alias_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}], "rows_count": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_resource_bindings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_resource_binding
#-----------------------------------------------------------------------------
class TestCreateResourceBinding():

    #--------------------------------------------------------
    # create_resource_binding()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_binding_all_params(self):
        # Set up mock
        url = base_url + '/resource_bindings'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "target_crn": "target_crn", "region_binding_id": "region_binding_id", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_alias_url": "resource_alias_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ResourceBindingPostParameters model
        resource_binding_post_parameters_model = {}
        resource_binding_post_parameters_model['serviceid_crn'] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393' 

        # Set up parameter values
        source = '25eba2a9-beef-450b-82cf-f5ad5e36c6dd'
        target = 'crn:v1:bluemix:public:bluemix:us-south:s/0ba4dba0-a120-4a1e-a124-5a249a904b76::cf-application:a1caa40b-2c24-4da8-8267-ac2c1a42ad0c'
        name = 'my-binding'
        parameters = resource_binding_post_parameters_model
        role = 'Writer'

        # Invoke method
        response = service.create_resource_binding(
            source,
            target,
            name=name,
            parameters=parameters,
            role=role,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source'] == source
        assert req_body['target'] == target
        assert req_body['name'] == name
        assert req_body['parameters'] == parameters
        assert req_body['role'] == role


    #--------------------------------------------------------
    # test_create_resource_binding_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_binding_required_params(self):
        # Set up mock
        url = base_url + '/resource_bindings'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "target_crn": "target_crn", "region_binding_id": "region_binding_id", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_alias_url": "resource_alias_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ResourceBindingPostParameters model
        resource_binding_post_parameters_model = {}
        resource_binding_post_parameters_model['serviceid_crn'] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393' 

        # Set up parameter values
        source = '25eba2a9-beef-450b-82cf-f5ad5e36c6dd'
        target = 'crn:v1:bluemix:public:bluemix:us-south:s/0ba4dba0-a120-4a1e-a124-5a249a904b76::cf-application:a1caa40b-2c24-4da8-8267-ac2c1a42ad0c'
        name = 'my-binding'
        parameters = resource_binding_post_parameters_model
        role = 'Writer'

        # Invoke method
        response = service.create_resource_binding(
            source,
            target,
            name=name,
            parameters=parameters,
            role=role,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source'] == source
        assert req_body['target'] == target
        assert req_body['name'] == name
        assert req_body['parameters'] == parameters
        assert req_body['role'] == role


#-----------------------------------------------------------------------------
# Test Class for get_resource_binding
#-----------------------------------------------------------------------------
class TestGetResourceBinding():

    #--------------------------------------------------------
    # get_resource_binding()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_binding_all_params(self):
        # Set up mock
        url = base_url + '/resource_bindings/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "target_crn": "target_crn", "region_binding_id": "region_binding_id", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_alias_url": "resource_alias_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_binding(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_binding_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_binding_required_params(self):
        # Set up mock
        url = base_url + '/resource_bindings/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "target_crn": "target_crn", "region_binding_id": "region_binding_id", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_alias_url": "resource_alias_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_binding(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_resource_binding
#-----------------------------------------------------------------------------
class TestDeleteResourceBinding():

    #--------------------------------------------------------
    # delete_resource_binding()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_binding_all_params(self):
        # Set up mock
        url = base_url + '/resource_bindings/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_binding(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_resource_binding_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_binding_required_params(self):
        # Set up mock
        url = base_url + '/resource_bindings/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_binding(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for update_resource_binding
#-----------------------------------------------------------------------------
class TestUpdateResourceBinding():

    #--------------------------------------------------------
    # update_resource_binding()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_binding_all_params(self):
        # Set up mock
        url = base_url + '/resource_bindings/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "target_crn": "target_crn", "region_binding_id": "region_binding_id", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_alias_url": "resource_alias_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        name = 'my-new-binding-name'

        # Invoke method
        response = service.update_resource_binding(
            id,
            name,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name


    #--------------------------------------------------------
    # test_update_resource_binding_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_binding_required_params(self):
        # Set up mock
        url = base_url + '/resource_bindings/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "source_crn": "source_crn", "target_crn": "target_crn", "region_binding_id": "region_binding_id", "state": "state", "credentials": {"apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_alias_url": "resource_alias_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        name = 'my-new-binding-name'

        # Invoke method
        response = service.update_resource_binding(
            id,
            name,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name


# endregion
##############################################################################
# End of Service: ResourceBindings
##############################################################################

##############################################################################
# Start of Service: ResourceAliases
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_resource_aliases
#-----------------------------------------------------------------------------
class TestListResourceAliases():

    #--------------------------------------------------------
    # list_resource_aliases()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_aliases_all_params(self):
        # Set up mock
        url = base_url + '/resource_aliases'
        mock_response = '{"next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "state": "state", "resource_instance_id": "resource_instance_id", "region_instance_id": "region_instance_id", "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}], "rows_count": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        guid = 'testString'
        name = 'testString'
        resource_instance_id = 'testString'
        region_instance_id = 'testString'
        resource_id = 'testString'
        resource_group_id = 'testString'
        limit = 'testString'
        updated_from = 'testString'
        updated_to = 'testString'

        # Invoke method
        response = service.list_resource_aliases(
            guid=guid,
            name=name,
            resource_instance_id=resource_instance_id,
            region_instance_id=region_instance_id,
            resource_id=resource_id,
            resource_group_id=resource_group_id,
            limit=limit,
            updated_from=updated_from,
            updated_to=updated_to
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'guid={}'.format(guid) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string
        assert 'region_instance_id={}'.format(region_instance_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'updated_from={}'.format(updated_from) in query_string
        assert 'updated_to={}'.format(updated_to) in query_string


    #--------------------------------------------------------
    # test_list_resource_aliases_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_aliases_required_params(self):
        # Set up mock
        url = base_url + '/resource_aliases'
        mock_response = '{"next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "state": "state", "resource_instance_id": "resource_instance_id", "region_instance_id": "region_instance_id", "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}], "rows_count": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_resource_aliases()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_resource_alias
#-----------------------------------------------------------------------------
class TestCreateResourceAlias():

    #--------------------------------------------------------
    # create_resource_alias()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_alias_all_params(self):
        # Set up mock
        url = base_url + '/resource_aliases'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "state": "state", "resource_instance_id": "resource_instance_id", "region_instance_id": "region_instance_id", "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'my-alias'
        source = 'a8dff6d3-d287-4668-a81d-c87c55c2656d'
        target = 'crn:v1:staging:public:bluemix:us-south:o/5e939cd5-6377-4383-b9e0-9db22cd11753::cf-space:66c8b915-101a-406c-a784-e6636676e4f5'

        # Invoke method
        response = service.create_resource_alias(
            name,
            source,
            target,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['source'] == source
        assert req_body['target'] == target


    #--------------------------------------------------------
    # test_create_resource_alias_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_alias_required_params(self):
        # Set up mock
        url = base_url + '/resource_aliases'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "state": "state", "resource_instance_id": "resource_instance_id", "region_instance_id": "region_instance_id", "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'my-alias'
        source = 'a8dff6d3-d287-4668-a81d-c87c55c2656d'
        target = 'crn:v1:staging:public:bluemix:us-south:o/5e939cd5-6377-4383-b9e0-9db22cd11753::cf-space:66c8b915-101a-406c-a784-e6636676e4f5'

        # Invoke method
        response = service.create_resource_alias(
            name,
            source,
            target,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['source'] == source
        assert req_body['target'] == target


#-----------------------------------------------------------------------------
# Test Class for get_resource_alias
#-----------------------------------------------------------------------------
class TestGetResourceAlias():

    #--------------------------------------------------------
    # get_resource_alias()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_alias_all_params(self):
        # Set up mock
        url = base_url + '/resource_aliases/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "state": "state", "resource_instance_id": "resource_instance_id", "region_instance_id": "region_instance_id", "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_alias(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_alias_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_alias_required_params(self):
        # Set up mock
        url = base_url + '/resource_aliases/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "state": "state", "resource_instance_id": "resource_instance_id", "region_instance_id": "region_instance_id", "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_alias(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_resource_alias
#-----------------------------------------------------------------------------
class TestDeleteResourceAlias():

    #--------------------------------------------------------
    # delete_resource_alias()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_alias_all_params(self):
        # Set up mock
        url = base_url + '/resource_aliases/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_alias(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_resource_alias_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_alias_required_params(self):
        # Set up mock
        url = base_url + '/resource_aliases/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_alias(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for update_resource_alias
#-----------------------------------------------------------------------------
class TestUpdateResourceAlias():

    #--------------------------------------------------------
    # update_resource_alias()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_alias_all_params(self):
        # Set up mock
        url = base_url + '/resource_aliases/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "state": "state", "resource_instance_id": "resource_instance_id", "region_instance_id": "region_instance_id", "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        name = 'my-new-alias-name'

        # Invoke method
        response = service.update_resource_alias(
            id,
            name,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name


    #--------------------------------------------------------
    # test_update_resource_alias_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_alias_required_params(self):
        # Set up mock
        url = base_url + '/resource_aliases/testString'
        mock_response = '{"id": "id", "guid": "guid", "crn": "crn", "url": "url", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "state": "state", "resource_instance_id": "resource_instance_id", "region_instance_id": "region_instance_id", "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00", "deleted_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        name = 'my-new-alias-name'

        # Invoke method
        response = service.update_resource_alias(
            id,
            name,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name


# endregion
##############################################################################
# End of Service: ResourceAliases
##############################################################################

##############################################################################
# Start of Service: ResourceReclamations
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_reclamations
#-----------------------------------------------------------------------------
class TestListReclamations():

    #--------------------------------------------------------
    # list_reclamations()
    #--------------------------------------------------------
    @responses.activate
    def test_list_reclamations_all_params(self):
        # Set up mock
        url = base_url + '/v1/reclamations'
        mock_response = '{"resources": [{"id": "id", "entity_id": "entity_id", "entity_type_id": "entity_type_id", "entity_crn": "entity_crn", "resource_instance_id": {"anyKey": "anyValue"}, "resource_group_id": "resource_group_id", "account_id": "account_id", "policy_id": "policy_id", "state": "state", "target_time": "target_time", "custom_properties": "custom_properties", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_instance_id = 'testString'

        # Invoke method
        response = service.list_reclamations(
            account_id=account_id,
            resource_instance_id=resource_instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string


    #--------------------------------------------------------
    # test_list_reclamations_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_reclamations_required_params(self):
        # Set up mock
        url = base_url + '/v1/reclamations'
        mock_response = '{"resources": [{"id": "id", "entity_id": "entity_id", "entity_type_id": "entity_type_id", "entity_crn": "entity_crn", "resource_instance_id": {"anyKey": "anyValue"}, "resource_group_id": "resource_group_id", "account_id": "account_id", "policy_id": "policy_id", "state": "state", "target_time": "target_time", "custom_properties": "custom_properties", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_reclamations()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for run_reclamation_action
#-----------------------------------------------------------------------------
class TestRunReclamationAction():

    #--------------------------------------------------------
    # run_reclamation_action()
    #--------------------------------------------------------
    @responses.activate
    def test_run_reclamation_action_all_params(self):
        # Set up mock
        url = base_url + '/v1/reclamations/testString/actions/testString'
        mock_response = '{"id": "id", "entity_id": "entity_id", "entity_type_id": "entity_type_id", "entity_crn": "entity_crn", "resource_instance_id": {"anyKey": "anyValue"}, "resource_group_id": "resource_group_id", "account_id": "account_id", "policy_id": "policy_id", "state": "state", "target_time": "target_time", "custom_properties": "custom_properties", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        action_name = 'testString'
        request_by = 'testString'
        comment = 'testString'

        # Invoke method
        response = service.run_reclamation_action(
            id,
            action_name,
            request_by=request_by,
            comment=comment,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['request_by'] == request_by
        assert req_body['comment'] == comment


    #--------------------------------------------------------
    # test_run_reclamation_action_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_run_reclamation_action_required_params(self):
        # Set up mock
        url = base_url + '/v1/reclamations/testString/actions/testString'
        mock_response = '{"id": "id", "entity_id": "entity_id", "entity_type_id": "entity_type_id", "entity_crn": "entity_crn", "resource_instance_id": {"anyKey": "anyValue"}, "resource_group_id": "resource_group_id", "account_id": "account_id", "policy_id": "policy_id", "state": "state", "target_time": "target_time", "custom_properties": "custom_properties", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        action_name = 'testString'

        # Invoke method
        response = service.run_reclamation_action(
            id,
            action_name
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ResourceReclamations
##############################################################################

