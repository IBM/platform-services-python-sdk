# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
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
Unit Tests for IamPolicyManagementV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.iam_policy_management_v1 import *


_service = IamPolicyManagementV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://iam.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Policies
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = IamPolicyManagementV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamPolicyManagementV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamPolicyManagementV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListPolicies():
    """
    Test Class for list_policies
    """

    @responses.activate
    def test_list_policies_all_params(self):
        """
        list_policies()
        """
        # Set up mock
        url = preprocess_url('/v1/policies')
        mock_response = '{"policies": [{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        accept_language = 'default'
        iam_id = 'testString'
        access_group_id = 'testString'
        type = 'access'
        service_type = 'service'
        tag_name = 'testString'
        tag_value = 'testString'
        sort = 'id'
        format = 'include_last_permit'
        state = 'active'

        # Invoke method
        response = _service.list_policies(
            account_id,
            accept_language=accept_language,
            iam_id=iam_id,
            access_group_id=access_group_id,
            type=type,
            service_type=service_type,
            tag_name=tag_name,
            tag_value=tag_value,
            sort=sort,
            format=format,
            state=state,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'iam_id={}'.format(iam_id) in query_string
        assert 'access_group_id={}'.format(access_group_id) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'service_type={}'.format(service_type) in query_string
        assert 'tag_name={}'.format(tag_name) in query_string
        assert 'tag_value={}'.format(tag_value) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'format={}'.format(format) in query_string
        assert 'state={}'.format(state) in query_string

    def test_list_policies_all_params_with_retries(self):
        # Enable retries and run test_list_policies_all_params.
        _service.enable_retries()
        self.test_list_policies_all_params()

        # Disable retries and run test_list_policies_all_params.
        _service.disable_retries()
        self.test_list_policies_all_params()

    @responses.activate
    def test_list_policies_required_params(self):
        """
        test_list_policies_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/policies')
        mock_response = '{"policies": [{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_policies(
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_list_policies_required_params_with_retries(self):
        # Enable retries and run test_list_policies_required_params.
        _service.enable_retries()
        self.test_list_policies_required_params()

        # Disable retries and run test_list_policies_required_params.
        _service.disable_retries()
        self.test_list_policies_required_params()

    @responses.activate
    def test_list_policies_value_error(self):
        """
        test_list_policies_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policies')
        mock_response = '{"policies": [{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}]}'
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
                _service.list_policies(**req_copy)

    def test_list_policies_value_error_with_retries(self):
        # Enable retries and run test_list_policies_value_error.
        _service.enable_retries()
        self.test_list_policies_value_error()

        # Disable retries and run test_list_policies_value_error.
        _service.disable_retries()
        self.test_list_policies_value_error()

class TestCreatePolicy():
    """
    Test Class for create_policy
    """

    @responses.activate
    def test_create_policy_all_params(self):
        """
        create_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/policies')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
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

        # Construct a dict representation of a ResourceTag model
        resource_tag_model = {}
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]
        policy_resource_model['tags'] = [resource_tag_model]

        # Set up parameter values
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]
        description = 'testString'
        accept_language = 'default'

        # Invoke method
        response = _service.create_policy(
            type,
            subjects,
            roles,
            resources,
            description=description,
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
        assert req_body['description'] == 'testString'

    def test_create_policy_all_params_with_retries(self):
        # Enable retries and run test_create_policy_all_params.
        _service.enable_retries()
        self.test_create_policy_all_params()

        # Disable retries and run test_create_policy_all_params.
        _service.disable_retries()
        self.test_create_policy_all_params()

    @responses.activate
    def test_create_policy_required_params(self):
        """
        test_create_policy_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/policies')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
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

        # Construct a dict representation of a ResourceTag model
        resource_tag_model = {}
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]
        policy_resource_model['tags'] = [resource_tag_model]

        # Set up parameter values
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]
        description = 'testString'

        # Invoke method
        response = _service.create_policy(
            type,
            subjects,
            roles,
            resources,
            description=description,
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
        assert req_body['description'] == 'testString'

    def test_create_policy_required_params_with_retries(self):
        # Enable retries and run test_create_policy_required_params.
        _service.enable_retries()
        self.test_create_policy_required_params()

        # Disable retries and run test_create_policy_required_params.
        _service.disable_retries()
        self.test_create_policy_required_params()

    @responses.activate
    def test_create_policy_value_error(self):
        """
        test_create_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policies')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
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

        # Construct a dict representation of a ResourceTag model
        resource_tag_model = {}
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]
        policy_resource_model['tags'] = [resource_tag_model]

        # Set up parameter values
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]
        description = 'testString'

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
                _service.create_policy(**req_copy)

    def test_create_policy_value_error_with_retries(self):
        # Enable retries and run test_create_policy_value_error.
        _service.enable_retries()
        self.test_create_policy_value_error()

        # Disable retries and run test_create_policy_value_error.
        _service.disable_retries()
        self.test_create_policy_value_error()

class TestUpdatePolicy():
    """
    Test Class for update_policy
    """

    @responses.activate
    def test_update_policy_all_params(self):
        """
        update_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
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

        # Construct a dict representation of a ResourceTag model
        resource_tag_model = {}
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]
        policy_resource_model['tags'] = [resource_tag_model]

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]
        description = 'testString'

        # Invoke method
        response = _service.update_policy(
            policy_id,
            if_match,
            type,
            subjects,
            roles,
            resources,
            description=description,
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
        assert req_body['description'] == 'testString'

    def test_update_policy_all_params_with_retries(self):
        # Enable retries and run test_update_policy_all_params.
        _service.enable_retries()
        self.test_update_policy_all_params()

        # Disable retries and run test_update_policy_all_params.
        _service.disable_retries()
        self.test_update_policy_all_params()

    @responses.activate
    def test_update_policy_value_error(self):
        """
        test_update_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
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

        # Construct a dict representation of a ResourceTag model
        resource_tag_model = {}
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        # Construct a dict representation of a PolicyResource model
        policy_resource_model = {}
        policy_resource_model['attributes'] = [resource_attribute_model]
        policy_resource_model['tags'] = [resource_tag_model]

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        subjects = [policy_subject_model]
        roles = [policy_role_model]
        resources = [policy_resource_model]
        description = 'testString'

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
                _service.update_policy(**req_copy)

    def test_update_policy_value_error_with_retries(self):
        # Enable retries and run test_update_policy_value_error.
        _service.enable_retries()
        self.test_update_policy_value_error()

        # Disable retries and run test_update_policy_value_error.
        _service.disable_retries()
        self.test_update_policy_value_error()

class TestGetPolicy():
    """
    Test Class for get_policy
    """

    @responses.activate
    def test_get_policy_all_params(self):
        """
        get_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = _service.get_policy(
            policy_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_policy_all_params_with_retries(self):
        # Enable retries and run test_get_policy_all_params.
        _service.enable_retries()
        self.test_get_policy_all_params()

        # Disable retries and run test_get_policy_all_params.
        _service.disable_retries()
        self.test_get_policy_all_params()

    @responses.activate
    def test_get_policy_value_error(self):
        """
        test_get_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
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
                _service.get_policy(**req_copy)

    def test_get_policy_value_error_with_retries(self):
        # Enable retries and run test_get_policy_value_error.
        _service.enable_retries()
        self.test_get_policy_value_error()

        # Disable retries and run test_get_policy_value_error.
        _service.disable_retries()
        self.test_get_policy_value_error()

class TestDeletePolicy():
    """
    Test Class for delete_policy
    """

    @responses.activate
    def test_delete_policy_all_params(self):
        """
        delete_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = _service.delete_policy(
            policy_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_policy_all_params_with_retries(self):
        # Enable retries and run test_delete_policy_all_params.
        _service.enable_retries()
        self.test_delete_policy_all_params()

        # Disable retries and run test_delete_policy_all_params.
        _service.disable_retries()
        self.test_delete_policy_all_params()

    @responses.activate
    def test_delete_policy_value_error(self):
        """
        test_delete_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
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
                _service.delete_policy(**req_copy)

    def test_delete_policy_value_error_with_retries(self):
        # Enable retries and run test_delete_policy_value_error.
        _service.enable_retries()
        self.test_delete_policy_value_error()

        # Disable retries and run test_delete_policy_value_error.
        _service.disable_retries()
        self.test_delete_policy_value_error()

class TestPatchPolicy():
    """
    Test Class for patch_policy
    """

    @responses.activate
    def test_patch_policy_all_params(self):
        """
        patch_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        state = 'active'

        # Invoke method
        response = _service.patch_policy(
            policy_id,
            if_match,
            state=state,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['state'] == 'active'

    def test_patch_policy_all_params_with_retries(self):
        # Enable retries and run test_patch_policy_all_params.
        _service.enable_retries()
        self.test_patch_policy_all_params()

        # Disable retries and run test_patch_policy_all_params.
        _service.disable_retries()
        self.test_patch_policy_all_params()

    @responses.activate
    def test_patch_policy_value_error(self):
        """
        test_patch_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        state = 'active'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.patch_policy(**req_copy)

    def test_patch_policy_value_error_with_retries(self):
        # Enable retries and run test_patch_policy_value_error.
        _service.enable_retries()
        self.test_patch_policy_value_error()

        # Disable retries and run test_patch_policy_value_error.
        _service.disable_retries()
        self.test_patch_policy_value_error()

# endregion
##############################################################################
# End of Service: Policies
##############################################################################

##############################################################################
# Start of Service: Roles
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = IamPolicyManagementV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamPolicyManagementV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamPolicyManagementV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListRoles():
    """
    Test Class for list_roles
    """

    @responses.activate
    def test_list_roles_all_params(self):
        """
        list_roles()
        """
        # Set up mock
        url = preprocess_url('/v2/roles')
        mock_response = '{"custom_roles": [{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}], "service_roles": [{"display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn"}], "system_roles": [{"display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accept_language = 'default'
        account_id = 'testString'
        service_name = 'iam-groups'
        source_service_name = 'iam-groups'
        policy_type = 'authorization'

        # Invoke method
        response = _service.list_roles(
            accept_language=accept_language,
            account_id=account_id,
            service_name=service_name,
            source_service_name=source_service_name,
            policy_type=policy_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'service_name={}'.format(service_name) in query_string
        assert 'source_service_name={}'.format(source_service_name) in query_string
        assert 'policy_type={}'.format(policy_type) in query_string

    def test_list_roles_all_params_with_retries(self):
        # Enable retries and run test_list_roles_all_params.
        _service.enable_retries()
        self.test_list_roles_all_params()

        # Disable retries and run test_list_roles_all_params.
        _service.disable_retries()
        self.test_list_roles_all_params()

    @responses.activate
    def test_list_roles_required_params(self):
        """
        test_list_roles_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/roles')
        mock_response = '{"custom_roles": [{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}], "service_roles": [{"display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn"}], "system_roles": [{"display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_roles()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_roles_required_params_with_retries(self):
        # Enable retries and run test_list_roles_required_params.
        _service.enable_retries()
        self.test_list_roles_required_params()

        # Disable retries and run test_list_roles_required_params.
        _service.disable_retries()
        self.test_list_roles_required_params()

class TestCreateRole():
    """
    Test Class for create_role
    """

    @responses.activate
    def test_create_role_all_params(self):
        """
        create_role()
        """
        # Set up mock
        url = preprocess_url('/v2/roles')
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        display_name = 'testString'
        actions = ['testString']
        name = 'Developer'
        account_id = 'testString'
        service_name = 'iam-groups'
        description = 'testString'
        accept_language = 'default'

        # Invoke method
        response = _service.create_role(
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
        assert req_body['name'] == 'Developer'
        assert req_body['account_id'] == 'testString'
        assert req_body['service_name'] == 'iam-groups'
        assert req_body['description'] == 'testString'

    def test_create_role_all_params_with_retries(self):
        # Enable retries and run test_create_role_all_params.
        _service.enable_retries()
        self.test_create_role_all_params()

        # Disable retries and run test_create_role_all_params.
        _service.disable_retries()
        self.test_create_role_all_params()

    @responses.activate
    def test_create_role_required_params(self):
        """
        test_create_role_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/roles')
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        display_name = 'testString'
        actions = ['testString']
        name = 'Developer'
        account_id = 'testString'
        service_name = 'iam-groups'
        description = 'testString'

        # Invoke method
        response = _service.create_role(
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
        assert req_body['name'] == 'Developer'
        assert req_body['account_id'] == 'testString'
        assert req_body['service_name'] == 'iam-groups'
        assert req_body['description'] == 'testString'

    def test_create_role_required_params_with_retries(self):
        # Enable retries and run test_create_role_required_params.
        _service.enable_retries()
        self.test_create_role_required_params()

        # Disable retries and run test_create_role_required_params.
        _service.disable_retries()
        self.test_create_role_required_params()

    @responses.activate
    def test_create_role_value_error(self):
        """
        test_create_role_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/roles')
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        display_name = 'testString'
        actions = ['testString']
        name = 'Developer'
        account_id = 'testString'
        service_name = 'iam-groups'
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
                _service.create_role(**req_copy)

    def test_create_role_value_error_with_retries(self):
        # Enable retries and run test_create_role_value_error.
        _service.enable_retries()
        self.test_create_role_value_error()

        # Disable retries and run test_create_role_value_error.
        _service.disable_retries()
        self.test_create_role_value_error()

class TestUpdateRole():
    """
    Test Class for update_role
    """

    @responses.activate
    def test_update_role_all_params(self):
        """
        update_role()
        """
        # Set up mock
        url = preprocess_url('/v2/roles/testString')
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
        response = _service.update_role(
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

    def test_update_role_all_params_with_retries(self):
        # Enable retries and run test_update_role_all_params.
        _service.enable_retries()
        self.test_update_role_all_params()

        # Disable retries and run test_update_role_all_params.
        _service.disable_retries()
        self.test_update_role_all_params()

    @responses.activate
    def test_update_role_value_error(self):
        """
        test_update_role_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/roles/testString')
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
                _service.update_role(**req_copy)

    def test_update_role_value_error_with_retries(self):
        # Enable retries and run test_update_role_value_error.
        _service.enable_retries()
        self.test_update_role_value_error()

        # Disable retries and run test_update_role_value_error.
        _service.disable_retries()
        self.test_update_role_value_error()

class TestGetRole():
    """
    Test Class for get_role
    """

    @responses.activate
    def test_get_role_all_params(self):
        """
        get_role()
        """
        # Set up mock
        url = preprocess_url('/v2/roles/testString')
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        role_id = 'testString'

        # Invoke method
        response = _service.get_role(
            role_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_role_all_params_with_retries(self):
        # Enable retries and run test_get_role_all_params.
        _service.enable_retries()
        self.test_get_role_all_params()

        # Disable retries and run test_get_role_all_params.
        _service.disable_retries()
        self.test_get_role_all_params()

    @responses.activate
    def test_get_role_value_error(self):
        """
        test_get_role_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/roles/testString')
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
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
                _service.get_role(**req_copy)

    def test_get_role_value_error_with_retries(self):
        # Enable retries and run test_get_role_value_error.
        _service.enable_retries()
        self.test_get_role_value_error()

        # Disable retries and run test_get_role_value_error.
        _service.disable_retries()
        self.test_get_role_value_error()

class TestDeleteRole():
    """
    Test Class for delete_role
    """

    @responses.activate
    def test_delete_role_all_params(self):
        """
        delete_role()
        """
        # Set up mock
        url = preprocess_url('/v2/roles/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        role_id = 'testString'

        # Invoke method
        response = _service.delete_role(
            role_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_role_all_params_with_retries(self):
        # Enable retries and run test_delete_role_all_params.
        _service.enable_retries()
        self.test_delete_role_all_params()

        # Disable retries and run test_delete_role_all_params.
        _service.disable_retries()
        self.test_delete_role_all_params()

    @responses.activate
    def test_delete_role_value_error(self):
        """
        test_delete_role_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/roles/testString')
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
                _service.delete_role(**req_copy)

    def test_delete_role_value_error_with_retries(self):
        # Enable retries and run test_delete_role_value_error.
        _service.enable_retries()
        self.test_delete_role_value_error()

        # Disable retries and run test_delete_role_value_error.
        _service.disable_retries()
        self.test_delete_role_value_error()

# endregion
##############################################################################
# End of Service: Roles
##############################################################################

##############################################################################
# Start of Service: V2Policies
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = IamPolicyManagementV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamPolicyManagementV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamPolicyManagementV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestV2ListPolicies():
    """
    Test Class for v2_list_policies
    """

    @responses.activate
    def test_v2_list_policies_all_params(self):
        """
        v2_list_policies()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"policies": [{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        accept_language = 'default'
        iam_id = 'testString'
        access_group_id = 'testString'
        type = 'access'
        service_type = 'service'
        service_name = 'testString'
        service_group_id = 'testString'
        format = 'include_last_permit'
        state = 'active'

        # Invoke method
        response = _service.v2_list_policies(
            account_id,
            accept_language=accept_language,
            iam_id=iam_id,
            access_group_id=access_group_id,
            type=type,
            service_type=service_type,
            service_name=service_name,
            service_group_id=service_group_id,
            format=format,
            state=state,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'iam_id={}'.format(iam_id) in query_string
        assert 'access_group_id={}'.format(access_group_id) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'service_type={}'.format(service_type) in query_string
        assert 'service_name={}'.format(service_name) in query_string
        assert 'service_group_id={}'.format(service_group_id) in query_string
        assert 'format={}'.format(format) in query_string
        assert 'state={}'.format(state) in query_string

    def test_v2_list_policies_all_params_with_retries(self):
        # Enable retries and run test_v2_list_policies_all_params.
        _service.enable_retries()
        self.test_v2_list_policies_all_params()

        # Disable retries and run test_v2_list_policies_all_params.
        _service.disable_retries()
        self.test_v2_list_policies_all_params()

    @responses.activate
    def test_v2_list_policies_required_params(self):
        """
        test_v2_list_policies_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"policies": [{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.v2_list_policies(
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_v2_list_policies_required_params_with_retries(self):
        # Enable retries and run test_v2_list_policies_required_params.
        _service.enable_retries()
        self.test_v2_list_policies_required_params()

        # Disable retries and run test_v2_list_policies_required_params.
        _service.disable_retries()
        self.test_v2_list_policies_required_params()

    @responses.activate
    def test_v2_list_policies_value_error(self):
        """
        test_v2_list_policies_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"policies": [{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}]}'
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
                _service.v2_list_policies(**req_copy)

    def test_v2_list_policies_value_error_with_retries(self):
        # Enable retries and run test_v2_list_policies_value_error.
        _service.enable_retries()
        self.test_v2_list_policies_value_error()

        # Disable retries and run test_v2_list_policies_value_error.
        _service.disable_retries()
        self.test_v2_list_policies_value_error()

class TestV2CreatePolicy():
    """
    Test Class for v2_create_policy
    """

    @responses.activate
    def test_v2_create_policy_all_params(self):
        """
        v2_create_policy()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseControlGrant model
        v2_policy_base_control_grant_model = {}
        v2_policy_base_control_grant_model['roles'] = [policy_role_model]

        # Construct a dict representation of a V2PolicyBaseControl model
        v2_policy_base_control_model = {}
        v2_policy_base_control_model['grant'] = v2_policy_base_control_grant_model

        # Construct a dict representation of a V2PolicyAttribute model
        v2_policy_attribute_model = {}
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseSubject model
        v2_policy_base_subject_model = {}
        v2_policy_base_subject_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseResource model
        v2_policy_base_resource_model = {}
        v2_policy_base_resource_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseRuleV2PolicyAttribute model
        v2_policy_base_rule_model = {}
        v2_policy_base_rule_model['key'] = 'testString'
        v2_policy_base_rule_model['operator'] = 'testString'
        v2_policy_base_rule_model['value'] = 'testString'

        # Set up parameter values
        type = 'testString'
        control = v2_policy_base_control_model
        description = 'testString'
        subject = v2_policy_base_subject_model
        resource = v2_policy_base_resource_model
        pattern = 'testString'
        rule = v2_policy_base_rule_model
        accept_language = 'default'

        # Invoke method
        response = _service.v2_create_policy(
            type,
            control,
            description=description,
            subject=subject,
            resource=resource,
            pattern=pattern,
            rule=rule,
            accept_language=accept_language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'testString'
        assert req_body['control'] == v2_policy_base_control_model
        assert req_body['description'] == 'testString'
        assert req_body['subject'] == v2_policy_base_subject_model
        assert req_body['resource'] == v2_policy_base_resource_model
        assert req_body['pattern'] == 'testString'
        assert req_body['rule'] == v2_policy_base_rule_model

    def test_v2_create_policy_all_params_with_retries(self):
        # Enable retries and run test_v2_create_policy_all_params.
        _service.enable_retries()
        self.test_v2_create_policy_all_params()

        # Disable retries and run test_v2_create_policy_all_params.
        _service.disable_retries()
        self.test_v2_create_policy_all_params()

    @responses.activate
    def test_v2_create_policy_required_params(self):
        """
        test_v2_create_policy_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseControlGrant model
        v2_policy_base_control_grant_model = {}
        v2_policy_base_control_grant_model['roles'] = [policy_role_model]

        # Construct a dict representation of a V2PolicyBaseControl model
        v2_policy_base_control_model = {}
        v2_policy_base_control_model['grant'] = v2_policy_base_control_grant_model

        # Construct a dict representation of a V2PolicyAttribute model
        v2_policy_attribute_model = {}
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseSubject model
        v2_policy_base_subject_model = {}
        v2_policy_base_subject_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseResource model
        v2_policy_base_resource_model = {}
        v2_policy_base_resource_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseRuleV2PolicyAttribute model
        v2_policy_base_rule_model = {}
        v2_policy_base_rule_model['key'] = 'testString'
        v2_policy_base_rule_model['operator'] = 'testString'
        v2_policy_base_rule_model['value'] = 'testString'

        # Set up parameter values
        type = 'testString'
        control = v2_policy_base_control_model
        description = 'testString'
        subject = v2_policy_base_subject_model
        resource = v2_policy_base_resource_model
        pattern = 'testString'
        rule = v2_policy_base_rule_model

        # Invoke method
        response = _service.v2_create_policy(
            type,
            control,
            description=description,
            subject=subject,
            resource=resource,
            pattern=pattern,
            rule=rule,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'testString'
        assert req_body['control'] == v2_policy_base_control_model
        assert req_body['description'] == 'testString'
        assert req_body['subject'] == v2_policy_base_subject_model
        assert req_body['resource'] == v2_policy_base_resource_model
        assert req_body['pattern'] == 'testString'
        assert req_body['rule'] == v2_policy_base_rule_model

    def test_v2_create_policy_required_params_with_retries(self):
        # Enable retries and run test_v2_create_policy_required_params.
        _service.enable_retries()
        self.test_v2_create_policy_required_params()

        # Disable retries and run test_v2_create_policy_required_params.
        _service.disable_retries()
        self.test_v2_create_policy_required_params()

    @responses.activate
    def test_v2_create_policy_value_error(self):
        """
        test_v2_create_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseControlGrant model
        v2_policy_base_control_grant_model = {}
        v2_policy_base_control_grant_model['roles'] = [policy_role_model]

        # Construct a dict representation of a V2PolicyBaseControl model
        v2_policy_base_control_model = {}
        v2_policy_base_control_model['grant'] = v2_policy_base_control_grant_model

        # Construct a dict representation of a V2PolicyAttribute model
        v2_policy_attribute_model = {}
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseSubject model
        v2_policy_base_subject_model = {}
        v2_policy_base_subject_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseResource model
        v2_policy_base_resource_model = {}
        v2_policy_base_resource_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseRuleV2PolicyAttribute model
        v2_policy_base_rule_model = {}
        v2_policy_base_rule_model['key'] = 'testString'
        v2_policy_base_rule_model['operator'] = 'testString'
        v2_policy_base_rule_model['value'] = 'testString'

        # Set up parameter values
        type = 'testString'
        control = v2_policy_base_control_model
        description = 'testString'
        subject = v2_policy_base_subject_model
        resource = v2_policy_base_resource_model
        pattern = 'testString'
        rule = v2_policy_base_rule_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "type": type,
            "control": control,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.v2_create_policy(**req_copy)

    def test_v2_create_policy_value_error_with_retries(self):
        # Enable retries and run test_v2_create_policy_value_error.
        _service.enable_retries()
        self.test_v2_create_policy_value_error()

        # Disable retries and run test_v2_create_policy_value_error.
        _service.disable_retries()
        self.test_v2_create_policy_value_error()

class TestV2UpdatePolicy():
    """
    Test Class for v2_update_policy
    """

    @responses.activate
    def test_v2_update_policy_all_params(self):
        """
        v2_update_policy()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseControlGrant model
        v2_policy_base_control_grant_model = {}
        v2_policy_base_control_grant_model['roles'] = [policy_role_model]

        # Construct a dict representation of a V2PolicyBaseControl model
        v2_policy_base_control_model = {}
        v2_policy_base_control_model['grant'] = v2_policy_base_control_grant_model

        # Construct a dict representation of a V2PolicyAttribute model
        v2_policy_attribute_model = {}
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseSubject model
        v2_policy_base_subject_model = {}
        v2_policy_base_subject_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseResource model
        v2_policy_base_resource_model = {}
        v2_policy_base_resource_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseRuleV2PolicyAttribute model
        v2_policy_base_rule_model = {}
        v2_policy_base_rule_model['key'] = 'testString'
        v2_policy_base_rule_model['operator'] = 'testString'
        v2_policy_base_rule_model['value'] = 'testString'

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        control = v2_policy_base_control_model
        description = 'testString'
        subject = v2_policy_base_subject_model
        resource = v2_policy_base_resource_model
        pattern = 'testString'
        rule = v2_policy_base_rule_model

        # Invoke method
        response = _service.v2_update_policy(
            policy_id,
            if_match,
            type,
            control,
            description=description,
            subject=subject,
            resource=resource,
            pattern=pattern,
            rule=rule,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'testString'
        assert req_body['control'] == v2_policy_base_control_model
        assert req_body['description'] == 'testString'
        assert req_body['subject'] == v2_policy_base_subject_model
        assert req_body['resource'] == v2_policy_base_resource_model
        assert req_body['pattern'] == 'testString'
        assert req_body['rule'] == v2_policy_base_rule_model

    def test_v2_update_policy_all_params_with_retries(self):
        # Enable retries and run test_v2_update_policy_all_params.
        _service.enable_retries()
        self.test_v2_update_policy_all_params()

        # Disable retries and run test_v2_update_policy_all_params.
        _service.disable_retries()
        self.test_v2_update_policy_all_params()

    @responses.activate
    def test_v2_update_policy_value_error(self):
        """
        test_v2_update_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PolicyRole model
        policy_role_model = {}
        policy_role_model['role_id'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseControlGrant model
        v2_policy_base_control_grant_model = {}
        v2_policy_base_control_grant_model['roles'] = [policy_role_model]

        # Construct a dict representation of a V2PolicyBaseControl model
        v2_policy_base_control_model = {}
        v2_policy_base_control_model['grant'] = v2_policy_base_control_grant_model

        # Construct a dict representation of a V2PolicyAttribute model
        v2_policy_attribute_model = {}
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyBaseSubject model
        v2_policy_base_subject_model = {}
        v2_policy_base_subject_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseResource model
        v2_policy_base_resource_model = {}
        v2_policy_base_resource_model['attributes'] = [v2_policy_attribute_model]

        # Construct a dict representation of a V2PolicyBaseRuleV2PolicyAttribute model
        v2_policy_base_rule_model = {}
        v2_policy_base_rule_model['key'] = 'testString'
        v2_policy_base_rule_model['operator'] = 'testString'
        v2_policy_base_rule_model['value'] = 'testString'

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        control = v2_policy_base_control_model
        description = 'testString'
        subject = v2_policy_base_subject_model
        resource = v2_policy_base_resource_model
        pattern = 'testString'
        rule = v2_policy_base_rule_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
            "if_match": if_match,
            "type": type,
            "control": control,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.v2_update_policy(**req_copy)

    def test_v2_update_policy_value_error_with_retries(self):
        # Enable retries and run test_v2_update_policy_value_error.
        _service.enable_retries()
        self.test_v2_update_policy_value_error()

        # Disable retries and run test_v2_update_policy_value_error.
        _service.disable_retries()
        self.test_v2_update_policy_value_error()

class TestV2GetPolicy():
    """
    Test Class for v2_get_policy
    """

    @responses.activate
    def test_v2_get_policy_all_params(self):
        """
        v2_get_policy()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = _service.v2_get_policy(
            policy_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_v2_get_policy_all_params_with_retries(self):
        # Enable retries and run test_v2_get_policy_all_params.
        _service.enable_retries()
        self.test_v2_get_policy_all_params()

        # Disable retries and run test_v2_get_policy_all_params.
        _service.disable_retries()
        self.test_v2_get_policy_all_params()

    @responses.activate
    def test_v2_get_policy_value_error(self):
        """
        test_v2_get_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "control": {"grant": {"roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}]}}, "resource": {"attributes": [{"key": "key", "operator": "operator", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "operator", "value": "anyValue"}, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
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
                _service.v2_get_policy(**req_copy)

    def test_v2_get_policy_value_error_with_retries(self):
        # Enable retries and run test_v2_get_policy_value_error.
        _service.enable_retries()
        self.test_v2_get_policy_value_error()

        # Disable retries and run test_v2_get_policy_value_error.
        _service.disable_retries()
        self.test_v2_get_policy_value_error()

class TestV2DeletePolicy():
    """
    Test Class for v2_delete_policy
    """

    @responses.activate
    def test_v2_delete_policy_all_params(self):
        """
        v2_delete_policy()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = _service.v2_delete_policy(
            policy_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_v2_delete_policy_all_params_with_retries(self):
        # Enable retries and run test_v2_delete_policy_all_params.
        _service.enable_retries()
        self.test_v2_delete_policy_all_params()

        # Disable retries and run test_v2_delete_policy_all_params.
        _service.disable_retries()
        self.test_v2_delete_policy_all_params()

    @responses.activate
    def test_v2_delete_policy_value_error(self):
        """
        test_v2_delete_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
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
                _service.v2_delete_policy(**req_copy)

    def test_v2_delete_policy_value_error_with_retries(self):
        # Enable retries and run test_v2_delete_policy_value_error.
        _service.enable_retries()
        self.test_v2_delete_policy_value_error()

        # Disable retries and run test_v2_delete_policy_value_error.
        _service.disable_retries()
        self.test_v2_delete_policy_value_error()

# endregion
##############################################################################
# End of Service: V2Policies
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_V2PolicyBaseControl():
    """
    Test Class for V2PolicyBaseControl
    """

    def test_v2_policy_base_control_serialization(self):
        """
        Test serialization/deserialization for V2PolicyBaseControl
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_role_model = {} # PolicyRole
        policy_role_model['role_id'] = 'testString'

        v2_policy_base_control_grant_model = {} # V2PolicyBaseControlGrant
        v2_policy_base_control_grant_model['roles'] = [policy_role_model]

        # Construct a json representation of a V2PolicyBaseControl model
        v2_policy_base_control_model_json = {}
        v2_policy_base_control_model_json['grant'] = v2_policy_base_control_grant_model

        # Construct a model instance of V2PolicyBaseControl by calling from_dict on the json representation
        v2_policy_base_control_model = V2PolicyBaseControl.from_dict(v2_policy_base_control_model_json)
        assert v2_policy_base_control_model != False

        # Construct a model instance of V2PolicyBaseControl by calling from_dict on the json representation
        v2_policy_base_control_model_dict = V2PolicyBaseControl.from_dict(v2_policy_base_control_model_json).__dict__
        v2_policy_base_control_model2 = V2PolicyBaseControl(**v2_policy_base_control_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_base_control_model == v2_policy_base_control_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_base_control_model_json2 = v2_policy_base_control_model.to_dict()
        assert v2_policy_base_control_model_json2 == v2_policy_base_control_model_json

class TestModel_V2PolicyBaseControlGrant():
    """
    Test Class for V2PolicyBaseControlGrant
    """

    def test_v2_policy_base_control_grant_serialization(self):
        """
        Test serialization/deserialization for V2PolicyBaseControlGrant
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_role_model = {} # PolicyRole
        policy_role_model['role_id'] = 'testString'

        # Construct a json representation of a V2PolicyBaseControlGrant model
        v2_policy_base_control_grant_model_json = {}
        v2_policy_base_control_grant_model_json['roles'] = [policy_role_model]

        # Construct a model instance of V2PolicyBaseControlGrant by calling from_dict on the json representation
        v2_policy_base_control_grant_model = V2PolicyBaseControlGrant.from_dict(v2_policy_base_control_grant_model_json)
        assert v2_policy_base_control_grant_model != False

        # Construct a model instance of V2PolicyBaseControlGrant by calling from_dict on the json representation
        v2_policy_base_control_grant_model_dict = V2PolicyBaseControlGrant.from_dict(v2_policy_base_control_grant_model_json).__dict__
        v2_policy_base_control_grant_model2 = V2PolicyBaseControlGrant(**v2_policy_base_control_grant_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_base_control_grant_model == v2_policy_base_control_grant_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_base_control_grant_model_json2 = v2_policy_base_control_grant_model.to_dict()
        assert v2_policy_base_control_grant_model_json2 == v2_policy_base_control_grant_model_json

class TestModel_V2PolicyBaseResource():
    """
    Test Class for V2PolicyBaseResource
    """

    def test_v2_policy_base_resource_serialization(self):
        """
        Test serialization/deserialization for V2PolicyBaseResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_attribute_model = {} # V2PolicyAttribute
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        # Construct a json representation of a V2PolicyBaseResource model
        v2_policy_base_resource_model_json = {}
        v2_policy_base_resource_model_json['attributes'] = [v2_policy_attribute_model]

        # Construct a model instance of V2PolicyBaseResource by calling from_dict on the json representation
        v2_policy_base_resource_model = V2PolicyBaseResource.from_dict(v2_policy_base_resource_model_json)
        assert v2_policy_base_resource_model != False

        # Construct a model instance of V2PolicyBaseResource by calling from_dict on the json representation
        v2_policy_base_resource_model_dict = V2PolicyBaseResource.from_dict(v2_policy_base_resource_model_json).__dict__
        v2_policy_base_resource_model2 = V2PolicyBaseResource(**v2_policy_base_resource_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_base_resource_model == v2_policy_base_resource_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_base_resource_model_json2 = v2_policy_base_resource_model.to_dict()
        assert v2_policy_base_resource_model_json2 == v2_policy_base_resource_model_json

class TestModel_V2PolicyBaseSubject():
    """
    Test Class for V2PolicyBaseSubject
    """

    def test_v2_policy_base_subject_serialization(self):
        """
        Test serialization/deserialization for V2PolicyBaseSubject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_attribute_model = {} # V2PolicyAttribute
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        # Construct a json representation of a V2PolicyBaseSubject model
        v2_policy_base_subject_model_json = {}
        v2_policy_base_subject_model_json['attributes'] = [v2_policy_attribute_model]

        # Construct a model instance of V2PolicyBaseSubject by calling from_dict on the json representation
        v2_policy_base_subject_model = V2PolicyBaseSubject.from_dict(v2_policy_base_subject_model_json)
        assert v2_policy_base_subject_model != False

        # Construct a model instance of V2PolicyBaseSubject by calling from_dict on the json representation
        v2_policy_base_subject_model_dict = V2PolicyBaseSubject.from_dict(v2_policy_base_subject_model_json).__dict__
        v2_policy_base_subject_model2 = V2PolicyBaseSubject(**v2_policy_base_subject_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_base_subject_model == v2_policy_base_subject_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_base_subject_model_json2 = v2_policy_base_subject_model.to_dict()
        assert v2_policy_base_subject_model_json2 == v2_policy_base_subject_model_json

class TestModel_CustomRole():
    """
    Test Class for CustomRole
    """

    def test_custom_role_serialization(self):
        """
        Test serialization/deserialization for CustomRole
        """

        # Construct a json representation of a CustomRole model
        custom_role_model_json = {}
        custom_role_model_json['display_name'] = 'testString'
        custom_role_model_json['description'] = 'testString'
        custom_role_model_json['actions'] = ['testString']
        custom_role_model_json['name'] = 'Developer'
        custom_role_model_json['account_id'] = 'testString'
        custom_role_model_json['service_name'] = 'iam-groups'

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

class TestModel_Policy():
    """
    Test Class for Policy
    """

    def test_policy_serialization(self):
        """
        Test serialization/deserialization for Policy
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subject_attribute_model = {} # SubjectAttribute
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        policy_subject_model = {} # PolicySubject
        policy_subject_model['attributes'] = [subject_attribute_model]

        policy_role_model = {} # PolicyRole
        policy_role_model['role_id'] = 'testString'

        resource_attribute_model = {} # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_model = {} # ResourceTag
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        policy_resource_model = {} # PolicyResource
        policy_resource_model['attributes'] = [resource_attribute_model]
        policy_resource_model['tags'] = [resource_tag_model]

        # Construct a json representation of a Policy model
        policy_model_json = {}
        policy_model_json['type'] = 'testString'
        policy_model_json['description'] = 'testString'
        policy_model_json['subjects'] = [policy_subject_model]
        policy_model_json['roles'] = [policy_role_model]
        policy_model_json['resources'] = [policy_resource_model]
        policy_model_json['state'] = 'active'

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

class TestModel_PolicyList():
    """
    Test Class for PolicyList
    """

    def test_policy_list_serialization(self):
        """
        Test serialization/deserialization for PolicyList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subject_attribute_model = {} # SubjectAttribute
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        policy_subject_model = {} # PolicySubject
        policy_subject_model['attributes'] = [subject_attribute_model]

        policy_role_model = {} # PolicyRole
        policy_role_model['role_id'] = 'testString'

        resource_attribute_model = {} # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_model = {} # ResourceTag
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        policy_resource_model = {} # PolicyResource
        policy_resource_model['attributes'] = [resource_attribute_model]
        policy_resource_model['tags'] = [resource_tag_model]

        policy_model = {} # Policy
        policy_model['type'] = 'testString'
        policy_model['description'] = 'testString'
        policy_model['subjects'] = [policy_subject_model]
        policy_model['roles'] = [policy_role_model]
        policy_model['resources'] = [policy_resource_model]
        policy_model['state'] = 'active'

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

class TestModel_PolicyResource():
    """
    Test Class for PolicyResource
    """

    def test_policy_resource_serialization(self):
        """
        Test serialization/deserialization for PolicyResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_attribute_model = {} # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_model = {} # ResourceTag
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        # Construct a json representation of a PolicyResource model
        policy_resource_model_json = {}
        policy_resource_model_json['attributes'] = [resource_attribute_model]
        policy_resource_model_json['tags'] = [resource_tag_model]

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

class TestModel_PolicyRole():
    """
    Test Class for PolicyRole
    """

    def test_policy_role_serialization(self):
        """
        Test serialization/deserialization for PolicyRole
        """

        # Construct a json representation of a PolicyRole model
        policy_role_model_json = {}
        policy_role_model_json['role_id'] = 'testString'

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

class TestModel_PolicySubject():
    """
    Test Class for PolicySubject
    """

    def test_policy_subject_serialization(self):
        """
        Test serialization/deserialization for PolicySubject
        """

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

class TestModel_ResourceAttribute():
    """
    Test Class for ResourceAttribute
    """

    def test_resource_attribute_serialization(self):
        """
        Test serialization/deserialization for ResourceAttribute
        """

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

class TestModel_ResourceTag():
    """
    Test Class for ResourceTag
    """

    def test_resource_tag_serialization(self):
        """
        Test serialization/deserialization for ResourceTag
        """

        # Construct a json representation of a ResourceTag model
        resource_tag_model_json = {}
        resource_tag_model_json['name'] = 'testString'
        resource_tag_model_json['value'] = 'testString'
        resource_tag_model_json['operator'] = 'testString'

        # Construct a model instance of ResourceTag by calling from_dict on the json representation
        resource_tag_model = ResourceTag.from_dict(resource_tag_model_json)
        assert resource_tag_model != False

        # Construct a model instance of ResourceTag by calling from_dict on the json representation
        resource_tag_model_dict = ResourceTag.from_dict(resource_tag_model_json).__dict__
        resource_tag_model2 = ResourceTag(**resource_tag_model_dict)

        # Verify the model instances are equivalent
        assert resource_tag_model == resource_tag_model2

        # Convert model instance back to dict and verify no loss of data
        resource_tag_model_json2 = resource_tag_model.to_dict()
        assert resource_tag_model_json2 == resource_tag_model_json

class TestModel_Role():
    """
    Test Class for Role
    """

    def test_role_serialization(self):
        """
        Test serialization/deserialization for Role
        """

        # Construct a json representation of a Role model
        role_model_json = {}
        role_model_json['display_name'] = 'testString'
        role_model_json['description'] = 'testString'
        role_model_json['actions'] = ['testString']

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

class TestModel_RoleList():
    """
    Test Class for RoleList
    """

    def test_role_list_serialization(self):
        """
        Test serialization/deserialization for RoleList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        custom_role_model = {} # CustomRole
        custom_role_model['display_name'] = 'testString'
        custom_role_model['description'] = 'testString'
        custom_role_model['actions'] = ['testString']
        custom_role_model['name'] = 'Developer'
        custom_role_model['account_id'] = 'testString'
        custom_role_model['service_name'] = 'iam-groups'

        role_model = {} # Role
        role_model['display_name'] = 'testString'
        role_model['description'] = 'testString'
        role_model['actions'] = ['testString']

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

class TestModel_SubjectAttribute():
    """
    Test Class for SubjectAttribute
    """

    def test_subject_attribute_serialization(self):
        """
        Test serialization/deserialization for SubjectAttribute
        """

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

class TestModel_V2Policy():
    """
    Test Class for V2Policy
    """

    def test_v2_policy_serialization(self):
        """
        Test serialization/deserialization for V2Policy
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_attribute_model = {} # V2PolicyAttribute
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        v2_policy_base_subject_model = {} # V2PolicyBaseSubject
        v2_policy_base_subject_model['attributes'] = [v2_policy_attribute_model]

        policy_role_model = {} # PolicyRole
        policy_role_model['role_id'] = 'testString'

        v2_policy_base_control_grant_model = {} # V2PolicyBaseControlGrant
        v2_policy_base_control_grant_model['roles'] = [policy_role_model]

        v2_policy_base_control_model = {} # V2PolicyBaseControl
        v2_policy_base_control_model['grant'] = v2_policy_base_control_grant_model

        v2_policy_base_resource_model = {} # V2PolicyBaseResource
        v2_policy_base_resource_model['attributes'] = [v2_policy_attribute_model]

        v2_policy_base_rule_model = {} # V2PolicyBaseRuleV2PolicyAttribute
        v2_policy_base_rule_model['key'] = 'testString'
        v2_policy_base_rule_model['operator'] = 'testString'
        v2_policy_base_rule_model['value'] = 'testString'

        # Construct a json representation of a V2Policy model
        v2_policy_model_json = {}
        v2_policy_model_json['type'] = 'testString'
        v2_policy_model_json['description'] = 'testString'
        v2_policy_model_json['subject'] = v2_policy_base_subject_model
        v2_policy_model_json['control'] = v2_policy_base_control_model
        v2_policy_model_json['resource'] = v2_policy_base_resource_model
        v2_policy_model_json['pattern'] = 'testString'
        v2_policy_model_json['rule'] = v2_policy_base_rule_model
        v2_policy_model_json['state'] = 'active'

        # Construct a model instance of V2Policy by calling from_dict on the json representation
        v2_policy_model = V2Policy.from_dict(v2_policy_model_json)
        assert v2_policy_model != False

        # Construct a model instance of V2Policy by calling from_dict on the json representation
        v2_policy_model_dict = V2Policy.from_dict(v2_policy_model_json).__dict__
        v2_policy_model2 = V2Policy(**v2_policy_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_model == v2_policy_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_model_json2 = v2_policy_model.to_dict()
        assert v2_policy_model_json2 == v2_policy_model_json

class TestModel_V2PolicyAttribute():
    """
    Test Class for V2PolicyAttribute
    """

    def test_v2_policy_attribute_serialization(self):
        """
        Test serialization/deserialization for V2PolicyAttribute
        """

        # Construct a json representation of a V2PolicyAttribute model
        v2_policy_attribute_model_json = {}
        v2_policy_attribute_model_json['key'] = 'testString'
        v2_policy_attribute_model_json['operator'] = 'testString'
        v2_policy_attribute_model_json['value'] = 'testString'

        # Construct a model instance of V2PolicyAttribute by calling from_dict on the json representation
        v2_policy_attribute_model = V2PolicyAttribute.from_dict(v2_policy_attribute_model_json)
        assert v2_policy_attribute_model != False

        # Construct a model instance of V2PolicyAttribute by calling from_dict on the json representation
        v2_policy_attribute_model_dict = V2PolicyAttribute.from_dict(v2_policy_attribute_model_json).__dict__
        v2_policy_attribute_model2 = V2PolicyAttribute(**v2_policy_attribute_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_attribute_model == v2_policy_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_attribute_model_json2 = v2_policy_attribute_model.to_dict()
        assert v2_policy_attribute_model_json2 == v2_policy_attribute_model_json

class TestModel_V2PolicyList():
    """
    Test Class for V2PolicyList
    """

    def test_v2_policy_list_serialization(self):
        """
        Test serialization/deserialization for V2PolicyList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_attribute_model = {} # V2PolicyAttribute
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        v2_policy_base_subject_model = {} # V2PolicyBaseSubject
        v2_policy_base_subject_model['attributes'] = [v2_policy_attribute_model]

        policy_role_model = {} # PolicyRole
        policy_role_model['role_id'] = 'testString'

        v2_policy_base_control_grant_model = {} # V2PolicyBaseControlGrant
        v2_policy_base_control_grant_model['roles'] = [policy_role_model]

        v2_policy_base_control_model = {} # V2PolicyBaseControl
        v2_policy_base_control_model['grant'] = v2_policy_base_control_grant_model

        v2_policy_base_resource_model = {} # V2PolicyBaseResource
        v2_policy_base_resource_model['attributes'] = [v2_policy_attribute_model]

        v2_policy_base_rule_model = {} # V2PolicyBaseRuleV2PolicyAttribute
        v2_policy_base_rule_model['key'] = 'testString'
        v2_policy_base_rule_model['operator'] = 'testString'
        v2_policy_base_rule_model['value'] = 'testString'

        v2_policy_model = {} # V2Policy
        v2_policy_model['type'] = 'testString'
        v2_policy_model['description'] = 'testString'
        v2_policy_model['subject'] = v2_policy_base_subject_model
        v2_policy_model['control'] = v2_policy_base_control_model
        v2_policy_model['resource'] = v2_policy_base_resource_model
        v2_policy_model['pattern'] = 'testString'
        v2_policy_model['rule'] = v2_policy_base_rule_model
        v2_policy_model['state'] = 'active'

        # Construct a json representation of a V2PolicyList model
        v2_policy_list_model_json = {}
        v2_policy_list_model_json['policies'] = [v2_policy_model]

        # Construct a model instance of V2PolicyList by calling from_dict on the json representation
        v2_policy_list_model = V2PolicyList.from_dict(v2_policy_list_model_json)
        assert v2_policy_list_model != False

        # Construct a model instance of V2PolicyList by calling from_dict on the json representation
        v2_policy_list_model_dict = V2PolicyList.from_dict(v2_policy_list_model_json).__dict__
        v2_policy_list_model2 = V2PolicyList(**v2_policy_list_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_list_model == v2_policy_list_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_list_model_json2 = v2_policy_list_model.to_dict()
        assert v2_policy_list_model_json2 == v2_policy_list_model_json

class TestModel_V2PolicyBaseRuleV2PolicyAttribute():
    """
    Test Class for V2PolicyBaseRuleV2PolicyAttribute
    """

    def test_v2_policy_base_rule_v2_policy_attribute_serialization(self):
        """
        Test serialization/deserialization for V2PolicyBaseRuleV2PolicyAttribute
        """

        # Construct a json representation of a V2PolicyBaseRuleV2PolicyAttribute model
        v2_policy_base_rule_v2_policy_attribute_model_json = {}
        v2_policy_base_rule_v2_policy_attribute_model_json['key'] = 'testString'
        v2_policy_base_rule_v2_policy_attribute_model_json['operator'] = 'testString'
        v2_policy_base_rule_v2_policy_attribute_model_json['value'] = 'testString'

        # Construct a model instance of V2PolicyBaseRuleV2PolicyAttribute by calling from_dict on the json representation
        v2_policy_base_rule_v2_policy_attribute_model = V2PolicyBaseRuleV2PolicyAttribute.from_dict(v2_policy_base_rule_v2_policy_attribute_model_json)
        assert v2_policy_base_rule_v2_policy_attribute_model != False

        # Construct a model instance of V2PolicyBaseRuleV2PolicyAttribute by calling from_dict on the json representation
        v2_policy_base_rule_v2_policy_attribute_model_dict = V2PolicyBaseRuleV2PolicyAttribute.from_dict(v2_policy_base_rule_v2_policy_attribute_model_json).__dict__
        v2_policy_base_rule_v2_policy_attribute_model2 = V2PolicyBaseRuleV2PolicyAttribute(**v2_policy_base_rule_v2_policy_attribute_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_base_rule_v2_policy_attribute_model == v2_policy_base_rule_v2_policy_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_base_rule_v2_policy_attribute_model_json2 = v2_policy_base_rule_v2_policy_attribute_model.to_dict()
        assert v2_policy_base_rule_v2_policy_attribute_model_json2 == v2_policy_base_rule_v2_policy_attribute_model_json

class TestModel_V2PolicyBaseRuleV2RuleWithConditions():
    """
    Test Class for V2PolicyBaseRuleV2RuleWithConditions
    """

    def test_v2_policy_base_rule_v2_rule_with_conditions_serialization(self):
        """
        Test serialization/deserialization for V2PolicyBaseRuleV2RuleWithConditions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_attribute_model = {} # V2PolicyAttribute
        v2_policy_attribute_model['key'] = 'testString'
        v2_policy_attribute_model['operator'] = 'testString'
        v2_policy_attribute_model['value'] = 'testString'

        # Construct a json representation of a V2PolicyBaseRuleV2RuleWithConditions model
        v2_policy_base_rule_v2_rule_with_conditions_model_json = {}
        v2_policy_base_rule_v2_rule_with_conditions_model_json['operator'] = 'and'
        v2_policy_base_rule_v2_rule_with_conditions_model_json['conditions'] = [v2_policy_attribute_model]

        # Construct a model instance of V2PolicyBaseRuleV2RuleWithConditions by calling from_dict on the json representation
        v2_policy_base_rule_v2_rule_with_conditions_model = V2PolicyBaseRuleV2RuleWithConditions.from_dict(v2_policy_base_rule_v2_rule_with_conditions_model_json)
        assert v2_policy_base_rule_v2_rule_with_conditions_model != False

        # Construct a model instance of V2PolicyBaseRuleV2RuleWithConditions by calling from_dict on the json representation
        v2_policy_base_rule_v2_rule_with_conditions_model_dict = V2PolicyBaseRuleV2RuleWithConditions.from_dict(v2_policy_base_rule_v2_rule_with_conditions_model_json).__dict__
        v2_policy_base_rule_v2_rule_with_conditions_model2 = V2PolicyBaseRuleV2RuleWithConditions(**v2_policy_base_rule_v2_rule_with_conditions_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_base_rule_v2_rule_with_conditions_model == v2_policy_base_rule_v2_rule_with_conditions_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_base_rule_v2_rule_with_conditions_model_json2 = v2_policy_base_rule_v2_rule_with_conditions_model.to_dict()
        assert v2_policy_base_rule_v2_rule_with_conditions_model_json2 == v2_policy_base_rule_v2_rule_with_conditions_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
