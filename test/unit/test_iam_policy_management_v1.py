# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2025.
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


_service = IamPolicyManagementV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://iam.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "policies": [{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
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
        limit = 50
        start = 'testString'

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
            limit=limit,
            start=start,
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
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "policies": [{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "policies": [{"id": "id", "type": "type", "description": "description", "subjects": [{"attributes": [{"name": "name", "value": "value"}]}], "roles": [{"role_id": "role_id", "display_name": "display_name", "description": "description"}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
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

    @responses.activate
    def test_list_policies_with_pager_get_next(self):
        """
        test_list_policies_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/policies')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"policies":[{"id":"id","type":"type","description":"description","subjects":[{"attributes":[{"name":"name","value":"value"}]}],"roles":[{"role_id":"role_id","display_name":"display_name","description":"description"}],"resources":[{"attributes":[{"name":"name","value":"value","operator":"operator"}],"tags":[{"name":"name","value":"value","operator":"operator"}]}],"href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","state":"active","template":{"id":"id","version":"version","assignment_id":"assignment_id","root_id":"root_id","root_version":"root_version"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"policies":[{"id":"id","type":"type","description":"description","subjects":[{"attributes":[{"name":"name","value":"value"}]}],"roles":[{"role_id":"role_id","display_name":"display_name","description":"description"}],"resources":[{"attributes":[{"name":"name","value":"value","operator":"operator"}],"tags":[{"name":"name","value":"value","operator":"operator"}]}],"href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","state":"active","template":{"id":"id","version":"version","assignment_id":"assignment_id","root_id":"root_id","root_version":"root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = PoliciesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            iam_id='testString',
            access_group_id='testString',
            type='access',
            service_type='service',
            tag_name='testString',
            tag_value='testString',
            sort='id',
            format='include_last_permit',
            state='active',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_policies_with_pager_get_all(self):
        """
        test_list_policies_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/policies')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"policies":[{"id":"id","type":"type","description":"description","subjects":[{"attributes":[{"name":"name","value":"value"}]}],"roles":[{"role_id":"role_id","display_name":"display_name","description":"description"}],"resources":[{"attributes":[{"name":"name","value":"value","operator":"operator"}],"tags":[{"name":"name","value":"value","operator":"operator"}]}],"href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","state":"active","template":{"id":"id","version":"version","assignment_id":"assignment_id","root_id":"root_id","root_version":"root_version"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"policies":[{"id":"id","type":"type","description":"description","subjects":[{"attributes":[{"name":"name","value":"value"}]}],"roles":[{"role_id":"role_id","display_name":"display_name","description":"description"}],"resources":[{"attributes":[{"name":"name","value":"value","operator":"operator"}],"tags":[{"name":"name","value":"value","operator":"operator"}]}],"href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","state":"active","template":{"id":"id","version":"version","assignment_id":"assignment_id","root_id":"root_id","root_version":"root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = PoliciesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            iam_id='testString',
            access_group_id='testString',
            type='access',
            service_type='service',
            tag_name='testString',
            tag_value='testString',
            sort='id',
            format='include_last_permit',
            state='active',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "policies": [{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21, "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
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
        limit = 50
        start = 'testString'

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
            limit=limit,
            start=start,
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
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "policies": [{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21, "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "policies": [{"type": "access", "description": "description", "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "id": "id", "href": "href", "control": {"grant": {"roles": [{"role_id": "role_id"}]}}, "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "state": "active", "last_permit_at": "last_permit_at", "last_permit_frequency": 21, "template": {"id": "id", "version": "version", "assignment_id": "assignment_id", "root_id": "root_id", "root_version": "root_version"}}]}'
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

    @responses.activate
    def test_list_v2_policies_with_pager_get_next(self):
        """
        test_list_v2_policies_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/policies')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"policies":[{"type":"access","description":"description","subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"id":"id","href":"href","control":{"grant":{"roles":[{"role_id":"role_id"}]}},"created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","state":"active","last_permit_at":"last_permit_at","last_permit_frequency":21,"template":{"id":"id","version":"version","assignment_id":"assignment_id","root_id":"root_id","root_version":"root_version"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"policies":[{"type":"access","description":"description","subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"id":"id","href":"href","control":{"grant":{"roles":[{"role_id":"role_id"}]}},"created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","state":"active","last_permit_at":"last_permit_at","last_permit_frequency":21,"template":{"id":"id","version":"version","assignment_id":"assignment_id","root_id":"root_id","root_version":"root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = V2PoliciesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            iam_id='testString',
            access_group_id='testString',
            type='access',
            service_type='service',
            service_name='testString',
            service_group_id='testString',
            sort='testString',
            format='include_last_permit',
            state='active',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_v2_policies_with_pager_get_all(self):
        """
        test_list_v2_policies_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/policies')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"policies":[{"type":"access","description":"description","subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"id":"id","href":"href","control":{"grant":{"roles":[{"role_id":"role_id"}]}},"created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","state":"active","last_permit_at":"last_permit_at","last_permit_frequency":21,"template":{"id":"id","version":"version","assignment_id":"assignment_id","root_id":"root_id","root_version":"root_version"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"policies":[{"type":"access","description":"description","subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"id":"id","href":"href","control":{"grant":{"roles":[{"role_id":"role_id"}]}},"created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","state":"active","last_permit_at":"last_permit_at","last_permit_frequency":21,"template":{"id":"id","version":"version","assignment_id":"assignment_id","root_id":"root_id","root_version":"root_version"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = V2PoliciesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            iam_id='testString',
            access_group_id='testString',
            type='access',
            service_type='service',
            service_name='testString',
            service_group_id='testString',
            sort='testString',
            format='include_last_permit',
            state='active',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "policy_templates": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
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
        name = 'testString'
        policy_service_type = 'service'
        policy_service_name = 'testString'
        policy_service_group_id = 'testString'
        policy_type = 'access'
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_policy_templates(
            account_id,
            accept_language=accept_language,
            state=state,
            name=name,
            policy_service_type=policy_service_type,
            policy_service_name=policy_service_name,
            policy_service_group_id=policy_service_group_id,
            policy_type=policy_type,
            limit=limit,
            start=start,
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
        assert 'name={}'.format(name) in query_string
        assert 'policy_service_type={}'.format(policy_service_type) in query_string
        assert 'policy_service_name={}'.format(policy_service_name) in query_string
        assert 'policy_service_group_id={}'.format(policy_service_group_id) in query_string
        assert 'policy_type={}'.format(policy_type) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "policy_templates": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "policy_templates": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
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

    @responses.activate
    def test_list_policy_templates_with_pager_get_next(self):
        """
        test_list_policy_templates_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/policy_templates')
        mock_response1 = '{"next":{"start":"1"},"policy_templates":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"policy":{"type":"access","description":"description","resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"control":{"grant":{"roles":[{"role_id":"role_id"}],"role_template_references":[{"id":"id","version":"version"}]}}},"state":"active","id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        mock_response2 = '{"policy_templates":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"policy":{"type":"access","description":"description","resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"control":{"grant":{"roles":[{"role_id":"role_id"}],"role_template_references":[{"id":"id","version":"version"}]}}},"state":"active","id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = PolicyTemplatesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            state='active',
            name='testString',
            policy_service_type='service',
            policy_service_name='testString',
            policy_service_group_id='testString',
            policy_type='access',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_policy_templates_with_pager_get_all(self):
        """
        test_list_policy_templates_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/policy_templates')
        mock_response1 = '{"next":{"start":"1"},"policy_templates":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"policy":{"type":"access","description":"description","resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"control":{"grant":{"roles":[{"role_id":"role_id"}],"role_template_references":[{"id":"id","version":"version"}]}}},"state":"active","id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        mock_response2 = '{"policy_templates":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"policy":{"type":"access","description":"description","resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"control":{"grant":{"roles":[{"role_id":"role_id"}],"role_template_references":[{"id":"id","version":"version"}]}}},"state":"active","id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = PolicyTemplatesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            state='active',
            name='testString',
            policy_service_type='service',
            policy_service_name='testString',
            policy_service_group_id='testString',
            policy_type='access',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
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

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a RoleTemplateReferencesItem model
        role_template_references_item_model = {}
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        # Construct a dict representation of a TemplateGrant model
        template_grant_model = {}
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        # Construct a dict representation of a TemplateControl model
        template_control_model = {}
        template_control_model['grant'] = template_grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
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

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a RoleTemplateReferencesItem model
        role_template_references_item_model = {}
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        # Construct a dict representation of a TemplateGrant model
        template_grant_model = {}
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        # Construct a dict representation of a TemplateControl model
        template_control_model = {}
        template_control_model['grant'] = template_grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
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

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a RoleTemplateReferencesItem model
        role_template_references_item_model = {}
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        # Construct a dict representation of a TemplateGrant model
        template_grant_model = {}
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        # Construct a dict representation of a TemplateControl model
        template_control_model = {}
        template_control_model['grant'] = template_grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
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

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a RoleTemplateReferencesItem model
        role_template_references_item_model = {}
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        # Construct a dict representation of a TemplateGrant model
        template_grant_model = {}
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        # Construct a dict representation of a TemplateControl model
        template_control_model = {}
        template_control_model['grant'] = template_grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "counts": {"template": {"current": 7, "limit": 5}, "version": {"current": 7, "limit": 5}}}'
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

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a RoleTemplateReferencesItem model
        role_template_references_item_model = {}
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        # Construct a dict representation of a TemplateGrant model
        template_grant_model = {}
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        # Construct a dict representation of a TemplateControl model
        template_control_model = {}
        template_control_model['grant'] = template_grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
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
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_policy_template_versions(
            policy_template_id,
            state=state,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'state={}'.format(state) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
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

    @responses.activate
    def test_list_policy_template_versions_with_pager_get_next(self):
        """
        test_list_policy_template_versions_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/policy_templates/testString/versions')
        mock_response1 = '{"next":{"start":"1"},"versions":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"policy":{"type":"access","description":"description","resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"control":{"grant":{"roles":[{"role_id":"role_id"}],"role_template_references":[{"id":"id","version":"version"}]}}},"state":"active","id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        mock_response2 = '{"versions":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"policy":{"type":"access","description":"description","resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"control":{"grant":{"roles":[{"role_id":"role_id"}],"role_template_references":[{"id":"id","version":"version"}]}}},"state":"active","id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = PolicyTemplateVersionsPager(
            client=_service,
            policy_template_id='testString',
            state='active',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_policy_template_versions_with_pager_get_all(self):
        """
        test_list_policy_template_versions_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/policy_templates/testString/versions')
        mock_response1 = '{"next":{"start":"1"},"versions":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"policy":{"type":"access","description":"description","resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"control":{"grant":{"roles":[{"role_id":"role_id"}],"role_template_references":[{"id":"id","version":"version"}]}}},"state":"active","id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        mock_response2 = '{"versions":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"policy":{"type":"access","description":"description","resource":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}],"tags":[{"key":"key","value":"value","operator":"stringEquals"}]},"subject":{"attributes":[{"key":"key","operator":"stringEquals","value":"anyValue"}]},"pattern":"pattern","rule":{"key":"key","operator":"stringEquals","value":"anyValue"},"control":{"grant":{"roles":[{"role_id":"role_id"}],"role_template_references":[{"id":"id","version":"version"}]}}},"state":"active","id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = PolicyTemplateVersionsPager(
            client=_service,
            policy_template_id='testString',
            state='active',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a RoleTemplateReferencesItem model
        role_template_references_item_model = {}
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        # Construct a dict representation of a TemplateGrant model
        template_grant_model = {}
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        # Construct a dict representation of a TemplateControl model
        template_control_model = {}
        template_control_model['grant'] = template_grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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

        # Construct a dict representation of a V2PolicySubjectAttribute model
        v2_policy_subject_attribute_model = {}
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        # Construct a dict representation of a V2PolicySubject model
        v2_policy_subject_model = {}
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        # Construct a dict representation of a V2PolicyRuleRuleAttribute model
        v2_policy_rule_model = {}
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role_id'] = 'testString'

        # Construct a dict representation of a RoleTemplateReferencesItem model
        role_template_references_item_model = {}
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        # Construct a dict representation of a TemplateGrant model
        template_grant_model = {}
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        # Construct a dict representation of a TemplateControl model
        template_control_model = {}
        template_control_model['grant'] = template_grant_model

        # Construct a dict representation of a TemplatePolicy model
        template_policy_model = {}
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "policy": {"type": "access", "description": "description", "resource": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}], "tags": [{"key": "key", "value": "value", "operator": "stringEquals"}]}, "subject": {"attributes": [{"key": "key", "operator": "stringEquals", "value": "anyValue"}]}, "pattern": "pattern", "rule": {"key": "key", "operator": "stringEquals", "value": "anyValue"}, "control": {"grant": {"roles": [{"role_id": "role_id"}], "role_template_references": [{"id": "id", "version": "version"}]}}}, "state": "active", "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        version = '1.0'
        account_id = 'testString'
        accept_language = 'default'
        template_id = 'testString'
        template_version = 'testString'
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_policy_assignments(
            version,
            account_id,
            accept_language=accept_language,
            template_id=template_id,
            template_version=template_version,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'version={}'.format(version) in query_string
        assert 'account_id={}'.format(account_id) in query_string
        assert 'template_id={}'.format(template_id) in query_string
        assert 'template_version={}'.format(template_version) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        version = '1.0'
        account_id = 'testString'

        # Invoke method
        response = _service.list_policy_assignments(
            version,
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'version={}'.format(version) in query_string
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
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        version = '1.0'
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version": version,
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

    @responses.activate
    def test_list_policy_assignments_with_pager_get_next(self):
        """
        test_list_policy_assignments_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/policy_assignments')
        mock_response1 = '{"next":{"start":"1"},"assignments":[{"target":{"type":"Account","id":"id"},"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","resources":[{"target":{"type":"Account","id":"id"},"policy":{"resource_created":{"id":"id"},"status":"status","error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"subject":{"id":"id","type":"iam_id"},"template":{"id":"id","version":"version"},"status":"in_progress"}],"total_count":2,"limit":1}'
        mock_response2 = '{"assignments":[{"target":{"type":"Account","id":"id"},"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","resources":[{"target":{"type":"Account","id":"id"},"policy":{"resource_created":{"id":"id"},"status":"status","error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"subject":{"id":"id","type":"iam_id"},"template":{"id":"id","version":"version"},"status":"in_progress"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = PolicyAssignmentsPager(
            client=_service,
            version='1.0',
            account_id='testString',
            accept_language='default',
            template_id='testString',
            template_version='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_policy_assignments_with_pager_get_all(self):
        """
        test_list_policy_assignments_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/policy_assignments')
        mock_response1 = '{"next":{"start":"1"},"assignments":[{"target":{"type":"Account","id":"id"},"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","resources":[{"target":{"type":"Account","id":"id"},"policy":{"resource_created":{"id":"id"},"status":"status","error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"subject":{"id":"id","type":"iam_id"},"template":{"id":"id","version":"version"},"status":"in_progress"}],"total_count":2,"limit":1}'
        mock_response2 = '{"assignments":[{"target":{"type":"Account","id":"id"},"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","resources":[{"target":{"type":"Account","id":"id"},"policy":{"resource_created":{"id":"id"},"status":"status","error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"subject":{"id":"id","type":"iam_id"},"template":{"id":"id","version":"version"},"status":"in_progress"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = PolicyAssignmentsPager(
            client=_service,
            version='1.0',
            account_id='testString',
            accept_language='default',
            template_id='testString',
            template_version='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreatePolicyTemplateAssignment:
    """
    Test Class for create_policy_template_assignment
    """

    @responses.activate
    def test_create_policy_template_assignment_all_params(self):
        """
        create_policy_template_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssignmentTargetDetails model
        assignment_target_details_model = {}
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a dict representation of a AssignmentTemplateDetails model
        assignment_template_details_model = {}
        assignment_template_details_model['id'] = 'testString'
        assignment_template_details_model['version'] = 'testString'

        # Set up parameter values
        version = '1.0'
        target = assignment_target_details_model
        templates = [assignment_template_details_model]
        accept_language = 'default'

        # Invoke method
        response = _service.create_policy_template_assignment(
            version,
            target,
            templates,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'version={}'.format(version) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['target'] == assignment_target_details_model
        assert req_body['templates'] == [assignment_template_details_model]

    def test_create_policy_template_assignment_all_params_with_retries(self):
        # Enable retries and run test_create_policy_template_assignment_all_params.
        _service.enable_retries()
        self.test_create_policy_template_assignment_all_params()

        # Disable retries and run test_create_policy_template_assignment_all_params.
        _service.disable_retries()
        self.test_create_policy_template_assignment_all_params()

    @responses.activate
    def test_create_policy_template_assignment_required_params(self):
        """
        test_create_policy_template_assignment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssignmentTargetDetails model
        assignment_target_details_model = {}
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a dict representation of a AssignmentTemplateDetails model
        assignment_template_details_model = {}
        assignment_template_details_model['id'] = 'testString'
        assignment_template_details_model['version'] = 'testString'

        # Set up parameter values
        version = '1.0'
        target = assignment_target_details_model
        templates = [assignment_template_details_model]

        # Invoke method
        response = _service.create_policy_template_assignment(
            version,
            target,
            templates,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'version={}'.format(version) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['target'] == assignment_target_details_model
        assert req_body['templates'] == [assignment_template_details_model]

    def test_create_policy_template_assignment_required_params_with_retries(self):
        # Enable retries and run test_create_policy_template_assignment_required_params.
        _service.enable_retries()
        self.test_create_policy_template_assignment_required_params()

        # Disable retries and run test_create_policy_template_assignment_required_params.
        _service.disable_retries()
        self.test_create_policy_template_assignment_required_params()

    @responses.activate
    def test_create_policy_template_assignment_value_error(self):
        """
        test_create_policy_template_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssignmentTargetDetails model
        assignment_target_details_model = {}
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a dict representation of a AssignmentTemplateDetails model
        assignment_template_details_model = {}
        assignment_template_details_model['id'] = 'testString'
        assignment_template_details_model['version'] = 'testString'

        # Set up parameter values
        version = '1.0'
        target = assignment_target_details_model
        templates = [assignment_template_details_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version": version,
            "target": target,
            "templates": templates,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_policy_template_assignment(**req_copy)

    def test_create_policy_template_assignment_value_error_with_retries(self):
        # Enable retries and run test_create_policy_template_assignment_value_error.
        _service.enable_retries()
        self.test_create_policy_template_assignment_value_error()

        # Disable retries and run test_create_policy_template_assignment_value_error.
        _service.disable_retries()
        self.test_create_policy_template_assignment_value_error()


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
        mock_response = '{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        version = '1.0'

        # Invoke method
        response = _service.get_policy_assignment(
            assignment_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'version={}'.format(version) in query_string

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
        mock_response = '{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        version = '1.0'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assignment_id": assignment_id,
            "version": version,
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


class TestUpdatePolicyAssignment:
    """
    Test Class for update_policy_assignment
    """

    @responses.activate
    def test_update_policy_assignment_all_params(self):
        """
        update_policy_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments/testString')
        mock_response = '{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        version = '1.0'
        if_match = 'testString'
        template_version = 'testString'

        # Invoke method
        response = _service.update_policy_assignment(
            assignment_id,
            version,
            if_match,
            template_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'version={}'.format(version) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['template_version'] == 'testString'

    def test_update_policy_assignment_all_params_with_retries(self):
        # Enable retries and run test_update_policy_assignment_all_params.
        _service.enable_retries()
        self.test_update_policy_assignment_all_params()

        # Disable retries and run test_update_policy_assignment_all_params.
        _service.disable_retries()
        self.test_update_policy_assignment_all_params()

    @responses.activate
    def test_update_policy_assignment_value_error(self):
        """
        test_update_policy_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments/testString')
        mock_response = '{"target": {"type": "Account", "id": "id"}, "id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "resources": [{"target": {"type": "Account", "id": "id"}, "policy": {"resource_created": {"id": "id"}, "status": "status", "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "subject": {"id": "id", "type": "iam_id"}, "template": {"id": "id", "version": "version"}, "status": "in_progress"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        version = '1.0'
        if_match = 'testString'
        template_version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assignment_id": assignment_id,
            "version": version,
            "if_match": if_match,
            "template_version": template_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_policy_assignment(**req_copy)

    def test_update_policy_assignment_value_error_with_retries(self):
        # Enable retries and run test_update_policy_assignment_value_error.
        _service.enable_retries()
        self.test_update_policy_assignment_value_error()

        # Disable retries and run test_update_policy_assignment_value_error.
        _service.disable_retries()
        self.test_update_policy_assignment_value_error()


class TestDeletePolicyAssignment:
    """
    Test Class for delete_policy_assignment
    """

    @responses.activate
    def test_delete_policy_assignment_all_params(self):
        """
        delete_policy_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        assignment_id = 'testString'

        # Invoke method
        response = _service.delete_policy_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_policy_assignment_all_params_with_retries(self):
        # Enable retries and run test_delete_policy_assignment_all_params.
        _service.enable_retries()
        self.test_delete_policy_assignment_all_params()

        # Disable retries and run test_delete_policy_assignment_all_params.
        _service.disable_retries()
        self.test_delete_policy_assignment_all_params()

    @responses.activate
    def test_delete_policy_assignment_value_error(self):
        """
        test_delete_policy_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/policy_assignments/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
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
                _service.delete_policy_assignment(**req_copy)

    def test_delete_policy_assignment_value_error_with_retries(self):
        # Enable retries and run test_delete_policy_assignment_value_error.
        _service.enable_retries()
        self.test_delete_policy_assignment_value_error()

        # Disable retries and run test_delete_policy_assignment_value_error.
        _service.disable_retries()
        self.test_delete_policy_assignment_value_error()


# endregion
##############################################################################
# End of Service: PolicyAssignments
##############################################################################

##############################################################################
# Start of Service: AccessManagementSettings
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


class TestGetSettings:
    """
    Test Class for get_settings
    """

    @responses.activate
    def test_get_settings_all_params(self):
        """
        get_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/settings/access_management')
        mock_response = '{"external_account_identity_interaction": {"identity_types": {"user": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service_id": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}}}}'
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

        # Invoke method
        response = _service.get_settings(
            account_id,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_settings_all_params_with_retries(self):
        # Enable retries and run test_get_settings_all_params.
        _service.enable_retries()
        self.test_get_settings_all_params()

        # Disable retries and run test_get_settings_all_params.
        _service.disable_retries()
        self.test_get_settings_all_params()

    @responses.activate
    def test_get_settings_required_params(self):
        """
        test_get_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/settings/access_management')
        mock_response = '{"external_account_identity_interaction": {"identity_types": {"user": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service_id": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}}}}'
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
        response = _service.get_settings(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_settings_required_params_with_retries(self):
        # Enable retries and run test_get_settings_required_params.
        _service.enable_retries()
        self.test_get_settings_required_params()

        # Disable retries and run test_get_settings_required_params.
        _service.disable_retries()
        self.test_get_settings_required_params()

    @responses.activate
    def test_get_settings_value_error(self):
        """
        test_get_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/settings/access_management')
        mock_response = '{"external_account_identity_interaction": {"identity_types": {"user": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service_id": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}}}}'
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
                _service.get_settings(**req_copy)

    def test_get_settings_value_error_with_retries(self):
        # Enable retries and run test_get_settings_value_error.
        _service.enable_retries()
        self.test_get_settings_value_error()

        # Disable retries and run test_get_settings_value_error.
        _service.disable_retries()
        self.test_get_settings_value_error()


class TestUpdateSettings:
    """
    Test Class for update_settings
    """

    @responses.activate
    def test_update_settings_all_params(self):
        """
        update_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/settings/access_management')
        mock_response = '{"external_account_identity_interaction": {"identity_types": {"user": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service_id": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}}}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a IdentityTypesBase model
        identity_types_base_model = {}
        identity_types_base_model['state'] = 'enabled'
        identity_types_base_model['external_allowed_accounts'] = ['testString']

        # Construct a dict representation of a IdentityTypesPatch model
        identity_types_patch_model = {}
        identity_types_patch_model['user'] = identity_types_base_model
        identity_types_patch_model['service_id'] = identity_types_base_model
        identity_types_patch_model['service'] = identity_types_base_model

        # Construct a dict representation of a ExternalAccountIdentityInteractionPatch model
        external_account_identity_interaction_patch_model = {}
        external_account_identity_interaction_patch_model['identity_types'] = identity_types_patch_model

        # Set up parameter values
        account_id = 'testString'
        if_match = 'testString'
        external_account_identity_interaction = external_account_identity_interaction_patch_model
        accept_language = 'default'

        # Invoke method
        response = _service.update_settings(
            account_id,
            if_match,
            external_account_identity_interaction=external_account_identity_interaction,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['external_account_identity_interaction'] == external_account_identity_interaction_patch_model

    def test_update_settings_all_params_with_retries(self):
        # Enable retries and run test_update_settings_all_params.
        _service.enable_retries()
        self.test_update_settings_all_params()

        # Disable retries and run test_update_settings_all_params.
        _service.disable_retries()
        self.test_update_settings_all_params()

    @responses.activate
    def test_update_settings_required_params(self):
        """
        test_update_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/settings/access_management')
        mock_response = '{"external_account_identity_interaction": {"identity_types": {"user": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service_id": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}}}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a IdentityTypesBase model
        identity_types_base_model = {}
        identity_types_base_model['state'] = 'enabled'
        identity_types_base_model['external_allowed_accounts'] = ['testString']

        # Construct a dict representation of a IdentityTypesPatch model
        identity_types_patch_model = {}
        identity_types_patch_model['user'] = identity_types_base_model
        identity_types_patch_model['service_id'] = identity_types_base_model
        identity_types_patch_model['service'] = identity_types_base_model

        # Construct a dict representation of a ExternalAccountIdentityInteractionPatch model
        external_account_identity_interaction_patch_model = {}
        external_account_identity_interaction_patch_model['identity_types'] = identity_types_patch_model

        # Set up parameter values
        account_id = 'testString'
        if_match = 'testString'
        external_account_identity_interaction = external_account_identity_interaction_patch_model

        # Invoke method
        response = _service.update_settings(
            account_id,
            if_match,
            external_account_identity_interaction=external_account_identity_interaction,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['external_account_identity_interaction'] == external_account_identity_interaction_patch_model

    def test_update_settings_required_params_with_retries(self):
        # Enable retries and run test_update_settings_required_params.
        _service.enable_retries()
        self.test_update_settings_required_params()

        # Disable retries and run test_update_settings_required_params.
        _service.disable_retries()
        self.test_update_settings_required_params()

    @responses.activate
    def test_update_settings_value_error(self):
        """
        test_update_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/settings/access_management')
        mock_response = '{"external_account_identity_interaction": {"identity_types": {"user": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service_id": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}, "service": {"state": "enabled", "external_allowed_accounts": ["external_allowed_accounts"]}}}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a IdentityTypesBase model
        identity_types_base_model = {}
        identity_types_base_model['state'] = 'enabled'
        identity_types_base_model['external_allowed_accounts'] = ['testString']

        # Construct a dict representation of a IdentityTypesPatch model
        identity_types_patch_model = {}
        identity_types_patch_model['user'] = identity_types_base_model
        identity_types_patch_model['service_id'] = identity_types_base_model
        identity_types_patch_model['service'] = identity_types_base_model

        # Construct a dict representation of a ExternalAccountIdentityInteractionPatch model
        external_account_identity_interaction_patch_model = {}
        external_account_identity_interaction_patch_model['identity_types'] = identity_types_patch_model

        # Set up parameter values
        account_id = 'testString'
        if_match = 'testString'
        external_account_identity_interaction = external_account_identity_interaction_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_settings(**req_copy)

    def test_update_settings_value_error_with_retries(self):
        # Enable retries and run test_update_settings_value_error.
        _service.enable_retries()
        self.test_update_settings_value_error()

        # Disable retries and run test_update_settings_value_error.
        _service.disable_retries()
        self.test_update_settings_value_error()


# endregion
##############################################################################
# End of Service: AccessManagementSettings
##############################################################################

##############################################################################
# Start of Service: ActionControlTemplates
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


class TestListActionControlTemplates:
    """
    Test Class for list_action_control_templates
    """

    @responses.activate
    def test_list_action_control_templates_all_params(self):
        """
        list_action_control_templates()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "action_control_templates": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
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
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_action_control_templates(
            account_id,
            accept_language=accept_language,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_action_control_templates_all_params_with_retries(self):
        # Enable retries and run test_list_action_control_templates_all_params.
        _service.enable_retries()
        self.test_list_action_control_templates_all_params()

        # Disable retries and run test_list_action_control_templates_all_params.
        _service.disable_retries()
        self.test_list_action_control_templates_all_params()

    @responses.activate
    def test_list_action_control_templates_required_params(self):
        """
        test_list_action_control_templates_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "action_control_templates": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
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
        response = _service.list_action_control_templates(
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

    def test_list_action_control_templates_required_params_with_retries(self):
        # Enable retries and run test_list_action_control_templates_required_params.
        _service.enable_retries()
        self.test_list_action_control_templates_required_params()

        # Disable retries and run test_list_action_control_templates_required_params.
        _service.disable_retries()
        self.test_list_action_control_templates_required_params()

    @responses.activate
    def test_list_action_control_templates_value_error(self):
        """
        test_list_action_control_templates_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "action_control_templates": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
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
                _service.list_action_control_templates(**req_copy)

    def test_list_action_control_templates_value_error_with_retries(self):
        # Enable retries and run test_list_action_control_templates_value_error.
        _service.enable_retries()
        self.test_list_action_control_templates_value_error()

        # Disable retries and run test_list_action_control_templates_value_error.
        _service.disable_retries()
        self.test_list_action_control_templates_value_error()

    @responses.activate
    def test_list_action_control_templates_with_pager_get_next(self):
        """
        test_list_action_control_templates_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/action_control_templates')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"action_control_templates":[{"name":"name","description":"description","account_id":"account_id","committed":false,"action_control":{"service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"action_control_templates":[{"name":"name","description":"description","account_id":"account_id","committed":false,"action_control":{"service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ActionControlTemplatesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_action_control_templates_with_pager_get_all(self):
        """
        test_list_action_control_templates_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/action_control_templates')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"action_control_templates":[{"name":"name","description":"description","account_id":"account_id","committed":false,"action_control":{"service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"action_control_templates":[{"name":"name","description":"description","account_id":"account_id","committed":false,"action_control":{"service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ActionControlTemplatesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateActionControlTemplate:
    """
    Test Class for create_action_control_template
    """

    @responses.activate
    def test_create_action_control_template_all_params(self):
        """
        create_action_control_template()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a TemplateActionControl model
        template_action_control_model = {}
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        description = 'testString'
        committed = True
        action_control = template_action_control_model
        accept_language = 'default'

        # Invoke method
        response = _service.create_action_control_template(
            name,
            account_id,
            description=description,
            committed=committed,
            action_control=action_control,
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
        assert req_body['description'] == 'testString'
        assert req_body['committed'] == True
        assert req_body['action_control'] == template_action_control_model

    def test_create_action_control_template_all_params_with_retries(self):
        # Enable retries and run test_create_action_control_template_all_params.
        _service.enable_retries()
        self.test_create_action_control_template_all_params()

        # Disable retries and run test_create_action_control_template_all_params.
        _service.disable_retries()
        self.test_create_action_control_template_all_params()

    @responses.activate
    def test_create_action_control_template_required_params(self):
        """
        test_create_action_control_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a TemplateActionControl model
        template_action_control_model = {}
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        description = 'testString'
        committed = True
        action_control = template_action_control_model

        # Invoke method
        response = _service.create_action_control_template(
            name,
            account_id,
            description=description,
            committed=committed,
            action_control=action_control,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['committed'] == True
        assert req_body['action_control'] == template_action_control_model

    def test_create_action_control_template_required_params_with_retries(self):
        # Enable retries and run test_create_action_control_template_required_params.
        _service.enable_retries()
        self.test_create_action_control_template_required_params()

        # Disable retries and run test_create_action_control_template_required_params.
        _service.disable_retries()
        self.test_create_action_control_template_required_params()

    @responses.activate
    def test_create_action_control_template_value_error(self):
        """
        test_create_action_control_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a TemplateActionControl model
        template_action_control_model = {}
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        description = 'testString'
        committed = True
        action_control = template_action_control_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_action_control_template(**req_copy)

    def test_create_action_control_template_value_error_with_retries(self):
        # Enable retries and run test_create_action_control_template_value_error.
        _service.enable_retries()
        self.test_create_action_control_template_value_error()

        # Disable retries and run test_create_action_control_template_value_error.
        _service.disable_retries()
        self.test_create_action_control_template_value_error()


class TestGetActionControlTemplate:
    """
    Test Class for get_action_control_template
    """

    @responses.activate
    def test_get_action_control_template_all_params(self):
        """
        get_action_control_template()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        action_control_template_id = 'testString'
        state = 'active'

        # Invoke method
        response = _service.get_action_control_template(
            action_control_template_id,
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

    def test_get_action_control_template_all_params_with_retries(self):
        # Enable retries and run test_get_action_control_template_all_params.
        _service.enable_retries()
        self.test_get_action_control_template_all_params()

        # Disable retries and run test_get_action_control_template_all_params.
        _service.disable_retries()
        self.test_get_action_control_template_all_params()

    @responses.activate
    def test_get_action_control_template_required_params(self):
        """
        test_get_action_control_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        action_control_template_id = 'testString'

        # Invoke method
        response = _service.get_action_control_template(
            action_control_template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_action_control_template_required_params_with_retries(self):
        # Enable retries and run test_get_action_control_template_required_params.
        _service.enable_retries()
        self.test_get_action_control_template_required_params()

        # Disable retries and run test_get_action_control_template_required_params.
        _service.disable_retries()
        self.test_get_action_control_template_required_params()

    @responses.activate
    def test_get_action_control_template_value_error(self):
        """
        test_get_action_control_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        action_control_template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_control_template_id": action_control_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_action_control_template(**req_copy)

    def test_get_action_control_template_value_error_with_retries(self):
        # Enable retries and run test_get_action_control_template_value_error.
        _service.enable_retries()
        self.test_get_action_control_template_value_error()

        # Disable retries and run test_get_action_control_template_value_error.
        _service.disable_retries()
        self.test_get_action_control_template_value_error()


class TestDeleteActionControlTemplate:
    """
    Test Class for delete_action_control_template
    """

    @responses.activate
    def test_delete_action_control_template_all_params(self):
        """
        delete_action_control_template()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        action_control_template_id = 'testString'

        # Invoke method
        response = _service.delete_action_control_template(
            action_control_template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_action_control_template_all_params_with_retries(self):
        # Enable retries and run test_delete_action_control_template_all_params.
        _service.enable_retries()
        self.test_delete_action_control_template_all_params()

        # Disable retries and run test_delete_action_control_template_all_params.
        _service.disable_retries()
        self.test_delete_action_control_template_all_params()

    @responses.activate
    def test_delete_action_control_template_value_error(self):
        """
        test_delete_action_control_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        action_control_template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_control_template_id": action_control_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_action_control_template(**req_copy)

    def test_delete_action_control_template_value_error_with_retries(self):
        # Enable retries and run test_delete_action_control_template_value_error.
        _service.enable_retries()
        self.test_delete_action_control_template_value_error()

        # Disable retries and run test_delete_action_control_template_value_error.
        _service.disable_retries()
        self.test_delete_action_control_template_value_error()


class TestCreateActionControlTemplateVersion:
    """
    Test Class for create_action_control_template_version
    """

    @responses.activate
    def test_create_action_control_template_version_all_params(self):
        """
        create_action_control_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a TemplateActionControl model
        template_action_control_model = {}
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        # Set up parameter values
        action_control_template_id = 'testString'
        name = 'testString'
        description = 'testString'
        action_control = template_action_control_model
        committed = True

        # Invoke method
        response = _service.create_action_control_template_version(
            action_control_template_id,
            name=name,
            description=description,
            action_control=action_control,
            committed=committed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['action_control'] == template_action_control_model
        assert req_body['committed'] == True

    def test_create_action_control_template_version_all_params_with_retries(self):
        # Enable retries and run test_create_action_control_template_version_all_params.
        _service.enable_retries()
        self.test_create_action_control_template_version_all_params()

        # Disable retries and run test_create_action_control_template_version_all_params.
        _service.disable_retries()
        self.test_create_action_control_template_version_all_params()

    @responses.activate
    def test_create_action_control_template_version_value_error(self):
        """
        test_create_action_control_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a TemplateActionControl model
        template_action_control_model = {}
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        # Set up parameter values
        action_control_template_id = 'testString'
        name = 'testString'
        description = 'testString'
        action_control = template_action_control_model
        committed = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_control_template_id": action_control_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_action_control_template_version(**req_copy)

    def test_create_action_control_template_version_value_error_with_retries(self):
        # Enable retries and run test_create_action_control_template_version_value_error.
        _service.enable_retries()
        self.test_create_action_control_template_version_value_error()

        # Disable retries and run test_create_action_control_template_version_value_error.
        _service.disable_retries()
        self.test_create_action_control_template_version_value_error()


class TestListActionControlTemplateVersions:
    """
    Test Class for list_action_control_template_versions
    """

    @responses.activate
    def test_list_action_control_template_versions_all_params(self):
        """
        list_action_control_template_versions()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        action_control_template_id = 'testString'
        state = 'active'
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_action_control_template_versions(
            action_control_template_id,
            state=state,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'state={}'.format(state) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_action_control_template_versions_all_params_with_retries(self):
        # Enable retries and run test_list_action_control_template_versions_all_params.
        _service.enable_retries()
        self.test_list_action_control_template_versions_all_params()

        # Disable retries and run test_list_action_control_template_versions_all_params.
        _service.disable_retries()
        self.test_list_action_control_template_versions_all_params()

    @responses.activate
    def test_list_action_control_template_versions_required_params(self):
        """
        test_list_action_control_template_versions_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        action_control_template_id = 'testString'

        # Invoke method
        response = _service.list_action_control_template_versions(
            action_control_template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_action_control_template_versions_required_params_with_retries(self):
        # Enable retries and run test_list_action_control_template_versions_required_params.
        _service.enable_retries()
        self.test_list_action_control_template_versions_required_params()

        # Disable retries and run test_list_action_control_template_versions_required_params.
        _service.disable_retries()
        self.test_list_action_control_template_versions_required_params()

    @responses.activate
    def test_list_action_control_template_versions_value_error(self):
        """
        test_list_action_control_template_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        action_control_template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_control_template_id": action_control_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_action_control_template_versions(**req_copy)

    def test_list_action_control_template_versions_value_error_with_retries(self):
        # Enable retries and run test_list_action_control_template_versions_value_error.
        _service.enable_retries()
        self.test_list_action_control_template_versions_value_error()

        # Disable retries and run test_list_action_control_template_versions_value_error.
        _service.disable_retries()
        self.test_list_action_control_template_versions_value_error()

    @responses.activate
    def test_list_action_control_template_versions_with_pager_get_next(self):
        """
        test_list_action_control_template_versions_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/action_control_templates/testString/versions')
        mock_response1 = '{"next":{"start":"1"},"versions":[{"name":"name","description":"description","account_id":"account_id","committed":false,"action_control":{"service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}],"total_count":2,"limit":1}'
        mock_response2 = '{"versions":[{"name":"name","description":"description","account_id":"account_id","committed":false,"action_control":{"service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ActionControlTemplateVersionsPager(
            client=_service,
            action_control_template_id='testString',
            state='active',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_action_control_template_versions_with_pager_get_all(self):
        """
        test_list_action_control_template_versions_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/action_control_templates/testString/versions')
        mock_response1 = '{"next":{"start":"1"},"versions":[{"name":"name","description":"description","account_id":"account_id","committed":false,"action_control":{"service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}],"total_count":2,"limit":1}'
        mock_response2 = '{"versions":[{"name":"name","description":"description","account_id":"account_id","committed":false,"action_control":{"service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ActionControlTemplateVersionsPager(
            client=_service,
            action_control_template_id='testString',
            state='active',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestReplaceActionControlTemplate:
    """
    Test Class for replace_action_control_template
    """

    @responses.activate
    def test_replace_action_control_template_all_params(self):
        """
        replace_action_control_template()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a TemplateActionControl model
        template_action_control_model = {}
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        # Set up parameter values
        action_control_template_id = 'testString'
        version = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'
        action_control = template_action_control_model
        committed = True

        # Invoke method
        response = _service.replace_action_control_template(
            action_control_template_id,
            version,
            if_match,
            name=name,
            description=description,
            action_control=action_control,
            committed=committed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['action_control'] == template_action_control_model
        assert req_body['committed'] == True

    def test_replace_action_control_template_all_params_with_retries(self):
        # Enable retries and run test_replace_action_control_template_all_params.
        _service.enable_retries()
        self.test_replace_action_control_template_all_params()

        # Disable retries and run test_replace_action_control_template_all_params.
        _service.disable_retries()
        self.test_replace_action_control_template_all_params()

    @responses.activate
    def test_replace_action_control_template_value_error(self):
        """
        test_replace_action_control_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a TemplateActionControl model
        template_action_control_model = {}
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        # Set up parameter values
        action_control_template_id = 'testString'
        version = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'
        action_control = template_action_control_model
        committed = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_control_template_id": action_control_template_id,
            "version": version,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_action_control_template(**req_copy)

    def test_replace_action_control_template_value_error_with_retries(self):
        # Enable retries and run test_replace_action_control_template_value_error.
        _service.enable_retries()
        self.test_replace_action_control_template_value_error()

        # Disable retries and run test_replace_action_control_template_value_error.
        _service.disable_retries()
        self.test_replace_action_control_template_value_error()


class TestDeleteActionControlTemplateVersion:
    """
    Test Class for delete_action_control_template_version
    """

    @responses.activate
    def test_delete_action_control_template_version_all_params(self):
        """
        delete_action_control_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        action_control_template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.delete_action_control_template_version(
            action_control_template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_action_control_template_version_all_params_with_retries(self):
        # Enable retries and run test_delete_action_control_template_version_all_params.
        _service.enable_retries()
        self.test_delete_action_control_template_version_all_params()

        # Disable retries and run test_delete_action_control_template_version_all_params.
        _service.disable_retries()
        self.test_delete_action_control_template_version_all_params()

    @responses.activate
    def test_delete_action_control_template_version_value_error(self):
        """
        test_delete_action_control_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        action_control_template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_control_template_id": action_control_template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_action_control_template_version(**req_copy)

    def test_delete_action_control_template_version_value_error_with_retries(self):
        # Enable retries and run test_delete_action_control_template_version_value_error.
        _service.enable_retries()
        self.test_delete_action_control_template_version_value_error()

        # Disable retries and run test_delete_action_control_template_version_value_error.
        _service.disable_retries()
        self.test_delete_action_control_template_version_value_error()


class TestGetActionControlTemplateVersion:
    """
    Test Class for get_action_control_template_version
    """

    @responses.activate
    def test_get_action_control_template_version_all_params(self):
        """
        get_action_control_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        action_control_template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.get_action_control_template_version(
            action_control_template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_action_control_template_version_all_params_with_retries(self):
        # Enable retries and run test_get_action_control_template_version_all_params.
        _service.enable_retries()
        self.test_get_action_control_template_version_all_params()

        # Disable retries and run test_get_action_control_template_version_all_params.
        _service.disable_retries()
        self.test_get_action_control_template_version_all_params()

    @responses.activate
    def test_get_action_control_template_version_value_error(self):
        """
        test_get_action_control_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "action_control": {"service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        action_control_template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_control_template_id": action_control_template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_action_control_template_version(**req_copy)

    def test_get_action_control_template_version_value_error_with_retries(self):
        # Enable retries and run test_get_action_control_template_version_value_error.
        _service.enable_retries()
        self.test_get_action_control_template_version_value_error()

        # Disable retries and run test_get_action_control_template_version_value_error.
        _service.disable_retries()
        self.test_get_action_control_template_version_value_error()


class TestCommitActionControlTemplate:
    """
    Test Class for commit_action_control_template
    """

    @responses.activate
    def test_commit_action_control_template_all_params(self):
        """
        commit_action_control_template()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        action_control_template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.commit_action_control_template(
            action_control_template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_commit_action_control_template_all_params_with_retries(self):
        # Enable retries and run test_commit_action_control_template_all_params.
        _service.enable_retries()
        self.test_commit_action_control_template_all_params()

        # Disable retries and run test_commit_action_control_template_all_params.
        _service.disable_retries()
        self.test_commit_action_control_template_all_params()

    @responses.activate
    def test_commit_action_control_template_value_error(self):
        """
        test_commit_action_control_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        action_control_template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_control_template_id": action_control_template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.commit_action_control_template(**req_copy)

    def test_commit_action_control_template_value_error_with_retries(self):
        # Enable retries and run test_commit_action_control_template_value_error.
        _service.enable_retries()
        self.test_commit_action_control_template_value_error()

        # Disable retries and run test_commit_action_control_template_value_error.
        _service.disable_retries()
        self.test_commit_action_control_template_value_error()


# endregion
##############################################################################
# End of Service: ActionControlTemplates
##############################################################################

##############################################################################
# Start of Service: ActionControlAssignments
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


class TestListActionControlAssignments:
    """
    Test Class for list_action_control_assignments
    """

    @responses.activate
    def test_list_action_control_assignments_all_params(self):
        """
        list_action_control_assignments()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
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
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_action_control_assignments(
            account_id,
            accept_language=accept_language,
            template_id=template_id,
            template_version=template_version,
            limit=limit,
            start=start,
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
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_action_control_assignments_all_params_with_retries(self):
        # Enable retries and run test_list_action_control_assignments_all_params.
        _service.enable_retries()
        self.test_list_action_control_assignments_all_params()

        # Disable retries and run test_list_action_control_assignments_all_params.
        _service.disable_retries()
        self.test_list_action_control_assignments_all_params()

    @responses.activate
    def test_list_action_control_assignments_required_params(self):
        """
        test_list_action_control_assignments_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
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
        response = _service.list_action_control_assignments(
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

    def test_list_action_control_assignments_required_params_with_retries(self):
        # Enable retries and run test_list_action_control_assignments_required_params.
        _service.enable_retries()
        self.test_list_action_control_assignments_required_params()

        # Disable retries and run test_list_action_control_assignments_required_params.
        _service.disable_retries()
        self.test_list_action_control_assignments_required_params()

    @responses.activate
    def test_list_action_control_assignments_value_error(self):
        """
        test_list_action_control_assignments_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
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
                _service.list_action_control_assignments(**req_copy)

    def test_list_action_control_assignments_value_error_with_retries(self):
        # Enable retries and run test_list_action_control_assignments_value_error.
        _service.enable_retries()
        self.test_list_action_control_assignments_value_error()

        # Disable retries and run test_list_action_control_assignments_value_error.
        _service.disable_retries()
        self.test_list_action_control_assignments_value_error()

    @responses.activate
    def test_list_action_control_assignments_with_pager_get_next(self):
        """
        test_list_action_control_assignments_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/action_control_assignments')
        mock_response1 = '{"next":{"start":"1"},"assignments":[{"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","operation":"create","resources":[{"target":{"type":"Account","id":"id"},"action_control":{"resource_created":{"id":"id"},"error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"template":{"id":"id","version":"version"},"target":{"type":"Account","id":"id"},"status":"accepted"}],"total_count":2,"limit":1}'
        mock_response2 = '{"assignments":[{"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","operation":"create","resources":[{"target":{"type":"Account","id":"id"},"action_control":{"resource_created":{"id":"id"},"error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"template":{"id":"id","version":"version"},"target":{"type":"Account","id":"id"},"status":"accepted"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ActionControlAssignmentsPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            template_id='testString',
            template_version='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_action_control_assignments_with_pager_get_all(self):
        """
        test_list_action_control_assignments_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/action_control_assignments')
        mock_response1 = '{"next":{"start":"1"},"assignments":[{"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","operation":"create","resources":[{"target":{"type":"Account","id":"id"},"action_control":{"resource_created":{"id":"id"},"error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"template":{"id":"id","version":"version"},"target":{"type":"Account","id":"id"},"status":"accepted"}],"total_count":2,"limit":1}'
        mock_response2 = '{"assignments":[{"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","operation":"create","resources":[{"target":{"type":"Account","id":"id"},"action_control":{"resource_created":{"id":"id"},"error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"template":{"id":"id","version":"version"},"target":{"type":"Account","id":"id"},"status":"accepted"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ActionControlAssignmentsPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            template_id='testString',
            template_version='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateActionControlTemplateAssignment:
    """
    Test Class for create_action_control_template_assignment
    """

    @responses.activate
    def test_create_action_control_template_assignment_all_params(self):
        """
        create_action_control_template_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssignmentTargetDetails model
        assignment_target_details_model = {}
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a dict representation of a ActionControlAssignmentTemplate model
        action_control_assignment_template_model = {}
        action_control_assignment_template_model['id'] = 'testString'
        action_control_assignment_template_model['version'] = 'testString'

        # Set up parameter values
        target = assignment_target_details_model
        templates = [action_control_assignment_template_model]
        accept_language = 'default'

        # Invoke method
        response = _service.create_action_control_template_assignment(
            target,
            templates,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['target'] == assignment_target_details_model
        assert req_body['templates'] == [action_control_assignment_template_model]

    def test_create_action_control_template_assignment_all_params_with_retries(self):
        # Enable retries and run test_create_action_control_template_assignment_all_params.
        _service.enable_retries()
        self.test_create_action_control_template_assignment_all_params()

        # Disable retries and run test_create_action_control_template_assignment_all_params.
        _service.disable_retries()
        self.test_create_action_control_template_assignment_all_params()

    @responses.activate
    def test_create_action_control_template_assignment_required_params(self):
        """
        test_create_action_control_template_assignment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssignmentTargetDetails model
        assignment_target_details_model = {}
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a dict representation of a ActionControlAssignmentTemplate model
        action_control_assignment_template_model = {}
        action_control_assignment_template_model['id'] = 'testString'
        action_control_assignment_template_model['version'] = 'testString'

        # Set up parameter values
        target = assignment_target_details_model
        templates = [action_control_assignment_template_model]

        # Invoke method
        response = _service.create_action_control_template_assignment(
            target,
            templates,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['target'] == assignment_target_details_model
        assert req_body['templates'] == [action_control_assignment_template_model]

    def test_create_action_control_template_assignment_required_params_with_retries(self):
        # Enable retries and run test_create_action_control_template_assignment_required_params.
        _service.enable_retries()
        self.test_create_action_control_template_assignment_required_params()

        # Disable retries and run test_create_action_control_template_assignment_required_params.
        _service.disable_retries()
        self.test_create_action_control_template_assignment_required_params()

    @responses.activate
    def test_create_action_control_template_assignment_value_error(self):
        """
        test_create_action_control_template_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssignmentTargetDetails model
        assignment_target_details_model = {}
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a dict representation of a ActionControlAssignmentTemplate model
        action_control_assignment_template_model = {}
        action_control_assignment_template_model['id'] = 'testString'
        action_control_assignment_template_model['version'] = 'testString'

        # Set up parameter values
        target = assignment_target_details_model
        templates = [action_control_assignment_template_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "target": target,
            "templates": templates,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_action_control_template_assignment(**req_copy)

    def test_create_action_control_template_assignment_value_error_with_retries(self):
        # Enable retries and run test_create_action_control_template_assignment_value_error.
        _service.enable_retries()
        self.test_create_action_control_template_assignment_value_error()

        # Disable retries and run test_create_action_control_template_assignment_value_error.
        _service.disable_retries()
        self.test_create_action_control_template_assignment_value_error()


class TestGetActionControlAssignment:
    """
    Test Class for get_action_control_assignment
    """

    @responses.activate
    def test_get_action_control_assignment_all_params(self):
        """
        get_action_control_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}'
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
        response = _service.get_action_control_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_action_control_assignment_all_params_with_retries(self):
        # Enable retries and run test_get_action_control_assignment_all_params.
        _service.enable_retries()
        self.test_get_action_control_assignment_all_params()

        # Disable retries and run test_get_action_control_assignment_all_params.
        _service.disable_retries()
        self.test_get_action_control_assignment_all_params()

    @responses.activate
    def test_get_action_control_assignment_value_error(self):
        """
        test_get_action_control_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}'
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
                _service.get_action_control_assignment(**req_copy)

    def test_get_action_control_assignment_value_error_with_retries(self):
        # Enable retries and run test_get_action_control_assignment_value_error.
        _service.enable_retries()
        self.test_get_action_control_assignment_value_error()

        # Disable retries and run test_get_action_control_assignment_value_error.
        _service.disable_retries()
        self.test_get_action_control_assignment_value_error()


class TestUpdateActionControlAssignment:
    """
    Test Class for update_action_control_assignment
    """

    @responses.activate
    def test_update_action_control_assignment_all_params(self):
        """
        update_action_control_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        if_match = 'testString'
        template_version = 'testString'

        # Invoke method
        response = _service.update_action_control_assignment(
            assignment_id,
            if_match,
            template_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['template_version'] == 'testString'

    def test_update_action_control_assignment_all_params_with_retries(self):
        # Enable retries and run test_update_action_control_assignment_all_params.
        _service.enable_retries()
        self.test_update_action_control_assignment_all_params()

        # Disable retries and run test_update_action_control_assignment_all_params.
        _service.disable_retries()
        self.test_update_action_control_assignment_all_params()

    @responses.activate
    def test_update_action_control_assignment_value_error(self):
        """
        test_update_action_control_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "action_control": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        if_match = 'testString'
        template_version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assignment_id": assignment_id,
            "if_match": if_match,
            "template_version": template_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_action_control_assignment(**req_copy)

    def test_update_action_control_assignment_value_error_with_retries(self):
        # Enable retries and run test_update_action_control_assignment_value_error.
        _service.enable_retries()
        self.test_update_action_control_assignment_value_error()

        # Disable retries and run test_update_action_control_assignment_value_error.
        _service.disable_retries()
        self.test_update_action_control_assignment_value_error()


class TestDeleteActionControlAssignment:
    """
    Test Class for delete_action_control_assignment
    """

    @responses.activate
    def test_delete_action_control_assignment_all_params(self):
        """
        delete_action_control_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        assignment_id = 'testString'

        # Invoke method
        response = _service.delete_action_control_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_action_control_assignment_all_params_with_retries(self):
        # Enable retries and run test_delete_action_control_assignment_all_params.
        _service.enable_retries()
        self.test_delete_action_control_assignment_all_params()

        # Disable retries and run test_delete_action_control_assignment_all_params.
        _service.disable_retries()
        self.test_delete_action_control_assignment_all_params()

    @responses.activate
    def test_delete_action_control_assignment_value_error(self):
        """
        test_delete_action_control_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/action_control_assignments/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
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
                _service.delete_action_control_assignment(**req_copy)

    def test_delete_action_control_assignment_value_error_with_retries(self):
        # Enable retries and run test_delete_action_control_assignment_value_error.
        _service.enable_retries()
        self.test_delete_action_control_assignment_value_error()

        # Disable retries and run test_delete_action_control_assignment_value_error.
        _service.disable_retries()
        self.test_delete_action_control_assignment_value_error()


# endregion
##############################################################################
# End of Service: ActionControlAssignments
##############################################################################

##############################################################################
# Start of Service: RoleTemplates
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


class TestListRoleTemplates:
    """
    Test Class for list_role_templates
    """

    @responses.activate
    def test_list_role_templates_all_params(self):
        """
        list_role_templates()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "role_templates": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
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
        name = 'testString'
        role_name = 'testString'
        role_service_name = 'testString'
        state = 'active'
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_role_templates(
            account_id,
            accept_language=accept_language,
            name=name,
            role_name=role_name,
            role_service_name=role_service_name,
            state=state,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'role_name={}'.format(role_name) in query_string
        assert 'role_service_name={}'.format(role_service_name) in query_string
        assert 'state={}'.format(state) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_role_templates_all_params_with_retries(self):
        # Enable retries and run test_list_role_templates_all_params.
        _service.enable_retries()
        self.test_list_role_templates_all_params()

        # Disable retries and run test_list_role_templates_all_params.
        _service.disable_retries()
        self.test_list_role_templates_all_params()

    @responses.activate
    def test_list_role_templates_required_params(self):
        """
        test_list_role_templates_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "role_templates": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
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
        response = _service.list_role_templates(
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

    def test_list_role_templates_required_params_with_retries(self):
        # Enable retries and run test_list_role_templates_required_params.
        _service.enable_retries()
        self.test_list_role_templates_required_params()

        # Disable retries and run test_list_role_templates_required_params.
        _service.disable_retries()
        self.test_list_role_templates_required_params()

    @responses.activate
    def test_list_role_templates_value_error(self):
        """
        test_list_role_templates_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "role_templates": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
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
                _service.list_role_templates(**req_copy)

    def test_list_role_templates_value_error_with_retries(self):
        # Enable retries and run test_list_role_templates_value_error.
        _service.enable_retries()
        self.test_list_role_templates_value_error()

        # Disable retries and run test_list_role_templates_value_error.
        _service.disable_retries()
        self.test_list_role_templates_value_error()

    @responses.activate
    def test_list_role_templates_with_pager_get_next(self):
        """
        test_list_role_templates_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/role_templates')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"role_templates":[{"name":"name","description":"description","account_id":"account_id","committed":false,"role":{"name":"name","display_name":"display_name","service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"role_templates":[{"name":"name","description":"description","account_id":"account_id","committed":false,"role":{"name":"name","display_name":"display_name","service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = RoleTemplatesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            name='testString',
            role_name='testString',
            role_service_name='testString',
            state='active',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_role_templates_with_pager_get_all(self):
        """
        test_list_role_templates_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/role_templates')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"role_templates":[{"name":"name","description":"description","account_id":"account_id","committed":false,"role":{"name":"name","display_name":"display_name","service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"role_templates":[{"name":"name","description":"description","account_id":"account_id","committed":false,"role":{"name":"name","display_name":"display_name","service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = RoleTemplatesPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            name='testString',
            role_name='testString',
            role_service_name='testString',
            state='active',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateRoleTemplate:
    """
    Test Class for create_role_template
    """

    @responses.activate
    def test_create_role_template_all_params(self):
        """
        create_role_template()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a RoleTemplatePrototypeRole model
        role_template_prototype_role_model = {}
        role_template_prototype_role_model['name'] = 'testString'
        role_template_prototype_role_model['display_name'] = 'testString'
        role_template_prototype_role_model['service_name'] = 'testString'
        role_template_prototype_role_model['description'] = 'testString'
        role_template_prototype_role_model['actions'] = ['testString']

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        description = 'testString'
        committed = True
        role = role_template_prototype_role_model
        accept_language = 'default'

        # Invoke method
        response = _service.create_role_template(
            name,
            account_id,
            description=description,
            committed=committed,
            role=role,
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
        assert req_body['description'] == 'testString'
        assert req_body['committed'] == True
        assert req_body['role'] == role_template_prototype_role_model

    def test_create_role_template_all_params_with_retries(self):
        # Enable retries and run test_create_role_template_all_params.
        _service.enable_retries()
        self.test_create_role_template_all_params()

        # Disable retries and run test_create_role_template_all_params.
        _service.disable_retries()
        self.test_create_role_template_all_params()

    @responses.activate
    def test_create_role_template_required_params(self):
        """
        test_create_role_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a RoleTemplatePrototypeRole model
        role_template_prototype_role_model = {}
        role_template_prototype_role_model['name'] = 'testString'
        role_template_prototype_role_model['display_name'] = 'testString'
        role_template_prototype_role_model['service_name'] = 'testString'
        role_template_prototype_role_model['description'] = 'testString'
        role_template_prototype_role_model['actions'] = ['testString']

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        description = 'testString'
        committed = True
        role = role_template_prototype_role_model

        # Invoke method
        response = _service.create_role_template(
            name,
            account_id,
            description=description,
            committed=committed,
            role=role,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['committed'] == True
        assert req_body['role'] == role_template_prototype_role_model

    def test_create_role_template_required_params_with_retries(self):
        # Enable retries and run test_create_role_template_required_params.
        _service.enable_retries()
        self.test_create_role_template_required_params()

        # Disable retries and run test_create_role_template_required_params.
        _service.disable_retries()
        self.test_create_role_template_required_params()

    @responses.activate
    def test_create_role_template_value_error(self):
        """
        test_create_role_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a RoleTemplatePrototypeRole model
        role_template_prototype_role_model = {}
        role_template_prototype_role_model['name'] = 'testString'
        role_template_prototype_role_model['display_name'] = 'testString'
        role_template_prototype_role_model['service_name'] = 'testString'
        role_template_prototype_role_model['description'] = 'testString'
        role_template_prototype_role_model['actions'] = ['testString']

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        description = 'testString'
        committed = True
        role = role_template_prototype_role_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_role_template(**req_copy)

    def test_create_role_template_value_error_with_retries(self):
        # Enable retries and run test_create_role_template_value_error.
        _service.enable_retries()
        self.test_create_role_template_value_error()

        # Disable retries and run test_create_role_template_value_error.
        _service.disable_retries()
        self.test_create_role_template_value_error()


class TestGetRoleTemplate:
    """
    Test Class for get_role_template
    """

    @responses.activate
    def test_get_role_template_all_params(self):
        """
        get_role_template()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_template_id = 'testString'
        state = 'active'

        # Invoke method
        response = _service.get_role_template(
            role_template_id,
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

    def test_get_role_template_all_params_with_retries(self):
        # Enable retries and run test_get_role_template_all_params.
        _service.enable_retries()
        self.test_get_role_template_all_params()

        # Disable retries and run test_get_role_template_all_params.
        _service.disable_retries()
        self.test_get_role_template_all_params()

    @responses.activate
    def test_get_role_template_required_params(self):
        """
        test_get_role_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_template_id = 'testString'

        # Invoke method
        response = _service.get_role_template(
            role_template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_role_template_required_params_with_retries(self):
        # Enable retries and run test_get_role_template_required_params.
        _service.enable_retries()
        self.test_get_role_template_required_params()

        # Disable retries and run test_get_role_template_required_params.
        _service.disable_retries()
        self.test_get_role_template_required_params()

    @responses.activate
    def test_get_role_template_value_error(self):
        """
        test_get_role_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_template_id": role_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_role_template(**req_copy)

    def test_get_role_template_value_error_with_retries(self):
        # Enable retries and run test_get_role_template_value_error.
        _service.enable_retries()
        self.test_get_role_template_value_error()

        # Disable retries and run test_get_role_template_value_error.
        _service.disable_retries()
        self.test_get_role_template_value_error()


class TestDeleteRoleTemplate:
    """
    Test Class for delete_role_template
    """

    @responses.activate
    def test_delete_role_template_all_params(self):
        """
        delete_role_template()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        role_template_id = 'testString'

        # Invoke method
        response = _service.delete_role_template(
            role_template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_role_template_all_params_with_retries(self):
        # Enable retries and run test_delete_role_template_all_params.
        _service.enable_retries()
        self.test_delete_role_template_all_params()

        # Disable retries and run test_delete_role_template_all_params.
        _service.disable_retries()
        self.test_delete_role_template_all_params()

    @responses.activate
    def test_delete_role_template_value_error(self):
        """
        test_delete_role_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        role_template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_template_id": role_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_role_template(**req_copy)

    def test_delete_role_template_value_error_with_retries(self):
        # Enable retries and run test_delete_role_template_value_error.
        _service.enable_retries()
        self.test_delete_role_template_value_error()

        # Disable retries and run test_delete_role_template_value_error.
        _service.disable_retries()
        self.test_delete_role_template_value_error()


class TestCreateRoleTemplateVersion:
    """
    Test Class for create_role_template_version
    """

    @responses.activate
    def test_create_role_template_version_all_params(self):
        """
        create_role_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a TemplateRole model
        template_role_model = {}
        template_role_model['display_name'] = 'testString'
        template_role_model['service_name'] = 'testString'
        template_role_model['description'] = 'testString'
        template_role_model['actions'] = ['testString']

        # Set up parameter values
        role_template_id = 'testString'
        name = 'testString'
        description = 'testString'
        role = template_role_model
        committed = True

        # Invoke method
        response = _service.create_role_template_version(
            role_template_id,
            name=name,
            description=description,
            role=role,
            committed=committed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['role'] == template_role_model
        assert req_body['committed'] == True

    def test_create_role_template_version_all_params_with_retries(self):
        # Enable retries and run test_create_role_template_version_all_params.
        _service.enable_retries()
        self.test_create_role_template_version_all_params()

        # Disable retries and run test_create_role_template_version_all_params.
        _service.disable_retries()
        self.test_create_role_template_version_all_params()

    @responses.activate
    def test_create_role_template_version_value_error(self):
        """
        test_create_role_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a TemplateRole model
        template_role_model = {}
        template_role_model['display_name'] = 'testString'
        template_role_model['service_name'] = 'testString'
        template_role_model['description'] = 'testString'
        template_role_model['actions'] = ['testString']

        # Set up parameter values
        role_template_id = 'testString'
        name = 'testString'
        description = 'testString'
        role = template_role_model
        committed = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_template_id": role_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_role_template_version(**req_copy)

    def test_create_role_template_version_value_error_with_retries(self):
        # Enable retries and run test_create_role_template_version_value_error.
        _service.enable_retries()
        self.test_create_role_template_version_value_error()

        # Disable retries and run test_create_role_template_version_value_error.
        _service.disable_retries()
        self.test_create_role_template_version_value_error()


class TestListRoleTemplateVersions:
    """
    Test Class for list_role_template_versions
    """

    @responses.activate
    def test_list_role_template_versions_all_params(self):
        """
        list_role_template_versions()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_template_id = 'testString'
        state = 'active'
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_role_template_versions(
            role_template_id,
            state=state,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'state={}'.format(state) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_role_template_versions_all_params_with_retries(self):
        # Enable retries and run test_list_role_template_versions_all_params.
        _service.enable_retries()
        self.test_list_role_template_versions_all_params()

        # Disable retries and run test_list_role_template_versions_all_params.
        _service.disable_retries()
        self.test_list_role_template_versions_all_params()

    @responses.activate
    def test_list_role_template_versions_required_params(self):
        """
        test_list_role_template_versions_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_template_id = 'testString'

        # Invoke method
        response = _service.list_role_template_versions(
            role_template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_role_template_versions_required_params_with_retries(self):
        # Enable retries and run test_list_role_template_versions_required_params.
        _service.enable_retries()
        self.test_list_role_template_versions_required_params()

        # Disable retries and run test_list_role_template_versions_required_params.
        _service.disable_retries()
        self.test_list_role_template_versions_required_params()

    @responses.activate
    def test_list_role_template_versions_value_error(self):
        """
        test_list_role_template_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_template_id": role_template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_role_template_versions(**req_copy)

    def test_list_role_template_versions_value_error_with_retries(self):
        # Enable retries and run test_list_role_template_versions_value_error.
        _service.enable_retries()
        self.test_list_role_template_versions_value_error()

        # Disable retries and run test_list_role_template_versions_value_error.
        _service.disable_retries()
        self.test_list_role_template_versions_value_error()

    @responses.activate
    def test_list_role_template_versions_with_pager_get_next(self):
        """
        test_list_role_template_versions_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/role_templates/testString/versions')
        mock_response1 = '{"next":{"start":"1"},"versions":[{"name":"name","description":"description","account_id":"account_id","committed":false,"role":{"name":"name","display_name":"display_name","service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}],"total_count":2,"limit":1}'
        mock_response2 = '{"versions":[{"name":"name","description":"description","account_id":"account_id","committed":false,"role":{"name":"name","display_name":"display_name","service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = RoleTemplateVersionsPager(
            client=_service,
            role_template_id='testString',
            state='active',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_role_template_versions_with_pager_get_all(self):
        """
        test_list_role_template_versions_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/role_templates/testString/versions')
        mock_response1 = '{"next":{"start":"1"},"versions":[{"name":"name","description":"description","account_id":"account_id","committed":false,"role":{"name":"name","display_name":"display_name","service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}],"total_count":2,"limit":1}'
        mock_response2 = '{"versions":[{"name":"name","description":"description","account_id":"account_id","committed":false,"role":{"name":"name","display_name":"display_name","service_name":"service_name","description":"description","actions":["actions"]},"id":"id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","version":"version","state":"active"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = RoleTemplateVersionsPager(
            client=_service,
            role_template_id='testString',
            state='active',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestReplaceRoleTemplate:
    """
    Test Class for replace_role_template
    """

    @responses.activate
    def test_replace_role_template_all_params(self):
        """
        replace_role_template()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a TemplateRole model
        template_role_model = {}
        template_role_model['display_name'] = 'testString'
        template_role_model['service_name'] = 'testString'
        template_role_model['description'] = 'testString'
        template_role_model['actions'] = ['testString']

        # Set up parameter values
        role_template_id = 'testString'
        version = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'
        role = template_role_model
        committed = True

        # Invoke method
        response = _service.replace_role_template(
            role_template_id,
            version,
            if_match,
            name=name,
            description=description,
            role=role,
            committed=committed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['role'] == template_role_model
        assert req_body['committed'] == True

    def test_replace_role_template_all_params_with_retries(self):
        # Enable retries and run test_replace_role_template_all_params.
        _service.enable_retries()
        self.test_replace_role_template_all_params()

        # Disable retries and run test_replace_role_template_all_params.
        _service.disable_retries()
        self.test_replace_role_template_all_params()

    @responses.activate
    def test_replace_role_template_value_error(self):
        """
        test_replace_role_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a TemplateRole model
        template_role_model = {}
        template_role_model['display_name'] = 'testString'
        template_role_model['service_name'] = 'testString'
        template_role_model['description'] = 'testString'
        template_role_model['actions'] = ['testString']

        # Set up parameter values
        role_template_id = 'testString'
        version = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'
        role = template_role_model
        committed = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_template_id": role_template_id,
            "version": version,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_role_template(**req_copy)

    def test_replace_role_template_value_error_with_retries(self):
        # Enable retries and run test_replace_role_template_value_error.
        _service.enable_retries()
        self.test_replace_role_template_value_error()

        # Disable retries and run test_replace_role_template_value_error.
        _service.disable_retries()
        self.test_replace_role_template_value_error()


class TestDeleteRoleTemplateVersion:
    """
    Test Class for delete_role_template_version
    """

    @responses.activate
    def test_delete_role_template_version_all_params(self):
        """
        delete_role_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        role_template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.delete_role_template_version(
            role_template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_role_template_version_all_params_with_retries(self):
        # Enable retries and run test_delete_role_template_version_all_params.
        _service.enable_retries()
        self.test_delete_role_template_version_all_params()

        # Disable retries and run test_delete_role_template_version_all_params.
        _service.disable_retries()
        self.test_delete_role_template_version_all_params()

    @responses.activate
    def test_delete_role_template_version_value_error(self):
        """
        test_delete_role_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        role_template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_template_id": role_template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_role_template_version(**req_copy)

    def test_delete_role_template_version_value_error_with_retries(self):
        # Enable retries and run test_delete_role_template_version_value_error.
        _service.enable_retries()
        self.test_delete_role_template_version_value_error()

        # Disable retries and run test_delete_role_template_version_value_error.
        _service.disable_retries()
        self.test_delete_role_template_version_value_error()


class TestGetRoleTemplateVersion:
    """
    Test Class for get_role_template_version
    """

    @responses.activate
    def test_get_role_template_version_all_params(self):
        """
        get_role_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.get_role_template_version(
            role_template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_role_template_version_all_params_with_retries(self):
        # Enable retries and run test_get_role_template_version_all_params.
        _service.enable_retries()
        self.test_get_role_template_version_all_params()

        # Disable retries and run test_get_role_template_version_all_params.
        _service.disable_retries()
        self.test_get_role_template_version_all_params()

    @responses.activate
    def test_get_role_template_version_value_error(self):
        """
        test_get_role_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions/testString')
        mock_response = '{"name": "name", "description": "description", "account_id": "account_id", "committed": false, "role": {"name": "name", "display_name": "display_name", "service_name": "service_name", "description": "description", "actions": ["actions"]}, "id": "id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "version": "version", "state": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        role_template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_template_id": role_template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_role_template_version(**req_copy)

    def test_get_role_template_version_value_error_with_retries(self):
        # Enable retries and run test_get_role_template_version_value_error.
        _service.enable_retries()
        self.test_get_role_template_version_value_error()

        # Disable retries and run test_get_role_template_version_value_error.
        _service.disable_retries()
        self.test_get_role_template_version_value_error()


class TestCommitRoleTemplate:
    """
    Test Class for commit_role_template
    """

    @responses.activate
    def test_commit_role_template_all_params(self):
        """
        commit_role_template()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        role_template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.commit_role_template(
            role_template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_commit_role_template_all_params_with_retries(self):
        # Enable retries and run test_commit_role_template_all_params.
        _service.enable_retries()
        self.test_commit_role_template_all_params()

        # Disable retries and run test_commit_role_template_all_params.
        _service.disable_retries()
        self.test_commit_role_template_all_params()

    @responses.activate
    def test_commit_role_template_value_error(self):
        """
        test_commit_role_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        role_template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_template_id": role_template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.commit_role_template(**req_copy)

    def test_commit_role_template_value_error_with_retries(self):
        # Enable retries and run test_commit_role_template_value_error.
        _service.enable_retries()
        self.test_commit_role_template_value_error()

        # Disable retries and run test_commit_role_template_value_error.
        _service.disable_retries()
        self.test_commit_role_template_value_error()


# endregion
##############################################################################
# End of Service: RoleTemplates
##############################################################################

##############################################################################
# Start of Service: RoleAssignments
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


class TestListRoleAssignments:
    """
    Test Class for list_role_assignments
    """

    @responses.activate
    def test_list_role_assignments_all_params(self):
        """
        list_role_assignments()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
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
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_role_assignments(
            account_id,
            accept_language=accept_language,
            template_id=template_id,
            template_version=template_version,
            limit=limit,
            start=start,
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
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_role_assignments_all_params_with_retries(self):
        # Enable retries and run test_list_role_assignments_all_params.
        _service.enable_retries()
        self.test_list_role_assignments_all_params()

        # Disable retries and run test_list_role_assignments_all_params.
        _service.disable_retries()
        self.test_list_role_assignments_all_params()

    @responses.activate
    def test_list_role_assignments_required_params(self):
        """
        test_list_role_assignments_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
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
        response = _service.list_role_assignments(
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

    def test_list_role_assignments_required_params_with_retries(self):
        # Enable retries and run test_list_role_assignments_required_params.
        _service.enable_retries()
        self.test_list_role_assignments_required_params()

        # Disable retries and run test_list_role_assignments_required_params.
        _service.disable_retries()
        self.test_list_role_assignments_required_params()

    @responses.activate
    def test_list_role_assignments_value_error(self):
        """
        test_list_role_assignments_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
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
                _service.list_role_assignments(**req_copy)

    def test_list_role_assignments_value_error_with_retries(self):
        # Enable retries and run test_list_role_assignments_value_error.
        _service.enable_retries()
        self.test_list_role_assignments_value_error()

        # Disable retries and run test_list_role_assignments_value_error.
        _service.disable_retries()
        self.test_list_role_assignments_value_error()

    @responses.activate
    def test_list_role_assignments_with_pager_get_next(self):
        """
        test_list_role_assignments_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/role_assignments')
        mock_response1 = '{"next":{"start":"1"},"assignments":[{"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","operation":"create","resources":[{"target":{"type":"Account","id":"id"},"role":{"resource_created":{"id":"id"},"error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"template":{"id":"id","version":"version"},"target":{"type":"Account","id":"id"},"status":"accepted"}],"total_count":2,"limit":1}'
        mock_response2 = '{"assignments":[{"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","operation":"create","resources":[{"target":{"type":"Account","id":"id"},"role":{"resource_created":{"id":"id"},"error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"template":{"id":"id","version":"version"},"target":{"type":"Account","id":"id"},"status":"accepted"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = RoleAssignmentsPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            template_id='testString',
            template_version='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_role_assignments_with_pager_get_all(self):
        """
        test_list_role_assignments_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/role_assignments')
        mock_response1 = '{"next":{"start":"1"},"assignments":[{"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","operation":"create","resources":[{"target":{"type":"Account","id":"id"},"role":{"resource_created":{"id":"id"},"error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"template":{"id":"id","version":"version"},"target":{"type":"Account","id":"id"},"status":"accepted"}],"total_count":2,"limit":1}'
        mock_response2 = '{"assignments":[{"id":"id","account_id":"account_id","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","operation":"create","resources":[{"target":{"type":"Account","id":"id"},"role":{"resource_created":{"id":"id"},"error_message":{"name":"name","errorCode":"error_code","message":"message","code":"code","errors":[{"code":"insufficent_permissions","message":"message","details":{"conflicts_with":{"etag":"etag","role":"role","policy":"policy"}},"more_info":"more_info"}]}}}],"template":{"id":"id","version":"version"},"target":{"type":"Account","id":"id"},"status":"accepted"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = RoleAssignmentsPager(
            client=_service,
            account_id='testString',
            accept_language='default',
            template_id='testString',
            template_version='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateRoleTemplateAssignment:
    """
    Test Class for create_role_template_assignment
    """

    @responses.activate
    def test_create_role_template_assignment_all_params(self):
        """
        create_role_template_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssignmentTargetDetails model
        assignment_target_details_model = {}
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a dict representation of a RoleAssignmentTemplate model
        role_assignment_template_model = {}
        role_assignment_template_model['id'] = 'testString'
        role_assignment_template_model['version'] = 'testString'

        # Set up parameter values
        target = assignment_target_details_model
        templates = [role_assignment_template_model]
        accept_language = 'default'

        # Invoke method
        response = _service.create_role_template_assignment(
            target,
            templates,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['target'] == assignment_target_details_model
        assert req_body['templates'] == [role_assignment_template_model]

    def test_create_role_template_assignment_all_params_with_retries(self):
        # Enable retries and run test_create_role_template_assignment_all_params.
        _service.enable_retries()
        self.test_create_role_template_assignment_all_params()

        # Disable retries and run test_create_role_template_assignment_all_params.
        _service.disable_retries()
        self.test_create_role_template_assignment_all_params()

    @responses.activate
    def test_create_role_template_assignment_required_params(self):
        """
        test_create_role_template_assignment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssignmentTargetDetails model
        assignment_target_details_model = {}
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a dict representation of a RoleAssignmentTemplate model
        role_assignment_template_model = {}
        role_assignment_template_model['id'] = 'testString'
        role_assignment_template_model['version'] = 'testString'

        # Set up parameter values
        target = assignment_target_details_model
        templates = [role_assignment_template_model]

        # Invoke method
        response = _service.create_role_template_assignment(
            target,
            templates,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['target'] == assignment_target_details_model
        assert req_body['templates'] == [role_assignment_template_model]

    def test_create_role_template_assignment_required_params_with_retries(self):
        # Enable retries and run test_create_role_template_assignment_required_params.
        _service.enable_retries()
        self.test_create_role_template_assignment_required_params()

        # Disable retries and run test_create_role_template_assignment_required_params.
        _service.disable_retries()
        self.test_create_role_template_assignment_required_params()

    @responses.activate
    def test_create_role_template_assignment_value_error(self):
        """
        test_create_role_template_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments')
        mock_response = '{"limit": 1, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "assignments": [{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssignmentTargetDetails model
        assignment_target_details_model = {}
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a dict representation of a RoleAssignmentTemplate model
        role_assignment_template_model = {}
        role_assignment_template_model['id'] = 'testString'
        role_assignment_template_model['version'] = 'testString'

        # Set up parameter values
        target = assignment_target_details_model
        templates = [role_assignment_template_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "target": target,
            "templates": templates,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_role_template_assignment(**req_copy)

    def test_create_role_template_assignment_value_error_with_retries(self):
        # Enable retries and run test_create_role_template_assignment_value_error.
        _service.enable_retries()
        self.test_create_role_template_assignment_value_error()

        # Disable retries and run test_create_role_template_assignment_value_error.
        _service.disable_retries()
        self.test_create_role_template_assignment_value_error()


class TestGetRoleAssignment:
    """
    Test Class for get_role_assignment
    """

    @responses.activate
    def test_get_role_assignment_all_params(self):
        """
        get_role_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}'
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
        response = _service.get_role_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_role_assignment_all_params_with_retries(self):
        # Enable retries and run test_get_role_assignment_all_params.
        _service.enable_retries()
        self.test_get_role_assignment_all_params()

        # Disable retries and run test_get_role_assignment_all_params.
        _service.disable_retries()
        self.test_get_role_assignment_all_params()

    @responses.activate
    def test_get_role_assignment_value_error(self):
        """
        test_get_role_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}'
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
                _service.get_role_assignment(**req_copy)

    def test_get_role_assignment_value_error_with_retries(self):
        # Enable retries and run test_get_role_assignment_value_error.
        _service.enable_retries()
        self.test_get_role_assignment_value_error()

        # Disable retries and run test_get_role_assignment_value_error.
        _service.disable_retries()
        self.test_get_role_assignment_value_error()


class TestUpdateRoleAssignment:
    """
    Test Class for update_role_assignment
    """

    @responses.activate
    def test_update_role_assignment_all_params(self):
        """
        update_role_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        if_match = 'testString'
        template_version = 'testString'

        # Invoke method
        response = _service.update_role_assignment(
            assignment_id,
            if_match,
            template_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['template_version'] == 'testString'

    def test_update_role_assignment_all_params_with_retries(self):
        # Enable retries and run test_update_role_assignment_all_params.
        _service.enable_retries()
        self.test_update_role_assignment_all_params()

        # Disable retries and run test_update_role_assignment_all_params.
        _service.disable_retries()
        self.test_update_role_assignment_all_params()

    @responses.activate
    def test_update_role_assignment_value_error(self):
        """
        test_update_role_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "operation": "create", "resources": [{"target": {"type": "Account", "id": "id"}, "role": {"resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "code": "code", "errors": [{"code": "insufficent_permissions", "message": "message", "details": {"conflicts_with": {"etag": "etag", "role": "role", "policy": "policy"}}, "more_info": "more_info"}]}}}], "template": {"id": "id", "version": "version"}, "target": {"type": "Account", "id": "id"}, "status": "accepted"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        if_match = 'testString'
        template_version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assignment_id": assignment_id,
            "if_match": if_match,
            "template_version": template_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_role_assignment(**req_copy)

    def test_update_role_assignment_value_error_with_retries(self):
        # Enable retries and run test_update_role_assignment_value_error.
        _service.enable_retries()
        self.test_update_role_assignment_value_error()

        # Disable retries and run test_update_role_assignment_value_error.
        _service.disable_retries()
        self.test_update_role_assignment_value_error()


class TestDeleteRoleAssignment:
    """
    Test Class for delete_role_assignment
    """

    @responses.activate
    def test_delete_role_assignment_all_params(self):
        """
        delete_role_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        assignment_id = 'testString'

        # Invoke method
        response = _service.delete_role_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_role_assignment_all_params_with_retries(self):
        # Enable retries and run test_delete_role_assignment_all_params.
        _service.enable_retries()
        self.test_delete_role_assignment_all_params()

        # Disable retries and run test_delete_role_assignment_all_params.
        _service.disable_retries()
        self.test_delete_role_assignment_all_params()

    @responses.activate
    def test_delete_role_assignment_value_error(self):
        """
        test_delete_role_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/role_assignments/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
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
                _service.delete_role_assignment(**req_copy)

    def test_delete_role_assignment_value_error_with_retries(self):
        # Enable retries and run test_delete_role_assignment_value_error.
        _service.enable_retries()
        self.test_delete_role_assignment_value_error()

        # Disable retries and run test_delete_role_assignment_value_error.
        _service.disable_retries()
        self.test_delete_role_assignment_value_error()


# endregion
##############################################################################
# End of Service: RoleAssignments
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AccountSettingsAccessManagement:
    """
    Test Class for AccountSettingsAccessManagement
    """

    def test_account_settings_access_management_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsAccessManagement
        """

        # Construct dict forms of any model objects needed in order to build this model.

        identity_types_base_model = {}  # IdentityTypesBase
        identity_types_base_model['state'] = 'enabled'
        identity_types_base_model['external_allowed_accounts'] = ['testString']

        identity_types_model = {}  # IdentityTypes
        identity_types_model['user'] = identity_types_base_model
        identity_types_model['service_id'] = identity_types_base_model
        identity_types_model['service'] = identity_types_base_model

        external_account_identity_interaction_model = {}  # ExternalAccountIdentityInteraction
        external_account_identity_interaction_model['identity_types'] = identity_types_model

        # Construct a json representation of a AccountSettingsAccessManagement model
        account_settings_access_management_model_json = {}
        account_settings_access_management_model_json['external_account_identity_interaction'] = (
            external_account_identity_interaction_model
        )

        # Construct a model instance of AccountSettingsAccessManagement by calling from_dict on the json representation
        account_settings_access_management_model = AccountSettingsAccessManagement.from_dict(
            account_settings_access_management_model_json
        )
        assert account_settings_access_management_model != False

        # Construct a model instance of AccountSettingsAccessManagement by calling from_dict on the json representation
        account_settings_access_management_model_dict = AccountSettingsAccessManagement.from_dict(
            account_settings_access_management_model_json
        ).__dict__
        account_settings_access_management_model2 = AccountSettingsAccessManagement(
            **account_settings_access_management_model_dict
        )

        # Verify the model instances are equivalent
        assert account_settings_access_management_model == account_settings_access_management_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_access_management_model_json2 = account_settings_access_management_model.to_dict()
        assert account_settings_access_management_model_json2 == account_settings_access_management_model_json


class TestModel_ActionControlAssignment:
    """
    Test Class for ActionControlAssignment
    """

    def test_action_control_assignment_serialization(self):
        """
        Test serialization/deserialization for ActionControlAssignment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        action_control_assignment_template_model = {}  # ActionControlAssignmentTemplate
        action_control_assignment_template_model['id'] = 'testString'
        action_control_assignment_template_model['version'] = 'testString'

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a json representation of a ActionControlAssignment model
        action_control_assignment_model_json = {}
        action_control_assignment_model_json['template'] = action_control_assignment_template_model
        action_control_assignment_model_json['target'] = assignment_target_details_model

        # Construct a model instance of ActionControlAssignment by calling from_dict on the json representation
        action_control_assignment_model = ActionControlAssignment.from_dict(action_control_assignment_model_json)
        assert action_control_assignment_model != False

        # Construct a model instance of ActionControlAssignment by calling from_dict on the json representation
        action_control_assignment_model_dict = ActionControlAssignment.from_dict(
            action_control_assignment_model_json
        ).__dict__
        action_control_assignment_model2 = ActionControlAssignment(**action_control_assignment_model_dict)

        # Verify the model instances are equivalent
        assert action_control_assignment_model == action_control_assignment_model2

        # Convert model instance back to dict and verify no loss of data
        action_control_assignment_model_json2 = action_control_assignment_model.to_dict()
        assert action_control_assignment_model_json2 == action_control_assignment_model_json


class TestModel_ActionControlAssignmentCollection:
    """
    Test Class for ActionControlAssignmentCollection
    """

    def test_action_control_assignment_collection_serialization(self):
        """
        Test serialization/deserialization for ActionControlAssignmentCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

        action_control_assignment_template_model = {}  # ActionControlAssignmentTemplate
        action_control_assignment_template_model['id'] = 'testString'
        action_control_assignment_template_model['version'] = 'testString'

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        action_control_assignment_model = {}  # ActionControlAssignment
        action_control_assignment_model['template'] = action_control_assignment_template_model
        action_control_assignment_model['target'] = assignment_target_details_model

        # Construct a json representation of a ActionControlAssignmentCollection model
        action_control_assignment_collection_model_json = {}
        action_control_assignment_collection_model_json['limit'] = 1
        action_control_assignment_collection_model_json['first'] = first_model
        action_control_assignment_collection_model_json['next'] = next_model
        action_control_assignment_collection_model_json['previous'] = previous_model
        action_control_assignment_collection_model_json['assignments'] = [action_control_assignment_model]

        # Construct a model instance of ActionControlAssignmentCollection by calling from_dict on the json representation
        action_control_assignment_collection_model = ActionControlAssignmentCollection.from_dict(
            action_control_assignment_collection_model_json
        )
        assert action_control_assignment_collection_model != False

        # Construct a model instance of ActionControlAssignmentCollection by calling from_dict on the json representation
        action_control_assignment_collection_model_dict = ActionControlAssignmentCollection.from_dict(
            action_control_assignment_collection_model_json
        ).__dict__
        action_control_assignment_collection_model2 = ActionControlAssignmentCollection(
            **action_control_assignment_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert action_control_assignment_collection_model == action_control_assignment_collection_model2

        # Convert model instance back to dict and verify no loss of data
        action_control_assignment_collection_model_json2 = action_control_assignment_collection_model.to_dict()
        assert action_control_assignment_collection_model_json2 == action_control_assignment_collection_model_json


class TestModel_ActionControlAssignmentResource:
    """
    Test Class for ActionControlAssignmentResource
    """

    def test_action_control_assignment_resource_serialization(self):
        """
        Test serialization/deserialization for ActionControlAssignmentResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        action_control_assignment_resource_created_model = {}  # ActionControlAssignmentResourceCreated
        action_control_assignment_resource_created_model['id'] = 'testString'

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        action_control_assignment_resource_action_control_model = {}  # ActionControlAssignmentResourceActionControl
        action_control_assignment_resource_action_control_model['resource_created'] = (
            action_control_assignment_resource_created_model
        )
        action_control_assignment_resource_action_control_model['error_message'] = assignment_resource_error_model

        # Construct a json representation of a ActionControlAssignmentResource model
        action_control_assignment_resource_model_json = {}
        action_control_assignment_resource_model_json['target'] = assignment_target_details_model
        action_control_assignment_resource_model_json['action_control'] = (
            action_control_assignment_resource_action_control_model
        )

        # Construct a model instance of ActionControlAssignmentResource by calling from_dict on the json representation
        action_control_assignment_resource_model = ActionControlAssignmentResource.from_dict(
            action_control_assignment_resource_model_json
        )
        assert action_control_assignment_resource_model != False

        # Construct a model instance of ActionControlAssignmentResource by calling from_dict on the json representation
        action_control_assignment_resource_model_dict = ActionControlAssignmentResource.from_dict(
            action_control_assignment_resource_model_json
        ).__dict__
        action_control_assignment_resource_model2 = ActionControlAssignmentResource(
            **action_control_assignment_resource_model_dict
        )

        # Verify the model instances are equivalent
        assert action_control_assignment_resource_model == action_control_assignment_resource_model2

        # Convert model instance back to dict and verify no loss of data
        action_control_assignment_resource_model_json2 = action_control_assignment_resource_model.to_dict()
        assert action_control_assignment_resource_model_json2 == action_control_assignment_resource_model_json


class TestModel_ActionControlAssignmentResourceActionControl:
    """
    Test Class for ActionControlAssignmentResourceActionControl
    """

    def test_action_control_assignment_resource_action_control_serialization(self):
        """
        Test serialization/deserialization for ActionControlAssignmentResourceActionControl
        """

        # Construct dict forms of any model objects needed in order to build this model.

        action_control_assignment_resource_created_model = {}  # ActionControlAssignmentResourceCreated
        action_control_assignment_resource_created_model['id'] = 'testString'

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        # Construct a json representation of a ActionControlAssignmentResourceActionControl model
        action_control_assignment_resource_action_control_model_json = {}
        action_control_assignment_resource_action_control_model_json['resource_created'] = (
            action_control_assignment_resource_created_model
        )
        action_control_assignment_resource_action_control_model_json['error_message'] = assignment_resource_error_model

        # Construct a model instance of ActionControlAssignmentResourceActionControl by calling from_dict on the json representation
        action_control_assignment_resource_action_control_model = (
            ActionControlAssignmentResourceActionControl.from_dict(
                action_control_assignment_resource_action_control_model_json
            )
        )
        assert action_control_assignment_resource_action_control_model != False

        # Construct a model instance of ActionControlAssignmentResourceActionControl by calling from_dict on the json representation
        action_control_assignment_resource_action_control_model_dict = (
            ActionControlAssignmentResourceActionControl.from_dict(
                action_control_assignment_resource_action_control_model_json
            ).__dict__
        )
        action_control_assignment_resource_action_control_model2 = ActionControlAssignmentResourceActionControl(
            **action_control_assignment_resource_action_control_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            action_control_assignment_resource_action_control_model
            == action_control_assignment_resource_action_control_model2
        )

        # Convert model instance back to dict and verify no loss of data
        action_control_assignment_resource_action_control_model_json2 = (
            action_control_assignment_resource_action_control_model.to_dict()
        )
        assert (
            action_control_assignment_resource_action_control_model_json2
            == action_control_assignment_resource_action_control_model_json
        )


class TestModel_ActionControlAssignmentResourceCreated:
    """
    Test Class for ActionControlAssignmentResourceCreated
    """

    def test_action_control_assignment_resource_created_serialization(self):
        """
        Test serialization/deserialization for ActionControlAssignmentResourceCreated
        """

        # Construct a json representation of a ActionControlAssignmentResourceCreated model
        action_control_assignment_resource_created_model_json = {}
        action_control_assignment_resource_created_model_json['id'] = 'testString'

        # Construct a model instance of ActionControlAssignmentResourceCreated by calling from_dict on the json representation
        action_control_assignment_resource_created_model = ActionControlAssignmentResourceCreated.from_dict(
            action_control_assignment_resource_created_model_json
        )
        assert action_control_assignment_resource_created_model != False

        # Construct a model instance of ActionControlAssignmentResourceCreated by calling from_dict on the json representation
        action_control_assignment_resource_created_model_dict = ActionControlAssignmentResourceCreated.from_dict(
            action_control_assignment_resource_created_model_json
        ).__dict__
        action_control_assignment_resource_created_model2 = ActionControlAssignmentResourceCreated(
            **action_control_assignment_resource_created_model_dict
        )

        # Verify the model instances are equivalent
        assert action_control_assignment_resource_created_model == action_control_assignment_resource_created_model2

        # Convert model instance back to dict and verify no loss of data
        action_control_assignment_resource_created_model_json2 = (
            action_control_assignment_resource_created_model.to_dict()
        )
        assert (
            action_control_assignment_resource_created_model_json2
            == action_control_assignment_resource_created_model_json
        )


class TestModel_ActionControlAssignmentTemplate:
    """
    Test Class for ActionControlAssignmentTemplate
    """

    def test_action_control_assignment_template_serialization(self):
        """
        Test serialization/deserialization for ActionControlAssignmentTemplate
        """

        # Construct a json representation of a ActionControlAssignmentTemplate model
        action_control_assignment_template_model_json = {}
        action_control_assignment_template_model_json['id'] = 'testString'
        action_control_assignment_template_model_json['version'] = 'testString'

        # Construct a model instance of ActionControlAssignmentTemplate by calling from_dict on the json representation
        action_control_assignment_template_model = ActionControlAssignmentTemplate.from_dict(
            action_control_assignment_template_model_json
        )
        assert action_control_assignment_template_model != False

        # Construct a model instance of ActionControlAssignmentTemplate by calling from_dict on the json representation
        action_control_assignment_template_model_dict = ActionControlAssignmentTemplate.from_dict(
            action_control_assignment_template_model_json
        ).__dict__
        action_control_assignment_template_model2 = ActionControlAssignmentTemplate(
            **action_control_assignment_template_model_dict
        )

        # Verify the model instances are equivalent
        assert action_control_assignment_template_model == action_control_assignment_template_model2

        # Convert model instance back to dict and verify no loss of data
        action_control_assignment_template_model_json2 = action_control_assignment_template_model.to_dict()
        assert action_control_assignment_template_model_json2 == action_control_assignment_template_model_json


class TestModel_ActionControlTemplate:
    """
    Test Class for ActionControlTemplate
    """

    def test_action_control_template_serialization(self):
        """
        Test serialization/deserialization for ActionControlTemplate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        template_action_control_model = {}  # TemplateActionControl
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        # Construct a json representation of a ActionControlTemplate model
        action_control_template_model_json = {}
        action_control_template_model_json['name'] = 'testString'
        action_control_template_model_json['description'] = 'testString'
        action_control_template_model_json['account_id'] = 'testString'
        action_control_template_model_json['committed'] = True
        action_control_template_model_json['action_control'] = template_action_control_model
        action_control_template_model_json['version'] = 'testString'
        action_control_template_model_json['state'] = 'active'

        # Construct a model instance of ActionControlTemplate by calling from_dict on the json representation
        action_control_template_model = ActionControlTemplate.from_dict(action_control_template_model_json)
        assert action_control_template_model != False

        # Construct a model instance of ActionControlTemplate by calling from_dict on the json representation
        action_control_template_model_dict = ActionControlTemplate.from_dict(
            action_control_template_model_json
        ).__dict__
        action_control_template_model2 = ActionControlTemplate(**action_control_template_model_dict)

        # Verify the model instances are equivalent
        assert action_control_template_model == action_control_template_model2

        # Convert model instance back to dict and verify no loss of data
        action_control_template_model_json2 = action_control_template_model.to_dict()
        assert action_control_template_model_json2 == action_control_template_model_json


class TestModel_ActionControlTemplateCollection:
    """
    Test Class for ActionControlTemplateCollection
    """

    def test_action_control_template_collection_serialization(self):
        """
        Test serialization/deserialization for ActionControlTemplateCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

        template_action_control_model = {}  # TemplateActionControl
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        action_control_template_model = {}  # ActionControlTemplate
        action_control_template_model['name'] = 'testString'
        action_control_template_model['description'] = 'testString'
        action_control_template_model['account_id'] = 'testString'
        action_control_template_model['committed'] = True
        action_control_template_model['action_control'] = template_action_control_model
        action_control_template_model['version'] = 'testString'
        action_control_template_model['state'] = 'active'

        # Construct a json representation of a ActionControlTemplateCollection model
        action_control_template_collection_model_json = {}
        action_control_template_collection_model_json['limit'] = 1
        action_control_template_collection_model_json['first'] = first_model
        action_control_template_collection_model_json['next'] = next_model
        action_control_template_collection_model_json['previous'] = previous_model
        action_control_template_collection_model_json['action_control_templates'] = [action_control_template_model]

        # Construct a model instance of ActionControlTemplateCollection by calling from_dict on the json representation
        action_control_template_collection_model = ActionControlTemplateCollection.from_dict(
            action_control_template_collection_model_json
        )
        assert action_control_template_collection_model != False

        # Construct a model instance of ActionControlTemplateCollection by calling from_dict on the json representation
        action_control_template_collection_model_dict = ActionControlTemplateCollection.from_dict(
            action_control_template_collection_model_json
        ).__dict__
        action_control_template_collection_model2 = ActionControlTemplateCollection(
            **action_control_template_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert action_control_template_collection_model == action_control_template_collection_model2

        # Convert model instance back to dict and verify no loss of data
        action_control_template_collection_model_json2 = action_control_template_collection_model.to_dict()
        assert action_control_template_collection_model_json2 == action_control_template_collection_model_json


class TestModel_ActionControlTemplateVersionsCollection:
    """
    Test Class for ActionControlTemplateVersionsCollection
    """

    def test_action_control_template_versions_collection_serialization(self):
        """
        Test serialization/deserialization for ActionControlTemplateVersionsCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

        template_action_control_model = {}  # TemplateActionControl
        template_action_control_model['service_name'] = 'testString'
        template_action_control_model['description'] = 'testString'
        template_action_control_model['actions'] = ['testString']

        action_control_template_model = {}  # ActionControlTemplate
        action_control_template_model['name'] = 'testString'
        action_control_template_model['description'] = 'testString'
        action_control_template_model['account_id'] = 'testString'
        action_control_template_model['committed'] = True
        action_control_template_model['action_control'] = template_action_control_model
        action_control_template_model['version'] = 'testString'
        action_control_template_model['state'] = 'active'

        # Construct a json representation of a ActionControlTemplateVersionsCollection model
        action_control_template_versions_collection_model_json = {}
        action_control_template_versions_collection_model_json['limit'] = 1
        action_control_template_versions_collection_model_json['first'] = first_model
        action_control_template_versions_collection_model_json['next'] = next_model
        action_control_template_versions_collection_model_json['previous'] = previous_model
        action_control_template_versions_collection_model_json['versions'] = [action_control_template_model]

        # Construct a model instance of ActionControlTemplateVersionsCollection by calling from_dict on the json representation
        action_control_template_versions_collection_model = ActionControlTemplateVersionsCollection.from_dict(
            action_control_template_versions_collection_model_json
        )
        assert action_control_template_versions_collection_model != False

        # Construct a model instance of ActionControlTemplateVersionsCollection by calling from_dict on the json representation
        action_control_template_versions_collection_model_dict = ActionControlTemplateVersionsCollection.from_dict(
            action_control_template_versions_collection_model_json
        ).__dict__
        action_control_template_versions_collection_model2 = ActionControlTemplateVersionsCollection(
            **action_control_template_versions_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert action_control_template_versions_collection_model == action_control_template_versions_collection_model2

        # Convert model instance back to dict and verify no loss of data
        action_control_template_versions_collection_model_json2 = (
            action_control_template_versions_collection_model.to_dict()
        )
        assert (
            action_control_template_versions_collection_model_json2
            == action_control_template_versions_collection_model_json
        )


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
        assignment_resource_created_model_dict = AssignmentResourceCreated.from_dict(
            assignment_resource_created_model_json
        ).__dict__
        assignment_resource_created_model2 = AssignmentResourceCreated(**assignment_resource_created_model_dict)

        # Verify the model instances are equivalent
        assert assignment_resource_created_model == assignment_resource_created_model2

        # Convert model instance back to dict and verify no loss of data
        assignment_resource_created_model_json2 = assignment_resource_created_model.to_dict()
        assert assignment_resource_created_model_json2 == assignment_resource_created_model_json


class TestModel_AssignmentResourceError:
    """
    Test Class for AssignmentResourceError
    """

    def test_assignment_resource_error_serialization(self):
        """
        Test serialization/deserialization for AssignmentResourceError
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

        # Construct a json representation of a AssignmentResourceError model
        assignment_resource_error_model_json = {}
        assignment_resource_error_model_json['name'] = 'testString'
        assignment_resource_error_model_json['errorCode'] = 'testString'
        assignment_resource_error_model_json['message'] = 'testString'
        assignment_resource_error_model_json['code'] = 'testString'
        assignment_resource_error_model_json['errors'] = [error_object_model]

        # Construct a model instance of AssignmentResourceError by calling from_dict on the json representation
        assignment_resource_error_model = AssignmentResourceError.from_dict(assignment_resource_error_model_json)
        assert assignment_resource_error_model != False

        # Construct a model instance of AssignmentResourceError by calling from_dict on the json representation
        assignment_resource_error_model_dict = AssignmentResourceError.from_dict(
            assignment_resource_error_model_json
        ).__dict__
        assignment_resource_error_model2 = AssignmentResourceError(**assignment_resource_error_model_dict)

        # Verify the model instances are equivalent
        assert assignment_resource_error_model == assignment_resource_error_model2

        # Convert model instance back to dict and verify no loss of data
        assignment_resource_error_model_json2 = assignment_resource_error_model.to_dict()
        assert assignment_resource_error_model_json2 == assignment_resource_error_model_json


class TestModel_AssignmentTargetDetails:
    """
    Test Class for AssignmentTargetDetails
    """

    def test_assignment_target_details_serialization(self):
        """
        Test serialization/deserialization for AssignmentTargetDetails
        """

        # Construct a json representation of a AssignmentTargetDetails model
        assignment_target_details_model_json = {}
        assignment_target_details_model_json['type'] = 'Account'
        assignment_target_details_model_json['id'] = 'testString'

        # Construct a model instance of AssignmentTargetDetails by calling from_dict on the json representation
        assignment_target_details_model = AssignmentTargetDetails.from_dict(assignment_target_details_model_json)
        assert assignment_target_details_model != False

        # Construct a model instance of AssignmentTargetDetails by calling from_dict on the json representation
        assignment_target_details_model_dict = AssignmentTargetDetails.from_dict(
            assignment_target_details_model_json
        ).__dict__
        assignment_target_details_model2 = AssignmentTargetDetails(**assignment_target_details_model_dict)

        # Verify the model instances are equivalent
        assert assignment_target_details_model == assignment_target_details_model2

        # Convert model instance back to dict and verify no loss of data
        assignment_target_details_model_json2 = assignment_target_details_model.to_dict()
        assert assignment_target_details_model_json2 == assignment_target_details_model_json


class TestModel_AssignmentTemplateDetails:
    """
    Test Class for AssignmentTemplateDetails
    """

    def test_assignment_template_details_serialization(self):
        """
        Test serialization/deserialization for AssignmentTemplateDetails
        """

        # Construct a json representation of a AssignmentTemplateDetails model
        assignment_template_details_model_json = {}
        assignment_template_details_model_json['id'] = 'testString'
        assignment_template_details_model_json['version'] = 'testString'

        # Construct a model instance of AssignmentTemplateDetails by calling from_dict on the json representation
        assignment_template_details_model = AssignmentTemplateDetails.from_dict(assignment_template_details_model_json)
        assert assignment_template_details_model != False

        # Construct a model instance of AssignmentTemplateDetails by calling from_dict on the json representation
        assignment_template_details_model_dict = AssignmentTemplateDetails.from_dict(
            assignment_template_details_model_json
        ).__dict__
        assignment_template_details_model2 = AssignmentTemplateDetails(**assignment_template_details_model_dict)

        # Verify the model instances are equivalent
        assert assignment_template_details_model == assignment_template_details_model2

        # Convert model instance back to dict and verify no loss of data
        assignment_template_details_model_json2 = assignment_template_details_model.to_dict()
        assert assignment_template_details_model_json2 == assignment_template_details_model_json


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


class TestModel_ExternalAccountIdentityInteraction:
    """
    Test Class for ExternalAccountIdentityInteraction
    """

    def test_external_account_identity_interaction_serialization(self):
        """
        Test serialization/deserialization for ExternalAccountIdentityInteraction
        """

        # Construct dict forms of any model objects needed in order to build this model.

        identity_types_base_model = {}  # IdentityTypesBase
        identity_types_base_model['state'] = 'enabled'
        identity_types_base_model['external_allowed_accounts'] = ['testString']

        identity_types_model = {}  # IdentityTypes
        identity_types_model['user'] = identity_types_base_model
        identity_types_model['service_id'] = identity_types_base_model
        identity_types_model['service'] = identity_types_base_model

        # Construct a json representation of a ExternalAccountIdentityInteraction model
        external_account_identity_interaction_model_json = {}
        external_account_identity_interaction_model_json['identity_types'] = identity_types_model

        # Construct a model instance of ExternalAccountIdentityInteraction by calling from_dict on the json representation
        external_account_identity_interaction_model = ExternalAccountIdentityInteraction.from_dict(
            external_account_identity_interaction_model_json
        )
        assert external_account_identity_interaction_model != False

        # Construct a model instance of ExternalAccountIdentityInteraction by calling from_dict on the json representation
        external_account_identity_interaction_model_dict = ExternalAccountIdentityInteraction.from_dict(
            external_account_identity_interaction_model_json
        ).__dict__
        external_account_identity_interaction_model2 = ExternalAccountIdentityInteraction(
            **external_account_identity_interaction_model_dict
        )

        # Verify the model instances are equivalent
        assert external_account_identity_interaction_model == external_account_identity_interaction_model2

        # Convert model instance back to dict and verify no loss of data
        external_account_identity_interaction_model_json2 = external_account_identity_interaction_model.to_dict()
        assert external_account_identity_interaction_model_json2 == external_account_identity_interaction_model_json


class TestModel_ExternalAccountIdentityInteractionPatch:
    """
    Test Class for ExternalAccountIdentityInteractionPatch
    """

    def test_external_account_identity_interaction_patch_serialization(self):
        """
        Test serialization/deserialization for ExternalAccountIdentityInteractionPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        identity_types_base_model = {}  # IdentityTypesBase
        identity_types_base_model['state'] = 'enabled'
        identity_types_base_model['external_allowed_accounts'] = ['testString']

        identity_types_patch_model = {}  # IdentityTypesPatch
        identity_types_patch_model['user'] = identity_types_base_model
        identity_types_patch_model['service_id'] = identity_types_base_model
        identity_types_patch_model['service'] = identity_types_base_model

        # Construct a json representation of a ExternalAccountIdentityInteractionPatch model
        external_account_identity_interaction_patch_model_json = {}
        external_account_identity_interaction_patch_model_json['identity_types'] = identity_types_patch_model

        # Construct a model instance of ExternalAccountIdentityInteractionPatch by calling from_dict on the json representation
        external_account_identity_interaction_patch_model = ExternalAccountIdentityInteractionPatch.from_dict(
            external_account_identity_interaction_patch_model_json
        )
        assert external_account_identity_interaction_patch_model != False

        # Construct a model instance of ExternalAccountIdentityInteractionPatch by calling from_dict on the json representation
        external_account_identity_interaction_patch_model_dict = ExternalAccountIdentityInteractionPatch.from_dict(
            external_account_identity_interaction_patch_model_json
        ).__dict__
        external_account_identity_interaction_patch_model2 = ExternalAccountIdentityInteractionPatch(
            **external_account_identity_interaction_patch_model_dict
        )

        # Verify the model instances are equivalent
        assert external_account_identity_interaction_patch_model == external_account_identity_interaction_patch_model2

        # Convert model instance back to dict and verify no loss of data
        external_account_identity_interaction_patch_model_json2 = (
            external_account_identity_interaction_patch_model.to_dict()
        )
        assert (
            external_account_identity_interaction_patch_model_json2
            == external_account_identity_interaction_patch_model_json
        )


class TestModel_First:
    """
    Test Class for First
    """

    def test_first_serialization(self):
        """
        Test serialization/deserialization for First
        """

        # Construct a json representation of a First model
        first_model_json = {}

        # Construct a model instance of First by calling from_dict on the json representation
        first_model = First.from_dict(first_model_json)
        assert first_model != False

        # Construct a model instance of First by calling from_dict on the json representation
        first_model_dict = First.from_dict(first_model_json).__dict__
        first_model2 = First(**first_model_dict)

        # Verify the model instances are equivalent
        assert first_model == first_model2

        # Convert model instance back to dict and verify no loss of data
        first_model_json2 = first_model.to_dict()
        assert first_model_json2 == first_model_json


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
        grant_with_enriched_roles_model_dict = GrantWithEnrichedRoles.from_dict(
            grant_with_enriched_roles_model_json
        ).__dict__
        grant_with_enriched_roles_model2 = GrantWithEnrichedRoles(**grant_with_enriched_roles_model_dict)

        # Verify the model instances are equivalent
        assert grant_with_enriched_roles_model == grant_with_enriched_roles_model2

        # Convert model instance back to dict and verify no loss of data
        grant_with_enriched_roles_model_json2 = grant_with_enriched_roles_model.to_dict()
        assert grant_with_enriched_roles_model_json2 == grant_with_enriched_roles_model_json


class TestModel_IdentityTypes:
    """
    Test Class for IdentityTypes
    """

    def test_identity_types_serialization(self):
        """
        Test serialization/deserialization for IdentityTypes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        identity_types_base_model = {}  # IdentityTypesBase
        identity_types_base_model['state'] = 'enabled'
        identity_types_base_model['external_allowed_accounts'] = ['testString']

        # Construct a json representation of a IdentityTypes model
        identity_types_model_json = {}
        identity_types_model_json['user'] = identity_types_base_model
        identity_types_model_json['service_id'] = identity_types_base_model
        identity_types_model_json['service'] = identity_types_base_model

        # Construct a model instance of IdentityTypes by calling from_dict on the json representation
        identity_types_model = IdentityTypes.from_dict(identity_types_model_json)
        assert identity_types_model != False

        # Construct a model instance of IdentityTypes by calling from_dict on the json representation
        identity_types_model_dict = IdentityTypes.from_dict(identity_types_model_json).__dict__
        identity_types_model2 = IdentityTypes(**identity_types_model_dict)

        # Verify the model instances are equivalent
        assert identity_types_model == identity_types_model2

        # Convert model instance back to dict and verify no loss of data
        identity_types_model_json2 = identity_types_model.to_dict()
        assert identity_types_model_json2 == identity_types_model_json


class TestModel_IdentityTypesBase:
    """
    Test Class for IdentityTypesBase
    """

    def test_identity_types_base_serialization(self):
        """
        Test serialization/deserialization for IdentityTypesBase
        """

        # Construct a json representation of a IdentityTypesBase model
        identity_types_base_model_json = {}
        identity_types_base_model_json['state'] = 'enabled'
        identity_types_base_model_json['external_allowed_accounts'] = ['testString']

        # Construct a model instance of IdentityTypesBase by calling from_dict on the json representation
        identity_types_base_model = IdentityTypesBase.from_dict(identity_types_base_model_json)
        assert identity_types_base_model != False

        # Construct a model instance of IdentityTypesBase by calling from_dict on the json representation
        identity_types_base_model_dict = IdentityTypesBase.from_dict(identity_types_base_model_json).__dict__
        identity_types_base_model2 = IdentityTypesBase(**identity_types_base_model_dict)

        # Verify the model instances are equivalent
        assert identity_types_base_model == identity_types_base_model2

        # Convert model instance back to dict and verify no loss of data
        identity_types_base_model_json2 = identity_types_base_model.to_dict()
        assert identity_types_base_model_json2 == identity_types_base_model_json


class TestModel_IdentityTypesPatch:
    """
    Test Class for IdentityTypesPatch
    """

    def test_identity_types_patch_serialization(self):
        """
        Test serialization/deserialization for IdentityTypesPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        identity_types_base_model = {}  # IdentityTypesBase
        identity_types_base_model['state'] = 'enabled'
        identity_types_base_model['external_allowed_accounts'] = ['testString']

        # Construct a json representation of a IdentityTypesPatch model
        identity_types_patch_model_json = {}
        identity_types_patch_model_json['user'] = identity_types_base_model
        identity_types_patch_model_json['service_id'] = identity_types_base_model
        identity_types_patch_model_json['service'] = identity_types_base_model

        # Construct a model instance of IdentityTypesPatch by calling from_dict on the json representation
        identity_types_patch_model = IdentityTypesPatch.from_dict(identity_types_patch_model_json)
        assert identity_types_patch_model != False

        # Construct a model instance of IdentityTypesPatch by calling from_dict on the json representation
        identity_types_patch_model_dict = IdentityTypesPatch.from_dict(identity_types_patch_model_json).__dict__
        identity_types_patch_model2 = IdentityTypesPatch(**identity_types_patch_model_dict)

        # Verify the model instances are equivalent
        assert identity_types_patch_model == identity_types_patch_model2

        # Convert model instance back to dict and verify no loss of data
        identity_types_patch_model_json2 = identity_types_patch_model.to_dict()
        assert identity_types_patch_model_json2 == identity_types_patch_model_json


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


class TestModel_Next:
    """
    Test Class for Next
    """

    def test_next_serialization(self):
        """
        Test serialization/deserialization for Next
        """

        # Construct a json representation of a Next model
        next_model_json = {}
        next_model_json['start'] = 'testString'

        # Construct a model instance of Next by calling from_dict on the json representation
        next_model = Next.from_dict(next_model_json)
        assert next_model != False

        # Construct a model instance of Next by calling from_dict on the json representation
        next_model_dict = Next.from_dict(next_model_json).__dict__
        next_model2 = Next(**next_model_dict)

        # Verify the model instances are equivalent
        assert next_model == next_model2

        # Convert model instance back to dict and verify no loss of data
        next_model_json2 = next_model.to_dict()
        assert next_model_json2 == next_model_json


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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        # Construct a json representation of a PolicyAssignmentResourcePolicy model
        policy_assignment_resource_policy_model_json = {}
        policy_assignment_resource_policy_model_json['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model_json['status'] = 'testString'
        policy_assignment_resource_policy_model_json['error_message'] = assignment_resource_error_model

        # Construct a model instance of PolicyAssignmentResourcePolicy by calling from_dict on the json representation
        policy_assignment_resource_policy_model = PolicyAssignmentResourcePolicy.from_dict(
            policy_assignment_resource_policy_model_json
        )
        assert policy_assignment_resource_policy_model != False

        # Construct a model instance of PolicyAssignmentResourcePolicy by calling from_dict on the json representation
        policy_assignment_resource_policy_model_dict = PolicyAssignmentResourcePolicy.from_dict(
            policy_assignment_resource_policy_model_json
        ).__dict__
        policy_assignment_resource_policy_model2 = PolicyAssignmentResourcePolicy(
            **policy_assignment_resource_policy_model_dict
        )

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = assignment_resource_error_model

        # Construct a json representation of a PolicyAssignmentResources model
        policy_assignment_resources_model_json = {}
        policy_assignment_resources_model_json['target'] = 'testString'
        policy_assignment_resources_model_json['policy'] = policy_assignment_resource_policy_model

        # Construct a model instance of PolicyAssignmentResources by calling from_dict on the json representation
        policy_assignment_resources_model = PolicyAssignmentResources.from_dict(policy_assignment_resources_model_json)
        assert policy_assignment_resources_model != False

        # Construct a model instance of PolicyAssignmentResources by calling from_dict on the json representation
        policy_assignment_resources_model_dict = PolicyAssignmentResources.from_dict(
            policy_assignment_resources_model_json
        ).__dict__
        policy_assignment_resources_model2 = PolicyAssignmentResources(**policy_assignment_resources_model_dict)

        # Verify the model instances are equivalent
        assert policy_assignment_resources_model == policy_assignment_resources_model2

        # Convert model instance back to dict and verify no loss of data
        policy_assignment_resources_model_json2 = policy_assignment_resources_model.to_dict()
        assert policy_assignment_resources_model_json2 == policy_assignment_resources_model_json


class TestModel_PolicyAssignmentV1:
    """
    Test Class for PolicyAssignmentV1
    """

    def test_policy_assignment_v1_serialization(self):
        """
        Test serialization/deserialization for PolicyAssignmentV1
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = assignment_resource_error_model

        policy_assignment_v1_resources_model = {}  # PolicyAssignmentV1Resources
        policy_assignment_v1_resources_model['target'] = assignment_target_details_model
        policy_assignment_v1_resources_model['policy'] = policy_assignment_resource_policy_model

        policy_assignment_v1_subject_model = {}  # PolicyAssignmentV1Subject

        assignment_template_details_model = {}  # AssignmentTemplateDetails
        assignment_template_details_model['id'] = 'testString'
        assignment_template_details_model['version'] = 'testString'

        # Construct a json representation of a PolicyAssignmentV1 model
        policy_assignment_v1_model_json = {}
        policy_assignment_v1_model_json['target'] = assignment_target_details_model
        policy_assignment_v1_model_json['resources'] = [policy_assignment_v1_resources_model]
        policy_assignment_v1_model_json['subject'] = policy_assignment_v1_subject_model
        policy_assignment_v1_model_json['template'] = assignment_template_details_model
        policy_assignment_v1_model_json['status'] = 'in_progress'

        # Construct a model instance of PolicyAssignmentV1 by calling from_dict on the json representation
        policy_assignment_v1_model = PolicyAssignmentV1.from_dict(policy_assignment_v1_model_json)
        assert policy_assignment_v1_model != False

        # Construct a model instance of PolicyAssignmentV1 by calling from_dict on the json representation
        policy_assignment_v1_model_dict = PolicyAssignmentV1.from_dict(policy_assignment_v1_model_json).__dict__
        policy_assignment_v1_model2 = PolicyAssignmentV1(**policy_assignment_v1_model_dict)

        # Verify the model instances are equivalent
        assert policy_assignment_v1_model == policy_assignment_v1_model2

        # Convert model instance back to dict and verify no loss of data
        policy_assignment_v1_model_json2 = policy_assignment_v1_model.to_dict()
        assert policy_assignment_v1_model_json2 == policy_assignment_v1_model_json


class TestModel_PolicyAssignmentV1Collection:
    """
    Test Class for PolicyAssignmentV1Collection
    """

    def test_policy_assignment_v1_collection_serialization(self):
        """
        Test serialization/deserialization for PolicyAssignmentV1Collection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = assignment_resource_error_model

        policy_assignment_v1_resources_model = {}  # PolicyAssignmentV1Resources
        policy_assignment_v1_resources_model['target'] = assignment_target_details_model
        policy_assignment_v1_resources_model['policy'] = policy_assignment_resource_policy_model

        policy_assignment_v1_subject_model = {}  # PolicyAssignmentV1Subject

        assignment_template_details_model = {}  # AssignmentTemplateDetails
        assignment_template_details_model['id'] = 'testString'
        assignment_template_details_model['version'] = 'testString'

        policy_assignment_v1_model = {}  # PolicyAssignmentV1
        policy_assignment_v1_model['target'] = assignment_target_details_model
        policy_assignment_v1_model['resources'] = [policy_assignment_v1_resources_model]
        policy_assignment_v1_model['subject'] = policy_assignment_v1_subject_model
        policy_assignment_v1_model['template'] = assignment_template_details_model
        policy_assignment_v1_model['status'] = 'in_progress'

        # Construct a json representation of a PolicyAssignmentV1Collection model
        policy_assignment_v1_collection_model_json = {}
        policy_assignment_v1_collection_model_json['limit'] = 1
        policy_assignment_v1_collection_model_json['first'] = first_model
        policy_assignment_v1_collection_model_json['next'] = next_model
        policy_assignment_v1_collection_model_json['previous'] = previous_model
        policy_assignment_v1_collection_model_json['assignments'] = [policy_assignment_v1_model]

        # Construct a model instance of PolicyAssignmentV1Collection by calling from_dict on the json representation
        policy_assignment_v1_collection_model = PolicyAssignmentV1Collection.from_dict(
            policy_assignment_v1_collection_model_json
        )
        assert policy_assignment_v1_collection_model != False

        # Construct a model instance of PolicyAssignmentV1Collection by calling from_dict on the json representation
        policy_assignment_v1_collection_model_dict = PolicyAssignmentV1Collection.from_dict(
            policy_assignment_v1_collection_model_json
        ).__dict__
        policy_assignment_v1_collection_model2 = PolicyAssignmentV1Collection(
            **policy_assignment_v1_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert policy_assignment_v1_collection_model == policy_assignment_v1_collection_model2

        # Convert model instance back to dict and verify no loss of data
        policy_assignment_v1_collection_model_json2 = policy_assignment_v1_collection_model.to_dict()
        assert policy_assignment_v1_collection_model_json2 == policy_assignment_v1_collection_model_json


class TestModel_PolicyAssignmentV1Resources:
    """
    Test Class for PolicyAssignmentV1Resources
    """

    def test_policy_assignment_v1_resources_serialization(self):
        """
        Test serialization/deserialization for PolicyAssignmentV1Resources
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = assignment_resource_error_model

        # Construct a json representation of a PolicyAssignmentV1Resources model
        policy_assignment_v1_resources_model_json = {}
        policy_assignment_v1_resources_model_json['target'] = assignment_target_details_model
        policy_assignment_v1_resources_model_json['policy'] = policy_assignment_resource_policy_model

        # Construct a model instance of PolicyAssignmentV1Resources by calling from_dict on the json representation
        policy_assignment_v1_resources_model = PolicyAssignmentV1Resources.from_dict(
            policy_assignment_v1_resources_model_json
        )
        assert policy_assignment_v1_resources_model != False

        # Construct a model instance of PolicyAssignmentV1Resources by calling from_dict on the json representation
        policy_assignment_v1_resources_model_dict = PolicyAssignmentV1Resources.from_dict(
            policy_assignment_v1_resources_model_json
        ).__dict__
        policy_assignment_v1_resources_model2 = PolicyAssignmentV1Resources(**policy_assignment_v1_resources_model_dict)

        # Verify the model instances are equivalent
        assert policy_assignment_v1_resources_model == policy_assignment_v1_resources_model2

        # Convert model instance back to dict and verify no loss of data
        policy_assignment_v1_resources_model_json2 = policy_assignment_v1_resources_model.to_dict()
        assert policy_assignment_v1_resources_model_json2 == policy_assignment_v1_resources_model_json


class TestModel_PolicyAssignmentV1Subject:
    """
    Test Class for PolicyAssignmentV1Subject
    """

    def test_policy_assignment_v1_subject_serialization(self):
        """
        Test serialization/deserialization for PolicyAssignmentV1Subject
        """

        # Construct a json representation of a PolicyAssignmentV1Subject model
        policy_assignment_v1_subject_model_json = {}

        # Construct a model instance of PolicyAssignmentV1Subject by calling from_dict on the json representation
        policy_assignment_v1_subject_model = PolicyAssignmentV1Subject.from_dict(
            policy_assignment_v1_subject_model_json
        )
        assert policy_assignment_v1_subject_model != False

        # Construct a model instance of PolicyAssignmentV1Subject by calling from_dict on the json representation
        policy_assignment_v1_subject_model_dict = PolicyAssignmentV1Subject.from_dict(
            policy_assignment_v1_subject_model_json
        ).__dict__
        policy_assignment_v1_subject_model2 = PolicyAssignmentV1Subject(**policy_assignment_v1_subject_model_dict)

        # Verify the model instances are equivalent
        assert policy_assignment_v1_subject_model == policy_assignment_v1_subject_model2

        # Convert model instance back to dict and verify no loss of data
        policy_assignment_v1_subject_model_json2 = policy_assignment_v1_subject_model.to_dict()
        assert policy_assignment_v1_subject_model_json2 == policy_assignment_v1_subject_model_json


class TestModel_PolicyCollection:
    """
    Test Class for PolicyCollection
    """

    def test_policy_collection_serialization(self):
        """
        Test serialization/deserialization for PolicyCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

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
        policy_collection_model_json['limit'] = 1
        policy_collection_model_json['first'] = first_model
        policy_collection_model_json['next'] = next_model
        policy_collection_model_json['previous'] = previous_model
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

        v2_policy_subject_attribute_model = {}  # V2PolicySubjectAttribute
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        v2_policy_subject_model = {}  # V2PolicySubject
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        role_template_references_item_model = {}  # RoleTemplateReferencesItem
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        template_grant_model = {}  # TemplateGrant
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        template_control_model = {}  # TemplateControl
        template_control_model['grant'] = template_grant_model

        template_policy_model = {}  # TemplatePolicy
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = assignment_resource_error_model

        policy_assignment_v1_resources_model = {}  # PolicyAssignmentV1Resources
        policy_assignment_v1_resources_model['target'] = assignment_target_details_model
        policy_assignment_v1_resources_model['policy'] = policy_assignment_resource_policy_model

        policy_assignment_v1_subject_model = {}  # PolicyAssignmentV1Subject

        assignment_template_details_model = {}  # AssignmentTemplateDetails
        assignment_template_details_model['id'] = 'testString'
        assignment_template_details_model['version'] = 'testString'

        policy_template_assignment_items_model = {}  # PolicyTemplateAssignmentItemsPolicyAssignmentV1
        policy_template_assignment_items_model['target'] = assignment_target_details_model
        policy_template_assignment_items_model['resources'] = [policy_assignment_v1_resources_model]
        policy_template_assignment_items_model['subject'] = policy_assignment_v1_subject_model
        policy_template_assignment_items_model['template'] = assignment_template_details_model
        policy_template_assignment_items_model['status'] = 'in_progress'

        # Construct a json representation of a PolicyTemplateAssignmentCollection model
        policy_template_assignment_collection_model_json = {}
        policy_template_assignment_collection_model_json['limit'] = 1
        policy_template_assignment_collection_model_json['first'] = first_model
        policy_template_assignment_collection_model_json['next'] = next_model
        policy_template_assignment_collection_model_json['previous'] = previous_model
        policy_template_assignment_collection_model_json['assignments'] = [policy_template_assignment_items_model]

        # Construct a model instance of PolicyTemplateAssignmentCollection by calling from_dict on the json representation
        policy_template_assignment_collection_model = PolicyTemplateAssignmentCollection.from_dict(
            policy_template_assignment_collection_model_json
        )
        assert policy_template_assignment_collection_model != False

        # Construct a model instance of PolicyTemplateAssignmentCollection by calling from_dict on the json representation
        policy_template_assignment_collection_model_dict = PolicyTemplateAssignmentCollection.from_dict(
            policy_template_assignment_collection_model_json
        ).__dict__
        policy_template_assignment_collection_model2 = PolicyTemplateAssignmentCollection(
            **policy_template_assignment_collection_model_dict
        )

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

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

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

        v2_policy_subject_attribute_model = {}  # V2PolicySubjectAttribute
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        v2_policy_subject_model = {}  # V2PolicySubject
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        role_template_references_item_model = {}  # RoleTemplateReferencesItem
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        template_grant_model = {}  # TemplateGrant
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        template_control_model = {}  # TemplateControl
        template_control_model['grant'] = template_grant_model

        template_policy_model = {}  # TemplatePolicy
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        policy_template_collection_model_json['limit'] = 1
        policy_template_collection_model_json['first'] = first_model
        policy_template_collection_model_json['next'] = next_model
        policy_template_collection_model_json['previous'] = previous_model
        policy_template_collection_model_json['policy_templates'] = [policy_template_model]

        # Construct a model instance of PolicyTemplateCollection by calling from_dict on the json representation
        policy_template_collection_model = PolicyTemplateCollection.from_dict(policy_template_collection_model_json)
        assert policy_template_collection_model != False

        # Construct a model instance of PolicyTemplateCollection by calling from_dict on the json representation
        policy_template_collection_model_dict = PolicyTemplateCollection.from_dict(
            policy_template_collection_model_json
        ).__dict__
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

        v2_policy_subject_attribute_model = {}  # V2PolicySubjectAttribute
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        v2_policy_subject_model = {}  # V2PolicySubject
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        role_template_references_item_model = {}  # RoleTemplateReferencesItem
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        template_grant_model = {}  # TemplateGrant
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        template_control_model = {}  # TemplateControl
        template_control_model['grant'] = template_grant_model

        template_policy_model = {}  # TemplatePolicy
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        policy_template_limit_data_model_dict = PolicyTemplateLimitData.from_dict(
            policy_template_limit_data_model_json
        ).__dict__
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
        policy_template_meta_data_model_dict = PolicyTemplateMetaData.from_dict(
            policy_template_meta_data_model_json
        ).__dict__
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

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

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

        v2_policy_subject_attribute_model = {}  # V2PolicySubjectAttribute
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        v2_policy_subject_model = {}  # V2PolicySubject
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        role_template_references_item_model = {}  # RoleTemplateReferencesItem
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        template_grant_model = {}  # TemplateGrant
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        template_control_model = {}  # TemplateControl
        template_control_model['grant'] = template_grant_model

        template_policy_model = {}  # TemplatePolicy
        template_policy_model['type'] = 'access'
        template_policy_model['description'] = 'testString'
        template_policy_model['resource'] = v2_policy_resource_model
        template_policy_model['subject'] = v2_policy_subject_model
        template_policy_model['pattern'] = 'testString'
        template_policy_model['rule'] = v2_policy_rule_model
        template_policy_model['control'] = template_control_model

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
        policy_template_versions_collection_model_json['limit'] = 1
        policy_template_versions_collection_model_json['first'] = first_model
        policy_template_versions_collection_model_json['next'] = next_model
        policy_template_versions_collection_model_json['previous'] = previous_model
        policy_template_versions_collection_model_json['versions'] = [policy_template_model]

        # Construct a model instance of PolicyTemplateVersionsCollection by calling from_dict on the json representation
        policy_template_versions_collection_model = PolicyTemplateVersionsCollection.from_dict(
            policy_template_versions_collection_model_json
        )
        assert policy_template_versions_collection_model != False

        # Construct a model instance of PolicyTemplateVersionsCollection by calling from_dict on the json representation
        policy_template_versions_collection_model_dict = PolicyTemplateVersionsCollection.from_dict(
            policy_template_versions_collection_model_json
        ).__dict__
        policy_template_versions_collection_model2 = PolicyTemplateVersionsCollection(
            **policy_template_versions_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert policy_template_versions_collection_model == policy_template_versions_collection_model2

        # Convert model instance back to dict and verify no loss of data
        policy_template_versions_collection_model_json2 = policy_template_versions_collection_model.to_dict()
        assert policy_template_versions_collection_model_json2 == policy_template_versions_collection_model_json


class TestModel_Previous:
    """
    Test Class for Previous
    """

    def test_previous_serialization(self):
        """
        Test serialization/deserialization for Previous
        """

        # Construct a json representation of a Previous model
        previous_model_json = {}
        previous_model_json['start'] = 'testString'

        # Construct a model instance of Previous by calling from_dict on the json representation
        previous_model = Previous.from_dict(previous_model_json)
        assert previous_model != False

        # Construct a model instance of Previous by calling from_dict on the json representation
        previous_model_dict = Previous.from_dict(previous_model_json).__dict__
        previous_model2 = Previous(**previous_model_dict)

        # Verify the model instances are equivalent
        assert previous_model == previous_model2

        # Convert model instance back to dict and verify no loss of data
        previous_model_json2 = previous_model.to_dict()
        assert previous_model_json2 == previous_model_json


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


class TestModel_RoleAssignment:
    """
    Test Class for RoleAssignment
    """

    def test_role_assignment_serialization(self):
        """
        Test serialization/deserialization for RoleAssignment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        role_assignment_template_model = {}  # RoleAssignmentTemplate
        role_assignment_template_model['id'] = 'testString'
        role_assignment_template_model['version'] = 'testString'

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        # Construct a json representation of a RoleAssignment model
        role_assignment_model_json = {}
        role_assignment_model_json['template'] = role_assignment_template_model
        role_assignment_model_json['target'] = assignment_target_details_model

        # Construct a model instance of RoleAssignment by calling from_dict on the json representation
        role_assignment_model = RoleAssignment.from_dict(role_assignment_model_json)
        assert role_assignment_model != False

        # Construct a model instance of RoleAssignment by calling from_dict on the json representation
        role_assignment_model_dict = RoleAssignment.from_dict(role_assignment_model_json).__dict__
        role_assignment_model2 = RoleAssignment(**role_assignment_model_dict)

        # Verify the model instances are equivalent
        assert role_assignment_model == role_assignment_model2

        # Convert model instance back to dict and verify no loss of data
        role_assignment_model_json2 = role_assignment_model.to_dict()
        assert role_assignment_model_json2 == role_assignment_model_json


class TestModel_RoleAssignmentCollection:
    """
    Test Class for RoleAssignmentCollection
    """

    def test_role_assignment_collection_serialization(self):
        """
        Test serialization/deserialization for RoleAssignmentCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

        role_assignment_template_model = {}  # RoleAssignmentTemplate
        role_assignment_template_model['id'] = 'testString'
        role_assignment_template_model['version'] = 'testString'

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        role_assignment_model = {}  # RoleAssignment
        role_assignment_model['template'] = role_assignment_template_model
        role_assignment_model['target'] = assignment_target_details_model

        # Construct a json representation of a RoleAssignmentCollection model
        role_assignment_collection_model_json = {}
        role_assignment_collection_model_json['limit'] = 1
        role_assignment_collection_model_json['first'] = first_model
        role_assignment_collection_model_json['next'] = next_model
        role_assignment_collection_model_json['previous'] = previous_model
        role_assignment_collection_model_json['assignments'] = [role_assignment_model]

        # Construct a model instance of RoleAssignmentCollection by calling from_dict on the json representation
        role_assignment_collection_model = RoleAssignmentCollection.from_dict(role_assignment_collection_model_json)
        assert role_assignment_collection_model != False

        # Construct a model instance of RoleAssignmentCollection by calling from_dict on the json representation
        role_assignment_collection_model_dict = RoleAssignmentCollection.from_dict(
            role_assignment_collection_model_json
        ).__dict__
        role_assignment_collection_model2 = RoleAssignmentCollection(**role_assignment_collection_model_dict)

        # Verify the model instances are equivalent
        assert role_assignment_collection_model == role_assignment_collection_model2

        # Convert model instance back to dict and verify no loss of data
        role_assignment_collection_model_json2 = role_assignment_collection_model.to_dict()
        assert role_assignment_collection_model_json2 == role_assignment_collection_model_json


class TestModel_RoleAssignmentResource:
    """
    Test Class for RoleAssignmentResource
    """

    def test_role_assignment_resource_serialization(self):
        """
        Test serialization/deserialization for RoleAssignmentResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

        role_assignment_resource_created_model = {}  # RoleAssignmentResourceCreated
        role_assignment_resource_created_model['id'] = 'testString'

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        role_assignment_resource_role_model = {}  # RoleAssignmentResourceRole
        role_assignment_resource_role_model['resource_created'] = role_assignment_resource_created_model
        role_assignment_resource_role_model['error_message'] = assignment_resource_error_model

        # Construct a json representation of a RoleAssignmentResource model
        role_assignment_resource_model_json = {}
        role_assignment_resource_model_json['target'] = assignment_target_details_model
        role_assignment_resource_model_json['role'] = role_assignment_resource_role_model

        # Construct a model instance of RoleAssignmentResource by calling from_dict on the json representation
        role_assignment_resource_model = RoleAssignmentResource.from_dict(role_assignment_resource_model_json)
        assert role_assignment_resource_model != False

        # Construct a model instance of RoleAssignmentResource by calling from_dict on the json representation
        role_assignment_resource_model_dict = RoleAssignmentResource.from_dict(
            role_assignment_resource_model_json
        ).__dict__
        role_assignment_resource_model2 = RoleAssignmentResource(**role_assignment_resource_model_dict)

        # Verify the model instances are equivalent
        assert role_assignment_resource_model == role_assignment_resource_model2

        # Convert model instance back to dict and verify no loss of data
        role_assignment_resource_model_json2 = role_assignment_resource_model.to_dict()
        assert role_assignment_resource_model_json2 == role_assignment_resource_model_json


class TestModel_RoleAssignmentResourceCreated:
    """
    Test Class for RoleAssignmentResourceCreated
    """

    def test_role_assignment_resource_created_serialization(self):
        """
        Test serialization/deserialization for RoleAssignmentResourceCreated
        """

        # Construct a json representation of a RoleAssignmentResourceCreated model
        role_assignment_resource_created_model_json = {}
        role_assignment_resource_created_model_json['id'] = 'testString'

        # Construct a model instance of RoleAssignmentResourceCreated by calling from_dict on the json representation
        role_assignment_resource_created_model = RoleAssignmentResourceCreated.from_dict(
            role_assignment_resource_created_model_json
        )
        assert role_assignment_resource_created_model != False

        # Construct a model instance of RoleAssignmentResourceCreated by calling from_dict on the json representation
        role_assignment_resource_created_model_dict = RoleAssignmentResourceCreated.from_dict(
            role_assignment_resource_created_model_json
        ).__dict__
        role_assignment_resource_created_model2 = RoleAssignmentResourceCreated(
            **role_assignment_resource_created_model_dict
        )

        # Verify the model instances are equivalent
        assert role_assignment_resource_created_model == role_assignment_resource_created_model2

        # Convert model instance back to dict and verify no loss of data
        role_assignment_resource_created_model_json2 = role_assignment_resource_created_model.to_dict()
        assert role_assignment_resource_created_model_json2 == role_assignment_resource_created_model_json


class TestModel_RoleAssignmentResourceRole:
    """
    Test Class for RoleAssignmentResourceRole
    """

    def test_role_assignment_resource_role_serialization(self):
        """
        Test serialization/deserialization for RoleAssignmentResourceRole
        """

        # Construct dict forms of any model objects needed in order to build this model.

        role_assignment_resource_created_model = {}  # RoleAssignmentResourceCreated
        role_assignment_resource_created_model['id'] = 'testString'

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        # Construct a json representation of a RoleAssignmentResourceRole model
        role_assignment_resource_role_model_json = {}
        role_assignment_resource_role_model_json['resource_created'] = role_assignment_resource_created_model
        role_assignment_resource_role_model_json['error_message'] = assignment_resource_error_model

        # Construct a model instance of RoleAssignmentResourceRole by calling from_dict on the json representation
        role_assignment_resource_role_model = RoleAssignmentResourceRole.from_dict(
            role_assignment_resource_role_model_json
        )
        assert role_assignment_resource_role_model != False

        # Construct a model instance of RoleAssignmentResourceRole by calling from_dict on the json representation
        role_assignment_resource_role_model_dict = RoleAssignmentResourceRole.from_dict(
            role_assignment_resource_role_model_json
        ).__dict__
        role_assignment_resource_role_model2 = RoleAssignmentResourceRole(**role_assignment_resource_role_model_dict)

        # Verify the model instances are equivalent
        assert role_assignment_resource_role_model == role_assignment_resource_role_model2

        # Convert model instance back to dict and verify no loss of data
        role_assignment_resource_role_model_json2 = role_assignment_resource_role_model.to_dict()
        assert role_assignment_resource_role_model_json2 == role_assignment_resource_role_model_json


class TestModel_RoleAssignmentTemplate:
    """
    Test Class for RoleAssignmentTemplate
    """

    def test_role_assignment_template_serialization(self):
        """
        Test serialization/deserialization for RoleAssignmentTemplate
        """

        # Construct a json representation of a RoleAssignmentTemplate model
        role_assignment_template_model_json = {}
        role_assignment_template_model_json['id'] = 'testString'
        role_assignment_template_model_json['version'] = 'testString'

        # Construct a model instance of RoleAssignmentTemplate by calling from_dict on the json representation
        role_assignment_template_model = RoleAssignmentTemplate.from_dict(role_assignment_template_model_json)
        assert role_assignment_template_model != False

        # Construct a model instance of RoleAssignmentTemplate by calling from_dict on the json representation
        role_assignment_template_model_dict = RoleAssignmentTemplate.from_dict(
            role_assignment_template_model_json
        ).__dict__
        role_assignment_template_model2 = RoleAssignmentTemplate(**role_assignment_template_model_dict)

        # Verify the model instances are equivalent
        assert role_assignment_template_model == role_assignment_template_model2

        # Convert model instance back to dict and verify no loss of data
        role_assignment_template_model_json2 = role_assignment_template_model.to_dict()
        assert role_assignment_template_model_json2 == role_assignment_template_model_json


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


class TestModel_RoleTemplate:
    """
    Test Class for RoleTemplate
    """

    def test_role_template_serialization(self):
        """
        Test serialization/deserialization for RoleTemplate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        role_template_prototype_role_model = {}  # RoleTemplatePrototypeRole
        role_template_prototype_role_model['name'] = 'testString'
        role_template_prototype_role_model['display_name'] = 'testString'
        role_template_prototype_role_model['service_name'] = 'testString'
        role_template_prototype_role_model['description'] = 'testString'
        role_template_prototype_role_model['actions'] = ['testString']

        # Construct a json representation of a RoleTemplate model
        role_template_model_json = {}
        role_template_model_json['name'] = 'testString'
        role_template_model_json['description'] = 'testString'
        role_template_model_json['account_id'] = 'testString'
        role_template_model_json['committed'] = True
        role_template_model_json['role'] = role_template_prototype_role_model
        role_template_model_json['version'] = 'testString'
        role_template_model_json['state'] = 'active'

        # Construct a model instance of RoleTemplate by calling from_dict on the json representation
        role_template_model = RoleTemplate.from_dict(role_template_model_json)
        assert role_template_model != False

        # Construct a model instance of RoleTemplate by calling from_dict on the json representation
        role_template_model_dict = RoleTemplate.from_dict(role_template_model_json).__dict__
        role_template_model2 = RoleTemplate(**role_template_model_dict)

        # Verify the model instances are equivalent
        assert role_template_model == role_template_model2

        # Convert model instance back to dict and verify no loss of data
        role_template_model_json2 = role_template_model.to_dict()
        assert role_template_model_json2 == role_template_model_json


class TestModel_RoleTemplateCollection:
    """
    Test Class for RoleTemplateCollection
    """

    def test_role_template_collection_serialization(self):
        """
        Test serialization/deserialization for RoleTemplateCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

        role_template_prototype_role_model = {}  # RoleTemplatePrototypeRole
        role_template_prototype_role_model['name'] = 'testString'
        role_template_prototype_role_model['display_name'] = 'testString'
        role_template_prototype_role_model['service_name'] = 'testString'
        role_template_prototype_role_model['description'] = 'testString'
        role_template_prototype_role_model['actions'] = ['testString']

        role_template_model = {}  # RoleTemplate
        role_template_model['name'] = 'testString'
        role_template_model['description'] = 'testString'
        role_template_model['account_id'] = 'testString'
        role_template_model['committed'] = True
        role_template_model['role'] = role_template_prototype_role_model
        role_template_model['version'] = 'testString'
        role_template_model['state'] = 'active'

        # Construct a json representation of a RoleTemplateCollection model
        role_template_collection_model_json = {}
        role_template_collection_model_json['limit'] = 1
        role_template_collection_model_json['first'] = first_model
        role_template_collection_model_json['next'] = next_model
        role_template_collection_model_json['previous'] = previous_model
        role_template_collection_model_json['role_templates'] = [role_template_model]

        # Construct a model instance of RoleTemplateCollection by calling from_dict on the json representation
        role_template_collection_model = RoleTemplateCollection.from_dict(role_template_collection_model_json)
        assert role_template_collection_model != False

        # Construct a model instance of RoleTemplateCollection by calling from_dict on the json representation
        role_template_collection_model_dict = RoleTemplateCollection.from_dict(
            role_template_collection_model_json
        ).__dict__
        role_template_collection_model2 = RoleTemplateCollection(**role_template_collection_model_dict)

        # Verify the model instances are equivalent
        assert role_template_collection_model == role_template_collection_model2

        # Convert model instance back to dict and verify no loss of data
        role_template_collection_model_json2 = role_template_collection_model.to_dict()
        assert role_template_collection_model_json2 == role_template_collection_model_json


class TestModel_RoleTemplatePrototypeRole:
    """
    Test Class for RoleTemplatePrototypeRole
    """

    def test_role_template_prototype_role_serialization(self):
        """
        Test serialization/deserialization for RoleTemplatePrototypeRole
        """

        # Construct a json representation of a RoleTemplatePrototypeRole model
        role_template_prototype_role_model_json = {}
        role_template_prototype_role_model_json['name'] = 'testString'
        role_template_prototype_role_model_json['display_name'] = 'testString'
        role_template_prototype_role_model_json['service_name'] = 'testString'
        role_template_prototype_role_model_json['description'] = 'testString'
        role_template_prototype_role_model_json['actions'] = ['testString']

        # Construct a model instance of RoleTemplatePrototypeRole by calling from_dict on the json representation
        role_template_prototype_role_model = RoleTemplatePrototypeRole.from_dict(
            role_template_prototype_role_model_json
        )
        assert role_template_prototype_role_model != False

        # Construct a model instance of RoleTemplatePrototypeRole by calling from_dict on the json representation
        role_template_prototype_role_model_dict = RoleTemplatePrototypeRole.from_dict(
            role_template_prototype_role_model_json
        ).__dict__
        role_template_prototype_role_model2 = RoleTemplatePrototypeRole(**role_template_prototype_role_model_dict)

        # Verify the model instances are equivalent
        assert role_template_prototype_role_model == role_template_prototype_role_model2

        # Convert model instance back to dict and verify no loss of data
        role_template_prototype_role_model_json2 = role_template_prototype_role_model.to_dict()
        assert role_template_prototype_role_model_json2 == role_template_prototype_role_model_json


class TestModel_RoleTemplateReferencesItem:
    """
    Test Class for RoleTemplateReferencesItem
    """

    def test_role_template_references_item_serialization(self):
        """
        Test serialization/deserialization for RoleTemplateReferencesItem
        """

        # Construct a json representation of a RoleTemplateReferencesItem model
        role_template_references_item_model_json = {}
        role_template_references_item_model_json['id'] = 'testString'
        role_template_references_item_model_json['version'] = 'testString'

        # Construct a model instance of RoleTemplateReferencesItem by calling from_dict on the json representation
        role_template_references_item_model = RoleTemplateReferencesItem.from_dict(
            role_template_references_item_model_json
        )
        assert role_template_references_item_model != False

        # Construct a model instance of RoleTemplateReferencesItem by calling from_dict on the json representation
        role_template_references_item_model_dict = RoleTemplateReferencesItem.from_dict(
            role_template_references_item_model_json
        ).__dict__
        role_template_references_item_model2 = RoleTemplateReferencesItem(**role_template_references_item_model_dict)

        # Verify the model instances are equivalent
        assert role_template_references_item_model == role_template_references_item_model2

        # Convert model instance back to dict and verify no loss of data
        role_template_references_item_model_json2 = role_template_references_item_model.to_dict()
        assert role_template_references_item_model_json2 == role_template_references_item_model_json


class TestModel_RoleTemplateVersionsCollection:
    """
    Test Class for RoleTemplateVersionsCollection
    """

    def test_role_template_versions_collection_serialization(self):
        """
        Test serialization/deserialization for RoleTemplateVersionsCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

        role_template_prototype_role_model = {}  # RoleTemplatePrototypeRole
        role_template_prototype_role_model['name'] = 'testString'
        role_template_prototype_role_model['display_name'] = 'testString'
        role_template_prototype_role_model['service_name'] = 'testString'
        role_template_prototype_role_model['description'] = 'testString'
        role_template_prototype_role_model['actions'] = ['testString']

        role_template_model = {}  # RoleTemplate
        role_template_model['name'] = 'testString'
        role_template_model['description'] = 'testString'
        role_template_model['account_id'] = 'testString'
        role_template_model['committed'] = True
        role_template_model['role'] = role_template_prototype_role_model
        role_template_model['version'] = 'testString'
        role_template_model['state'] = 'active'

        # Construct a json representation of a RoleTemplateVersionsCollection model
        role_template_versions_collection_model_json = {}
        role_template_versions_collection_model_json['limit'] = 1
        role_template_versions_collection_model_json['first'] = first_model
        role_template_versions_collection_model_json['next'] = next_model
        role_template_versions_collection_model_json['previous'] = previous_model
        role_template_versions_collection_model_json['versions'] = [role_template_model]

        # Construct a model instance of RoleTemplateVersionsCollection by calling from_dict on the json representation
        role_template_versions_collection_model = RoleTemplateVersionsCollection.from_dict(
            role_template_versions_collection_model_json
        )
        assert role_template_versions_collection_model != False

        # Construct a model instance of RoleTemplateVersionsCollection by calling from_dict on the json representation
        role_template_versions_collection_model_dict = RoleTemplateVersionsCollection.from_dict(
            role_template_versions_collection_model_json
        ).__dict__
        role_template_versions_collection_model2 = RoleTemplateVersionsCollection(
            **role_template_versions_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert role_template_versions_collection_model == role_template_versions_collection_model2

        # Convert model instance back to dict and verify no loss of data
        role_template_versions_collection_model_json2 = role_template_versions_collection_model.to_dict()
        assert role_template_versions_collection_model_json2 == role_template_versions_collection_model_json


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


class TestModel_TemplateActionControl:
    """
    Test Class for TemplateActionControl
    """

    def test_template_action_control_serialization(self):
        """
        Test serialization/deserialization for TemplateActionControl
        """

        # Construct a json representation of a TemplateActionControl model
        template_action_control_model_json = {}
        template_action_control_model_json['service_name'] = 'testString'
        template_action_control_model_json['description'] = 'testString'
        template_action_control_model_json['actions'] = ['testString']

        # Construct a model instance of TemplateActionControl by calling from_dict on the json representation
        template_action_control_model = TemplateActionControl.from_dict(template_action_control_model_json)
        assert template_action_control_model != False

        # Construct a model instance of TemplateActionControl by calling from_dict on the json representation
        template_action_control_model_dict = TemplateActionControl.from_dict(
            template_action_control_model_json
        ).__dict__
        template_action_control_model2 = TemplateActionControl(**template_action_control_model_dict)

        # Verify the model instances are equivalent
        assert template_action_control_model == template_action_control_model2

        # Convert model instance back to dict and verify no loss of data
        template_action_control_model_json2 = template_action_control_model.to_dict()
        assert template_action_control_model_json2 == template_action_control_model_json


class TestModel_TemplateControl:
    """
    Test Class for TemplateControl
    """

    def test_template_control_serialization(self):
        """
        Test serialization/deserialization for TemplateControl
        """

        # Construct dict forms of any model objects needed in order to build this model.

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        role_template_references_item_model = {}  # RoleTemplateReferencesItem
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        template_grant_model = {}  # TemplateGrant
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        # Construct a json representation of a TemplateControl model
        template_control_model_json = {}
        template_control_model_json['grant'] = template_grant_model

        # Construct a model instance of TemplateControl by calling from_dict on the json representation
        template_control_model = TemplateControl.from_dict(template_control_model_json)
        assert template_control_model != False

        # Construct a model instance of TemplateControl by calling from_dict on the json representation
        template_control_model_dict = TemplateControl.from_dict(template_control_model_json).__dict__
        template_control_model2 = TemplateControl(**template_control_model_dict)

        # Verify the model instances are equivalent
        assert template_control_model == template_control_model2

        # Convert model instance back to dict and verify no loss of data
        template_control_model_json2 = template_control_model.to_dict()
        assert template_control_model_json2 == template_control_model_json


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


class TestModel_TemplateGrant:
    """
    Test Class for TemplateGrant
    """

    def test_template_grant_serialization(self):
        """
        Test serialization/deserialization for TemplateGrant
        """

        # Construct dict forms of any model objects needed in order to build this model.

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        role_template_references_item_model = {}  # RoleTemplateReferencesItem
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        # Construct a json representation of a TemplateGrant model
        template_grant_model_json = {}
        template_grant_model_json['roles'] = [roles_model]
        template_grant_model_json['role_template_references'] = [role_template_references_item_model]

        # Construct a model instance of TemplateGrant by calling from_dict on the json representation
        template_grant_model = TemplateGrant.from_dict(template_grant_model_json)
        assert template_grant_model != False

        # Construct a model instance of TemplateGrant by calling from_dict on the json representation
        template_grant_model_dict = TemplateGrant.from_dict(template_grant_model_json).__dict__
        template_grant_model2 = TemplateGrant(**template_grant_model_dict)

        # Verify the model instances are equivalent
        assert template_grant_model == template_grant_model2

        # Convert model instance back to dict and verify no loss of data
        template_grant_model_json2 = template_grant_model.to_dict()
        assert template_grant_model_json2 == template_grant_model_json


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

        v2_policy_subject_attribute_model = {}  # V2PolicySubjectAttribute
        v2_policy_subject_attribute_model['key'] = 'testString'
        v2_policy_subject_attribute_model['operator'] = 'stringEquals'
        v2_policy_subject_attribute_model['value'] = 'testString'

        v2_policy_subject_model = {}  # V2PolicySubject
        v2_policy_subject_model['attributes'] = [v2_policy_subject_attribute_model]

        v2_policy_rule_model = {}  # V2PolicyRuleRuleAttribute
        v2_policy_rule_model['key'] = 'testString'
        v2_policy_rule_model['operator'] = 'stringEquals'
        v2_policy_rule_model['value'] = 'testString'

        roles_model = {}  # Roles
        roles_model['role_id'] = 'testString'

        role_template_references_item_model = {}  # RoleTemplateReferencesItem
        role_template_references_item_model['id'] = 'testString'
        role_template_references_item_model['version'] = 'testString'

        template_grant_model = {}  # TemplateGrant
        template_grant_model['roles'] = [roles_model]
        template_grant_model['role_template_references'] = [role_template_references_item_model]

        template_control_model = {}  # TemplateControl
        template_control_model['grant'] = template_grant_model

        # Construct a json representation of a TemplatePolicy model
        template_policy_model_json = {}
        template_policy_model_json['type'] = 'access'
        template_policy_model_json['description'] = 'testString'
        template_policy_model_json['resource'] = v2_policy_resource_model
        template_policy_model_json['subject'] = v2_policy_subject_model
        template_policy_model_json['pattern'] = 'testString'
        template_policy_model_json['rule'] = v2_policy_rule_model
        template_policy_model_json['control'] = template_control_model

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


class TestModel_TemplateRole:
    """
    Test Class for TemplateRole
    """

    def test_template_role_serialization(self):
        """
        Test serialization/deserialization for TemplateRole
        """

        # Construct a json representation of a TemplateRole model
        template_role_model_json = {}
        template_role_model_json['display_name'] = 'testString'
        template_role_model_json['service_name'] = 'testString'
        template_role_model_json['description'] = 'testString'
        template_role_model_json['actions'] = ['testString']

        # Construct a model instance of TemplateRole by calling from_dict on the json representation
        template_role_model = TemplateRole.from_dict(template_role_model_json)
        assert template_role_model != False

        # Construct a model instance of TemplateRole by calling from_dict on the json representation
        template_role_model_dict = TemplateRole.from_dict(template_role_model_json).__dict__
        template_role_model2 = TemplateRole(**template_role_model_dict)

        # Verify the model instances are equivalent
        assert template_role_model == template_role_model2

        # Convert model instance back to dict and verify no loss of data
        template_role_model_json2 = template_role_model.to_dict()
        assert template_role_model_json2 == template_role_model_json


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

        first_model = {}  # First

        next_model = {}  # Next
        next_model['start'] = 'testString'

        previous_model = {}  # Previous
        previous_model['start'] = 'testString'

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
        v2_policy_collection_model_json['limit'] = 1
        v2_policy_collection_model_json['first'] = first_model
        v2_policy_collection_model_json['next'] = next_model
        v2_policy_collection_model_json['previous'] = previous_model
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
        v2_policy_resource_attribute_model = V2PolicyResourceAttribute.from_dict(
            v2_policy_resource_attribute_model_json
        )
        assert v2_policy_resource_attribute_model != False

        # Construct a model instance of V2PolicyResourceAttribute by calling from_dict on the json representation
        v2_policy_resource_attribute_model_dict = V2PolicyResourceAttribute.from_dict(
            v2_policy_resource_attribute_model_json
        ).__dict__
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
        v2_policy_subject_attribute_model_dict = V2PolicySubjectAttribute.from_dict(
            v2_policy_subject_attribute_model_json
        ).__dict__
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
        v2_policy_template_meta_data_model_dict = V2PolicyTemplateMetaData.from_dict(
            v2_policy_template_meta_data_model_json
        ).__dict__
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
        control_response_control_model_dict = ControlResponseControl.from_dict(
            control_response_control_model_json
        ).__dict__
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
        control_response_control_with_enriched_roles_model = ControlResponseControlWithEnrichedRoles.from_dict(
            control_response_control_with_enriched_roles_model_json
        )
        assert control_response_control_with_enriched_roles_model != False

        # Construct a model instance of ControlResponseControlWithEnrichedRoles by calling from_dict on the json representation
        control_response_control_with_enriched_roles_model_dict = ControlResponseControlWithEnrichedRoles.from_dict(
            control_response_control_with_enriched_roles_model_json
        ).__dict__
        control_response_control_with_enriched_roles_model2 = ControlResponseControlWithEnrichedRoles(
            **control_response_control_with_enriched_roles_model_dict
        )

        # Verify the model instances are equivalent
        assert control_response_control_with_enriched_roles_model == control_response_control_with_enriched_roles_model2

        # Convert model instance back to dict and verify no loss of data
        control_response_control_with_enriched_roles_model_json2 = (
            control_response_control_with_enriched_roles_model.to_dict()
        )
        assert (
            control_response_control_with_enriched_roles_model_json2
            == control_response_control_with_enriched_roles_model_json
        )


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
        nested_condition_rule_attribute_model = NestedConditionRuleAttribute.from_dict(
            nested_condition_rule_attribute_model_json
        )
        assert nested_condition_rule_attribute_model != False

        # Construct a model instance of NestedConditionRuleAttribute by calling from_dict on the json representation
        nested_condition_rule_attribute_model_dict = NestedConditionRuleAttribute.from_dict(
            nested_condition_rule_attribute_model_json
        ).__dict__
        nested_condition_rule_attribute_model2 = NestedConditionRuleAttribute(
            **nested_condition_rule_attribute_model_dict
        )

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
        nested_condition_rule_with_conditions_model = NestedConditionRuleWithConditions.from_dict(
            nested_condition_rule_with_conditions_model_json
        )
        assert nested_condition_rule_with_conditions_model != False

        # Construct a model instance of NestedConditionRuleWithConditions by calling from_dict on the json representation
        nested_condition_rule_with_conditions_model_dict = NestedConditionRuleWithConditions.from_dict(
            nested_condition_rule_with_conditions_model_json
        ).__dict__
        nested_condition_rule_with_conditions_model2 = NestedConditionRuleWithConditions(
            **nested_condition_rule_with_conditions_model_dict
        )

        # Verify the model instances are equivalent
        assert nested_condition_rule_with_conditions_model == nested_condition_rule_with_conditions_model2

        # Convert model instance back to dict and verify no loss of data
        nested_condition_rule_with_conditions_model_json2 = nested_condition_rule_with_conditions_model.to_dict()
        assert nested_condition_rule_with_conditions_model_json2 == nested_condition_rule_with_conditions_model_json


class TestModel_PolicyTemplateAssignmentItemsPolicyAssignment:
    """
    Test Class for PolicyTemplateAssignmentItemsPolicyAssignment
    """

    def test_policy_template_assignment_items_policy_assignment_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplateAssignmentItemsPolicyAssignment
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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = assignment_resource_error_model

        policy_assignment_resources_model = {}  # PolicyAssignmentResources
        policy_assignment_resources_model['target'] = 'testString'
        policy_assignment_resources_model['policy'] = policy_assignment_resource_policy_model

        # Construct a json representation of a PolicyTemplateAssignmentItemsPolicyAssignment model
        policy_template_assignment_items_policy_assignment_model_json = {}
        policy_template_assignment_items_policy_assignment_model_json['template_id'] = 'testString'
        policy_template_assignment_items_policy_assignment_model_json['template_version'] = 'testString'
        policy_template_assignment_items_policy_assignment_model_json['assignment_id'] = 'testString'
        policy_template_assignment_items_policy_assignment_model_json['target_type'] = 'Account'
        policy_template_assignment_items_policy_assignment_model_json['target'] = 'testString'
        policy_template_assignment_items_policy_assignment_model_json['resources'] = [policy_assignment_resources_model]
        policy_template_assignment_items_policy_assignment_model_json['status'] = 'in_progress'

        # Construct a model instance of PolicyTemplateAssignmentItemsPolicyAssignment by calling from_dict on the json representation
        policy_template_assignment_items_policy_assignment_model = (
            PolicyTemplateAssignmentItemsPolicyAssignment.from_dict(
                policy_template_assignment_items_policy_assignment_model_json
            )
        )
        assert policy_template_assignment_items_policy_assignment_model != False

        # Construct a model instance of PolicyTemplateAssignmentItemsPolicyAssignment by calling from_dict on the json representation
        policy_template_assignment_items_policy_assignment_model_dict = (
            PolicyTemplateAssignmentItemsPolicyAssignment.from_dict(
                policy_template_assignment_items_policy_assignment_model_json
            ).__dict__
        )
        policy_template_assignment_items_policy_assignment_model2 = PolicyTemplateAssignmentItemsPolicyAssignment(
            **policy_template_assignment_items_policy_assignment_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            policy_template_assignment_items_policy_assignment_model
            == policy_template_assignment_items_policy_assignment_model2
        )

        # Convert model instance back to dict and verify no loss of data
        policy_template_assignment_items_policy_assignment_model_json2 = (
            policy_template_assignment_items_policy_assignment_model.to_dict()
        )
        assert (
            policy_template_assignment_items_policy_assignment_model_json2
            == policy_template_assignment_items_policy_assignment_model_json
        )


class TestModel_PolicyTemplateAssignmentItemsPolicyAssignmentV1:
    """
    Test Class for PolicyTemplateAssignmentItemsPolicyAssignmentV1
    """

    def test_policy_template_assignment_items_policy_assignment_v1_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplateAssignmentItemsPolicyAssignmentV1
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_target_details_model = {}  # AssignmentTargetDetails
        assignment_target_details_model['type'] = 'Account'
        assignment_target_details_model['id'] = 'testString'

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

        assignment_resource_error_model = {}  # AssignmentResourceError
        assignment_resource_error_model['name'] = 'testString'
        assignment_resource_error_model['errorCode'] = 'testString'
        assignment_resource_error_model['message'] = 'testString'
        assignment_resource_error_model['code'] = 'testString'
        assignment_resource_error_model['errors'] = [error_object_model]

        policy_assignment_resource_policy_model = {}  # PolicyAssignmentResourcePolicy
        policy_assignment_resource_policy_model['resource_created'] = assignment_resource_created_model
        policy_assignment_resource_policy_model['status'] = 'testString'
        policy_assignment_resource_policy_model['error_message'] = assignment_resource_error_model

        policy_assignment_v1_resources_model = {}  # PolicyAssignmentV1Resources
        policy_assignment_v1_resources_model['target'] = assignment_target_details_model
        policy_assignment_v1_resources_model['policy'] = policy_assignment_resource_policy_model

        policy_assignment_v1_subject_model = {}  # PolicyAssignmentV1Subject

        assignment_template_details_model = {}  # AssignmentTemplateDetails
        assignment_template_details_model['id'] = 'testString'
        assignment_template_details_model['version'] = 'testString'

        # Construct a json representation of a PolicyTemplateAssignmentItemsPolicyAssignmentV1 model
        policy_template_assignment_items_policy_assignment_v1_model_json = {}
        policy_template_assignment_items_policy_assignment_v1_model_json['target'] = assignment_target_details_model
        policy_template_assignment_items_policy_assignment_v1_model_json['resources'] = [
            policy_assignment_v1_resources_model
        ]
        policy_template_assignment_items_policy_assignment_v1_model_json['subject'] = policy_assignment_v1_subject_model
        policy_template_assignment_items_policy_assignment_v1_model_json['template'] = assignment_template_details_model
        policy_template_assignment_items_policy_assignment_v1_model_json['status'] = 'in_progress'

        # Construct a model instance of PolicyTemplateAssignmentItemsPolicyAssignmentV1 by calling from_dict on the json representation
        policy_template_assignment_items_policy_assignment_v1_model = (
            PolicyTemplateAssignmentItemsPolicyAssignmentV1.from_dict(
                policy_template_assignment_items_policy_assignment_v1_model_json
            )
        )
        assert policy_template_assignment_items_policy_assignment_v1_model != False

        # Construct a model instance of PolicyTemplateAssignmentItemsPolicyAssignmentV1 by calling from_dict on the json representation
        policy_template_assignment_items_policy_assignment_v1_model_dict = (
            PolicyTemplateAssignmentItemsPolicyAssignmentV1.from_dict(
                policy_template_assignment_items_policy_assignment_v1_model_json
            ).__dict__
        )
        policy_template_assignment_items_policy_assignment_v1_model2 = PolicyTemplateAssignmentItemsPolicyAssignmentV1(
            **policy_template_assignment_items_policy_assignment_v1_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            policy_template_assignment_items_policy_assignment_v1_model
            == policy_template_assignment_items_policy_assignment_v1_model2
        )

        # Convert model instance back to dict and verify no loss of data
        policy_template_assignment_items_policy_assignment_v1_model_json2 = (
            policy_template_assignment_items_policy_assignment_v1_model.to_dict()
        )
        assert (
            policy_template_assignment_items_policy_assignment_v1_model_json2
            == policy_template_assignment_items_policy_assignment_v1_model_json
        )


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
        v2_policy_rule_rule_attribute_model = V2PolicyRuleRuleAttribute.from_dict(
            v2_policy_rule_rule_attribute_model_json
        )
        assert v2_policy_rule_rule_attribute_model != False

        # Construct a model instance of V2PolicyRuleRuleAttribute by calling from_dict on the json representation
        v2_policy_rule_rule_attribute_model_dict = V2PolicyRuleRuleAttribute.from_dict(
            v2_policy_rule_rule_attribute_model_json
        ).__dict__
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
        v2_policy_rule_rule_with_nested_conditions_model = V2PolicyRuleRuleWithNestedConditions.from_dict(
            v2_policy_rule_rule_with_nested_conditions_model_json
        )
        assert v2_policy_rule_rule_with_nested_conditions_model != False

        # Construct a model instance of V2PolicyRuleRuleWithNestedConditions by calling from_dict on the json representation
        v2_policy_rule_rule_with_nested_conditions_model_dict = V2PolicyRuleRuleWithNestedConditions.from_dict(
            v2_policy_rule_rule_with_nested_conditions_model_json
        ).__dict__
        v2_policy_rule_rule_with_nested_conditions_model2 = V2PolicyRuleRuleWithNestedConditions(
            **v2_policy_rule_rule_with_nested_conditions_model_dict
        )

        # Verify the model instances are equivalent
        assert v2_policy_rule_rule_with_nested_conditions_model == v2_policy_rule_rule_with_nested_conditions_model2

        # Convert model instance back to dict and verify no loss of data
        v2_policy_rule_rule_with_nested_conditions_model_json2 = (
            v2_policy_rule_rule_with_nested_conditions_model.to_dict()
        )
        assert (
            v2_policy_rule_rule_with_nested_conditions_model_json2
            == v2_policy_rule_rule_with_nested_conditions_model_json
        )


# endregion
##############################################################################
# End of Model Tests
##############################################################################
