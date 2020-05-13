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
from ibm_platform_services.iam_policy_management_v1 import *


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
            service_type=service_type,
            headers={}
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
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string


    #--------------------------------------------------------
    # test_list_policies_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_policies_value_error(self):
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

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_policies(**req_copy)



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
            accept_language=accept_language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'testString'
        assert req_body['subjects'] == [policy_request_subjects_item_model]
        assert req_body['roles'] == [policy_request_roles_item_model]
        assert req_body['resources'] == [policy_request_resources_item_model]


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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'testString'
        assert req_body['subjects'] == [policy_request_subjects_item_model]
        assert req_body['roles'] == [policy_request_roles_item_model]
        assert req_body['resources'] == [policy_request_resources_item_model]


    #--------------------------------------------------------
    # test_create_policy_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_policy_value_error(self):
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

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "type": type,
            "subjects": subjects,
            "roles": roles,
            "resources": resources,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_policy(**req_copy)



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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'testString'
        assert req_body['subjects'] == [policy_request_subjects_item_model]
        assert req_body['roles'] == [policy_request_roles_item_model]
        assert req_body['resources'] == [policy_request_resources_item_model]


    #--------------------------------------------------------
    # test_update_policy_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_policy_value_error(self):
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

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
            "if_match": if_match,
            "type": type,
            "subjects": subjects,
            "roles": roles,
            "resources": resources,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_policy(**req_copy)



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
            policy_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_policy_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_policy_value_error(self):
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

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_policy(**req_copy)



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
            policy_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_policy_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_policy_value_error(self):
        # Set up mock
        url = base_url + '/v1/policies/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        policy_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_policy(**req_copy)



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
        mock_response = '{"custom_roles": [{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}], "service_roles": [{"display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"]}], "system_roles": [{"display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"]}]}'
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
            service_name=service_name,
            headers={}
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
        mock_response = '{"custom_roles": [{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}], "service_roles": [{"display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"]}], "system_roles": [{"display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"]}]}'
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
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
            accept_language=accept_language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['service_name'] == 'testString'
        assert req_body['display_name'] == 'testString'
        assert req_body['actions'] == ['testString']
        assert req_body['description'] == 'testString'


    #--------------------------------------------------------
    # test_create_role_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_role_required_params(self):
        # Set up mock
        url = base_url + '/v2/roles'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['service_name'] == 'testString'
        assert req_body['display_name'] == 'testString'
        assert req_body['actions'] == ['testString']
        assert req_body['description'] == 'testString'


    #--------------------------------------------------------
    # test_create_role_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_role_value_error(self):
        # Set up mock
        url = base_url + '/v2/roles'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "account_id": account_id,
            "service_name": service_name,
            "display_name": display_name,
            "actions": actions,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_role(**req_copy)



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
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['display_name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['actions'] == ['testString']


    #--------------------------------------------------------
    # test_update_role_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_role_value_error(self):
        # Set up mock
        url = base_url + '/v2/roles/testString'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_id": role_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_role(**req_copy)



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
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        role_id = 'testString'

        # Invoke method
        response = service.get_role(
            role_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_role_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_role_value_error(self):
        # Set up mock
        url = base_url + '/v2/roles/testString'
        mock_response = '{"id": "id", "name": "name", "account_id": "account_id", "service_name": "service_name", "display_name": "display_name", "description": "description", "crn": "crn", "actions": ["actions"], "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        role_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_id": role_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_role(**req_copy)



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
            role_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_role_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_role_value_error(self):
        # Set up mock
        url = base_url + '/v2/roles/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        role_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_id": role_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_role(**req_copy)



# endregion
##############################################################################
# End of Service: Roles
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for PolicyBaseResourcesItem
#-----------------------------------------------------------------------------
class TestPolicyBaseResourcesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyBaseResourcesItem
    #--------------------------------------------------------
    def test_policy_base_resources_item_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        policy_base_resources_item_attributes_item_model = {} # PolicyBaseResourcesItemAttributesItem
        policy_base_resources_item_attributes_item_model['name'] = 'testString'
        policy_base_resources_item_attributes_item_model['value'] = 'testString'
        policy_base_resources_item_attributes_item_model['operator'] = 'testString'

        # Construct a json representation of a PolicyBaseResourcesItem model
        policy_base_resources_item_model_json = {}
        policy_base_resources_item_model_json['attributes'] = [policy_base_resources_item_attributes_item_model]

        # Construct a model instance of PolicyBaseResourcesItem by calling from_dict on the json representation
        policy_base_resources_item_model = PolicyBaseResourcesItem.from_dict(policy_base_resources_item_model_json)
        assert policy_base_resources_item_model != False

        # Construct a model instance of PolicyBaseResourcesItem by calling from_dict on the json representation
        policy_base_resources_item_model_dict = PolicyBaseResourcesItem.from_dict(policy_base_resources_item_model_json).__dict__
        policy_base_resources_item_model2 = PolicyBaseResourcesItem(**policy_base_resources_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_base_resources_item_model == policy_base_resources_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_base_resources_item_model_json2 = policy_base_resources_item_model.to_dict()
        assert policy_base_resources_item_model_json2 == policy_base_resources_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyBaseResourcesItemAttributesItem
#-----------------------------------------------------------------------------
class TestPolicyBaseResourcesItemAttributesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyBaseResourcesItemAttributesItem
    #--------------------------------------------------------
    def test_policy_base_resources_item_attributes_item_serialization(self):

        # Construct a json representation of a PolicyBaseResourcesItemAttributesItem model
        policy_base_resources_item_attributes_item_model_json = {}
        policy_base_resources_item_attributes_item_model_json['name'] = 'testString'
        policy_base_resources_item_attributes_item_model_json['value'] = 'testString'
        policy_base_resources_item_attributes_item_model_json['operator'] = 'testString'

        # Construct a model instance of PolicyBaseResourcesItemAttributesItem by calling from_dict on the json representation
        policy_base_resources_item_attributes_item_model = PolicyBaseResourcesItemAttributesItem.from_dict(policy_base_resources_item_attributes_item_model_json)
        assert policy_base_resources_item_attributes_item_model != False

        # Construct a model instance of PolicyBaseResourcesItemAttributesItem by calling from_dict on the json representation
        policy_base_resources_item_attributes_item_model_dict = PolicyBaseResourcesItemAttributesItem.from_dict(policy_base_resources_item_attributes_item_model_json).__dict__
        policy_base_resources_item_attributes_item_model2 = PolicyBaseResourcesItemAttributesItem(**policy_base_resources_item_attributes_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_base_resources_item_attributes_item_model == policy_base_resources_item_attributes_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_base_resources_item_attributes_item_model_json2 = policy_base_resources_item_attributes_item_model.to_dict()
        assert policy_base_resources_item_attributes_item_model_json2 == policy_base_resources_item_attributes_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyBaseSubjectsItem
#-----------------------------------------------------------------------------
class TestPolicyBaseSubjectsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyBaseSubjectsItem
    #--------------------------------------------------------
    def test_policy_base_subjects_item_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        policy_base_subjects_item_attributes_item_model = {} # PolicyBaseSubjectsItemAttributesItem
        policy_base_subjects_item_attributes_item_model['name'] = 'testString'
        policy_base_subjects_item_attributes_item_model['value'] = 'testString'

        # Construct a json representation of a PolicyBaseSubjectsItem model
        policy_base_subjects_item_model_json = {}
        policy_base_subjects_item_model_json['attributes'] = [policy_base_subjects_item_attributes_item_model]

        # Construct a model instance of PolicyBaseSubjectsItem by calling from_dict on the json representation
        policy_base_subjects_item_model = PolicyBaseSubjectsItem.from_dict(policy_base_subjects_item_model_json)
        assert policy_base_subjects_item_model != False

        # Construct a model instance of PolicyBaseSubjectsItem by calling from_dict on the json representation
        policy_base_subjects_item_model_dict = PolicyBaseSubjectsItem.from_dict(policy_base_subjects_item_model_json).__dict__
        policy_base_subjects_item_model2 = PolicyBaseSubjectsItem(**policy_base_subjects_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_base_subjects_item_model == policy_base_subjects_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_base_subjects_item_model_json2 = policy_base_subjects_item_model.to_dict()
        assert policy_base_subjects_item_model_json2 == policy_base_subjects_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyBaseSubjectsItemAttributesItem
#-----------------------------------------------------------------------------
class TestPolicyBaseSubjectsItemAttributesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyBaseSubjectsItemAttributesItem
    #--------------------------------------------------------
    def test_policy_base_subjects_item_attributes_item_serialization(self):

        # Construct a json representation of a PolicyBaseSubjectsItemAttributesItem model
        policy_base_subjects_item_attributes_item_model_json = {}
        policy_base_subjects_item_attributes_item_model_json['name'] = 'testString'
        policy_base_subjects_item_attributes_item_model_json['value'] = 'testString'

        # Construct a model instance of PolicyBaseSubjectsItemAttributesItem by calling from_dict on the json representation
        policy_base_subjects_item_attributes_item_model = PolicyBaseSubjectsItemAttributesItem.from_dict(policy_base_subjects_item_attributes_item_model_json)
        assert policy_base_subjects_item_attributes_item_model != False

        # Construct a model instance of PolicyBaseSubjectsItemAttributesItem by calling from_dict on the json representation
        policy_base_subjects_item_attributes_item_model_dict = PolicyBaseSubjectsItemAttributesItem.from_dict(policy_base_subjects_item_attributes_item_model_json).__dict__
        policy_base_subjects_item_attributes_item_model2 = PolicyBaseSubjectsItemAttributesItem(**policy_base_subjects_item_attributes_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_base_subjects_item_attributes_item_model == policy_base_subjects_item_attributes_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_base_subjects_item_attributes_item_model_json2 = policy_base_subjects_item_attributes_item_model.to_dict()
        assert policy_base_subjects_item_attributes_item_model_json2 == policy_base_subjects_item_attributes_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyRequestResourcesItem
#-----------------------------------------------------------------------------
class TestPolicyRequestResourcesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyRequestResourcesItem
    #--------------------------------------------------------
    def test_policy_request_resources_item_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        policy_request_resources_item_attributes_item_model = {} # PolicyRequestResourcesItemAttributesItem
        policy_request_resources_item_attributes_item_model['name'] = 'testString'
        policy_request_resources_item_attributes_item_model['value'] = 'testString'
        policy_request_resources_item_attributes_item_model['operator'] = 'testString'

        # Construct a json representation of a PolicyRequestResourcesItem model
        policy_request_resources_item_model_json = {}
        policy_request_resources_item_model_json['attributes'] = [policy_request_resources_item_attributes_item_model]

        # Construct a model instance of PolicyRequestResourcesItem by calling from_dict on the json representation
        policy_request_resources_item_model = PolicyRequestResourcesItem.from_dict(policy_request_resources_item_model_json)
        assert policy_request_resources_item_model != False

        # Construct a model instance of PolicyRequestResourcesItem by calling from_dict on the json representation
        policy_request_resources_item_model_dict = PolicyRequestResourcesItem.from_dict(policy_request_resources_item_model_json).__dict__
        policy_request_resources_item_model2 = PolicyRequestResourcesItem(**policy_request_resources_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_request_resources_item_model == policy_request_resources_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_request_resources_item_model_json2 = policy_request_resources_item_model.to_dict()
        assert policy_request_resources_item_model_json2 == policy_request_resources_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyRequestResourcesItemAttributesItem
#-----------------------------------------------------------------------------
class TestPolicyRequestResourcesItemAttributesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyRequestResourcesItemAttributesItem
    #--------------------------------------------------------
    def test_policy_request_resources_item_attributes_item_serialization(self):

        # Construct a json representation of a PolicyRequestResourcesItemAttributesItem model
        policy_request_resources_item_attributes_item_model_json = {}
        policy_request_resources_item_attributes_item_model_json['name'] = 'testString'
        policy_request_resources_item_attributes_item_model_json['value'] = 'testString'
        policy_request_resources_item_attributes_item_model_json['operator'] = 'testString'

        # Construct a model instance of PolicyRequestResourcesItemAttributesItem by calling from_dict on the json representation
        policy_request_resources_item_attributes_item_model = PolicyRequestResourcesItemAttributesItem.from_dict(policy_request_resources_item_attributes_item_model_json)
        assert policy_request_resources_item_attributes_item_model != False

        # Construct a model instance of PolicyRequestResourcesItemAttributesItem by calling from_dict on the json representation
        policy_request_resources_item_attributes_item_model_dict = PolicyRequestResourcesItemAttributesItem.from_dict(policy_request_resources_item_attributes_item_model_json).__dict__
        policy_request_resources_item_attributes_item_model2 = PolicyRequestResourcesItemAttributesItem(**policy_request_resources_item_attributes_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_request_resources_item_attributes_item_model == policy_request_resources_item_attributes_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_request_resources_item_attributes_item_model_json2 = policy_request_resources_item_attributes_item_model.to_dict()
        assert policy_request_resources_item_attributes_item_model_json2 == policy_request_resources_item_attributes_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyRequestRolesItem
#-----------------------------------------------------------------------------
class TestPolicyRequestRolesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyRequestRolesItem
    #--------------------------------------------------------
    def test_policy_request_roles_item_serialization(self):

        # Construct a json representation of a PolicyRequestRolesItem model
        policy_request_roles_item_model_json = {}
        policy_request_roles_item_model_json['role_id'] = 'testString'

        # Construct a model instance of PolicyRequestRolesItem by calling from_dict on the json representation
        policy_request_roles_item_model = PolicyRequestRolesItem.from_dict(policy_request_roles_item_model_json)
        assert policy_request_roles_item_model != False

        # Construct a model instance of PolicyRequestRolesItem by calling from_dict on the json representation
        policy_request_roles_item_model_dict = PolicyRequestRolesItem.from_dict(policy_request_roles_item_model_json).__dict__
        policy_request_roles_item_model2 = PolicyRequestRolesItem(**policy_request_roles_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_request_roles_item_model == policy_request_roles_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_request_roles_item_model_json2 = policy_request_roles_item_model.to_dict()
        assert policy_request_roles_item_model_json2 == policy_request_roles_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyRequestSubjectsItem
#-----------------------------------------------------------------------------
class TestPolicyRequestSubjectsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyRequestSubjectsItem
    #--------------------------------------------------------
    def test_policy_request_subjects_item_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        policy_request_subjects_item_attributes_item_model = {} # PolicyRequestSubjectsItemAttributesItem
        policy_request_subjects_item_attributes_item_model['name'] = 'testString'
        policy_request_subjects_item_attributes_item_model['value'] = 'testString'

        # Construct a json representation of a PolicyRequestSubjectsItem model
        policy_request_subjects_item_model_json = {}
        policy_request_subjects_item_model_json['attributes'] = [policy_request_subjects_item_attributes_item_model]

        # Construct a model instance of PolicyRequestSubjectsItem by calling from_dict on the json representation
        policy_request_subjects_item_model = PolicyRequestSubjectsItem.from_dict(policy_request_subjects_item_model_json)
        assert policy_request_subjects_item_model != False

        # Construct a model instance of PolicyRequestSubjectsItem by calling from_dict on the json representation
        policy_request_subjects_item_model_dict = PolicyRequestSubjectsItem.from_dict(policy_request_subjects_item_model_json).__dict__
        policy_request_subjects_item_model2 = PolicyRequestSubjectsItem(**policy_request_subjects_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_request_subjects_item_model == policy_request_subjects_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_request_subjects_item_model_json2 = policy_request_subjects_item_model.to_dict()
        assert policy_request_subjects_item_model_json2 == policy_request_subjects_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyRequestSubjectsItemAttributesItem
#-----------------------------------------------------------------------------
class TestPolicyRequestSubjectsItemAttributesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyRequestSubjectsItemAttributesItem
    #--------------------------------------------------------
    def test_policy_request_subjects_item_attributes_item_serialization(self):

        # Construct a json representation of a PolicyRequestSubjectsItemAttributesItem model
        policy_request_subjects_item_attributes_item_model_json = {}
        policy_request_subjects_item_attributes_item_model_json['name'] = 'testString'
        policy_request_subjects_item_attributes_item_model_json['value'] = 'testString'

        # Construct a model instance of PolicyRequestSubjectsItemAttributesItem by calling from_dict on the json representation
        policy_request_subjects_item_attributes_item_model = PolicyRequestSubjectsItemAttributesItem.from_dict(policy_request_subjects_item_attributes_item_model_json)
        assert policy_request_subjects_item_attributes_item_model != False

        # Construct a model instance of PolicyRequestSubjectsItemAttributesItem by calling from_dict on the json representation
        policy_request_subjects_item_attributes_item_model_dict = PolicyRequestSubjectsItemAttributesItem.from_dict(policy_request_subjects_item_attributes_item_model_json).__dict__
        policy_request_subjects_item_attributes_item_model2 = PolicyRequestSubjectsItemAttributesItem(**policy_request_subjects_item_attributes_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_request_subjects_item_attributes_item_model == policy_request_subjects_item_attributes_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_request_subjects_item_attributes_item_model_json2 = policy_request_subjects_item_attributes_item_model.to_dict()
        assert policy_request_subjects_item_attributes_item_model_json2 == policy_request_subjects_item_attributes_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyRolesItem
#-----------------------------------------------------------------------------
class TestPolicyRolesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyRolesItem
    #--------------------------------------------------------
    def test_policy_roles_item_serialization(self):

        # Construct a json representation of a PolicyRolesItem model
        policy_roles_item_model_json = {}
        policy_roles_item_model_json['role_id'] = 'testString'
        policy_roles_item_model_json['display_name'] = 'testString'
        policy_roles_item_model_json['description'] = 'testString'

        # Construct a model instance of PolicyRolesItem by calling from_dict on the json representation
        policy_roles_item_model = PolicyRolesItem.from_dict(policy_roles_item_model_json)
        assert policy_roles_item_model != False

        # Construct a model instance of PolicyRolesItem by calling from_dict on the json representation
        policy_roles_item_model_dict = PolicyRolesItem.from_dict(policy_roles_item_model_json).__dict__
        policy_roles_item_model2 = PolicyRolesItem(**policy_roles_item_model_dict)

        # Verify the model instances are equivalent
        assert policy_roles_item_model == policy_roles_item_model2

        # Convert model instance back to dict and verify no loss of data
        policy_roles_item_model_json2 = policy_roles_item_model.to_dict()
        assert policy_roles_item_model_json2 == policy_roles_item_model_json

#-----------------------------------------------------------------------------
# Test Class for RoleListCustomRolesItem
#-----------------------------------------------------------------------------
class TestRoleListCustomRolesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for RoleListCustomRolesItem
    #--------------------------------------------------------
    def test_role_list_custom_roles_item_serialization(self):

        # Construct a json representation of a RoleListCustomRolesItem model
        role_list_custom_roles_item_model_json = {}
        role_list_custom_roles_item_model_json['id'] = 'testString'
        role_list_custom_roles_item_model_json['name'] = 'testString'
        role_list_custom_roles_item_model_json['account_id'] = 'testString'
        role_list_custom_roles_item_model_json['service_name'] = 'testString'
        role_list_custom_roles_item_model_json['display_name'] = 'testString'
        role_list_custom_roles_item_model_json['description'] = 'testString'
        role_list_custom_roles_item_model_json['crn'] = 'testString'
        role_list_custom_roles_item_model_json['actions'] = ['testString']
        role_list_custom_roles_item_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        role_list_custom_roles_item_model_json['created_by_id'] = 'testString'
        role_list_custom_roles_item_model_json['last_modified_at'] = '2020-01-28T18:40:40.123456Z'
        role_list_custom_roles_item_model_json['last_modified_by_id'] = 'testString'
        role_list_custom_roles_item_model_json['href'] = 'testString'

        # Construct a model instance of RoleListCustomRolesItem by calling from_dict on the json representation
        role_list_custom_roles_item_model = RoleListCustomRolesItem.from_dict(role_list_custom_roles_item_model_json)
        assert role_list_custom_roles_item_model != False

        # Construct a model instance of RoleListCustomRolesItem by calling from_dict on the json representation
        role_list_custom_roles_item_model_dict = RoleListCustomRolesItem.from_dict(role_list_custom_roles_item_model_json).__dict__
        role_list_custom_roles_item_model2 = RoleListCustomRolesItem(**role_list_custom_roles_item_model_dict)

        # Verify the model instances are equivalent
        assert role_list_custom_roles_item_model == role_list_custom_roles_item_model2

        # Convert model instance back to dict and verify no loss of data
        role_list_custom_roles_item_model_json2 = role_list_custom_roles_item_model.to_dict()
        assert role_list_custom_roles_item_model_json2 == role_list_custom_roles_item_model_json

#-----------------------------------------------------------------------------
# Test Class for RoleListServiceRolesItem
#-----------------------------------------------------------------------------
class TestRoleListServiceRolesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for RoleListServiceRolesItem
    #--------------------------------------------------------
    def test_role_list_service_roles_item_serialization(self):

        # Construct a json representation of a RoleListServiceRolesItem model
        role_list_service_roles_item_model_json = {}
        role_list_service_roles_item_model_json['display_name'] = 'testString'
        role_list_service_roles_item_model_json['description'] = 'testString'
        role_list_service_roles_item_model_json['crn'] = 'testString'
        role_list_service_roles_item_model_json['actions'] = ['testString']

        # Construct a model instance of RoleListServiceRolesItem by calling from_dict on the json representation
        role_list_service_roles_item_model = RoleListServiceRolesItem.from_dict(role_list_service_roles_item_model_json)
        assert role_list_service_roles_item_model != False

        # Construct a model instance of RoleListServiceRolesItem by calling from_dict on the json representation
        role_list_service_roles_item_model_dict = RoleListServiceRolesItem.from_dict(role_list_service_roles_item_model_json).__dict__
        role_list_service_roles_item_model2 = RoleListServiceRolesItem(**role_list_service_roles_item_model_dict)

        # Verify the model instances are equivalent
        assert role_list_service_roles_item_model == role_list_service_roles_item_model2

        # Convert model instance back to dict and verify no loss of data
        role_list_service_roles_item_model_json2 = role_list_service_roles_item_model.to_dict()
        assert role_list_service_roles_item_model_json2 == role_list_service_roles_item_model_json

#-----------------------------------------------------------------------------
# Test Class for RoleListSystemRolesItem
#-----------------------------------------------------------------------------
class TestRoleListSystemRolesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for RoleListSystemRolesItem
    #--------------------------------------------------------
    def test_role_list_system_roles_item_serialization(self):

        # Construct a json representation of a RoleListSystemRolesItem model
        role_list_system_roles_item_model_json = {}
        role_list_system_roles_item_model_json['display_name'] = 'testString'
        role_list_system_roles_item_model_json['description'] = 'testString'
        role_list_system_roles_item_model_json['crn'] = 'testString'
        role_list_system_roles_item_model_json['actions'] = ['testString']

        # Construct a model instance of RoleListSystemRolesItem by calling from_dict on the json representation
        role_list_system_roles_item_model = RoleListSystemRolesItem.from_dict(role_list_system_roles_item_model_json)
        assert role_list_system_roles_item_model != False

        # Construct a model instance of RoleListSystemRolesItem by calling from_dict on the json representation
        role_list_system_roles_item_model_dict = RoleListSystemRolesItem.from_dict(role_list_system_roles_item_model_json).__dict__
        role_list_system_roles_item_model2 = RoleListSystemRolesItem(**role_list_system_roles_item_model_dict)

        # Verify the model instances are equivalent
        assert role_list_system_roles_item_model == role_list_system_roles_item_model2

        # Convert model instance back to dict and verify no loss of data
        role_list_system_roles_item_model_json2 = role_list_system_roles_item_model.to_dict()
        assert role_list_system_roles_item_model_json2 == role_list_system_roles_item_model_json

#-----------------------------------------------------------------------------
# Test Class for CustomRole
#-----------------------------------------------------------------------------
class TestCustomRole():

    #--------------------------------------------------------
    # Test serialization/deserialization for CustomRole
    #--------------------------------------------------------
    def test_custom_role_serialization(self):

        # Construct a json representation of a CustomRole model
        custom_role_model_json = {}
        custom_role_model_json['id'] = 'testString'
        custom_role_model_json['name'] = 'testString'
        custom_role_model_json['account_id'] = 'testString'
        custom_role_model_json['service_name'] = 'testString'
        custom_role_model_json['display_name'] = 'testString'
        custom_role_model_json['description'] = 'testString'
        custom_role_model_json['crn'] = 'testString'
        custom_role_model_json['actions'] = ['testString']
        custom_role_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        custom_role_model_json['created_by_id'] = 'testString'
        custom_role_model_json['last_modified_at'] = '2020-01-28T18:40:40.123456Z'
        custom_role_model_json['last_modified_by_id'] = 'testString'
        custom_role_model_json['href'] = 'testString'

        # Construct a model instance of CustomRole by calling from_dict on the json representation
        custom_role_model = CustomRole.from_dict(custom_role_model_json)
        assert custom_role_model != False

        # Construct a model instance of CustomRole by calling from_dict on the json representation
        custom_role_model_dict = CustomRole.from_dict(custom_role_model_json).__dict__
        custom_role_model2 = CustomRole(**custom_role_model_dict)

        # Verify the model instances are equivalent
        assert custom_role_model == custom_role_model2

        # Convert model instance back to dict and verify no loss of data
        custom_role_model_json2 = custom_role_model.to_dict()
        assert custom_role_model_json2 == custom_role_model_json

#-----------------------------------------------------------------------------
# Test Class for Policy
#-----------------------------------------------------------------------------
class TestPolicy():

    #--------------------------------------------------------
    # Test serialization/deserialization for Policy
    #--------------------------------------------------------
    def test_policy_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        policy_base_resources_item_attributes_item_model = {} # PolicyBaseResourcesItemAttributesItem
        policy_base_resources_item_attributes_item_model['name'] = 'testString'
        policy_base_resources_item_attributes_item_model['value'] = 'testString'
        policy_base_resources_item_attributes_item_model['operator'] = 'testString'

        policy_base_subjects_item_attributes_item_model = {} # PolicyBaseSubjectsItemAttributesItem
        policy_base_subjects_item_attributes_item_model['name'] = 'testString'
        policy_base_subjects_item_attributes_item_model['value'] = 'testString'

        policy_base_resources_item_model = {} # PolicyBaseResourcesItem
        policy_base_resources_item_model['attributes'] = [policy_base_resources_item_attributes_item_model]

        policy_base_subjects_item_model = {} # PolicyBaseSubjectsItem
        policy_base_subjects_item_model['attributes'] = [policy_base_subjects_item_attributes_item_model]

        policy_roles_item_model = {} # PolicyRolesItem
        policy_roles_item_model['role_id'] = 'testString'
        policy_roles_item_model['display_name'] = 'testString'
        policy_roles_item_model['description'] = 'testString'

        # Construct a json representation of a Policy model
        policy_model_json = {}
        policy_model_json['id'] = 'testString'
        policy_model_json['type'] = 'testString'
        policy_model_json['subjects'] = [policy_base_subjects_item_model]
        policy_model_json['roles'] = [policy_roles_item_model]
        policy_model_json['resources'] = [policy_base_resources_item_model]
        policy_model_json['href'] = 'testString'
        policy_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        policy_model_json['created_by_id'] = 'testString'
        policy_model_json['last_modified_at'] = '2020-01-28T18:40:40.123456Z'
        policy_model_json['last_modified_by_id'] = 'testString'

        # Construct a model instance of Policy by calling from_dict on the json representation
        policy_model = Policy.from_dict(policy_model_json)
        assert policy_model != False

        # Construct a model instance of Policy by calling from_dict on the json representation
        policy_model_dict = Policy.from_dict(policy_model_json).__dict__
        policy_model2 = Policy(**policy_model_dict)

        # Verify the model instances are equivalent
        assert policy_model == policy_model2

        # Convert model instance back to dict and verify no loss of data
        policy_model_json2 = policy_model.to_dict()
        assert policy_model_json2 == policy_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyList
#-----------------------------------------------------------------------------
class TestPolicyList():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyList
    #--------------------------------------------------------
    def test_policy_list_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        policy_base_resources_item_attributes_item_model = {} # PolicyBaseResourcesItemAttributesItem
        policy_base_resources_item_attributes_item_model['name'] = 'testString'
        policy_base_resources_item_attributes_item_model['value'] = 'testString'
        policy_base_resources_item_attributes_item_model['operator'] = 'testString'

        policy_base_subjects_item_attributes_item_model = {} # PolicyBaseSubjectsItemAttributesItem
        policy_base_subjects_item_attributes_item_model['name'] = 'testString'
        policy_base_subjects_item_attributes_item_model['value'] = 'testString'

        policy_base_resources_item_model = {} # PolicyBaseResourcesItem
        policy_base_resources_item_model['attributes'] = [policy_base_resources_item_attributes_item_model]

        policy_base_subjects_item_model = {} # PolicyBaseSubjectsItem
        policy_base_subjects_item_model['attributes'] = [policy_base_subjects_item_attributes_item_model]

        policy_roles_item_model = {} # PolicyRolesItem
        policy_roles_item_model['role_id'] = 'testString'
        policy_roles_item_model['display_name'] = 'testString'
        policy_roles_item_model['description'] = 'testString'

        policy_model = {} # Policy
        policy_model['id'] = 'testString'
        policy_model['type'] = 'testString'
        policy_model['subjects'] = [policy_base_subjects_item_model]
        policy_model['roles'] = [policy_roles_item_model]
        policy_model['resources'] = [policy_base_resources_item_model]
        policy_model['href'] = 'testString'
        policy_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        policy_model['created_by_id'] = 'testString'
        policy_model['last_modified_at'] = '2020-01-28T18:40:40.123456Z'
        policy_model['last_modified_by_id'] = 'testString'

        # Construct a json representation of a PolicyList model
        policy_list_model_json = {}
        policy_list_model_json['policies'] = [policy_model]

        # Construct a model instance of PolicyList by calling from_dict on the json representation
        policy_list_model = PolicyList.from_dict(policy_list_model_json)
        assert policy_list_model != False

        # Construct a model instance of PolicyList by calling from_dict on the json representation
        policy_list_model_dict = PolicyList.from_dict(policy_list_model_json).__dict__
        policy_list_model2 = PolicyList(**policy_list_model_dict)

        # Verify the model instances are equivalent
        assert policy_list_model == policy_list_model2

        # Convert model instance back to dict and verify no loss of data
        policy_list_model_json2 = policy_list_model.to_dict()
        assert policy_list_model_json2 == policy_list_model_json

#-----------------------------------------------------------------------------
# Test Class for RoleList
#-----------------------------------------------------------------------------
class TestRoleList():

    #--------------------------------------------------------
    # Test serialization/deserialization for RoleList
    #--------------------------------------------------------
    def test_role_list_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        role_list_custom_roles_item_model = {} # RoleListCustomRolesItem
        role_list_custom_roles_item_model['id'] = 'testString'
        role_list_custom_roles_item_model['name'] = 'testString'
        role_list_custom_roles_item_model['account_id'] = 'testString'
        role_list_custom_roles_item_model['service_name'] = 'testString'
        role_list_custom_roles_item_model['display_name'] = 'testString'
        role_list_custom_roles_item_model['description'] = 'testString'
        role_list_custom_roles_item_model['crn'] = 'testString'
        role_list_custom_roles_item_model['actions'] = ['testString']
        role_list_custom_roles_item_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        role_list_custom_roles_item_model['created_by_id'] = 'testString'
        role_list_custom_roles_item_model['last_modified_at'] = '2020-01-28T18:40:40.123456Z'
        role_list_custom_roles_item_model['last_modified_by_id'] = 'testString'
        role_list_custom_roles_item_model['href'] = 'testString'

        role_list_service_roles_item_model = {} # RoleListServiceRolesItem
        role_list_service_roles_item_model['display_name'] = 'testString'
        role_list_service_roles_item_model['description'] = 'testString'
        role_list_service_roles_item_model['crn'] = 'testString'
        role_list_service_roles_item_model['actions'] = ['testString']

        role_list_system_roles_item_model = {} # RoleListSystemRolesItem
        role_list_system_roles_item_model['display_name'] = 'testString'
        role_list_system_roles_item_model['description'] = 'testString'
        role_list_system_roles_item_model['crn'] = 'testString'
        role_list_system_roles_item_model['actions'] = ['testString']

        # Construct a json representation of a RoleList model
        role_list_model_json = {}
        role_list_model_json['custom_roles'] = [role_list_custom_roles_item_model]
        role_list_model_json['service_roles'] = [role_list_service_roles_item_model]
        role_list_model_json['system_roles'] = [role_list_system_roles_item_model]

        # Construct a model instance of RoleList by calling from_dict on the json representation
        role_list_model = RoleList.from_dict(role_list_model_json)
        assert role_list_model != False

        # Construct a model instance of RoleList by calling from_dict on the json representation
        role_list_model_dict = RoleList.from_dict(role_list_model_json).__dict__
        role_list_model2 = RoleList(**role_list_model_dict)

        # Verify the model instances are equivalent
        assert role_list_model == role_list_model2

        # Convert model instance back to dict and verify no loss of data
        role_list_model_json2 = role_list_model.to_dict()
        assert role_list_model_json2 == role_list_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
