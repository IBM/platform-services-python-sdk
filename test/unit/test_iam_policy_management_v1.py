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

        # Construct a dict representation of a SubjectAttribute model
        subject_attribute_model = {}
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a PolicySubject model
        policy_subject_model = {}
        policy_subject_model['attributes'] = [subject_attribute_model]

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a ResourceAttribute model
        resource_attribute_model = {}
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]

        # Set up parameter values
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]
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
        assert req_body['subjects'] == [policy_subject_model]
        assert req_body['roles'] == [policy_role_model]
        assert req_body['resources'] == [policy_resource_model]


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

        # Construct a dict representation of a SubjectAttribute model
        subject_attribute_model = {}
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a PolicySubject model
        policy_subject_model = {}
        policy_subject_model['attributes'] = [subject_attribute_model]

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a ResourceAttribute model
        resource_attribute_model = {}
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]

        # Set up parameter values
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]

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
        assert req_body['subjects'] == [policy_subject_model]
        assert req_body['roles'] == [policy_role_model]
        assert req_body['resources'] == [policy_resource_model]


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

        # Construct a dict representation of a SubjectAttribute model
        subject_attribute_model = {}
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a PolicySubject model
        policy_subject_model = {}
        policy_subject_model['attributes'] = [subject_attribute_model]

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a ResourceAttribute model
        resource_attribute_model = {}
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]

        # Set up parameter values
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]

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

        # Construct a dict representation of a SubjectAttribute model
        subject_attribute_model = {}
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a PolicySubject model
        policy_subject_model = {}
        policy_subject_model['attributes'] = [subject_attribute_model]

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a ResourceAttribute model
        resource_attribute_model = {}
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]

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
        assert req_body['subjects'] == [policy_subject_model]
        assert req_body['roles'] == [policy_role_model]
        assert req_body['resources'] == [policy_resource_model]


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

        # Construct a dict representation of a SubjectAttribute model
        subject_attribute_model = {}
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a PolicySubject model
        policy_subject_model = {}
        policy_subject_model['attributes'] = [subject_attribute_model]

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a ResourceAttribute model
        resource_attribute_model = {}
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]

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
        mock_response = '{"custom_roles": [{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "name", "account_id": "account_id", "service_name": "service_name", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}], "service_roles": [{"display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn"}], "system_roles": [{"display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn"}]}'
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
        mock_response = '{"custom_roles": [{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "name", "account_id": "account_id", "service_name": "service_name", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}], "service_roles": [{"display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn"}], "system_roles": [{"display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn"}]}'
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
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "name", "account_id": "account_id", "service_name": "service_name", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        display_name = 'testString'
        actions = ['testString']
        name = 'testString'
        account_id = 'testString'
        service_name = 'testString'
        description = 'testString'
        accept_language = 'testString'

        # Invoke method
        response = service.create_role(
            display_name,
            actions,
            name,
            account_id,
            service_name,
            description=description,
            accept_language=accept_language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['display_name'] == 'testString'
        assert req_body['actions'] == ['testString']
        assert req_body['name'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['service_name'] == 'testString'
        assert req_body['description'] == 'testString'


    #--------------------------------------------------------
    # test_create_role_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_role_required_params(self):
        # Set up mock
        url = base_url + '/v2/roles'
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "name", "account_id": "account_id", "service_name": "service_name", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        display_name = 'testString'
        actions = ['testString']
        name = 'testString'
        account_id = 'testString'
        service_name = 'testString'
        description = 'testString'

        # Invoke method
        response = service.create_role(
            display_name,
            actions,
            name,
            account_id,
            service_name,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['display_name'] == 'testString'
        assert req_body['actions'] == ['testString']
        assert req_body['name'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['service_name'] == 'testString'
        assert req_body['description'] == 'testString'


    #--------------------------------------------------------
    # test_create_role_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_role_value_error(self):
        # Set up mock
        url = base_url + '/v2/roles'
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "name", "account_id": "account_id", "service_name": "service_name", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        display_name = 'testString'
        actions = ['testString']
        name = 'testString'
        account_id = 'testString'
        service_name = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "display_name": display_name,
            "actions": actions,
            "name": name,
            "account_id": account_id,
            "service_name": service_name,
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
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "name", "account_id": "account_id", "service_name": "service_name", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "name", "account_id": "account_id", "service_name": "service_name", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "name", "account_id": "account_id", "service_name": "service_name", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "name", "account_id": "account_id", "service_name": "service_name", "created_at": "2019-01-01T12:00:00", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
        custom_role_model_json['display_name'] = 'testString'
        custom_role_model_json['description'] = 'testString'
        custom_role_model_json['actions'] = ['testString']
        custom_role_model_json['crn'] = 'testString'
        custom_role_model_json['name'] = 'testString'
        custom_role_model_json['account_id'] = 'testString'
        custom_role_model_json['service_name'] = 'testString'
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

        resource_attribute_model = {} # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        subject_attribute_model = {} # SubjectAttribute
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        policy_resource_model = {} # PolicyResource
        policy_resource_model['attributes'] = [resource_attribute_model]

        policy_role_model = {} # PolicyRole
        policy_role_model['role_id'] = 'testString'
        policy_role_model['display_name'] = 'testString'
        policy_role_model['description'] = 'testString'

        policy_subject_model = {} # PolicySubject
        policy_subject_model['attributes'] = [subject_attribute_model]

        # Construct a json representation of a Policy model
        policy_model_json = {}
        policy_model_json['id'] = 'testString'
        policy_model_json['type'] = 'testString'
        policy_model_json['subjects'] = [policy_subject_model]
        policy_model_json['roles'] = [policy_role_model]
        policy_model_json['resources'] = [policy_resource_model]
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

        resource_attribute_model = {} # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        subject_attribute_model = {} # SubjectAttribute
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        policy_resource_model = {} # PolicyResource
        policy_resource_model['attributes'] = [resource_attribute_model]

        policy_role_model = {} # PolicyRole
        policy_role_model['role_id'] = 'testString'
        policy_role_model['display_name'] = 'testString'
        policy_role_model['description'] = 'testString'

        policy_subject_model = {} # PolicySubject
        policy_subject_model['attributes'] = [subject_attribute_model]

        policy_model = {} # Policy
        policy_model['id'] = 'testString'
        policy_model['type'] = 'testString'
        policy_model['subjects'] = [policy_subject_model]
        policy_model['roles'] = [policy_role_model]
        policy_model['resources'] = [policy_resource_model]
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
# Test Class for PolicyResource
#-----------------------------------------------------------------------------
class TestPolicyResource():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyResource
    #--------------------------------------------------------
    def test_policy_resource_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        resource_attribute_model = {} # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        # Construct a json representation of a PolicyResource model
        policy_resource_model_json = {}
        policy_resource_model_json['attributes'] = [resource_attribute_model]

        # Construct a model instance of PolicyResource by calling from_dict on the json representation
        policy_resource_model = PolicyResource.from_dict(policy_resource_model_json)
        assert policy_resource_model != False

        # Construct a model instance of PolicyResource by calling from_dict on the json representation
        policy_resource_model_dict = PolicyResource.from_dict(policy_resource_model_json).__dict__
        policy_resource_model2 = PolicyResource(**policy_resource_model_dict)

        # Verify the model instances are equivalent
        assert policy_resource_model == policy_resource_model2

        # Convert model instance back to dict and verify no loss of data
        policy_resource_model_json2 = policy_resource_model.to_dict()
        assert policy_resource_model_json2 == policy_resource_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicyRole
#-----------------------------------------------------------------------------
class TestPolicyRole():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicyRole
    #--------------------------------------------------------
    def test_policy_role_serialization(self):

        # Construct a json representation of a PolicyRole model
        policy_role_model_json = {}
        policy_role_model_json['role_id'] = 'testString'
        policy_role_model_json['display_name'] = 'testString'
        policy_role_model_json['description'] = 'testString'

        # Construct a model instance of PolicyRole by calling from_dict on the json representation
        policy_role_model = PolicyRole.from_dict(policy_role_model_json)
        assert policy_role_model != False

        # Construct a model instance of PolicyRole by calling from_dict on the json representation
        policy_role_model_dict = PolicyRole.from_dict(policy_role_model_json).__dict__
        policy_role_model2 = PolicyRole(**policy_role_model_dict)

        # Verify the model instances are equivalent
        assert policy_role_model == policy_role_model2

        # Convert model instance back to dict and verify no loss of data
        policy_role_model_json2 = policy_role_model.to_dict()
        assert policy_role_model_json2 == policy_role_model_json

#-----------------------------------------------------------------------------
# Test Class for PolicySubject
#-----------------------------------------------------------------------------
class TestPolicySubject():

    #--------------------------------------------------------
    # Test serialization/deserialization for PolicySubject
    #--------------------------------------------------------
    def test_policy_subject_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        subject_attribute_model = {} # SubjectAttribute
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        # Construct a json representation of a PolicySubject model
        policy_subject_model_json = {}
        policy_subject_model_json['attributes'] = [subject_attribute_model]

        # Construct a model instance of PolicySubject by calling from_dict on the json representation
        policy_subject_model = PolicySubject.from_dict(policy_subject_model_json)
        assert policy_subject_model != False

        # Construct a model instance of PolicySubject by calling from_dict on the json representation
        policy_subject_model_dict = PolicySubject.from_dict(policy_subject_model_json).__dict__
        policy_subject_model2 = PolicySubject(**policy_subject_model_dict)

        # Verify the model instances are equivalent
        assert policy_subject_model == policy_subject_model2

        # Convert model instance back to dict and verify no loss of data
        policy_subject_model_json2 = policy_subject_model.to_dict()
        assert policy_subject_model_json2 == policy_subject_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceAttribute
#-----------------------------------------------------------------------------
class TestResourceAttribute():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceAttribute
    #--------------------------------------------------------
    def test_resource_attribute_serialization(self):

        # Construct a json representation of a ResourceAttribute model
        resource_attribute_model_json = {}
        resource_attribute_model_json['name'] = 'testString'
        resource_attribute_model_json['value'] = 'testString'
        resource_attribute_model_json['operator'] = 'testString'

        # Construct a model instance of ResourceAttribute by calling from_dict on the json representation
        resource_attribute_model = ResourceAttribute.from_dict(resource_attribute_model_json)
        assert resource_attribute_model != False

        # Construct a model instance of ResourceAttribute by calling from_dict on the json representation
        resource_attribute_model_dict = ResourceAttribute.from_dict(resource_attribute_model_json).__dict__
        resource_attribute_model2 = ResourceAttribute(**resource_attribute_model_dict)

        # Verify the model instances are equivalent
        assert resource_attribute_model == resource_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        resource_attribute_model_json2 = resource_attribute_model.to_dict()
        assert resource_attribute_model_json2 == resource_attribute_model_json

#-----------------------------------------------------------------------------
# Test Class for Role
#-----------------------------------------------------------------------------
class TestRole():

    #--------------------------------------------------------
    # Test serialization/deserialization for Role
    #--------------------------------------------------------
    def test_role_serialization(self):

        # Construct a json representation of a Role model
        role_model_json = {}
        role_model_json['display_name'] = 'testString'
        role_model_json['description'] = 'testString'
        role_model_json['actions'] = ['testString']
        role_model_json['crn'] = 'testString'

        # Construct a model instance of Role by calling from_dict on the json representation
        role_model = Role.from_dict(role_model_json)
        assert role_model != False

        # Construct a model instance of Role by calling from_dict on the json representation
        role_model_dict = Role.from_dict(role_model_json).__dict__
        role_model2 = Role(**role_model_dict)

        # Verify the model instances are equivalent
        assert role_model == role_model2

        # Convert model instance back to dict and verify no loss of data
        role_model_json2 = role_model.to_dict()
        assert role_model_json2 == role_model_json

#-----------------------------------------------------------------------------
# Test Class for RoleList
#-----------------------------------------------------------------------------
class TestRoleList():

    #--------------------------------------------------------
    # Test serialization/deserialization for RoleList
    #--------------------------------------------------------
    def test_role_list_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        custom_role_model = {} # CustomRole
        custom_role_model['id'] = 'testString'
        custom_role_model['display_name'] = 'testString'
        custom_role_model['description'] = 'testString'
        custom_role_model['actions'] = ['testString']
        custom_role_model['crn'] = 'testString'
        custom_role_model['name'] = 'testString'
        custom_role_model['account_id'] = 'testString'
        custom_role_model['service_name'] = 'testString'
        custom_role_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        custom_role_model['created_by_id'] = 'testString'
        custom_role_model['last_modified_at'] = '2020-01-28T18:40:40.123456Z'
        custom_role_model['last_modified_by_id'] = 'testString'
        custom_role_model['href'] = 'testString'

        role_model = {} # Role
        role_model['display_name'] = 'testString'
        role_model['description'] = 'testString'
        role_model['actions'] = ['testString']
        role_model['crn'] = 'testString'

        # Construct a json representation of a RoleList model
        role_list_model_json = {}
        role_list_model_json['custom_roles'] = [custom_role_model]
        role_list_model_json['service_roles'] = [role_model]
        role_list_model_json['system_roles'] = [role_model]

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

#-----------------------------------------------------------------------------
# Test Class for SubjectAttribute
#-----------------------------------------------------------------------------
class TestSubjectAttribute():

    #--------------------------------------------------------
    # Test serialization/deserialization for SubjectAttribute
    #--------------------------------------------------------
    def test_subject_attribute_serialization(self):

        # Construct a json representation of a SubjectAttribute model
        subject_attribute_model_json = {}
        subject_attribute_model_json['name'] = 'testString'
        subject_attribute_model_json['value'] = 'testString'

        # Construct a model instance of SubjectAttribute by calling from_dict on the json representation
        subject_attribute_model = SubjectAttribute.from_dict(subject_attribute_model_json)
        assert subject_attribute_model != False

        # Construct a model instance of SubjectAttribute by calling from_dict on the json representation
        subject_attribute_model_dict = SubjectAttribute.from_dict(subject_attribute_model_json).__dict__
        subject_attribute_model2 = SubjectAttribute(**subject_attribute_model_dict)

        # Verify the model instances are equivalent
        assert subject_attribute_model == subject_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        subject_attribute_model_json2 = subject_attribute_model.to_dict()
        assert subject_attribute_model_json2 == subject_attribute_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
