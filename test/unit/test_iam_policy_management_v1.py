# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Policies
##############################################################################
# region


class TestNewInstance:
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


class TestListPolicies:
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
        mock_response = '{"policies": [{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        mock_response = '{"policies": [{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_policies(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        mock_response = '{"policies": [{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_policies(**req_copy)

    def test_list_policies_value_error_with_retries(self):
        # Enable retries and run test_list_policies_value_error.
        _service.enable_retries()
        self.test_list_policies_value_error()

        # Disable retries and run test_list_policies_value_error.
        _service.disable_retries()
        self.test_list_policies_value_error()


class TestCreatePolicy:
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            headers={},
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            headers={},
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_policy(**req_copy)

    def test_create_policy_value_error_with_retries(self):
        # Enable retries and run test_create_policy_value_error.
        _service.enable_retries()
        self.test_create_policy_value_error()

        # Disable retries and run test_create_policy_value_error.
        _service.disable_retries()
        self.test_create_policy_value_error()


class TestReplacePolicy:
    """
    Test Class for replace_policy
    """

    @responses.activate
    def test_replace_policy_all_params(self):
        """
        replace_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        response = _service.replace_policy(
            policy_id,
            if_match,
            type,
            subjects,
            roles,
            resources,
            description=description,
            headers={},
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

    def test_replace_policy_all_params_with_retries(self):
        # Enable retries and run test_replace_policy_all_params.
        _service.enable_retries()
        self.test_replace_policy_all_params()

        # Disable retries and run test_replace_policy_all_params.
        _service.disable_retries()
        self.test_replace_policy_all_params()

    @responses.activate
    def test_replace_policy_value_error(self):
        """
        test_replace_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_policy(**req_copy)

    def test_replace_policy_value_error_with_retries(self):
        # Enable retries and run test_replace_policy_value_error.
        _service.enable_retries()
        self.test_replace_policy_value_error()

        # Disable retries and run test_replace_policy_value_error.
        _service.disable_retries()
        self.test_replace_policy_value_error()


class TestGetPolicy:
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
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = _service.get_policy(
            policy_id,
            headers={},
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
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_policy(**req_copy)

    def test_get_policy_value_error_with_retries(self):
        # Enable retries and run test_get_policy_value_error.
        _service.enable_retries()
        self.test_get_policy_value_error()

        # Disable retries and run test_get_policy_value_error.
        _service.disable_retries()
        self.test_get_policy_value_error()


class TestDeletePolicy:
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        policy_id = 'testString'

        # Invoke method
        response = _service.delete_policy(
            policy_id,
            headers={},
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        policy_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_policy(**req_copy)

    def test_delete_policy_value_error_with_retries(self):
        # Enable retries and run test_delete_policy_value_error.
        _service.enable_retries()
        self.test_delete_policy_value_error()

        # Disable retries and run test_delete_policy_value_error.
        _service.disable_retries()
        self.test_delete_policy_value_error()


class TestUpdatePolicyState:
    """
    Test Class for update_policy_state
    """

    @responses.activate
    def test_update_policy_state_all_params(self):
        """
        update_policy_state()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_id = 'testString'
        if_match = 'testString'
        state = 'active'

        # Invoke method
        response = _service.update_policy_state(
            policy_id,
            if_match,
            state=state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['state'] == 'active'

    def test_update_policy_state_all_params_with_retries(self):
        # Enable retries and run test_update_policy_state_all_params.
        _service.enable_retries()
        self.test_update_policy_state_all_params()

        # Disable retries and run test_update_policy_state_all_params.
        _service.disable_retries()
        self.test_update_policy_state_all_params()

    @responses.activate
    def test_update_policy_state_value_error(self):
        """
        test_update_policy_state_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policies/testString')
        mock_response = '{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_policy_state(**req_copy)

    def test_update_policy_state_value_error_with_retries(self):
        # Enable retries and run test_update_policy_state_value_error.
        _service.enable_retries()
        self.test_update_policy_state_value_error()

        # Disable retries and run test_update_policy_state_value_error.
        _service.disable_retries()
        self.test_update_policy_state_value_error()


# endregion
##############################################################################
# End of Service: Policies
##############################################################################

##############################################################################
# Start of Service: Roles
##############################################################################
# region


class TestNewInstance:
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


class TestListRoles:
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
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        accept_language = 'default'
        account_id = 'testString'
        service_name = 'iam-groups'
        source_service_name = 'iam-groups'
        policy_type = 'authorization'
        service_group_id = 'IAM'

        # Invoke method
        response = _service.list_roles(
            accept_language=accept_language,
            account_id=account_id,
            service_name=service_name,
            source_service_name=source_service_name,
            policy_type=policy_type,
            service_group_id=service_group_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'service_name={}'.format(service_name) in query_string
        assert 'source_service_name={}'.format(source_service_name) in query_string
        assert 'policy_type={}'.format(policy_type) in query_string
        assert 'service_group_id={}'.format(service_group_id) in query_string

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
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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


class TestCreateRole:
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            headers={},
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            headers={},
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_role(**req_copy)

    def test_create_role_value_error_with_retries(self):
        # Enable retries and run test_create_role_value_error.
        _service.enable_retries()
        self.test_create_role_value_error()

        # Disable retries and run test_create_role_value_error.
        _service.disable_retries()
        self.test_create_role_value_error()


class TestReplaceRole:
    """
    Test Class for replace_role
    """

    @responses.activate
    def test_replace_role_all_params(self):
        """
        replace_role()
        """
        # Set up mock
        url = preprocess_url('/v2/roles/testString')
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_id = 'testString'
        if_match = 'testString'
        display_name = 'testString'
        actions = ['testString']
        description = 'testString'

        # Invoke method
        response = _service.replace_role(
            role_id,
            if_match,
            display_name,
            actions,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['display_name'] == 'testString'
        assert req_body['actions'] == ['testString']
        assert req_body['description'] == 'testString'

    def test_replace_role_all_params_with_retries(self):
        # Enable retries and run test_replace_role_all_params.
        _service.enable_retries()
        self.test_replace_role_all_params()

        # Disable retries and run test_replace_role_all_params.
        _service.disable_retries()
        self.test_replace_role_all_params()

    @responses.activate
    def test_replace_role_value_error(self):
        """
        test_replace_role_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/roles/testString')
        mock_response = '{"id": "id", "display_name": "display_name", "description": "description", "actions": ["actions"], "crn": "crn", "name": "Developer", "account_id": "account_id", "service_name": "iam-groups", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_id = 'testString'
        if_match = 'testString'
        display_name = 'testString'
        actions = ['testString']
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_id": role_id,
            "if_match": if_match,
            "display_name": display_name,
            "actions": actions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_role(**req_copy)

    def test_replace_role_value_error_with_retries(self):
        # Enable retries and run test_replace_role_value_error.
        _service.enable_retries()
        self.test_replace_role_value_error()

        # Disable retries and run test_replace_role_value_error.
        _service.disable_retries()
        self.test_replace_role_value_error()


class TestGetRole:
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
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_id = 'testString'

        # Invoke method
        response = _service.get_role(
            role_id,
            headers={},
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
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_id": role_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_role(**req_copy)

    def test_get_role_value_error_with_retries(self):
        # Enable retries and run test_get_role_value_error.
        _service.enable_retries()
        self.test_get_role_value_error()

        # Disable retries and run test_get_role_value_error.
        _service.disable_retries()
        self.test_get_role_value_error()


class TestDeleteRole:
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        role_id = 'testString'

        # Invoke method
        response = _service.delete_role(
            role_id,
            headers={},
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        role_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_id": role_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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


class TestNewInstance:
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


class TestListV2Policies:
    """
    Test Class for list_v2_policies
    """

    @responses.activate
    def test_list_v2_policies_all_params(self):
        """
        list_v2_policies()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"policies": [{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21, "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        accept_language = 'default'
        iam_id = 'testString'
        access_group_id = 'testString'
        type = 'access'
        service_type = 'service'
        service_name = 'testString'
        service_group_id = 'testString'
        sort = 'testString'
        format = 'include_last_permit'
        state = 'active'

        # Invoke method
        response = _service.list_v2_policies(
            account_id,
            accept_language=accept_language,
            iam_id=iam_id,
            access_group_id=access_group_id,
            type=type,
            service_type=service_type,
            service_name=service_name,
            service_group_id=service_group_id,
            sort=sort,
            format=format,
            state=state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'iam_id={}'.format(iam_id) in query_string
        assert 'access_group_id={}'.format(access_group_id) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'service_type={}'.format(service_type) in query_string
        assert 'service_name={}'.format(service_name) in query_string
        assert 'service_group_id={}'.format(service_group_id) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'format={}'.format(format) in query_string
        assert 'state={}'.format(state) in query_string

    def test_list_v2_policies_all_params_with_retries(self):
        # Enable retries and run test_list_v2_policies_all_params.
        _service.enable_retries()
        self.test_list_v2_policies_all_params()

        # Disable retries and run test_list_v2_policies_all_params.
        _service.disable_retries()
        self.test_list_v2_policies_all_params()

    @responses.activate
    def test_list_v2_policies_required_params(self):
        """
        test_list_v2_policies_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"policies": [{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21, "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_v2_policies(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_list_v2_policies_required_params_with_retries(self):
        # Enable retries and run test_list_v2_policies_required_params.
        _service.enable_retries()
        self.test_list_v2_policies_required_params()

        # Disable retries and run test_list_v2_policies_required_params.
        _service.disable_retries()
        self.test_list_v2_policies_required_params()

    @responses.activate
    def test_list_v2_policies_value_error(self):
        """
        test_list_v2_policies_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"policies": [{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21, "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_v2_policies(**req_copy)

    def test_list_v2_policies_value_error_with_retries(self):
        # Enable retries and run test_list_v2_policies_value_error.
        _service.enable_retries()
        self.test_list_v2_policies_value_error()

        # Disable retries and run test_list_v2_policies_value_error.
        _service.disable_retries()
        self.test_list_v2_policies_value_error()


class TestCreateV2Policy:
    """
    Test Class for create_v2_policy
    """

    @responses.activate
    def test_create_v2_policy_all_params(self):
        """
        create_v2_policy()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Set up parameter values
        control = control_model
        type = 'access'
        description = 'testString'
        subject = v2_policy_subject_model
        resource = v2_policy_resource_model
        pattern = 'testString'
        rule = v2_policy_rule_model
        accept_language = 'default'

        # Invoke method
        response = _service.create_v2_policy(
            control,
            type,
            description=description,
            subject=subject,
            resource=resource,
            pattern=pattern,
            rule=rule,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['control'] == control_model
        assert req_body['type'] == 'access'
        assert req_body['description'] == 'testString'
        assert req_body['subject'] == v2_policy_subject_model
        assert req_body['resource'] == v2_policy_resource_model
        assert req_body['pattern'] == 'testString'
        assert req_body['rule'] == v2_policy_rule_model

    def test_create_v2_policy_all_params_with_retries(self):
        # Enable retries and run test_create_v2_policy_all_params.
        _service.enable_retries()
        self.test_create_v2_policy_all_params()

        # Disable retries and run test_create_v2_policy_all_params.
        _service.disable_retries()
        self.test_create_v2_policy_all_params()

    @responses.activate
    def test_create_v2_policy_required_params(self):
        """
        test_create_v2_policy_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Set up parameter values
        control = control_model
        type = 'access'
        description = 'testString'
        subject = v2_policy_subject_model
        resource = v2_policy_resource_model
        pattern = 'testString'
        rule = v2_policy_rule_model

        # Invoke method
        response = _service.create_v2_policy(
            control,
            type,
            description=description,
            subject=subject,
            resource=resource,
            pattern=pattern,
            rule=rule,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['control'] == control_model
        assert req_body['type'] == 'access'
        assert req_body['description'] == 'testString'
        assert req_body['subject'] == v2_policy_subject_model
        assert req_body['resource'] == v2_policy_resource_model
        assert req_body['pattern'] == 'testString'
        assert req_body['rule'] == v2_policy_rule_model

    def test_create_v2_policy_required_params_with_retries(self):
        # Enable retries and run test_create_v2_policy_required_params.
        _service.enable_retries()
        self.test_create_v2_policy_required_params()

        # Disable retries and run test_create_v2_policy_required_params.
        _service.disable_retries()
        self.test_create_v2_policy_required_params()

    @responses.activate
    def test_create_v2_policy_value_error(self):
        """
        test_create_v2_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies')
        mock_response = '{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Set up parameter values
        control = control_model
        type = 'access'
        description = 'testString'
        subject = v2_policy_subject_model
        resource = v2_policy_resource_model
        pattern = 'testString'
        rule = v2_policy_rule_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "control": control,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_v2_policy(**req_copy)

    def test_create_v2_policy_value_error_with_retries(self):
        # Enable retries and run test_create_v2_policy_value_error.
        _service.enable_retries()
        self.test_create_v2_policy_value_error()

        # Disable retries and run test_create_v2_policy_value_error.
        _service.disable_retries()
        self.test_create_v2_policy_value_error()


class TestReplaceV2Policy:
    """
    Test Class for replace_v2_policy
    """

    @responses.activate
    def test_replace_v2_policy_all_params(self):
        """
        replace_v2_policy()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        mock_response = '{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Set up parameter values
        id = 'testString'
        if_match = 'testString'
        control = control_model
        type = 'access'
        description = 'testString'
        subject = v2_policy_subject_model
        resource = v2_policy_resource_model
        pattern = 'testString'
        rule = v2_policy_rule_model

        # Invoke method
        response = _service.replace_v2_policy(
            id,
            if_match,
            control,
            type,
            description=description,
            subject=subject,
            resource=resource,
            pattern=pattern,
            rule=rule,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['control'] == control_model
        assert req_body['type'] == 'access'
        assert req_body['description'] == 'testString'
        assert req_body['subject'] == v2_policy_subject_model
        assert req_body['resource'] == v2_policy_resource_model
        assert req_body['pattern'] == 'testString'
        assert req_body['rule'] == v2_policy_rule_model

    def test_replace_v2_policy_all_params_with_retries(self):
        # Enable retries and run test_replace_v2_policy_all_params.
        _service.enable_retries()
        self.test_replace_v2_policy_all_params()

        # Disable retries and run test_replace_v2_policy_all_params.
        _service.disable_retries()
        self.test_replace_v2_policy_all_params()

    @responses.activate
    def test_replace_v2_policy_value_error(self):
        """
        test_replace_v2_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        mock_response = '{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Set up parameter values
        id = 'testString'
        if_match = 'testString'
        control = control_model
        type = 'access'
        description = 'testString'
        subject = v2_policy_subject_model
        resource = v2_policy_resource_model
        pattern = 'testString'
        rule = v2_policy_rule_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "if_match": if_match,
            "control": control,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_v2_policy(**req_copy)

    def test_replace_v2_policy_value_error_with_retries(self):
        # Enable retries and run test_replace_v2_policy_value_error.
        _service.enable_retries()
        self.test_replace_v2_policy_value_error()

        # Disable retries and run test_replace_v2_policy_value_error.
        _service.disable_retries()
        self.test_replace_v2_policy_value_error()


class TestGetV2Policy:
    """
    Test Class for get_v2_policy
    """

    @responses.activate
    def test_get_v2_policy_all_params(self):
        """
        get_v2_policy()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        mock_response = '{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21, "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        format = 'include_last_permit'

        # Invoke method
        response = _service.get_v2_policy(
            id,
            format=format,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'format={}'.format(format) in query_string

    def test_get_v2_policy_all_params_with_retries(self):
        # Enable retries and run test_get_v2_policy_all_params.
        _service.enable_retries()
        self.test_get_v2_policy_all_params()

        # Disable retries and run test_get_v2_policy_all_params.
        _service.disable_retries()
        self.test_get_v2_policy_all_params()

    @responses.activate
    def test_get_v2_policy_required_params(self):
        """
        test_get_v2_policy_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        mock_response = '{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21, "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_v2_policy(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_v2_policy_required_params_with_retries(self):
        # Enable retries and run test_get_v2_policy_required_params.
        _service.enable_retries()
        self.test_get_v2_policy_required_params()

        # Disable retries and run test_get_v2_policy_required_params.
        _service.disable_retries()
        self.test_get_v2_policy_required_params()

    @responses.activate
    def test_get_v2_policy_value_error(self):
        """
        test_get_v2_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        mock_response = '{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21, "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_v2_policy(**req_copy)

    def test_get_v2_policy_value_error_with_retries(self):
        # Enable retries and run test_get_v2_policy_value_error.
        _service.enable_retries()
        self.test_get_v2_policy_value_error()

        # Disable retries and run test_get_v2_policy_value_error.
        _service.disable_retries()
        self.test_get_v2_policy_value_error()


class TestDeleteV2Policy:
    """
    Test Class for delete_v2_policy
    """

    @responses.activate
    def test_delete_v2_policy_all_params(self):
        """
        delete_v2_policy()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_v2_policy(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_v2_policy_all_params_with_retries(self):
        # Enable retries and run test_delete_v2_policy_all_params.
        _service.enable_retries()
        self.test_delete_v2_policy_all_params()

        # Disable retries and run test_delete_v2_policy_all_params.
        _service.disable_retries()
        self.test_delete_v2_policy_all_params()

    @responses.activate
    def test_delete_v2_policy_value_error(self):
        """
        test_delete_v2_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/policies/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_v2_policy(**req_copy)

    def test_delete_v2_policy_value_error_with_retries(self):
        # Enable retries and run test_delete_v2_policy_value_error.
        _service.enable_retries()
        self.test_delete_v2_policy_value_error()

        # Disable retries and run test_delete_v2_policy_value_error.
        _service.disable_retries()
        self.test_delete_v2_policy_value_error()


# endregion
##############################################################################
# End of Service: V2Policies
##############################################################################

##############################################################################
# Start of Service: PolicyTemplates
##############################################################################
# region


class TestNewInstance:
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


class TestListPolicyTemplates:
    """
    Test Class for list_policy_templates
    """

    @responses.activate
    def test_list_policy_templates_all_params(self):
        """
        list_policy_templates()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates')
        mock_response = '{"policy_templates": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        accept_language = 'default'
        state = 'active'

        # Invoke method
        response = _service.list_policy_templates(
            account_id,
            accept_language=accept_language,
            state=state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'state={}'.format(state) in query_string

    def test_list_policy_templates_all_params_with_retries(self):
        # Enable retries and run test_list_policy_templates_all_params.
        _service.enable_retries()
        self.test_list_policy_templates_all_params()

        # Disable retries and run test_list_policy_templates_all_params.
        _service.disable_retries()
        self.test_list_policy_templates_all_params()

    @responses.activate
    def test_list_policy_templates_required_params(self):
        """
        test_list_policy_templates_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates')
        mock_response = '{"policy_templates": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_policy_templates(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_list_policy_templates_required_params_with_retries(self):
        # Enable retries and run test_list_policy_templates_required_params.
        _service.enable_retries()
        self.test_list_policy_templates_required_params()

        # Disable retries and run test_list_policy_templates_required_params.
        _service.disable_retries()
        self.test_list_policy_templates_required_params()

    @responses.activate
    def test_list_policy_templates_value_error(self):
        """
        test_list_policy_templates_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates')
        mock_response = '{"policy_templates": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_policy_templates(**req_copy)

    def test_list_policy_templates_value_error_with_retries(self):
        # Enable retries and run test_list_policy_templates_value_error.
        _service.enable_retries()
        self.test_list_policy_templates_value_error()

        # Disable retries and run test_list_policy_templates_value_error.
        _service.disable_retries()
        self.test_list_policy_templates_value_error()


class TestCreatePolicyTemplate:
    """
    Test Class for create_policy_template
    """

    @responses.activate
    def test_create_policy_template_all_params(self):
        """
        create_policy_template()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        policy = template_policy_model
        description = 'testString'
        committed = True
        accept_language = 'default'

        # Invoke method
        response = _service.create_policy_template(
            name,
            account_id,
            policy,
            description=description,
            committed=committed,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['policy'] == template_policy_model
        assert req_body['description'] == 'testString'
        assert req_body['committed'] == True

    def test_create_policy_template_all_params_with_retries(self):
        # Enable retries and run test_create_policy_template_all_params.
        _service.enable_retries()
        self.test_create_policy_template_all_params()

        # Disable retries and run test_create_policy_template_all_params.
        _service.disable_retries()
        self.test_create_policy_template_all_params()

    @responses.activate
    def test_create_policy_template_required_params(self):
        """
        test_create_policy_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        policy = template_policy_model
        description = 'testString'
        committed = True

        # Invoke method
        response = _service.create_policy_template(
            name,
            account_id,
            policy,
            description=description,
            committed=committed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['policy'] == template_policy_model
        assert req_body['description'] == 'testString'
        assert req_body['committed'] == True

    def test_create_policy_template_required_params_with_retries(self):
        # Enable retries and run test_create_policy_template_required_params.
        _service.enable_retries()
        self.test_create_policy_template_required_params()

        # Disable retries and run test_create_policy_template_required_params.
        _service.disable_retries()
        self.test_create_policy_template_required_params()

    @responses.activate
    def test_create_policy_template_value_error(self):
        """
        test_create_policy_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        policy = template_policy_model
        description = 'testString'
        committed = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "account_id": account_id,
            "policy": policy,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_policy_template(**req_copy)

    def test_create_policy_template_value_error_with_retries(self):
        # Enable retries and run test_create_policy_template_value_error.
        _service.enable_retries()
        self.test_create_policy_template_value_error()

        # Disable retries and run test_create_policy_template_value_error.
        _service.disable_retries()
        self.test_create_policy_template_value_error()


class TestGetPolicyTemplate:
    """
    Test Class for get_policy_template
    """

    @responses.activate
    def test_get_policy_template_all_params(self):
        """
        get_policy_template()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_template_id = 'testString'
        state = 'active'

        # Invoke method
        response = _service.get_policy_template(
            policy_template_id,
            state=state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'state={}'.format(state) in query_string

    def test_get_policy_template_all_params_with_retries(self):
        # Enable retries and run test_get_policy_template_all_params.
        _service.enable_retries()
        self.test_get_policy_template_all_params()

        # Disable retries and run test_get_policy_template_all_params.
        _service.disable_retries()
        self.test_get_policy_template_all_params()

    @responses.activate
    def test_get_policy_template_required_params(self):
        """
        test_get_policy_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_template_id = 'testString'

        # Invoke method
        response = _service.get_policy_template(
            policy_template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_policy_template_required_params_with_retries(self):
        # Enable retries and run test_get_policy_template_required_params.
        _service.enable_retries()
        self.test_get_policy_template_required_params()

        # Disable retries and run test_get_policy_template_required_params.
        _service.disable_retries()
        self.test_get_policy_template_required_params()

    @responses.activate
    def test_get_policy_template_value_error(self):
        """
        test_get_policy_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_template_id": policy_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_policy_template(**req_copy)

    def test_get_policy_template_value_error_with_retries(self):
        # Enable retries and run test_get_policy_template_value_error.
        _service.enable_retries()
        self.test_get_policy_template_value_error()

        # Disable retries and run test_get_policy_template_value_error.
        _service.disable_retries()
        self.test_get_policy_template_value_error()


class TestDeletePolicyTemplate:
    """
    Test Class for delete_policy_template
    """

    @responses.activate
    def test_delete_policy_template_all_params(self):
        """
        delete_policy_template()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        policy_template_id = 'testString'

        # Invoke method
        response = _service.delete_policy_template(
            policy_template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_policy_template_all_params_with_retries(self):
        # Enable retries and run test_delete_policy_template_all_params.
        _service.enable_retries()
        self.test_delete_policy_template_all_params()

        # Disable retries and run test_delete_policy_template_all_params.
        _service.disable_retries()
        self.test_delete_policy_template_all_params()

    @responses.activate
    def test_delete_policy_template_value_error(self):
        """
        test_delete_policy_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        policy_template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_template_id": policy_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_policy_template(**req_copy)

    def test_delete_policy_template_value_error_with_retries(self):
        # Enable retries and run test_delete_policy_template_value_error.
        _service.enable_retries()
        self.test_delete_policy_template_value_error()

        # Disable retries and run test_delete_policy_template_value_error.
        _service.disable_retries()
        self.test_delete_policy_template_value_error()


class TestCreatePolicyTemplateVersion:
    """
    Test Class for create_policy_template_version
    """

    @responses.activate
    def test_create_policy_template_version_all_params(self):
        """
        create_policy_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        # Set up parameter values
        policy_template_id = 'testString'
        policy = template_policy_model
        name = 'testString'
        description = 'testString'
        committed = True

        # Invoke method
        response = _service.create_policy_template_version(
            policy_template_id,
            policy,
            name=name,
            description=description,
            committed=committed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['policy'] == template_policy_model
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['committed'] == True

    def test_create_policy_template_version_all_params_with_retries(self):
        # Enable retries and run test_create_policy_template_version_all_params.
        _service.enable_retries()
        self.test_create_policy_template_version_all_params()

        # Disable retries and run test_create_policy_template_version_all_params.
        _service.disable_retries()
        self.test_create_policy_template_version_all_params()

    @responses.activate
    def test_create_policy_template_version_value_error(self):
        """
        test_create_policy_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        # Set up parameter values
        policy_template_id = 'testString'
        policy = template_policy_model
        name = 'testString'
        description = 'testString'
        committed = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_template_id": policy_template_id,
            "policy": policy,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_policy_template_version(**req_copy)

    def test_create_policy_template_version_value_error_with_retries(self):
        # Enable retries and run test_create_policy_template_version_value_error.
        _service.enable_retries()
        self.test_create_policy_template_version_value_error()

        # Disable retries and run test_create_policy_template_version_value_error.
        _service.disable_retries()
        self.test_create_policy_template_version_value_error()


class TestListPolicyTemplateVersions:
    """
    Test Class for list_policy_template_versions
    """

    @responses.activate
    def test_list_policy_template_versions_all_params(self):
        """
        list_policy_template_versions()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions')
        mock_response = '{"versions": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_template_id = 'testString'
        state = 'active'

        # Invoke method
        response = _service.list_policy_template_versions(
            policy_template_id,
            state=state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'state={}'.format(state) in query_string

    def test_list_policy_template_versions_all_params_with_retries(self):
        # Enable retries and run test_list_policy_template_versions_all_params.
        _service.enable_retries()
        self.test_list_policy_template_versions_all_params()

        # Disable retries and run test_list_policy_template_versions_all_params.
        _service.disable_retries()
        self.test_list_policy_template_versions_all_params()

    @responses.activate
    def test_list_policy_template_versions_required_params(self):
        """
        test_list_policy_template_versions_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions')
        mock_response = '{"versions": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_template_id = 'testString'

        # Invoke method
        response = _service.list_policy_template_versions(
            policy_template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_policy_template_versions_required_params_with_retries(self):
        # Enable retries and run test_list_policy_template_versions_required_params.
        _service.enable_retries()
        self.test_list_policy_template_versions_required_params()

        # Disable retries and run test_list_policy_template_versions_required_params.
        _service.disable_retries()
        self.test_list_policy_template_versions_required_params()

    @responses.activate
    def test_list_policy_template_versions_value_error(self):
        """
        test_list_policy_template_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions')
        mock_response = '{"versions": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_template_id": policy_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_policy_template_versions(**req_copy)

    def test_list_policy_template_versions_value_error_with_retries(self):
        # Enable retries and run test_list_policy_template_versions_value_error.
        _service.enable_retries()
        self.test_list_policy_template_versions_value_error()

        # Disable retries and run test_list_policy_template_versions_value_error.
        _service.disable_retries()
        self.test_list_policy_template_versions_value_error()


class TestReplacePolicyTemplate:
    """
    Test Class for replace_policy_template
    """

    @responses.activate
    def test_replace_policy_template_all_params(self):
        """
        replace_policy_template()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        # Set up parameter values
        policy_template_id = 'testString'
        version = 'testString'
        if_match = 'testString'
        policy = template_policy_model
        name = 'testString'
        description = 'testString'
        committed = True

        # Invoke method
        response = _service.replace_policy_template(
            policy_template_id,
            version,
            if_match,
            policy,
            name=name,
            description=description,
            committed=committed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['policy'] == template_policy_model
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['committed'] == True

    def test_replace_policy_template_all_params_with_retries(self):
        # Enable retries and run test_replace_policy_template_all_params.
        _service.enable_retries()
        self.test_replace_policy_template_all_params()

        # Disable retries and run test_replace_policy_template_all_params.
        _service.disable_retries()
        self.test_replace_policy_template_all_params()

    @responses.activate
    def test_replace_policy_template_value_error(self):
        """
        test_replace_policy_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model = {}
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model = {}
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a dict representation of a V2PolicyResource model
        v2_policy_resource_model = {}
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a Grant model
        grant_model = {}
        grant_model['roles'] = [roles_model]

        # Construct a dict representation of a Control model
        control_model = {}
        control_model['grant'] = grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        # Set up parameter values
        policy_template_id = 'testString'
        version = 'testString'
        if_match = 'testString'
        policy = template_policy_model
        name = 'testString'
        description = 'testString'
        committed = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_template_id": policy_template_id,
            "version": version,
            "if_match": if_match,
            "policy": policy,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_policy_template(**req_copy)

    def test_replace_policy_template_value_error_with_retries(self):
        # Enable retries and run test_replace_policy_template_value_error.
        _service.enable_retries()
        self.test_replace_policy_template_value_error()

        # Disable retries and run test_replace_policy_template_value_error.
        _service.disable_retries()
        self.test_replace_policy_template_value_error()


class TestDeletePolicyTemplateVersion:
    """
    Test Class for delete_policy_template_version
    """

    @responses.activate
    def test_delete_policy_template_version_all_params(self):
        """
        delete_policy_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        policy_template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.delete_policy_template_version(
            policy_template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_policy_template_version_all_params_with_retries(self):
        # Enable retries and run test_delete_policy_template_version_all_params.
        _service.enable_retries()
        self.test_delete_policy_template_version_all_params()

        # Disable retries and run test_delete_policy_template_version_all_params.
        _service.disable_retries()
        self.test_delete_policy_template_version_all_params()

    @responses.activate
    def test_delete_policy_template_version_value_error(self):
        """
        test_delete_policy_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        policy_template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_template_id": policy_template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_policy_template_version(**req_copy)

    def test_delete_policy_template_version_value_error_with_retries(self):
        # Enable retries and run test_delete_policy_template_version_value_error.
        _service.enable_retries()
        self.test_delete_policy_template_version_value_error()

        # Disable retries and run test_delete_policy_template_version_value_error.
        _service.disable_retries()
        self.test_delete_policy_template_version_value_error()


class TestGetPolicyTemplateVersion:
    """
    Test Class for get_policy_template_version
    """

    @responses.activate
    def test_get_policy_template_version_all_params(self):
        """
        get_policy_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.get_policy_template_version(
            policy_template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_policy_template_version_all_params_with_retries(self):
        # Enable retries and run test_get_policy_template_version_all_params.
        _service.enable_retries()
        self.test_get_policy_template_version_all_params()

        # Disable retries and run test_get_policy_template_version_all_params.
        _service.disable_retries()
        self.test_get_policy_template_version_all_params()

    @responses.activate
    def test_get_policy_template_version_value_error(self):
        """
        test_get_policy_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        policy_template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_template_id": policy_template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_policy_template_version(**req_copy)

    def test_get_policy_template_version_value_error_with_retries(self):
        # Enable retries and run test_get_policy_template_version_value_error.
        _service.enable_retries()
        self.test_get_policy_template_version_value_error()

        # Disable retries and run test_get_policy_template_version_value_error.
        _service.disable_retries()
        self.test_get_policy_template_version_value_error()


class TestCommitPolicyTemplate:
    """
    Test Class for commit_policy_template
    """

    @responses.activate
    def test_commit_policy_template_all_params(self):
        """
        commit_policy_template()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        policy_template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.commit_policy_template(
            policy_template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_commit_policy_template_all_params_with_retries(self):
        # Enable retries and run test_commit_policy_template_all_params.
        _service.enable_retries()
        self.test_commit_policy_template_all_params()

        # Disable retries and run test_commit_policy_template_all_params.
        _service.disable_retries()
        self.test_commit_policy_template_all_params()

    @responses.activate
    def test_commit_policy_template_value_error(self):
        """
        test_commit_policy_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        policy_template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "policy_template_id": policy_template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.commit_policy_template(**req_copy)

    def test_commit_policy_template_value_error_with_retries(self):
        # Enable retries and run test_commit_policy_template_value_error.
        _service.enable_retries()
        self.test_commit_policy_template_value_error()

        # Disable retries and run test_commit_policy_template_value_error.
        _service.disable_retries()
        self.test_commit_policy_template_value_error()


# endregion
##############################################################################
# End of Service: PolicyTemplates
##############################################################################

##############################################################################
# Start of Service: PolicyAssignments
##############################################################################
# region


class TestNewInstance:
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


class TestListPolicyAssignments:
    """
    Test Class for list_policy_assignments
    """

    @responses.activate
    def test_list_policy_assignments_all_params(self):
        """
        list_policy_assignments()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments')
        mock_response = '{"assignments": [{"template_id": "template_id", "template_version": "template_version", "assignment_id": "assignment_id", "target_type": "Account", "target": "target", "options": [{"subject_type": "iam_id", "subject_id": "subject_id", "root_requester_id": "root_requester_id", "root_template_id": "root_template_id", "root_template_version": "root_template_version"}], "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": "target", "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"trace": "trace", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}], "status_code": 11}}}], "status": "in_progress"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        accept_language = 'default'
        template_id = 'testString'
        template_version = 'testString'

        # Invoke method
        response = _service.list_policy_assignments(
            account_id,
            accept_language=accept_language,
            template_id=template_id,
            template_version=template_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'template_id={}'.format(template_id) in query_string
        assert 'template_version={}'.format(template_version) in query_string

    def test_list_policy_assignments_all_params_with_retries(self):
        # Enable retries and run test_list_policy_assignments_all_params.
        _service.enable_retries()
        self.test_list_policy_assignments_all_params()

        # Disable retries and run test_list_policy_assignments_all_params.
        _service.disable_retries()
        self.test_list_policy_assignments_all_params()

    @responses.activate
    def test_list_policy_assignments_required_params(self):
        """
        test_list_policy_assignments_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments')
        mock_response = '{"assignments": [{"template_id": "template_id", "template_version": "template_version", "assignment_id": "assignment_id", "target_type": "Account", "target": "target", "options": [{"subject_type": "iam_id", "subject_id": "subject_id", "root_requester_id": "root_requester_id", "root_template_id": "root_template_id", "root_template_version": "root_template_version"}], "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": "target", "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"trace": "trace", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}], "status_code": 11}}}], "status": "in_progress"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_policy_assignments(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_list_policy_assignments_required_params_with_retries(self):
        # Enable retries and run test_list_policy_assignments_required_params.
        _service.enable_retries()
        self.test_list_policy_assignments_required_params()

        # Disable retries and run test_list_policy_assignments_required_params.
        _service.disable_retries()
        self.test_list_policy_assignments_required_params()

    @responses.activate
    def test_list_policy_assignments_value_error(self):
        """
        test_list_policy_assignments_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments')
        mock_response = '{"assignments": [{"template_id": "template_id", "template_version": "template_version", "assignment_id": "assignment_id", "target_type": "Account", "target": "target", "options": [{"subject_type": "iam_id", "subject_id": "subject_id", "root_requester_id": "root_requester_id", "root_template_id": "root_template_id", "root_template_version": "root_template_version"}], "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": "target", "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"trace": "trace", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}], "status_code": 11}}}], "status": "in_progress"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_policy_assignments(**req_copy)

    def test_list_policy_assignments_value_error_with_retries(self):
        # Enable retries and run test_list_policy_assignments_value_error.
        _service.enable_retries()
        self.test_list_policy_assignments_value_error()

        # Disable retries and run test_list_policy_assignments_value_error.
        _service.disable_retries()
        self.test_list_policy_assignments_value_error()


class TestGetPolicyAssignment:
    """
    Test Class for get_policy_assignment
    """

    @responses.activate
    def test_get_policy_assignment_all_params(self):
        """
        get_policy_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments/testString')
        mock_response = '{"template_id": "template_id", "template_version": "template_version", "assignment_id": "assignment_id", "target_type": "Account", "target": "target", "options": [{"subject_type": "iam_id", "subject_id": "subject_id", "root_requester_id": "root_requester_id", "root_template_id": "root_template_id", "root_template_version": "root_template_version"}], "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": "target", "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"trace": "trace", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}], "status_code": 11}}}], "status": "in_progress"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'

        # Invoke method
        response = _service.get_policy_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_policy_assignment_all_params_with_retries(self):
        # Enable retries and run test_get_policy_assignment_all_params.
        _service.enable_retries()
        self.test_get_policy_assignment_all_params()

        # Disable retries and run test_get_policy_assignment_all_params.
        _service.disable_retries()
        self.test_get_policy_assignment_all_params()

    @responses.activate
    def test_get_policy_assignment_value_error(self):
        """
        test_get_policy_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments/testString')
        mock_response = '{"template_id": "template_id", "template_version": "template_version", "assignment_id": "assignment_id", "target_type": "Account", "target": "target", "options": [{"subject_type": "iam_id", "subject_id": "subject_id", "root_requester_id": "root_requester_id", "root_template_id": "root_template_id", "root_template_version": "root_template_version"}], "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": "target", "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"trace": "trace", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}], "status_code": 11}}}], "status": "in_progress"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assignment_id": assignment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_policy_assignment(**req_copy)

    def test_get_policy_assignment_value_error_with_retries(self):
        # Enable retries and run test_get_policy_assignment_value_error.
        _service.enable_retries()
        self.test_get_policy_assignment_value_error()

        # Disable retries and run test_get_policy_assignment_value_error.
        _service.disable_retries()
        self.test_get_policy_assignment_value_error()


# endregion
##############################################################################
# End of Service: PolicyAssignments
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AssignmentResourceCreated:
    """
    Test Class for AssignmentResourceCreated
    """

    def test_assignment_resource_created_serialization(self):
        """
        Test serialization/deserialization for AssignmentResourceCreated
        """

        # Construct a json representation of a AssignmentResourceCreated model
        assignment_resource_created_model_json = {}
        assignment_resource_created_model_json['id'] = 'testString'

        # Construct a model instance of AssignmentResourceCreated by calling from_dict on the json representation
        assignment_resource_created_model = AssignmentResourceCreated.from_dict(assignment_resource_created_model_json)
        assert assignment_resource_created_model != False

        # Construct a model instance of AssignmentResourceCreated by calling from_dict on the json representation
        assignment_resource_created_model_dict = AssignmentResourceCreated.from_dict(assignment_resource_created_model_json).__dict__
        assignment_resource_created_model2 = AssignmentResourceCreated(**assignment_resource_created_model_dict)

        # Verify the model instances are equivalent
        assert assignment_resource_created_model == assignment_resource_created_model2

        # Convert model instance back to dict and verify no loss of data
        assignment_resource_created_model_json2 = assignment_resource_created_model.to_dict()
        assert assignment_resource_created_model_json2 == assignment_resource_created_model_json


class TestModel_ConflictsWith:
    """
    Test Class for ConflictsWith
    """

    def test_conflicts_with_serialization(self):
        """
        Test serialization/deserialization for ConflictsWith
        """

        # Construct a json representation of a ConflictsWith model
        conflicts_with_model_json = {}
        conflicts_with_model_json['etag'] = 'testString'
        conflicts_with_model_json['role'] = 'testString'
        conflicts_with_model_json['policy'] = 'testString'

        # Construct a model instance of ConflictsWith by calling from_dict on the json representation
        conflicts_with_model = ConflictsWith.from_dict(conflicts_with_model_json)
        assert conflicts_with_model != False

        # Construct a model instance of ConflictsWith by calling from_dict on the json representation
        conflicts_with_model_dict = ConflictsWith.from_dict(conflicts_with_model_json).__dict__
        conflicts_with_model2 = ConflictsWith(**conflicts_with_model_dict)

        # Verify the model instances are equivalent
        assert conflicts_with_model == conflicts_with_model2

        # Convert model instance back to dict and verify no loss of data
        conflicts_with_model_json2 = conflicts_with_model.to_dict()
        assert conflicts_with_model_json2 == conflicts_with_model_json


class TestModel_Control:
    """
    Test Class for Control
    """

    def test_control_serialization(self):
        """
        Test serialization/deserialization for Control
        """

        # Construct dict forms of any model objects needed in order to build this model.

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        # Construct a json representation of a Control model
        control_model_json = {}
        control_model_json['grant'] = grant_model

        # Construct a model instance of Control by calling from_dict on the json representation
        control_model = Control.from_dict(control_model_json)
        assert control_model != False

        # Construct a model instance of Control by calling from_dict on the json representation
        control_model_dict = Control.from_dict(control_model_json).__dict__
        control_model2 = Control(**control_model_dict)

        # Verify the model instances are equivalent
        assert control_model == control_model2

        # Convert model instance back to dict and verify no loss of data
        control_model_json2 = control_model.to_dict()
        assert control_model_json2 == control_model_json


class TestModel_CustomRole:
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


class TestModel_EnrichedRoles:
    """
    Test Class for EnrichedRoles
    """

    def test_enriched_roles_serialization(self):
        """
        Test serialization/deserialization for EnrichedRoles
        """

        # Construct dict forms of any model objects needed in order to build this model.

        role_action_model = {}  # RoleAction
        role_action_model['id'] = 'testString'
        role_action_model['display_name'] = 'testString'
        role_action_model['description'] = 'testString'

        # Construct a json representation of a EnrichedRoles model
        enriched_roles_model_json = {}
        enriched_roles_model_json['role_id'] = 'testString'
        enriched_roles_model_json['actions'] = [role_action_model]

        # Construct a model instance of EnrichedRoles by calling from_dict on the json representation
        enriched_roles_model = EnrichedRoles.from_dict(enriched_roles_model_json)
        assert enriched_roles_model != False

        # Construct a model instance of EnrichedRoles by calling from_dict on the json representation
        enriched_roles_model_dict = EnrichedRoles.from_dict(enriched_roles_model_json).__dict__
        enriched_roles_model2 = EnrichedRoles(**enriched_roles_model_dict)

        # Verify the model instances are equivalent
        assert enriched_roles_model == enriched_roles_model2

        # Convert model instance back to dict and verify no loss of data
        enriched_roles_model_json2 = enriched_roles_model.to_dict()
        assert enriched_roles_model_json2 == enriched_roles_model_json


class TestModel_ErrorDetails:
    """
    Test Class for ErrorDetails
    """

    def test_error_details_serialization(self):
        """
        Test serialization/deserialization for ErrorDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        conflicts_with_model = {}  # ConflictsWith
        conflicts_with_model['etag'] = 'testString'
        conflicts_with_model['role'] = 'testString'
        conflicts_with_model['policy'] = 'testString'

        # Construct a json representation of a ErrorDetails model
        error_details_model_json = {}
        error_details_model_json['conflicts_with'] = conflicts_with_model

        # Construct a model instance of ErrorDetails by calling from_dict on the json representation
        error_details_model = ErrorDetails.from_dict(error_details_model_json)
        assert error_details_model != False

        # Construct a model instance of ErrorDetails by calling from_dict on the json representation
        error_details_model_dict = ErrorDetails.from_dict(error_details_model_json).__dict__
        error_details_model2 = ErrorDetails(**error_details_model_dict)

        # Verify the model instances are equivalent
        assert error_details_model == error_details_model2

        # Convert model instance back to dict and verify no loss of data
        error_details_model_json2 = error_details_model.to_dict()
        assert error_details_model_json2 == error_details_model_json


class TestModel_ErrorObject:
    """
    Test Class for ErrorObject
    """

    def test_error_object_serialization(self):
        """
        Test serialization/deserialization for ErrorObject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        conflicts_with_model = {}  # ConflictsWith
        conflicts_with_model['etag'] = 'testString'
        conflicts_with_model['role'] = 'testString'
        conflicts_with_model['policy'] = 'testString'

        error_details_model = {}  # ErrorDetails
        error_details_model['conflicts_with'] = conflicts_with_model

        # Construct a json representation of a ErrorObject model
        error_object_model_json = {}
        error_object_model_json['code'] = 'insufficent_permissions'
        error_object_model_json['message'] = 'testString'
        error_object_model_json['details'] = error_details_model
        error_object_model_json['more_info'] = 'testString'

        # Construct a model instance of ErrorObject by calling from_dict on the json representation
        error_object_model = ErrorObject.from_dict(error_object_model_json)
        assert error_object_model != False

        # Construct a model instance of ErrorObject by calling from_dict on the json representation
        error_object_model_dict = ErrorObject.from_dict(error_object_model_json).__dict__
        error_object_model2 = ErrorObject(**error_object_model_dict)

        # Verify the model instances are equivalent
        assert error_object_model == error_object_model2

        # Convert model instance back to dict and verify no loss of data
        error_object_model_json2 = error_object_model.to_dict()
        assert error_object_model_json2 == error_object_model_json


class TestModel_ErrorResponse:
    """
    Test Class for ErrorResponse
    """

    def test_error_response_serialization(self):
        """
        Test serialization/deserialization for ErrorResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        conflicts_with_model = {}  # ConflictsWith
        conflicts_with_model['etag'] = 'testString'
        conflicts_with_model['role'] = 'testString'
        conflicts_with_model['policy'] = 'testString'

        error_details_model = {}  # ErrorDetails
        error_details_model['conflicts_with'] = conflicts_with_model

        error_object_model = {}  # ErrorObject
        error_object_model['code'] = 'insufficent_permissions'
        error_object_model['message'] = 'testString'
        error_object_model['details'] = error_details_model
        error_object_model['more_info'] = 'testString'

        # Construct a json representation of a ErrorResponse model
        error_response_model_json = {}
        error_response_model_json['trace'] = 'testString'
        error_response_model_json['errors'] = [error_object_model]
        error_response_model_json['status_code'] = 38

        # Construct a model instance of ErrorResponse by calling from_dict on the json representation
        error_response_model = ErrorResponse.from_dict(error_response_model_json)
        assert error_response_model != False

        # Construct a model instance of ErrorResponse by calling from_dict on the json representation
        error_response_model_dict = ErrorResponse.from_dict(error_response_model_json).__dict__
        error_response_model2 = ErrorResponse(**error_response_model_dict)

        # Verify the model instances are equivalent
        assert error_response_model == error_response_model2

        # Convert model instance back to dict and verify no loss of data
        error_response_model_json2 = error_response_model.to_dict()
        assert error_response_model_json2 == error_response_model_json


class TestModel_Grant:
    """
    Test Class for Grant
    """

    def test_grant_serialization(self):
        """
        Test serialization/deserialization for Grant
        """

        # Construct dict forms of any model objects needed in order to build this model.

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        # Construct a json representation of a Grant model
        grant_model_json = {}
        grant_model_json['roles'] = [roles_model]

        # Construct a model instance of Grant by calling from_dict on the json representation
        grant_model = Grant.from_dict(grant_model_json)
        assert grant_model != False

        # Construct a model instance of Grant by calling from_dict on the json representation
        grant_model_dict = Grant.from_dict(grant_model_json).__dict__
        grant_model2 = Grant(**grant_model_dict)

        # Verify the model instances are equivalent
        assert grant_model == grant_model2

        # Convert model instance back to dict and verify no loss of data
        grant_model_json2 = grant_model.to_dict()
        assert grant_model_json2 == grant_model_json


class TestModel_GrantWithEnrichedRoles:
    """
    Test Class for GrantWithEnrichedRoles
    """

    def test_grant_with_enriched_roles_serialization(self):
        """
        Test serialization/deserialization for GrantWithEnrichedRoles
        """

        # Construct dict forms of any model objects needed in order to build this model.

        role_action_model = {}  # RoleAction
        role_action_model['id'] = 'testString'
        role_action_model['display_name'] = 'testString'
        role_action_model['description'] = 'testString'

        enriched_roles_model = {}  # EnrichedRoles
        enriched_roles_model['role_id'] = 'testString'
        enriched_roles_model['actions'] = [role_action_model]

        # Construct a json representation of a GrantWithEnrichedRoles model
        grant_with_enriched_roles_model_json = {}
        grant_with_enriched_roles_model_json['roles'] = [enriched_roles_model]

        # Construct a model instance of GrantWithEnrichedRoles by calling from_dict on the json representation
        grant_with_enriched_roles_model = GrantWithEnrichedRoles.from_dict(grant_with_enriched_roles_model_json)
        assert grant_with_enriched_roles_model != False

        # Construct a model instance of GrantWithEnrichedRoles by calling from_dict on the json representation
        grant_with_enriched_roles_model_dict = GrantWithEnrichedRoles.from_dict(grant_with_enriched_roles_model_json).__dict__
        grant_with_enriched_roles_model2 = GrantWithEnrichedRoles(**grant_with_enriched_roles_model_dict)

        # Verify the model instances are equivalent
        assert grant_with_enriched_roles_model == grant_with_enriched_roles_model2

        # Convert model instance back to dict and verify no loss of data
        grant_with_enriched_roles_model_json2 = grant_with_enriched_roles_model.to_dict()
        assert grant_with_enriched_roles_model_json2 == grant_with_enriched_roles_model_json


class TestModel_LimitData:
    """
    Test Class for LimitData
    """

    def test_limit_data_serialization(self):
        """
        Test serialization/deserialization for LimitData
        """

        # Construct a json representation of a LimitData model
        limit_data_model_json = {}

        # Construct a model instance of LimitData by calling from_dict on the json representation
        limit_data_model = LimitData.from_dict(limit_data_model_json)
        assert limit_data_model != False

        # Construct a model instance of LimitData by calling from_dict on the json representation
        limit_data_model_dict = LimitData.from_dict(limit_data_model_json).__dict__
        limit_data_model2 = LimitData(**limit_data_model_dict)

        # Verify the model instances are equivalent
        assert limit_data_model == limit_data_model2

        # Convert model instance back to dict and verify no loss of data
        limit_data_model_json2 = limit_data_model.to_dict()
        assert limit_data_model_json2 == limit_data_model_json


class TestModel_Policy:
    """
    Test Class for Policy
    """

    def test_policy_serialization(self):
        """
        Test serialization/deserialization for Policy
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subject_attribute_model = {}  # SubjectAttribute
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        policy_subject_model = {}  # PolicySubject
        policy_subject_model['attributes'] = [subject_attribute_model]

        policy_role_model = {}  # PolicyRole
        policy_role_model['role_id'] = 'testString'

        resource_attribute_model = {}  # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_model = {}  # ResourceTag
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        policy_resource_model = {}  # PolicyResource
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


class TestModel_PolicyAssignment:
    """
    Test Class for PolicyAssignment
    """

    def test_policy_assignment_serialization(self):
        """
        Test serialization/deserialization for PolicyAssignment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_assignment_options_model = {}  # PolicyAssignmentOptions
        policy_assignment_options_model['subject_type'] = 'iam_id'
        policy_assignment_options_model['subject_id'] = 'testString'
        policy_assignment_options_model['root_requester_id'] = 'testString'
        policy_assignment_options_model['root_template_id'] = 'testString'
        policy_assignment_options_model['root_template_version'] = 'testString'

        assignment_resource_created_model = {}  # AssignmentResourceCreated
        assignment_resource_created_model['id'] = 'testString'

        conflicts_with_model = {}  # ConflictsWith
        conflicts_with_model['etag'] = 'testString'
        conflicts_with_model['role'] = 'testString'
        conflicts_with_model['policy'] = 'testString'

        error_details_model = {}  # ErrorDetails
        error_details_model['conflicts_with'] = conflicts_with_model

        error_object_model = {}  # ErrorObject
        error_object_model['code'] = 'insufficent_permissions'
        error_object_model['message'] = 'testString'
        error_object_model['details'] = error_details_model
        error_object_model['more_info'] = 'testString'

        error_response_model = {}  # ErrorResponse
        error_response_model['trace'] = 'testString'
        error_response_model['errors'] = [error_object_model]
        error_response_model['status_code'] = 38

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = error_response_model

        policy_assignment_resources_model = {}  # PolicyAssignmentResources
        policy_assignment_resources_model['target'] = 'testString'
        policy_assignment_resources_model['policy'] = policy_assignment_resource_policy_model

        # Construct a json representation of a PolicyAssignment model
        policy_assignment_model_json = {}
        policy_assignment_model_json['template_id'] = 'testString'
        policy_assignment_model_json['template_version'] = 'testString'
        policy_assignment_model_json['assignment_id'] = 'testString'
        policy_assignment_model_json['target_type'] = 'Account'
        policy_assignment_model_json['target'] = 'testString'
        policy_assignment_model_json['options'] = [policy_assignment_options_model]
        policy_assignment_model_json['resources'] = [policy_assignment_resources_model]
        policy_assignment_model_json['status'] = 'in_progress'

        # Construct a model instance of PolicyAssignment by calling from_dict on the json representation
        policy_assignment_model = PolicyAssignment.from_dict(policy_assignment_model_json)
        assert policy_assignment_model != False

        # Construct a model instance of PolicyAssignment by calling from_dict on the json representation
        policy_assignment_model_dict = PolicyAssignment.from_dict(policy_assignment_model_json).__dict__
        policy_assignment_model2 = PolicyAssignment(**policy_assignment_model_dict)

        # Verify the model instances are equivalent
        assert policy_assignment_model == policy_assignment_model2

        # Convert model instance back to dict and verify no loss of data
        policy_assignment_model_json2 = policy_assignment_model.to_dict()
        assert policy_assignment_model_json2 == policy_assignment_model_json


class TestModel_PolicyAssignmentOptions:
    """
    Test Class for PolicyAssignmentOptions
    """

    def test_policy_assignment_options_serialization(self):
        """
        Test serialization/deserialization for PolicyAssignmentOptions
        """

        # Construct a json representation of a PolicyAssignmentOptions model
        policy_assignment_options_model_json = {}
        policy_assignment_options_model_json['subject_type'] = 'iam_id'
        policy_assignment_options_model_json['subject_id'] = 'testString'
        policy_assignment_options_model_json['root_requester_id'] = 'testString'
        policy_assignment_options_model_json['root_template_id'] = 'testString'
        policy_assignment_options_model_json['root_template_version'] = 'testString'

        # Construct a model instance of PolicyAssignmentOptions by calling from_dict on the json representation
        policy_assignment_options_model = PolicyAssignmentOptions.from_dict(policy_assignment_options_model_json)
        assert policy_assignment_options_model != False

        # Construct a model instance of PolicyAssignmentOptions by calling from_dict on the json representation
        policy_assignment_options_model_dict = PolicyAssignmentOptions.from_dict(policy_assignment_options_model_json).__dict__
        policy_assignment_options_model2 = PolicyAssignmentOptions(**policy_assignment_options_model_dict)

        # Verify the model instances are equivalent
        assert policy_assignment_options_model == policy_assignment_options_model2

        # Convert model instance back to dict and verify no loss of data
        policy_assignment_options_model_json2 = policy_assignment_options_model.to_dict()
        assert policy_assignment_options_model_json2 == policy_assignment_options_model_json


class TestModel_PolicyAssignmentResourcePolicy:
    """
    Test Class for PolicyAssignmentResourcePolicy
    """

    def test_policy_assignment_resource_policy_serialization(self):
        """
        Test serialization/deserialization for PolicyAssignmentResourcePolicy
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_resource_created_model = {}  # AssignmentResourceCreated
        assignment_resource_created_model['id'] = 'testString'

        conflicts_with_model = {}  # ConflictsWith
        conflicts_with_model['etag'] = 'testString'
        conflicts_with_model['role'] = 'testString'
        conflicts_with_model['policy'] = 'testString'

        error_details_model = {}  # ErrorDetails
        error_details_model['conflicts_with'] = conflicts_with_model

        error_object_model = {}  # ErrorObject
        error_object_model['code'] = 'insufficent_permissions'
        error_object_model['message'] = 'testString'
        error_object_model['details'] = error_details_model
        error_object_model['more_info'] = 'testString'

        error_response_model = {}  # ErrorResponse
        error_response_model['trace'] = 'testString'
        error_response_model['errors'] = [error_object_model]
        error_response_model['status_code'] = 38

        # Construct a json representation of a PolicyAssignmentResourcePolicy model
        policy_assignment_resource_policy_model_json = {}
        policy_assignment_resource_policy_model_json['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model_json['status'] = 'testString'
        policy_assignment_resource_policy_model_json['error_message'] = error_response_model

        # Construct a model instance of PolicyAssignmentResourcePolicy by calling from_dict on the json representation
        policy_assignment_resource_policy_model = PolicyAssignmentResourcePolicy.from_dict(policy_assignment_resource_policy_model_json)
        assert policy_assignment_resource_policy_model != False

        # Construct a model instance of PolicyAssignmentResourcePolicy by calling from_dict on the json representation
        policy_assignment_resource_policy_model_dict = PolicyAssignmentResourcePolicy.from_dict(policy_assignment_resource_policy_model_json).__dict__
        policy_assignment_resource_policy_model2 = PolicyAssignmentResourcePolicy(**policy_assignment_resource_policy_model_dict)

        # Verify the model instances are equivalent
        assert policy_assignment_resource_policy_model == policy_assignment_resource_policy_model2

        # Convert model instance back to dict and verify no loss of data
        policy_assignment_resource_policy_model_json2 = policy_assignment_resource_policy_model.to_dict()
        assert policy_assignment_resource_policy_model_json2 == policy_assignment_resource_policy_model_json


class TestModel_PolicyAssignmentResources:
    """
    Test Class for PolicyAssignmentResources
    """

    def test_policy_assignment_resources_serialization(self):
        """
        Test serialization/deserialization for PolicyAssignmentResources
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_resource_created_model = {}  # AssignmentResourceCreated
        assignment_resource_created_model['id'] = 'testString'

        conflicts_with_model = {}  # ConflictsWith
        conflicts_with_model['etag'] = 'testString'
        conflicts_with_model['role'] = 'testString'
        conflicts_with_model['policy'] = 'testString'

        error_details_model = {}  # ErrorDetails
        error_details_model['conflicts_with'] = conflicts_with_model

        error_object_model = {}  # ErrorObject
        error_object_model['code'] = 'insufficent_permissions'
        error_object_model['message'] = 'testString'
        error_object_model['details'] = error_details_model
        error_object_model['more_info'] = 'testString'

        error_response_model = {}  # ErrorResponse
        error_response_model['trace'] = 'testString'
        error_response_model['errors'] = [error_object_model]
        error_response_model['status_code'] = 38

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = error_response_model

        # Construct a json representation of a PolicyAssignmentResources model
        policy_assignment_resources_model_json = {}
        policy_assignment_resources_model_json['target'] = 'testString'
        policy_assignment_resources_model_json['policy'] = policy_assignment_resource_policy_model

        # Construct a model instance of PolicyAssignmentResources by calling from_dict on the json representation
        policy_assignment_resources_model = PolicyAssignmentResources.from_dict(policy_assignment_resources_model_json)
        assert policy_assignment_resources_model != False

        # Construct a model instance of PolicyAssignmentResources by calling from_dict on the json representation
        policy_assignment_resources_model_dict = PolicyAssignmentResources.from_dict(policy_assignment_resources_model_json).__dict__
        policy_assignment_resources_model2 = PolicyAssignmentResources(**policy_assignment_resources_model_dict)

        # Verify the model instances are equivalent
        assert policy_assignment_resources_model == policy_assignment_resources_model2

        # Convert model instance back to dict and verify no loss of data
        policy_assignment_resources_model_json2 = policy_assignment_resources_model.to_dict()
        assert policy_assignment_resources_model_json2 == policy_assignment_resources_model_json


class TestModel_PolicyCollection:
    """
    Test Class for PolicyCollection
    """

    def test_policy_collection_serialization(self):
        """
        Test serialization/deserialization for PolicyCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subject_attribute_model = {}  # SubjectAttribute
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        policy_subject_model = {}  # PolicySubject
        policy_subject_model['attributes'] = [subject_attribute_model]

        policy_role_model = {}  # PolicyRole
        policy_role_model['role_id'] = 'testString'

        resource_attribute_model = {}  # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_model = {}  # ResourceTag
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        policy_resource_model = {}  # PolicyResource
        policy_resource_model['attributes'] = [resource_attribute_model]
        policy_resource_model['tags'] = [resource_tag_model]

        template_metadata_model = {}  # TemplateMetadata
        template_metadata_model['id'] = 'testString'
        template_metadata_model['version'] = 'testString'
        template_metadata_model['assignment_id'] = 'testString'
        template_metadata_model['root_id'] = 'testString'
        template_metadata_model['root_version'] = 'testString'

        policy_template_meta_data_model = {}  # PolicyTemplateMetaData
        policy_template_meta_data_model['type'] = 'testString'
        policy_template_meta_data_model['description'] = 'testString'
        policy_template_meta_data_model['subjects'] = [policy_subject_model]
        policy_template_meta_data_model['roles'] = [policy_role_model]
        policy_template_meta_data_model['resources'] = [policy_resource_model]
        policy_template_meta_data_model['state'] = 'active'
        policy_template_meta_data_model['template'] = template_metadata_model

        # Construct a json representation of a PolicyCollection model
        policy_collection_model_json = {}
        policy_collection_model_json['policies'] = [policy_template_meta_data_model]

        # Construct a model instance of PolicyCollection by calling from_dict on the json representation
        policy_collection_model = PolicyCollection.from_dict(policy_collection_model_json)
        assert policy_collection_model != False

        # Construct a model instance of PolicyCollection by calling from_dict on the json representation
        policy_collection_model_dict = PolicyCollection.from_dict(policy_collection_model_json).__dict__
        policy_collection_model2 = PolicyCollection(**policy_collection_model_dict)

        # Verify the model instances are equivalent
        assert policy_collection_model == policy_collection_model2

        # Convert model instance back to dict and verify no loss of data
        policy_collection_model_json2 = policy_collection_model.to_dict()
        assert policy_collection_model_json2 == policy_collection_model_json


class TestModel_PolicyResource:
    """
    Test Class for PolicyResource
    """

    def test_policy_resource_serialization(self):
        """
        Test serialization/deserialization for PolicyResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_attribute_model = {}  # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_model = {}  # ResourceTag
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


class TestModel_PolicyRole:
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


class TestModel_PolicySubject:
    """
    Test Class for PolicySubject
    """

    def test_policy_subject_serialization(self):
        """
        Test serialization/deserialization for PolicySubject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subject_attribute_model = {}  # SubjectAttribute
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


class TestModel_PolicyTemplate:
    """
    Test Class for PolicyTemplate
    """

    def test_policy_template_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_resource_attribute_model = {}  # V2PolicyResourceAttribute
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        v2_policy_resource_tag_model = {}  # V2PolicyResourceTag
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        v2_policy_resource_model = {}  # V2PolicyResource
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        control_model = {}  # Control
        control_model['grant'] = grant_model

        template_policy_model = {}  # TemplatePolicy
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        # Construct a json representation of a PolicyTemplate model
        policy_template_model_json = {}
        policy_template_model_json['name'] = 'testString'
        policy_template_model_json['description'] = 'testString'
        policy_template_model_json['account_id'] = 'testString'
        policy_template_model_json['version'] = 'testString'
        policy_template_model_json['committed'] = True
        policy_template_model_json['policy'] = template_policy_model
        policy_template_model_json['state'] = 'active'

        # Construct a model instance of PolicyTemplate by calling from_dict on the json representation
        policy_template_model = PolicyTemplate.from_dict(policy_template_model_json)
        assert policy_template_model != False

        # Construct a model instance of PolicyTemplate by calling from_dict on the json representation
        policy_template_model_dict = PolicyTemplate.from_dict(policy_template_model_json).__dict__
        policy_template_model2 = PolicyTemplate(**policy_template_model_dict)

        # Verify the model instances are equivalent
        assert policy_template_model == policy_template_model2

        # Convert model instance back to dict and verify no loss of data
        policy_template_model_json2 = policy_template_model.to_dict()
        assert policy_template_model_json2 == policy_template_model_json


class TestModel_PolicyTemplateAssignmentCollection:
    """
    Test Class for PolicyTemplateAssignmentCollection
    """

    def test_policy_template_assignment_collection_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplateAssignmentCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_assignment_options_model = {}  # PolicyAssignmentOptions
        policy_assignment_options_model['subject_type'] = 'iam_id'
        policy_assignment_options_model['subject_id'] = 'testString'
        policy_assignment_options_model['root_requester_id'] = 'testString'
        policy_assignment_options_model['root_template_id'] = 'testString'
        policy_assignment_options_model['root_template_version'] = 'testString'

        assignment_resource_created_model = {}  # AssignmentResourceCreated
        assignment_resource_created_model['id'] = 'testString'

        conflicts_with_model = {}  # ConflictsWith
        conflicts_with_model['etag'] = 'testString'
        conflicts_with_model['role'] = 'testString'
        conflicts_with_model['policy'] = 'testString'

        error_details_model = {}  # ErrorDetails
        error_details_model['conflicts_with'] = conflicts_with_model

        error_object_model = {}  # ErrorObject
        error_object_model['code'] = 'insufficent_permissions'
        error_object_model['message'] = 'testString'
        error_object_model['details'] = error_details_model
        error_object_model['more_info'] = 'testString'

        error_response_model = {}  # ErrorResponse
        error_response_model['trace'] = 'testString'
        error_response_model['errors'] = [error_object_model]
        error_response_model['status_code'] = 38

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = error_response_model

        policy_assignment_resources_model = {}  # PolicyAssignmentResources
        policy_assignment_resources_model['target'] = 'testString'
        policy_assignment_resources_model['policy'] = policy_assignment_resource_policy_model

        policy_assignment_model = {}  # PolicyAssignment
        policy_assignment_model['template_id'] = 'testString'
        policy_assignment_model['template_version'] = 'testString'
        policy_assignment_model['assignment_id'] = 'testString'
        policy_assignment_model['target_type'] = 'Account'
        policy_assignment_model['target'] = 'testString'
        policy_assignment_model['options'] = [policy_assignment_options_model]
        policy_assignment_model['resources'] = [policy_assignment_resources_model]
        policy_assignment_model['status'] = 'in_progress'

        # Construct a json representation of a PolicyTemplateAssignmentCollection model
        policy_template_assignment_collection_model_json = {}
        policy_template_assignment_collection_model_json['assignments'] = [policy_assignment_model]

        # Construct a model instance of PolicyTemplateAssignmentCollection by calling from_dict on the json representation
        policy_template_assignment_collection_model = PolicyTemplateAssignmentCollection.from_dict(policy_template_assignment_collection_model_json)
        assert policy_template_assignment_collection_model != False

        # Construct a model instance of PolicyTemplateAssignmentCollection by calling from_dict on the json representation
        policy_template_assignment_collection_model_dict = PolicyTemplateAssignmentCollection.from_dict(policy_template_assignment_collection_model_json).__dict__
        policy_template_assignment_collection_model2 = PolicyTemplateAssignmentCollection(**policy_template_assignment_collection_model_dict)

        # Verify the model instances are equivalent
        assert policy_template_assignment_collection_model == policy_template_assignment_collection_model2

        # Convert model instance back to dict and verify no loss of data
        policy_template_assignment_collection_model_json2 = policy_template_assignment_collection_model.to_dict()
        assert policy_template_assignment_collection_model_json2 == policy_template_assignment_collection_model_json


class TestModel_PolicyTemplateCollection:
    """
    Test Class for PolicyTemplateCollection
    """

    def test_policy_template_collection_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplateCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_resource_attribute_model = {}  # V2PolicyResourceAttribute
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        v2_policy_resource_tag_model = {}  # V2PolicyResourceTag
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        v2_policy_resource_model = {}  # V2PolicyResource
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        control_model = {}  # Control
        control_model['grant'] = grant_model

        template_policy_model = {}  # TemplatePolicy
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        policy_template_model = {}  # PolicyTemplate
        policy_template_model['name'] = 'testString'
        policy_template_model['description'] = 'testString'
        policy_template_model['account_id'] = 'testString'
        policy_template_model['version'] = 'testString'
        policy_template_model['committed'] = True
        policy_template_model['policy'] = template_policy_model
        policy_template_model['state'] = 'active'

        # Construct a json representation of a PolicyTemplateCollection model
        policy_template_collection_model_json = {}
        policy_template_collection_model_json['policy_templates'] = [policy_template_model]

        # Construct a model instance of PolicyTemplateCollection by calling from_dict on the json representation
        policy_template_collection_model = PolicyTemplateCollection.from_dict(policy_template_collection_model_json)
        assert policy_template_collection_model != False

        # Construct a model instance of PolicyTemplateCollection by calling from_dict on the json representation
        policy_template_collection_model_dict = PolicyTemplateCollection.from_dict(policy_template_collection_model_json).__dict__
        policy_template_collection_model2 = PolicyTemplateCollection(**policy_template_collection_model_dict)

        # Verify the model instances are equivalent
        assert policy_template_collection_model == policy_template_collection_model2

        # Convert model instance back to dict and verify no loss of data
        policy_template_collection_model_json2 = policy_template_collection_model.to_dict()
        assert policy_template_collection_model_json2 == policy_template_collection_model_json


class TestModel_PolicyTemplateLimitData:
    """
    Test Class for PolicyTemplateLimitData
    """

    def test_policy_template_limit_data_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplateLimitData
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_resource_attribute_model = {}  # V2PolicyResourceAttribute
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        v2_policy_resource_tag_model = {}  # V2PolicyResourceTag
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        v2_policy_resource_model = {}  # V2PolicyResource
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        control_model = {}  # Control
        control_model['grant'] = grant_model

        template_policy_model = {}  # TemplatePolicy
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        limit_data_model = {}  # LimitData

        template_count_data_model = {}  # TemplateCountData
        template_count_data_model['template'] = limit_data_model
        template_count_data_model['version'] = limit_data_model

        # Construct a json representation of a PolicyTemplateLimitData model
        policy_template_limit_data_model_json = {}
        policy_template_limit_data_model_json['name'] = 'testString'
        policy_template_limit_data_model_json['description'] = 'testString'
        policy_template_limit_data_model_json['account_id'] = 'testString'
        policy_template_limit_data_model_json['version'] = 'testString'
        policy_template_limit_data_model_json['committed'] = True
        policy_template_limit_data_model_json['policy'] = template_policy_model
        policy_template_limit_data_model_json['state'] = 'active'
        policy_template_limit_data_model_json['counts'] = template_count_data_model

        # Construct a model instance of PolicyTemplateLimitData by calling from_dict on the json representation
        policy_template_limit_data_model = PolicyTemplateLimitData.from_dict(policy_template_limit_data_model_json)
        assert policy_template_limit_data_model != False

        # Construct a model instance of PolicyTemplateLimitData by calling from_dict on the json representation
        policy_template_limit_data_model_dict = PolicyTemplateLimitData.from_dict(policy_template_limit_data_model_json).__dict__
        policy_template_limit_data_model2 = PolicyTemplateLimitData(**policy_template_limit_data_model_dict)

        # Verify the model instances are equivalent
        assert policy_template_limit_data_model == policy_template_limit_data_model2

        # Convert model instance back to dict and verify no loss of data
        policy_template_limit_data_model_json2 = policy_template_limit_data_model.to_dict()
        assert policy_template_limit_data_model_json2 == policy_template_limit_data_model_json


class TestModel_PolicyTemplateMetaData:
    """
    Test Class for PolicyTemplateMetaData
    """

    def test_policy_template_meta_data_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplateMetaData
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subject_attribute_model = {}  # SubjectAttribute
        subject_attribute_model['name'] = 'testString'
        subject_attribute_model['value'] = 'testString'

        policy_subject_model = {}  # PolicySubject
        policy_subject_model['attributes'] = [subject_attribute_model]

        policy_role_model = {}  # PolicyRole
        policy_role_model['role_id'] = 'testString'

        resource_attribute_model = {}  # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_model = {}  # ResourceTag
        resource_tag_model['name'] = 'testString'
        resource_tag_model['value'] = 'testString'
        resource_tag_model['operator'] = 'testString'

        policy_resource_model = {}  # PolicyResource
        policy_resource_model['attributes'] = [resource_attribute_model]
        policy_resource_model['tags'] = [resource_tag_model]

        template_metadata_model = {}  # TemplateMetadata
        template_metadata_model['id'] = 'testString'
        template_metadata_model['version'] = 'testString'
        template_metadata_model['assignment_id'] = 'testString'
        template_metadata_model['root_id'] = 'testString'
        template_metadata_model['root_version'] = 'testString'

        # Construct a json representation of a PolicyTemplateMetaData model
        policy_template_meta_data_model_json = {}
        policy_template_meta_data_model_json['type'] = 'testString'
        policy_template_meta_data_model_json['description'] = 'testString'
        policy_template_meta_data_model_json['subjects'] = [policy_subject_model]
        policy_template_meta_data_model_json['roles'] = [policy_role_model]
        policy_template_meta_data_model_json['resources'] = [policy_resource_model]
        policy_template_meta_data_model_json['state'] = 'active'
        policy_template_meta_data_model_json['template'] = template_metadata_model

        # Construct a model instance of PolicyTemplateMetaData by calling from_dict on the json representation
        policy_template_meta_data_model = PolicyTemplateMetaData.from_dict(policy_template_meta_data_model_json)
        assert policy_template_meta_data_model != False

        # Construct a model instance of PolicyTemplateMetaData by calling from_dict on the json representation
        policy_template_meta_data_model_dict = PolicyTemplateMetaData.from_dict(policy_template_meta_data_model_json).__dict__
        policy_template_meta_data_model2 = PolicyTemplateMetaData(**policy_template_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert policy_template_meta_data_model == policy_template_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        policy_template_meta_data_model_json2 = policy_template_meta_data_model.to_dict()
        assert policy_template_meta_data_model_json2 == policy_template_meta_data_model_json


class TestModel_PolicyTemplateVersionsCollection:
    """
    Test Class for PolicyTemplateVersionsCollection
    """

    def test_policy_template_versions_collection_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplateVersionsCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_resource_attribute_model = {}  # V2PolicyResourceAttribute
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        v2_policy_resource_tag_model = {}  # V2PolicyResourceTag
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        v2_policy_resource_model = {}  # V2PolicyResource
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        control_model = {}  # Control
        control_model['grant'] = grant_model

        template_policy_model = {}  # TemplatePolicy
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = control_model

        policy_template_model = {}  # PolicyTemplate
        policy_template_model['name'] = 'testString'
        policy_template_model['description'] = 'testString'
        policy_template_model['account_id'] = 'testString'
        policy_template_model['version'] = 'testString'
        policy_template_model['committed'] = True
        policy_template_model['policy'] = template_policy_model
        policy_template_model['state'] = 'active'

        # Construct a json representation of a PolicyTemplateVersionsCollection model
        policy_template_versions_collection_model_json = {}
        policy_template_versions_collection_model_json['versions'] = [policy_template_model]

        # Construct a model instance of PolicyTemplateVersionsCollection by calling from_dict on the json representation
        policy_template_versions_collection_model = PolicyTemplateVersionsCollection.from_dict(policy_template_versions_collection_model_json)
        assert policy_template_versions_collection_model != False

        # Construct a model instance of PolicyTemplateVersionsCollection by calling from_dict on the json representation
        policy_template_versions_collection_model_dict = PolicyTemplateVersionsCollection.from_dict(policy_template_versions_collection_model_json).__dict__
        policy_template_versions_collection_model2 = PolicyTemplateVersionsCollection(**policy_template_versions_collection_model_dict)

        # Verify the model instances are equivalent
        assert policy_template_versions_collection_model == policy_template_versions_collection_model2

        # Convert model instance back to dict and verify no loss of data
        policy_template_versions_collection_model_json2 = policy_template_versions_collection_model.to_dict()
        assert policy_template_versions_collection_model_json2 == policy_template_versions_collection_model_json


class TestModel_ResourceAttribute:
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


class TestModel_ResourceTag:
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


class TestModel_Role:
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


class TestModel_RoleAction:
    """
    Test Class for RoleAction
    """

    def test_role_action_serialization(self):
        """
        Test serialization/deserialization for RoleAction
        """

        # Construct a json representation of a RoleAction model
        role_action_model_json = {}
        role_action_model_json['id'] = 'testString'
        role_action_model_json['display_name'] = 'testString'
        role_action_model_json['description'] = 'testString'

        # Construct a model instance of RoleAction by calling from_dict on the json representation
        role_action_model = RoleAction.from_dict(role_action_model_json)
        assert role_action_model != False

        # Construct a model instance of RoleAction by calling from_dict on the json representation
        role_action_model_dict = RoleAction.from_dict(role_action_model_json).__dict__
        role_action_model2 = RoleAction(**role_action_model_dict)

        # Verify the model instances are equivalent
        assert role_action_model == role_action_model2

        # Convert model instance back to dict and verify no loss of data
        role_action_model_json2 = role_action_model.to_dict()
        assert role_action_model_json2 == role_action_model_json


class TestModel_RoleCollection:
    """
    Test Class for RoleCollection
    """

    def test_role_collection_serialization(self):
        """
        Test serialization/deserialization for RoleCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        custom_role_model = {}  # CustomRole
        custom_role_model['display_name'] = 'testString'
        custom_role_model['description'] = 'testString'
        custom_role_model['actions'] = ['testString']
        custom_role_model['name'] = 'Developer'
        custom_role_model['account_id'] = 'testString'
        custom_role_model['service_name'] = 'iam-groups'

        role_model = {}  # Role
        role_model['display_name'] = 'testString'
        role_model['description'] = 'testString'
        role_model['actions'] = ['testString']

        # Construct a json representation of a RoleCollection model
        role_collection_model_json = {}
        role_collection_model_json['custom_roles'] = [custom_role_model]
        role_collection_model_json['service_roles'] = [role_model]
        role_collection_model_json['system_roles'] = [role_model]

        # Construct a model instance of RoleCollection by calling from_dict on the json representation
        role_collection_model = RoleCollection.from_dict(role_collection_model_json)
        assert role_collection_model != False

        # Construct a model instance of RoleCollection by calling from_dict on the json representation
        role_collection_model_dict = RoleCollection.from_dict(role_collection_model_json).__dict__
        role_collection_model2 = RoleCollection(**role_collection_model_dict)

        # Verify the model instances are equivalent
        assert role_collection_model == role_collection_model2

        # Convert model instance back to dict and verify no loss of data
        role_collection_model_json2 = role_collection_model.to_dict()
        assert role_collection_model_json2 == role_collection_model_json


class TestModel_Roles:
    """
    Test Class for Roles
    """

    def test_roles_serialization(self):
        """
        Test serialization/deserialization for Roles
        """

        # Construct a json representation of a Roles model
        roles_model_json = {}
        roles_model_json['role_id'] = 'testString'

        # Construct a model instance of Roles by calling from_dict on the json representation
        roles_model = Roles.from_dict(roles_model_json)
        assert roles_model != False

        # Construct a model instance of Roles by calling from_dict on the json representation
        roles_model_dict = Roles.from_dict(roles_model_json).__dict__
        roles_model2 = Roles(**roles_model_dict)

        # Verify the model instances are equivalent
        assert roles_model == roles_model2

        # Convert model instance back to dict and verify no loss of data
        roles_model_json2 = roles_model.to_dict()
        assert roles_model_json2 == roles_model_json


class TestModel_RuleAttribute:
    """
    Test Class for RuleAttribute
    """

    def test_rule_attribute_serialization(self):
        """
        Test serialization/deserialization for RuleAttribute
        """

        # Construct a json representation of a RuleAttribute model
        rule_attribute_model_json = {}
        rule_attribute_model_json['key'] = 'testString'
        rule_attribute_model_json['operator'] = 'stringEquals'
        rule_attribute_model_json['value'] = 'testString'

        # Construct a model instance of RuleAttribute by calling from_dict on the json representation
        rule_attribute_model = RuleAttribute.from_dict(rule_attribute_model_json)
        assert rule_attribute_model != False

        # Construct a model instance of RuleAttribute by calling from_dict on the json representation
        rule_attribute_model_dict = RuleAttribute.from_dict(rule_attribute_model_json).__dict__
        rule_attribute_model2 = RuleAttribute(**rule_attribute_model_dict)

        # Verify the model instances are equivalent
        assert rule_attribute_model == rule_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        rule_attribute_model_json2 = rule_attribute_model.to_dict()
        assert rule_attribute_model_json2 == rule_attribute_model_json


class TestModel_SubjectAttribute:
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


class TestModel_TemplateCountData:
    """
    Test Class for TemplateCountData
    """

    def test_template_count_data_serialization(self):
        """
        Test serialization/deserialization for TemplateCountData
        """

        # Construct dict forms of any model objects needed in order to build this model.

        limit_data_model = {}  # LimitData

        # Construct a json representation of a TemplateCountData model
        template_count_data_model_json = {}
        template_count_data_model_json['template'] = limit_data_model
        template_count_data_model_json['version'] = limit_data_model

        # Construct a model instance of TemplateCountData by calling from_dict on the json representation
        template_count_data_model = TemplateCountData.from_dict(template_count_data_model_json)
        assert template_count_data_model != False

        # Construct a model instance of TemplateCountData by calling from_dict on the json representation
        template_count_data_model_dict = TemplateCountData.from_dict(template_count_data_model_json).__dict__
        template_count_data_model2 = TemplateCountData(**template_count_data_model_dict)

        # Verify the model instances are equivalent
        assert template_count_data_model == template_count_data_model2

        # Convert model instance back to dict and verify no loss of data
        template_count_data_model_json2 = template_count_data_model.to_dict()
        assert template_count_data_model_json2 == template_count_data_model_json


class TestModel_TemplateMetadata:
    """
    Test Class for TemplateMetadata
    """

    def test_template_metadata_serialization(self):
        """
        Test serialization/deserialization for TemplateMetadata
        """

        # Construct a json representation of a TemplateMetadata model
        template_metadata_model_json = {}
        template_metadata_model_json['id'] = 'testString'
        template_metadata_model_json['version'] = 'testString'
        template_metadata_model_json['assignment_id'] = 'testString'
        template_metadata_model_json['root_id'] = 'testString'
        template_metadata_model_json['root_version'] = 'testString'

        # Construct a model instance of TemplateMetadata by calling from_dict on the json representation
        template_metadata_model = TemplateMetadata.from_dict(template_metadata_model_json)
        assert template_metadata_model != False

        # Construct a model instance of TemplateMetadata by calling from_dict on the json representation
        template_metadata_model_dict = TemplateMetadata.from_dict(template_metadata_model_json).__dict__
        template_metadata_model2 = TemplateMetadata(**template_metadata_model_dict)

        # Verify the model instances are equivalent
        assert template_metadata_model == template_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        template_metadata_model_json2 = template_metadata_model.to_dict()
        assert template_metadata_model_json2 == template_metadata_model_json


class TestModel_TemplatePolicy:
    """
    Test Class for TemplatePolicy
    """

    def test_template_policy_serialization(self):
        """
        Test serialization/deserialization for TemplatePolicy
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_resource_attribute_model = {}  # V2PolicyResourceAttribute
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        v2_policy_resource_tag_model = {}  # V2PolicyResourceTag
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        v2_policy_resource_model = {}  # V2PolicyResource
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        control_model = {}  # Control
        control_model['grant'] = grant_model

        # Construct a json representation of a TemplatePolicy model
        template_policy_model_json = {}
        template_policy_model_json['type'] = 'access'
        template_policy_model_json['description'] = 'testString'
        template_policy_model_json['resource'] = v2_policy_resource_model
        template_policy_model_json['pattern'] = 'testString'
        template_policy_model_json['rule'] = v2_policy_rule_model
        template_policy_model_json['control'] = control_model

        # Construct a model instance of TemplatePolicy by calling from_dict on the json representation
        template_policy_model = TemplatePolicy.from_dict(template_policy_model_json)
        assert template_policy_model != False

        # Construct a model instance of TemplatePolicy by calling from_dict on the json representation
        template_policy_model_dict = TemplatePolicy.from_dict(template_policy_model_json).__dict__
        template_policy_model2 = TemplatePolicy(**template_policy_model_dict)

        # Verify the model instances are equivalent
        assert template_policy_model == template_policy_model2

        # Convert model instance back to dict and verify no loss of data
        template_policy_model_json2 = template_policy_model.to_dict()
        assert template_policy_model_json2 == template_policy_model_json


class TestModel_V2Policy:
    """
    Test Class for V2Policy
    """

    def test_v2_policy_serialization(self):
        """
        Test serialization/deserialization for V2Policy
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_subject_attribute_model = {}  # V2PolicySubjectAttribute
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        v2_policy_subject_model = {}  # V2PolicySubject
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        v2_policy_resource_attribute_model = {}  # V2PolicyResourceAttribute
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        v2_policy_resource_tag_model = {}  # V2PolicyResourceTag
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        v2_policy_resource_model = {}  # V2PolicyResource
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        control_response_model = {}  # ControlResponseControl
        control_response_model['grant'] = grant_model

        # Construct a json representation of a V2Policy model
        v2_policy_model_json = {}
        v2_policy_model_json['type'] = 'access'
        v2_policy_model_json['description'] = 'testString'
        v2_policy_model_json['subject'] = v2_policy_subject_model
        v2_policy_model_json['resource'] = v2_policy_resource_model
        v2_policy_model_json['pattern'] = 'testString'
        v2_policy_model_json['rule'] = v2_policy_rule_model
        v2_policy_model_json['control'] = control_response_model
        v2_policy_model_json['state'] = 'active'
        v2_policy_model_json['last_permit_at'] = 'testString'
        v2_policy_model_json['last_permit_frequency'] = 38

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


class TestModel_V2PolicyCollection:
    """
    Test Class for V2PolicyCollection
    """

    def test_v2_policy_collection_serialization(self):
        """
        Test serialization/deserialization for V2PolicyCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_subject_attribute_model = {}  # V2PolicySubjectAttribute
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        v2_policy_subject_model = {}  # V2PolicySubject
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        v2_policy_resource_attribute_model = {}  # V2PolicyResourceAttribute
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        v2_policy_resource_tag_model = {}  # V2PolicyResourceTag
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        v2_policy_resource_model = {}  # V2PolicyResource
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        control_response_model = {}  # ControlResponseControl
        control_response_model['grant'] = grant_model

        template_metadata_model = {}  # TemplateMetadata
        template_metadata_model['id'] = 'testString'
        template_metadata_model['version'] = 'testString'
        template_metadata_model['assignment_id'] = 'testString'
        template_metadata_model['root_id'] = 'testString'
        template_metadata_model['root_version'] = 'testString'

        v2_policy_template_meta_data_model = {}  # V2PolicyTemplateMetaData
        v2_policy_template_meta_data_model['type'] = 'access'
        v2_policy_template_meta_data_model['description'] = 'testString'
        v2_policy_template_meta_data_model['subject'] = v2_policy_subject_model
        v2_policy_template_meta_data_model['resource'] = v2_policy_resource_model
        v2_policy_template_meta_data_model['pattern'] = 'testString'
        v2_policy_template_meta_data_model['rule'] = v2_policy_rule_model
        v2_policy_template_meta_data_model['control'] = control_response_model
        v2_policy_template_meta_data_model['state'] = 'active'
        v2_policy_template_meta_data_model['last_permit_at'] = 'testString'
        v2_policy_template_meta_data_model['last_permit_frequency'] = 38
        v2_policy_template_meta_data_model['template'] = template_metadata_model

        # Construct a json representation of a V2PolicyCollection model
        v2_policy_collection_model_json = {}
        v2_policy_collection_model_json['policies'] = [v2_policy_template_meta_data_model]

        # Construct a model instance of V2PolicyCollection by calling from_dict on the json representation
        v2_policy_collection_model = V2PolicyCollection.from_dict(v2_policy_collection_model_json)
        assert v2_policy_collection_model != False

        # Construct a model instance of V2PolicyCollection by calling from_dict on the json representation
        v2_policy_collection_model_dict = V2PolicyCollection.from_dict(v2_policy_collection_model_json).__dict__
        v2_policy_collection_model2 = V2PolicyCollection(**v2_policy_collection_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_collection_model == v2_policy_collection_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_collection_model_json2 = v2_policy_collection_model.to_dict()
        assert v2_policy_collection_model_json2 == v2_policy_collection_model_json


class TestModel_V2PolicyResource:
    """
    Test Class for V2PolicyResource
    """

    def test_v2_policy_resource_serialization(self):
        """
        Test serialization/deserialization for V2PolicyResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_resource_attribute_model = {}  # V2PolicyResourceAttribute
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        v2_policy_resource_tag_model = {}  # V2PolicyResourceTag
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        # Construct a json representation of a V2PolicyResource model
        v2_policy_resource_model_json = {}
        v2_policy_resource_model_json['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model_json['tags'] = [v2_policy_resource_tag_model]

        # Construct a model instance of V2PolicyResource by calling from_dict on the json representation
        v2_policy_resource_model = V2PolicyResource.from_dict(v2_policy_resource_model_json)
        assert v2_policy_resource_model != False

        # Construct a model instance of V2PolicyResource by calling from_dict on the json representation
        v2_policy_resource_model_dict = V2PolicyResource.from_dict(v2_policy_resource_model_json).__dict__
        v2_policy_resource_model2 = V2PolicyResource(**v2_policy_resource_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_resource_model == v2_policy_resource_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_resource_model_json2 = v2_policy_resource_model.to_dict()
        assert v2_policy_resource_model_json2 == v2_policy_resource_model_json


class TestModel_V2PolicyResourceAttribute:
    """
    Test Class for V2PolicyResourceAttribute
    """

    def test_v2_policy_resource_attribute_serialization(self):
        """
        Test serialization/deserialization for V2PolicyResourceAttribute
        """

        # Construct a json representation of a V2PolicyResourceAttribute model
        v2_policy_resource_attribute_model_json = {}
        v2_policy_resource_attribute_model_json['key'] = 'testString'
        v2_policy_resource_attribute_model_json['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model_json['value'] = 'testString'

        # Construct a model instance of V2PolicyResourceAttribute by calling from_dict on the json representation
        v2_policy_resource_attribute_model = V2PolicyResourceAttribute.from_dict(v2_policy_resource_attribute_model_json)
        assert v2_policy_resource_attribute_model != False

        # Construct a model instance of V2PolicyResourceAttribute by calling from_dict on the json representation
        v2_policy_resource_attribute_model_dict = V2PolicyResourceAttribute.from_dict(v2_policy_resource_attribute_model_json).__dict__
        v2_policy_resource_attribute_model2 = V2PolicyResourceAttribute(**v2_policy_resource_attribute_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_resource_attribute_model == v2_policy_resource_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_resource_attribute_model_json2 = v2_policy_resource_attribute_model.to_dict()
        assert v2_policy_resource_attribute_model_json2 == v2_policy_resource_attribute_model_json


class TestModel_V2PolicyResourceTag:
    """
    Test Class for V2PolicyResourceTag
    """

    def test_v2_policy_resource_tag_serialization(self):
        """
        Test serialization/deserialization for V2PolicyResourceTag
        """

        # Construct a json representation of a V2PolicyResourceTag model
        v2_policy_resource_tag_model_json = {}
        v2_policy_resource_tag_model_json['key'] = 'testString'
        v2_policy_resource_tag_model_json['value'] = 'testString'
        v2_policy_resource_tag_model_json['operator'] = 'stringEquals'

        # Construct a model instance of V2PolicyResourceTag by calling from_dict on the json representation
        v2_policy_resource_tag_model = V2PolicyResourceTag.from_dict(v2_policy_resource_tag_model_json)
        assert v2_policy_resource_tag_model != False

        # Construct a model instance of V2PolicyResourceTag by calling from_dict on the json representation
        v2_policy_resource_tag_model_dict = V2PolicyResourceTag.from_dict(v2_policy_resource_tag_model_json).__dict__
        v2_policy_resource_tag_model2 = V2PolicyResourceTag(**v2_policy_resource_tag_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_resource_tag_model == v2_policy_resource_tag_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_resource_tag_model_json2 = v2_policy_resource_tag_model.to_dict()
        assert v2_policy_resource_tag_model_json2 == v2_policy_resource_tag_model_json


class TestModel_V2PolicySubject:
    """
    Test Class for V2PolicySubject
    """

    def test_v2_policy_subject_serialization(self):
        """
        Test serialization/deserialization for V2PolicySubject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_subject_attribute_model = {}  # V2PolicySubjectAttribute
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a json representation of a V2PolicySubject model
        v2_policy_subject_model_json = {}
        v2_policy_subject_model_json['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a model instance of V2PolicySubject by calling from_dict on the json representation
        v2_policy_subject_model = V2PolicySubject.from_dict(v2_policy_subject_model_json)
        assert v2_policy_subject_model != False

        # Construct a model instance of V2PolicySubject by calling from_dict on the json representation
        v2_policy_subject_model_dict = V2PolicySubject.from_dict(v2_policy_subject_model_json).__dict__
        v2_policy_subject_model2 = V2PolicySubject(**v2_policy_subject_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_subject_model == v2_policy_subject_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_subject_model_json2 = v2_policy_subject_model.to_dict()
        assert v2_policy_subject_model_json2 == v2_policy_subject_model_json


class TestModel_V2PolicySubjectAttribute:
    """
    Test Class for V2PolicySubjectAttribute
    """

    def test_v2_policy_subject_attribute_serialization(self):
        """
        Test serialization/deserialization for V2PolicySubjectAttribute
        """

        # Construct a json representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model_json = {}
        v2_policy_subject_attribute_model_json['key'] = 'testString'
        v2_policy_subject_attribute_model_json['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model_json['value'] = 'testString'

        # Construct a model instance of V2PolicySubjectAttribute by calling from_dict on the json representation
        v2_policy_subject_attribute_model = V2PolicySubjectAttribute.from_dict(v2_policy_subject_attribute_model_json)
        assert v2_policy_subject_attribute_model != False

        # Construct a model instance of V2PolicySubjectAttribute by calling from_dict on the json representation
        v2_policy_subject_attribute_model_dict = V2PolicySubjectAttribute.from_dict(v2_policy_subject_attribute_model_json).__dict__
        v2_policy_subject_attribute_model2 = V2PolicySubjectAttribute(**v2_policy_subject_attribute_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_subject_attribute_model == v2_policy_subject_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_subject_attribute_model_json2 = v2_policy_subject_attribute_model.to_dict()
        assert v2_policy_subject_attribute_model_json2 == v2_policy_subject_attribute_model_json


class TestModel_V2PolicyTemplateMetaData:
    """
    Test Class for V2PolicyTemplateMetaData
    """

    def test_v2_policy_template_meta_data_serialization(self):
        """
        Test serialization/deserialization for V2PolicyTemplateMetaData
        """

        # Construct dict forms of any model objects needed in order to build this model.

        v2_policy_subject_attribute_model = {}  # V2PolicySubjectAttribute
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        v2_policy_subject_model = {}  # V2PolicySubject
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        v2_policy_resource_attribute_model = {}  # V2PolicyResourceAttribute
        v2_policy_resource_attribute_model['key'] = 'testString'
        v2_policy_resource_attribute_model['operator'] = 'stringEquals'
        v2_policy_resource_attribute_model['value'] = 'testString'

        v2_policy_resource_tag_model = {}  # V2PolicyResourceTag
        v2_policy_resource_tag_model['key'] = 'testString'
        v2_policy_resource_tag_model['value'] = 'testString'
        v2_policy_resource_tag_model['operator'] = 'stringEquals'

        v2_policy_resource_model = {}  # V2PolicyResource
        v2_policy_resource_model['attributes'] = [v2_policy_resource_attribute_model]
        v2_policy_resource_model['tags'] = [v2_policy_resource_tag_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        control_response_model = {}  # ControlResponseControl
        control_response_model['grant'] = grant_model

        template_metadata_model = {}  # TemplateMetadata
        template_metadata_model['id'] = 'testString'
        template_metadata_model['version'] = 'testString'
        template_metadata_model['assignment_id'] = 'testString'
        template_metadata_model['root_id'] = 'testString'
        template_metadata_model['root_version'] = 'testString'

        # Construct a json representation of a V2PolicyTemplateMetaData model
        v2_policy_template_meta_data_model_json = {}
        v2_policy_template_meta_data_model_json['type'] = 'access'
        v2_policy_template_meta_data_model_json['description'] = 'testString'
        v2_policy_template_meta_data_model_json['subject'] = v2_policy_subject_model
        v2_policy_template_meta_data_model_json['resource'] = v2_policy_resource_model
        v2_policy_template_meta_data_model_json['pattern'] = 'testString'
        v2_policy_template_meta_data_model_json['rule'] = v2_policy_rule_model
        v2_policy_template_meta_data_model_json['control'] = control_response_model
        v2_policy_template_meta_data_model_json['state'] = 'active'
        v2_policy_template_meta_data_model_json['last_permit_at'] = 'testString'
        v2_policy_template_meta_data_model_json['last_permit_frequency'] = 38
        v2_policy_template_meta_data_model_json['template'] = template_metadata_model

        # Construct a model instance of V2PolicyTemplateMetaData by calling from_dict on the json representation
        v2_policy_template_meta_data_model = V2PolicyTemplateMetaData.from_dict(v2_policy_template_meta_data_model_json)
        assert v2_policy_template_meta_data_model != False

        # Construct a model instance of V2PolicyTemplateMetaData by calling from_dict on the json representation
        v2_policy_template_meta_data_model_dict = V2PolicyTemplateMetaData.from_dict(v2_policy_template_meta_data_model_json).__dict__
        v2_policy_template_meta_data_model2 = V2PolicyTemplateMetaData(**v2_policy_template_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_template_meta_data_model == v2_policy_template_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_template_meta_data_model_json2 = v2_policy_template_meta_data_model.to_dict()
        assert v2_policy_template_meta_data_model_json2 == v2_policy_template_meta_data_model_json


class TestModel_ControlResponseControl:
    """
    Test Class for ControlResponseControl
    """

    def test_control_response_control_serialization(self):
        """
        Test serialization/deserialization for ControlResponseControl
        """

        # Construct dict forms of any model objects needed in order to build this model.

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        grant_model = {}  # Grant
        grant_model['roles'] = [roles_model]

        # Construct a json representation of a ControlResponseControl model
        control_response_control_model_json = {}
        control_response_control_model_json['grant'] = grant_model

        # Construct a model instance of ControlResponseControl by calling from_dict on the json representation
        control_response_control_model = ControlResponseControl.from_dict(control_response_control_model_json)
        assert control_response_control_model != False

        # Construct a model instance of ControlResponseControl by calling from_dict on the json representation
        control_response_control_model_dict = ControlResponseControl.from_dict(control_response_control_model_json).__dict__
        control_response_control_model2 = ControlResponseControl(**control_response_control_model_dict)

        # Verify the model instances are equivalent
        assert control_response_control_model == control_response_control_model2

        # Convert model instance back to dict and verify no loss of data
        control_response_control_model_json2 = control_response_control_model.to_dict()
        assert control_response_control_model_json2 == control_response_control_model_json


class TestModel_ControlResponseControlWithEnrichedRoles:
    """
    Test Class for ControlResponseControlWithEnrichedRoles
    """

    def test_control_response_control_with_enriched_roles_serialization(self):
        """
        Test serialization/deserialization for ControlResponseControlWithEnrichedRoles
        """

        # Construct dict forms of any model objects needed in order to build this model.

        role_action_model = {}  # RoleAction
        role_action_model['id'] = 'testString'
        role_action_model['display_name'] = 'testString'
        role_action_model['description'] = 'testString'

        enriched_roles_model = {}  # EnrichedRoles
        enriched_roles_model['role_id'] = 'testString'
        enriched_roles_model['actions'] = [role_action_model]

        grant_with_enriched_roles_model = {}  # GrantWithEnrichedRoles
        grant_with_enriched_roles_model['roles'] = [enriched_roles_model]

        # Construct a json representation of a ControlResponseControlWithEnrichedRoles model
        control_response_control_with_enriched_roles_model_json = {}
        control_response_control_with_enriched_roles_model_json['grant'] = grant_with_enriched_roles_model

        # Construct a model instance of ControlResponseControlWithEnrichedRoles by calling from_dict on the json representation
        control_response_control_with_enriched_roles_model = ControlResponseControlWithEnrichedRoles.from_dict(control_response_control_with_enriched_roles_model_json)
        assert control_response_control_with_enriched_roles_model != False

        # Construct a model instance of ControlResponseControlWithEnrichedRoles by calling from_dict on the json representation
        control_response_control_with_enriched_roles_model_dict = ControlResponseControlWithEnrichedRoles.from_dict(control_response_control_with_enriched_roles_model_json).__dict__
        control_response_control_with_enriched_roles_model2 = ControlResponseControlWithEnrichedRoles(**control_response_control_with_enriched_roles_model_dict)

        # Verify the model instances are equivalent
        assert control_response_control_with_enriched_roles_model == control_response_control_with_enriched_roles_model2

        # Convert model instance back to dict and verify no loss of data
        control_response_control_with_enriched_roles_model_json2 = control_response_control_with_enriched_roles_model.to_dict()
        assert control_response_control_with_enriched_roles_model_json2 == control_response_control_with_enriched_roles_model_json


class TestModel_NestedConditionRuleAttribute:
    """
    Test Class for NestedConditionRuleAttribute
    """

    def test_nested_condition_rule_attribute_serialization(self):
        """
        Test serialization/deserialization for NestedConditionRuleAttribute
        """

        # Construct a json representation of a NestedConditionRuleAttribute model
        nested_condition_rule_attribute_model_json = {}
        nested_condition_rule_attribute_model_json['key'] = 'testString'
        nested_condition_rule_attribute_model_json['operator'] = 'stringEquals'
        nested_condition_rule_attribute_model_json['value'] = 'testString'

        # Construct a model instance of NestedConditionRuleAttribute by calling from_dict on the json representation
        nested_condition_rule_attribute_model = NestedConditionRuleAttribute.from_dict(nested_condition_rule_attribute_model_json)
        assert nested_condition_rule_attribute_model != False

        # Construct a model instance of NestedConditionRuleAttribute by calling from_dict on the json representation
        nested_condition_rule_attribute_model_dict = NestedConditionRuleAttribute.from_dict(nested_condition_rule_attribute_model_json).__dict__
        nested_condition_rule_attribute_model2 = NestedConditionRuleAttribute(**nested_condition_rule_attribute_model_dict)

        # Verify the model instances are equivalent
        assert nested_condition_rule_attribute_model == nested_condition_rule_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        nested_condition_rule_attribute_model_json2 = nested_condition_rule_attribute_model.to_dict()
        assert nested_condition_rule_attribute_model_json2 == nested_condition_rule_attribute_model_json


class TestModel_NestedConditionRuleWithConditions:
    """
    Test Class for NestedConditionRuleWithConditions
    """

    def test_nested_condition_rule_with_conditions_serialization(self):
        """
        Test serialization/deserialization for NestedConditionRuleWithConditions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_attribute_model = {}  # RuleAttribute
        rule_attribute_model['key'] = 'testString'
        rule_attribute_model['operator'] = 'stringEquals'
        rule_attribute_model['value'] = 'testString'

        # Construct a json representation of a NestedConditionRuleWithConditions model
        nested_condition_rule_with_conditions_model_json = {}
        nested_condition_rule_with_conditions_model_json['operator'] = 'and'
        nested_condition_rule_with_conditions_model_json['conditions'] = [rule_attribute_model]

        # Construct a model instance of NestedConditionRuleWithConditions by calling from_dict on the json representation
        nested_condition_rule_with_conditions_model = NestedConditionRuleWithConditions.from_dict(nested_condition_rule_with_conditions_model_json)
        assert nested_condition_rule_with_conditions_model != False

        # Construct a model instance of NestedConditionRuleWithConditions by calling from_dict on the json representation
        nested_condition_rule_with_conditions_model_dict = NestedConditionRuleWithConditions.from_dict(nested_condition_rule_with_conditions_model_json).__dict__
        nested_condition_rule_with_conditions_model2 = NestedConditionRuleWithConditions(**nested_condition_rule_with_conditions_model_dict)

        # Verify the model instances are equivalent
        assert nested_condition_rule_with_conditions_model == nested_condition_rule_with_conditions_model2

        # Convert model instance back to dict and verify no loss of data
        nested_condition_rule_with_conditions_model_json2 = nested_condition_rule_with_conditions_model.to_dict()
        assert nested_condition_rule_with_conditions_model_json2 == nested_condition_rule_with_conditions_model_json


class TestModel_V2PolicyRuleRuleAttribute:
    """
    Test Class for V2PolicyRuleRuleAttribute
    """

    def test_v2_policy_rule_rule_attribute_serialization(self):
        """
        Test serialization/deserialization for V2PolicyRuleRuleAttribute
        """

        # Construct a json representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_rule_attribute_model_json = {}
        v2_policy_rule_rule_attribute_model_json['key'] = 'testString'
        v2_policy_rule_rule_attribute_model_json['operator'] = 'stringEquals'
        v2_policy_rule_rule_attribute_model_json['value'] = 'testString'

        # Construct a model instance of V2PolicyRuleRuleAttribute by calling from_dict on the json representation
        v2_policy_rule_rule_attribute_model = V2PolicyRuleRuleAttribute.from_dict(v2_policy_rule_rule_attribute_model_json)
        assert v2_policy_rule_rule_attribute_model != False

        # Construct a model instance of V2PolicyRuleRuleAttribute by calling from_dict on the json representation
        v2_policy_rule_rule_attribute_model_dict = V2PolicyRuleRuleAttribute.from_dict(v2_policy_rule_rule_attribute_model_json).__dict__
        v2_policy_rule_rule_attribute_model2 = V2PolicyRuleRuleAttribute(**v2_policy_rule_rule_attribute_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_rule_rule_attribute_model == v2_policy_rule_rule_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_rule_rule_attribute_model_json2 = v2_policy_rule_rule_attribute_model.to_dict()
        assert v2_policy_rule_rule_attribute_model_json2 == v2_policy_rule_rule_attribute_model_json


class TestModel_V2PolicyRuleRuleWithNestedConditions:
    """
    Test Class for V2PolicyRuleRuleWithNestedConditions
    """

    def test_v2_policy_rule_rule_with_nested_conditions_serialization(self):
        """
        Test serialization/deserialization for V2PolicyRuleRuleWithNestedConditions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        nested_condition_model = {}  # NestedConditionRuleAttribute
        nested_condition_model['key'] = 'testString'
        nested_condition_model['operator'] = 'stringEquals'
        nested_condition_model['value'] = 'testString'

        # Construct a json representation of a V2PolicyRuleRuleWithNestedConditions model
        v2_policy_rule_rule_with_nested_conditions_model_json = {}
        v2_policy_rule_rule_with_nested_conditions_model_json['operator'] = 'and'
        v2_policy_rule_rule_with_nested_conditions_model_json['conditions'] = [nested_condition_model]

        # Construct a model instance of V2PolicyRuleRuleWithNestedConditions by calling from_dict on the json representation
        v2_policy_rule_rule_with_nested_conditions_model = V2PolicyRuleRuleWithNestedConditions.from_dict(v2_policy_rule_rule_with_nested_conditions_model_json)
        assert v2_policy_rule_rule_with_nested_conditions_model != False

        # Construct a model instance of V2PolicyRuleRuleWithNestedConditions by calling from_dict on the json representation
        v2_policy_rule_rule_with_nested_conditions_model_dict = V2PolicyRuleRuleWithNestedConditions.from_dict(v2_policy_rule_rule_with_nested_conditions_model_json).__dict__
        v2_policy_rule_rule_with_nested_conditions_model2 = V2PolicyRuleRuleWithNestedConditions(**v2_policy_rule_rule_with_nested_conditions_model_dict)

        # Verify the model instances are equivalent
        assert v2_policy_rule_rule_with_nested_conditions_model == v2_policy_rule_rule_with_nested_conditions_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_rule_rule_with_nested_conditions_model_json2 = v2_policy_rule_rule_with_nested_conditions_model.to_dict()
        assert v2_policy_rule_rule_with_nested_conditions_model_json2 == v2_policy_rule_rule_with_nested_conditions_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
