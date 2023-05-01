# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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


_service = IamAccessGroupsV2(authenticator=NoAuthAuthenticator())

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
# Start of Service: AccessGroupOperations
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


class TestCreateAccessGroup:
    """
    Test Class for create_access_group
    """

    @responses.activate
    def test_create_access_group_all_params(self):
        """
        create_access_group()
        """
        # Set up mock
        url = preprocess_url('/v2/groups')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        account_id = 'testString'
        name = 'Managers'
        description = 'Group for managers'

        # Invoke method
        response = _service.create_access_group(
            account_id,
            name,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_access_group(**req_copy)

    def test_create_access_group_value_error_with_retries(self):
        # Enable retries and run test_create_access_group_value_error.
        _service.enable_retries()
        self.test_create_access_group_value_error()

        # Disable retries and run test_create_access_group_value_error.
        _service.disable_retries()
        self.test_create_access_group_value_error()


class TestListAccessGroups:
    """
    Test Class for list_access_groups
    """

    @responses.activate
    def test_list_access_groups_all_params(self):
        """
        list_access_groups()
        """
        # Set up mock
        url = preprocess_url('/v2/groups')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups": [{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'
        iam_id = 'testString'
        search = 'testString'
        membership_type = 'static'
        limit = 100
        offset = 38
        sort = 'name'
        show_federated = False
        hide_public_access = False

        # Invoke method
        response = _service.list_access_groups(
            account_id,
            transaction_id=transaction_id,
            iam_id=iam_id,
            search=search,
            membership_type=membership_type,
            limit=limit,
            offset=offset,
            sort=sort,
            show_federated=show_federated,
            hide_public_access=hide_public_access,
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
        assert 'search={}'.format(search) in query_string
        assert 'membership_type={}'.format(membership_type) in query_string
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
        url = preprocess_url('/v2/groups')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups": [{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}]}'
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
        response = _service.list_access_groups(
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
        url = preprocess_url('/v2/groups')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups": [{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}]}'
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
                _service.list_access_groups(**req_copy)

    def test_list_access_groups_value_error_with_retries(self):
        # Enable retries and run test_list_access_groups_value_error.
        _service.enable_retries()
        self.test_list_access_groups_value_error()

        # Disable retries and run test_list_access_groups_value_error.
        _service.disable_retries()
        self.test_list_access_groups_value_error()

    @responses.activate
    def test_list_access_groups_with_pager_get_next(self):
        """
        test_list_access_groups_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/groups')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"groups":[{"id":"id","name":"name","description":"description","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","href":"href","is_federated":true}]}'
        mock_response2 = '{"total_count":2,"limit":1,"groups":[{"id":"id","name":"name","description":"description","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","href":"href","is_federated":true}]}'
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
        pager = AccessGroupsPager(
            client=_service,
            account_id='testString',
            transaction_id='testString',
            iam_id='testString',
            search='testString',
            membership_type='static',
            limit=10,
            sort='name',
            show_federated=False,
            hide_public_access=False,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_access_groups_with_pager_get_all(self):
        """
        test_list_access_groups_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/groups')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"groups":[{"id":"id","name":"name","description":"description","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","href":"href","is_federated":true}]}'
        mock_response2 = '{"total_count":2,"limit":1,"groups":[{"id":"id","name":"name","description":"description","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id","last_modified_at":"2019-01-01T12:00:00.000Z","last_modified_by_id":"last_modified_by_id","href":"href","is_federated":true}]}'
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
        pager = AccessGroupsPager(
            client=_service,
            account_id='testString',
            transaction_id='testString',
            iam_id='testString',
            search='testString',
            membership_type='static',
            limit=10,
            sort='name',
            show_federated=False,
            hide_public_access=False,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetAccessGroup:
    """
    Test Class for get_access_group
    """

    @responses.activate
    def test_get_access_group_all_params(self):
        """
        get_access_group()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'
        show_federated = False

        # Invoke method
        response = _service.get_access_group(
            access_group_id,
            transaction_id=transaction_id,
            show_federated=show_federated,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = _service.get_access_group(
            access_group_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_access_group(**req_copy)

    def test_get_access_group_value_error_with_retries(self):
        # Enable retries and run test_get_access_group_value_error.
        _service.enable_retries()
        self.test_get_access_group_value_error()

        # Disable retries and run test_get_access_group_value_error.
        _service.disable_retries()
        self.test_get_access_group_value_error()


class TestUpdateAccessGroup:
    """
    Test Class for update_access_group
    """

    @responses.activate
    def test_update_access_group_all_params(self):
        """
        update_access_group()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
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
        url = preprocess_url('/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
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
        url = preprocess_url('/v2/groups/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_access_group(**req_copy)

    def test_update_access_group_value_error_with_retries(self):
        # Enable retries and run test_update_access_group_value_error.
        _service.enable_retries()
        self.test_update_access_group_value_error()

        # Disable retries and run test_update_access_group_value_error.
        _service.disable_retries()
        self.test_update_access_group_value_error()


class TestDeleteAccessGroup:
    """
    Test Class for delete_access_group
    """

    @responses.activate
    def test_delete_access_group_all_params(self):
        """
        delete_access_group()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'
        force = False

        # Invoke method
        response = _service.delete_access_group(
            access_group_id,
            transaction_id=transaction_id,
            force=force,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = _service.delete_access_group(
            access_group_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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


class TestNewInstance:
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


class TestIsMemberOfAccessGroup:
    """
    Test Class for is_member_of_access_group
    """

    @responses.activate
    def test_is_member_of_access_group_all_params(self):
        """
        is_member_of_access_group()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/members/testString')
        responses.add(
            responses.HEAD,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.is_member_of_access_group(
            access_group_id,
            iam_id,
            transaction_id=transaction_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/members/testString')
        responses.add(
            responses.HEAD,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.is_member_of_access_group(
            access_group_id,
            iam_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/members/testString')
        responses.add(
            responses.HEAD,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.is_member_of_access_group(**req_copy)

    def test_is_member_of_access_group_value_error_with_retries(self):
        # Enable retries and run test_is_member_of_access_group_value_error.
        _service.enable_retries()
        self.test_is_member_of_access_group_value_error()

        # Disable retries and run test_is_member_of_access_group_value_error.
        _service.disable_retries()
        self.test_is_member_of_access_group_value_error()


class TestAddMembersToAccessGroup:
    """
    Test Class for add_members_to_access_group
    """

    @responses.activate
    def test_add_members_to_access_group_all_params(self):
        """
        add_members_to_access_group()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/members')
        mock_response = '{"members": [{"iam_id": "iam_id", "type": "type", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

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
            headers={},
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
        url = preprocess_url('/v2/groups/testString/members')
        mock_response = '{"members": [{"iam_id": "iam_id", "type": "type", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

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
            headers={},
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
        url = preprocess_url('/v2/groups/testString/members')
        mock_response = '{"members": [{"iam_id": "iam_id", "type": "type", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_members_to_access_group(**req_copy)

    def test_add_members_to_access_group_value_error_with_retries(self):
        # Enable retries and run test_add_members_to_access_group_value_error.
        _service.enable_retries()
        self.test_add_members_to_access_group_value_error()

        # Disable retries and run test_add_members_to_access_group_value_error.
        _service.disable_retries()
        self.test_add_members_to_access_group_value_error()


class TestListAccessGroupMembers:
    """
    Test Class for list_access_group_members
    """

    @responses.activate
    def test_list_access_group_members_all_params(self):
        """
        list_access_group_members()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/members')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "members": [{"iam_id": "iam_id", "type": "type", "membership_type": "membership_type", "name": "name", "email": "email", "description": "description", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'
        membership_type = 'static'
        limit = 100
        offset = 38
        type = 'testString'
        verbose = False
        sort = 'testString'

        # Invoke method
        response = _service.list_access_group_members(
            access_group_id,
            transaction_id=transaction_id,
            membership_type=membership_type,
            limit=limit,
            offset=offset,
            type=type,
            verbose=verbose,
            sort=sort,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'membership_type={}'.format(membership_type) in query_string
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
        url = preprocess_url('/v2/groups/testString/members')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "members": [{"iam_id": "iam_id", "type": "type", "membership_type": "membership_type", "name": "name", "email": "email", "description": "description", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = _service.list_access_group_members(
            access_group_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/members')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "members": [{"iam_id": "iam_id", "type": "type", "membership_type": "membership_type", "name": "name", "email": "email", "description": "description", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_access_group_members(**req_copy)

    def test_list_access_group_members_value_error_with_retries(self):
        # Enable retries and run test_list_access_group_members_value_error.
        _service.enable_retries()
        self.test_list_access_group_members_value_error()

        # Disable retries and run test_list_access_group_members_value_error.
        _service.disable_retries()
        self.test_list_access_group_members_value_error()

    @responses.activate
    def test_list_access_group_members_with_pager_get_next(self):
        """
        test_list_access_group_members_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/groups/testString/members')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"members":[{"iam_id":"iam_id","type":"type","membership_type":"membership_type","name":"name","email":"email","description":"description","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id"}],"limit":1}'
        mock_response2 = '{"total_count":2,"members":[{"iam_id":"iam_id","type":"type","membership_type":"membership_type","name":"name","email":"email","description":"description","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id"}],"limit":1}'
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
        pager = AccessGroupMembersPager(
            client=_service,
            access_group_id='testString',
            transaction_id='testString',
            membership_type='static',
            limit=10,
            type='testString',
            verbose=False,
            sort='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_access_group_members_with_pager_get_all(self):
        """
        test_list_access_group_members_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/groups/testString/members')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"members":[{"iam_id":"iam_id","type":"type","membership_type":"membership_type","name":"name","email":"email","description":"description","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id"}],"limit":1}'
        mock_response2 = '{"total_count":2,"members":[{"iam_id":"iam_id","type":"type","membership_type":"membership_type","name":"name","email":"email","description":"description","href":"href","created_at":"2019-01-01T12:00:00.000Z","created_by_id":"created_by_id"}],"limit":1}'
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
        pager = AccessGroupMembersPager(
            client=_service,
            access_group_id='testString',
            transaction_id='testString',
            membership_type='static',
            limit=10,
            type='testString',
            verbose=False,
            sort='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestRemoveMemberFromAccessGroup:
    """
    Test Class for remove_member_from_access_group
    """

    @responses.activate
    def test_remove_member_from_access_group_all_params(self):
        """
        remove_member_from_access_group()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/members/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.remove_member_from_access_group(
            access_group_id,
            iam_id,
            transaction_id=transaction_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/members/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.remove_member_from_access_group(
            access_group_id,
            iam_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/members/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.remove_member_from_access_group(**req_copy)

    def test_remove_member_from_access_group_value_error_with_retries(self):
        # Enable retries and run test_remove_member_from_access_group_value_error.
        _service.enable_retries()
        self.test_remove_member_from_access_group_value_error()

        # Disable retries and run test_remove_member_from_access_group_value_error.
        _service.disable_retries()
        self.test_remove_member_from_access_group_value_error()


class TestRemoveMembersFromAccessGroup:
    """
    Test Class for remove_members_from_access_group
    """

    @responses.activate
    def test_remove_members_from_access_group_all_params(self):
        """
        remove_members_from_access_group()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/members/delete')
        mock_response = '{"access_group_id": "access_group_id", "members": [{"iam_id": "iam_id", "trace": "trace", "status_code": 11, "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

        # Set up parameter values
        access_group_id = 'testString'
        members = ['IBMId-user1', 'iam-ServiceId-123', 'iam-Profile-123']
        transaction_id = 'testString'

        # Invoke method
        response = _service.remove_members_from_access_group(
            access_group_id,
            members=members,
            transaction_id=transaction_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/members/delete')
        mock_response = '{"access_group_id": "access_group_id", "members": [{"iam_id": "iam_id", "trace": "trace", "status_code": 11, "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

        # Set up parameter values
        access_group_id = 'testString'
        members = ['IBMId-user1', 'iam-ServiceId-123', 'iam-Profile-123']

        # Invoke method
        response = _service.remove_members_from_access_group(
            access_group_id,
            members=members,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/members/delete')
        mock_response = '{"access_group_id": "access_group_id", "members": [{"iam_id": "iam_id", "trace": "trace", "status_code": 11, "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

        # Set up parameter values
        access_group_id = 'testString'
        members = ['IBMId-user1', 'iam-ServiceId-123', 'iam-Profile-123']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.remove_members_from_access_group(**req_copy)

    def test_remove_members_from_access_group_value_error_with_retries(self):
        # Enable retries and run test_remove_members_from_access_group_value_error.
        _service.enable_retries()
        self.test_remove_members_from_access_group_value_error()

        # Disable retries and run test_remove_members_from_access_group_value_error.
        _service.disable_retries()
        self.test_remove_members_from_access_group_value_error()


class TestRemoveMemberFromAllAccessGroups:
    """
    Test Class for remove_member_from_all_access_groups
    """

    @responses.activate
    def test_remove_member_from_all_access_groups_all_params(self):
        """
        remove_member_from_all_access_groups()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.remove_member_from_all_access_groups(
            account_id,
            iam_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.remove_member_from_all_access_groups(
            account_id,
            iam_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.remove_member_from_all_access_groups(**req_copy)

    def test_remove_member_from_all_access_groups_value_error_with_retries(self):
        # Enable retries and run test_remove_member_from_all_access_groups_value_error.
        _service.enable_retries()
        self.test_remove_member_from_all_access_groups_value_error()

        # Disable retries and run test_remove_member_from_all_access_groups_value_error.
        _service.disable_retries()
        self.test_remove_member_from_all_access_groups_value_error()


class TestAddMemberToMultipleAccessGroups:
    """
    Test Class for add_member_to_multiple_access_groups
    """

    @responses.activate
    def test_add_member_to_multiple_access_groups_all_params(self):
        """
        add_member_to_multiple_access_groups()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups/_allgroups/members/testString')
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=207,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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


class TestNewInstance:
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


class TestAddAccessGroupRule:
    """
    Test Class for add_access_group_rule
    """

    @responses.activate
    def test_add_access_group_rule_all_params(self):
        """
        add_access_group_rule()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/rules')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_access_group_rule(**req_copy)

    def test_add_access_group_rule_value_error_with_retries(self):
        # Enable retries and run test_add_access_group_rule_value_error.
        _service.enable_retries()
        self.test_add_access_group_rule_value_error()

        # Disable retries and run test_add_access_group_rule_value_error.
        _service.disable_retries()
        self.test_add_access_group_rule_value_error()


class TestListAccessGroupRules:
    """
    Test Class for list_access_group_rules
    """

    @responses.activate
    def test_list_access_group_rules_all_params(self):
        """
        list_access_group_rules()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/rules')
        mock_response = '{"rules": [{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.list_access_group_rules(
            access_group_id,
            transaction_id=transaction_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules')
        mock_response = '{"rules": [{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = _service.list_access_group_rules(
            access_group_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules')
        mock_response = '{"rules": [{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_access_group_rules(**req_copy)

    def test_list_access_group_rules_value_error_with_retries(self):
        # Enable retries and run test_list_access_group_rules_value_error.
        _service.enable_retries()
        self.test_list_access_group_rules_value_error()

        # Disable retries and run test_list_access_group_rules_value_error.
        _service.disable_retries()
        self.test_list_access_group_rules_value_error()


class TestGetAccessGroupRule:
    """
    Test Class for get_access_group_rule
    """

    @responses.activate
    def test_get_access_group_rule_all_params(self):
        """
        get_access_group_rule()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_access_group_rule(
            access_group_id,
            rule_id,
            transaction_id=transaction_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.get_access_group_rule(
            access_group_id,
            rule_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_access_group_rule(**req_copy)

    def test_get_access_group_rule_value_error_with_retries(self):
        # Enable retries and run test_get_access_group_rule_value_error.
        _service.enable_retries()
        self.test_get_access_group_rule_value_error()

        # Disable retries and run test_get_access_group_rule_value_error.
        _service.disable_retries()
        self.test_get_access_group_rule_value_error()


class TestReplaceAccessGroupRule:
    """
    Test Class for replace_access_group_rule
    """

    @responses.activate
    def test_replace_access_group_rule_all_params(self):
        """
        replace_access_group_rule()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules/testString')
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "EQUALS", "value": "value"}], "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_access_group_rule(**req_copy)

    def test_replace_access_group_rule_value_error_with_retries(self):
        # Enable retries and run test_replace_access_group_rule_value_error.
        _service.enable_retries()
        self.test_replace_access_group_rule_value_error()

        # Disable retries and run test_replace_access_group_rule_value_error.
        _service.disable_retries()
        self.test_replace_access_group_rule_value_error()


class TestRemoveAccessGroupRule:
    """
    Test Class for remove_access_group_rule
    """

    @responses.activate
    def test_remove_access_group_rule_all_params(self):
        """
        remove_access_group_rule()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/testString/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.remove_access_group_rule(
            access_group_id,
            rule_id,
            transaction_id=transaction_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.remove_access_group_rule(
            access_group_id,
            rule_id,
            headers={},
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
        url = preprocess_url('/v2/groups/testString/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_group_id": access_group_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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
# Start of Service: TemplateOperations
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


class TestCreateTemplate:
    """
    Test Class for create_template
    """

    @responses.activate
    def test_create_template_all_params(self):
        """
        create_template()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a MembersActionControls model
        members_action_controls_model = {}
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = False

        # Construct a dict representation of a MembersInput model
        members_input_model = {}
        members_input_model['users'] = ['IBMid-123', 'IBMid-234']
        members_input_model['service_ids'] = ['testString']
        members_input_model['action_controls'] = members_action_controls_model

        # Construct a dict representation of a ConditionInput model
        condition_input_model = {}
        condition_input_model['claim'] = 'blueGroup'
        condition_input_model['operator'] = 'CONTAINS'
        condition_input_model['value'] = 'test-bluegroup-saml'

        # Construct a dict representation of a RulesActionControls model
        rules_action_controls_model = {}
        rules_action_controls_model['remove'] = False
        rules_action_controls_model['update'] = False

        # Construct a dict representation of a RuleInput model
        rule_input_model = {}
        rule_input_model['name'] = 'Manager group rule'
        rule_input_model['expiration'] = 12
        rule_input_model['realm_name'] = 'https://idp.example.org/SAML2'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        # Construct a dict representation of a AssertionsActionControls model
        assertions_action_controls_model = {}
        assertions_action_controls_model['add'] = False
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        # Construct a dict representation of a AssertionsInput model
        assertions_input_model = {}
        assertions_input_model['rules'] = [rule_input_model]
        assertions_input_model['action_controls'] = assertions_action_controls_model

        # Construct a dict representation of a AccessActionControls model
        access_action_controls_model = {}
        access_action_controls_model['add'] = False

        # Construct a dict representation of a AccessGroupActionControls model
        access_group_action_controls_model = {}
        access_group_action_controls_model['access'] = access_action_controls_model

        # Construct a dict representation of a AccessGroupInput model
        access_group_input_model = {}
        access_group_input_model['name'] = 'IAM Admin Group'
        access_group_input_model[
            'description'
        ] = 'This access group template allows admin access to all IAM platform services in the account.'
        access_group_input_model['members'] = members_input_model
        access_group_input_model['assertions'] = assertions_input_model
        access_group_input_model['action_controls'] = access_group_action_controls_model

        # Construct a dict representation of a PolicyTemplatesInput model
        policy_templates_input_model = {}
        policy_templates_input_model['id'] = 'policyTemplateId-123'
        policy_templates_input_model['version'] = '1'

        # Set up parameter values
        name = 'IAM Admin Group template'
        description = 'This access group template allows admin access to all IAM platform services in the account.'
        account_id = 'accountID-123'
        access_group = access_group_input_model
        policy_template_references = [policy_templates_input_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_template(
            name,
            description,
            account_id,
            access_group=access_group,
            policy_template_references=policy_template_references,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'IAM Admin Group template'
        assert (
            req_body['description']
            == 'This access group template allows admin access to all IAM platform services in the account.'
        )
        assert req_body['account_id'] == 'accountID-123'
        assert req_body['access_group'] == access_group_input_model
        assert req_body['policy_template_references'] == [policy_templates_input_model]

    def test_create_template_all_params_with_retries(self):
        # Enable retries and run test_create_template_all_params.
        _service.enable_retries()
        self.test_create_template_all_params()

        # Disable retries and run test_create_template_all_params.
        _service.disable_retries()
        self.test_create_template_all_params()

    @responses.activate
    def test_create_template_required_params(self):
        """
        test_create_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a MembersActionControls model
        members_action_controls_model = {}
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = False

        # Construct a dict representation of a MembersInput model
        members_input_model = {}
        members_input_model['users'] = ['IBMid-123', 'IBMid-234']
        members_input_model['service_ids'] = ['testString']
        members_input_model['action_controls'] = members_action_controls_model

        # Construct a dict representation of a ConditionInput model
        condition_input_model = {}
        condition_input_model['claim'] = 'blueGroup'
        condition_input_model['operator'] = 'CONTAINS'
        condition_input_model['value'] = 'test-bluegroup-saml'

        # Construct a dict representation of a RulesActionControls model
        rules_action_controls_model = {}
        rules_action_controls_model['remove'] = False
        rules_action_controls_model['update'] = False

        # Construct a dict representation of a RuleInput model
        rule_input_model = {}
        rule_input_model['name'] = 'Manager group rule'
        rule_input_model['expiration'] = 12
        rule_input_model['realm_name'] = 'https://idp.example.org/SAML2'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        # Construct a dict representation of a AssertionsActionControls model
        assertions_action_controls_model = {}
        assertions_action_controls_model['add'] = False
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        # Construct a dict representation of a AssertionsInput model
        assertions_input_model = {}
        assertions_input_model['rules'] = [rule_input_model]
        assertions_input_model['action_controls'] = assertions_action_controls_model

        # Construct a dict representation of a AccessActionControls model
        access_action_controls_model = {}
        access_action_controls_model['add'] = False

        # Construct a dict representation of a AccessGroupActionControls model
        access_group_action_controls_model = {}
        access_group_action_controls_model['access'] = access_action_controls_model

        # Construct a dict representation of a AccessGroupInput model
        access_group_input_model = {}
        access_group_input_model['name'] = 'IAM Admin Group'
        access_group_input_model[
            'description'
        ] = 'This access group template allows admin access to all IAM platform services in the account.'
        access_group_input_model['members'] = members_input_model
        access_group_input_model['assertions'] = assertions_input_model
        access_group_input_model['action_controls'] = access_group_action_controls_model

        # Construct a dict representation of a PolicyTemplatesInput model
        policy_templates_input_model = {}
        policy_templates_input_model['id'] = 'policyTemplateId-123'
        policy_templates_input_model['version'] = '1'

        # Set up parameter values
        name = 'IAM Admin Group template'
        description = 'This access group template allows admin access to all IAM platform services in the account.'
        account_id = 'accountID-123'
        access_group = access_group_input_model
        policy_template_references = [policy_templates_input_model]

        # Invoke method
        response = _service.create_template(
            name,
            description,
            account_id,
            access_group=access_group,
            policy_template_references=policy_template_references,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'IAM Admin Group template'
        assert (
            req_body['description']
            == 'This access group template allows admin access to all IAM platform services in the account.'
        )
        assert req_body['account_id'] == 'accountID-123'
        assert req_body['access_group'] == access_group_input_model
        assert req_body['policy_template_references'] == [policy_templates_input_model]

    def test_create_template_required_params_with_retries(self):
        # Enable retries and run test_create_template_required_params.
        _service.enable_retries()
        self.test_create_template_required_params()

        # Disable retries and run test_create_template_required_params.
        _service.disable_retries()
        self.test_create_template_required_params()

    @responses.activate
    def test_create_template_value_error(self):
        """
        test_create_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a MembersActionControls model
        members_action_controls_model = {}
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = False

        # Construct a dict representation of a MembersInput model
        members_input_model = {}
        members_input_model['users'] = ['IBMid-123', 'IBMid-234']
        members_input_model['service_ids'] = ['testString']
        members_input_model['action_controls'] = members_action_controls_model

        # Construct a dict representation of a ConditionInput model
        condition_input_model = {}
        condition_input_model['claim'] = 'blueGroup'
        condition_input_model['operator'] = 'CONTAINS'
        condition_input_model['value'] = 'test-bluegroup-saml'

        # Construct a dict representation of a RulesActionControls model
        rules_action_controls_model = {}
        rules_action_controls_model['remove'] = False
        rules_action_controls_model['update'] = False

        # Construct a dict representation of a RuleInput model
        rule_input_model = {}
        rule_input_model['name'] = 'Manager group rule'
        rule_input_model['expiration'] = 12
        rule_input_model['realm_name'] = 'https://idp.example.org/SAML2'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        # Construct a dict representation of a AssertionsActionControls model
        assertions_action_controls_model = {}
        assertions_action_controls_model['add'] = False
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        # Construct a dict representation of a AssertionsInput model
        assertions_input_model = {}
        assertions_input_model['rules'] = [rule_input_model]
        assertions_input_model['action_controls'] = assertions_action_controls_model

        # Construct a dict representation of a AccessActionControls model
        access_action_controls_model = {}
        access_action_controls_model['add'] = False

        # Construct a dict representation of a AccessGroupActionControls model
        access_group_action_controls_model = {}
        access_group_action_controls_model['access'] = access_action_controls_model

        # Construct a dict representation of a AccessGroupInput model
        access_group_input_model = {}
        access_group_input_model['name'] = 'IAM Admin Group'
        access_group_input_model[
            'description'
        ] = 'This access group template allows admin access to all IAM platform services in the account.'
        access_group_input_model['members'] = members_input_model
        access_group_input_model['assertions'] = assertions_input_model
        access_group_input_model['action_controls'] = access_group_action_controls_model

        # Construct a dict representation of a PolicyTemplatesInput model
        policy_templates_input_model = {}
        policy_templates_input_model['id'] = 'policyTemplateId-123'
        policy_templates_input_model['version'] = '1'

        # Set up parameter values
        name = 'IAM Admin Group template'
        description = 'This access group template allows admin access to all IAM platform services in the account.'
        account_id = 'accountID-123'
        access_group = access_group_input_model
        policy_template_references = [policy_templates_input_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "description": description,
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_template(**req_copy)

    def test_create_template_value_error_with_retries(self):
        # Enable retries and run test_create_template_value_error.
        _service.enable_retries()
        self.test_create_template_value_error()

        # Disable retries and run test_create_template_value_error.
        _service.disable_retries()
        self.test_create_template_value_error()


class TestListTemplate:
    """
    Test Class for list_template
    """

    @responses.activate
    def test_list_template_all_params(self):
        """
        list_template()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups_templates": [{"id": "id", "name": "name", "description": "description", "version": "version", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'accountID-123'
        transaction_id = 'testString'
        limit = 50
        offset = 0
        verbose = True

        # Invoke method
        response = _service.list_template(
            account_id,
            transaction_id=transaction_id,
            limit=limit,
            offset=offset,
            verbose=verbose,
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
        assert 'offset={}'.format(offset) in query_string
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string

    def test_list_template_all_params_with_retries(self):
        # Enable retries and run test_list_template_all_params.
        _service.enable_retries()
        self.test_list_template_all_params()

        # Disable retries and run test_list_template_all_params.
        _service.disable_retries()
        self.test_list_template_all_params()

    @responses.activate
    def test_list_template_required_params(self):
        """
        test_list_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups_templates": [{"id": "id", "name": "name", "description": "description", "version": "version", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'accountID-123'

        # Invoke method
        response = _service.list_template(
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

    def test_list_template_required_params_with_retries(self):
        # Enable retries and run test_list_template_required_params.
        _service.enable_retries()
        self.test_list_template_required_params()

        # Disable retries and run test_list_template_required_params.
        _service.disable_retries()
        self.test_list_template_required_params()

    @responses.activate
    def test_list_template_value_error(self):
        """
        test_list_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups_templates": [{"id": "id", "name": "name", "description": "description", "version": "version", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'accountID-123'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_template(**req_copy)

    def test_list_template_value_error_with_retries(self):
        # Enable retries and run test_list_template_value_error.
        _service.enable_retries()
        self.test_list_template_value_error()

        # Disable retries and run test_list_template_value_error.
        _service.disable_retries()
        self.test_list_template_value_error()

    @responses.activate
    def test_list_template_with_pager_get_next(self):
        """
        test_list_template_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/groups_templates')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"groups_templates":[{"id":"id","name":"name","description":"description","version":"version","created_at":"created_at","created_by_id":"created_by_id","last_modified_at":"last_modified_at","last_modified_by_id":"last_modified_by_id","href":"href"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"groups_templates":[{"id":"id","name":"name","description":"description","version":"version","created_at":"created_at","created_by_id":"created_by_id","last_modified_at":"last_modified_at","last_modified_by_id":"last_modified_by_id","href":"href"}]}'
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
        pager = TemplatePager(
            client=_service,
            account_id='accountID-123',
            transaction_id='testString',
            limit=50,
            verbose=True,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_template_with_pager_get_all(self):
        """
        test_list_template_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/groups_templates')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"groups_templates":[{"id":"id","name":"name","description":"description","version":"version","created_at":"created_at","created_by_id":"created_by_id","last_modified_at":"last_modified_at","last_modified_by_id":"last_modified_by_id","href":"href"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"groups_templates":[{"id":"id","name":"name","description":"description","version":"version","created_at":"created_at","created_by_id":"created_by_id","last_modified_at":"last_modified_at","last_modified_by_id":"last_modified_by_id","href":"href"}]}'
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
        pager = TemplatePager(
            client=_service,
            account_id='accountID-123',
            transaction_id='testString',
            limit=50,
            verbose=True,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateTemplateVersion:
    """
    Test Class for create_template_version
    """

    @responses.activate
    def test_create_template_version_all_params(self):
        """
        create_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a MembersActionControls model
        members_action_controls_model = {}
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = True

        # Construct a dict representation of a MembersInput model
        members_input_model = {}
        members_input_model['users'] = ['IBMid-123', 'IBMid-234']
        members_input_model['service_ids'] = ['testString']
        members_input_model['action_controls'] = members_action_controls_model

        # Construct a dict representation of a ConditionInput model
        condition_input_model = {}
        condition_input_model['claim'] = 'blueGroup'
        condition_input_model['operator'] = 'CONTAINS'
        condition_input_model['value'] = 'test-bluegroup-saml'

        # Construct a dict representation of a RulesActionControls model
        rules_action_controls_model = {}
        rules_action_controls_model['remove'] = True
        rules_action_controls_model['update'] = True

        # Construct a dict representation of a RuleInput model
        rule_input_model = {}
        rule_input_model['name'] = 'Manager group rule'
        rule_input_model['expiration'] = 12
        rule_input_model['realm_name'] = 'https://idp.example.org/SAML2'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        # Construct a dict representation of a AssertionsActionControls model
        assertions_action_controls_model = {}
        assertions_action_controls_model['add'] = True
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        # Construct a dict representation of a AssertionsInput model
        assertions_input_model = {}
        assertions_input_model['rules'] = [rule_input_model]
        assertions_input_model['action_controls'] = assertions_action_controls_model

        # Construct a dict representation of a AccessActionControls model
        access_action_controls_model = {}
        access_action_controls_model['add'] = True

        # Construct a dict representation of a AccessGroupActionControls model
        access_group_action_controls_model = {}
        access_group_action_controls_model['access'] = access_action_controls_model

        # Construct a dict representation of a AccessGroupInput model
        access_group_input_model = {}
        access_group_input_model['name'] = 'IAM Admin Group 8'
        access_group_input_model[
            'description'
        ] = 'This access group template allows admin access to all IAM platform services in the account.'
        access_group_input_model['members'] = members_input_model
        access_group_input_model['assertions'] = assertions_input_model
        access_group_input_model['action_controls'] = access_group_action_controls_model

        # Construct a dict representation of a PolicyTemplatesInput model
        policy_templates_input_model = {}
        policy_templates_input_model['id'] = 'policyTemplateId-123'
        policy_templates_input_model['version'] = '1'

        # Set up parameter values
        template_id = 'testString'
        name = 'IAM Admin Group template 2'
        description = 'This access group template allows admin access to all IAM platform services in the account.'
        access_group = access_group_input_model
        policy_template_references = [policy_templates_input_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_template_version(
            template_id,
            name=name,
            description=description,
            access_group=access_group,
            policy_template_references=policy_template_references,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'IAM Admin Group template 2'
        assert (
            req_body['description']
            == 'This access group template allows admin access to all IAM platform services in the account.'
        )
        assert req_body['access_group'] == access_group_input_model
        assert req_body['policy_template_references'] == [policy_templates_input_model]

    def test_create_template_version_all_params_with_retries(self):
        # Enable retries and run test_create_template_version_all_params.
        _service.enable_retries()
        self.test_create_template_version_all_params()

        # Disable retries and run test_create_template_version_all_params.
        _service.disable_retries()
        self.test_create_template_version_all_params()

    @responses.activate
    def test_create_template_version_required_params(self):
        """
        test_create_template_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        template_id = 'testString'

        # Invoke method
        response = _service.create_template_version(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_template_version_required_params_with_retries(self):
        # Enable retries and run test_create_template_version_required_params.
        _service.enable_retries()
        self.test_create_template_version_required_params()

        # Disable retries and run test_create_template_version_required_params.
        _service.disable_retries()
        self.test_create_template_version_required_params()

    @responses.activate
    def test_create_template_version_value_error(self):
        """
        test_create_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_template_version(**req_copy)

    def test_create_template_version_value_error_with_retries(self):
        # Enable retries and run test_create_template_version_value_error.
        _service.enable_retries()
        self.test_create_template_version_value_error()

        # Disable retries and run test_create_template_version_value_error.
        _service.disable_retries()
        self.test_create_template_version_value_error()


class TestListTemplateVersions:
    """
    Test Class for list_template_versions
    """

    @responses.activate
    def test_list_template_versions_all_params(self):
        """
        list_template_versions()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        limit = 100
        offset = 0

        # Invoke method
        response = _service.list_template_versions(
            template_id,
            limit=limit,
            offset=offset,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string

    def test_list_template_versions_all_params_with_retries(self):
        # Enable retries and run test_list_template_versions_all_params.
        _service.enable_retries()
        self.test_list_template_versions_all_params()

        # Disable retries and run test_list_template_versions_all_params.
        _service.disable_retries()
        self.test_list_template_versions_all_params()

    @responses.activate
    def test_list_template_versions_required_params(self):
        """
        test_list_template_versions_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'

        # Invoke method
        response = _service.list_template_versions(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_template_versions_required_params_with_retries(self):
        # Enable retries and run test_list_template_versions_required_params.
        _service.enable_retries()
        self.test_list_template_versions_required_params()

        # Disable retries and run test_list_template_versions_required_params.
        _service.disable_retries()
        self.test_list_template_versions_required_params()

    @responses.activate
    def test_list_template_versions_value_error(self):
        """
        test_list_template_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions')
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "versions": [{"name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_template_versions(**req_copy)

    def test_list_template_versions_value_error_with_retries(self):
        # Enable retries and run test_list_template_versions_value_error.
        _service.enable_retries()
        self.test_list_template_versions_value_error()

        # Disable retries and run test_list_template_versions_value_error.
        _service.disable_retries()
        self.test_list_template_versions_value_error()

    @responses.activate
    def test_list_template_versions_with_pager_get_next(self):
        """
        test_list_template_versions_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/groups_templates/testString/versions')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"versions":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"access_group":{"name":"name","description":"description","members":{"users":["users"],"service_ids":["service_ids"],"action_controls":{"add":false,"remove":true}},"assertions":{"rules":[{"name":"name","expiration":10,"realm_name":"realm_name","conditions":[{"claim":"claim","operator":"operator","value":"value"}],"action_controls":{"remove":true,"update":true}}],"action_controls":{"add":false,"remove":true,"update":true}},"action_controls":{"access":{"add":false}}},"policy_template_references":[{"id":"id","version":"version"}],"href":"href","created_at":"created_at","created_by_id":"created_by_id","last_modified_at":"last_modified_at","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        mock_response2 = '{"versions":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"access_group":{"name":"name","description":"description","members":{"users":["users"],"service_ids":["service_ids"],"action_controls":{"add":false,"remove":true}},"assertions":{"rules":[{"name":"name","expiration":10,"realm_name":"realm_name","conditions":[{"claim":"claim","operator":"operator","value":"value"}],"action_controls":{"remove":true,"update":true}}],"action_controls":{"add":false,"remove":true,"update":true}},"action_controls":{"access":{"add":false}}},"policy_template_references":[{"id":"id","version":"version"}],"href":"href","created_at":"created_at","created_by_id":"created_by_id","last_modified_at":"last_modified_at","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
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
        pager = TemplateVersionsPager(
            client=_service,
            template_id='testString',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_template_versions_with_pager_get_all(self):
        """
        test_list_template_versions_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/groups_templates/testString/versions')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"versions":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"access_group":{"name":"name","description":"description","members":{"users":["users"],"service_ids":["service_ids"],"action_controls":{"add":false,"remove":true}},"assertions":{"rules":[{"name":"name","expiration":10,"realm_name":"realm_name","conditions":[{"claim":"claim","operator":"operator","value":"value"}],"action_controls":{"remove":true,"update":true}}],"action_controls":{"add":false,"remove":true,"update":true}},"action_controls":{"access":{"add":false}}},"policy_template_references":[{"id":"id","version":"version"}],"href":"href","created_at":"created_at","created_by_id":"created_by_id","last_modified_at":"last_modified_at","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
        mock_response2 = '{"versions":[{"name":"name","description":"description","account_id":"account_id","version":"version","committed":false,"access_group":{"name":"name","description":"description","members":{"users":["users"],"service_ids":["service_ids"],"action_controls":{"add":false,"remove":true}},"assertions":{"rules":[{"name":"name","expiration":10,"realm_name":"realm_name","conditions":[{"claim":"claim","operator":"operator","value":"value"}],"action_controls":{"remove":true,"update":true}}],"action_controls":{"add":false,"remove":true,"update":true}},"action_controls":{"access":{"add":false}}},"policy_template_references":[{"id":"id","version":"version"}],"href":"href","created_at":"created_at","created_by_id":"created_by_id","last_modified_at":"last_modified_at","last_modified_by_id":"last_modified_by_id"}],"total_count":2,"limit":1}'
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
        pager = TemplateVersionsPager(
            client=_service,
            template_id='testString',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetTemplateSpecificVersion:
    """
    Test Class for get_template_specific_version
    """

    @responses.activate
    def test_get_template_specific_version_all_params(self):
        """
        get_template_specific_version()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_template_specific_version(
            template_id,
            version_num,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_template_specific_version_all_params_with_retries(self):
        # Enable retries and run test_get_template_specific_version_all_params.
        _service.enable_retries()
        self.test_get_template_specific_version_all_params()

        # Disable retries and run test_get_template_specific_version_all_params.
        _service.disable_retries()
        self.test_get_template_specific_version_all_params()

    @responses.activate
    def test_get_template_specific_version_required_params(self):
        """
        test_get_template_specific_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'

        # Invoke method
        response = _service.get_template_specific_version(
            template_id,
            version_num,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_template_specific_version_required_params_with_retries(self):
        # Enable retries and run test_get_template_specific_version_required_params.
        _service.enable_retries()
        self.test_get_template_specific_version_required_params()

        # Disable retries and run test_get_template_specific_version_required_params.
        _service.disable_retries()
        self.test_get_template_specific_version_required_params()

    @responses.activate
    def test_get_template_specific_version_value_error(self):
        """
        test_get_template_specific_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version_num": version_num,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_template_specific_version(**req_copy)

    def test_get_template_specific_version_value_error_with_retries(self):
        # Enable retries and run test_get_template_specific_version_value_error.
        _service.enable_retries()
        self.test_get_template_specific_version_value_error()

        # Disable retries and run test_get_template_specific_version_value_error.
        _service.disable_retries()
        self.test_get_template_specific_version_value_error()


class TestReplaceTemplateVersion:
    """
    Test Class for replace_template_version
    """

    @responses.activate
    def test_replace_template_version_all_params(self):
        """
        replace_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a MembersActionControls model
        members_action_controls_model = {}
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = True

        # Construct a dict representation of a MembersInput model
        members_input_model = {}
        members_input_model['users'] = ['IBMid-5500085Q21']
        members_input_model['service_ids'] = ['testString']
        members_input_model['action_controls'] = members_action_controls_model

        # Construct a dict representation of a ConditionInput model
        condition_input_model = {}
        condition_input_model['claim'] = 'blueGroup'
        condition_input_model['operator'] = 'CONTAINS'
        condition_input_model['value'] = 'test-bluegroup-saml'

        # Construct a dict representation of a RulesActionControls model
        rules_action_controls_model = {}
        rules_action_controls_model['remove'] = True
        rules_action_controls_model['update'] = True

        # Construct a dict representation of a RuleInput model
        rule_input_model = {}
        rule_input_model['name'] = 'Manager group rule'
        rule_input_model['expiration'] = 12
        rule_input_model['realm_name'] = 'https://idp.example.org/SAML2'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        # Construct a dict representation of a AssertionsActionControls model
        assertions_action_controls_model = {}
        assertions_action_controls_model['add'] = True
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        # Construct a dict representation of a AssertionsInput model
        assertions_input_model = {}
        assertions_input_model['rules'] = [rule_input_model]
        assertions_input_model['action_controls'] = assertions_action_controls_model

        # Construct a dict representation of a AccessActionControls model
        access_action_controls_model = {}
        access_action_controls_model['add'] = True

        # Construct a dict representation of a AccessGroupActionControls model
        access_group_action_controls_model = {}
        access_group_action_controls_model['access'] = access_action_controls_model

        # Construct a dict representation of a AccessGroupInput model
        access_group_input_model = {}
        access_group_input_model['name'] = 'IAM Admin Group 8'
        access_group_input_model[
            'description'
        ] = 'This access group template allows admin access to all IAM platform services in the account.'
        access_group_input_model['members'] = members_input_model
        access_group_input_model['assertions'] = assertions_input_model
        access_group_input_model['action_controls'] = access_group_action_controls_model

        # Construct a dict representation of a PolicyTemplatesInput model
        policy_templates_input_model = {}
        policy_templates_input_model['id'] = 'policyTemplateId-123'
        policy_templates_input_model['version'] = '1'

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'
        if_match = 'testString'
        id = 'testString'
        name = 'IAM Admin Group template 2'
        description = 'This access group template allows admin access to all IAM platform services in the account.'
        account_id = 'testString'
        version = 'testString'
        committed = True
        access_group = access_group_input_model
        policy_template_references = [policy_templates_input_model]
        href = 'testString'
        created_at = string_to_datetime('2019-01-01T12:00:00.000Z')
        created_by_id = 'testString'
        last_modified_at = string_to_datetime('2019-01-01T12:00:00.000Z')
        last_modified_by_id = 'testString'
        transaction_id = '83adf5bd-de790caa3'

        # Invoke method
        response = _service.replace_template_version(
            template_id,
            version_num,
            if_match,
            id=id,
            name=name,
            description=description,
            account_id=account_id,
            version=version,
            committed=committed,
            access_group=access_group,
            policy_template_references=policy_template_references,
            href=href,
            created_at=created_at,
            created_by_id=created_by_id,
            last_modified_at=last_modified_at,
            last_modified_by_id=last_modified_by_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'IAM Admin Group template 2'
        assert (
            req_body['description']
            == 'This access group template allows admin access to all IAM platform services in the account.'
        )
        assert req_body['account_id'] == 'testString'
        assert req_body['version'] == 'testString'
        assert req_body['committed'] == True
        assert req_body['access_group'] == access_group_input_model
        assert req_body['policy_template_references'] == [policy_templates_input_model]
        assert req_body['href'] == 'testString'
        assert req_body['created_at'] == '2019-01-01T12:00:00Z'
        assert req_body['created_by_id'] == 'testString'
        assert req_body['last_modified_at'] == '2019-01-01T12:00:00Z'
        assert req_body['last_modified_by_id'] == 'testString'

    def test_replace_template_version_all_params_with_retries(self):
        # Enable retries and run test_replace_template_version_all_params.
        _service.enable_retries()
        self.test_replace_template_version_all_params()

        # Disable retries and run test_replace_template_version_all_params.
        _service.disable_retries()
        self.test_replace_template_version_all_params()

    @responses.activate
    def test_replace_template_version_required_params(self):
        """
        test_replace_template_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'
        if_match = 'testString'

        # Invoke method
        response = _service.replace_template_version(
            template_id,
            version_num,
            if_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_replace_template_version_required_params_with_retries(self):
        # Enable retries and run test_replace_template_version_required_params.
        _service.enable_retries()
        self.test_replace_template_version_required_params()

        # Disable retries and run test_replace_template_version_required_params.
        _service.disable_retries()
        self.test_replace_template_version_required_params()

    @responses.activate
    def test_replace_template_version_value_error(self):
        """
        test_replace_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'
        if_match = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version_num": version_num,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_template_version(**req_copy)

    def test_replace_template_version_value_error_with_retries(self):
        # Enable retries and run test_replace_template_version_value_error.
        _service.enable_retries()
        self.test_replace_template_version_value_error()

        # Disable retries and run test_replace_template_version_value_error.
        _service.disable_retries()
        self.test_replace_template_version_value_error()


class TestDeleteTemplateVersion:
    """
    Test Class for delete_template_version
    """

    @responses.activate
    def test_delete_template_version_all_params(self):
        """
        delete_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_template_version(
            template_id,
            version_num,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_template_version_all_params_with_retries(self):
        # Enable retries and run test_delete_template_version_all_params.
        _service.enable_retries()
        self.test_delete_template_version_all_params()

        # Disable retries and run test_delete_template_version_all_params.
        _service.disable_retries()
        self.test_delete_template_version_all_params()

    @responses.activate
    def test_delete_template_version_required_params(self):
        """
        test_delete_template_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'

        # Invoke method
        response = _service.delete_template_version(
            template_id,
            version_num,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_template_version_required_params_with_retries(self):
        # Enable retries and run test_delete_template_version_required_params.
        _service.enable_retries()
        self.test_delete_template_version_required_params()

        # Disable retries and run test_delete_template_version_required_params.
        _service.disable_retries()
        self.test_delete_template_version_required_params()

    @responses.activate
    def test_delete_template_version_value_error(self):
        """
        test_delete_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version_num": version_num,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_template_version(**req_copy)

    def test_delete_template_version_value_error_with_retries(self):
        # Enable retries and run test_delete_template_version_value_error.
        _service.enable_retries()
        self.test_delete_template_version_value_error()

        # Disable retries and run test_delete_template_version_value_error.
        _service.disable_retries()
        self.test_delete_template_version_value_error()


class TestCommitTemplate:
    """
    Test Class for commit_template
    """

    @responses.activate
    def test_commit_template_all_params(self):
        """
        commit_template()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString/commit')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'
        if_match = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.commit_template(
            template_id,
            version_num,
            if_match,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_commit_template_all_params_with_retries(self):
        # Enable retries and run test_commit_template_all_params.
        _service.enable_retries()
        self.test_commit_template_all_params()

        # Disable retries and run test_commit_template_all_params.
        _service.disable_retries()
        self.test_commit_template_all_params()

    @responses.activate
    def test_commit_template_required_params(self):
        """
        test_commit_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString/commit')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'
        if_match = 'testString'

        # Invoke method
        response = _service.commit_template(
            template_id,
            version_num,
            if_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_commit_template_required_params_with_retries(self):
        # Enable retries and run test_commit_template_required_params.
        _service.enable_retries()
        self.test_commit_template_required_params()

        # Disable retries and run test_commit_template_required_params.
        _service.disable_retries()
        self.test_commit_template_required_params()

    @responses.activate
    def test_commit_template_value_error(self):
        """
        test_commit_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString/versions/testString/commit')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version_num = 'testString'
        if_match = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version_num": version_num,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.commit_template(**req_copy)

    def test_commit_template_value_error_with_retries(self):
        # Enable retries and run test_commit_template_value_error.
        _service.enable_retries()
        self.test_commit_template_value_error()

        # Disable retries and run test_commit_template_value_error.
        _service.disable_retries()
        self.test_commit_template_value_error()


class TestGetTemplateLatestVersion:
    """
    Test Class for get_template_latest_version
    """

    @responses.activate
    def test_get_template_latest_version_all_params(self):
        """
        get_template_latest_version()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_template_latest_version(
            template_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_template_latest_version_all_params_with_retries(self):
        # Enable retries and run test_get_template_latest_version_all_params.
        _service.enable_retries()
        self.test_get_template_latest_version_all_params()

        # Disable retries and run test_get_template_latest_version_all_params.
        _service.disable_retries()
        self.test_get_template_latest_version_all_params()

    @responses.activate
    def test_get_template_latest_version_required_params(self):
        """
        test_get_template_latest_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'

        # Invoke method
        response = _service.get_template_latest_version(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_template_latest_version_required_params_with_retries(self):
        # Enable retries and run test_get_template_latest_version_required_params.
        _service.enable_retries()
        self.test_get_template_latest_version_required_params()

        # Disable retries and run test_get_template_latest_version_required_params.
        _service.disable_retries()
        self.test_get_template_latest_version_required_params()

    @responses.activate
    def test_get_template_latest_version_value_error(self):
        """
        test_get_template_latest_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "version": "version", "committed": false, "access_group": {"name": "name", "description": "description", "members": {"users": ["users"], "service_ids": ["service_ids"], "action_controls": {"add": false, "remove": true}}, "assertions": {"rules": [{"name": "name", "expiration": 10, "realm_name": "realm_name", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "action_controls": {"remove": true, "update": true}}], "action_controls": {"add": false, "remove": true, "update": true}}, "action_controls": {"access": {"add": false}}}, "policy_template_references": [{"id": "id", "version": "version"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_template_latest_version(**req_copy)

    def test_get_template_latest_version_value_error_with_retries(self):
        # Enable retries and run test_get_template_latest_version_value_error.
        _service.enable_retries()
        self.test_get_template_latest_version_value_error()

        # Disable retries and run test_get_template_latest_version_value_error.
        _service.disable_retries()
        self.test_get_template_latest_version_value_error()


class TestDeleteTemplate:
    """
    Test Class for delete_template
    """

    @responses.activate
    def test_delete_template_all_params(self):
        """
        delete_template()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_template(
            template_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_template_all_params_with_retries(self):
        # Enable retries and run test_delete_template_all_params.
        _service.enable_retries()
        self.test_delete_template_all_params()

        # Disable retries and run test_delete_template_all_params.
        _service.disable_retries()
        self.test_delete_template_all_params()

    @responses.activate
    def test_delete_template_required_params(self):
        """
        test_delete_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'

        # Invoke method
        response = _service.delete_template(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_template_required_params_with_retries(self):
        # Enable retries and run test_delete_template_required_params.
        _service.enable_retries()
        self.test_delete_template_required_params()

        # Disable retries and run test_delete_template_required_params.
        _service.disable_retries()
        self.test_delete_template_required_params()

    @responses.activate
    def test_delete_template_value_error(self):
        """
        test_delete_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_template(**req_copy)

    def test_delete_template_value_error_with_retries(self):
        # Enable retries and run test_delete_template_value_error.
        _service.enable_retries()
        self.test_delete_template_value_error()

        # Disable retries and run test_delete_template_value_error.
        _service.disable_retries()
        self.test_delete_template_value_error()


class TestCreateAssignTemplate:
    """
    Test Class for create_assign_template
    """

    @responses.activate
    def test_create_assign_template_all_params(self):
        """
        create_assign_template()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment')
        mock_response = '{"id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": "template_version", "target_type": "target_type", "target": "target", "operation": "operation", "status": "status", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        template_id = 'AccessGroupTemplateId-4be4'
        template_version = '1'
        target_type = 'accountGroup'
        target = '0a45594d0f-123'
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_assign_template(
            template_id,
            template_version,
            target_type,
            target,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['template_id'] == 'AccessGroupTemplateId-4be4'
        assert req_body['template_version'] == '1'
        assert req_body['target_type'] == 'accountGroup'
        assert req_body['target'] == '0a45594d0f-123'

    def test_create_assign_template_all_params_with_retries(self):
        # Enable retries and run test_create_assign_template_all_params.
        _service.enable_retries()
        self.test_create_assign_template_all_params()

        # Disable retries and run test_create_assign_template_all_params.
        _service.disable_retries()
        self.test_create_assign_template_all_params()

    @responses.activate
    def test_create_assign_template_required_params(self):
        """
        test_create_assign_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment')
        mock_response = '{"id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": "template_version", "target_type": "target_type", "target": "target", "operation": "operation", "status": "status", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        template_id = 'AccessGroupTemplateId-4be4'
        template_version = '1'
        target_type = 'accountGroup'
        target = '0a45594d0f-123'

        # Invoke method
        response = _service.create_assign_template(
            template_id,
            template_version,
            target_type,
            target,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['template_id'] == 'AccessGroupTemplateId-4be4'
        assert req_body['template_version'] == '1'
        assert req_body['target_type'] == 'accountGroup'
        assert req_body['target'] == '0a45594d0f-123'

    def test_create_assign_template_required_params_with_retries(self):
        # Enable retries and run test_create_assign_template_required_params.
        _service.enable_retries()
        self.test_create_assign_template_required_params()

        # Disable retries and run test_create_assign_template_required_params.
        _service.disable_retries()
        self.test_create_assign_template_required_params()

    @responses.activate
    def test_create_assign_template_value_error(self):
        """
        test_create_assign_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment')
        mock_response = '{"id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": "template_version", "target_type": "target_type", "target": "target", "operation": "operation", "status": "status", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        template_id = 'AccessGroupTemplateId-4be4'
        template_version = '1'
        target_type = 'accountGroup'
        target = '0a45594d0f-123'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "template_version": template_version,
            "target_type": target_type,
            "target": target,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_assign_template(**req_copy)

    def test_create_assign_template_value_error_with_retries(self):
        # Enable retries and run test_create_assign_template_value_error.
        _service.enable_retries()
        self.test_create_assign_template_value_error()

        # Disable retries and run test_create_assign_template_value_error.
        _service.disable_retries()
        self.test_create_assign_template_value_error()


class TestListAssignment:
    """
    Test Class for list_assignment
    """

    @responses.activate
    def test_list_assignment_all_params(self):
        """
        list_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment')
        mock_response = '{"total": 5, "limit": 5, "offset": 6, "groups_assignment": [{"id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": "template_version", "target_type": "target_type", "target": "target", "operation": "operation", "status": "status", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'accountID-123'

        # Invoke method
        response = _service.list_assignment(
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_list_assignment_all_params_with_retries(self):
        # Enable retries and run test_list_assignment_all_params.
        _service.enable_retries()
        self.test_list_assignment_all_params()

        # Disable retries and run test_list_assignment_all_params.
        _service.disable_retries()
        self.test_list_assignment_all_params()

    @responses.activate
    def test_list_assignment_required_params(self):
        """
        test_list_assignment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment')
        mock_response = '{"total": 5, "limit": 5, "offset": 6, "groups_assignment": [{"id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": "template_version", "target_type": "target_type", "target": "target", "operation": "operation", "status": "status", "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_assignment()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_assignment_required_params_with_retries(self):
        # Enable retries and run test_list_assignment_required_params.
        _service.enable_retries()
        self.test_list_assignment_required_params()

        # Disable retries and run test_list_assignment_required_params.
        _service.disable_retries()
        self.test_list_assignment_required_params()


class TestGetAssignment:
    """
    Test Class for get_assignment
    """

    @responses.activate
    def test_get_assignment_all_params(self):
        """
        get_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": "template_version", "target_type": "target_type", "target": "target", "operation": "operation", "status": "status", "resources": [{"target": "target", "access_group": {"group": {"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}, "members": [{"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}], "rules": [{"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}]}, "policy_template_references": [{"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assignment_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_assignment(
            assignment_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_get_assignment_all_params_with_retries(self):
        # Enable retries and run test_get_assignment_all_params.
        _service.enable_retries()
        self.test_get_assignment_all_params()

        # Disable retries and run test_get_assignment_all_params.
        _service.disable_retries()
        self.test_get_assignment_all_params()

    @responses.activate
    def test_get_assignment_required_params(self):
        """
        test_get_assignment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": "template_version", "target_type": "target_type", "target": "target", "operation": "operation", "status": "status", "resources": [{"target": "target", "access_group": {"group": {"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}, "members": [{"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}], "rules": [{"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}]}, "policy_template_references": [{"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assignment_id = 'testString'

        # Invoke method
        response = _service.get_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_get_assignment_required_params_with_retries(self):
        # Enable retries and run test_get_assignment_required_params.
        _service.enable_retries()
        self.test_get_assignment_required_params()

        # Disable retries and run test_get_assignment_required_params.
        _service.disable_retries()
        self.test_get_assignment_required_params()

    @responses.activate
    def test_get_assignment_value_error(self):
        """
        test_get_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": "template_version", "target_type": "target_type", "target": "target", "operation": "operation", "status": "status", "resources": [{"target": "target", "access_group": {"group": {"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}, "members": [{"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}], "rules": [{"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}]}, "policy_template_references": [{"id": "id", "name": "name", "version": "version", "resource": "resource", "error": "error", "operation": "operation", "status": "status"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
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
                _service.get_assignment(**req_copy)

    def test_get_assignment_value_error_with_retries(self):
        # Enable retries and run test_get_assignment_value_error.
        _service.enable_retries()
        self.test_get_assignment_value_error()

        # Disable retries and run test_get_assignment_value_error.
        _service.disable_retries()
        self.test_get_assignment_value_error()


class TestDeleteAssignment:
    """
    Test Class for delete_assignment
    """

    @responses.activate
    def test_delete_assignment_all_params(self):
        """
        delete_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        assignment_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_assignment(
            assignment_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_assignment_all_params_with_retries(self):
        # Enable retries and run test_delete_assignment_all_params.
        _service.enable_retries()
        self.test_delete_assignment_all_params()

        # Disable retries and run test_delete_assignment_all_params.
        _service.disable_retries()
        self.test_delete_assignment_all_params()

    @responses.activate
    def test_delete_assignment_required_params(self):
        """
        test_delete_assignment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        assignment_id = 'testString'

        # Invoke method
        response = _service.delete_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_assignment_required_params_with_retries(self):
        # Enable retries and run test_delete_assignment_required_params.
        _service.enable_retries()
        self.test_delete_assignment_required_params()

        # Disable retries and run test_delete_assignment_required_params.
        _service.disable_retries()
        self.test_delete_assignment_required_params()

    @responses.activate
    def test_delete_assignment_value_error(self):
        """
        test_delete_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/groups_assignment/testString')
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
                _service.delete_assignment(**req_copy)

    def test_delete_assignment_value_error_with_retries(self):
        # Enable retries and run test_delete_assignment_value_error.
        _service.enable_retries()
        self.test_delete_assignment_value_error()

        # Disable retries and run test_delete_assignment_value_error.
        _service.disable_retries()
        self.test_delete_assignment_value_error()


# endregion
##############################################################################
# End of Service: TemplateOperations
##############################################################################

##############################################################################
# Start of Service: AccountSettings
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


class TestGetAccountSettings:
    """
    Test Class for get_account_settings
    """

    @responses.activate
    def test_get_account_settings_all_params(self):
        """
        get_account_settings()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_account_settings(
            account_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
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
        response = _service.get_account_settings(
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
        url = preprocess_url('/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
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
                _service.get_account_settings(**req_copy)

    def test_get_account_settings_value_error_with_retries(self):
        # Enable retries and run test_get_account_settings_value_error.
        _service.enable_retries()
        self.test_get_account_settings_value_error()

        # Disable retries and run test_get_account_settings_value_error.
        _service.disable_retries()
        self.test_get_account_settings_value_error()


class TestUpdateAccountSettings:
    """
    Test Class for update_account_settings
    """

    @responses.activate
    def test_update_account_settings_all_params(self):
        """
        update_account_settings()
        """
        # Set up mock
        url = preprocess_url('/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        public_access_enabled = True
        transaction_id = 'testString'

        # Invoke method
        response = _service.update_account_settings(
            account_id,
            public_access_enabled=public_access_enabled,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        public_access_enabled = True

        # Invoke method
        response = _service.update_account_settings(
            account_id,
            public_access_enabled=public_access_enabled,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        url = preprocess_url('/v2/groups/settings')
        mock_response = '{"account_id": "account_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        public_access_enabled = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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


class TestModel_AccessActionControls:
    """
    Test Class for AccessActionControls
    """

    def test_access_action_controls_serialization(self):
        """
        Test serialization/deserialization for AccessActionControls
        """

        # Construct a json representation of a AccessActionControls model
        access_action_controls_model_json = {}
        access_action_controls_model_json['add'] = True

        # Construct a model instance of AccessActionControls by calling from_dict on the json representation
        access_action_controls_model = AccessActionControls.from_dict(access_action_controls_model_json)
        assert access_action_controls_model != False

        # Construct a model instance of AccessActionControls by calling from_dict on the json representation
        access_action_controls_model_dict = AccessActionControls.from_dict(access_action_controls_model_json).__dict__
        access_action_controls_model2 = AccessActionControls(**access_action_controls_model_dict)

        # Verify the model instances are equivalent
        assert access_action_controls_model == access_action_controls_model2

        # Convert model instance back to dict and verify no loss of data
        access_action_controls_model_json2 = access_action_controls_model.to_dict()
        assert access_action_controls_model_json2 == access_action_controls_model_json


class TestModel_AccessGroupActionControls:
    """
    Test Class for AccessGroupActionControls
    """

    def test_access_group_action_controls_serialization(self):
        """
        Test serialization/deserialization for AccessGroupActionControls
        """

        # Construct dict forms of any model objects needed in order to build this model.

        access_action_controls_model = {}  # AccessActionControls
        access_action_controls_model['add'] = True

        # Construct a json representation of a AccessGroupActionControls model
        access_group_action_controls_model_json = {}
        access_group_action_controls_model_json['access'] = access_action_controls_model

        # Construct a model instance of AccessGroupActionControls by calling from_dict on the json representation
        access_group_action_controls_model = AccessGroupActionControls.from_dict(
            access_group_action_controls_model_json
        )
        assert access_group_action_controls_model != False

        # Construct a model instance of AccessGroupActionControls by calling from_dict on the json representation
        access_group_action_controls_model_dict = AccessGroupActionControls.from_dict(
            access_group_action_controls_model_json
        ).__dict__
        access_group_action_controls_model2 = AccessGroupActionControls(**access_group_action_controls_model_dict)

        # Verify the model instances are equivalent
        assert access_group_action_controls_model == access_group_action_controls_model2

        # Convert model instance back to dict and verify no loss of data
        access_group_action_controls_model_json2 = access_group_action_controls_model.to_dict()
        assert access_group_action_controls_model_json2 == access_group_action_controls_model_json


class TestModel_AccessGroupInput:
    """
    Test Class for AccessGroupInput
    """

    def test_access_group_input_serialization(self):
        """
        Test serialization/deserialization for AccessGroupInput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        members_action_controls_model = {}  # MembersActionControls
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = True

        members_input_model = {}  # MembersInput
        members_input_model['users'] = ['testString']
        members_input_model['service_ids'] = ['testString']
        members_input_model['action_controls'] = members_action_controls_model

        condition_input_model = {}  # ConditionInput
        condition_input_model['claim'] = 'testString'
        condition_input_model['operator'] = 'testString'
        condition_input_model['value'] = 'testString'

        rules_action_controls_model = {}  # RulesActionControls
        rules_action_controls_model['remove'] = True
        rules_action_controls_model['update'] = True

        rule_input_model = {}  # RuleInput
        rule_input_model['name'] = 'testString'
        rule_input_model['expiration'] = 38
        rule_input_model['realm_name'] = 'testString'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        assertions_action_controls_model = {}  # AssertionsActionControls
        assertions_action_controls_model['add'] = True
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        assertions_input_model = {}  # AssertionsInput
        assertions_input_model['rules'] = [rule_input_model]
        assertions_input_model['action_controls'] = assertions_action_controls_model

        access_action_controls_model = {}  # AccessActionControls
        access_action_controls_model['add'] = True

        access_group_action_controls_model = {}  # AccessGroupActionControls
        access_group_action_controls_model['access'] = access_action_controls_model

        # Construct a json representation of a AccessGroupInput model
        access_group_input_model_json = {}
        access_group_input_model_json['name'] = 'testString'
        access_group_input_model_json['description'] = 'testString'
        access_group_input_model_json['members'] = members_input_model
        access_group_input_model_json['assertions'] = assertions_input_model
        access_group_input_model_json['action_controls'] = access_group_action_controls_model

        # Construct a model instance of AccessGroupInput by calling from_dict on the json representation
        access_group_input_model = AccessGroupInput.from_dict(access_group_input_model_json)
        assert access_group_input_model != False

        # Construct a model instance of AccessGroupInput by calling from_dict on the json representation
        access_group_input_model_dict = AccessGroupInput.from_dict(access_group_input_model_json).__dict__
        access_group_input_model2 = AccessGroupInput(**access_group_input_model_dict)

        # Verify the model instances are equivalent
        assert access_group_input_model == access_group_input_model2

        # Convert model instance back to dict and verify no loss of data
        access_group_input_model_json2 = access_group_input_model.to_dict()
        assert access_group_input_model_json2 == access_group_input_model_json


class TestModel_AccountSettings:
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
        account_settings_model_json['last_modified_at'] = '2019-01-01T12:00:00Z'
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


class TestModel_AddGroupMembersRequestMembersItem:
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
        add_group_members_request_members_item_model = AddGroupMembersRequestMembersItem.from_dict(
            add_group_members_request_members_item_model_json
        )
        assert add_group_members_request_members_item_model != False

        # Construct a model instance of AddGroupMembersRequestMembersItem by calling from_dict on the json representation
        add_group_members_request_members_item_model_dict = AddGroupMembersRequestMembersItem.from_dict(
            add_group_members_request_members_item_model_json
        ).__dict__
        add_group_members_request_members_item_model2 = AddGroupMembersRequestMembersItem(
            **add_group_members_request_members_item_model_dict
        )

        # Verify the model instances are equivalent
        assert add_group_members_request_members_item_model == add_group_members_request_members_item_model2

        # Convert model instance back to dict and verify no loss of data
        add_group_members_request_members_item_model_json2 = add_group_members_request_members_item_model.to_dict()
        assert add_group_members_request_members_item_model_json2 == add_group_members_request_members_item_model_json


class TestModel_AddGroupMembersResponse:
    """
    Test Class for AddGroupMembersResponse
    """

    def test_add_group_members_response_serialization(self):
        """
        Test serialization/deserialization for AddGroupMembersResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {}  # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        add_group_members_response_members_item_model = {}  # AddGroupMembersResponseMembersItem
        add_group_members_response_members_item_model['iam_id'] = 'testString'
        add_group_members_response_members_item_model['type'] = 'testString'
        add_group_members_response_members_item_model['created_at'] = '2019-01-01T12:00:00Z'
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
        add_group_members_response_model_dict = AddGroupMembersResponse.from_dict(
            add_group_members_response_model_json
        ).__dict__
        add_group_members_response_model2 = AddGroupMembersResponse(**add_group_members_response_model_dict)

        # Verify the model instances are equivalent
        assert add_group_members_response_model == add_group_members_response_model2

        # Convert model instance back to dict and verify no loss of data
        add_group_members_response_model_json2 = add_group_members_response_model.to_dict()
        assert add_group_members_response_model_json2 == add_group_members_response_model_json


class TestModel_AddGroupMembersResponseMembersItem:
    """
    Test Class for AddGroupMembersResponseMembersItem
    """

    def test_add_group_members_response_members_item_serialization(self):
        """
        Test serialization/deserialization for AddGroupMembersResponseMembersItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {}  # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        # Construct a json representation of a AddGroupMembersResponseMembersItem model
        add_group_members_response_members_item_model_json = {}
        add_group_members_response_members_item_model_json['iam_id'] = 'testString'
        add_group_members_response_members_item_model_json['type'] = 'testString'
        add_group_members_response_members_item_model_json['created_at'] = '2019-01-01T12:00:00Z'
        add_group_members_response_members_item_model_json['created_by_id'] = 'testString'
        add_group_members_response_members_item_model_json['status_code'] = 38
        add_group_members_response_members_item_model_json['trace'] = 'testString'
        add_group_members_response_members_item_model_json['errors'] = [error_model]

        # Construct a model instance of AddGroupMembersResponseMembersItem by calling from_dict on the json representation
        add_group_members_response_members_item_model = AddGroupMembersResponseMembersItem.from_dict(
            add_group_members_response_members_item_model_json
        )
        assert add_group_members_response_members_item_model != False

        # Construct a model instance of AddGroupMembersResponseMembersItem by calling from_dict on the json representation
        add_group_members_response_members_item_model_dict = AddGroupMembersResponseMembersItem.from_dict(
            add_group_members_response_members_item_model_json
        ).__dict__
        add_group_members_response_members_item_model2 = AddGroupMembersResponseMembersItem(
            **add_group_members_response_members_item_model_dict
        )

        # Verify the model instances are equivalent
        assert add_group_members_response_members_item_model == add_group_members_response_members_item_model2

        # Convert model instance back to dict and verify no loss of data
        add_group_members_response_members_item_model_json2 = add_group_members_response_members_item_model.to_dict()
        assert add_group_members_response_members_item_model_json2 == add_group_members_response_members_item_model_json


class TestModel_AddMembershipMultipleGroupsResponse:
    """
    Test Class for AddMembershipMultipleGroupsResponse
    """

    def test_add_membership_multiple_groups_response_serialization(self):
        """
        Test serialization/deserialization for AddMembershipMultipleGroupsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {}  # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        add_membership_multiple_groups_response_groups_item_model = {}  # AddMembershipMultipleGroupsResponseGroupsItem
        add_membership_multiple_groups_response_groups_item_model['access_group_id'] = 'testString'
        add_membership_multiple_groups_response_groups_item_model['status_code'] = 38
        add_membership_multiple_groups_response_groups_item_model['trace'] = 'testString'
        add_membership_multiple_groups_response_groups_item_model['errors'] = [error_model]

        # Construct a json representation of a AddMembershipMultipleGroupsResponse model
        add_membership_multiple_groups_response_model_json = {}
        add_membership_multiple_groups_response_model_json['iam_id'] = 'testString'
        add_membership_multiple_groups_response_model_json['groups'] = [
            add_membership_multiple_groups_response_groups_item_model
        ]

        # Construct a model instance of AddMembershipMultipleGroupsResponse by calling from_dict on the json representation
        add_membership_multiple_groups_response_model = AddMembershipMultipleGroupsResponse.from_dict(
            add_membership_multiple_groups_response_model_json
        )
        assert add_membership_multiple_groups_response_model != False

        # Construct a model instance of AddMembershipMultipleGroupsResponse by calling from_dict on the json representation
        add_membership_multiple_groups_response_model_dict = AddMembershipMultipleGroupsResponse.from_dict(
            add_membership_multiple_groups_response_model_json
        ).__dict__
        add_membership_multiple_groups_response_model2 = AddMembershipMultipleGroupsResponse(
            **add_membership_multiple_groups_response_model_dict
        )

        # Verify the model instances are equivalent
        assert add_membership_multiple_groups_response_model == add_membership_multiple_groups_response_model2

        # Convert model instance back to dict and verify no loss of data
        add_membership_multiple_groups_response_model_json2 = add_membership_multiple_groups_response_model.to_dict()
        assert add_membership_multiple_groups_response_model_json2 == add_membership_multiple_groups_response_model_json


class TestModel_AddMembershipMultipleGroupsResponseGroupsItem:
    """
    Test Class for AddMembershipMultipleGroupsResponseGroupsItem
    """

    def test_add_membership_multiple_groups_response_groups_item_serialization(self):
        """
        Test serialization/deserialization for AddMembershipMultipleGroupsResponseGroupsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {}  # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        # Construct a json representation of a AddMembershipMultipleGroupsResponseGroupsItem model
        add_membership_multiple_groups_response_groups_item_model_json = {}
        add_membership_multiple_groups_response_groups_item_model_json['access_group_id'] = 'testString'
        add_membership_multiple_groups_response_groups_item_model_json['status_code'] = 38
        add_membership_multiple_groups_response_groups_item_model_json['trace'] = 'testString'
        add_membership_multiple_groups_response_groups_item_model_json['errors'] = [error_model]

        # Construct a model instance of AddMembershipMultipleGroupsResponseGroupsItem by calling from_dict on the json representation
        add_membership_multiple_groups_response_groups_item_model = (
            AddMembershipMultipleGroupsResponseGroupsItem.from_dict(
                add_membership_multiple_groups_response_groups_item_model_json
            )
        )
        assert add_membership_multiple_groups_response_groups_item_model != False

        # Construct a model instance of AddMembershipMultipleGroupsResponseGroupsItem by calling from_dict on the json representation
        add_membership_multiple_groups_response_groups_item_model_dict = (
            AddMembershipMultipleGroupsResponseGroupsItem.from_dict(
                add_membership_multiple_groups_response_groups_item_model_json
            ).__dict__
        )
        add_membership_multiple_groups_response_groups_item_model2 = AddMembershipMultipleGroupsResponseGroupsItem(
            **add_membership_multiple_groups_response_groups_item_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            add_membership_multiple_groups_response_groups_item_model
            == add_membership_multiple_groups_response_groups_item_model2
        )

        # Convert model instance back to dict and verify no loss of data
        add_membership_multiple_groups_response_groups_item_model_json2 = (
            add_membership_multiple_groups_response_groups_item_model.to_dict()
        )
        assert (
            add_membership_multiple_groups_response_groups_item_model_json2
            == add_membership_multiple_groups_response_groups_item_model_json
        )


class TestModel_AssertionsActionControls:
    """
    Test Class for AssertionsActionControls
    """

    def test_assertions_action_controls_serialization(self):
        """
        Test serialization/deserialization for AssertionsActionControls
        """

        # Construct a json representation of a AssertionsActionControls model
        assertions_action_controls_model_json = {}
        assertions_action_controls_model_json['add'] = True
        assertions_action_controls_model_json['remove'] = True
        assertions_action_controls_model_json['update'] = True

        # Construct a model instance of AssertionsActionControls by calling from_dict on the json representation
        assertions_action_controls_model = AssertionsActionControls.from_dict(assertions_action_controls_model_json)
        assert assertions_action_controls_model != False

        # Construct a model instance of AssertionsActionControls by calling from_dict on the json representation
        assertions_action_controls_model_dict = AssertionsActionControls.from_dict(
            assertions_action_controls_model_json
        ).__dict__
        assertions_action_controls_model2 = AssertionsActionControls(**assertions_action_controls_model_dict)

        # Verify the model instances are equivalent
        assert assertions_action_controls_model == assertions_action_controls_model2

        # Convert model instance back to dict and verify no loss of data
        assertions_action_controls_model_json2 = assertions_action_controls_model.to_dict()
        assert assertions_action_controls_model_json2 == assertions_action_controls_model_json


class TestModel_AssertionsInput:
    """
    Test Class for AssertionsInput
    """

    def test_assertions_input_serialization(self):
        """
        Test serialization/deserialization for AssertionsInput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        condition_input_model = {}  # ConditionInput
        condition_input_model['claim'] = 'testString'
        condition_input_model['operator'] = 'testString'
        condition_input_model['value'] = 'testString'

        rules_action_controls_model = {}  # RulesActionControls
        rules_action_controls_model['remove'] = True
        rules_action_controls_model['update'] = True

        rule_input_model = {}  # RuleInput
        rule_input_model['name'] = 'testString'
        rule_input_model['expiration'] = 38
        rule_input_model['realm_name'] = 'testString'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        assertions_action_controls_model = {}  # AssertionsActionControls
        assertions_action_controls_model['add'] = True
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        # Construct a json representation of a AssertionsInput model
        assertions_input_model_json = {}
        assertions_input_model_json['rules'] = [rule_input_model]
        assertions_input_model_json['action_controls'] = assertions_action_controls_model

        # Construct a model instance of AssertionsInput by calling from_dict on the json representation
        assertions_input_model = AssertionsInput.from_dict(assertions_input_model_json)
        assert assertions_input_model != False

        # Construct a model instance of AssertionsInput by calling from_dict on the json representation
        assertions_input_model_dict = AssertionsInput.from_dict(assertions_input_model_json).__dict__
        assertions_input_model2 = AssertionsInput(**assertions_input_model_dict)

        # Verify the model instances are equivalent
        assert assertions_input_model == assertions_input_model2

        # Convert model instance back to dict and verify no loss of data
        assertions_input_model_json2 = assertions_input_model.to_dict()
        assert assertions_input_model_json2 == assertions_input_model_json


class TestModel_AssignmentResourceAccessGroup:
    """
    Test Class for AssignmentResourceAccessGroup
    """

    def test_assignment_resource_access_group_serialization(self):
        """
        Test serialization/deserialization for AssignmentResourceAccessGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_resource_entry_model = {}  # AssignmentResourceEntry
        assignment_resource_entry_model['id'] = 'testString'
        assignment_resource_entry_model['name'] = 'testString'
        assignment_resource_entry_model['version'] = 'testString'
        assignment_resource_entry_model['resource'] = 'testString'
        assignment_resource_entry_model['error'] = 'testString'
        assignment_resource_entry_model['operation'] = 'testString'
        assignment_resource_entry_model['status'] = 'testString'

        # Construct a json representation of a AssignmentResourceAccessGroup model
        assignment_resource_access_group_model_json = {}
        assignment_resource_access_group_model_json['group'] = assignment_resource_entry_model
        assignment_resource_access_group_model_json['members'] = [assignment_resource_entry_model]
        assignment_resource_access_group_model_json['rules'] = [assignment_resource_entry_model]

        # Construct a model instance of AssignmentResourceAccessGroup by calling from_dict on the json representation
        assignment_resource_access_group_model = AssignmentResourceAccessGroup.from_dict(
            assignment_resource_access_group_model_json
        )
        assert assignment_resource_access_group_model != False

        # Construct a model instance of AssignmentResourceAccessGroup by calling from_dict on the json representation
        assignment_resource_access_group_model_dict = AssignmentResourceAccessGroup.from_dict(
            assignment_resource_access_group_model_json
        ).__dict__
        assignment_resource_access_group_model2 = AssignmentResourceAccessGroup(
            **assignment_resource_access_group_model_dict
        )

        # Verify the model instances are equivalent
        assert assignment_resource_access_group_model == assignment_resource_access_group_model2

        # Convert model instance back to dict and verify no loss of data
        assignment_resource_access_group_model_json2 = assignment_resource_access_group_model.to_dict()
        assert assignment_resource_access_group_model_json2 == assignment_resource_access_group_model_json


class TestModel_AssignmentResourceEntry:
    """
    Test Class for AssignmentResourceEntry
    """

    def test_assignment_resource_entry_serialization(self):
        """
        Test serialization/deserialization for AssignmentResourceEntry
        """

        # Construct a json representation of a AssignmentResourceEntry model
        assignment_resource_entry_model_json = {}
        assignment_resource_entry_model_json['id'] = 'testString'
        assignment_resource_entry_model_json['name'] = 'testString'
        assignment_resource_entry_model_json['version'] = 'testString'
        assignment_resource_entry_model_json['resource'] = 'testString'
        assignment_resource_entry_model_json['error'] = 'testString'
        assignment_resource_entry_model_json['operation'] = 'testString'
        assignment_resource_entry_model_json['status'] = 'testString'

        # Construct a model instance of AssignmentResourceEntry by calling from_dict on the json representation
        assignment_resource_entry_model = AssignmentResourceEntry.from_dict(assignment_resource_entry_model_json)
        assert assignment_resource_entry_model != False

        # Construct a model instance of AssignmentResourceEntry by calling from_dict on the json representation
        assignment_resource_entry_model_dict = AssignmentResourceEntry.from_dict(
            assignment_resource_entry_model_json
        ).__dict__
        assignment_resource_entry_model2 = AssignmentResourceEntry(**assignment_resource_entry_model_dict)

        # Verify the model instances are equivalent
        assert assignment_resource_entry_model == assignment_resource_entry_model2

        # Convert model instance back to dict and verify no loss of data
        assignment_resource_entry_model_json2 = assignment_resource_entry_model.to_dict()
        assert assignment_resource_entry_model_json2 == assignment_resource_entry_model_json


class TestModel_ConditionInput:
    """
    Test Class for ConditionInput
    """

    def test_condition_input_serialization(self):
        """
        Test serialization/deserialization for ConditionInput
        """

        # Construct a json representation of a ConditionInput model
        condition_input_model_json = {}
        condition_input_model_json['claim'] = 'testString'
        condition_input_model_json['operator'] = 'testString'
        condition_input_model_json['value'] = 'testString'

        # Construct a model instance of ConditionInput by calling from_dict on the json representation
        condition_input_model = ConditionInput.from_dict(condition_input_model_json)
        assert condition_input_model != False

        # Construct a model instance of ConditionInput by calling from_dict on the json representation
        condition_input_model_dict = ConditionInput.from_dict(condition_input_model_json).__dict__
        condition_input_model2 = ConditionInput(**condition_input_model_dict)

        # Verify the model instances are equivalent
        assert condition_input_model == condition_input_model2

        # Convert model instance back to dict and verify no loss of data
        condition_input_model_json2 = condition_input_model.to_dict()
        assert condition_input_model_json2 == condition_input_model_json


class TestModel_CreateTemplateResponse:
    """
    Test Class for CreateTemplateResponse
    """

    def test_create_template_response_serialization(self):
        """
        Test serialization/deserialization for CreateTemplateResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        members_action_controls_model = {}  # MembersActionControls
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = True

        members_input_model = {}  # MembersInput
        members_input_model['users'] = ['testString']
        members_input_model['service_ids'] = ['testString']
        members_input_model['action_controls'] = members_action_controls_model

        condition_input_model = {}  # ConditionInput
        condition_input_model['claim'] = 'testString'
        condition_input_model['operator'] = 'testString'
        condition_input_model['value'] = 'testString'

        rules_action_controls_model = {}  # RulesActionControls
        rules_action_controls_model['remove'] = True
        rules_action_controls_model['update'] = True

        rule_input_model = {}  # RuleInput
        rule_input_model['name'] = 'testString'
        rule_input_model['expiration'] = 38
        rule_input_model['realm_name'] = 'testString'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        assertions_action_controls_model = {}  # AssertionsActionControls
        assertions_action_controls_model['add'] = True
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        assertions_input_model = {}  # AssertionsInput
        assertions_input_model['rules'] = [rule_input_model]
        assertions_input_model['action_controls'] = assertions_action_controls_model

        access_action_controls_model = {}  # AccessActionControls
        access_action_controls_model['add'] = True

        access_group_action_controls_model = {}  # AccessGroupActionControls
        access_group_action_controls_model['access'] = access_action_controls_model

        access_group_input_model = {}  # AccessGroupInput
        access_group_input_model['name'] = 'testString'
        access_group_input_model['description'] = 'testString'
        access_group_input_model['members'] = members_input_model
        access_group_input_model['assertions'] = assertions_input_model
        access_group_input_model['action_controls'] = access_group_action_controls_model

        policy_templates_input_model = {}  # PolicyTemplatesInput
        policy_templates_input_model['id'] = 'testString'
        policy_templates_input_model['version'] = 'testString'

        # Construct a json representation of a CreateTemplateResponse model
        create_template_response_model_json = {}
        create_template_response_model_json['id'] = 'testString'
        create_template_response_model_json['name'] = 'testString'
        create_template_response_model_json['description'] = 'testString'
        create_template_response_model_json['account_id'] = 'testString'
        create_template_response_model_json['version'] = 'testString'
        create_template_response_model_json['committed'] = True
        create_template_response_model_json['access_group'] = access_group_input_model
        create_template_response_model_json['policy_template_references'] = [policy_templates_input_model]
        create_template_response_model_json['href'] = 'testString'
        create_template_response_model_json['created_at'] = '2019-01-01T12:00:00Z'
        create_template_response_model_json['created_by_id'] = 'testString'
        create_template_response_model_json['last_modified_at'] = '2019-01-01T12:00:00Z'
        create_template_response_model_json['last_modified_by_id'] = 'testString'

        # Construct a model instance of CreateTemplateResponse by calling from_dict on the json representation
        create_template_response_model = CreateTemplateResponse.from_dict(create_template_response_model_json)
        assert create_template_response_model != False

        # Construct a model instance of CreateTemplateResponse by calling from_dict on the json representation
        create_template_response_model_dict = CreateTemplateResponse.from_dict(
            create_template_response_model_json
        ).__dict__
        create_template_response_model2 = CreateTemplateResponse(**create_template_response_model_dict)

        # Verify the model instances are equivalent
        assert create_template_response_model == create_template_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_template_response_model_json2 = create_template_response_model.to_dict()
        assert create_template_response_model_json2 == create_template_response_model_json


class TestModel_DeleteFromAllGroupsResponse:
    """
    Test Class for DeleteFromAllGroupsResponse
    """

    def test_delete_from_all_groups_response_serialization(self):
        """
        Test serialization/deserialization for DeleteFromAllGroupsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {}  # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        delete_from_all_groups_response_groups_item_model = {}  # DeleteFromAllGroupsResponseGroupsItem
        delete_from_all_groups_response_groups_item_model['access_group_id'] = 'testString'
        delete_from_all_groups_response_groups_item_model['status_code'] = 38
        delete_from_all_groups_response_groups_item_model['trace'] = 'testString'
        delete_from_all_groups_response_groups_item_model['errors'] = [error_model]

        # Construct a json representation of a DeleteFromAllGroupsResponse model
        delete_from_all_groups_response_model_json = {}
        delete_from_all_groups_response_model_json['iam_id'] = 'testString'
        delete_from_all_groups_response_model_json['groups'] = [delete_from_all_groups_response_groups_item_model]

        # Construct a model instance of DeleteFromAllGroupsResponse by calling from_dict on the json representation
        delete_from_all_groups_response_model = DeleteFromAllGroupsResponse.from_dict(
            delete_from_all_groups_response_model_json
        )
        assert delete_from_all_groups_response_model != False

        # Construct a model instance of DeleteFromAllGroupsResponse by calling from_dict on the json representation
        delete_from_all_groups_response_model_dict = DeleteFromAllGroupsResponse.from_dict(
            delete_from_all_groups_response_model_json
        ).__dict__
        delete_from_all_groups_response_model2 = DeleteFromAllGroupsResponse(
            **delete_from_all_groups_response_model_dict
        )

        # Verify the model instances are equivalent
        assert delete_from_all_groups_response_model == delete_from_all_groups_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_from_all_groups_response_model_json2 = delete_from_all_groups_response_model.to_dict()
        assert delete_from_all_groups_response_model_json2 == delete_from_all_groups_response_model_json


class TestModel_DeleteFromAllGroupsResponseGroupsItem:
    """
    Test Class for DeleteFromAllGroupsResponseGroupsItem
    """

    def test_delete_from_all_groups_response_groups_item_serialization(self):
        """
        Test serialization/deserialization for DeleteFromAllGroupsResponseGroupsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {}  # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        # Construct a json representation of a DeleteFromAllGroupsResponseGroupsItem model
        delete_from_all_groups_response_groups_item_model_json = {}
        delete_from_all_groups_response_groups_item_model_json['access_group_id'] = 'testString'
        delete_from_all_groups_response_groups_item_model_json['status_code'] = 38
        delete_from_all_groups_response_groups_item_model_json['trace'] = 'testString'
        delete_from_all_groups_response_groups_item_model_json['errors'] = [error_model]

        # Construct a model instance of DeleteFromAllGroupsResponseGroupsItem by calling from_dict on the json representation
        delete_from_all_groups_response_groups_item_model = DeleteFromAllGroupsResponseGroupsItem.from_dict(
            delete_from_all_groups_response_groups_item_model_json
        )
        assert delete_from_all_groups_response_groups_item_model != False

        # Construct a model instance of DeleteFromAllGroupsResponseGroupsItem by calling from_dict on the json representation
        delete_from_all_groups_response_groups_item_model_dict = DeleteFromAllGroupsResponseGroupsItem.from_dict(
            delete_from_all_groups_response_groups_item_model_json
        ).__dict__
        delete_from_all_groups_response_groups_item_model2 = DeleteFromAllGroupsResponseGroupsItem(
            **delete_from_all_groups_response_groups_item_model_dict
        )

        # Verify the model instances are equivalent
        assert delete_from_all_groups_response_groups_item_model == delete_from_all_groups_response_groups_item_model2

        # Convert model instance back to dict and verify no loss of data
        delete_from_all_groups_response_groups_item_model_json2 = (
            delete_from_all_groups_response_groups_item_model.to_dict()
        )
        assert (
            delete_from_all_groups_response_groups_item_model_json2
            == delete_from_all_groups_response_groups_item_model_json
        )


class TestModel_DeleteGroupBulkMembersResponse:
    """
    Test Class for DeleteGroupBulkMembersResponse
    """

    def test_delete_group_bulk_members_response_serialization(self):
        """
        Test serialization/deserialization for DeleteGroupBulkMembersResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {}  # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        delete_group_bulk_members_response_members_item_model = {}  # DeleteGroupBulkMembersResponseMembersItem
        delete_group_bulk_members_response_members_item_model['iam_id'] = 'testString'
        delete_group_bulk_members_response_members_item_model['trace'] = 'testString'
        delete_group_bulk_members_response_members_item_model['status_code'] = 38
        delete_group_bulk_members_response_members_item_model['errors'] = [error_model]

        # Construct a json representation of a DeleteGroupBulkMembersResponse model
        delete_group_bulk_members_response_model_json = {}
        delete_group_bulk_members_response_model_json['access_group_id'] = 'testString'
        delete_group_bulk_members_response_model_json['members'] = [
            delete_group_bulk_members_response_members_item_model
        ]

        # Construct a model instance of DeleteGroupBulkMembersResponse by calling from_dict on the json representation
        delete_group_bulk_members_response_model = DeleteGroupBulkMembersResponse.from_dict(
            delete_group_bulk_members_response_model_json
        )
        assert delete_group_bulk_members_response_model != False

        # Construct a model instance of DeleteGroupBulkMembersResponse by calling from_dict on the json representation
        delete_group_bulk_members_response_model_dict = DeleteGroupBulkMembersResponse.from_dict(
            delete_group_bulk_members_response_model_json
        ).__dict__
        delete_group_bulk_members_response_model2 = DeleteGroupBulkMembersResponse(
            **delete_group_bulk_members_response_model_dict
        )

        # Verify the model instances are equivalent
        assert delete_group_bulk_members_response_model == delete_group_bulk_members_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_group_bulk_members_response_model_json2 = delete_group_bulk_members_response_model.to_dict()
        assert delete_group_bulk_members_response_model_json2 == delete_group_bulk_members_response_model_json


class TestModel_DeleteGroupBulkMembersResponseMembersItem:
    """
    Test Class for DeleteGroupBulkMembersResponseMembersItem
    """

    def test_delete_group_bulk_members_response_members_item_serialization(self):
        """
        Test serialization/deserialization for DeleteGroupBulkMembersResponseMembersItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_model = {}  # Error
        error_model['code'] = 'testString'
        error_model['message'] = 'testString'

        # Construct a json representation of a DeleteGroupBulkMembersResponseMembersItem model
        delete_group_bulk_members_response_members_item_model_json = {}
        delete_group_bulk_members_response_members_item_model_json['iam_id'] = 'testString'
        delete_group_bulk_members_response_members_item_model_json['trace'] = 'testString'
        delete_group_bulk_members_response_members_item_model_json['status_code'] = 38
        delete_group_bulk_members_response_members_item_model_json['errors'] = [error_model]

        # Construct a model instance of DeleteGroupBulkMembersResponseMembersItem by calling from_dict on the json representation
        delete_group_bulk_members_response_members_item_model = DeleteGroupBulkMembersResponseMembersItem.from_dict(
            delete_group_bulk_members_response_members_item_model_json
        )
        assert delete_group_bulk_members_response_members_item_model != False

        # Construct a model instance of DeleteGroupBulkMembersResponseMembersItem by calling from_dict on the json representation
        delete_group_bulk_members_response_members_item_model_dict = (
            DeleteGroupBulkMembersResponseMembersItem.from_dict(
                delete_group_bulk_members_response_members_item_model_json
            ).__dict__
        )
        delete_group_bulk_members_response_members_item_model2 = DeleteGroupBulkMembersResponseMembersItem(
            **delete_group_bulk_members_response_members_item_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            delete_group_bulk_members_response_members_item_model
            == delete_group_bulk_members_response_members_item_model2
        )

        # Convert model instance back to dict and verify no loss of data
        delete_group_bulk_members_response_members_item_model_json2 = (
            delete_group_bulk_members_response_members_item_model.to_dict()
        )
        assert (
            delete_group_bulk_members_response_members_item_model_json2
            == delete_group_bulk_members_response_members_item_model_json
        )


class TestModel_Error:
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


class TestModel_GetTemplateAssignmentResponse:
    """
    Test Class for GetTemplateAssignmentResponse
    """

    def test_get_template_assignment_response_serialization(self):
        """
        Test serialization/deserialization for GetTemplateAssignmentResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_resource_entry_model = {}  # AssignmentResourceEntry
        assignment_resource_entry_model['id'] = 'testString'
        assignment_resource_entry_model['name'] = 'testString'
        assignment_resource_entry_model['version'] = 'testString'
        assignment_resource_entry_model['resource'] = 'testString'
        assignment_resource_entry_model['error'] = 'testString'
        assignment_resource_entry_model['operation'] = 'testString'
        assignment_resource_entry_model['status'] = 'testString'

        assignment_resource_access_group_model = {}  # AssignmentResourceAccessGroup
        assignment_resource_access_group_model['group'] = assignment_resource_entry_model
        assignment_resource_access_group_model['members'] = [assignment_resource_entry_model]
        assignment_resource_access_group_model['rules'] = [assignment_resource_entry_model]

        resource_list_with_target_account_id_model = {}  # ResourceListWithTargetAccountID
        resource_list_with_target_account_id_model['target'] = 'testString'
        resource_list_with_target_account_id_model['access_group'] = assignment_resource_access_group_model
        resource_list_with_target_account_id_model['policy_template_references'] = [assignment_resource_entry_model]

        # Construct a json representation of a GetTemplateAssignmentResponse model
        get_template_assignment_response_model_json = {}
        get_template_assignment_response_model_json['id'] = 'testString'
        get_template_assignment_response_model_json['account_id'] = 'testString'
        get_template_assignment_response_model_json['template_id'] = 'testString'
        get_template_assignment_response_model_json['template_version'] = 'testString'
        get_template_assignment_response_model_json['target_type'] = 'testString'
        get_template_assignment_response_model_json['target'] = 'testString'
        get_template_assignment_response_model_json['operation'] = 'testString'
        get_template_assignment_response_model_json['status'] = 'testString'
        get_template_assignment_response_model_json['resources'] = [resource_list_with_target_account_id_model]
        get_template_assignment_response_model_json['href'] = 'testString'
        get_template_assignment_response_model_json['created_at'] = '2019-01-01T12:00:00Z'
        get_template_assignment_response_model_json['created_by'] = 'testString'
        get_template_assignment_response_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        get_template_assignment_response_model_json['updated_by'] = 'testString'

        # Construct a model instance of GetTemplateAssignmentResponse by calling from_dict on the json representation
        get_template_assignment_response_model = GetTemplateAssignmentResponse.from_dict(
            get_template_assignment_response_model_json
        )
        assert get_template_assignment_response_model != False

        # Construct a model instance of GetTemplateAssignmentResponse by calling from_dict on the json representation
        get_template_assignment_response_model_dict = GetTemplateAssignmentResponse.from_dict(
            get_template_assignment_response_model_json
        ).__dict__
        get_template_assignment_response_model2 = GetTemplateAssignmentResponse(
            **get_template_assignment_response_model_dict
        )

        # Verify the model instances are equivalent
        assert get_template_assignment_response_model == get_template_assignment_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_template_assignment_response_model_json2 = get_template_assignment_response_model.to_dict()
        assert get_template_assignment_response_model_json2 == get_template_assignment_response_model_json


class TestModel_Group:
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


class TestModel_GroupMembersList:
    """
    Test Class for GroupMembersList
    """

    def test_group_members_list_serialization(self):
        """
        Test serialization/deserialization for GroupMembersList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        href_struct_model = {}  # HrefStruct
        href_struct_model['href'] = 'testString'

        list_group_members_response_member_model = {}  # ListGroupMembersResponseMember
        list_group_members_response_member_model['iam_id'] = 'testString'
        list_group_members_response_member_model['type'] = 'testString'
        list_group_members_response_member_model['membership_type'] = 'testString'
        list_group_members_response_member_model['name'] = 'testString'
        list_group_members_response_member_model['email'] = 'testString'
        list_group_members_response_member_model['description'] = 'testString'
        list_group_members_response_member_model['href'] = 'testString'
        list_group_members_response_member_model['created_at'] = '2019-01-01T12:00:00Z'
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


class TestModel_GroupsList:
    """
    Test Class for GroupsList
    """

    def test_groups_list_serialization(self):
        """
        Test serialization/deserialization for GroupsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        href_struct_model = {}  # HrefStruct
        href_struct_model['href'] = 'testString'

        group_model = {}  # Group
        group_model['id'] = 'testString'
        group_model['name'] = 'testString'
        group_model['description'] = 'testString'
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


class TestModel_HrefStruct:
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


class TestModel_ListGroupMembersResponseMember:
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
        list_group_members_response_member_model_json['membership_type'] = 'testString'
        list_group_members_response_member_model_json['name'] = 'testString'
        list_group_members_response_member_model_json['email'] = 'testString'
        list_group_members_response_member_model_json['description'] = 'testString'
        list_group_members_response_member_model_json['href'] = 'testString'
        list_group_members_response_member_model_json['created_at'] = '2019-01-01T12:00:00Z'
        list_group_members_response_member_model_json['created_by_id'] = 'testString'

        # Construct a model instance of ListGroupMembersResponseMember by calling from_dict on the json representation
        list_group_members_response_member_model = ListGroupMembersResponseMember.from_dict(
            list_group_members_response_member_model_json
        )
        assert list_group_members_response_member_model != False

        # Construct a model instance of ListGroupMembersResponseMember by calling from_dict on the json representation
        list_group_members_response_member_model_dict = ListGroupMembersResponseMember.from_dict(
            list_group_members_response_member_model_json
        ).__dict__
        list_group_members_response_member_model2 = ListGroupMembersResponseMember(
            **list_group_members_response_member_model_dict
        )

        # Verify the model instances are equivalent
        assert list_group_members_response_member_model == list_group_members_response_member_model2

        # Convert model instance back to dict and verify no loss of data
        list_group_members_response_member_model_json2 = list_group_members_response_member_model.to_dict()
        assert list_group_members_response_member_model_json2 == list_group_members_response_member_model_json


class TestModel_ListTemplateVersionsResponse:
    """
    Test Class for ListTemplateVersionsResponse
    """

    def test_list_template_versions_response_serialization(self):
        """
        Test serialization/deserialization for ListTemplateVersionsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        href_struct_model = {}  # HrefStruct
        href_struct_model['href'] = 'testString'

        members_action_controls_model = {}  # MembersActionControls
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = True

        members_input_model = {}  # MembersInput
        members_input_model['users'] = ['testString']
        members_input_model['service_ids'] = ['testString']
        members_input_model['action_controls'] = members_action_controls_model

        condition_input_model = {}  # ConditionInput
        condition_input_model['claim'] = 'testString'
        condition_input_model['operator'] = 'testString'
        condition_input_model['value'] = 'testString'

        rules_action_controls_model = {}  # RulesActionControls
        rules_action_controls_model['remove'] = True
        rules_action_controls_model['update'] = True

        rule_input_model = {}  # RuleInput
        rule_input_model['name'] = 'testString'
        rule_input_model['expiration'] = 38
        rule_input_model['realm_name'] = 'testString'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        assertions_action_controls_model = {}  # AssertionsActionControls
        assertions_action_controls_model['add'] = True
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        assertions_input_model = {}  # AssertionsInput
        assertions_input_model['rules'] = [rule_input_model]
        assertions_input_model['action_controls'] = assertions_action_controls_model

        access_action_controls_model = {}  # AccessActionControls
        access_action_controls_model['add'] = True

        access_group_action_controls_model = {}  # AccessGroupActionControls
        access_group_action_controls_model['access'] = access_action_controls_model

        access_group_input_model = {}  # AccessGroupInput
        access_group_input_model['name'] = 'testString'
        access_group_input_model['description'] = 'testString'
        access_group_input_model['members'] = members_input_model
        access_group_input_model['assertions'] = assertions_input_model
        access_group_input_model['action_controls'] = access_group_action_controls_model

        policy_templates_input_model = {}  # PolicyTemplatesInput
        policy_templates_input_model['id'] = 'testString'
        policy_templates_input_model['version'] = 'testString'

        list_templates_versions_response_model = {}  # ListTemplatesVersionsResponse
        list_templates_versions_response_model['name'] = 'testString'
        list_templates_versions_response_model['description'] = 'testString'
        list_templates_versions_response_model['account_id'] = 'testString'
        list_templates_versions_response_model['version'] = 'testString'
        list_templates_versions_response_model['committed'] = True
        list_templates_versions_response_model['access_group'] = access_group_input_model
        list_templates_versions_response_model['policy_template_references'] = [policy_templates_input_model]
        list_templates_versions_response_model['href'] = 'testString'
        list_templates_versions_response_model['created_at'] = 'testString'
        list_templates_versions_response_model['created_by_id'] = 'testString'
        list_templates_versions_response_model['last_modified_at'] = 'testString'
        list_templates_versions_response_model['last_modified_by_id'] = 'testString'

        # Construct a json representation of a ListTemplateVersionsResponse model
        list_template_versions_response_model_json = {}
        list_template_versions_response_model_json['limit'] = 38
        list_template_versions_response_model_json['offset'] = 38
        list_template_versions_response_model_json['total_count'] = 38
        list_template_versions_response_model_json['first'] = href_struct_model
        list_template_versions_response_model_json['previous'] = href_struct_model
        list_template_versions_response_model_json['next'] = href_struct_model
        list_template_versions_response_model_json['last'] = href_struct_model
        list_template_versions_response_model_json['versions'] = [list_templates_versions_response_model]

        # Construct a model instance of ListTemplateVersionsResponse by calling from_dict on the json representation
        list_template_versions_response_model = ListTemplateVersionsResponse.from_dict(
            list_template_versions_response_model_json
        )
        assert list_template_versions_response_model != False

        # Construct a model instance of ListTemplateVersionsResponse by calling from_dict on the json representation
        list_template_versions_response_model_dict = ListTemplateVersionsResponse.from_dict(
            list_template_versions_response_model_json
        ).__dict__
        list_template_versions_response_model2 = ListTemplateVersionsResponse(
            **list_template_versions_response_model_dict
        )

        # Verify the model instances are equivalent
        assert list_template_versions_response_model == list_template_versions_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_template_versions_response_model_json2 = list_template_versions_response_model.to_dict()
        assert list_template_versions_response_model_json2 == list_template_versions_response_model_json


class TestModel_ListTemplatesResponse:
    """
    Test Class for ListTemplatesResponse
    """

    def test_list_templates_response_serialization(self):
        """
        Test serialization/deserialization for ListTemplatesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        href_struct_model = {}  # HrefStruct
        href_struct_model['href'] = 'testString'

        template_item_model = {}  # TemplateItem
        template_item_model['id'] = 'testString'
        template_item_model['name'] = 'testString'
        template_item_model['description'] = 'testString'
        template_item_model['version'] = 'testString'
        template_item_model['created_at'] = 'testString'
        template_item_model['created_by_id'] = 'testString'
        template_item_model['last_modified_at'] = 'testString'
        template_item_model['last_modified_by_id'] = 'testString'
        template_item_model['href'] = 'testString'

        # Construct a json representation of a ListTemplatesResponse model
        list_templates_response_model_json = {}
        list_templates_response_model_json['limit'] = 38
        list_templates_response_model_json['offset'] = 38
        list_templates_response_model_json['total_count'] = 38
        list_templates_response_model_json['first'] = href_struct_model
        list_templates_response_model_json['previous'] = href_struct_model
        list_templates_response_model_json['next'] = href_struct_model
        list_templates_response_model_json['last'] = href_struct_model
        list_templates_response_model_json['groups_templates'] = [template_item_model]

        # Construct a model instance of ListTemplatesResponse by calling from_dict on the json representation
        list_templates_response_model = ListTemplatesResponse.from_dict(list_templates_response_model_json)
        assert list_templates_response_model != False

        # Construct a model instance of ListTemplatesResponse by calling from_dict on the json representation
        list_templates_response_model_dict = ListTemplatesResponse.from_dict(
            list_templates_response_model_json
        ).__dict__
        list_templates_response_model2 = ListTemplatesResponse(**list_templates_response_model_dict)

        # Verify the model instances are equivalent
        assert list_templates_response_model == list_templates_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_templates_response_model_json2 = list_templates_response_model.to_dict()
        assert list_templates_response_model_json2 == list_templates_response_model_json


class TestModel_ListTemplatesVersionsResponse:
    """
    Test Class for ListTemplatesVersionsResponse
    """

    def test_list_templates_versions_response_serialization(self):
        """
        Test serialization/deserialization for ListTemplatesVersionsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        members_action_controls_model = {}  # MembersActionControls
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = True

        members_input_model = {}  # MembersInput
        members_input_model['users'] = ['testString']
        members_input_model['service_ids'] = ['testString']
        members_input_model['action_controls'] = members_action_controls_model

        condition_input_model = {}  # ConditionInput
        condition_input_model['claim'] = 'testString'
        condition_input_model['operator'] = 'testString'
        condition_input_model['value'] = 'testString'

        rules_action_controls_model = {}  # RulesActionControls
        rules_action_controls_model['remove'] = True
        rules_action_controls_model['update'] = True

        rule_input_model = {}  # RuleInput
        rule_input_model['name'] = 'testString'
        rule_input_model['expiration'] = 38
        rule_input_model['realm_name'] = 'testString'
        rule_input_model['conditions'] = [condition_input_model]
        rule_input_model['action_controls'] = rules_action_controls_model

        assertions_action_controls_model = {}  # AssertionsActionControls
        assertions_action_controls_model['add'] = True
        assertions_action_controls_model['remove'] = True
        assertions_action_controls_model['update'] = True

        assertions_input_model = {}  # AssertionsInput
        assertions_input_model['rules'] = [rule_input_model]
        assertions_input_model['action_controls'] = assertions_action_controls_model

        access_action_controls_model = {}  # AccessActionControls
        access_action_controls_model['add'] = True

        access_group_action_controls_model = {}  # AccessGroupActionControls
        access_group_action_controls_model['access'] = access_action_controls_model

        access_group_input_model = {}  # AccessGroupInput
        access_group_input_model['name'] = 'testString'
        access_group_input_model['description'] = 'testString'
        access_group_input_model['members'] = members_input_model
        access_group_input_model['assertions'] = assertions_input_model
        access_group_input_model['action_controls'] = access_group_action_controls_model

        policy_templates_input_model = {}  # PolicyTemplatesInput
        policy_templates_input_model['id'] = 'testString'
        policy_templates_input_model['version'] = 'testString'

        # Construct a json representation of a ListTemplatesVersionsResponse model
        list_templates_versions_response_model_json = {}
        list_templates_versions_response_model_json['name'] = 'testString'
        list_templates_versions_response_model_json['description'] = 'testString'
        list_templates_versions_response_model_json['account_id'] = 'testString'
        list_templates_versions_response_model_json['version'] = 'testString'
        list_templates_versions_response_model_json['committed'] = True
        list_templates_versions_response_model_json['access_group'] = access_group_input_model
        list_templates_versions_response_model_json['policy_template_references'] = [policy_templates_input_model]
        list_templates_versions_response_model_json['href'] = 'testString'
        list_templates_versions_response_model_json['created_at'] = 'testString'
        list_templates_versions_response_model_json['created_by_id'] = 'testString'
        list_templates_versions_response_model_json['last_modified_at'] = 'testString'
        list_templates_versions_response_model_json['last_modified_by_id'] = 'testString'

        # Construct a model instance of ListTemplatesVersionsResponse by calling from_dict on the json representation
        list_templates_versions_response_model = ListTemplatesVersionsResponse.from_dict(
            list_templates_versions_response_model_json
        )
        assert list_templates_versions_response_model != False

        # Construct a model instance of ListTemplatesVersionsResponse by calling from_dict on the json representation
        list_templates_versions_response_model_dict = ListTemplatesVersionsResponse.from_dict(
            list_templates_versions_response_model_json
        ).__dict__
        list_templates_versions_response_model2 = ListTemplatesVersionsResponse(
            **list_templates_versions_response_model_dict
        )

        # Verify the model instances are equivalent
        assert list_templates_versions_response_model == list_templates_versions_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_templates_versions_response_model_json2 = list_templates_versions_response_model.to_dict()
        assert list_templates_versions_response_model_json2 == list_templates_versions_response_model_json


class TestModel_MembersActionControls:
    """
    Test Class for MembersActionControls
    """

    def test_members_action_controls_serialization(self):
        """
        Test serialization/deserialization for MembersActionControls
        """

        # Construct a json representation of a MembersActionControls model
        members_action_controls_model_json = {}
        members_action_controls_model_json['add'] = True
        members_action_controls_model_json['remove'] = True

        # Construct a model instance of MembersActionControls by calling from_dict on the json representation
        members_action_controls_model = MembersActionControls.from_dict(members_action_controls_model_json)
        assert members_action_controls_model != False

        # Construct a model instance of MembersActionControls by calling from_dict on the json representation
        members_action_controls_model_dict = MembersActionControls.from_dict(
            members_action_controls_model_json
        ).__dict__
        members_action_controls_model2 = MembersActionControls(**members_action_controls_model_dict)

        # Verify the model instances are equivalent
        assert members_action_controls_model == members_action_controls_model2

        # Convert model instance back to dict and verify no loss of data
        members_action_controls_model_json2 = members_action_controls_model.to_dict()
        assert members_action_controls_model_json2 == members_action_controls_model_json


class TestModel_MembersInput:
    """
    Test Class for MembersInput
    """

    def test_members_input_serialization(self):
        """
        Test serialization/deserialization for MembersInput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        members_action_controls_model = {}  # MembersActionControls
        members_action_controls_model['add'] = True
        members_action_controls_model['remove'] = True

        # Construct a json representation of a MembersInput model
        members_input_model_json = {}
        members_input_model_json['users'] = ['testString']
        members_input_model_json['service_ids'] = ['testString']
        members_input_model_json['action_controls'] = members_action_controls_model

        # Construct a model instance of MembersInput by calling from_dict on the json representation
        members_input_model = MembersInput.from_dict(members_input_model_json)
        assert members_input_model != False

        # Construct a model instance of MembersInput by calling from_dict on the json representation
        members_input_model_dict = MembersInput.from_dict(members_input_model_json).__dict__
        members_input_model2 = MembersInput(**members_input_model_dict)

        # Verify the model instances are equivalent
        assert members_input_model == members_input_model2

        # Convert model instance back to dict and verify no loss of data
        members_input_model_json2 = members_input_model.to_dict()
        assert members_input_model_json2 == members_input_model_json


class TestModel_PolicyTemplatesInput:
    """
    Test Class for PolicyTemplatesInput
    """

    def test_policy_templates_input_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplatesInput
        """

        # Construct a json representation of a PolicyTemplatesInput model
        policy_templates_input_model_json = {}
        policy_templates_input_model_json['id'] = 'testString'
        policy_templates_input_model_json['version'] = 'testString'

        # Construct a model instance of PolicyTemplatesInput by calling from_dict on the json representation
        policy_templates_input_model = PolicyTemplatesInput.from_dict(policy_templates_input_model_json)
        assert policy_templates_input_model != False

        # Construct a model instance of PolicyTemplatesInput by calling from_dict on the json representation
        policy_templates_input_model_dict = PolicyTemplatesInput.from_dict(policy_templates_input_model_json).__dict__
        policy_templates_input_model2 = PolicyTemplatesInput(**policy_templates_input_model_dict)

        # Verify the model instances are equivalent
        assert policy_templates_input_model == policy_templates_input_model2

        # Convert model instance back to dict and verify no loss of data
        policy_templates_input_model_json2 = policy_templates_input_model.to_dict()
        assert policy_templates_input_model_json2 == policy_templates_input_model_json


class TestModel_ResourceListWithTargetAccountID:
    """
    Test Class for ResourceListWithTargetAccountID
    """

    def test_resource_list_with_target_account_id_serialization(self):
        """
        Test serialization/deserialization for ResourceListWithTargetAccountID
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assignment_resource_entry_model = {}  # AssignmentResourceEntry
        assignment_resource_entry_model['id'] = 'testString'
        assignment_resource_entry_model['name'] = 'testString'
        assignment_resource_entry_model['version'] = 'testString'
        assignment_resource_entry_model['resource'] = 'testString'
        assignment_resource_entry_model['error'] = 'testString'
        assignment_resource_entry_model['operation'] = 'testString'
        assignment_resource_entry_model['status'] = 'testString'

        assignment_resource_access_group_model = {}  # AssignmentResourceAccessGroup
        assignment_resource_access_group_model['group'] = assignment_resource_entry_model
        assignment_resource_access_group_model['members'] = [assignment_resource_entry_model]
        assignment_resource_access_group_model['rules'] = [assignment_resource_entry_model]

        # Construct a json representation of a ResourceListWithTargetAccountID model
        resource_list_with_target_account_id_model_json = {}
        resource_list_with_target_account_id_model_json['target'] = 'testString'
        resource_list_with_target_account_id_model_json['access_group'] = assignment_resource_access_group_model
        resource_list_with_target_account_id_model_json['policy_template_references'] = [
            assignment_resource_entry_model
        ]

        # Construct a model instance of ResourceListWithTargetAccountID by calling from_dict on the json representation
        resource_list_with_target_account_id_model = ResourceListWithTargetAccountID.from_dict(
            resource_list_with_target_account_id_model_json
        )
        assert resource_list_with_target_account_id_model != False

        # Construct a model instance of ResourceListWithTargetAccountID by calling from_dict on the json representation
        resource_list_with_target_account_id_model_dict = ResourceListWithTargetAccountID.from_dict(
            resource_list_with_target_account_id_model_json
        ).__dict__
        resource_list_with_target_account_id_model2 = ResourceListWithTargetAccountID(
            **resource_list_with_target_account_id_model_dict
        )

        # Verify the model instances are equivalent
        assert resource_list_with_target_account_id_model == resource_list_with_target_account_id_model2

        # Convert model instance back to dict and verify no loss of data
        resource_list_with_target_account_id_model_json2 = resource_list_with_target_account_id_model.to_dict()
        assert resource_list_with_target_account_id_model_json2 == resource_list_with_target_account_id_model_json


class TestModel_Rule:
    """
    Test Class for Rule
    """

    def test_rule_serialization(self):
        """
        Test serialization/deserialization for Rule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_conditions_model = {}  # RuleConditions
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
        rule_model_json['created_at'] = '2019-01-01T12:00:00Z'
        rule_model_json['created_by_id'] = 'testString'
        rule_model_json['last_modified_at'] = '2019-01-01T12:00:00Z'
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


class TestModel_RuleConditions:
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


class TestModel_RuleInput:
    """
    Test Class for RuleInput
    """

    def test_rule_input_serialization(self):
        """
        Test serialization/deserialization for RuleInput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        condition_input_model = {}  # ConditionInput
        condition_input_model['claim'] = 'testString'
        condition_input_model['operator'] = 'testString'
        condition_input_model['value'] = 'testString'

        rules_action_controls_model = {}  # RulesActionControls
        rules_action_controls_model['remove'] = True
        rules_action_controls_model['update'] = True

        # Construct a json representation of a RuleInput model
        rule_input_model_json = {}
        rule_input_model_json['name'] = 'testString'
        rule_input_model_json['expiration'] = 38
        rule_input_model_json['realm_name'] = 'testString'
        rule_input_model_json['conditions'] = [condition_input_model]
        rule_input_model_json['action_controls'] = rules_action_controls_model

        # Construct a model instance of RuleInput by calling from_dict on the json representation
        rule_input_model = RuleInput.from_dict(rule_input_model_json)
        assert rule_input_model != False

        # Construct a model instance of RuleInput by calling from_dict on the json representation
        rule_input_model_dict = RuleInput.from_dict(rule_input_model_json).__dict__
        rule_input_model2 = RuleInput(**rule_input_model_dict)

        # Verify the model instances are equivalent
        assert rule_input_model == rule_input_model2

        # Convert model instance back to dict and verify no loss of data
        rule_input_model_json2 = rule_input_model.to_dict()
        assert rule_input_model_json2 == rule_input_model_json


class TestModel_RulesActionControls:
    """
    Test Class for RulesActionControls
    """

    def test_rules_action_controls_serialization(self):
        """
        Test serialization/deserialization for RulesActionControls
        """

        # Construct a json representation of a RulesActionControls model
        rules_action_controls_model_json = {}
        rules_action_controls_model_json['remove'] = True
        rules_action_controls_model_json['update'] = True

        # Construct a model instance of RulesActionControls by calling from_dict on the json representation
        rules_action_controls_model = RulesActionControls.from_dict(rules_action_controls_model_json)
        assert rules_action_controls_model != False

        # Construct a model instance of RulesActionControls by calling from_dict on the json representation
        rules_action_controls_model_dict = RulesActionControls.from_dict(rules_action_controls_model_json).__dict__
        rules_action_controls_model2 = RulesActionControls(**rules_action_controls_model_dict)

        # Verify the model instances are equivalent
        assert rules_action_controls_model == rules_action_controls_model2

        # Convert model instance back to dict and verify no loss of data
        rules_action_controls_model_json2 = rules_action_controls_model.to_dict()
        assert rules_action_controls_model_json2 == rules_action_controls_model_json


class TestModel_RulesList:
    """
    Test Class for RulesList
    """

    def test_rules_list_serialization(self):
        """
        Test serialization/deserialization for RulesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_conditions_model = {}  # RuleConditions
        rule_conditions_model['claim'] = 'testString'
        rule_conditions_model['operator'] = 'EQUALS'
        rule_conditions_model['value'] = 'testString'

        rule_model = {}  # Rule
        rule_model['id'] = 'testString'
        rule_model['name'] = 'testString'
        rule_model['expiration'] = 38
        rule_model['realm_name'] = 'testString'
        rule_model['access_group_id'] = 'testString'
        rule_model['account_id'] = 'testString'
        rule_model['conditions'] = [rule_conditions_model]
        rule_model['created_at'] = '2019-01-01T12:00:00Z'
        rule_model['created_by_id'] = 'testString'
        rule_model['last_modified_at'] = '2019-01-01T12:00:00Z'
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


class TestModel_TemplateCreateAssignmentResponse:
    """
    Test Class for TemplateCreateAssignmentResponse
    """

    def test_template_create_assignment_response_serialization(self):
        """
        Test serialization/deserialization for TemplateCreateAssignmentResponse
        """

        # Construct a json representation of a TemplateCreateAssignmentResponse model
        template_create_assignment_response_model_json = {}
        template_create_assignment_response_model_json['id'] = 'testString'
        template_create_assignment_response_model_json['account_id'] = 'testString'
        template_create_assignment_response_model_json['template_id'] = 'testString'
        template_create_assignment_response_model_json['template_version'] = 'testString'
        template_create_assignment_response_model_json['target_type'] = 'testString'
        template_create_assignment_response_model_json['target'] = 'testString'
        template_create_assignment_response_model_json['operation'] = 'testString'
        template_create_assignment_response_model_json['status'] = 'testString'
        template_create_assignment_response_model_json['href'] = 'testString'
        template_create_assignment_response_model_json['created_at'] = '2019-01-01T12:00:00Z'
        template_create_assignment_response_model_json['created_by'] = 'testString'
        template_create_assignment_response_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        template_create_assignment_response_model_json['updated_by'] = 'testString'

        # Construct a model instance of TemplateCreateAssignmentResponse by calling from_dict on the json representation
        template_create_assignment_response_model = TemplateCreateAssignmentResponse.from_dict(
            template_create_assignment_response_model_json
        )
        assert template_create_assignment_response_model != False

        # Construct a model instance of TemplateCreateAssignmentResponse by calling from_dict on the json representation
        template_create_assignment_response_model_dict = TemplateCreateAssignmentResponse.from_dict(
            template_create_assignment_response_model_json
        ).__dict__
        template_create_assignment_response_model2 = TemplateCreateAssignmentResponse(
            **template_create_assignment_response_model_dict
        )

        # Verify the model instances are equivalent
        assert template_create_assignment_response_model == template_create_assignment_response_model2

        # Convert model instance back to dict and verify no loss of data
        template_create_assignment_response_model_json2 = template_create_assignment_response_model.to_dict()
        assert template_create_assignment_response_model_json2 == template_create_assignment_response_model_json


class TestModel_TemplateItem:
    """
    Test Class for TemplateItem
    """

    def test_template_item_serialization(self):
        """
        Test serialization/deserialization for TemplateItem
        """

        # Construct a json representation of a TemplateItem model
        template_item_model_json = {}
        template_item_model_json['id'] = 'testString'
        template_item_model_json['name'] = 'testString'
        template_item_model_json['description'] = 'testString'
        template_item_model_json['version'] = 'testString'
        template_item_model_json['created_at'] = 'testString'
        template_item_model_json['created_by_id'] = 'testString'
        template_item_model_json['last_modified_at'] = 'testString'
        template_item_model_json['last_modified_by_id'] = 'testString'
        template_item_model_json['href'] = 'testString'

        # Construct a model instance of TemplateItem by calling from_dict on the json representation
        template_item_model = TemplateItem.from_dict(template_item_model_json)
        assert template_item_model != False

        # Construct a model instance of TemplateItem by calling from_dict on the json representation
        template_item_model_dict = TemplateItem.from_dict(template_item_model_json).__dict__
        template_item_model2 = TemplateItem(**template_item_model_dict)

        # Verify the model instances are equivalent
        assert template_item_model == template_item_model2

        # Convert model instance back to dict and verify no loss of data
        template_item_model_json2 = template_item_model.to_dict()
        assert template_item_model_json2 == template_item_model_json


class TestModel_TemplatesListAssignmentResponse:
    """
    Test Class for TemplatesListAssignmentResponse
    """

    def test_templates_list_assignment_response_serialization(self):
        """
        Test serialization/deserialization for TemplatesListAssignmentResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        template_create_assignment_response_model = {}  # TemplateCreateAssignmentResponse
        template_create_assignment_response_model['id'] = 'testString'
        template_create_assignment_response_model['account_id'] = 'testString'
        template_create_assignment_response_model['template_id'] = 'testString'
        template_create_assignment_response_model['template_version'] = 'testString'
        template_create_assignment_response_model['target_type'] = 'testString'
        template_create_assignment_response_model['target'] = 'testString'
        template_create_assignment_response_model['operation'] = 'testString'
        template_create_assignment_response_model['status'] = 'testString'
        template_create_assignment_response_model['href'] = 'testString'
        template_create_assignment_response_model['created_at'] = '2019-01-01T12:00:00Z'
        template_create_assignment_response_model['created_by'] = 'testString'
        template_create_assignment_response_model['updated_at'] = '2019-01-01T12:00:00Z'
        template_create_assignment_response_model['updated_by'] = 'testString'

        # Construct a json representation of a TemplatesListAssignmentResponse model
        templates_list_assignment_response_model_json = {}
        templates_list_assignment_response_model_json['total'] = 26
        templates_list_assignment_response_model_json['limit'] = 26
        templates_list_assignment_response_model_json['offset'] = 26
        templates_list_assignment_response_model_json['groups_assignment'] = [template_create_assignment_response_model]

        # Construct a model instance of TemplatesListAssignmentResponse by calling from_dict on the json representation
        templates_list_assignment_response_model = TemplatesListAssignmentResponse.from_dict(
            templates_list_assignment_response_model_json
        )
        assert templates_list_assignment_response_model != False

        # Construct a model instance of TemplatesListAssignmentResponse by calling from_dict on the json representation
        templates_list_assignment_response_model_dict = TemplatesListAssignmentResponse.from_dict(
            templates_list_assignment_response_model_json
        ).__dict__
        templates_list_assignment_response_model2 = TemplatesListAssignmentResponse(
            **templates_list_assignment_response_model_dict
        )

        # Verify the model instances are equivalent
        assert templates_list_assignment_response_model == templates_list_assignment_response_model2

        # Convert model instance back to dict and verify no loss of data
        templates_list_assignment_response_model_json2 = templates_list_assignment_response_model.to_dict()
        assert templates_list_assignment_response_model_json2 == templates_list_assignment_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
