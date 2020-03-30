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
from platform_services.iam_policy_management_v1 import *


service = IamPolicyManagementV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://iam.test.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Policies
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_policies
#-----------------------------------------------------------------------------
class TestListPolicies():

    #--------------------------------------------------------
    # list_policies()
    #--------------------------------------------------------
    @responses.activate
    def test_list_policies_all_params(self):
        # Set up mock
        url = base_url + '/v1/policies'
        mock_response = '{"policies": [{"id": "id", "type": "type", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        accept_language = 'testString'
        iam_id = 'testString'
        access_group_id = 'testString'
        type = 'testString'
        service_type = 'testString'

        # Invoke method
        response = service.list_policies(
            account_id,
            accept_language=accept_language,
            iam_id=iam_id,
            access_group_id=access_group_id,
            type=type,
            service_type=service_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'iam_id={}'.format(iam_id) in query_string
        assert 'access_group_id={}'.format(access_group_id) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'service_type={}'.format(service_type) in query_string


    #--------------------------------------------------------
    # test_list_policies_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_policies_required_params(self):
        # Set up mock
        url = base_url + '/v1/policies'
        mock_response = '{"policies": [{"id": "id", "type": "type", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.list_policies(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string


#-----------------------------------------------------------------------------
# Test Class for create_policy
#-----------------------------------------------------------------------------
class TestCreatePolicy():

    #--------------------------------------------------------
    # create_policy()
    #--------------------------------------------------------
    @responses.activate
    def test_create_policy_all_params(self):
        # Set up mock
        url = base_url + '/v1/policies'
        mock_response = '{"id": "id", "type": "type", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PolicyRequestSubjectsItemAttributesItem model
        policy_request_subjects_item_attributes_item_model = {}
        policy_request_subjects_item_attributes_item_model['name'] = 'testString' 
        policy_request_subjects_item_attributes_item_model['value'] = 'testString' 

        # Construct a dict representation of a PolicyRequestSubjectsItem model
        policy_request_subjects_item_model = {}
        policy_request_subjects_item_model['attributes'] = [policy_request_subjects_item_attributes_item_model] 

        # Construct a dict representation of a PolicyRequestRolesItem model
        policy_request_roles_item_model = {}
        policy_request_roles_item_model['role_id'] = 'testString' 

        # Construct a dict representation of a PolicyRequestResourcesItemAttributesItem model
        policy_request_resources_item_attributes_item_model = {}
        policy_request_resources_item_attributes_item_model['name'] = 'testString' 
        policy_request_resources_item_attributes_item_model['value'] = 'testString' 
        policy_request_resources_item_attributes_item_model['operator'] = 'testString' 

        # Construct a dict representation of a PolicyRequestResourcesItem model
        policy_request_resources_item_model = {}
        policy_request_resources_item_model['attributes'] = [policy_request_resources_item_attributes_item_model] 

        # Set up parameter values
        type = 'testString'
        subjects = [policy_request_subjects_item_model]
        roles = [policy_request_roles_item_model]
        resources = [policy_request_resources_item_model]
        accept_language = 'testString'

        # Invoke method
        response = service.create_policy(
            type,
            subjects,
            roles,
            resources,
            accept_language=accept_language
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['subjects'] == subjects
        assert req_body['roles'] == roles
        assert req_body['resources'] == resources


    #--------------------------------------------------------
    # test_create_policy_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_policy_required_params(self):
        # Set up mock
        url = base_url + '/v1/policies'
        mock_response = '{"id": "id", "type": "type", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PolicyRequestSubjectsItemAttributesItem model
        policy_request_subjects_item_attributes_item_model = {}
        policy_request_subjects_item_attributes_item_model['name'] = 'testString' 
        policy_request_subjects_item_attributes_item_model['value'] = 'testString' 

        # Construct a dict representation of a PolicyRequestSubjectsItem model
        policy_request_subjects_item_model = {}
        policy_request_subjects_item_model['attributes'] = [policy_request_subjects_item_attributes_item_model] 

        # Construct a dict representation of a PolicyRequestRolesItem model
        policy_request_roles_item_model = {}
        policy_request_roles_item_model['role_id'] = 'testString' 

        # Construct a dict representation of a PolicyRequestResourcesItemAttributesItem model
        policy_request_resources_item_attributes_item_model = {}
        policy_request_resources_item_attributes_item_model['name'] = 'testString' 
        policy_request_resources_item_attributes_item_model['value'] = 'testString' 
        policy_request_resources_item_attributes_item_model['operator'] = 'testString' 

        # Construct a dict representation of a PolicyRequestResourcesItem model
        policy_request_resources_item_model = {}
        policy_request_resources_item_model['attributes'] = [policy_request_resources_item_attributes_item_model] 

        # Set up parameter values
        type = 'testString'
        subjects = [policy_request_subjects_item_model]
        roles = [policy_request_roles_item_model]
        resources = [policy_request_resources_item_model]

        # Invoke method
        response = service.create_policy(
            type,
            subjects,
            roles,
            resources,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['subjects'] == subjects
        assert req_body['roles'] == roles
        assert req_body['resources'] == resources


#-----------------------------------------------------------------------------
# Test Class for update_policy
#-----------------------------------------------------------------------------
class TestUpdatePolicy():

    #--------------------------------------------------------
    # update_policy()
    #--------------------------------------------------------
    @responses.activate
    def test_update_policy_all_params(self):
        # Set up mock
        url = base_url + '/v1/policies/testString'
        mock_response = '{"id": "id", "type": "type", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PolicyRequestSubjectsItemAttributesItem model
        policy_request_subjects_item_attributes_item_model = {}
        policy_request_subjects_item_attributes_item_model['name'] = 'testString' 
        policy_request_subjects_item_attributes_item_model['value'] = 'testString' 

        # Construct a dict representation of a PolicyRequestSubjectsItem model
        policy_request_subjects_item_model = {}
        policy_request_subjects_item_model['attributes'] = [policy_request_subjects_item_attributes_item_model] 

        # Construct a dict representation of a PolicyRequestRolesItem model
        policy_request_roles_item_model = {}
        policy_request_roles_item_model['role_id'] = 'testString' 

        # Construct a dict representation of a PolicyRequestResourcesItemAttributesItem model
        policy_request_resources_item_attributes_item_model = {}
        policy_request_resources_item_attributes_item_model['name'] = 'testString' 
        policy_request_resources_item_attributes_item_model['value'] = 'testString' 
        policy_request_resources_item_attributes_item_model['operator'] = 'testString' 

        # Construct a dict representation of a PolicyRequestResourcesItem model
        policy_request_resources_item_model = {}
        policy_request_resources_item_model['attributes'] = [policy_request_resources_item_attributes_item_model] 

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        subjects = [policy_request_subjects_item_model]
        roles = [policy_request_roles_item_model]
        resources = [policy_request_resources_item_model]

        # Invoke method
        response = service.update_policy(
            policy_id,
            if_match,
            type,
            subjects,
            roles,
            resources,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['subjects'] == subjects
        assert req_body['roles'] == roles
        assert req_body['resources'] == resources


    #--------------------------------------------------------
    # test_update_policy_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_policy_required_params(self):
        # Set up mock
        url = base_url + '/v1/policies/testString'
        mock_response = '{"id": "id", "type": "type", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PolicyRequestSubjectsItemAttributesItem model
        policy_request_subjects_item_attributes_item_model = {}
        policy_request_subjects_item_attributes_item_model['name'] = 'testString' 
        policy_request_subjects_item_attributes_item_model['value'] = 'testString' 

        # Construct a dict representation of a PolicyRequestSubjectsItem model
        policy_request_subjects_item_model = {}
        policy_request_subjects_item_model['attributes'] = [policy_request_subjects_item_attributes_item_model] 

        # Construct a dict representation of a PolicyRequestRolesItem model
        policy_request_roles_item_model = {}
        policy_request_roles_item_model['role_id'] = 'testString' 

        # Construct a dict representation of a PolicyRequestResourcesItemAttributesItem model
        policy_request_resources_item_attributes_item_model = {}
        policy_request_resources_item_attributes_item_model['name'] = 'testString' 
        policy_request_resources_item_attributes_item_model['value'] = 'testString' 
        policy_request_resources_item_attributes_item_model['operator'] = 'testString' 

        # Construct a dict representation of a PolicyRequestResourcesItem model
        policy_request_resources_item_model = {}
        policy_request_resources_item_model['attributes'] = [policy_request_resources_item_attributes_item_model] 

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        subjects = [policy_request_subjects_item_model]
        roles = [policy_request_roles_item_model]
        resources = [policy_request_resources_item_model]

        # Invoke method
        response = service.update_policy(
            policy_id,
            if_match,
            type,
            subjects,
            roles,
            resources,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['subjects'] == subjects
        assert req_body['roles'] == roles
        assert req_body['resources'] == resources


#-----------------------------------------------------------------------------
# Test Class for get_policy
#-----------------------------------------------------------------------------
class TestGetPolicy():

    #--------------------------------------------------------
    # get_policy()
    #--------------------------------------------------------
    @responses.activate
    def test_get_policy_all_params(self):
        # Set up mock
        url = base_url + '/v1/policies/testString'
        mock_response = '{"id": "id", "type": "type", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = service.get_policy(
            policy_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_policy_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_policy_required_params(self):
        # Set up mock
        url = base_url + '/v1/policies/testString'
        mock_response = '{"id": "id", "type": "type", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = service.get_policy(
            policy_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_policy
#-----------------------------------------------------------------------------
class TestDeletePolicy():

    #--------------------------------------------------------
    # delete_policy()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_policy_all_params(self):
        # Set up mock
        url = base_url + '/v1/policies/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = service.delete_policy(
            policy_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_policy_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_policy_required_params(self):
        # Set up mock
        url = base_url + '/v1/policies/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = service.delete_policy(
            policy_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


# endregion
##############################################################################
# End of Service: Policies
##############################################################################

##############################################################################
# Start of Service: Roles
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_roles
#-----------------------------------------------------------------------------
class TestListRoles():

    #--------------------------------------------------------
    # list_roles()
    #--------------------------------------------------------
    @responses.activate
    def test_list_roles_all_params(self):
        # Set up mock
        url = base_url + '/v2/roles'
        mock_response = '{"custom_roles": [{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}], "service_roles": [{"crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"]}], "system_roles": [{"crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accept_language = 'testString'
        account_id = 'testString'
        service_name = 'testString'

        # Invoke method
        response = service.list_roles(
            accept_language=accept_language,
            account_id=account_id,
            service_name=service_name
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'service_name={}'.format(service_name) in query_string


    #--------------------------------------------------------
    # test_list_roles_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_roles_required_params(self):
        # Set up mock
        url = base_url + '/v2/roles'
        mock_response = '{"custom_roles": [{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}], "service_roles": [{"crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"]}], "system_roles": [{"crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_roles()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_role
#-----------------------------------------------------------------------------
class TestCreateRole():

    #--------------------------------------------------------
    # create_role()
    #--------------------------------------------------------
    @responses.activate
    def test_create_role_all_params(self):
        # Set up mock
        url = base_url + '/v2/roles'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        service_name = 'testString'
        display_name = 'testString'
        actions = ['testString']
        description = 'testString'
        accept_language = 'testString'

        # Invoke method
        response = service.create_role(
            name,
            account_id,
            service_name,
            display_name,
            actions,
            description=description,
            accept_language=accept_language
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['account_id'] == account_id
        assert req_body['service_name'] == service_name
        assert req_body['display_name'] == display_name
        assert req_body['actions'] == actions
        assert req_body['description'] == description


    #--------------------------------------------------------
    # test_create_role_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_role_required_params(self):
        # Set up mock
        url = base_url + '/v2/roles'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        service_name = 'testString'
        display_name = 'testString'
        actions = ['testString']
        description = 'testString'

        # Invoke method
        response = service.create_role(
            name,
            account_id,
            service_name,
            display_name,
            actions,
            description=description,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['account_id'] == account_id
        assert req_body['service_name'] == service_name
        assert req_body['display_name'] == display_name
        assert req_body['actions'] == actions
        assert req_body['description'] == description


#-----------------------------------------------------------------------------
# Test Class for update_role
#-----------------------------------------------------------------------------
class TestUpdateRole():

    #--------------------------------------------------------
    # update_role()
    #--------------------------------------------------------
    @responses.activate
    def test_update_role_all_params(self):
        # Set up mock
        url = base_url + '/v2/roles/testString'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        role_id = 'testString'
        if_match = 'testString'
        display_name = 'testString'
        description = 'testString'
        actions = ['testString']

        # Invoke method
        response = service.update_role(
            role_id,
            if_match,
            display_name=display_name,
            description=description,
            actions=actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['display_name'] == display_name
        assert req_body['description'] == description
        assert req_body['actions'] == actions


    #--------------------------------------------------------
    # test_update_role_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_role_required_params(self):
        # Set up mock
        url = base_url + '/v2/roles/testString'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        role_id = 'testString'
        if_match = 'testString'
        display_name = 'testString'
        description = 'testString'
        actions = ['testString']

        # Invoke method
        response = service.update_role(
            role_id,
            if_match,
            display_name=display_name,
            description=description,
            actions=actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['display_name'] == display_name
        assert req_body['description'] == description
        assert req_body['actions'] == actions


#-----------------------------------------------------------------------------
# Test Class for get_role
#-----------------------------------------------------------------------------
class TestGetRole():

    #--------------------------------------------------------
    # get_role()
    #--------------------------------------------------------
    @responses.activate
    def test_get_role_all_params(self):
        # Set up mock
        url = base_url + '/v2/roles/testString'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        role_id = 'testString'

        # Invoke method
        response = service.get_role(
            role_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_role_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_role_required_params(self):
        # Set up mock
        url = base_url + '/v2/roles/testString'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "crn": "crn", "display_name": "display_name", "description": "description", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        role_id = 'testString'

        # Invoke method
        response = service.get_role(
            role_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_role
#-----------------------------------------------------------------------------
class TestDeleteRole():

    #--------------------------------------------------------
    # delete_role()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_role_all_params(self):
        # Set up mock
        url = base_url + '/v2/roles/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        role_id = 'testString'

        # Invoke method
        response = service.delete_role(
            role_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_role_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_role_required_params(self):
        # Set up mock
        url = base_url + '/v2/roles/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        role_id = 'testString'

        # Invoke method
        response = service.delete_role(
            role_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


# endregion
##############################################################################
# End of Service: Roles
##############################################################################

