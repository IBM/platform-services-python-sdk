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
Unit Tests for IamAccessGroupsV2
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
from ibm_platform_services.iam_access_groups_v2 import *


_service = IamAccessGroupsV2(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://iam.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: AccessGroupOperations
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

        service = IamAccessGroupsV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamAccessGroupsV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamAccessGroupsV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestCreateAccessGroup():
    """
    Test Class for create_access_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_access_group_all_params(self):
        """
        create_access_group()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        account_id = 'testString'
        name = 'Managers'
        description = 'Group for managers'
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_access_group(
            account_id,
            name,
            description=description,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Managers'
        assert req_body['description'] == 'Group for managers'

    def test_create_access_group_all_params_with_retries(self):
        # Enable retries and run test_create_access_group_all_params.
        _service.enable_retries()
        self.test_create_access_group_all_params()

        # Disable retries and run test_create_access_group_all_params.
        _service.disable_retries()
        self.test_create_access_group_all_params()

    @responses.activate
    def test_create_access_group_required_params(self):
        """
        test_create_access_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        account_id = 'testString'
        name = 'Managers'
        description = 'Group for managers'

        # Invoke method
        response = _service.create_access_group(
            account_id,
            name,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Managers'
        assert req_body['description'] == 'Group for managers'

    def test_create_access_group_required_params_with_retries(self):
        # Enable retries and run test_create_access_group_required_params.
        _service.enable_retries()
        self.test_create_access_group_required_params()

        # Disable retries and run test_create_access_group_required_params.
        _service.disable_retries()
        self.test_create_access_group_required_params()

    @responses.activate
    def test_create_access_group_value_error(self):
        """
        test_create_access_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        account_id = 'testString'
        name = 'Managers'
        description = 'Group for managers'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_access_group(**req_copy)


    def test_create_access_group_value_error_with_retries(self):
        # Enable retries and run test_create_access_group_value_error.
        _service.enable_retries()
        self.test_create_access_group_value_error()

        # Disable retries and run test_create_access_group_value_error.
        _service.disable_retries()
        self.test_create_access_group_value_error()

class TestListAccessGroups():
    """
    Test Class for list_access_groups
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_access_groups_all_params(self):
        """
        list_access_groups()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups": [{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'
        iam_id = 'testString'
        limit = 38
        offset = 38
        sort = 'name'
        show_federated = False
        hide_public_access = False

        # Invoke method
        response = _service.list_access_groups(
            account_id,
            transaction_id=transaction_id,
            iam_id=iam_id,
            limit=limit,
            offset=offset,
            sort=sort,
            show_federated=show_federated,
            hide_public_access=hide_public_access,
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
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'show_federated={}'.format('true' if show_federated else 'false') in query_string
        assert 'hide_public_access={}'.format('true' if hide_public_access else 'false') in query_string

    def test_list_access_groups_all_params_with_retries(self):
        # Enable retries and run test_list_access_groups_all_params.
        _service.enable_retries()
        self.test_list_access_groups_all_params()

        # Disable retries and run test_list_access_groups_all_params.
        _service.disable_retries()
        self.test_list_access_groups_all_params()

    @responses.activate
    def test_list_access_groups_required_params(self):
        """
        test_list_access_groups_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups": [{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_access_groups(
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

    def test_list_access_groups_required_params_with_retries(self):
        # Enable retries and run test_list_access_groups_required_params.
        _service.enable_retries()
        self.test_list_access_groups_required_params()

        # Disable retries and run test_list_access_groups_required_params.
        _service.disable_retries()
        self.test_list_access_groups_required_params()

    @responses.activate
    def test_list_access_groups_value_error(self):
        """
        test_list_access_groups_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups": [{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}]}'
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
                _service.list_access_groups(**req_copy)


    def test_list_access_groups_value_error_with_retries(self):
        # Enable retries and run test_list_access_groups_value_error.
        _service.enable_retries()
        self.test_list_access_groups_value_error()

        # Disable retries and run test_list_access_groups_value_error.
        _service.disable_retries()
        self.test_list_access_groups_value_error()

class TestGetAccessGroup():
    """
    Test Class for get_access_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_access_group_all_params(self):
        """
        get_access_group()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'
        show_federated = False

        # Invoke method
        response = _service.get_access_group(
            access_group_id,
            transaction_id=transaction_id,
            show_federated=show_federated,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'show_federated={}'.format('true' if show_federated else 'false') in query_string

    def test_get_access_group_all_params_with_retries(self):
        # Enable retries and run test_get_access_group_all_params.
        _service.enable_retries()
        self.test_get_access_group_all_params()

        # Disable retries and run test_get_access_group_all_params.
        _service.disable_retries()
        self.test_get_access_group_all_params()

    @responses.activate
    def test_get_access_group_required_params(self):
        """
        test_get_access_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = _service.get_access_group(
            access_group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_access_group_required_params_with_retries(self):
        # Enable retries and run test_get_access_group_required_params.
        _service.enable_retries()
        self.test_get_access_group_required_params()

        # Disable retries and run test_get_access_group_required_params.
        _service.disable_retries()
        self.test_get_access_group_required_params()

    @responses.activate
    def test_get_access_group_value_error(self):
        """
        test_get_access_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_access_group(**req_copy)


    def test_get_access_group_value_error_with_retries(self):
        # Enable retries and run test_get_access_group_value_error.
        _service.enable_retries()
        self.test_get_access_group_value_error()

        # Disable retries and run test_get_access_group_value_error.
        _service.disable_retries()
        self.test_get_access_group_value_error()

class TestUpdateAccessGroup():
    """
    Test Class for update_access_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_access_group_all_params(self):
        """
        update_access_group()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        if_match = 'testString'
        name = 'Awesome Managers'
        description = 'Group for awesome managers.'
        transaction_id = 'testString'

        # Invoke method
        response = _service.update_access_group(
            access_group_id,
            if_match,
            name=name,
            description=description,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Awesome Managers'
        assert req_body['description'] == 'Group for awesome managers.'

    def test_update_access_group_all_params_with_retries(self):
        # Enable retries and run test_update_access_group_all_params.
        _service.enable_retries()
        self.test_update_access_group_all_params()

        # Disable retries and run test_update_access_group_all_params.
        _service.disable_retries()
        self.test_update_access_group_all_params()

    @responses.activate
    def test_update_access_group_required_params(self):
        """
        test_update_access_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        if_match = 'testString'
        name = 'Awesome Managers'
        description = 'Group for awesome managers.'

        # Invoke method
        response = _service.update_access_group(
            access_group_id,
            if_match,
            name=name,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Awesome Managers'
        assert req_body['description'] == 'Group for awesome managers.'

    def test_update_access_group_required_params_with_retries(self):
        # Enable retries and run test_update_access_group_required_params.
        _service.enable_retries()
        self.test_update_access_group_required_params()

        # Disable retries and run test_update_access_group_required_params.
        _service.disable_retries()
        self.test_update_access_group_required_params()

    @responses.activate
    def test_update_access_group_value_error(self):
        """
        test_update_access_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        if_match = 'testString'
        name = 'Awesome Managers'
        description = 'Group for awesome managers.'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_access_group(**req_copy)


    def test_update_access_group_value_error_with_retries(self):
        # Enable retries and run test_update_access_group_value_error.
        _service.enable_retries()
        self.test_update_access_group_value_error()

        # Disable retries and run test_update_access_group_value_error.
        _service.disable_retries()
        self.test_update_access_group_value_error()

class TestDeleteAccessGroup():
    """
    Test Class for delete_access_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_access_group_all_params(self):
        """
        delete_access_group()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'
        force = False

        # Invoke method
        response = _service.delete_access_group(
            access_group_id,
            transaction_id=transaction_id,
            force=force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'force={}'.format('true' if force else 'false') in query_string

    def test_delete_access_group_all_params_with_retries(self):
        # Enable retries and run test_delete_access_group_all_params.
        _service.enable_retries()
        self.test_delete_access_group_all_params()

        # Disable retries and run test_delete_access_group_all_params.
        _service.disable_retries()
        self.test_delete_access_group_all_params()

    @responses.activate
    def test_delete_access_group_required_params(self):
        """
        test_delete_access_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = _service.delete_access_group(
            access_group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_access_group_required_params_with_retries(self):
        # Enable retries and run test_delete_access_group_required_params.
        _service.enable_retries()
        self.test_delete_access_group_required_params()

        # Disable retries and run test_delete_access_group_required_params.
        _service.disable_retries()
        self.test_delete_access_group_required_params()

    @responses.activate
    def test_delete_access_group_value_error(self):
        """
        test_delete_access_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_access_group(**req_copy)


    def test_delete_access_group_value_error_with_retries(self):
        # Enable retries and run test_delete_access_group_value_error.
        _service.enable_retries()
        self.test_delete_access_group_value_error()

        # Disable retries and run test_delete_access_group_value_error.
        _service.disable_retries()
        self.test_delete_access_group_value_error()

# endregion
##############################################################################
# End of Service: AccessGroupOperations
##############################################################################

##############################################################################
# Start of Service: MembershipOperations
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

        service = IamAccessGroupsV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamAccessGroupsV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamAccessGroupsV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestIsMemberOfAccessGroup():
    """
    Test Class for is_member_of_access_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_is_member_of_access_group_all_params(self):
        """
        is_member_of_access_group()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members/testString')
        responses.add(responses.HEAD,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.is_member_of_access_group(
            access_group_id,
            iam_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_is_member_of_access_group_all_params_with_retries(self):
        # Enable retries and run test_is_member_of_access_group_all_params.
        _service.enable_retries()
        self.test_is_member_of_access_group_all_params()

        # Disable retries and run test_is_member_of_access_group_all_params.
        _service.disable_retries()
        self.test_is_member_of_access_group_all_params()

    @responses.activate
    def test_is_member_of_access_group_required_params(self):
        """
        test_is_member_of_access_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members/testString')
        responses.add(responses.HEAD,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.is_member_of_access_group(
            access_group_id,
            iam_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_is_member_of_access_group_required_params_with_retries(self):
        # Enable retries and run test_is_member_of_access_group_required_params.
        _service.enable_retries()
        self.test_is_member_of_access_group_required_params()

        # Disable retries and run test_is_member_of_access_group_required_params.
        _service.disable_retries()
        self.test_is_member_of_access_group_required_params()

    @responses.activate
    def test_is_member_of_access_group_value_error(self):
        """
        test_is_member_of_access_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members/testString')
        responses.add(responses.HEAD,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.is_member_of_access_group(**req_copy)


    def test_is_member_of_access_group_value_error_with_retries(self):
        # Enable retries and run test_is_member_of_access_group_value_error.
        _service.enable_retries()
        self.test_is_member_of_access_group_value_error()

        # Disable retries and run test_is_member_of_access_group_value_error.
        _service.disable_retries()
        self.test_is_member_of_access_group_value_error()

class TestAddMembersToAccessGroup():
    """
    Test Class for add_members_to_access_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_members_to_access_group_all_params(self):
        """
        add_members_to_access_group()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members')
        mock_response = '{"members": [{"iam_id": "iam_id", "type": "type", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Construct a dict representation of a AddGroupMembersRequestMembersItem model
        add_group_members_request_members_item_model = {}
        add_group_members_request_members_item_model['iam_id'] = 'IBMid-user1'
        add_group_members_request_members_item_model['type'] = 'user'

        # Set up parameter values
        access_group_id = 'testString'
        members = [add_group_members_request_members_item_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.add_members_to_access_group(
            access_group_id,
            members=members,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['members'] == [add_group_members_request_members_item_model]

    def test_add_members_to_access_group_all_params_with_retries(self):
        # Enable retries and run test_add_members_to_access_group_all_params.
        _service.enable_retries()
        self.test_add_members_to_access_group_all_params()

        # Disable retries and run test_add_members_to_access_group_all_params.
        _service.disable_retries()
        self.test_add_members_to_access_group_all_params()

    @responses.activate
    def test_add_members_to_access_group_required_params(self):
        """
        test_add_members_to_access_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members')
        mock_response = '{"members": [{"iam_id": "iam_id", "type": "type", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Construct a dict representation of a AddGroupMembersRequestMembersItem model
        add_group_members_request_members_item_model = {}
        add_group_members_request_members_item_model['iam_id'] = 'IBMid-user1'
        add_group_members_request_members_item_model['type'] = 'user'

        # Set up parameter values
        access_group_id = 'testString'
        members = [add_group_members_request_members_item_model]

        # Invoke method
        response = _service.add_members_to_access_group(
            access_group_id,
            members=members,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['members'] == [add_group_members_request_members_item_model]

    def test_add_members_to_access_group_required_params_with_retries(self):
        # Enable retries and run test_add_members_to_access_group_required_params.
        _service.enable_retries()
        self.test_add_members_to_access_group_required_params()

        # Disable retries and run test_add_members_to_access_group_required_params.
        _service.disable_retries()
        self.test_add_members_to_access_group_required_params()

    @responses.activate
    def test_add_members_to_access_group_value_error(self):
        """
        test_add_members_to_access_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members')
        mock_response = '{"members": [{"iam_id": "iam_id", "type": "type", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Construct a dict representation of a AddGroupMembersRequestMembersItem model
        add_group_members_request_members_item_model = {}
        add_group_members_request_members_item_model['iam_id'] = 'IBMid-user1'
        add_group_members_request_members_item_model['type'] = 'user'

        # Set up parameter values
        access_group_id = 'testString'
        members = [add_group_members_request_members_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_members_to_access_group(**req_copy)


    def test_add_members_to_access_group_value_error_with_retries(self):
        # Enable retries and run test_add_members_to_access_group_value_error.
        _service.enable_retries()
        self.test_add_members_to_access_group_value_error()

        # Disable retries and run test_add_members_to_access_group_value_error.
        _service.disable_retries()
        self.test_add_members_to_access_group_value_error()

class TestListAccessGroupMembers():
    """
    Test Class for list_access_group_members
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_access_group_members_all_params(self):
        """
        list_access_group_members()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "members": [{"iam_id": "iam_id", "type": "type", "name": "name", "email": "email", "description": "description", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'
        limit = 38
        offset = 38
        type = 'testString'
        verbose = False
        sort = 'testString'

        # Invoke method
        response = _service.list_access_group_members(
            access_group_id,
            transaction_id=transaction_id,
            limit=limit,
            offset=offset,
            type=type,
            verbose=verbose,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string

    def test_list_access_group_members_all_params_with_retries(self):
        # Enable retries and run test_list_access_group_members_all_params.
        _service.enable_retries()
        self.test_list_access_group_members_all_params()

        # Disable retries and run test_list_access_group_members_all_params.
        _service.disable_retries()
        self.test_list_access_group_members_all_params()

    @responses.activate
    def test_list_access_group_members_required_params(self):
        """
        test_list_access_group_members_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "members": [{"iam_id": "iam_id", "type": "type", "name": "name", "email": "email", "description": "description", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = _service.list_access_group_members(
            access_group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_access_group_members_required_params_with_retries(self):
        # Enable retries and run test_list_access_group_members_required_params.
        _service.enable_retries()
        self.test_list_access_group_members_required_params()

        # Disable retries and run test_list_access_group_members_required_params.
        _service.disable_retries()
        self.test_list_access_group_members_required_params()

    @responses.activate
    def test_list_access_group_members_value_error(self):
        """
        test_list_access_group_members_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "members": [{"iam_id": "iam_id", "type": "type", "name": "name", "email": "email", "description": "description", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_access_group_members(**req_copy)


    def test_list_access_group_members_value_error_with_retries(self):
        # Enable retries and run test_list_access_group_members_value_error.
        _service.enable_retries()
        self.test_list_access_group_members_value_error()

        # Disable retries and run test_list_access_group_members_value_error.
        _service.disable_retries()
        self.test_list_access_group_members_value_error()

class TestRemoveMemberFromAccessGroup():
    """
    Test Class for remove_member_from_access_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_remove_member_from_access_group_all_params(self):
        """
        remove_member_from_access_group()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.remove_member_from_access_group(
            access_group_id,
            iam_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_remove_member_from_access_group_all_params_with_retries(self):
        # Enable retries and run test_remove_member_from_access_group_all_params.
        _service.enable_retries()
        self.test_remove_member_from_access_group_all_params()

        # Disable retries and run test_remove_member_from_access_group_all_params.
        _service.disable_retries()
        self.test_remove_member_from_access_group_all_params()

    @responses.activate
    def test_remove_member_from_access_group_required_params(self):
        """
        test_remove_member_from_access_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.remove_member_from_access_group(
            access_group_id,
            iam_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_remove_member_from_access_group_required_params_with_retries(self):
        # Enable retries and run test_remove_member_from_access_group_required_params.
        _service.enable_retries()
        self.test_remove_member_from_access_group_required_params()

        # Disable retries and run test_remove_member_from_access_group_required_params.
        _service.disable_retries()
        self.test_remove_member_from_access_group_required_params()

    @responses.activate
    def test_remove_member_from_access_group_value_error(self):
        """
        test_remove_member_from_access_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.remove_member_from_access_group(**req_copy)


    def test_remove_member_from_access_group_value_error_with_retries(self):
        # Enable retries and run test_remove_member_from_access_group_value_error.
        _service.enable_retries()
        self.test_remove_member_from_access_group_value_error()

        # Disable retries and run test_remove_member_from_access_group_value_error.
        _service.disable_retries()
        self.test_remove_member_from_access_group_value_error()

class TestRemoveMembersFromAccessGroup():
    """
    Test Class for remove_members_from_access_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_remove_members_from_access_group_all_params(self):
        """
        remove_members_from_access_group()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members/delete')
        mock_response = '{"access_group_id": "access_group_id", "members": [{"iam_id": "iam_id", "trace": "trace", "status_code": 11, "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        access_group_id = 'testString'
        members = ['IBMId-user1', 'iam-ServiceId-123', 'iam-Profile-123']
        transaction_id = 'testString'

        # Invoke method
        response = _service.remove_members_from_access_group(
            access_group_id,
            members=members,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['members'] == ['IBMId-user1', 'iam-ServiceId-123', 'iam-Profile-123']

    def test_remove_members_from_access_group_all_params_with_retries(self):
        # Enable retries and run test_remove_members_from_access_group_all_params.
        _service.enable_retries()
        self.test_remove_members_from_access_group_all_params()

        # Disable retries and run test_remove_members_from_access_group_all_params.
        _service.disable_retries()
        self.test_remove_members_from_access_group_all_params()

    @responses.activate
    def test_remove_members_from_access_group_required_params(self):
        """
        test_remove_members_from_access_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members/delete')
        mock_response = '{"access_group_id": "access_group_id", "members": [{"iam_id": "iam_id", "trace": "trace", "status_code": 11, "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        access_group_id = 'testString'
        members = ['IBMId-user1', 'iam-ServiceId-123', 'iam-Profile-123']

        # Invoke method
        response = _service.remove_members_from_access_group(
            access_group_id,
            members=members,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['members'] == ['IBMId-user1', 'iam-ServiceId-123', 'iam-Profile-123']

    def test_remove_members_from_access_group_required_params_with_retries(self):
        # Enable retries and run test_remove_members_from_access_group_required_params.
        _service.enable_retries()
        self.test_remove_members_from_access_group_required_params()

        # Disable retries and run test_remove_members_from_access_group_required_params.
        _service.disable_retries()
        self.test_remove_members_from_access_group_required_params()

    @responses.activate
    def test_remove_members_from_access_group_value_error(self):
        """
        test_remove_members_from_access_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/members/delete')
        mock_response = '{"access_group_id": "access_group_id", "members": [{"iam_id": "iam_id", "trace": "trace", "status_code": 11, "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        access_group_id = 'testString'
        members = ['IBMId-user1', 'iam-ServiceId-123', 'iam-Profile-123']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.remove_members_from_access_group(**req_copy)


    def test_remove_members_from_access_group_value_error_with_retries(self):
        # Enable retries and run test_remove_members_from_access_group_value_error.
        _service.enable_retries()
        self.test_remove_members_from_access_group_value_error()

        # Disable retries and run test_remove_members_from_access_group_value_error.
        _service.disable_retries()
        self.test_remove_members_from_access_group_value_error()

class TestRemoveMemberFromAllAccessGroups():
    """
    Test Class for remove_member_from_all_access_groups
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_remove_member_from_all_access_groups_all_params(self):
        """
        remove_member_from_all_access_groups()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.remove_member_from_all_access_groups(
            account_id,
            iam_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_remove_member_from_all_access_groups_all_params_with_retries(self):
        # Enable retries and run test_remove_member_from_all_access_groups_all_params.
        _service.enable_retries()
        self.test_remove_member_from_all_access_groups_all_params()

        # Disable retries and run test_remove_member_from_all_access_groups_all_params.
        _service.disable_retries()
        self.test_remove_member_from_all_access_groups_all_params()

    @responses.activate
    def test_remove_member_from_all_access_groups_required_params(self):
        """
        test_remove_member_from_all_access_groups_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.remove_member_from_all_access_groups(
            account_id,
            iam_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_remove_member_from_all_access_groups_required_params_with_retries(self):
        # Enable retries and run test_remove_member_from_all_access_groups_required_params.
        _service.enable_retries()
        self.test_remove_member_from_all_access_groups_required_params()

        # Disable retries and run test_remove_member_from_all_access_groups_required_params.
        _service.disable_retries()
        self.test_remove_member_from_all_access_groups_required_params()

    @responses.activate
    def test_remove_member_from_all_access_groups_value_error(self):
        """
        test_remove_member_from_all_access_groups_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.remove_member_from_all_access_groups(**req_copy)


    def test_remove_member_from_all_access_groups_value_error_with_retries(self):
        # Enable retries and run test_remove_member_from_all_access_groups_value_error.
        _service.enable_retries()
        self.test_remove_member_from_all_access_groups_value_error()

        # Disable retries and run test_remove_member_from_all_access_groups_value_error.
        _service.disable_retries()
        self.test_remove_member_from_all_access_groups_value_error()

class TestAddMemberToMultipleAccessGroups():
    """
    Test Class for add_member_to_multiple_access_groups
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_member_to_multiple_access_groups_all_params(self):
        """
        add_member_to_multiple_access_groups()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        type = 'user'
        groups = ['access-group-id-1']
        transaction_id = 'testString'

        # Invoke method
        response = _service.add_member_to_multiple_access_groups(
            account_id,
            iam_id,
            type=type,
            groups=groups,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'user'
        assert req_body['groups'] == ['access-group-id-1']

    def test_add_member_to_multiple_access_groups_all_params_with_retries(self):
        # Enable retries and run test_add_member_to_multiple_access_groups_all_params.
        _service.enable_retries()
        self.test_add_member_to_multiple_access_groups_all_params()

        # Disable retries and run test_add_member_to_multiple_access_groups_all_params.
        _service.disable_retries()
        self.test_add_member_to_multiple_access_groups_all_params()

    @responses.activate
    def test_add_member_to_multiple_access_groups_required_params(self):
        """
        test_add_member_to_multiple_access_groups_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        type = 'user'
        groups = ['access-group-id-1']

        # Invoke method
        response = _service.add_member_to_multiple_access_groups(
            account_id,
            iam_id,
            type=type,
            groups=groups,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'user'
        assert req_body['groups'] == ['access-group-id-1']

    def test_add_member_to_multiple_access_groups_required_params_with_retries(self):
        # Enable retries and run test_add_member_to_multiple_access_groups_required_params.
        _service.enable_retries()
        self.test_add_member_to_multiple_access_groups_required_params()

        # Disable retries and run test_add_member_to_multiple_access_groups_required_params.
        _service.disable_retries()
        self.test_add_member_to_multiple_access_groups_required_params()

    @responses.activate
    def test_add_member_to_multiple_access_groups_value_error(self):
        """
        test_add_member_to_multiple_access_groups_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        type = 'user'
        groups = ['access-group-id-1']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_member_to_multiple_access_groups(**req_copy)


    def test_add_member_to_multiple_access_groups_value_error_with_retries(self):
        # Enable retries and run test_add_member_to_multiple_access_groups_value_error.
        _service.enable_retries()
        self.test_add_member_to_multiple_access_groups_value_error()

        # Disable retries and run test_add_member_to_multiple_access_groups_value_error.
        _service.disable_retries()
        self.test_add_member_to_multiple_access_groups_value_error()

# endregion
##############################################################################
# End of Service: MembershipOperations
##############################################################################

##############################################################################
# Start of Service: RuleOperations
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

        service = IamAccessGroupsV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamAccessGroupsV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamAccessGroupsV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestAddAccessGroupRule():
    """
    Test Class for add_access_group_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_access_group_rule_all_params(self):
        """
        add_access_group_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'isManager'
        rule_conditions_model['operator'] = 'EQUALS'
        rule_conditions_model['value'] = 'true'

        # Set up parameter values
        access_group_id = 'testString'
        expiration = 12
        realm_name = 'https://idp.example.org/SAML2'
        conditions = [rule_conditions_model]
        name = 'Manager group rule'
        transaction_id = 'testString'

        # Invoke method
        response = _service.add_access_group_rule(
            access_group_id,
            expiration,
            realm_name,
            conditions,
            name=name,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expiration'] == 12
        assert req_body['realm_name'] == 'https://idp.example.org/SAML2'
        assert req_body['conditions'] == [rule_conditions_model]
        assert req_body['name'] == 'Manager group rule'

    def test_add_access_group_rule_all_params_with_retries(self):
        # Enable retries and run test_add_access_group_rule_all_params.
        _service.enable_retries()
        self.test_add_access_group_rule_all_params()

        # Disable retries and run test_add_access_group_rule_all_params.
        _service.disable_retries()
        self.test_add_access_group_rule_all_params()

    @responses.activate
    def test_add_access_group_rule_required_params(self):
        """
        test_add_access_group_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'isManager'
        rule_conditions_model['operator'] = 'EQUALS'
        rule_conditions_model['value'] = 'true'

        # Set up parameter values
        access_group_id = 'testString'
        expiration = 12
        realm_name = 'https://idp.example.org/SAML2'
        conditions = [rule_conditions_model]
        name = 'Manager group rule'

        # Invoke method
        response = _service.add_access_group_rule(
            access_group_id,
            expiration,
            realm_name,
            conditions,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expiration'] == 12
        assert req_body['realm_name'] == 'https://idp.example.org/SAML2'
        assert req_body['conditions'] == [rule_conditions_model]
        assert req_body['name'] == 'Manager group rule'

    def test_add_access_group_rule_required_params_with_retries(self):
        # Enable retries and run test_add_access_group_rule_required_params.
        _service.enable_retries()
        self.test_add_access_group_rule_required_params()

        # Disable retries and run test_add_access_group_rule_required_params.
        _service.disable_retries()
        self.test_add_access_group_rule_required_params()

    @responses.activate
    def test_add_access_group_rule_value_error(self):
        """
        test_add_access_group_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'isManager'
        rule_conditions_model['operator'] = 'EQUALS'
        rule_conditions_model['value'] = 'true'

        # Set up parameter values
        access_group_id = 'testString'
        expiration = 12
        realm_name = 'https://idp.example.org/SAML2'
        conditions = [rule_conditions_model]
        name = 'Manager group rule'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "expiration": expiration,
            "realm_name": realm_name,
            "conditions": conditions,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_access_group_rule(**req_copy)


    def test_add_access_group_rule_value_error_with_retries(self):
        # Enable retries and run test_add_access_group_rule_value_error.
        _service.enable_retries()
        self.test_add_access_group_rule_value_error()

        # Disable retries and run test_add_access_group_rule_value_error.
        _service.disable_retries()
        self.test_add_access_group_rule_value_error()

class TestListAccessGroupRules():
    """
    Test Class for list_access_group_rules
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_access_group_rules_all_params(self):
        """
        list_access_group_rules()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules')
        mock_response = '{"rules": [{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.list_access_group_rules(
            access_group_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_access_group_rules_all_params_with_retries(self):
        # Enable retries and run test_list_access_group_rules_all_params.
        _service.enable_retries()
        self.test_list_access_group_rules_all_params()

        # Disable retries and run test_list_access_group_rules_all_params.
        _service.disable_retries()
        self.test_list_access_group_rules_all_params()

    @responses.activate
    def test_list_access_group_rules_required_params(self):
        """
        test_list_access_group_rules_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules')
        mock_response = '{"rules": [{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = _service.list_access_group_rules(
            access_group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_access_group_rules_required_params_with_retries(self):
        # Enable retries and run test_list_access_group_rules_required_params.
        _service.enable_retries()
        self.test_list_access_group_rules_required_params()

        # Disable retries and run test_list_access_group_rules_required_params.
        _service.disable_retries()
        self.test_list_access_group_rules_required_params()

    @responses.activate
    def test_list_access_group_rules_value_error(self):
        """
        test_list_access_group_rules_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules')
        mock_response = '{"rules": [{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_access_group_rules(**req_copy)


    def test_list_access_group_rules_value_error_with_retries(self):
        # Enable retries and run test_list_access_group_rules_value_error.
        _service.enable_retries()
        self.test_list_access_group_rules_value_error()

        # Disable retries and run test_list_access_group_rules_value_error.
        _service.disable_retries()
        self.test_list_access_group_rules_value_error()

class TestGetAccessGroupRule():
    """
    Test Class for get_access_group_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_access_group_rule_all_params(self):
        """
        get_access_group_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_access_group_rule(
            access_group_id,
            rule_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_access_group_rule_all_params_with_retries(self):
        # Enable retries and run test_get_access_group_rule_all_params.
        _service.enable_retries()
        self.test_get_access_group_rule_all_params()

        # Disable retries and run test_get_access_group_rule_all_params.
        _service.disable_retries()
        self.test_get_access_group_rule_all_params()

    @responses.activate
    def test_get_access_group_rule_required_params(self):
        """
        test_get_access_group_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.get_access_group_rule(
            access_group_id,
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_access_group_rule_required_params_with_retries(self):
        # Enable retries and run test_get_access_group_rule_required_params.
        _service.enable_retries()
        self.test_get_access_group_rule_required_params()

        # Disable retries and run test_get_access_group_rule_required_params.
        _service.disable_retries()
        self.test_get_access_group_rule_required_params()

    @responses.activate
    def test_get_access_group_rule_value_error(self):
        """
        test_get_access_group_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_access_group_rule(**req_copy)


    def test_get_access_group_rule_value_error_with_retries(self):
        # Enable retries and run test_get_access_group_rule_value_error.
        _service.enable_retries()
        self.test_get_access_group_rule_value_error()

        # Disable retries and run test_get_access_group_rule_value_error.
        _service.disable_retries()
        self.test_get_access_group_rule_value_error()

class TestReplaceAccessGroupRule():
    """
    Test Class for replace_access_group_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_access_group_rule_all_params(self):
        """
        replace_access_group_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'isManager'
        rule_conditions_model['operator'] = 'EQUALS'
        rule_conditions_model['value'] = 'true'

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        if_match = 'testString'
        expiration = 12
        realm_name = 'https://idp.example.org/SAML2'
        conditions = [rule_conditions_model]
        name = 'Manager group rule'
        transaction_id = 'testString'

        # Invoke method
        response = _service.replace_access_group_rule(
            access_group_id,
            rule_id,
            if_match,
            expiration,
            realm_name,
            conditions,
            name=name,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expiration'] == 12
        assert req_body['realm_name'] == 'https://idp.example.org/SAML2'
        assert req_body['conditions'] == [rule_conditions_model]
        assert req_body['name'] == 'Manager group rule'

    def test_replace_access_group_rule_all_params_with_retries(self):
        # Enable retries and run test_replace_access_group_rule_all_params.
        _service.enable_retries()
        self.test_replace_access_group_rule_all_params()

        # Disable retries and run test_replace_access_group_rule_all_params.
        _service.disable_retries()
        self.test_replace_access_group_rule_all_params()

    @responses.activate
    def test_replace_access_group_rule_required_params(self):
        """
        test_replace_access_group_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'isManager'
        rule_conditions_model['operator'] = 'EQUALS'
        rule_conditions_model['value'] = 'true'

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        if_match = 'testString'
        expiration = 12
        realm_name = 'https://idp.example.org/SAML2'
        conditions = [rule_conditions_model]
        name = 'Manager group rule'

        # Invoke method
        response = _service.replace_access_group_rule(
            access_group_id,
            rule_id,
            if_match,
            expiration,
            realm_name,
            conditions,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expiration'] == 12
        assert req_body['realm_name'] == 'https://idp.example.org/SAML2'
        assert req_body['conditions'] == [rule_conditions_model]
        assert req_body['name'] == 'Manager group rule'

    def test_replace_access_group_rule_required_params_with_retries(self):
        # Enable retries and run test_replace_access_group_rule_required_params.
        _service.enable_retries()
        self.test_replace_access_group_rule_required_params()

        # Disable retries and run test_replace_access_group_rule_required_params.
        _service.disable_retries()
        self.test_replace_access_group_rule_required_params()

    @responses.activate
    def test_replace_access_group_rule_value_error(self):
        """
        test_replace_access_group_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'isManager'
        rule_conditions_model['operator'] = 'EQUALS'
        rule_conditions_model['value'] = 'true'

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        if_match = 'testString'
        expiration = 12
        realm_name = 'https://idp.example.org/SAML2'
        conditions = [rule_conditions_model]
        name = 'Manager group rule'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "rule_id": rule_id,
            "if_match": if_match,
            "expiration": expiration,
            "realm_name": realm_name,
            "conditions": conditions,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_access_group_rule(**req_copy)


    def test_replace_access_group_rule_value_error_with_retries(self):
        # Enable retries and run test_replace_access_group_rule_value_error.
        _service.enable_retries()
        self.test_replace_access_group_rule_value_error()

        # Disable retries and run test_replace_access_group_rule_value_error.
        _service.disable_retries()
        self.test_replace_access_group_rule_value_error()

class TestRemoveAccessGroupRule():
    """
    Test Class for remove_access_group_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_remove_access_group_rule_all_params(self):
        """
        remove_access_group_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.remove_access_group_rule(
            access_group_id,
            rule_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_remove_access_group_rule_all_params_with_retries(self):
        # Enable retries and run test_remove_access_group_rule_all_params.
        _service.enable_retries()
        self.test_remove_access_group_rule_all_params()

        # Disable retries and run test_remove_access_group_rule_all_params.
        _service.disable_retries()
        self.test_remove_access_group_rule_all_params()

    @responses.activate
    def test_remove_access_group_rule_required_params(self):
        """
        test_remove_access_group_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.remove_access_group_rule(
            access_group_id,
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_remove_access_group_rule_required_params_with_retries(self):
        # Enable retries and run test_remove_access_group_rule_required_params.
        _service.enable_retries()
        self.test_remove_access_group_rule_required_params()

        # Disable retries and run test_remove_access_group_rule_required_params.
        _service.disable_retries()
        self.test_remove_access_group_rule_required_params()

    @responses.activate
    def test_remove_access_group_rule_value_error(self):
        """
        test_remove_access_group_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/testString/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.remove_access_group_rule(**req_copy)


    def test_remove_access_group_rule_value_error_with_retries(self):
        # Enable retries and run test_remove_access_group_rule_value_error.
        _service.enable_retries()
        self.test_remove_access_group_rule_value_error()

        # Disable retries and run test_remove_access_group_rule_value_error.
        _service.disable_retries()
        self.test_remove_access_group_rule_value_error()

# endregion
##############################################################################
# End of Service: RuleOperations
##############################################################################

##############################################################################
# Start of Service: AccountSettings
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

        service = IamAccessGroupsV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamAccessGroupsV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamAccessGroupsV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestGetAccountSettings():
    """
    Test Class for get_account_settings
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_account_settings_all_params(self):
        """
        get_account_settings()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_account_settings(
            account_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_get_account_settings_all_params_with_retries(self):
        # Enable retries and run test_get_account_settings_all_params.
        _service.enable_retries()
        self.test_get_account_settings_all_params()

        # Disable retries and run test_get_account_settings_all_params.
        _service.disable_retries()
        self.test_get_account_settings_all_params()

    @responses.activate
    def test_get_account_settings_required_params(self):
        """
        test_get_account_settings_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.get_account_settings(
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

    def test_get_account_settings_required_params_with_retries(self):
        # Enable retries and run test_get_account_settings_required_params.
        _service.enable_retries()
        self.test_get_account_settings_required_params()

        # Disable retries and run test_get_account_settings_required_params.
        _service.disable_retries()
        self.test_get_account_settings_required_params()

    @responses.activate
    def test_get_account_settings_value_error(self):
        """
        test_get_account_settings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
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
                _service.get_account_settings(**req_copy)


    def test_get_account_settings_value_error_with_retries(self):
        # Enable retries and run test_get_account_settings_value_error.
        _service.enable_retries()
        self.test_get_account_settings_value_error()

        # Disable retries and run test_get_account_settings_value_error.
        _service.disable_retries()
        self.test_get_account_settings_value_error()

class TestUpdateAccountSettings():
    """
    Test Class for update_account_settings
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_account_settings_all_params(self):
        """
        update_account_settings()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        public_access_enabled = True
        transaction_id = 'testString'

        # Invoke method
        response = _service.update_account_settings(
            account_id,
            public_access_enabled=public_access_enabled,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['public_access_enabled'] == True

    def test_update_account_settings_all_params_with_retries(self):
        # Enable retries and run test_update_account_settings_all_params.
        _service.enable_retries()
        self.test_update_account_settings_all_params()

        # Disable retries and run test_update_account_settings_all_params.
        _service.disable_retries()
        self.test_update_account_settings_all_params()

    @responses.activate
    def test_update_account_settings_required_params(self):
        """
        test_update_account_settings_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        public_access_enabled = True

        # Invoke method
        response = _service.update_account_settings(
            account_id,
            public_access_enabled=public_access_enabled,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['public_access_enabled'] == True

    def test_update_account_settings_required_params_with_retries(self):
        # Enable retries and run test_update_account_settings_required_params.
        _service.enable_retries()
        self.test_update_account_settings_required_params()

        # Disable retries and run test_update_account_settings_required_params.
        _service.disable_retries()
        self.test_update_account_settings_required_params()

    @responses.activate
    def test_update_account_settings_value_error(self):
        """
        test_update_account_settings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        public_access_enabled = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_account_settings(**req_copy)


    def test_update_account_settings_value_error_with_retries(self):
        # Enable retries and run test_update_account_settings_value_error.
        _service.enable_retries()
        self.test_update_account_settings_value_error()

        # Disable retries and run test_update_account_settings_value_error.
        _service.disable_retries()
        self.test_update_account_settings_value_error()

# endregion
##############################################################################
# End of Service: AccountSettings
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AccountSettings():
    """
    Test Class for AccountSettings
    """

    def test_account_settings_serialization(self):
        """
        Test serialization/deserialization for AccountSettings
        """

        # Construct a json representation of a AccountSettings model
        account_settings_model_json = {}
        account_settings_model_json['account_id'] = 'testString'
        account_settings_model_json['last_modified_at'] = "2019-01-01T12:00:00Z"
        account_settings_model_json['last_modified_by_id'] = 'testString'
        account_settings_model_json['public_access_enabled'] = True

        # Construct a model instance of AccountSettings by calling from_dict on the json representation
        account_settings_model = AccountSettings.from_dict(account_settings_model_json)
        assert account_settings_model != False

        # Construct a model instance of AccountSettings by calling from_dict on the json representation
        account_settings_model_dict = AccountSettings.from_dict(account_settings_model_json).__dict__
        account_settings_model2 = AccountSettings(**account_settings_model_dict)

        # Verify the model instances are equivalent
        assert account_settings_model == account_settings_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_model_json2 = account_settings_model.to_dict()
        assert account_settings_model_json2 == account_settings_model_json

class TestModel_AddGroupMembersRequestMembersItem():
    """
    Test Class for AddGroupMembersRequestMembersItem
    """

    def test_add_group_members_request_members_item_serialization(self):
        """
        Test serialization/deserialization for AddGroupMembersRequestMembersItem
        """

        # Construct a json representation of a AddGroupMembersRequestMembersItem model
        add_group_members_request_members_item_model_json = {}
        add_group_members_request_members_item_model_json['iam_id'] = 'testString'
        add_group_members_request_members_item_model_json['type'] = 'testString'

        # Construct a model instance of AddGroupMembersRequestMembersItem by calling from_dict on the json representation
        add_group_members_request_members_item_model = AddGroupMembersRequestMembersItem.from_dict(add_group_members_request_members_item_model_json)
        assert add_group_members_request_members_item_model != False

        # Construct a model instance of AddGroupMembersRequestMembersItem by calling from_dict on the json representation
        add_group_members_request_members_item_model_dict = AddGroupMembersRequestMembersItem.from_dict(add_group_members_request_members_item_model_json).__dict__
        add_group_members_request_members_item_model2 = AddGroupMembersRequestMembersItem(**add_group_members_request_members_item_model_dict)

        # Verify the model instances are equivalent
        assert add_group_members_request_members_item_model == add_group_members_request_members_item_model2

        # Convert model instance back to dict and verify no loss of data
        add_group_members_request_members_item_model_json2 = add_group_members_request_members_item_model.to_dict()
        assert add_group_members_request_members_item_model_json2 == add_group_members_request_members_item_model_json

class TestModel_AddGroupMembersResponse():
    """
    Test Class for AddGroupMembersResponse
    """

    def test_add_group_members_response_serialization(self):
        """
        Test serialization/deserialization for AddGroupMembersResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {} # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        add_group_members_response_members_item_model = {} # AddGroupMembersResponseMembersItem
        add_group_members_response_members_item_model['iam_id'] = 'testString'
        add_group_members_response_members_item_model['type'] = 'testString'
        add_group_members_response_members_item_model['created_at'] = "2019-01-01T12:00:00Z"
        add_group_members_response_members_item_model['created_by_id'] = 'testString'
        add_group_members_response_members_item_model['status_code'] = 38
        add_group_members_response_members_item_model['trace'] = 'testString'
        add_group_members_response_members_item_model['errors'] = [error_model]

        # Construct a json representation of a AddGroupMembersResponse model
        add_group_members_response_model_json = {}
        add_group_members_response_model_json['members'] = [add_group_members_response_members_item_model]

        # Construct a model instance of AddGroupMembersResponse by calling from_dict on the json representation
        add_group_members_response_model = AddGroupMembersResponse.from_dict(add_group_members_response_model_json)
        assert add_group_members_response_model != False

        # Construct a model instance of AddGroupMembersResponse by calling from_dict on the json representation
        add_group_members_response_model_dict = AddGroupMembersResponse.from_dict(add_group_members_response_model_json).__dict__
        add_group_members_response_model2 = AddGroupMembersResponse(**add_group_members_response_model_dict)

        # Verify the model instances are equivalent
        assert add_group_members_response_model == add_group_members_response_model2

        # Convert model instance back to dict and verify no loss of data
        add_group_members_response_model_json2 = add_group_members_response_model.to_dict()
        assert add_group_members_response_model_json2 == add_group_members_response_model_json

class TestModel_AddGroupMembersResponseMembersItem():
    """
    Test Class for AddGroupMembersResponseMembersItem
    """

    def test_add_group_members_response_members_item_serialization(self):
        """
        Test serialization/deserialization for AddGroupMembersResponseMembersItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {} # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        # Construct a json representation of a AddGroupMembersResponseMembersItem model
        add_group_members_response_members_item_model_json = {}
        add_group_members_response_members_item_model_json['iam_id'] = 'testString'
        add_group_members_response_members_item_model_json['type'] = 'testString'
        add_group_members_response_members_item_model_json['created_at'] = "2019-01-01T12:00:00Z"
        add_group_members_response_members_item_model_json['created_by_id'] = 'testString'
        add_group_members_response_members_item_model_json['status_code'] = 38
        add_group_members_response_members_item_model_json['trace'] = 'testString'
        add_group_members_response_members_item_model_json['errors'] = [error_model]

        # Construct a model instance of AddGroupMembersResponseMembersItem by calling from_dict on the json representation
        add_group_members_response_members_item_model = AddGroupMembersResponseMembersItem.from_dict(add_group_members_response_members_item_model_json)
        assert add_group_members_response_members_item_model != False

        # Construct a model instance of AddGroupMembersResponseMembersItem by calling from_dict on the json representation
        add_group_members_response_members_item_model_dict = AddGroupMembersResponseMembersItem.from_dict(add_group_members_response_members_item_model_json).__dict__
        add_group_members_response_members_item_model2 = AddGroupMembersResponseMembersItem(**add_group_members_response_members_item_model_dict)

        # Verify the model instances are equivalent
        assert add_group_members_response_members_item_model == add_group_members_response_members_item_model2

        # Convert model instance back to dict and verify no loss of data
        add_group_members_response_members_item_model_json2 = add_group_members_response_members_item_model.to_dict()
        assert add_group_members_response_members_item_model_json2 == add_group_members_response_members_item_model_json

class TestModel_AddMembershipMultipleGroupsResponse():
    """
    Test Class for AddMembershipMultipleGroupsResponse
    """

    def test_add_membership_multiple_groups_response_serialization(self):
        """
        Test serialization/deserialization for AddMembershipMultipleGroupsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {} # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        add_membership_multiple_groups_response_groups_item_model = {} # AddMembershipMultipleGroupsResponseGroupsItem
        add_membership_multiple_groups_response_groups_item_model['access_group_id'] = 'testString'
        add_membership_multiple_groups_response_groups_item_model['status_code'] = 38
        add_membership_multiple_groups_response_groups_item_model['trace'] = 'testString'
        add_membership_multiple_groups_response_groups_item_model['errors'] = [error_model]

        # Construct a json representation of a AddMembershipMultipleGroupsResponse model
        add_membership_multiple_groups_response_model_json = {}
        add_membership_multiple_groups_response_model_json['iam_id'] = 'testString'
        add_membership_multiple_groups_response_model_json['groups'] = [add_membership_multiple_groups_response_groups_item_model]

        # Construct a model instance of AddMembershipMultipleGroupsResponse by calling from_dict on the json representation
        add_membership_multiple_groups_response_model = AddMembershipMultipleGroupsResponse.from_dict(add_membership_multiple_groups_response_model_json)
        assert add_membership_multiple_groups_response_model != False

        # Construct a model instance of AddMembershipMultipleGroupsResponse by calling from_dict on the json representation
        add_membership_multiple_groups_response_model_dict = AddMembershipMultipleGroupsResponse.from_dict(add_membership_multiple_groups_response_model_json).__dict__
        add_membership_multiple_groups_response_model2 = AddMembershipMultipleGroupsResponse(**add_membership_multiple_groups_response_model_dict)

        # Verify the model instances are equivalent
        assert add_membership_multiple_groups_response_model == add_membership_multiple_groups_response_model2

        # Convert model instance back to dict and verify no loss of data
        add_membership_multiple_groups_response_model_json2 = add_membership_multiple_groups_response_model.to_dict()
        assert add_membership_multiple_groups_response_model_json2 == add_membership_multiple_groups_response_model_json

class TestModel_AddMembershipMultipleGroupsResponseGroupsItem():
    """
    Test Class for AddMembershipMultipleGroupsResponseGroupsItem
    """

    def test_add_membership_multiple_groups_response_groups_item_serialization(self):
        """
        Test serialization/deserialization for AddMembershipMultipleGroupsResponseGroupsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {} # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        # Construct a json representation of a AddMembershipMultipleGroupsResponseGroupsItem model
        add_membership_multiple_groups_response_groups_item_model_json = {}
        add_membership_multiple_groups_response_groups_item_model_json['access_group_id'] = 'testString'
        add_membership_multiple_groups_response_groups_item_model_json['status_code'] = 38
        add_membership_multiple_groups_response_groups_item_model_json['trace'] = 'testString'
        add_membership_multiple_groups_response_groups_item_model_json['errors'] = [error_model]

        # Construct a model instance of AddMembershipMultipleGroupsResponseGroupsItem by calling from_dict on the json representation
        add_membership_multiple_groups_response_groups_item_model = AddMembershipMultipleGroupsResponseGroupsItem.from_dict(add_membership_multiple_groups_response_groups_item_model_json)
        assert add_membership_multiple_groups_response_groups_item_model != False

        # Construct a model instance of AddMembershipMultipleGroupsResponseGroupsItem by calling from_dict on the json representation
        add_membership_multiple_groups_response_groups_item_model_dict = AddMembershipMultipleGroupsResponseGroupsItem.from_dict(add_membership_multiple_groups_response_groups_item_model_json).__dict__
        add_membership_multiple_groups_response_groups_item_model2 = AddMembershipMultipleGroupsResponseGroupsItem(**add_membership_multiple_groups_response_groups_item_model_dict)

        # Verify the model instances are equivalent
        assert add_membership_multiple_groups_response_groups_item_model == add_membership_multiple_groups_response_groups_item_model2

        # Convert model instance back to dict and verify no loss of data
        add_membership_multiple_groups_response_groups_item_model_json2 = add_membership_multiple_groups_response_groups_item_model.to_dict()
        assert add_membership_multiple_groups_response_groups_item_model_json2 == add_membership_multiple_groups_response_groups_item_model_json

class TestModel_DeleteFromAllGroupsResponse():
    """
    Test Class for DeleteFromAllGroupsResponse
    """

    def test_delete_from_all_groups_response_serialization(self):
        """
        Test serialization/deserialization for DeleteFromAllGroupsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {} # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        delete_from_all_groups_response_groups_item_model = {} # DeleteFromAllGroupsResponseGroupsItem
        delete_from_all_groups_response_groups_item_model['access_group_id'] = 'testString'
        delete_from_all_groups_response_groups_item_model['status_code'] = 38
        delete_from_all_groups_response_groups_item_model['trace'] = 'testString'
        delete_from_all_groups_response_groups_item_model['errors'] = [error_model]

        # Construct a json representation of a DeleteFromAllGroupsResponse model
        delete_from_all_groups_response_model_json = {}
        delete_from_all_groups_response_model_json['iam_id'] = 'testString'
        delete_from_all_groups_response_model_json['groups'] = [delete_from_all_groups_response_groups_item_model]

        # Construct a model instance of DeleteFromAllGroupsResponse by calling from_dict on the json representation
        delete_from_all_groups_response_model = DeleteFromAllGroupsResponse.from_dict(delete_from_all_groups_response_model_json)
        assert delete_from_all_groups_response_model != False

        # Construct a model instance of DeleteFromAllGroupsResponse by calling from_dict on the json representation
        delete_from_all_groups_response_model_dict = DeleteFromAllGroupsResponse.from_dict(delete_from_all_groups_response_model_json).__dict__
        delete_from_all_groups_response_model2 = DeleteFromAllGroupsResponse(**delete_from_all_groups_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_from_all_groups_response_model == delete_from_all_groups_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_from_all_groups_response_model_json2 = delete_from_all_groups_response_model.to_dict()
        assert delete_from_all_groups_response_model_json2 == delete_from_all_groups_response_model_json

class TestModel_DeleteFromAllGroupsResponseGroupsItem():
    """
    Test Class for DeleteFromAllGroupsResponseGroupsItem
    """

    def test_delete_from_all_groups_response_groups_item_serialization(self):
        """
        Test serialization/deserialization for DeleteFromAllGroupsResponseGroupsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {} # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        # Construct a json representation of a DeleteFromAllGroupsResponseGroupsItem model
        delete_from_all_groups_response_groups_item_model_json = {}
        delete_from_all_groups_response_groups_item_model_json['access_group_id'] = 'testString'
        delete_from_all_groups_response_groups_item_model_json['status_code'] = 38
        delete_from_all_groups_response_groups_item_model_json['trace'] = 'testString'
        delete_from_all_groups_response_groups_item_model_json['errors'] = [error_model]

        # Construct a model instance of DeleteFromAllGroupsResponseGroupsItem by calling from_dict on the json representation
        delete_from_all_groups_response_groups_item_model = DeleteFromAllGroupsResponseGroupsItem.from_dict(delete_from_all_groups_response_groups_item_model_json)
        assert delete_from_all_groups_response_groups_item_model != False

        # Construct a model instance of DeleteFromAllGroupsResponseGroupsItem by calling from_dict on the json representation
        delete_from_all_groups_response_groups_item_model_dict = DeleteFromAllGroupsResponseGroupsItem.from_dict(delete_from_all_groups_response_groups_item_model_json).__dict__
        delete_from_all_groups_response_groups_item_model2 = DeleteFromAllGroupsResponseGroupsItem(**delete_from_all_groups_response_groups_item_model_dict)

        # Verify the model instances are equivalent
        assert delete_from_all_groups_response_groups_item_model == delete_from_all_groups_response_groups_item_model2

        # Convert model instance back to dict and verify no loss of data
        delete_from_all_groups_response_groups_item_model_json2 = delete_from_all_groups_response_groups_item_model.to_dict()
        assert delete_from_all_groups_response_groups_item_model_json2 == delete_from_all_groups_response_groups_item_model_json

class TestModel_DeleteGroupBulkMembersResponse():
    """
    Test Class for DeleteGroupBulkMembersResponse
    """

    def test_delete_group_bulk_members_response_serialization(self):
        """
        Test serialization/deserialization for DeleteGroupBulkMembersResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {} # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        delete_group_bulk_members_response_members_item_model = {} # DeleteGroupBulkMembersResponseMembersItem
        delete_group_bulk_members_response_members_item_model['iam_id'] = 'testString'
        delete_group_bulk_members_response_members_item_model['trace'] = 'testString'
        delete_group_bulk_members_response_members_item_model['status_code'] = 38
        delete_group_bulk_members_response_members_item_model['errors'] = [error_model]

        # Construct a json representation of a DeleteGroupBulkMembersResponse model
        delete_group_bulk_members_response_model_json = {}
        delete_group_bulk_members_response_model_json['access_group_id'] = 'testString'
        delete_group_bulk_members_response_model_json['members'] = [delete_group_bulk_members_response_members_item_model]

        # Construct a model instance of DeleteGroupBulkMembersResponse by calling from_dict on the json representation
        delete_group_bulk_members_response_model = DeleteGroupBulkMembersResponse.from_dict(delete_group_bulk_members_response_model_json)
        assert delete_group_bulk_members_response_model != False

        # Construct a model instance of DeleteGroupBulkMembersResponse by calling from_dict on the json representation
        delete_group_bulk_members_response_model_dict = DeleteGroupBulkMembersResponse.from_dict(delete_group_bulk_members_response_model_json).__dict__
        delete_group_bulk_members_response_model2 = DeleteGroupBulkMembersResponse(**delete_group_bulk_members_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_group_bulk_members_response_model == delete_group_bulk_members_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_group_bulk_members_response_model_json2 = delete_group_bulk_members_response_model.to_dict()
        assert delete_group_bulk_members_response_model_json2 == delete_group_bulk_members_response_model_json

class TestModel_DeleteGroupBulkMembersResponseMembersItem():
    """
    Test Class for DeleteGroupBulkMembersResponseMembersItem
    """

    def test_delete_group_bulk_members_response_members_item_serialization(self):
        """
        Test serialization/deserialization for DeleteGroupBulkMembersResponseMembersItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {} # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        # Construct a json representation of a DeleteGroupBulkMembersResponseMembersItem model
        delete_group_bulk_members_response_members_item_model_json = {}
        delete_group_bulk_members_response_members_item_model_json['iam_id'] = 'testString'
        delete_group_bulk_members_response_members_item_model_json['trace'] = 'testString'
        delete_group_bulk_members_response_members_item_model_json['status_code'] = 38
        delete_group_bulk_members_response_members_item_model_json['errors'] = [error_model]

        # Construct a model instance of DeleteGroupBulkMembersResponseMembersItem by calling from_dict on the json representation
        delete_group_bulk_members_response_members_item_model = DeleteGroupBulkMembersResponseMembersItem.from_dict(delete_group_bulk_members_response_members_item_model_json)
        assert delete_group_bulk_members_response_members_item_model != False

        # Construct a model instance of DeleteGroupBulkMembersResponseMembersItem by calling from_dict on the json representation
        delete_group_bulk_members_response_members_item_model_dict = DeleteGroupBulkMembersResponseMembersItem.from_dict(delete_group_bulk_members_response_members_item_model_json).__dict__
        delete_group_bulk_members_response_members_item_model2 = DeleteGroupBulkMembersResponseMembersItem(**delete_group_bulk_members_response_members_item_model_dict)

        # Verify the model instances are equivalent
        assert delete_group_bulk_members_response_members_item_model == delete_group_bulk_members_response_members_item_model2

        # Convert model instance back to dict and verify no loss of data
        delete_group_bulk_members_response_members_item_model_json2 = delete_group_bulk_members_response_members_item_model.to_dict()
        assert delete_group_bulk_members_response_members_item_model_json2 == delete_group_bulk_members_response_members_item_model_json

class TestModel_Error():
    """
    Test Class for Error
    """

    def test_error_serialization(self):
        """
        Test serialization/deserialization for Error
        """

        # Construct a json representation of a Error model
        error_model_json = {}
        error_model_json['code'] = 'testString'
        error_model_json['message'] = 'testString'

        # Construct a model instance of Error by calling from_dict on the json representation
        error_model = Error.from_dict(error_model_json)
        assert error_model != False

        # Construct a model instance of Error by calling from_dict on the json representation
        error_model_dict = Error.from_dict(error_model_json).__dict__
        error_model2 = Error(**error_model_dict)

        # Verify the model instances are equivalent
        assert error_model == error_model2

        # Convert model instance back to dict and verify no loss of data
        error_model_json2 = error_model.to_dict()
        assert error_model_json2 == error_model_json

class TestModel_Group():
    """
    Test Class for Group
    """

    def test_group_serialization(self):
        """
        Test serialization/deserialization for Group
        """

        # Construct a json representation of a Group model
        group_model_json = {}
        group_model_json['id'] = 'testString'
        group_model_json['name'] = 'testString'
        group_model_json['description'] = 'testString'
        group_model_json['account_id'] = 'testString'
        group_model_json['created_at'] = "2019-01-01T12:00:00Z"
        group_model_json['created_by_id'] = 'testString'
        group_model_json['last_modified_at'] = "2019-01-01T12:00:00Z"
        group_model_json['last_modified_by_id'] = 'testString'
        group_model_json['href'] = 'testString'
        group_model_json['is_federated'] = True

        # Construct a model instance of Group by calling from_dict on the json representation
        group_model = Group.from_dict(group_model_json)
        assert group_model != False

        # Construct a model instance of Group by calling from_dict on the json representation
        group_model_dict = Group.from_dict(group_model_json).__dict__
        group_model2 = Group(**group_model_dict)

        # Verify the model instances are equivalent
        assert group_model == group_model2

        # Convert model instance back to dict and verify no loss of data
        group_model_json2 = group_model.to_dict()
        assert group_model_json2 == group_model_json

class TestModel_GroupMembersList():
    """
    Test Class for GroupMembersList
    """

    def test_group_members_list_serialization(self):
        """
        Test serialization/deserialization for GroupMembersList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        href_struct_model = {} # HrefStruct
        href_struct_model['href'] = 'testString'

        list_group_members_response_member_model = {} # ListGroupMembersResponseMember
        list_group_members_response_member_model['iam_id'] = 'testString'
        list_group_members_response_member_model['type'] = 'testString'
        list_group_members_response_member_model['name'] = 'testString'
        list_group_members_response_member_model['email'] = 'testString'
        list_group_members_response_member_model['description'] = 'testString'
        list_group_members_response_member_model['href'] = 'testString'
        list_group_members_response_member_model['created_at'] = "2019-01-01T12:00:00Z"
        list_group_members_response_member_model['created_by_id'] = 'testString'

        # Construct a json representation of a GroupMembersList model
        group_members_list_model_json = {}
        group_members_list_model_json['limit'] = 38
        group_members_list_model_json['offset'] = 38
        group_members_list_model_json['total_count'] = 38
        group_members_list_model_json['first'] = href_struct_model
        group_members_list_model_json['previous'] = href_struct_model
        group_members_list_model_json['next'] = href_struct_model
        group_members_list_model_json['last'] = href_struct_model
        group_members_list_model_json['members'] = [list_group_members_response_member_model]

        # Construct a model instance of GroupMembersList by calling from_dict on the json representation
        group_members_list_model = GroupMembersList.from_dict(group_members_list_model_json)
        assert group_members_list_model != False

        # Construct a model instance of GroupMembersList by calling from_dict on the json representation
        group_members_list_model_dict = GroupMembersList.from_dict(group_members_list_model_json).__dict__
        group_members_list_model2 = GroupMembersList(**group_members_list_model_dict)

        # Verify the model instances are equivalent
        assert group_members_list_model == group_members_list_model2

        # Convert model instance back to dict and verify no loss of data
        group_members_list_model_json2 = group_members_list_model.to_dict()
        assert group_members_list_model_json2 == group_members_list_model_json

class TestModel_GroupsList():
    """
    Test Class for GroupsList
    """

    def test_groups_list_serialization(self):
        """
        Test serialization/deserialization for GroupsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        href_struct_model = {} # HrefStruct
        href_struct_model['href'] = 'testString'

        group_model = {} # Group
        group_model['id'] = 'testString'
        group_model['name'] = 'testString'
        group_model['description'] = 'testString'
        group_model['account_id'] = 'testString'
        group_model['created_at'] = "2019-01-01T12:00:00Z"
        group_model['created_by_id'] = 'testString'
        group_model['last_modified_at'] = "2019-01-01T12:00:00Z"
        group_model['last_modified_by_id'] = 'testString'
        group_model['href'] = 'testString'
        group_model['is_federated'] = True

        # Construct a json representation of a GroupsList model
        groups_list_model_json = {}
        groups_list_model_json['limit'] = 38
        groups_list_model_json['offset'] = 38
        groups_list_model_json['total_count'] = 38
        groups_list_model_json['first'] = href_struct_model
        groups_list_model_json['previous'] = href_struct_model
        groups_list_model_json['next'] = href_struct_model
        groups_list_model_json['last'] = href_struct_model
        groups_list_model_json['groups'] = [group_model]

        # Construct a model instance of GroupsList by calling from_dict on the json representation
        groups_list_model = GroupsList.from_dict(groups_list_model_json)
        assert groups_list_model != False

        # Construct a model instance of GroupsList by calling from_dict on the json representation
        groups_list_model_dict = GroupsList.from_dict(groups_list_model_json).__dict__
        groups_list_model2 = GroupsList(**groups_list_model_dict)

        # Verify the model instances are equivalent
        assert groups_list_model == groups_list_model2

        # Convert model instance back to dict and verify no loss of data
        groups_list_model_json2 = groups_list_model.to_dict()
        assert groups_list_model_json2 == groups_list_model_json

class TestModel_HrefStruct():
    """
    Test Class for HrefStruct
    """

    def test_href_struct_serialization(self):
        """
        Test serialization/deserialization for HrefStruct
        """

        # Construct a json representation of a HrefStruct model
        href_struct_model_json = {}
        href_struct_model_json['href'] = 'testString'

        # Construct a model instance of HrefStruct by calling from_dict on the json representation
        href_struct_model = HrefStruct.from_dict(href_struct_model_json)
        assert href_struct_model != False

        # Construct a model instance of HrefStruct by calling from_dict on the json representation
        href_struct_model_dict = HrefStruct.from_dict(href_struct_model_json).__dict__
        href_struct_model2 = HrefStruct(**href_struct_model_dict)

        # Verify the model instances are equivalent
        assert href_struct_model == href_struct_model2

        # Convert model instance back to dict and verify no loss of data
        href_struct_model_json2 = href_struct_model.to_dict()
        assert href_struct_model_json2 == href_struct_model_json

class TestModel_ListGroupMembersResponseMember():
    """
    Test Class for ListGroupMembersResponseMember
    """

    def test_list_group_members_response_member_serialization(self):
        """
        Test serialization/deserialization for ListGroupMembersResponseMember
        """

        # Construct a json representation of a ListGroupMembersResponseMember model
        list_group_members_response_member_model_json = {}
        list_group_members_response_member_model_json['iam_id'] = 'testString'
        list_group_members_response_member_model_json['type'] = 'testString'
        list_group_members_response_member_model_json['name'] = 'testString'
        list_group_members_response_member_model_json['email'] = 'testString'
        list_group_members_response_member_model_json['description'] = 'testString'
        list_group_members_response_member_model_json['href'] = 'testString'
        list_group_members_response_member_model_json['created_at'] = "2019-01-01T12:00:00Z"
        list_group_members_response_member_model_json['created_by_id'] = 'testString'

        # Construct a model instance of ListGroupMembersResponseMember by calling from_dict on the json representation
        list_group_members_response_member_model = ListGroupMembersResponseMember.from_dict(list_group_members_response_member_model_json)
        assert list_group_members_response_member_model != False

        # Construct a model instance of ListGroupMembersResponseMember by calling from_dict on the json representation
        list_group_members_response_member_model_dict = ListGroupMembersResponseMember.from_dict(list_group_members_response_member_model_json).__dict__
        list_group_members_response_member_model2 = ListGroupMembersResponseMember(**list_group_members_response_member_model_dict)

        # Verify the model instances are equivalent
        assert list_group_members_response_member_model == list_group_members_response_member_model2

        # Convert model instance back to dict and verify no loss of data
        list_group_members_response_member_model_json2 = list_group_members_response_member_model.to_dict()
        assert list_group_members_response_member_model_json2 == list_group_members_response_member_model_json

class TestModel_Rule():
    """
    Test Class for Rule
    """

    def test_rule_serialization(self):
        """
        Test serialization/deserialization for Rule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_conditions_model = {} # RuleConditions
        rule_conditions_model['claim'] = 'testString'
        rule_conditions_model['operator'] = 'EQUALS'
        rule_conditions_model['value'] = 'testString'

        # Construct a json representation of a Rule model
        rule_model_json = {}
        rule_model_json['id'] = 'testString'
        rule_model_json['name'] = 'testString'
        rule_model_json['expiration'] = 38
        rule_model_json['realm_name'] = 'testString'
        rule_model_json['access_group_id'] = 'testString'
        rule_model_json['account_id'] = 'testString'
        rule_model_json['conditions'] = [rule_conditions_model]
        rule_model_json['created_at'] = "2019-01-01T12:00:00Z"
        rule_model_json['created_by_id'] = 'testString'
        rule_model_json['last_modified_at'] = "2019-01-01T12:00:00Z"
        rule_model_json['last_modified_by_id'] = 'testString'

        # Construct a model instance of Rule by calling from_dict on the json representation
        rule_model = Rule.from_dict(rule_model_json)
        assert rule_model != False

        # Construct a model instance of Rule by calling from_dict on the json representation
        rule_model_dict = Rule.from_dict(rule_model_json).__dict__
        rule_model2 = Rule(**rule_model_dict)

        # Verify the model instances are equivalent
        assert rule_model == rule_model2

        # Convert model instance back to dict and verify no loss of data
        rule_model_json2 = rule_model.to_dict()
        assert rule_model_json2 == rule_model_json

class TestModel_RuleConditions():
    """
    Test Class for RuleConditions
    """

    def test_rule_conditions_serialization(self):
        """
        Test serialization/deserialization for RuleConditions
        """

        # Construct a json representation of a RuleConditions model
        rule_conditions_model_json = {}
        rule_conditions_model_json['claim'] = 'testString'
        rule_conditions_model_json['operator'] = 'EQUALS'
        rule_conditions_model_json['value'] = 'testString'

        # Construct a model instance of RuleConditions by calling from_dict on the json representation
        rule_conditions_model = RuleConditions.from_dict(rule_conditions_model_json)
        assert rule_conditions_model != False

        # Construct a model instance of RuleConditions by calling from_dict on the json representation
        rule_conditions_model_dict = RuleConditions.from_dict(rule_conditions_model_json).__dict__
        rule_conditions_model2 = RuleConditions(**rule_conditions_model_dict)

        # Verify the model instances are equivalent
        assert rule_conditions_model == rule_conditions_model2

        # Convert model instance back to dict and verify no loss of data
        rule_conditions_model_json2 = rule_conditions_model.to_dict()
        assert rule_conditions_model_json2 == rule_conditions_model_json

class TestModel_RulesList():
    """
    Test Class for RulesList
    """

    def test_rules_list_serialization(self):
        """
        Test serialization/deserialization for RulesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_conditions_model = {} # RuleConditions
        rule_conditions_model['claim'] = 'testString'
        rule_conditions_model['operator'] = 'EQUALS'
        rule_conditions_model['value'] = 'testString'

        rule_model = {} # Rule
        rule_model['id'] = 'testString'
        rule_model['name'] = 'testString'
        rule_model['expiration'] = 38
        rule_model['realm_name'] = 'testString'
        rule_model['access_group_id'] = 'testString'
        rule_model['account_id'] = 'testString'
        rule_model['conditions'] = [rule_conditions_model]
        rule_model['created_at'] = "2019-01-01T12:00:00Z"
        rule_model['created_by_id'] = 'testString'
        rule_model['last_modified_at'] = "2019-01-01T12:00:00Z"
        rule_model['last_modified_by_id'] = 'testString'

        # Construct a json representation of a RulesList model
        rules_list_model_json = {}
        rules_list_model_json['rules'] = [rule_model]

        # Construct a model instance of RulesList by calling from_dict on the json representation
        rules_list_model = RulesList.from_dict(rules_list_model_json)
        assert rules_list_model != False

        # Construct a model instance of RulesList by calling from_dict on the json representation
        rules_list_model_dict = RulesList.from_dict(rules_list_model_json).__dict__
        rules_list_model2 = RulesList(**rules_list_model_dict)

        # Verify the model instances are equivalent
        assert rules_list_model == rules_list_model2

        # Convert model instance back to dict and verify no loss of data
        rules_list_model_json2 = rules_list_model.to_dict()
        assert rules_list_model_json2 == rules_list_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
