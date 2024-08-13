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
Unit Tests for IamIdentityV1
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
from ibm_platform_services.iam_identity_v1 import *


_service = IamIdentityV1(authenticator=NoAuthAuthenticator())

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
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: APIKeyOperations
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListApiKeys:
    """
    Test Class for list_api_keys
    """

    @responses.activate
    def test_list_api_keys_all_params(self):
        """
        list_api_keys()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "apikeys": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        pagesize = 38
        pagetoken = 'testString'
        scope = 'entity'
        type = 'user'
        sort = 'testString'
        order = 'asc'
        include_history = False

        # Invoke method
        response = _service.list_api_keys(
            account_id=account_id,
            iam_id=iam_id,
            pagesize=pagesize,
            pagetoken=pagetoken,
            scope=scope,
            type=type,
            sort=sort,
            order=order,
            include_history=include_history,
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
        assert 'pagesize={}'.format(pagesize) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'scope={}'.format(scope) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_list_api_keys_all_params_with_retries(self):
        # Enable retries and run test_list_api_keys_all_params.
        _service.enable_retries()
        self.test_list_api_keys_all_params()

        # Disable retries and run test_list_api_keys_all_params.
        _service.disable_retries()
        self.test_list_api_keys_all_params()

    @responses.activate
    def test_list_api_keys_required_params(self):
        """
        test_list_api_keys_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "apikeys": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_api_keys()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_api_keys_required_params_with_retries(self):
        # Enable retries and run test_list_api_keys_required_params.
        _service.enable_retries()
        self.test_list_api_keys_required_params()

        # Disable retries and run test_list_api_keys_required_params.
        _service.disable_retries()
        self.test_list_api_keys_required_params()


class TestCreateApiKey:
    """
    Test Class for create_api_key
    """

    @responses.activate
    def test_create_api_key_all_params(self):
        """
        create_api_key()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        name = 'testString'
        iam_id = 'testString'
        description = 'testString'
        account_id = 'testString'
        apikey = 'testString'
        store_value = True
        support_sessions = True
        action_when_leaked = 'testString'
        entity_lock = 'false'
        entity_disable = 'false'

        # Invoke method
        response = _service.create_api_key(
            name,
            iam_id,
            description=description,
            account_id=account_id,
            apikey=apikey,
            store_value=store_value,
            support_sessions=support_sessions,
            action_when_leaked=action_when_leaked,
            entity_lock=entity_lock,
            entity_disable=entity_disable,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['iam_id'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['apikey'] == 'testString'
        assert req_body['store_value'] == True
        assert req_body['support_sessions'] == True
        assert req_body['action_when_leaked'] == 'testString'

    def test_create_api_key_all_params_with_retries(self):
        # Enable retries and run test_create_api_key_all_params.
        _service.enable_retries()
        self.test_create_api_key_all_params()

        # Disable retries and run test_create_api_key_all_params.
        _service.disable_retries()
        self.test_create_api_key_all_params()

    @responses.activate
    def test_create_api_key_required_params(self):
        """
        test_create_api_key_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        name = 'testString'
        iam_id = 'testString'
        description = 'testString'
        account_id = 'testString'
        apikey = 'testString'
        store_value = True
        support_sessions = True
        action_when_leaked = 'testString'

        # Invoke method
        response = _service.create_api_key(
            name,
            iam_id,
            description=description,
            account_id=account_id,
            apikey=apikey,
            store_value=store_value,
            support_sessions=support_sessions,
            action_when_leaked=action_when_leaked,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['iam_id'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['apikey'] == 'testString'
        assert req_body['store_value'] == True
        assert req_body['support_sessions'] == True
        assert req_body['action_when_leaked'] == 'testString'

    def test_create_api_key_required_params_with_retries(self):
        # Enable retries and run test_create_api_key_required_params.
        _service.enable_retries()
        self.test_create_api_key_required_params()

        # Disable retries and run test_create_api_key_required_params.
        _service.disable_retries()
        self.test_create_api_key_required_params()

    @responses.activate
    def test_create_api_key_value_error(self):
        """
        test_create_api_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        name = 'testString'
        iam_id = 'testString'
        description = 'testString'
        account_id = 'testString'
        apikey = 'testString'
        store_value = True
        support_sessions = True
        action_when_leaked = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_api_key(**req_copy)

    def test_create_api_key_value_error_with_retries(self):
        # Enable retries and run test_create_api_key_value_error.
        _service.enable_retries()
        self.test_create_api_key_value_error()

        # Disable retries and run test_create_api_key_value_error.
        _service.disable_retries()
        self.test_create_api_key_value_error()


class TestGetApiKeysDetails:
    """
    Test Class for get_api_keys_details
    """

    @responses.activate
    def test_get_api_keys_details_all_params(self):
        """
        get_api_keys_details()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/details')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        iam_api_key = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_api_keys_details(
            iam_api_key=iam_api_key,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_get_api_keys_details_all_params_with_retries(self):
        # Enable retries and run test_get_api_keys_details_all_params.
        _service.enable_retries()
        self.test_get_api_keys_details_all_params()

        # Disable retries and run test_get_api_keys_details_all_params.
        _service.disable_retries()
        self.test_get_api_keys_details_all_params()

    @responses.activate
    def test_get_api_keys_details_required_params(self):
        """
        test_get_api_keys_details_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/details')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_api_keys_details()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_api_keys_details_required_params_with_retries(self):
        # Enable retries and run test_get_api_keys_details_required_params.
        _service.enable_retries()
        self.test_get_api_keys_details_required_params()

        # Disable retries and run test_get_api_keys_details_required_params.
        _service.disable_retries()
        self.test_get_api_keys_details_required_params()


class TestGetApiKey:
    """
    Test Class for get_api_key
    """

    @responses.activate
    def test_get_api_key_all_params(self):
        """
        get_api_key()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        include_history = False
        include_activity = False

        # Invoke method
        response = _service.get_api_key(
            id,
            include_history=include_history,
            include_activity=include_activity,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string
        assert 'include_activity={}'.format('true' if include_activity else 'false') in query_string

    def test_get_api_key_all_params_with_retries(self):
        # Enable retries and run test_get_api_key_all_params.
        _service.enable_retries()
        self.test_get_api_key_all_params()

        # Disable retries and run test_get_api_key_all_params.
        _service.disable_retries()
        self.test_get_api_key_all_params()

    @responses.activate
    def test_get_api_key_required_params(self):
        """
        test_get_api_key_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
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
        response = _service.get_api_key(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_api_key_required_params_with_retries(self):
        # Enable retries and run test_get_api_key_required_params.
        _service.enable_retries()
        self.test_get_api_key_required_params()

        # Disable retries and run test_get_api_key_required_params.
        _service.disable_retries()
        self.test_get_api_key_required_params()

    @responses.activate
    def test_get_api_key_value_error(self):
        """
        test_get_api_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
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
                _service.get_api_key(**req_copy)

    def test_get_api_key_value_error_with_retries(self):
        # Enable retries and run test_get_api_key_value_error.
        _service.enable_retries()
        self.test_get_api_key_value_error()

        # Disable retries and run test_get_api_key_value_error.
        _service.disable_retries()
        self.test_get_api_key_value_error()


class TestUpdateApiKey:
    """
    Test Class for update_api_key
    """

    @responses.activate
    def test_update_api_key_all_params(self):
        """
        update_api_key()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'
        support_sessions = True
        action_when_leaked = 'testString'

        # Invoke method
        response = _service.update_api_key(
            id,
            if_match,
            name=name,
            description=description,
            support_sessions=support_sessions,
            action_when_leaked=action_when_leaked,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['support_sessions'] == True
        assert req_body['action_when_leaked'] == 'testString'

    def test_update_api_key_all_params_with_retries(self):
        # Enable retries and run test_update_api_key_all_params.
        _service.enable_retries()
        self.test_update_api_key_all_params()

        # Disable retries and run test_update_api_key_all_params.
        _service.disable_retries()
        self.test_update_api_key_all_params()

    @responses.activate
    def test_update_api_key_value_error(self):
        """
        test_update_api_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'
        support_sessions = True
        action_when_leaked = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_api_key(**req_copy)

    def test_update_api_key_value_error_with_retries(self):
        # Enable retries and run test_update_api_key_value_error.
        _service.enable_retries()
        self.test_update_api_key_value_error()

        # Disable retries and run test_update_api_key_value_error.
        _service.disable_retries()
        self.test_update_api_key_value_error()


class TestDeleteApiKey:
    """
    Test Class for delete_api_key
    """

    @responses.activate
    def test_delete_api_key_all_params(self):
        """
        delete_api_key()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_api_key(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_api_key_all_params_with_retries(self):
        # Enable retries and run test_delete_api_key_all_params.
        _service.enable_retries()
        self.test_delete_api_key_all_params()

        # Disable retries and run test_delete_api_key_all_params.
        _service.disable_retries()
        self.test_delete_api_key_all_params()

    @responses.activate
    def test_delete_api_key_value_error(self):
        """
        test_delete_api_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString')
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
                _service.delete_api_key(**req_copy)

    def test_delete_api_key_value_error_with_retries(self):
        # Enable retries and run test_delete_api_key_value_error.
        _service.enable_retries()
        self.test_delete_api_key_value_error()

        # Disable retries and run test_delete_api_key_value_error.
        _service.disable_retries()
        self.test_delete_api_key_value_error()


class TestLockApiKey:
    """
    Test Class for lock_api_key
    """

    @responses.activate
    def test_lock_api_key_all_params(self):
        """
        lock_api_key()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString/lock')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.lock_api_key(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_lock_api_key_all_params_with_retries(self):
        # Enable retries and run test_lock_api_key_all_params.
        _service.enable_retries()
        self.test_lock_api_key_all_params()

        # Disable retries and run test_lock_api_key_all_params.
        _service.disable_retries()
        self.test_lock_api_key_all_params()

    @responses.activate
    def test_lock_api_key_value_error(self):
        """
        test_lock_api_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString/lock')
        responses.add(
            responses.POST,
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
                _service.lock_api_key(**req_copy)

    def test_lock_api_key_value_error_with_retries(self):
        # Enable retries and run test_lock_api_key_value_error.
        _service.enable_retries()
        self.test_lock_api_key_value_error()

        # Disable retries and run test_lock_api_key_value_error.
        _service.disable_retries()
        self.test_lock_api_key_value_error()


class TestUnlockApiKey:
    """
    Test Class for unlock_api_key
    """

    @responses.activate
    def test_unlock_api_key_all_params(self):
        """
        unlock_api_key()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString/lock')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.unlock_api_key(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_unlock_api_key_all_params_with_retries(self):
        # Enable retries and run test_unlock_api_key_all_params.
        _service.enable_retries()
        self.test_unlock_api_key_all_params()

        # Disable retries and run test_unlock_api_key_all_params.
        _service.disable_retries()
        self.test_unlock_api_key_all_params()

    @responses.activate
    def test_unlock_api_key_value_error(self):
        """
        test_unlock_api_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString/lock')
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
                _service.unlock_api_key(**req_copy)

    def test_unlock_api_key_value_error_with_retries(self):
        # Enable retries and run test_unlock_api_key_value_error.
        _service.enable_retries()
        self.test_unlock_api_key_value_error()

        # Disable retries and run test_unlock_api_key_value_error.
        _service.disable_retries()
        self.test_unlock_api_key_value_error()


class TestDisableApiKey:
    """
    Test Class for disable_api_key
    """

    @responses.activate
    def test_disable_api_key_all_params(self):
        """
        disable_api_key()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString/disable')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.disable_api_key(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_disable_api_key_all_params_with_retries(self):
        # Enable retries and run test_disable_api_key_all_params.
        _service.enable_retries()
        self.test_disable_api_key_all_params()

        # Disable retries and run test_disable_api_key_all_params.
        _service.disable_retries()
        self.test_disable_api_key_all_params()

    @responses.activate
    def test_disable_api_key_value_error(self):
        """
        test_disable_api_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString/disable')
        responses.add(
            responses.POST,
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
                _service.disable_api_key(**req_copy)

    def test_disable_api_key_value_error_with_retries(self):
        # Enable retries and run test_disable_api_key_value_error.
        _service.enable_retries()
        self.test_disable_api_key_value_error()

        # Disable retries and run test_disable_api_key_value_error.
        _service.disable_retries()
        self.test_disable_api_key_value_error()


class TestEnableApiKey:
    """
    Test Class for enable_api_key
    """

    @responses.activate
    def test_enable_api_key_all_params(self):
        """
        enable_api_key()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString/disable')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.enable_api_key(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_enable_api_key_all_params_with_retries(self):
        # Enable retries and run test_enable_api_key_all_params.
        _service.enable_retries()
        self.test_enable_api_key_all_params()

        # Disable retries and run test_enable_api_key_all_params.
        _service.disable_retries()
        self.test_enable_api_key_all_params()

    @responses.activate
    def test_enable_api_key_value_error(self):
        """
        test_enable_api_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/apikeys/testString/disable')
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
                _service.enable_api_key(**req_copy)

    def test_enable_api_key_value_error_with_retries(self):
        # Enable retries and run test_enable_api_key_value_error.
        _service.enable_retries()
        self.test_enable_api_key_value_error()

        # Disable retries and run test_enable_api_key_value_error.
        _service.disable_retries()
        self.test_enable_api_key_value_error()


# endregion
##############################################################################
# End of Service: APIKeyOperations
##############################################################################

##############################################################################
# Start of Service: ServiceIDOperations
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListServiceIds:
    """
    Test Class for list_service_ids
    """

    @responses.activate
    def test_list_service_ids_all_params(self):
        """
        list_service_ids()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "serviceids": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        pagesize = 38
        pagetoken = 'testString'
        sort = 'testString'
        order = 'asc'
        include_history = False

        # Invoke method
        response = _service.list_service_ids(
            account_id=account_id,
            name=name,
            pagesize=pagesize,
            pagetoken=pagetoken,
            sort=sort,
            order=order,
            include_history=include_history,
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
        assert 'pagesize={}'.format(pagesize) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_list_service_ids_all_params_with_retries(self):
        # Enable retries and run test_list_service_ids_all_params.
        _service.enable_retries()
        self.test_list_service_ids_all_params()

        # Disable retries and run test_list_service_ids_all_params.
        _service.disable_retries()
        self.test_list_service_ids_all_params()

    @responses.activate
    def test_list_service_ids_required_params(self):
        """
        test_list_service_ids_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "serviceids": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_service_ids()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_service_ids_required_params_with_retries(self):
        # Enable retries and run test_list_service_ids_required_params.
        _service.enable_retries()
        self.test_list_service_ids_required_params()

        # Disable retries and run test_list_service_ids_required_params.
        _service.disable_retries()
        self.test_list_service_ids_required_params()


class TestCreateServiceId:
    """
    Test Class for create_service_id
    """

    @responses.activate
    def test_create_service_id_all_params(self):
        """
        create_service_id()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ApiKeyInsideCreateServiceIdRequest model
        api_key_inside_create_service_id_request_model = {}
        api_key_inside_create_service_id_request_model['name'] = 'testString'
        api_key_inside_create_service_id_request_model['description'] = 'testString'
        api_key_inside_create_service_id_request_model['apikey'] = 'testString'
        api_key_inside_create_service_id_request_model['store_value'] = True

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        unique_instance_crns = ['testString']
        apikey = api_key_inside_create_service_id_request_model
        entity_lock = 'false'

        # Invoke method
        response = _service.create_service_id(
            account_id,
            name,
            description=description,
            unique_instance_crns=unique_instance_crns,
            apikey=apikey,
            entity_lock=entity_lock,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['unique_instance_crns'] == ['testString']
        assert req_body['apikey'] == api_key_inside_create_service_id_request_model

    def test_create_service_id_all_params_with_retries(self):
        # Enable retries and run test_create_service_id_all_params.
        _service.enable_retries()
        self.test_create_service_id_all_params()

        # Disable retries and run test_create_service_id_all_params.
        _service.disable_retries()
        self.test_create_service_id_all_params()

    @responses.activate
    def test_create_service_id_required_params(self):
        """
        test_create_service_id_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ApiKeyInsideCreateServiceIdRequest model
        api_key_inside_create_service_id_request_model = {}
        api_key_inside_create_service_id_request_model['name'] = 'testString'
        api_key_inside_create_service_id_request_model['description'] = 'testString'
        api_key_inside_create_service_id_request_model['apikey'] = 'testString'
        api_key_inside_create_service_id_request_model['store_value'] = True

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        unique_instance_crns = ['testString']
        apikey = api_key_inside_create_service_id_request_model

        # Invoke method
        response = _service.create_service_id(
            account_id,
            name,
            description=description,
            unique_instance_crns=unique_instance_crns,
            apikey=apikey,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['unique_instance_crns'] == ['testString']
        assert req_body['apikey'] == api_key_inside_create_service_id_request_model

    def test_create_service_id_required_params_with_retries(self):
        # Enable retries and run test_create_service_id_required_params.
        _service.enable_retries()
        self.test_create_service_id_required_params()

        # Disable retries and run test_create_service_id_required_params.
        _service.disable_retries()
        self.test_create_service_id_required_params()

    @responses.activate
    def test_create_service_id_value_error(self):
        """
        test_create_service_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ApiKeyInsideCreateServiceIdRequest model
        api_key_inside_create_service_id_request_model = {}
        api_key_inside_create_service_id_request_model['name'] = 'testString'
        api_key_inside_create_service_id_request_model['description'] = 'testString'
        api_key_inside_create_service_id_request_model['apikey'] = 'testString'
        api_key_inside_create_service_id_request_model['store_value'] = True

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        unique_instance_crns = ['testString']
        apikey = api_key_inside_create_service_id_request_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_service_id(**req_copy)

    def test_create_service_id_value_error_with_retries(self):
        # Enable retries and run test_create_service_id_value_error.
        _service.enable_retries()
        self.test_create_service_id_value_error()

        # Disable retries and run test_create_service_id_value_error.
        _service.disable_retries()
        self.test_create_service_id_value_error()


class TestGetServiceId:
    """
    Test Class for get_service_id
    """

    @responses.activate
    def test_get_service_id_all_params(self):
        """
        get_service_id()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        include_history = False
        include_activity = False

        # Invoke method
        response = _service.get_service_id(
            id,
            include_history=include_history,
            include_activity=include_activity,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string
        assert 'include_activity={}'.format('true' if include_activity else 'false') in query_string

    def test_get_service_id_all_params_with_retries(self):
        # Enable retries and run test_get_service_id_all_params.
        _service.enable_retries()
        self.test_get_service_id_all_params()

        # Disable retries and run test_get_service_id_all_params.
        _service.disable_retries()
        self.test_get_service_id_all_params()

    @responses.activate
    def test_get_service_id_required_params(self):
        """
        test_get_service_id_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}'
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
        response = _service.get_service_id(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_service_id_required_params_with_retries(self):
        # Enable retries and run test_get_service_id_required_params.
        _service.enable_retries()
        self.test_get_service_id_required_params()

        # Disable retries and run test_get_service_id_required_params.
        _service.disable_retries()
        self.test_get_service_id_required_params()

    @responses.activate
    def test_get_service_id_value_error(self):
        """
        test_get_service_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}'
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
                _service.get_service_id(**req_copy)

    def test_get_service_id_value_error_with_retries(self):
        # Enable retries and run test_get_service_id_value_error.
        _service.enable_retries()
        self.test_get_service_id_value_error()

        # Disable retries and run test_get_service_id_value_error.
        _service.disable_retries()
        self.test_get_service_id_value_error()


class TestUpdateServiceId:
    """
    Test Class for update_service_id
    """

    @responses.activate
    def test_update_service_id_all_params(self):
        """
        update_service_id()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'
        unique_instance_crns = ['testString']

        # Invoke method
        response = _service.update_service_id(
            id,
            if_match,
            name=name,
            description=description,
            unique_instance_crns=unique_instance_crns,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['unique_instance_crns'] == ['testString']

    def test_update_service_id_all_params_with_retries(self):
        # Enable retries and run test_update_service_id_all_params.
        _service.enable_retries()
        self.test_update_service_id_all_params()

        # Disable retries and run test_update_service_id_all_params.
        _service.disable_retries()
        self.test_update_service_id_all_params()

    @responses.activate
    def test_update_service_id_value_error(self):
        """
        test_update_service_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "disabled": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "support_sessions": true, "action_when_leaked": "action_when_leaked", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}, "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'
        unique_instance_crns = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_service_id(**req_copy)

    def test_update_service_id_value_error_with_retries(self):
        # Enable retries and run test_update_service_id_value_error.
        _service.enable_retries()
        self.test_update_service_id_value_error()

        # Disable retries and run test_update_service_id_value_error.
        _service.disable_retries()
        self.test_update_service_id_value_error()


class TestDeleteServiceId:
    """
    Test Class for delete_service_id
    """

    @responses.activate
    def test_delete_service_id_all_params(self):
        """
        delete_service_id()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_service_id(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_service_id_all_params_with_retries(self):
        # Enable retries and run test_delete_service_id_all_params.
        _service.enable_retries()
        self.test_delete_service_id_all_params()

        # Disable retries and run test_delete_service_id_all_params.
        _service.disable_retries()
        self.test_delete_service_id_all_params()

    @responses.activate
    def test_delete_service_id_value_error(self):
        """
        test_delete_service_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString')
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
                _service.delete_service_id(**req_copy)

    def test_delete_service_id_value_error_with_retries(self):
        # Enable retries and run test_delete_service_id_value_error.
        _service.enable_retries()
        self.test_delete_service_id_value_error()

        # Disable retries and run test_delete_service_id_value_error.
        _service.disable_retries()
        self.test_delete_service_id_value_error()


class TestLockServiceId:
    """
    Test Class for lock_service_id
    """

    @responses.activate
    def test_lock_service_id_all_params(self):
        """
        lock_service_id()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString/lock')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.lock_service_id(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_lock_service_id_all_params_with_retries(self):
        # Enable retries and run test_lock_service_id_all_params.
        _service.enable_retries()
        self.test_lock_service_id_all_params()

        # Disable retries and run test_lock_service_id_all_params.
        _service.disable_retries()
        self.test_lock_service_id_all_params()

    @responses.activate
    def test_lock_service_id_value_error(self):
        """
        test_lock_service_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString/lock')
        responses.add(
            responses.POST,
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
                _service.lock_service_id(**req_copy)

    def test_lock_service_id_value_error_with_retries(self):
        # Enable retries and run test_lock_service_id_value_error.
        _service.enable_retries()
        self.test_lock_service_id_value_error()

        # Disable retries and run test_lock_service_id_value_error.
        _service.disable_retries()
        self.test_lock_service_id_value_error()


class TestUnlockServiceId:
    """
    Test Class for unlock_service_id
    """

    @responses.activate
    def test_unlock_service_id_all_params(self):
        """
        unlock_service_id()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString/lock')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.unlock_service_id(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_unlock_service_id_all_params_with_retries(self):
        # Enable retries and run test_unlock_service_id_all_params.
        _service.enable_retries()
        self.test_unlock_service_id_all_params()

        # Disable retries and run test_unlock_service_id_all_params.
        _service.disable_retries()
        self.test_unlock_service_id_all_params()

    @responses.activate
    def test_unlock_service_id_value_error(self):
        """
        test_unlock_service_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/serviceids/testString/lock')
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
                _service.unlock_service_id(**req_copy)

    def test_unlock_service_id_value_error_with_retries(self):
        # Enable retries and run test_unlock_service_id_value_error.
        _service.enable_retries()
        self.test_unlock_service_id_value_error()

        # Disable retries and run test_unlock_service_id_value_error.
        _service.disable_retries()
        self.test_unlock_service_id_value_error()


# endregion
##############################################################################
# End of Service: ServiceIDOperations
##############################################################################

##############################################################################
# Start of Service: TrustedProfilesOperations
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateProfile:
    """
    Test Class for create_profile
    """

    @responses.activate
    def test_create_profile_all_params(self):
        """
        create_profile()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.create_profile(
            name,
            account_id,
            description=description,
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

    def test_create_profile_all_params_with_retries(self):
        # Enable retries and run test_create_profile_all_params.
        _service.enable_retries()
        self.test_create_profile_all_params()

        # Disable retries and run test_create_profile_all_params.
        _service.disable_retries()
        self.test_create_profile_all_params()

    @responses.activate
    def test_create_profile_value_error(self):
        """
        test_create_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_profile(**req_copy)

    def test_create_profile_value_error_with_retries(self):
        # Enable retries and run test_create_profile_value_error.
        _service.enable_retries()
        self.test_create_profile_value_error()

        # Disable retries and run test_create_profile_value_error.
        _service.disable_retries()
        self.test_create_profile_value_error()


class TestListProfiles:
    """
    Test Class for list_profiles
    """

    @responses.activate
    def test_list_profiles_all_params(self):
        """
        list_profiles()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "profiles": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        pagesize = 38
        sort = 'testString'
        order = 'asc'
        include_history = False
        pagetoken = 'testString'

        # Invoke method
        response = _service.list_profiles(
            account_id,
            name=name,
            pagesize=pagesize,
            sort=sort,
            order=order,
            include_history=include_history,
            pagetoken=pagetoken,
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
        assert 'pagesize={}'.format(pagesize) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string

    def test_list_profiles_all_params_with_retries(self):
        # Enable retries and run test_list_profiles_all_params.
        _service.enable_retries()
        self.test_list_profiles_all_params()

        # Disable retries and run test_list_profiles_all_params.
        _service.disable_retries()
        self.test_list_profiles_all_params()

    @responses.activate
    def test_list_profiles_required_params(self):
        """
        test_list_profiles_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "profiles": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}]}'
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
        response = _service.list_profiles(
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

    def test_list_profiles_required_params_with_retries(self):
        # Enable retries and run test_list_profiles_required_params.
        _service.enable_retries()
        self.test_list_profiles_required_params()

        # Disable retries and run test_list_profiles_required_params.
        _service.disable_retries()
        self.test_list_profiles_required_params()

    @responses.activate
    def test_list_profiles_value_error(self):
        """
        test_list_profiles_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "profiles": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}]}'
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
                _service.list_profiles(**req_copy)

    def test_list_profiles_value_error_with_retries(self):
        # Enable retries and run test_list_profiles_value_error.
        _service.enable_retries()
        self.test_list_profiles_value_error()

        # Disable retries and run test_list_profiles_value_error.
        _service.disable_retries()
        self.test_list_profiles_value_error()


class TestGetProfile:
    """
    Test Class for get_profile
    """

    @responses.activate
    def test_get_profile_all_params(self):
        """
        get_profile()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        include_activity = False

        # Invoke method
        response = _service.get_profile(
            profile_id,
            include_activity=include_activity,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_activity={}'.format('true' if include_activity else 'false') in query_string

    def test_get_profile_all_params_with_retries(self):
        # Enable retries and run test_get_profile_all_params.
        _service.enable_retries()
        self.test_get_profile_all_params()

        # Disable retries and run test_get_profile_all_params.
        _service.disable_retries()
        self.test_get_profile_all_params()

    @responses.activate
    def test_get_profile_required_params(self):
        """
        test_get_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Invoke method
        response = _service.get_profile(
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_required_params_with_retries(self):
        # Enable retries and run test_get_profile_required_params.
        _service.enable_retries()
        self.test_get_profile_required_params()

        # Disable retries and run test_get_profile_required_params.
        _service.disable_retries()
        self.test_get_profile_required_params()

    @responses.activate
    def test_get_profile_value_error(self):
        """
        test_get_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_profile(**req_copy)

    def test_get_profile_value_error_with_retries(self):
        # Enable retries and run test_get_profile_value_error.
        _service.enable_retries()
        self.test_get_profile_value_error()

        # Disable retries and run test_get_profile_value_error.
        _service.disable_retries()
        self.test_get_profile_value_error()


class TestUpdateProfile:
    """
    Test Class for update_profile
    """

    @responses.activate
    def test_update_profile_all_params(self):
        """
        update_profile()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.update_profile(
            profile_id,
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
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'

    def test_update_profile_all_params_with_retries(self):
        # Enable retries and run test_update_profile_all_params.
        _service.enable_retries()
        self.test_update_profile_all_params()

        # Disable retries and run test_update_profile_all_params.
        _service.disable_retries()
        self.test_update_profile_all_params()

    @responses.activate
    def test_update_profile_value_error(self):
        """
        test_update_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "template_id": "template_id", "assignment_id": "assignment_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "activity": {"last_authn": "last_authn", "authn_count": 11}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_profile(**req_copy)

    def test_update_profile_value_error_with_retries(self):
        # Enable retries and run test_update_profile_value_error.
        _service.enable_retries()
        self.test_update_profile_value_error()

        # Disable retries and run test_update_profile_value_error.
        _service.disable_retries()
        self.test_update_profile_value_error()


class TestDeleteProfile:
    """
    Test Class for delete_profile
    """

    @responses.activate
    def test_delete_profile_all_params(self):
        """
        delete_profile()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Invoke method
        response = _service.delete_profile(
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_profile_all_params_with_retries(self):
        # Enable retries and run test_delete_profile_all_params.
        _service.enable_retries()
        self.test_delete_profile_all_params()

        # Disable retries and run test_delete_profile_all_params.
        _service.disable_retries()
        self.test_delete_profile_all_params()

    @responses.activate
    def test_delete_profile_value_error(self):
        """
        test_delete_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_profile(**req_copy)

    def test_delete_profile_value_error_with_retries(self):
        # Enable retries and run test_delete_profile_value_error.
        _service.enable_retries()
        self.test_delete_profile_value_error()

        # Disable retries and run test_delete_profile_value_error.
        _service.disable_retries()
        self.test_delete_profile_value_error()


class TestCreateClaimRule:
    """
    Test Class for create_claim_rule
    """

    @responses.activate
    def test_create_claim_rule_all_params(self):
        """
        create_claim_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a dict representation of a ResponseContext model
        response_context_model = {}
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        # Set up parameter values
        profile_id = 'testString'
        type = 'testString'
        conditions = [profile_claim_rule_conditions_model]
        context = response_context_model
        name = 'testString'
        realm_name = 'testString'
        cr_type = 'testString'
        expiration = 38

        # Invoke method
        response = _service.create_claim_rule(
            profile_id,
            type,
            conditions,
            context=context,
            name=name,
            realm_name=realm_name,
            cr_type=cr_type,
            expiration=expiration,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'testString'
        assert req_body['conditions'] == [profile_claim_rule_conditions_model]
        assert req_body['context'] == response_context_model
        assert req_body['name'] == 'testString'
        assert req_body['realm_name'] == 'testString'
        assert req_body['cr_type'] == 'testString'
        assert req_body['expiration'] == 38

    def test_create_claim_rule_all_params_with_retries(self):
        # Enable retries and run test_create_claim_rule_all_params.
        _service.enable_retries()
        self.test_create_claim_rule_all_params()

        # Disable retries and run test_create_claim_rule_all_params.
        _service.disable_retries()
        self.test_create_claim_rule_all_params()

    @responses.activate
    def test_create_claim_rule_value_error(self):
        """
        test_create_claim_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a dict representation of a ResponseContext model
        response_context_model = {}
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        # Set up parameter values
        profile_id = 'testString'
        type = 'testString'
        conditions = [profile_claim_rule_conditions_model]
        context = response_context_model
        name = 'testString'
        realm_name = 'testString'
        cr_type = 'testString'
        expiration = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "type": type,
            "conditions": conditions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_claim_rule(**req_copy)

    def test_create_claim_rule_value_error_with_retries(self):
        # Enable retries and run test_create_claim_rule_value_error.
        _service.enable_retries()
        self.test_create_claim_rule_value_error()

        # Disable retries and run test_create_claim_rule_value_error.
        _service.disable_retries()
        self.test_create_claim_rule_value_error()


class TestListClaimRules:
    """
    Test Class for list_claim_rules
    """

    @responses.activate
    def test_list_claim_rules_all_params(self):
        """
        list_claim_rules()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "rules": [{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Invoke method
        response = _service.list_claim_rules(
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_claim_rules_all_params_with_retries(self):
        # Enable retries and run test_list_claim_rules_all_params.
        _service.enable_retries()
        self.test_list_claim_rules_all_params()

        # Disable retries and run test_list_claim_rules_all_params.
        _service.disable_retries()
        self.test_list_claim_rules_all_params()

    @responses.activate
    def test_list_claim_rules_value_error(self):
        """
        test_list_claim_rules_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "rules": [{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_claim_rules(**req_copy)

    def test_list_claim_rules_value_error_with_retries(self):
        # Enable retries and run test_list_claim_rules_value_error.
        _service.enable_retries()
        self.test_list_claim_rules_value_error()

        # Disable retries and run test_list_claim_rules_value_error.
        _service.disable_retries()
        self.test_list_claim_rules_value_error()


class TestGetClaimRule:
    """
    Test Class for get_claim_rule
    """

    @responses.activate
    def test_get_claim_rule_all_params(self):
        """
        get_claim_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.get_claim_rule(
            profile_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_claim_rule_all_params_with_retries(self):
        # Enable retries and run test_get_claim_rule_all_params.
        _service.enable_retries()
        self.test_get_claim_rule_all_params()

        # Disable retries and run test_get_claim_rule_all_params.
        _service.disable_retries()
        self.test_get_claim_rule_all_params()

    @responses.activate
    def test_get_claim_rule_value_error(self):
        """
        test_get_claim_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_claim_rule(**req_copy)

    def test_get_claim_rule_value_error_with_retries(self):
        # Enable retries and run test_get_claim_rule_value_error.
        _service.enable_retries()
        self.test_get_claim_rule_value_error()

        # Disable retries and run test_get_claim_rule_value_error.
        _service.disable_retries()
        self.test_get_claim_rule_value_error()


class TestUpdateClaimRule:
    """
    Test Class for update_claim_rule
    """

    @responses.activate
    def test_update_claim_rule_all_params(self):
        """
        update_claim_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a dict representation of a ResponseContext model
        response_context_model = {}
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        conditions = [profile_claim_rule_conditions_model]
        context = response_context_model
        name = 'testString'
        realm_name = 'testString'
        cr_type = 'testString'
        expiration = 38

        # Invoke method
        response = _service.update_claim_rule(
            profile_id,
            rule_id,
            if_match,
            type,
            conditions,
            context=context,
            name=name,
            realm_name=realm_name,
            cr_type=cr_type,
            expiration=expiration,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'testString'
        assert req_body['conditions'] == [profile_claim_rule_conditions_model]
        assert req_body['context'] == response_context_model
        assert req_body['name'] == 'testString'
        assert req_body['realm_name'] == 'testString'
        assert req_body['cr_type'] == 'testString'
        assert req_body['expiration'] == 38

    def test_update_claim_rule_all_params_with_retries(self):
        # Enable retries and run test_update_claim_rule_all_params.
        _service.enable_retries()
        self.test_update_claim_rule_all_params()

        # Disable retries and run test_update_claim_rule_all_params.
        _service.disable_retries()
        self.test_update_claim_rule_all_params()

    @responses.activate
    def test_update_claim_rule_value_error(self):
        """
        test_update_claim_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a dict representation of a ResponseContext model
        response_context_model = {}
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'
        if_match = 'testString'
        type = 'testString'
        conditions = [profile_claim_rule_conditions_model]
        context = response_context_model
        name = 'testString'
        realm_name = 'testString'
        cr_type = 'testString'
        expiration = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "rule_id": rule_id,
            "if_match": if_match,
            "type": type,
            "conditions": conditions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_claim_rule(**req_copy)

    def test_update_claim_rule_value_error_with_retries(self):
        # Enable retries and run test_update_claim_rule_value_error.
        _service.enable_retries()
        self.test_update_claim_rule_value_error()

        # Disable retries and run test_update_claim_rule_value_error.
        _service.disable_retries()
        self.test_update_claim_rule_value_error()


class TestDeleteClaimRule:
    """
    Test Class for delete_claim_rule
    """

    @responses.activate
    def test_delete_claim_rule_all_params(self):
        """
        delete_claim_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.delete_claim_rule(
            profile_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_claim_rule_all_params_with_retries(self):
        # Enable retries and run test_delete_claim_rule_all_params.
        _service.enable_retries()
        self.test_delete_claim_rule_all_params()

        # Disable retries and run test_delete_claim_rule_all_params.
        _service.disable_retries()
        self.test_delete_claim_rule_all_params()

    @responses.activate
    def test_delete_claim_rule_value_error(self):
        """
        test_delete_claim_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_claim_rule(**req_copy)

    def test_delete_claim_rule_value_error_with_retries(self):
        # Enable retries and run test_delete_claim_rule_value_error.
        _service.enable_retries()
        self.test_delete_claim_rule_value_error()

        # Disable retries and run test_delete_claim_rule_value_error.
        _service.disable_retries()
        self.test_delete_claim_rule_value_error()


class TestCreateLink:
    """
    Test Class for create_link
    """

    @responses.activate
    def test_create_link_all_params(self):
        """
        create_link()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/links')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a CreateProfileLinkRequestLink model
        create_profile_link_request_link_model = {}
        create_profile_link_request_link_model['crn'] = 'testString'
        create_profile_link_request_link_model['namespace'] = 'testString'
        create_profile_link_request_link_model['name'] = 'testString'

        # Set up parameter values
        profile_id = 'testString'
        cr_type = 'testString'
        link = create_profile_link_request_link_model
        name = 'testString'

        # Invoke method
        response = _service.create_link(
            profile_id,
            cr_type,
            link,
            name=name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cr_type'] == 'testString'
        assert req_body['link'] == create_profile_link_request_link_model
        assert req_body['name'] == 'testString'

    def test_create_link_all_params_with_retries(self):
        # Enable retries and run test_create_link_all_params.
        _service.enable_retries()
        self.test_create_link_all_params()

        # Disable retries and run test_create_link_all_params.
        _service.disable_retries()
        self.test_create_link_all_params()

    @responses.activate
    def test_create_link_value_error(self):
        """
        test_create_link_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/links')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a CreateProfileLinkRequestLink model
        create_profile_link_request_link_model = {}
        create_profile_link_request_link_model['crn'] = 'testString'
        create_profile_link_request_link_model['namespace'] = 'testString'
        create_profile_link_request_link_model['name'] = 'testString'

        # Set up parameter values
        profile_id = 'testString'
        cr_type = 'testString'
        link = create_profile_link_request_link_model
        name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "cr_type": cr_type,
            "link": link,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_link(**req_copy)

    def test_create_link_value_error_with_retries(self):
        # Enable retries and run test_create_link_value_error.
        _service.enable_retries()
        self.test_create_link_value_error()

        # Disable retries and run test_create_link_value_error.
        _service.disable_retries()
        self.test_create_link_value_error()


class TestListLinks:
    """
    Test Class for list_links
    """

    @responses.activate
    def test_list_links_all_params(self):
        """
        list_links()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/links')
        mock_response = '{"links": [{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Invoke method
        response = _service.list_links(
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_links_all_params_with_retries(self):
        # Enable retries and run test_list_links_all_params.
        _service.enable_retries()
        self.test_list_links_all_params()

        # Disable retries and run test_list_links_all_params.
        _service.disable_retries()
        self.test_list_links_all_params()

    @responses.activate
    def test_list_links_value_error(self):
        """
        test_list_links_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/links')
        mock_response = '{"links": [{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_links(**req_copy)

    def test_list_links_value_error_with_retries(self):
        # Enable retries and run test_list_links_value_error.
        _service.enable_retries()
        self.test_list_links_value_error()

        # Disable retries and run test_list_links_value_error.
        _service.disable_retries()
        self.test_list_links_value_error()


class TestGetLink:
    """
    Test Class for get_link
    """

    @responses.activate
    def test_get_link_all_params(self):
        """
        get_link()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/links/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        link_id = 'testString'

        # Invoke method
        response = _service.get_link(
            profile_id,
            link_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_link_all_params_with_retries(self):
        # Enable retries and run test_get_link_all_params.
        _service.enable_retries()
        self.test_get_link_all_params()

        # Disable retries and run test_get_link_all_params.
        _service.disable_retries()
        self.test_get_link_all_params()

    @responses.activate
    def test_get_link_value_error(self):
        """
        test_get_link_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/links/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        link_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "link_id": link_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_link(**req_copy)

    def test_get_link_value_error_with_retries(self):
        # Enable retries and run test_get_link_value_error.
        _service.enable_retries()
        self.test_get_link_value_error()

        # Disable retries and run test_get_link_value_error.
        _service.disable_retries()
        self.test_get_link_value_error()


class TestDeleteLink:
    """
    Test Class for delete_link
    """

    @responses.activate
    def test_delete_link_all_params(self):
        """
        delete_link()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/links/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        profile_id = 'testString'
        link_id = 'testString'

        # Invoke method
        response = _service.delete_link(
            profile_id,
            link_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_link_all_params_with_retries(self):
        # Enable retries and run test_delete_link_all_params.
        _service.enable_retries()
        self.test_delete_link_all_params()

        # Disable retries and run test_delete_link_all_params.
        _service.disable_retries()
        self.test_delete_link_all_params()

    @responses.activate
    def test_delete_link_value_error(self):
        """
        test_delete_link_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/links/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        profile_id = 'testString'
        link_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "link_id": link_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_link(**req_copy)

    def test_delete_link_value_error_with_retries(self):
        # Enable retries and run test_delete_link_value_error.
        _service.enable_retries()
        self.test_delete_link_value_error()

        # Disable retries and run test_delete_link_value_error.
        _service.disable_retries()
        self.test_delete_link_value_error()


class TestGetProfileIdentities:
    """
    Test Class for get_profile_identities
    """

    @responses.activate
    def test_get_profile_identities_all_params(self):
        """
        get_profile_identities()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities')
        mock_response = '{"entity_tag": "entity_tag", "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Invoke method
        response = _service.get_profile_identities(
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_identities_all_params_with_retries(self):
        # Enable retries and run test_get_profile_identities_all_params.
        _service.enable_retries()
        self.test_get_profile_identities_all_params()

        # Disable retries and run test_get_profile_identities_all_params.
        _service.disable_retries()
        self.test_get_profile_identities_all_params()

    @responses.activate
    def test_get_profile_identities_value_error(self):
        """
        test_get_profile_identities_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities')
        mock_response = '{"entity_tag": "entity_tag", "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_profile_identities(**req_copy)

    def test_get_profile_identities_value_error_with_retries(self):
        # Enable retries and run test_get_profile_identities_value_error.
        _service.enable_retries()
        self.test_get_profile_identities_value_error()

        # Disable retries and run test_get_profile_identities_value_error.
        _service.disable_retries()
        self.test_get_profile_identities_value_error()


class TestSetProfileIdentities:
    """
    Test Class for set_profile_identities
    """

    @responses.activate
    def test_set_profile_identities_all_params(self):
        """
        set_profile_identities()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities')
        mock_response = '{"entity_tag": "entity_tag", "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileIdentityRequest model
        profile_identity_request_model = {}
        profile_identity_request_model['identifier'] = 'testString'
        profile_identity_request_model['type'] = 'user'
        profile_identity_request_model['accounts'] = ['testString']
        profile_identity_request_model['description'] = 'testString'

        # Set up parameter values
        profile_id = 'testString'
        if_match = 'testString'
        identities = [profile_identity_request_model]

        # Invoke method
        response = _service.set_profile_identities(
            profile_id,
            if_match,
            identities=identities,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['identities'] == [profile_identity_request_model]

    def test_set_profile_identities_all_params_with_retries(self):
        # Enable retries and run test_set_profile_identities_all_params.
        _service.enable_retries()
        self.test_set_profile_identities_all_params()

        # Disable retries and run test_set_profile_identities_all_params.
        _service.disable_retries()
        self.test_set_profile_identities_all_params()

    @responses.activate
    def test_set_profile_identities_value_error(self):
        """
        test_set_profile_identities_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities')
        mock_response = '{"entity_tag": "entity_tag", "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileIdentityRequest model
        profile_identity_request_model = {}
        profile_identity_request_model['identifier'] = 'testString'
        profile_identity_request_model['type'] = 'user'
        profile_identity_request_model['accounts'] = ['testString']
        profile_identity_request_model['description'] = 'testString'

        # Set up parameter values
        profile_id = 'testString'
        if_match = 'testString'
        identities = [profile_identity_request_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.set_profile_identities(**req_copy)

    def test_set_profile_identities_value_error_with_retries(self):
        # Enable retries and run test_set_profile_identities_value_error.
        _service.enable_retries()
        self.test_set_profile_identities_value_error()

        # Disable retries and run test_set_profile_identities_value_error.
        _service.disable_retries()
        self.test_set_profile_identities_value_error()


class TestSetProfileIdentity:
    """
    Test Class for set_profile_identity
    """

    @responses.activate
    def test_set_profile_identity_all_params(self):
        """
        set_profile_identity()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities/user')
        mock_response = '{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        identity_type = 'user'
        identifier = 'testString'
        type = 'user'
        accounts = ['testString']
        description = 'testString'

        # Invoke method
        response = _service.set_profile_identity(
            profile_id,
            identity_type,
            identifier,
            type,
            accounts=accounts,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['identifier'] == 'testString'
        assert req_body['type'] == 'user'
        assert req_body['accounts'] == ['testString']
        assert req_body['description'] == 'testString'

    def test_set_profile_identity_all_params_with_retries(self):
        # Enable retries and run test_set_profile_identity_all_params.
        _service.enable_retries()
        self.test_set_profile_identity_all_params()

        # Disable retries and run test_set_profile_identity_all_params.
        _service.disable_retries()
        self.test_set_profile_identity_all_params()

    @responses.activate
    def test_set_profile_identity_value_error(self):
        """
        test_set_profile_identity_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities/user')
        mock_response = '{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        identity_type = 'user'
        identifier = 'testString'
        type = 'user'
        accounts = ['testString']
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "identity_type": identity_type,
            "identifier": identifier,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.set_profile_identity(**req_copy)

    def test_set_profile_identity_value_error_with_retries(self):
        # Enable retries and run test_set_profile_identity_value_error.
        _service.enable_retries()
        self.test_set_profile_identity_value_error()

        # Disable retries and run test_set_profile_identity_value_error.
        _service.disable_retries()
        self.test_set_profile_identity_value_error()


class TestGetProfileIdentity:
    """
    Test Class for get_profile_identity
    """

    @responses.activate
    def test_get_profile_identity_all_params(self):
        """
        get_profile_identity()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities/user/testString')
        mock_response = '{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        identity_type = 'user'
        identifier_id = 'testString'

        # Invoke method
        response = _service.get_profile_identity(
            profile_id,
            identity_type,
            identifier_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_identity_all_params_with_retries(self):
        # Enable retries and run test_get_profile_identity_all_params.
        _service.enable_retries()
        self.test_get_profile_identity_all_params()

        # Disable retries and run test_get_profile_identity_all_params.
        _service.disable_retries()
        self.test_get_profile_identity_all_params()

    @responses.activate
    def test_get_profile_identity_value_error(self):
        """
        test_get_profile_identity_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities/user/testString')
        mock_response = '{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profile_id = 'testString'
        identity_type = 'user'
        identifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "identity_type": identity_type,
            "identifier_id": identifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_profile_identity(**req_copy)

    def test_get_profile_identity_value_error_with_retries(self):
        # Enable retries and run test_get_profile_identity_value_error.
        _service.enable_retries()
        self.test_get_profile_identity_value_error()

        # Disable retries and run test_get_profile_identity_value_error.
        _service.disable_retries()
        self.test_get_profile_identity_value_error()


class TestDeleteProfileIdentity:
    """
    Test Class for delete_profile_identity
    """

    @responses.activate
    def test_delete_profile_identity_all_params(self):
        """
        delete_profile_identity()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities/user/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        profile_id = 'testString'
        identity_type = 'user'
        identifier_id = 'testString'

        # Invoke method
        response = _service.delete_profile_identity(
            profile_id,
            identity_type,
            identifier_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_profile_identity_all_params_with_retries(self):
        # Enable retries and run test_delete_profile_identity_all_params.
        _service.enable_retries()
        self.test_delete_profile_identity_all_params()

        # Disable retries and run test_delete_profile_identity_all_params.
        _service.disable_retries()
        self.test_delete_profile_identity_all_params()

    @responses.activate
    def test_delete_profile_identity_value_error(self):
        """
        test_delete_profile_identity_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profiles/testString/identities/user/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        profile_id = 'testString'
        identity_type = 'user'
        identifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "identity_type": identity_type,
            "identifier_id": identifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_profile_identity(**req_copy)

    def test_delete_profile_identity_value_error_with_retries(self):
        # Enable retries and run test_delete_profile_identity_value_error.
        _service.enable_retries()
        self.test_delete_profile_identity_value_error()

        # Disable retries and run test_delete_profile_identity_value_error.
        _service.disable_retries()
        self.test_delete_profile_identity_value_error()


# endregion
##############################################################################
# End of Service: TrustedProfilesOperations
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
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
        url = preprocess_url('/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_account_settings(
            account_id,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

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
        url = preprocess_url('/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}'
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
        url = preprocess_url('/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}'
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
        url = preprocess_url('/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AccountSettingsUserMFA model
        account_settings_user_mfa_model = {}
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        # Set up parameter values
        if_match = 'testString'
        account_id = 'testString'
        restrict_create_service_id = 'RESTRICTED'
        restrict_create_platform_apikey = 'RESTRICTED'
        allowed_ip_addresses = 'testString'
        mfa = 'NONE'
        user_mfa = [account_settings_user_mfa_model]
        session_expiration_in_seconds = '86400'
        session_invalidation_in_seconds = '7200'
        max_sessions_per_identity = 'testString'
        system_access_token_expiration_in_seconds = '3600'
        system_refresh_token_expiration_in_seconds = '259200'

        # Invoke method
        response = _service.update_account_settings(
            if_match,
            account_id,
            restrict_create_service_id=restrict_create_service_id,
            restrict_create_platform_apikey=restrict_create_platform_apikey,
            allowed_ip_addresses=allowed_ip_addresses,
            mfa=mfa,
            user_mfa=user_mfa,
            session_expiration_in_seconds=session_expiration_in_seconds,
            session_invalidation_in_seconds=session_invalidation_in_seconds,
            max_sessions_per_identity=max_sessions_per_identity,
            system_access_token_expiration_in_seconds=system_access_token_expiration_in_seconds,
            system_refresh_token_expiration_in_seconds=system_refresh_token_expiration_in_seconds,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['restrict_create_service_id'] == 'RESTRICTED'
        assert req_body['restrict_create_platform_apikey'] == 'RESTRICTED'
        assert req_body['allowed_ip_addresses'] == 'testString'
        assert req_body['mfa'] == 'NONE'
        assert req_body['user_mfa'] == [account_settings_user_mfa_model]
        assert req_body['session_expiration_in_seconds'] == '86400'
        assert req_body['session_invalidation_in_seconds'] == '7200'
        assert req_body['max_sessions_per_identity'] == 'testString'
        assert req_body['system_access_token_expiration_in_seconds'] == '3600'
        assert req_body['system_refresh_token_expiration_in_seconds'] == '259200'

    def test_update_account_settings_all_params_with_retries(self):
        # Enable retries and run test_update_account_settings_all_params.
        _service.enable_retries()
        self.test_update_account_settings_all_params()

        # Disable retries and run test_update_account_settings_all_params.
        _service.disable_retries()
        self.test_update_account_settings_all_params()

    @responses.activate
    def test_update_account_settings_value_error(self):
        """
        test_update_account_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AccountSettingsUserMFA model
        account_settings_user_mfa_model = {}
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        # Set up parameter values
        if_match = 'testString'
        account_id = 'testString'
        restrict_create_service_id = 'RESTRICTED'
        restrict_create_platform_apikey = 'RESTRICTED'
        allowed_ip_addresses = 'testString'
        mfa = 'NONE'
        user_mfa = [account_settings_user_mfa_model]
        session_expiration_in_seconds = '86400'
        session_invalidation_in_seconds = '7200'
        max_sessions_per_identity = 'testString'
        system_access_token_expiration_in_seconds = '3600'
        system_refresh_token_expiration_in_seconds = '259200'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "if_match": if_match,
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
# Start of Service: MFAEnrollmentStatus
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetMfaStatus:
    """
    Test Class for get_mfa_status
    """

    @responses.activate
    def test_get_mfa_status_all_params(self):
        """
        get_mfa_status()
        """
        # Set up mock
        url = preprocess_url('/v1/mfa/accounts/testString/status')
        mock_response = '{"iam_id": "iam_id", "effective_mfa_type": "effective_mfa_type", "id_based_mfa": {"trait_account_default": "NONE", "trait_user_specific": "NONE", "trait_effective": "NONE", "complies": true, "comply_state": "NO"}, "account_based_mfa": {"security_questions": {"required": true, "enrolled": true}, "totp": {"required": true, "enrolled": true}, "verisign": {"required": true, "enrolled": true}, "complies": true}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.get_mfa_status(
            account_id,
            iam_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'iam_id={}'.format(iam_id) in query_string

    def test_get_mfa_status_all_params_with_retries(self):
        # Enable retries and run test_get_mfa_status_all_params.
        _service.enable_retries()
        self.test_get_mfa_status_all_params()

        # Disable retries and run test_get_mfa_status_all_params.
        _service.disable_retries()
        self.test_get_mfa_status_all_params()

    @responses.activate
    def test_get_mfa_status_value_error(self):
        """
        test_get_mfa_status_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/mfa/accounts/testString/status')
        mock_response = '{"iam_id": "iam_id", "effective_mfa_type": "effective_mfa_type", "id_based_mfa": {"trait_account_default": "NONE", "trait_user_specific": "NONE", "trait_effective": "NONE", "complies": true, "comply_state": "NO"}, "account_based_mfa": {"security_questions": {"required": true, "enrolled": true}, "totp": {"required": true, "enrolled": true}, "verisign": {"required": true, "enrolled": true}, "complies": true}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
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
                _service.get_mfa_status(**req_copy)

    def test_get_mfa_status_value_error_with_retries(self):
        # Enable retries and run test_get_mfa_status_value_error.
        _service.enable_retries()
        self.test_get_mfa_status_value_error()

        # Disable retries and run test_get_mfa_status_value_error.
        _service.disable_retries()
        self.test_get_mfa_status_value_error()


class TestCreateMfaReport:
    """
    Test Class for create_mfa_report
    """

    @responses.activate
    def test_create_mfa_report_all_params(self):
        """
        create_mfa_report()
        """
        # Set up mock
        url = preprocess_url('/v1/mfa/accounts/testString/report')
        mock_response = '{"reference": "reference"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        account_id = 'testString'
        type = 'testString'

        # Invoke method
        response = _service.create_mfa_report(
            account_id,
            type=type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string

    def test_create_mfa_report_all_params_with_retries(self):
        # Enable retries and run test_create_mfa_report_all_params.
        _service.enable_retries()
        self.test_create_mfa_report_all_params()

        # Disable retries and run test_create_mfa_report_all_params.
        _service.disable_retries()
        self.test_create_mfa_report_all_params()

    @responses.activate
    def test_create_mfa_report_required_params(self):
        """
        test_create_mfa_report_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/mfa/accounts/testString/report')
        mock_response = '{"reference": "reference"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.create_mfa_report(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_create_mfa_report_required_params_with_retries(self):
        # Enable retries and run test_create_mfa_report_required_params.
        _service.enable_retries()
        self.test_create_mfa_report_required_params()

        # Disable retries and run test_create_mfa_report_required_params.
        _service.disable_retries()
        self.test_create_mfa_report_required_params()

    @responses.activate
    def test_create_mfa_report_value_error(self):
        """
        test_create_mfa_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/mfa/accounts/testString/report')
        mock_response = '{"reference": "reference"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
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
                _service.create_mfa_report(**req_copy)

    def test_create_mfa_report_value_error_with_retries(self):
        # Enable retries and run test_create_mfa_report_value_error.
        _service.enable_retries()
        self.test_create_mfa_report_value_error()

        # Disable retries and run test_create_mfa_report_value_error.
        _service.disable_retries()
        self.test_create_mfa_report_value_error()


class TestGetMfaReport:
    """
    Test Class for get_mfa_report
    """

    @responses.activate
    def test_get_mfa_report_all_params(self):
        """
        get_mfa_report()
        """
        # Set up mock
        url = preprocess_url('/v1/mfa/accounts/testString/report/testString')
        mock_response = '{"created_by": "created_by", "reference": "reference", "report_time": "report_time", "account_id": "account_id", "ims_account_id": "ims_account_id", "users": [{"iam_id": "iam_id", "name": "name", "username": "username", "email": "email", "enrollments": {"effective_mfa_type": "effective_mfa_type", "id_based_mfa": {"trait_account_default": "NONE", "trait_user_specific": "NONE", "trait_effective": "NONE", "complies": true, "comply_state": "NO"}, "account_based_mfa": {"security_questions": {"required": true, "enrolled": true}, "totp": {"required": true, "enrolled": true}, "verisign": {"required": true, "enrolled": true}, "complies": true}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        reference = 'testString'

        # Invoke method
        response = _service.get_mfa_report(
            account_id,
            reference,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_mfa_report_all_params_with_retries(self):
        # Enable retries and run test_get_mfa_report_all_params.
        _service.enable_retries()
        self.test_get_mfa_report_all_params()

        # Disable retries and run test_get_mfa_report_all_params.
        _service.disable_retries()
        self.test_get_mfa_report_all_params()

    @responses.activate
    def test_get_mfa_report_value_error(self):
        """
        test_get_mfa_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/mfa/accounts/testString/report/testString')
        mock_response = '{"created_by": "created_by", "reference": "reference", "report_time": "report_time", "account_id": "account_id", "ims_account_id": "ims_account_id", "users": [{"iam_id": "iam_id", "name": "name", "username": "username", "email": "email", "enrollments": {"effective_mfa_type": "effective_mfa_type", "id_based_mfa": {"trait_account_default": "NONE", "trait_user_specific": "NONE", "trait_effective": "NONE", "complies": true, "comply_state": "NO"}, "account_based_mfa": {"security_questions": {"required": true, "enrolled": true}, "totp": {"required": true, "enrolled": true}, "verisign": {"required": true, "enrolled": true}, "complies": true}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        reference = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "reference": reference,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_mfa_report(**req_copy)

    def test_get_mfa_report_value_error_with_retries(self):
        # Enable retries and run test_get_mfa_report_value_error.
        _service.enable_retries()
        self.test_get_mfa_report_value_error()

        # Disable retries and run test_get_mfa_report_value_error.
        _service.disable_retries()
        self.test_get_mfa_report_value_error()


# endregion
##############################################################################
# End of Service: MFAEnrollmentStatus
##############################################################################

##############################################################################
# Start of Service: AccountSettingsAssignments
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListAccountSettingsAssignments:
    """
    Test Class for list_account_settings_assignments
    """

    @responses.activate
    def test_list_account_settings_assignments_all_params(self):
        """
        list_account_settings_assignments()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "assignments": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        template_id = 'testString'
        template_version = 'testString'
        target = 'testString'
        target_type = 'Account'
        limit = 20
        pagetoken = 'testString'
        sort = 'created_at'
        order = 'asc'
        include_history = False

        # Invoke method
        response = _service.list_account_settings_assignments(
            account_id=account_id,
            template_id=template_id,
            template_version=template_version,
            target=target,
            target_type=target_type,
            limit=limit,
            pagetoken=pagetoken,
            sort=sort,
            order=order,
            include_history=include_history,
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
        assert 'target={}'.format(target) in query_string
        assert 'target_type={}'.format(target_type) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_list_account_settings_assignments_all_params_with_retries(self):
        # Enable retries and run test_list_account_settings_assignments_all_params.
        _service.enable_retries()
        self.test_list_account_settings_assignments_all_params()

        # Disable retries and run test_list_account_settings_assignments_all_params.
        _service.disable_retries()
        self.test_list_account_settings_assignments_all_params()

    @responses.activate
    def test_list_account_settings_assignments_required_params(self):
        """
        test_list_account_settings_assignments_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "assignments": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_account_settings_assignments()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_account_settings_assignments_required_params_with_retries(self):
        # Enable retries and run test_list_account_settings_assignments_required_params.
        _service.enable_retries()
        self.test_list_account_settings_assignments_required_params()

        # Disable retries and run test_list_account_settings_assignments_required_params.
        _service.disable_retries()
        self.test_list_account_settings_assignments_required_params()


class TestCreateAccountSettingsAssignment:
    """
    Test Class for create_account_settings_assignment
    """

    @responses.activate
    def test_create_account_settings_assignment_all_params(self):
        """
        create_account_settings_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        template_id = 'testString'
        template_version = 1
        target_type = 'Account'
        target = 'testString'

        # Invoke method
        response = _service.create_account_settings_assignment(
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
        assert req_body['template_id'] == 'testString'
        assert req_body['template_version'] == 1
        assert req_body['target_type'] == 'Account'
        assert req_body['target'] == 'testString'

    def test_create_account_settings_assignment_all_params_with_retries(self):
        # Enable retries and run test_create_account_settings_assignment_all_params.
        _service.enable_retries()
        self.test_create_account_settings_assignment_all_params()

        # Disable retries and run test_create_account_settings_assignment_all_params.
        _service.disable_retries()
        self.test_create_account_settings_assignment_all_params()

    @responses.activate
    def test_create_account_settings_assignment_value_error(self):
        """
        test_create_account_settings_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        template_id = 'testString'
        template_version = 1
        target_type = 'Account'
        target = 'testString'

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
                _service.create_account_settings_assignment(**req_copy)

    def test_create_account_settings_assignment_value_error_with_retries(self):
        # Enable retries and run test_create_account_settings_assignment_value_error.
        _service.enable_retries()
        self.test_create_account_settings_assignment_value_error()

        # Disable retries and run test_create_account_settings_assignment_value_error.
        _service.disable_retries()
        self.test_create_account_settings_assignment_value_error()


class TestGetAccountSettingsAssignment:
    """
    Test Class for get_account_settings_assignment
    """

    @responses.activate
    def test_get_account_settings_assignment_all_params(self):
        """
        get_account_settings_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_account_settings_assignment(
            assignment_id,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_get_account_settings_assignment_all_params_with_retries(self):
        # Enable retries and run test_get_account_settings_assignment_all_params.
        _service.enable_retries()
        self.test_get_account_settings_assignment_all_params()

        # Disable retries and run test_get_account_settings_assignment_all_params.
        _service.disable_retries()
        self.test_get_account_settings_assignment_all_params()

    @responses.activate
    def test_get_account_settings_assignment_required_params(self):
        """
        test_get_account_settings_assignment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
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
        response = _service.get_account_settings_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_account_settings_assignment_required_params_with_retries(self):
        # Enable retries and run test_get_account_settings_assignment_required_params.
        _service.enable_retries()
        self.test_get_account_settings_assignment_required_params()

        # Disable retries and run test_get_account_settings_assignment_required_params.
        _service.disable_retries()
        self.test_get_account_settings_assignment_required_params()

    @responses.activate
    def test_get_account_settings_assignment_value_error(self):
        """
        test_get_account_settings_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
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
                _service.get_account_settings_assignment(**req_copy)

    def test_get_account_settings_assignment_value_error_with_retries(self):
        # Enable retries and run test_get_account_settings_assignment_value_error.
        _service.enable_retries()
        self.test_get_account_settings_assignment_value_error()

        # Disable retries and run test_get_account_settings_assignment_value_error.
        _service.disable_retries()
        self.test_get_account_settings_assignment_value_error()


class TestDeleteAccountSettingsAssignment:
    """
    Test Class for delete_account_settings_assignment
    """

    @responses.activate
    def test_delete_account_settings_assignment_all_params(self):
        """
        delete_account_settings_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "status_code": "status_code", "errors": [{"code": "code", "message_code": "message_code", "message": "message", "details": "details"}], "trace": "trace"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assignment_id = 'testString'

        # Invoke method
        response = _service.delete_account_settings_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_account_settings_assignment_all_params_with_retries(self):
        # Enable retries and run test_delete_account_settings_assignment_all_params.
        _service.enable_retries()
        self.test_delete_account_settings_assignment_all_params()

        # Disable retries and run test_delete_account_settings_assignment_all_params.
        _service.disable_retries()
        self.test_delete_account_settings_assignment_all_params()

    @responses.activate
    def test_delete_account_settings_assignment_value_error(self):
        """
        test_delete_account_settings_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "status_code": "status_code", "errors": [{"code": "code", "message_code": "message_code", "message": "message", "details": "details"}], "trace": "trace"}'
        responses.add(
            responses.DELETE,
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
                _service.delete_account_settings_assignment(**req_copy)

    def test_delete_account_settings_assignment_value_error_with_retries(self):
        # Enable retries and run test_delete_account_settings_assignment_value_error.
        _service.enable_retries()
        self.test_delete_account_settings_assignment_value_error()

        # Disable retries and run test_delete_account_settings_assignment_value_error.
        _service.disable_retries()
        self.test_delete_account_settings_assignment_value_error()


class TestUpdateAccountSettingsAssignment:
    """
    Test Class for update_account_settings_assignment
    """

    @responses.activate
    def test_update_account_settings_assignment_all_params(self):
        """
        update_account_settings_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
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
        template_version = 1

        # Invoke method
        response = _service.update_account_settings_assignment(
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
        assert req_body['template_version'] == 1

    def test_update_account_settings_assignment_all_params_with_retries(self):
        # Enable retries and run test_update_account_settings_assignment_all_params.
        _service.enable_retries()
        self.test_update_account_settings_assignment_all_params()

        # Disable retries and run test_update_account_settings_assignment_all_params.
        _service.disable_retries()
        self.test_update_account_settings_assignment_all_params()

    @responses.activate
    def test_update_account_settings_assignment_value_error(self):
        """
        test_update_account_settings_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
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
        template_version = 1

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assignment_id": assignment_id,
            "if_match": if_match,
            "template_version": template_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_account_settings_assignment(**req_copy)

    def test_update_account_settings_assignment_value_error_with_retries(self):
        # Enable retries and run test_update_account_settings_assignment_value_error.
        _service.enable_retries()
        self.test_update_account_settings_assignment_value_error()

        # Disable retries and run test_update_account_settings_assignment_value_error.
        _service.disable_retries()
        self.test_update_account_settings_assignment_value_error()


# endregion
##############################################################################
# End of Service: AccountSettingsAssignments
##############################################################################

##############################################################################
# Start of Service: AccountSettingsTemplate
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListAccountSettingsTemplates:
    """
    Test Class for list_account_settings_templates
    """

    @responses.activate
    def test_list_account_settings_templates_all_params(self):
        """
        list_account_settings_templates()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "account_settings_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        limit = '20'
        pagetoken = 'testString'
        sort = 'created_at'
        order = 'asc'
        include_history = 'false'

        # Invoke method
        response = _service.list_account_settings_templates(
            account_id=account_id,
            limit=limit,
            pagetoken=pagetoken,
            sort=sort,
            order=order,
            include_history=include_history,
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
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format(include_history) in query_string

    def test_list_account_settings_templates_all_params_with_retries(self):
        # Enable retries and run test_list_account_settings_templates_all_params.
        _service.enable_retries()
        self.test_list_account_settings_templates_all_params()

        # Disable retries and run test_list_account_settings_templates_all_params.
        _service.disable_retries()
        self.test_list_account_settings_templates_all_params()

    @responses.activate
    def test_list_account_settings_templates_required_params(self):
        """
        test_list_account_settings_templates_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "account_settings_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_account_settings_templates()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_account_settings_templates_required_params_with_retries(self):
        # Enable retries and run test_list_account_settings_templates_required_params.
        _service.enable_retries()
        self.test_list_account_settings_templates_required_params()

        # Disable retries and run test_list_account_settings_templates_required_params.
        _service.disable_retries()
        self.test_list_account_settings_templates_required_params()


class TestCreateAccountSettingsTemplate:
    """
    Test Class for create_account_settings_template
    """

    @responses.activate
    def test_create_account_settings_template_all_params(self):
        """
        create_account_settings_template()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AccountSettingsUserMFA model
        account_settings_user_mfa_model = {}
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        # Construct a dict representation of a AccountSettingsComponent model
        account_settings_component_model = {}
        account_settings_component_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_component_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_component_model['allowed_ip_addresses'] = 'testString'
        account_settings_component_model['mfa'] = 'NONE'
        account_settings_component_model['user_mfa'] = [account_settings_user_mfa_model]
        account_settings_component_model['session_expiration_in_seconds'] = '86400'
        account_settings_component_model['session_invalidation_in_seconds'] = '7200'
        account_settings_component_model['max_sessions_per_identity'] = 'testString'
        account_settings_component_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_component_model['system_refresh_token_expiration_in_seconds'] = '259200'

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        account_settings = account_settings_component_model

        # Invoke method
        response = _service.create_account_settings_template(
            account_id=account_id,
            name=name,
            description=description,
            account_settings=account_settings,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['account_settings'] == account_settings_component_model

    def test_create_account_settings_template_all_params_with_retries(self):
        # Enable retries and run test_create_account_settings_template_all_params.
        _service.enable_retries()
        self.test_create_account_settings_template_all_params()

        # Disable retries and run test_create_account_settings_template_all_params.
        _service.disable_retries()
        self.test_create_account_settings_template_all_params()


class TestGetLatestAccountSettingsTemplateVersion:
    """
    Test Class for get_latest_account_settings_template_version
    """

    @responses.activate
    def test_get_latest_account_settings_template_version_all_params(self):
        """
        get_latest_account_settings_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_latest_account_settings_template_version(
            template_id,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_get_latest_account_settings_template_version_all_params_with_retries(self):
        # Enable retries and run test_get_latest_account_settings_template_version_all_params.
        _service.enable_retries()
        self.test_get_latest_account_settings_template_version_all_params()

        # Disable retries and run test_get_latest_account_settings_template_version_all_params.
        _service.disable_retries()
        self.test_get_latest_account_settings_template_version_all_params()

    @responses.activate
    def test_get_latest_account_settings_template_version_required_params(self):
        """
        test_get_latest_account_settings_template_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
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
        response = _service.get_latest_account_settings_template_version(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_latest_account_settings_template_version_required_params_with_retries(self):
        # Enable retries and run test_get_latest_account_settings_template_version_required_params.
        _service.enable_retries()
        self.test_get_latest_account_settings_template_version_required_params()

        # Disable retries and run test_get_latest_account_settings_template_version_required_params.
        _service.disable_retries()
        self.test_get_latest_account_settings_template_version_required_params()

    @responses.activate
    def test_get_latest_account_settings_template_version_value_error(self):
        """
        test_get_latest_account_settings_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
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
                _service.get_latest_account_settings_template_version(**req_copy)

    def test_get_latest_account_settings_template_version_value_error_with_retries(self):
        # Enable retries and run test_get_latest_account_settings_template_version_value_error.
        _service.enable_retries()
        self.test_get_latest_account_settings_template_version_value_error()

        # Disable retries and run test_get_latest_account_settings_template_version_value_error.
        _service.disable_retries()
        self.test_get_latest_account_settings_template_version_value_error()


class TestDeleteAllVersionsOfAccountSettingsTemplate:
    """
    Test Class for delete_all_versions_of_account_settings_template
    """

    @responses.activate
    def test_delete_all_versions_of_account_settings_template_all_params(self):
        """
        delete_all_versions_of_account_settings_template()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'

        # Invoke method
        response = _service.delete_all_versions_of_account_settings_template(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_all_versions_of_account_settings_template_all_params_with_retries(self):
        # Enable retries and run test_delete_all_versions_of_account_settings_template_all_params.
        _service.enable_retries()
        self.test_delete_all_versions_of_account_settings_template_all_params()

        # Disable retries and run test_delete_all_versions_of_account_settings_template_all_params.
        _service.disable_retries()
        self.test_delete_all_versions_of_account_settings_template_all_params()

    @responses.activate
    def test_delete_all_versions_of_account_settings_template_value_error(self):
        """
        test_delete_all_versions_of_account_settings_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString')
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
                _service.delete_all_versions_of_account_settings_template(**req_copy)

    def test_delete_all_versions_of_account_settings_template_value_error_with_retries(self):
        # Enable retries and run test_delete_all_versions_of_account_settings_template_value_error.
        _service.enable_retries()
        self.test_delete_all_versions_of_account_settings_template_value_error()

        # Disable retries and run test_delete_all_versions_of_account_settings_template_value_error.
        _service.disable_retries()
        self.test_delete_all_versions_of_account_settings_template_value_error()


class TestListVersionsOfAccountSettingsTemplate:
    """
    Test Class for list_versions_of_account_settings_template
    """

    @responses.activate
    def test_list_versions_of_account_settings_template_all_params(self):
        """
        list_versions_of_account_settings_template()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "account_settings_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        limit = '20'
        pagetoken = 'testString'
        sort = 'created_at'
        order = 'asc'
        include_history = 'false'

        # Invoke method
        response = _service.list_versions_of_account_settings_template(
            template_id,
            limit=limit,
            pagetoken=pagetoken,
            sort=sort,
            order=order,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format(include_history) in query_string

    def test_list_versions_of_account_settings_template_all_params_with_retries(self):
        # Enable retries and run test_list_versions_of_account_settings_template_all_params.
        _service.enable_retries()
        self.test_list_versions_of_account_settings_template_all_params()

        # Disable retries and run test_list_versions_of_account_settings_template_all_params.
        _service.disable_retries()
        self.test_list_versions_of_account_settings_template_all_params()

    @responses.activate
    def test_list_versions_of_account_settings_template_required_params(self):
        """
        test_list_versions_of_account_settings_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "account_settings_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
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
        response = _service.list_versions_of_account_settings_template(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_versions_of_account_settings_template_required_params_with_retries(self):
        # Enable retries and run test_list_versions_of_account_settings_template_required_params.
        _service.enable_retries()
        self.test_list_versions_of_account_settings_template_required_params()

        # Disable retries and run test_list_versions_of_account_settings_template_required_params.
        _service.disable_retries()
        self.test_list_versions_of_account_settings_template_required_params()

    @responses.activate
    def test_list_versions_of_account_settings_template_value_error(self):
        """
        test_list_versions_of_account_settings_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "account_settings_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
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
                _service.list_versions_of_account_settings_template(**req_copy)

    def test_list_versions_of_account_settings_template_value_error_with_retries(self):
        # Enable retries and run test_list_versions_of_account_settings_template_value_error.
        _service.enable_retries()
        self.test_list_versions_of_account_settings_template_value_error()

        # Disable retries and run test_list_versions_of_account_settings_template_value_error.
        _service.disable_retries()
        self.test_list_versions_of_account_settings_template_value_error()


class TestCreateAccountSettingsTemplateVersion:
    """
    Test Class for create_account_settings_template_version
    """

    @responses.activate
    def test_create_account_settings_template_version_all_params(self):
        """
        create_account_settings_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AccountSettingsUserMFA model
        account_settings_user_mfa_model = {}
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        # Construct a dict representation of a AccountSettingsComponent model
        account_settings_component_model = {}
        account_settings_component_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_component_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_component_model['allowed_ip_addresses'] = 'testString'
        account_settings_component_model['mfa'] = 'NONE'
        account_settings_component_model['user_mfa'] = [account_settings_user_mfa_model]
        account_settings_component_model['session_expiration_in_seconds'] = '86400'
        account_settings_component_model['session_invalidation_in_seconds'] = '7200'
        account_settings_component_model['max_sessions_per_identity'] = 'testString'
        account_settings_component_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_component_model['system_refresh_token_expiration_in_seconds'] = '259200'

        # Set up parameter values
        template_id = 'testString'
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        account_settings = account_settings_component_model

        # Invoke method
        response = _service.create_account_settings_template_version(
            template_id,
            account_id=account_id,
            name=name,
            description=description,
            account_settings=account_settings,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['account_settings'] == account_settings_component_model

    def test_create_account_settings_template_version_all_params_with_retries(self):
        # Enable retries and run test_create_account_settings_template_version_all_params.
        _service.enable_retries()
        self.test_create_account_settings_template_version_all_params()

        # Disable retries and run test_create_account_settings_template_version_all_params.
        _service.disable_retries()
        self.test_create_account_settings_template_version_all_params()

    @responses.activate
    def test_create_account_settings_template_version_value_error(self):
        """
        test_create_account_settings_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AccountSettingsUserMFA model
        account_settings_user_mfa_model = {}
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        # Construct a dict representation of a AccountSettingsComponent model
        account_settings_component_model = {}
        account_settings_component_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_component_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_component_model['allowed_ip_addresses'] = 'testString'
        account_settings_component_model['mfa'] = 'NONE'
        account_settings_component_model['user_mfa'] = [account_settings_user_mfa_model]
        account_settings_component_model['session_expiration_in_seconds'] = '86400'
        account_settings_component_model['session_invalidation_in_seconds'] = '7200'
        account_settings_component_model['max_sessions_per_identity'] = 'testString'
        account_settings_component_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_component_model['system_refresh_token_expiration_in_seconds'] = '259200'

        # Set up parameter values
        template_id = 'testString'
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        account_settings = account_settings_component_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_account_settings_template_version(**req_copy)

    def test_create_account_settings_template_version_value_error_with_retries(self):
        # Enable retries and run test_create_account_settings_template_version_value_error.
        _service.enable_retries()
        self.test_create_account_settings_template_version_value_error()

        # Disable retries and run test_create_account_settings_template_version_value_error.
        _service.disable_retries()
        self.test_create_account_settings_template_version_value_error()


class TestGetAccountSettingsTemplateVersion:
    """
    Test Class for get_account_settings_template_version
    """

    @responses.activate
    def test_get_account_settings_template_version_all_params(self):
        """
        get_account_settings_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_account_settings_template_version(
            template_id,
            version,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_get_account_settings_template_version_all_params_with_retries(self):
        # Enable retries and run test_get_account_settings_template_version_all_params.
        _service.enable_retries()
        self.test_get_account_settings_template_version_all_params()

        # Disable retries and run test_get_account_settings_template_version_all_params.
        _service.disable_retries()
        self.test_get_account_settings_template_version_all_params()

    @responses.activate
    def test_get_account_settings_template_version_required_params(self):
        """
        test_get_account_settings_template_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.get_account_settings_template_version(
            template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_account_settings_template_version_required_params_with_retries(self):
        # Enable retries and run test_get_account_settings_template_version_required_params.
        _service.enable_retries()
        self.test_get_account_settings_template_version_required_params()

        # Disable retries and run test_get_account_settings_template_version_required_params.
        _service.disable_retries()
        self.test_get_account_settings_template_version_required_params()

    @responses.activate
    def test_get_account_settings_template_version_value_error(self):
        """
        test_get_account_settings_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_account_settings_template_version(**req_copy)

    def test_get_account_settings_template_version_value_error_with_retries(self):
        # Enable retries and run test_get_account_settings_template_version_value_error.
        _service.enable_retries()
        self.test_get_account_settings_template_version_value_error()

        # Disable retries and run test_get_account_settings_template_version_value_error.
        _service.disable_retries()
        self.test_get_account_settings_template_version_value_error()


class TestUpdateAccountSettingsTemplateVersion:
    """
    Test Class for update_account_settings_template_version
    """

    @responses.activate
    def test_update_account_settings_template_version_all_params(self):
        """
        update_account_settings_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AccountSettingsUserMFA model
        account_settings_user_mfa_model = {}
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        # Construct a dict representation of a AccountSettingsComponent model
        account_settings_component_model = {}
        account_settings_component_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_component_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_component_model['allowed_ip_addresses'] = 'testString'
        account_settings_component_model['mfa'] = 'NONE'
        account_settings_component_model['user_mfa'] = [account_settings_user_mfa_model]
        account_settings_component_model['session_expiration_in_seconds'] = '86400'
        account_settings_component_model['session_invalidation_in_seconds'] = '7200'
        account_settings_component_model['max_sessions_per_identity'] = 'testString'
        account_settings_component_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_component_model['system_refresh_token_expiration_in_seconds'] = '259200'

        # Set up parameter values
        if_match = 'testString'
        template_id = 'testString'
        version = 'testString'
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        account_settings = account_settings_component_model

        # Invoke method
        response = _service.update_account_settings_template_version(
            if_match,
            template_id,
            version,
            account_id=account_id,
            name=name,
            description=description,
            account_settings=account_settings,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['account_settings'] == account_settings_component_model

    def test_update_account_settings_template_version_all_params_with_retries(self):
        # Enable retries and run test_update_account_settings_template_version_all_params.
        _service.enable_retries()
        self.test_update_account_settings_template_version_all_params()

        # Disable retries and run test_update_account_settings_template_version_all_params.
        _service.disable_retries()
        self.test_update_account_settings_template_version_all_params()

    @responses.activate
    def test_update_account_settings_template_version_value_error(self):
        """
        test_update_account_settings_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "account_settings": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AccountSettingsUserMFA model
        account_settings_user_mfa_model = {}
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        # Construct a dict representation of a AccountSettingsComponent model
        account_settings_component_model = {}
        account_settings_component_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_component_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_component_model['allowed_ip_addresses'] = 'testString'
        account_settings_component_model['mfa'] = 'NONE'
        account_settings_component_model['user_mfa'] = [account_settings_user_mfa_model]
        account_settings_component_model['session_expiration_in_seconds'] = '86400'
        account_settings_component_model['session_invalidation_in_seconds'] = '7200'
        account_settings_component_model['max_sessions_per_identity'] = 'testString'
        account_settings_component_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_component_model['system_refresh_token_expiration_in_seconds'] = '259200'

        # Set up parameter values
        if_match = 'testString'
        template_id = 'testString'
        version = 'testString'
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        account_settings = account_settings_component_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "if_match": if_match,
            "template_id": template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_account_settings_template_version(**req_copy)

    def test_update_account_settings_template_version_value_error_with_retries(self):
        # Enable retries and run test_update_account_settings_template_version_value_error.
        _service.enable_retries()
        self.test_update_account_settings_template_version_value_error()

        # Disable retries and run test_update_account_settings_template_version_value_error.
        _service.disable_retries()
        self.test_update_account_settings_template_version_value_error()


class TestDeleteAccountSettingsTemplateVersion:
    """
    Test Class for delete_account_settings_template_version
    """

    @responses.activate
    def test_delete_account_settings_template_version_all_params(self):
        """
        delete_account_settings_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.delete_account_settings_template_version(
            template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_account_settings_template_version_all_params_with_retries(self):
        # Enable retries and run test_delete_account_settings_template_version_all_params.
        _service.enable_retries()
        self.test_delete_account_settings_template_version_all_params()

        # Disable retries and run test_delete_account_settings_template_version_all_params.
        _service.disable_retries()
        self.test_delete_account_settings_template_version_all_params()

    @responses.activate
    def test_delete_account_settings_template_version_value_error(self):
        """
        test_delete_account_settings_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_account_settings_template_version(**req_copy)

    def test_delete_account_settings_template_version_value_error_with_retries(self):
        # Enable retries and run test_delete_account_settings_template_version_value_error.
        _service.enable_retries()
        self.test_delete_account_settings_template_version_value_error()

        # Disable retries and run test_delete_account_settings_template_version_value_error.
        _service.disable_retries()
        self.test_delete_account_settings_template_version_value_error()


class TestCommitAccountSettingsTemplate:
    """
    Test Class for commit_account_settings_template
    """

    @responses.activate
    def test_commit_account_settings_template_all_params(self):
        """
        commit_account_settings_template()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.commit_account_settings_template(
            template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_commit_account_settings_template_all_params_with_retries(self):
        # Enable retries and run test_commit_account_settings_template_all_params.
        _service.enable_retries()
        self.test_commit_account_settings_template_all_params()

        # Disable retries and run test_commit_account_settings_template_all_params.
        _service.disable_retries()
        self.test_commit_account_settings_template_all_params()

    @responses.activate
    def test_commit_account_settings_template_value_error(self):
        """
        test_commit_account_settings_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/account_settings_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.commit_account_settings_template(**req_copy)

    def test_commit_account_settings_template_value_error_with_retries(self):
        # Enable retries and run test_commit_account_settings_template_value_error.
        _service.enable_retries()
        self.test_commit_account_settings_template_value_error()

        # Disable retries and run test_commit_account_settings_template_value_error.
        _service.disable_retries()
        self.test_commit_account_settings_template_value_error()


# endregion
##############################################################################
# End of Service: AccountSettingsTemplate
##############################################################################

##############################################################################
# Start of Service: ActivityOperations
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateReport:
    """
    Test Class for create_report
    """

    @responses.activate
    def test_create_report_all_params(self):
        """
        create_report()
        """
        # Set up mock
        url = preprocess_url('/v1/activity/accounts/testString/report')
        mock_response = '{"reference": "reference"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        account_id = 'testString'
        type = 'inactive'
        duration = '720'

        # Invoke method
        response = _service.create_report(
            account_id,
            type=type,
            duration=duration,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string
        assert 'duration={}'.format(duration) in query_string

    def test_create_report_all_params_with_retries(self):
        # Enable retries and run test_create_report_all_params.
        _service.enable_retries()
        self.test_create_report_all_params()

        # Disable retries and run test_create_report_all_params.
        _service.disable_retries()
        self.test_create_report_all_params()

    @responses.activate
    def test_create_report_required_params(self):
        """
        test_create_report_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/activity/accounts/testString/report')
        mock_response = '{"reference": "reference"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.create_report(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_create_report_required_params_with_retries(self):
        # Enable retries and run test_create_report_required_params.
        _service.enable_retries()
        self.test_create_report_required_params()

        # Disable retries and run test_create_report_required_params.
        _service.disable_retries()
        self.test_create_report_required_params()

    @responses.activate
    def test_create_report_value_error(self):
        """
        test_create_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/activity/accounts/testString/report')
        mock_response = '{"reference": "reference"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
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
                _service.create_report(**req_copy)

    def test_create_report_value_error_with_retries(self):
        # Enable retries and run test_create_report_value_error.
        _service.enable_retries()
        self.test_create_report_value_error()

        # Disable retries and run test_create_report_value_error.
        _service.disable_retries()
        self.test_create_report_value_error()


class TestGetReport:
    """
    Test Class for get_report
    """

    @responses.activate
    def test_get_report_all_params(self):
        """
        get_report()
        """
        # Set up mock
        url = preprocess_url('/v1/activity/accounts/testString/report/testString')
        mock_response = '{"created_by": "created_by", "reference": "reference", "report_duration": "report_duration", "report_start_time": "report_start_time", "report_end_time": "report_end_time", "users": [{"iam_id": "iam_id", "name": "name", "username": "username", "email": "email", "last_authn": "last_authn"}], "apikeys": [{"id": "id", "name": "name", "type": "type", "serviceid": {"id": "id", "name": "name"}, "user": {"iam_id": "iam_id", "name": "name", "username": "username", "email": "email"}, "last_authn": "last_authn"}], "serviceids": [{"id": "id", "name": "name", "last_authn": "last_authn"}], "profiles": [{"id": "id", "name": "name", "last_authn": "last_authn"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        reference = 'testString'

        # Invoke method
        response = _service.get_report(
            account_id,
            reference,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_all_params_with_retries(self):
        # Enable retries and run test_get_report_all_params.
        _service.enable_retries()
        self.test_get_report_all_params()

        # Disable retries and run test_get_report_all_params.
        _service.disable_retries()
        self.test_get_report_all_params()

    @responses.activate
    def test_get_report_value_error(self):
        """
        test_get_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/activity/accounts/testString/report/testString')
        mock_response = '{"created_by": "created_by", "reference": "reference", "report_duration": "report_duration", "report_start_time": "report_start_time", "report_end_time": "report_end_time", "users": [{"iam_id": "iam_id", "name": "name", "username": "username", "email": "email", "last_authn": "last_authn"}], "apikeys": [{"id": "id", "name": "name", "type": "type", "serviceid": {"id": "id", "name": "name"}, "user": {"iam_id": "iam_id", "name": "name", "username": "username", "email": "email"}, "last_authn": "last_authn"}], "serviceids": [{"id": "id", "name": "name", "last_authn": "last_authn"}], "profiles": [{"id": "id", "name": "name", "last_authn": "last_authn"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        reference = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "reference": reference,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_report(**req_copy)

    def test_get_report_value_error_with_retries(self):
        # Enable retries and run test_get_report_value_error.
        _service.enable_retries()
        self.test_get_report_value_error()

        # Disable retries and run test_get_report_value_error.
        _service.disable_retries()
        self.test_get_report_value_error()


# endregion
##############################################################################
# End of Service: ActivityOperations
##############################################################################

##############################################################################
# Start of Service: EffectiveAccountSettings
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetEffectiveAccountSettings:
    """
    Test Class for get_effective_account_settings
    """

    @responses.activate
    def test_get_effective_account_settings_all_params(self):
        """
        get_effective_account_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/effective_settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "effective": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE", "name": "name", "userName": "user_name", "email": "email", "description": "description"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "account": {"account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE", "name": "name", "userName": "user_name", "email": "email", "description": "description"}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "assigned_templates": [{"template_id": "template_id", "template_version": 16, "template_name": "template_name", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE", "name": "name", "userName": "user_name", "email": "email", "description": "description"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        include_history = False
        resolve_user_mfa = False

        # Invoke method
        response = _service.get_effective_account_settings(
            account_id,
            include_history=include_history,
            resolve_user_mfa=resolve_user_mfa,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string
        assert 'resolve_user_mfa={}'.format('true' if resolve_user_mfa else 'false') in query_string

    def test_get_effective_account_settings_all_params_with_retries(self):
        # Enable retries and run test_get_effective_account_settings_all_params.
        _service.enable_retries()
        self.test_get_effective_account_settings_all_params()

        # Disable retries and run test_get_effective_account_settings_all_params.
        _service.disable_retries()
        self.test_get_effective_account_settings_all_params()

    @responses.activate
    def test_get_effective_account_settings_required_params(self):
        """
        test_get_effective_account_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/effective_settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "effective": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE", "name": "name", "userName": "user_name", "email": "email", "description": "description"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "account": {"account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE", "name": "name", "userName": "user_name", "email": "email", "description": "description"}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "assigned_templates": [{"template_id": "template_id", "template_version": 16, "template_name": "template_name", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE", "name": "name", "userName": "user_name", "email": "email", "description": "description"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}]}'
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
        response = _service.get_effective_account_settings(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_effective_account_settings_required_params_with_retries(self):
        # Enable retries and run test_get_effective_account_settings_required_params.
        _service.enable_retries()
        self.test_get_effective_account_settings_required_params()

        # Disable retries and run test_get_effective_account_settings_required_params.
        _service.disable_retries()
        self.test_get_effective_account_settings_required_params()

    @responses.activate
    def test_get_effective_account_settings_value_error(self):
        """
        test_get_effective_account_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/accounts/testString/effective_settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "effective": {"restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE", "name": "name", "userName": "user_name", "email": "email", "description": "description"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "account": {"account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE", "name": "name", "userName": "user_name", "email": "email", "description": "description"}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}, "assigned_templates": [{"template_id": "template_id", "template_version": 16, "template_name": "template_name", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "mfa": "NONE", "user_mfa": [{"iam_id": "iam_id", "mfa": "NONE", "name": "name", "userName": "user_name", "email": "email", "description": "description"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity", "system_access_token_expiration_in_seconds": "3600", "system_refresh_token_expiration_in_seconds": "259200"}]}'
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
                _service.get_effective_account_settings(**req_copy)

    def test_get_effective_account_settings_value_error_with_retries(self):
        # Enable retries and run test_get_effective_account_settings_value_error.
        _service.enable_retries()
        self.test_get_effective_account_settings_value_error()

        # Disable retries and run test_get_effective_account_settings_value_error.
        _service.disable_retries()
        self.test_get_effective_account_settings_value_error()


# endregion
##############################################################################
# End of Service: EffectiveAccountSettings
##############################################################################

##############################################################################
# Start of Service: TrustedProfileAssignments
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListTrustedProfileAssignments:
    """
    Test Class for list_trusted_profile_assignments
    """

    @responses.activate
    def test_list_trusted_profile_assignments_all_params(self):
        """
        list_trusted_profile_assignments()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "assignments": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        template_id = 'testString'
        template_version = 'testString'
        target = 'testString'
        target_type = 'Account'
        limit = 20
        pagetoken = 'testString'
        sort = 'created_at'
        order = 'asc'
        include_history = False

        # Invoke method
        response = _service.list_trusted_profile_assignments(
            account_id=account_id,
            template_id=template_id,
            template_version=template_version,
            target=target,
            target_type=target_type,
            limit=limit,
            pagetoken=pagetoken,
            sort=sort,
            order=order,
            include_history=include_history,
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
        assert 'target={}'.format(target) in query_string
        assert 'target_type={}'.format(target_type) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_list_trusted_profile_assignments_all_params_with_retries(self):
        # Enable retries and run test_list_trusted_profile_assignments_all_params.
        _service.enable_retries()
        self.test_list_trusted_profile_assignments_all_params()

        # Disable retries and run test_list_trusted_profile_assignments_all_params.
        _service.disable_retries()
        self.test_list_trusted_profile_assignments_all_params()

    @responses.activate
    def test_list_trusted_profile_assignments_required_params(self):
        """
        test_list_trusted_profile_assignments_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "assignments": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_trusted_profile_assignments()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_trusted_profile_assignments_required_params_with_retries(self):
        # Enable retries and run test_list_trusted_profile_assignments_required_params.
        _service.enable_retries()
        self.test_list_trusted_profile_assignments_required_params()

        # Disable retries and run test_list_trusted_profile_assignments_required_params.
        _service.disable_retries()
        self.test_list_trusted_profile_assignments_required_params()


class TestCreateTrustedProfileAssignment:
    """
    Test Class for create_trusted_profile_assignment
    """

    @responses.activate
    def test_create_trusted_profile_assignment_all_params(self):
        """
        create_trusted_profile_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        template_id = 'testString'
        template_version = 1
        target_type = 'Account'
        target = 'testString'

        # Invoke method
        response = _service.create_trusted_profile_assignment(
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
        assert req_body['template_id'] == 'testString'
        assert req_body['template_version'] == 1
        assert req_body['target_type'] == 'Account'
        assert req_body['target'] == 'testString'

    def test_create_trusted_profile_assignment_all_params_with_retries(self):
        # Enable retries and run test_create_trusted_profile_assignment_all_params.
        _service.enable_retries()
        self.test_create_trusted_profile_assignment_all_params()

        # Disable retries and run test_create_trusted_profile_assignment_all_params.
        _service.disable_retries()
        self.test_create_trusted_profile_assignment_all_params()

    @responses.activate
    def test_create_trusted_profile_assignment_value_error(self):
        """
        test_create_trusted_profile_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        template_id = 'testString'
        template_version = 1
        target_type = 'Account'
        target = 'testString'

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
                _service.create_trusted_profile_assignment(**req_copy)

    def test_create_trusted_profile_assignment_value_error_with_retries(self):
        # Enable retries and run test_create_trusted_profile_assignment_value_error.
        _service.enable_retries()
        self.test_create_trusted_profile_assignment_value_error()

        # Disable retries and run test_create_trusted_profile_assignment_value_error.
        _service.disable_retries()
        self.test_create_trusted_profile_assignment_value_error()


class TestGetTrustedProfileAssignment:
    """
    Test Class for get_trusted_profile_assignment
    """

    @responses.activate
    def test_get_trusted_profile_assignment_all_params(self):
        """
        get_trusted_profile_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assignment_id = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_trusted_profile_assignment(
            assignment_id,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_get_trusted_profile_assignment_all_params_with_retries(self):
        # Enable retries and run test_get_trusted_profile_assignment_all_params.
        _service.enable_retries()
        self.test_get_trusted_profile_assignment_all_params()

        # Disable retries and run test_get_trusted_profile_assignment_all_params.
        _service.disable_retries()
        self.test_get_trusted_profile_assignment_all_params()

    @responses.activate
    def test_get_trusted_profile_assignment_required_params(self):
        """
        test_get_trusted_profile_assignment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
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
        response = _service.get_trusted_profile_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_trusted_profile_assignment_required_params_with_retries(self):
        # Enable retries and run test_get_trusted_profile_assignment_required_params.
        _service.enable_retries()
        self.test_get_trusted_profile_assignment_required_params()

        # Disable retries and run test_get_trusted_profile_assignment_required_params.
        _service.disable_retries()
        self.test_get_trusted_profile_assignment_required_params()

    @responses.activate
    def test_get_trusted_profile_assignment_value_error(self):
        """
        test_get_trusted_profile_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
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
                _service.get_trusted_profile_assignment(**req_copy)

    def test_get_trusted_profile_assignment_value_error_with_retries(self):
        # Enable retries and run test_get_trusted_profile_assignment_value_error.
        _service.enable_retries()
        self.test_get_trusted_profile_assignment_value_error()

        # Disable retries and run test_get_trusted_profile_assignment_value_error.
        _service.disable_retries()
        self.test_get_trusted_profile_assignment_value_error()


class TestDeleteTrustedProfileAssignment:
    """
    Test Class for delete_trusted_profile_assignment
    """

    @responses.activate
    def test_delete_trusted_profile_assignment_all_params(self):
        """
        delete_trusted_profile_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "status_code": "status_code", "errors": [{"code": "code", "message_code": "message_code", "message": "message", "details": "details"}], "trace": "trace"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assignment_id = 'testString'

        # Invoke method
        response = _service.delete_trusted_profile_assignment(
            assignment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_trusted_profile_assignment_all_params_with_retries(self):
        # Enable retries and run test_delete_trusted_profile_assignment_all_params.
        _service.enable_retries()
        self.test_delete_trusted_profile_assignment_all_params()

        # Disable retries and run test_delete_trusted_profile_assignment_all_params.
        _service.disable_retries()
        self.test_delete_trusted_profile_assignment_all_params()

    @responses.activate
    def test_delete_trusted_profile_assignment_value_error(self):
        """
        test_delete_trusted_profile_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "status_code": "status_code", "errors": [{"code": "code", "message_code": "message_code", "message": "message", "details": "details"}], "trace": "trace"}'
        responses.add(
            responses.DELETE,
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
                _service.delete_trusted_profile_assignment(**req_copy)

    def test_delete_trusted_profile_assignment_value_error_with_retries(self):
        # Enable retries and run test_delete_trusted_profile_assignment_value_error.
        _service.enable_retries()
        self.test_delete_trusted_profile_assignment_value_error()

        # Disable retries and run test_delete_trusted_profile_assignment_value_error.
        _service.disable_retries()
        self.test_delete_trusted_profile_assignment_value_error()


class TestUpdateTrustedProfileAssignment:
    """
    Test Class for update_trusted_profile_assignment
    """

    @responses.activate
    def test_update_trusted_profile_assignment_all_params(self):
        """
        update_trusted_profile_assignment()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
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
        template_version = 1

        # Invoke method
        response = _service.update_trusted_profile_assignment(
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
        assert req_body['template_version'] == 1

    def test_update_trusted_profile_assignment_all_params_with_retries(self):
        # Enable retries and run test_update_trusted_profile_assignment_all_params.
        _service.enable_retries()
        self.test_update_trusted_profile_assignment_all_params()

        # Disable retries and run test_update_trusted_profile_assignment_all_params.
        _service.disable_retries()
        self.test_update_trusted_profile_assignment_all_params()

    @responses.activate
    def test_update_trusted_profile_assignment_value_error(self):
        """
        test_update_trusted_profile_assignment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_assignments/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "account_id": "account_id", "template_id": "template_id", "template_version": 16, "target_type": "target_type", "target": "target", "status": "status", "resources": [{"target": "target", "profile": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "account_settings": {"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}, "policy_template_refs": [{"id": "id", "version": "version", "resource_created": {"id": "id"}, "error_message": {"name": "name", "errorCode": "error_code", "message": "message", "statusCode": "status_code"}, "status": "status"}]}], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "href": "href", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "entity_tag": "entity_tag"}'
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
        template_version = 1

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assignment_id": assignment_id,
            "if_match": if_match,
            "template_version": template_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_trusted_profile_assignment(**req_copy)

    def test_update_trusted_profile_assignment_value_error_with_retries(self):
        # Enable retries and run test_update_trusted_profile_assignment_value_error.
        _service.enable_retries()
        self.test_update_trusted_profile_assignment_value_error()

        # Disable retries and run test_update_trusted_profile_assignment_value_error.
        _service.disable_retries()
        self.test_update_trusted_profile_assignment_value_error()


# endregion
##############################################################################
# End of Service: TrustedProfileAssignments
##############################################################################

##############################################################################
# Start of Service: TrustedProfileTemplate
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

        service = IamIdentityV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IamIdentityV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IamIdentityV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListProfileTemplates:
    """
    Test Class for list_profile_templates
    """

    @responses.activate
    def test_list_profile_templates_all_params(self):
        """
        list_profile_templates()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "profile_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'testString'
        limit = '20'
        pagetoken = 'testString'
        sort = 'created_at'
        order = 'asc'
        include_history = 'false'

        # Invoke method
        response = _service.list_profile_templates(
            account_id=account_id,
            limit=limit,
            pagetoken=pagetoken,
            sort=sort,
            order=order,
            include_history=include_history,
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
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format(include_history) in query_string

    def test_list_profile_templates_all_params_with_retries(self):
        # Enable retries and run test_list_profile_templates_all_params.
        _service.enable_retries()
        self.test_list_profile_templates_all_params()

        # Disable retries and run test_list_profile_templates_all_params.
        _service.disable_retries()
        self.test_list_profile_templates_all_params()

    @responses.activate
    def test_list_profile_templates_required_params(self):
        """
        test_list_profile_templates_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "profile_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_profile_templates()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_profile_templates_required_params_with_retries(self):
        # Enable retries and run test_list_profile_templates_required_params.
        _service.enable_retries()
        self.test_list_profile_templates_required_params()

        # Disable retries and run test_list_profile_templates_required_params.
        _service.disable_retries()
        self.test_list_profile_templates_required_params()


class TestCreateProfileTemplate:
    """
    Test Class for create_profile_template
    """

    @responses.activate
    def test_create_profile_template_all_params(self):
        """
        create_profile_template()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a dict representation of a TrustedProfileTemplateClaimRule model
        trusted_profile_template_claim_rule_model = {}
        trusted_profile_template_claim_rule_model['name'] = 'testString'
        trusted_profile_template_claim_rule_model['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model['expiration'] = 38
        trusted_profile_template_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        # Construct a dict representation of a ProfileIdentityRequest model
        profile_identity_request_model = {}
        profile_identity_request_model['identifier'] = 'testString'
        profile_identity_request_model['type'] = 'user'
        profile_identity_request_model['accounts'] = ['testString']
        profile_identity_request_model['description'] = 'testString'

        # Construct a dict representation of a TemplateProfileComponentRequest model
        template_profile_component_request_model = {}
        template_profile_component_request_model['name'] = 'testString'
        template_profile_component_request_model['description'] = 'testString'
        template_profile_component_request_model['rules'] = [trusted_profile_template_claim_rule_model]
        template_profile_component_request_model['identities'] = [profile_identity_request_model]

        # Construct a dict representation of a PolicyTemplateReference model
        policy_template_reference_model = {}
        policy_template_reference_model['id'] = 'testString'
        policy_template_reference_model['version'] = 'testString'

        # Construct a dict representation of a ActionControlsIdentities model
        action_controls_identities_model = {}
        action_controls_identities_model['add'] = True
        action_controls_identities_model['remove'] = True

        # Construct a dict representation of a ActionControlsRules model
        action_controls_rules_model = {}
        action_controls_rules_model['add'] = True
        action_controls_rules_model['remove'] = True

        # Construct a dict representation of a ActionControlsPolicies model
        action_controls_policies_model = {}
        action_controls_policies_model['add'] = True
        action_controls_policies_model['remove'] = True

        # Construct a dict representation of a ActionControls model
        action_controls_model = {}
        action_controls_model['identities'] = action_controls_identities_model
        action_controls_model['rules'] = action_controls_rules_model
        action_controls_model['policies'] = action_controls_policies_model

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        profile = template_profile_component_request_model
        policy_template_references = [policy_template_reference_model]
        action_controls = action_controls_model

        # Invoke method
        response = _service.create_profile_template(
            account_id=account_id,
            name=name,
            description=description,
            profile=profile,
            policy_template_references=policy_template_references,
            action_controls=action_controls,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['profile'] == template_profile_component_request_model
        assert req_body['policy_template_references'] == [policy_template_reference_model]
        assert req_body['action_controls'] == action_controls_model

    def test_create_profile_template_all_params_with_retries(self):
        # Enable retries and run test_create_profile_template_all_params.
        _service.enable_retries()
        self.test_create_profile_template_all_params()

        # Disable retries and run test_create_profile_template_all_params.
        _service.disable_retries()
        self.test_create_profile_template_all_params()


class TestGetLatestProfileTemplateVersion:
    """
    Test Class for get_latest_profile_template_version
    """

    @responses.activate
    def test_get_latest_profile_template_version_all_params(self):
        """
        get_latest_profile_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_latest_profile_template_version(
            template_id,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_get_latest_profile_template_version_all_params_with_retries(self):
        # Enable retries and run test_get_latest_profile_template_version_all_params.
        _service.enable_retries()
        self.test_get_latest_profile_template_version_all_params()

        # Disable retries and run test_get_latest_profile_template_version_all_params.
        _service.disable_retries()
        self.test_get_latest_profile_template_version_all_params()

    @responses.activate
    def test_get_latest_profile_template_version_required_params(self):
        """
        test_get_latest_profile_template_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
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
        response = _service.get_latest_profile_template_version(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_latest_profile_template_version_required_params_with_retries(self):
        # Enable retries and run test_get_latest_profile_template_version_required_params.
        _service.enable_retries()
        self.test_get_latest_profile_template_version_required_params()

        # Disable retries and run test_get_latest_profile_template_version_required_params.
        _service.disable_retries()
        self.test_get_latest_profile_template_version_required_params()

    @responses.activate
    def test_get_latest_profile_template_version_value_error(self):
        """
        test_get_latest_profile_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
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
                _service.get_latest_profile_template_version(**req_copy)

    def test_get_latest_profile_template_version_value_error_with_retries(self):
        # Enable retries and run test_get_latest_profile_template_version_value_error.
        _service.enable_retries()
        self.test_get_latest_profile_template_version_value_error()

        # Disable retries and run test_get_latest_profile_template_version_value_error.
        _service.disable_retries()
        self.test_get_latest_profile_template_version_value_error()


class TestDeleteAllVersionsOfProfileTemplate:
    """
    Test Class for delete_all_versions_of_profile_template
    """

    @responses.activate
    def test_delete_all_versions_of_profile_template_all_params(self):
        """
        delete_all_versions_of_profile_template()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'

        # Invoke method
        response = _service.delete_all_versions_of_profile_template(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_all_versions_of_profile_template_all_params_with_retries(self):
        # Enable retries and run test_delete_all_versions_of_profile_template_all_params.
        _service.enable_retries()
        self.test_delete_all_versions_of_profile_template_all_params()

        # Disable retries and run test_delete_all_versions_of_profile_template_all_params.
        _service.disable_retries()
        self.test_delete_all_versions_of_profile_template_all_params()

    @responses.activate
    def test_delete_all_versions_of_profile_template_value_error(self):
        """
        test_delete_all_versions_of_profile_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString')
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
                _service.delete_all_versions_of_profile_template(**req_copy)

    def test_delete_all_versions_of_profile_template_value_error_with_retries(self):
        # Enable retries and run test_delete_all_versions_of_profile_template_value_error.
        _service.enable_retries()
        self.test_delete_all_versions_of_profile_template_value_error()

        # Disable retries and run test_delete_all_versions_of_profile_template_value_error.
        _service.disable_retries()
        self.test_delete_all_versions_of_profile_template_value_error()


class TestListVersionsOfProfileTemplate:
    """
    Test Class for list_versions_of_profile_template
    """

    @responses.activate
    def test_list_versions_of_profile_template_all_params(self):
        """
        list_versions_of_profile_template()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "profile_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        limit = '20'
        pagetoken = 'testString'
        sort = 'created_at'
        order = 'asc'
        include_history = 'false'

        # Invoke method
        response = _service.list_versions_of_profile_template(
            template_id,
            limit=limit,
            pagetoken=pagetoken,
            sort=sort,
            order=order,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format(include_history) in query_string

    def test_list_versions_of_profile_template_all_params_with_retries(self):
        # Enable retries and run test_list_versions_of_profile_template_all_params.
        _service.enable_retries()
        self.test_list_versions_of_profile_template_all_params()

        # Disable retries and run test_list_versions_of_profile_template_all_params.
        _service.disable_retries()
        self.test_list_versions_of_profile_template_all_params()

    @responses.activate
    def test_list_versions_of_profile_template_required_params(self):
        """
        test_list_versions_of_profile_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "profile_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
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
        response = _service.list_versions_of_profile_template(
            template_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_versions_of_profile_template_required_params_with_retries(self):
        # Enable retries and run test_list_versions_of_profile_template_required_params.
        _service.enable_retries()
        self.test_list_versions_of_profile_template_required_params()

        # Disable retries and run test_list_versions_of_profile_template_required_params.
        _service.disable_retries()
        self.test_list_versions_of_profile_template_required_params()

    @responses.activate
    def test_list_versions_of_profile_template_value_error(self):
        """
        test_list_versions_of_profile_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 20, "first": "first", "previous": "previous", "next": "next", "profile_templates": [{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
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
                _service.list_versions_of_profile_template(**req_copy)

    def test_list_versions_of_profile_template_value_error_with_retries(self):
        # Enable retries and run test_list_versions_of_profile_template_value_error.
        _service.enable_retries()
        self.test_list_versions_of_profile_template_value_error()

        # Disable retries and run test_list_versions_of_profile_template_value_error.
        _service.disable_retries()
        self.test_list_versions_of_profile_template_value_error()


class TestCreateProfileTemplateVersion:
    """
    Test Class for create_profile_template_version
    """

    @responses.activate
    def test_create_profile_template_version_all_params(self):
        """
        create_profile_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a dict representation of a TrustedProfileTemplateClaimRule model
        trusted_profile_template_claim_rule_model = {}
        trusted_profile_template_claim_rule_model['name'] = 'testString'
        trusted_profile_template_claim_rule_model['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model['expiration'] = 38
        trusted_profile_template_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        # Construct a dict representation of a ProfileIdentityRequest model
        profile_identity_request_model = {}
        profile_identity_request_model['identifier'] = 'testString'
        profile_identity_request_model['type'] = 'user'
        profile_identity_request_model['accounts'] = ['testString']
        profile_identity_request_model['description'] = 'testString'

        # Construct a dict representation of a TemplateProfileComponentRequest model
        template_profile_component_request_model = {}
        template_profile_component_request_model['name'] = 'testString'
        template_profile_component_request_model['description'] = 'testString'
        template_profile_component_request_model['rules'] = [trusted_profile_template_claim_rule_model]
        template_profile_component_request_model['identities'] = [profile_identity_request_model]

        # Construct a dict representation of a PolicyTemplateReference model
        policy_template_reference_model = {}
        policy_template_reference_model['id'] = 'testString'
        policy_template_reference_model['version'] = 'testString'

        # Construct a dict representation of a ActionControlsIdentities model
        action_controls_identities_model = {}
        action_controls_identities_model['add'] = True
        action_controls_identities_model['remove'] = True

        # Construct a dict representation of a ActionControlsRules model
        action_controls_rules_model = {}
        action_controls_rules_model['add'] = True
        action_controls_rules_model['remove'] = True

        # Construct a dict representation of a ActionControlsPolicies model
        action_controls_policies_model = {}
        action_controls_policies_model['add'] = True
        action_controls_policies_model['remove'] = True

        # Construct a dict representation of a ActionControls model
        action_controls_model = {}
        action_controls_model['identities'] = action_controls_identities_model
        action_controls_model['rules'] = action_controls_rules_model
        action_controls_model['policies'] = action_controls_policies_model

        # Set up parameter values
        template_id = 'testString'
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        profile = template_profile_component_request_model
        policy_template_references = [policy_template_reference_model]
        action_controls = action_controls_model

        # Invoke method
        response = _service.create_profile_template_version(
            template_id,
            account_id=account_id,
            name=name,
            description=description,
            profile=profile,
            policy_template_references=policy_template_references,
            action_controls=action_controls,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['profile'] == template_profile_component_request_model
        assert req_body['policy_template_references'] == [policy_template_reference_model]
        assert req_body['action_controls'] == action_controls_model

    def test_create_profile_template_version_all_params_with_retries(self):
        # Enable retries and run test_create_profile_template_version_all_params.
        _service.enable_retries()
        self.test_create_profile_template_version_all_params()

        # Disable retries and run test_create_profile_template_version_all_params.
        _service.disable_retries()
        self.test_create_profile_template_version_all_params()

    @responses.activate
    def test_create_profile_template_version_value_error(self):
        """
        test_create_profile_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a dict representation of a TrustedProfileTemplateClaimRule model
        trusted_profile_template_claim_rule_model = {}
        trusted_profile_template_claim_rule_model['name'] = 'testString'
        trusted_profile_template_claim_rule_model['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model['expiration'] = 38
        trusted_profile_template_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        # Construct a dict representation of a ProfileIdentityRequest model
        profile_identity_request_model = {}
        profile_identity_request_model['identifier'] = 'testString'
        profile_identity_request_model['type'] = 'user'
        profile_identity_request_model['accounts'] = ['testString']
        profile_identity_request_model['description'] = 'testString'

        # Construct a dict representation of a TemplateProfileComponentRequest model
        template_profile_component_request_model = {}
        template_profile_component_request_model['name'] = 'testString'
        template_profile_component_request_model['description'] = 'testString'
        template_profile_component_request_model['rules'] = [trusted_profile_template_claim_rule_model]
        template_profile_component_request_model['identities'] = [profile_identity_request_model]

        # Construct a dict representation of a PolicyTemplateReference model
        policy_template_reference_model = {}
        policy_template_reference_model['id'] = 'testString'
        policy_template_reference_model['version'] = 'testString'

        # Construct a dict representation of a ActionControlsIdentities model
        action_controls_identities_model = {}
        action_controls_identities_model['add'] = True
        action_controls_identities_model['remove'] = True

        # Construct a dict representation of a ActionControlsRules model
        action_controls_rules_model = {}
        action_controls_rules_model['add'] = True
        action_controls_rules_model['remove'] = True

        # Construct a dict representation of a ActionControlsPolicies model
        action_controls_policies_model = {}
        action_controls_policies_model['add'] = True
        action_controls_policies_model['remove'] = True

        # Construct a dict representation of a ActionControls model
        action_controls_model = {}
        action_controls_model['identities'] = action_controls_identities_model
        action_controls_model['rules'] = action_controls_rules_model
        action_controls_model['policies'] = action_controls_policies_model

        # Set up parameter values
        template_id = 'testString'
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        profile = template_profile_component_request_model
        policy_template_references = [policy_template_reference_model]
        action_controls = action_controls_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_profile_template_version(**req_copy)

    def test_create_profile_template_version_value_error_with_retries(self):
        # Enable retries and run test_create_profile_template_version_value_error.
        _service.enable_retries()
        self.test_create_profile_template_version_value_error()

        # Disable retries and run test_create_profile_template_version_value_error.
        _service.disable_retries()
        self.test_create_profile_template_version_value_error()


class TestGetProfileTemplateVersion:
    """
    Test Class for get_profile_template_version
    """

    @responses.activate
    def test_get_profile_template_version_all_params(self):
        """
        get_profile_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_profile_template_version(
            template_id,
            version,
            include_history=include_history,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string

    def test_get_profile_template_version_all_params_with_retries(self):
        # Enable retries and run test_get_profile_template_version_all_params.
        _service.enable_retries()
        self.test_get_profile_template_version_all_params()

        # Disable retries and run test_get_profile_template_version_all_params.
        _service.disable_retries()
        self.test_get_profile_template_version_all_params()

    @responses.activate
    def test_get_profile_template_version_required_params(self):
        """
        test_get_profile_template_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.get_profile_template_version(
            template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_template_version_required_params_with_retries(self):
        # Enable retries and run test_get_profile_template_version_required_params.
        _service.enable_retries()
        self.test_get_profile_template_version_required_params()

        # Disable retries and run test_get_profile_template_version_required_params.
        _service.disable_retries()
        self.test_get_profile_template_version_required_params()

    @responses.activate
    def test_get_profile_template_version_value_error(self):
        """
        test_get_profile_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_profile_template_version(**req_copy)

    def test_get_profile_template_version_value_error_with_retries(self):
        # Enable retries and run test_get_profile_template_version_value_error.
        _service.enable_retries()
        self.test_get_profile_template_version_value_error()

        # Disable retries and run test_get_profile_template_version_value_error.
        _service.disable_retries()
        self.test_get_profile_template_version_value_error()


class TestUpdateProfileTemplateVersion:
    """
    Test Class for update_profile_template_version
    """

    @responses.activate
    def test_update_profile_template_version_all_params(self):
        """
        update_profile_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a dict representation of a TrustedProfileTemplateClaimRule model
        trusted_profile_template_claim_rule_model = {}
        trusted_profile_template_claim_rule_model['name'] = 'testString'
        trusted_profile_template_claim_rule_model['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model['expiration'] = 38
        trusted_profile_template_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        # Construct a dict representation of a ProfileIdentityRequest model
        profile_identity_request_model = {}
        profile_identity_request_model['identifier'] = 'testString'
        profile_identity_request_model['type'] = 'user'
        profile_identity_request_model['accounts'] = ['testString']
        profile_identity_request_model['description'] = 'testString'

        # Construct a dict representation of a TemplateProfileComponentRequest model
        template_profile_component_request_model = {}
        template_profile_component_request_model['name'] = 'testString'
        template_profile_component_request_model['description'] = 'testString'
        template_profile_component_request_model['rules'] = [trusted_profile_template_claim_rule_model]
        template_profile_component_request_model['identities'] = [profile_identity_request_model]

        # Construct a dict representation of a PolicyTemplateReference model
        policy_template_reference_model = {}
        policy_template_reference_model['id'] = 'testString'
        policy_template_reference_model['version'] = 'testString'

        # Construct a dict representation of a ActionControlsIdentities model
        action_controls_identities_model = {}
        action_controls_identities_model['add'] = True
        action_controls_identities_model['remove'] = True

        # Construct a dict representation of a ActionControlsRules model
        action_controls_rules_model = {}
        action_controls_rules_model['add'] = True
        action_controls_rules_model['remove'] = True

        # Construct a dict representation of a ActionControlsPolicies model
        action_controls_policies_model = {}
        action_controls_policies_model['add'] = True
        action_controls_policies_model['remove'] = True

        # Construct a dict representation of a ActionControls model
        action_controls_model = {}
        action_controls_model['identities'] = action_controls_identities_model
        action_controls_model['rules'] = action_controls_rules_model
        action_controls_model['policies'] = action_controls_policies_model

        # Set up parameter values
        if_match = 'testString'
        template_id = 'testString'
        version = 'testString'
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        profile = template_profile_component_request_model
        policy_template_references = [policy_template_reference_model]
        action_controls = action_controls_model

        # Invoke method
        response = _service.update_profile_template_version(
            if_match,
            template_id,
            version,
            account_id=account_id,
            name=name,
            description=description,
            profile=profile,
            policy_template_references=policy_template_references,
            action_controls=action_controls,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['profile'] == template_profile_component_request_model
        assert req_body['policy_template_references'] == [policy_template_reference_model]
        assert req_body['action_controls'] == action_controls_model

    def test_update_profile_template_version_all_params_with_retries(self):
        # Enable retries and run test_update_profile_template_version_all_params.
        _service.enable_retries()
        self.test_update_profile_template_version_all_params()

        # Disable retries and run test_update_profile_template_version_all_params.
        _service.disable_retries()
        self.test_update_profile_template_version_all_params()

    @responses.activate
    def test_update_profile_template_version_value_error(self):
        """
        test_update_profile_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions/testString')
        mock_response = '{"id": "id", "version": 7, "account_id": "account_id", "name": "name", "description": "description", "committed": false, "profile": {"name": "name", "description": "description", "rules": [{"name": "name", "type": "Profile-SAML", "realm_name": "realm_name", "expiration": 10, "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}], "identities": [{"iam_id": "iam_id", "identifier": "identifier", "type": "user", "accounts": ["accounts"], "description": "description"}]}, "policy_template_references": [{"id": "id", "version": "version"}], "action_controls": {"identities": {"add": false, "remove": true}, "rules": {"add": false, "remove": true}, "policies": {"add": false, "remove": true}}, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "entity_tag": "entity_tag", "crn": "crn", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a dict representation of a TrustedProfileTemplateClaimRule model
        trusted_profile_template_claim_rule_model = {}
        trusted_profile_template_claim_rule_model['name'] = 'testString'
        trusted_profile_template_claim_rule_model['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model['expiration'] = 38
        trusted_profile_template_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        # Construct a dict representation of a ProfileIdentityRequest model
        profile_identity_request_model = {}
        profile_identity_request_model['identifier'] = 'testString'
        profile_identity_request_model['type'] = 'user'
        profile_identity_request_model['accounts'] = ['testString']
        profile_identity_request_model['description'] = 'testString'

        # Construct a dict representation of a TemplateProfileComponentRequest model
        template_profile_component_request_model = {}
        template_profile_component_request_model['name'] = 'testString'
        template_profile_component_request_model['description'] = 'testString'
        template_profile_component_request_model['rules'] = [trusted_profile_template_claim_rule_model]
        template_profile_component_request_model['identities'] = [profile_identity_request_model]

        # Construct a dict representation of a PolicyTemplateReference model
        policy_template_reference_model = {}
        policy_template_reference_model['id'] = 'testString'
        policy_template_reference_model['version'] = 'testString'

        # Construct a dict representation of a ActionControlsIdentities model
        action_controls_identities_model = {}
        action_controls_identities_model['add'] = True
        action_controls_identities_model['remove'] = True

        # Construct a dict representation of a ActionControlsRules model
        action_controls_rules_model = {}
        action_controls_rules_model['add'] = True
        action_controls_rules_model['remove'] = True

        # Construct a dict representation of a ActionControlsPolicies model
        action_controls_policies_model = {}
        action_controls_policies_model['add'] = True
        action_controls_policies_model['remove'] = True

        # Construct a dict representation of a ActionControls model
        action_controls_model = {}
        action_controls_model['identities'] = action_controls_identities_model
        action_controls_model['rules'] = action_controls_rules_model
        action_controls_model['policies'] = action_controls_policies_model

        # Set up parameter values
        if_match = 'testString'
        template_id = 'testString'
        version = 'testString'
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        profile = template_profile_component_request_model
        policy_template_references = [policy_template_reference_model]
        action_controls = action_controls_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "if_match": if_match,
            "template_id": template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_profile_template_version(**req_copy)

    def test_update_profile_template_version_value_error_with_retries(self):
        # Enable retries and run test_update_profile_template_version_value_error.
        _service.enable_retries()
        self.test_update_profile_template_version_value_error()

        # Disable retries and run test_update_profile_template_version_value_error.
        _service.disable_retries()
        self.test_update_profile_template_version_value_error()


class TestDeleteProfileTemplateVersion:
    """
    Test Class for delete_profile_template_version
    """

    @responses.activate
    def test_delete_profile_template_version_all_params(self):
        """
        delete_profile_template_version()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.delete_profile_template_version(
            template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_profile_template_version_all_params_with_retries(self):
        # Enable retries and run test_delete_profile_template_version_all_params.
        _service.enable_retries()
        self.test_delete_profile_template_version_all_params()

        # Disable retries and run test_delete_profile_template_version_all_params.
        _service.disable_retries()
        self.test_delete_profile_template_version_all_params()

    @responses.activate
    def test_delete_profile_template_version_value_error(self):
        """
        test_delete_profile_template_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_profile_template_version(**req_copy)

    def test_delete_profile_template_version_value_error_with_retries(self):
        # Enable retries and run test_delete_profile_template_version_value_error.
        _service.enable_retries()
        self.test_delete_profile_template_version_value_error()

        # Disable retries and run test_delete_profile_template_version_value_error.
        _service.disable_retries()
        self.test_delete_profile_template_version_value_error()


class TestCommitProfileTemplate:
    """
    Test Class for commit_profile_template
    """

    @responses.activate
    def test_commit_profile_template_all_params(self):
        """
        commit_profile_template()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Invoke method
        response = _service.commit_profile_template(
            template_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_commit_profile_template_all_params_with_retries(self):
        # Enable retries and run test_commit_profile_template_all_params.
        _service.enable_retries()
        self.test_commit_profile_template_all_params()

        # Disable retries and run test_commit_profile_template_all_params.
        _service.disable_retries()
        self.test_commit_profile_template_all_params()

    @responses.activate
    def test_commit_profile_template_value_error(self):
        """
        test_commit_profile_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/profile_templates/testString/versions/testString/commit')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        template_id = 'testString'
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "template_id": template_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.commit_profile_template(**req_copy)

    def test_commit_profile_template_value_error_with_retries(self):
        # Enable retries and run test_commit_profile_template_value_error.
        _service.enable_retries()
        self.test_commit_profile_template_value_error()

        # Disable retries and run test_commit_profile_template_value_error.
        _service.disable_retries()
        self.test_commit_profile_template_value_error()


# endregion
##############################################################################
# End of Service: TrustedProfileTemplate
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AccountBasedMfaEnrollment:
    """
    Test Class for AccountBasedMfaEnrollment
    """

    def test_account_based_mfa_enrollment_serialization(self):
        """
        Test serialization/deserialization for AccountBasedMfaEnrollment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mfa_enrollment_type_status_model = {}  # MfaEnrollmentTypeStatus
        mfa_enrollment_type_status_model['required'] = True
        mfa_enrollment_type_status_model['enrolled'] = True

        # Construct a json representation of a AccountBasedMfaEnrollment model
        account_based_mfa_enrollment_model_json = {}
        account_based_mfa_enrollment_model_json['security_questions'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model_json['totp'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model_json['verisign'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model_json['complies'] = True

        # Construct a model instance of AccountBasedMfaEnrollment by calling from_dict on the json representation
        account_based_mfa_enrollment_model = AccountBasedMfaEnrollment.from_dict(
            account_based_mfa_enrollment_model_json
        )
        assert account_based_mfa_enrollment_model != False

        # Construct a model instance of AccountBasedMfaEnrollment by calling from_dict on the json representation
        account_based_mfa_enrollment_model_dict = AccountBasedMfaEnrollment.from_dict(
            account_based_mfa_enrollment_model_json
        ).__dict__
        account_based_mfa_enrollment_model2 = AccountBasedMfaEnrollment(**account_based_mfa_enrollment_model_dict)

        # Verify the model instances are equivalent
        assert account_based_mfa_enrollment_model == account_based_mfa_enrollment_model2

        # Convert model instance back to dict and verify no loss of data
        account_based_mfa_enrollment_model_json2 = account_based_mfa_enrollment_model.to_dict()
        assert account_based_mfa_enrollment_model_json2 == account_based_mfa_enrollment_model_json


class TestModel_AccountSettingsAccountSection:
    """
    Test Class for AccountSettingsAccountSection
    """

    def test_account_settings_account_section_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsAccountSection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        effective_account_settings_user_mfa_model = {}  # EffectiveAccountSettingsUserMFA
        effective_account_settings_user_mfa_model['iam_id'] = 'testString'
        effective_account_settings_user_mfa_model['mfa'] = 'NONE'
        effective_account_settings_user_mfa_model['name'] = 'testString'
        effective_account_settings_user_mfa_model['userName'] = 'testString'
        effective_account_settings_user_mfa_model['email'] = 'testString'
        effective_account_settings_user_mfa_model['description'] = 'testString'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        # Construct a json representation of a AccountSettingsAccountSection model
        account_settings_account_section_model_json = {}
        account_settings_account_section_model_json['account_id'] = 'testString'
        account_settings_account_section_model_json['restrict_create_service_id'] = 'NOT_SET'
        account_settings_account_section_model_json['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_account_section_model_json['allowed_ip_addresses'] = 'testString'
        account_settings_account_section_model_json['mfa'] = 'NONE'
        account_settings_account_section_model_json['user_mfa'] = [effective_account_settings_user_mfa_model]
        account_settings_account_section_model_json['history'] = [enity_history_record_model]
        account_settings_account_section_model_json['session_expiration_in_seconds'] = '86400'
        account_settings_account_section_model_json['session_invalidation_in_seconds'] = '7200'
        account_settings_account_section_model_json['max_sessions_per_identity'] = 'testString'
        account_settings_account_section_model_json['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_account_section_model_json['system_refresh_token_expiration_in_seconds'] = '259200'

        # Construct a model instance of AccountSettingsAccountSection by calling from_dict on the json representation
        account_settings_account_section_model = AccountSettingsAccountSection.from_dict(
            account_settings_account_section_model_json
        )
        assert account_settings_account_section_model != False

        # Construct a model instance of AccountSettingsAccountSection by calling from_dict on the json representation
        account_settings_account_section_model_dict = AccountSettingsAccountSection.from_dict(
            account_settings_account_section_model_json
        ).__dict__
        account_settings_account_section_model2 = AccountSettingsAccountSection(
            **account_settings_account_section_model_dict
        )

        # Verify the model instances are equivalent
        assert account_settings_account_section_model == account_settings_account_section_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_account_section_model_json2 = account_settings_account_section_model.to_dict()
        assert account_settings_account_section_model_json2 == account_settings_account_section_model_json


class TestModel_AccountSettingsAssignedTemplatesSection:
    """
    Test Class for AccountSettingsAssignedTemplatesSection
    """

    def test_account_settings_assigned_templates_section_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsAssignedTemplatesSection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        effective_account_settings_user_mfa_model = {}  # EffectiveAccountSettingsUserMFA
        effective_account_settings_user_mfa_model['iam_id'] = 'testString'
        effective_account_settings_user_mfa_model['mfa'] = 'NONE'
        effective_account_settings_user_mfa_model['name'] = 'testString'
        effective_account_settings_user_mfa_model['userName'] = 'testString'
        effective_account_settings_user_mfa_model['email'] = 'testString'
        effective_account_settings_user_mfa_model['description'] = 'testString'

        # Construct a json representation of a AccountSettingsAssignedTemplatesSection model
        account_settings_assigned_templates_section_model_json = {}
        account_settings_assigned_templates_section_model_json['template_id'] = 'testString'
        account_settings_assigned_templates_section_model_json['template_version'] = 26
        account_settings_assigned_templates_section_model_json['template_name'] = 'testString'
        account_settings_assigned_templates_section_model_json['restrict_create_service_id'] = 'NOT_SET'
        account_settings_assigned_templates_section_model_json['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_assigned_templates_section_model_json['allowed_ip_addresses'] = 'testString'
        account_settings_assigned_templates_section_model_json['mfa'] = 'NONE'
        account_settings_assigned_templates_section_model_json['user_mfa'] = [effective_account_settings_user_mfa_model]
        account_settings_assigned_templates_section_model_json['session_expiration_in_seconds'] = '86400'
        account_settings_assigned_templates_section_model_json['session_invalidation_in_seconds'] = '7200'
        account_settings_assigned_templates_section_model_json['max_sessions_per_identity'] = 'testString'
        account_settings_assigned_templates_section_model_json['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_assigned_templates_section_model_json['system_refresh_token_expiration_in_seconds'] = '259200'

        # Construct a model instance of AccountSettingsAssignedTemplatesSection by calling from_dict on the json representation
        account_settings_assigned_templates_section_model = AccountSettingsAssignedTemplatesSection.from_dict(
            account_settings_assigned_templates_section_model_json
        )
        assert account_settings_assigned_templates_section_model != False

        # Construct a model instance of AccountSettingsAssignedTemplatesSection by calling from_dict on the json representation
        account_settings_assigned_templates_section_model_dict = AccountSettingsAssignedTemplatesSection.from_dict(
            account_settings_assigned_templates_section_model_json
        ).__dict__
        account_settings_assigned_templates_section_model2 = AccountSettingsAssignedTemplatesSection(
            **account_settings_assigned_templates_section_model_dict
        )

        # Verify the model instances are equivalent
        assert account_settings_assigned_templates_section_model == account_settings_assigned_templates_section_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_assigned_templates_section_model_json2 = (
            account_settings_assigned_templates_section_model.to_dict()
        )
        assert (
            account_settings_assigned_templates_section_model_json2
            == account_settings_assigned_templates_section_model_json
        )


class TestModel_AccountSettingsComponent:
    """
    Test Class for AccountSettingsComponent
    """

    def test_account_settings_component_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsComponent
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_settings_user_mfa_model = {}  # AccountSettingsUserMFA
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        # Construct a json representation of a AccountSettingsComponent model
        account_settings_component_model_json = {}
        account_settings_component_model_json['restrict_create_service_id'] = 'NOT_SET'
        account_settings_component_model_json['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_component_model_json['allowed_ip_addresses'] = 'testString'
        account_settings_component_model_json['mfa'] = 'NONE'
        account_settings_component_model_json['user_mfa'] = [account_settings_user_mfa_model]
        account_settings_component_model_json['session_expiration_in_seconds'] = '86400'
        account_settings_component_model_json['session_invalidation_in_seconds'] = '7200'
        account_settings_component_model_json['max_sessions_per_identity'] = 'testString'
        account_settings_component_model_json['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_component_model_json['system_refresh_token_expiration_in_seconds'] = '259200'

        # Construct a model instance of AccountSettingsComponent by calling from_dict on the json representation
        account_settings_component_model = AccountSettingsComponent.from_dict(account_settings_component_model_json)
        assert account_settings_component_model != False

        # Construct a model instance of AccountSettingsComponent by calling from_dict on the json representation
        account_settings_component_model_dict = AccountSettingsComponent.from_dict(
            account_settings_component_model_json
        ).__dict__
        account_settings_component_model2 = AccountSettingsComponent(**account_settings_component_model_dict)

        # Verify the model instances are equivalent
        assert account_settings_component_model == account_settings_component_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_component_model_json2 = account_settings_component_model.to_dict()
        assert account_settings_component_model_json2 == account_settings_component_model_json


class TestModel_AccountSettingsEffectiveSection:
    """
    Test Class for AccountSettingsEffectiveSection
    """

    def test_account_settings_effective_section_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsEffectiveSection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        effective_account_settings_user_mfa_model = {}  # EffectiveAccountSettingsUserMFA
        effective_account_settings_user_mfa_model['iam_id'] = 'testString'
        effective_account_settings_user_mfa_model['mfa'] = 'NONE'
        effective_account_settings_user_mfa_model['name'] = 'testString'
        effective_account_settings_user_mfa_model['userName'] = 'testString'
        effective_account_settings_user_mfa_model['email'] = 'testString'
        effective_account_settings_user_mfa_model['description'] = 'testString'

        # Construct a json representation of a AccountSettingsEffectiveSection model
        account_settings_effective_section_model_json = {}
        account_settings_effective_section_model_json['restrict_create_service_id'] = 'NOT_SET'
        account_settings_effective_section_model_json['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_effective_section_model_json['allowed_ip_addresses'] = 'testString'
        account_settings_effective_section_model_json['mfa'] = 'NONE'
        account_settings_effective_section_model_json['user_mfa'] = [effective_account_settings_user_mfa_model]
        account_settings_effective_section_model_json['session_expiration_in_seconds'] = '86400'
        account_settings_effective_section_model_json['session_invalidation_in_seconds'] = '7200'
        account_settings_effective_section_model_json['max_sessions_per_identity'] = 'testString'
        account_settings_effective_section_model_json['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_effective_section_model_json['system_refresh_token_expiration_in_seconds'] = '259200'

        # Construct a model instance of AccountSettingsEffectiveSection by calling from_dict on the json representation
        account_settings_effective_section_model = AccountSettingsEffectiveSection.from_dict(
            account_settings_effective_section_model_json
        )
        assert account_settings_effective_section_model != False

        # Construct a model instance of AccountSettingsEffectiveSection by calling from_dict on the json representation
        account_settings_effective_section_model_dict = AccountSettingsEffectiveSection.from_dict(
            account_settings_effective_section_model_json
        ).__dict__
        account_settings_effective_section_model2 = AccountSettingsEffectiveSection(
            **account_settings_effective_section_model_dict
        )

        # Verify the model instances are equivalent
        assert account_settings_effective_section_model == account_settings_effective_section_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_effective_section_model_json2 = account_settings_effective_section_model.to_dict()
        assert account_settings_effective_section_model_json2 == account_settings_effective_section_model_json


class TestModel_AccountSettingsResponse:
    """
    Test Class for AccountSettingsResponse
    """

    def test_account_settings_response_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        account_settings_user_mfa_model = {}  # AccountSettingsUserMFA
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        # Construct a json representation of a AccountSettingsResponse model
        account_settings_response_model_json = {}
        account_settings_response_model_json['context'] = response_context_model
        account_settings_response_model_json['account_id'] = 'testString'
        account_settings_response_model_json['restrict_create_service_id'] = 'NOT_SET'
        account_settings_response_model_json['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_response_model_json['allowed_ip_addresses'] = 'testString'
        account_settings_response_model_json['entity_tag'] = 'testString'
        account_settings_response_model_json['mfa'] = 'NONE'
        account_settings_response_model_json['user_mfa'] = [account_settings_user_mfa_model]
        account_settings_response_model_json['history'] = [enity_history_record_model]
        account_settings_response_model_json['session_expiration_in_seconds'] = '86400'
        account_settings_response_model_json['session_invalidation_in_seconds'] = '7200'
        account_settings_response_model_json['max_sessions_per_identity'] = 'testString'
        account_settings_response_model_json['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_response_model_json['system_refresh_token_expiration_in_seconds'] = '259200'

        # Construct a model instance of AccountSettingsResponse by calling from_dict on the json representation
        account_settings_response_model = AccountSettingsResponse.from_dict(account_settings_response_model_json)
        assert account_settings_response_model != False

        # Construct a model instance of AccountSettingsResponse by calling from_dict on the json representation
        account_settings_response_model_dict = AccountSettingsResponse.from_dict(
            account_settings_response_model_json
        ).__dict__
        account_settings_response_model2 = AccountSettingsResponse(**account_settings_response_model_dict)

        # Verify the model instances are equivalent
        assert account_settings_response_model == account_settings_response_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_response_model_json2 = account_settings_response_model.to_dict()
        assert account_settings_response_model_json2 == account_settings_response_model_json


class TestModel_AccountSettingsTemplateList:
    """
    Test Class for AccountSettingsTemplateList
    """

    def test_account_settings_template_list_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsTemplateList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        account_settings_user_mfa_model = {}  # AccountSettingsUserMFA
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        account_settings_component_model = {}  # AccountSettingsComponent
        account_settings_component_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_component_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_component_model['allowed_ip_addresses'] = 'testString'
        account_settings_component_model['mfa'] = 'NONE'
        account_settings_component_model['user_mfa'] = [account_settings_user_mfa_model]
        account_settings_component_model['session_expiration_in_seconds'] = '86400'
        account_settings_component_model['session_invalidation_in_seconds'] = '7200'
        account_settings_component_model['max_sessions_per_identity'] = 'testString'
        account_settings_component_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_component_model['system_refresh_token_expiration_in_seconds'] = '259200'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        account_settings_template_response_model = {}  # AccountSettingsTemplateResponse
        account_settings_template_response_model['id'] = 'testString'
        account_settings_template_response_model['version'] = 26
        account_settings_template_response_model['account_id'] = 'testString'
        account_settings_template_response_model['name'] = 'testString'
        account_settings_template_response_model['description'] = 'testString'
        account_settings_template_response_model['committed'] = True
        account_settings_template_response_model['account_settings'] = account_settings_component_model
        account_settings_template_response_model['history'] = [enity_history_record_model]
        account_settings_template_response_model['entity_tag'] = 'testString'
        account_settings_template_response_model['crn'] = 'testString'
        account_settings_template_response_model['created_at'] = 'testString'
        account_settings_template_response_model['created_by_id'] = 'testString'
        account_settings_template_response_model['last_modified_at'] = 'testString'
        account_settings_template_response_model['last_modified_by_id'] = 'testString'

        # Construct a json representation of a AccountSettingsTemplateList model
        account_settings_template_list_model_json = {}
        account_settings_template_list_model_json['context'] = response_context_model
        account_settings_template_list_model_json['offset'] = 26
        account_settings_template_list_model_json['limit'] = 20
        account_settings_template_list_model_json['first'] = 'testString'
        account_settings_template_list_model_json['previous'] = 'testString'
        account_settings_template_list_model_json['next'] = 'testString'
        account_settings_template_list_model_json['account_settings_templates'] = [
            account_settings_template_response_model
        ]

        # Construct a model instance of AccountSettingsTemplateList by calling from_dict on the json representation
        account_settings_template_list_model = AccountSettingsTemplateList.from_dict(
            account_settings_template_list_model_json
        )
        assert account_settings_template_list_model != False

        # Construct a model instance of AccountSettingsTemplateList by calling from_dict on the json representation
        account_settings_template_list_model_dict = AccountSettingsTemplateList.from_dict(
            account_settings_template_list_model_json
        ).__dict__
        account_settings_template_list_model2 = AccountSettingsTemplateList(**account_settings_template_list_model_dict)

        # Verify the model instances are equivalent
        assert account_settings_template_list_model == account_settings_template_list_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_template_list_model_json2 = account_settings_template_list_model.to_dict()
        assert account_settings_template_list_model_json2 == account_settings_template_list_model_json


class TestModel_AccountSettingsTemplateResponse:
    """
    Test Class for AccountSettingsTemplateResponse
    """

    def test_account_settings_template_response_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsTemplateResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_settings_user_mfa_model = {}  # AccountSettingsUserMFA
        account_settings_user_mfa_model['iam_id'] = 'testString'
        account_settings_user_mfa_model['mfa'] = 'NONE'

        account_settings_component_model = {}  # AccountSettingsComponent
        account_settings_component_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_component_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_component_model['allowed_ip_addresses'] = 'testString'
        account_settings_component_model['mfa'] = 'NONE'
        account_settings_component_model['user_mfa'] = [account_settings_user_mfa_model]
        account_settings_component_model['session_expiration_in_seconds'] = '86400'
        account_settings_component_model['session_invalidation_in_seconds'] = '7200'
        account_settings_component_model['max_sessions_per_identity'] = 'testString'
        account_settings_component_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_component_model['system_refresh_token_expiration_in_seconds'] = '259200'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        # Construct a json representation of a AccountSettingsTemplateResponse model
        account_settings_template_response_model_json = {}
        account_settings_template_response_model_json['id'] = 'testString'
        account_settings_template_response_model_json['version'] = 26
        account_settings_template_response_model_json['account_id'] = 'testString'
        account_settings_template_response_model_json['name'] = 'testString'
        account_settings_template_response_model_json['description'] = 'testString'
        account_settings_template_response_model_json['committed'] = True
        account_settings_template_response_model_json['account_settings'] = account_settings_component_model
        account_settings_template_response_model_json['history'] = [enity_history_record_model]
        account_settings_template_response_model_json['entity_tag'] = 'testString'
        account_settings_template_response_model_json['crn'] = 'testString'
        account_settings_template_response_model_json['created_at'] = 'testString'
        account_settings_template_response_model_json['created_by_id'] = 'testString'
        account_settings_template_response_model_json['last_modified_at'] = 'testString'
        account_settings_template_response_model_json['last_modified_by_id'] = 'testString'

        # Construct a model instance of AccountSettingsTemplateResponse by calling from_dict on the json representation
        account_settings_template_response_model = AccountSettingsTemplateResponse.from_dict(
            account_settings_template_response_model_json
        )
        assert account_settings_template_response_model != False

        # Construct a model instance of AccountSettingsTemplateResponse by calling from_dict on the json representation
        account_settings_template_response_model_dict = AccountSettingsTemplateResponse.from_dict(
            account_settings_template_response_model_json
        ).__dict__
        account_settings_template_response_model2 = AccountSettingsTemplateResponse(
            **account_settings_template_response_model_dict
        )

        # Verify the model instances are equivalent
        assert account_settings_template_response_model == account_settings_template_response_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_template_response_model_json2 = account_settings_template_response_model.to_dict()
        assert account_settings_template_response_model_json2 == account_settings_template_response_model_json


class TestModel_AccountSettingsUserMFA:
    """
    Test Class for AccountSettingsUserMFA
    """

    def test_account_settings_user_mfa_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsUserMFA
        """

        # Construct a json representation of a AccountSettingsUserMFA model
        account_settings_user_mfa_model_json = {}
        account_settings_user_mfa_model_json['iam_id'] = 'testString'
        account_settings_user_mfa_model_json['mfa'] = 'NONE'

        # Construct a model instance of AccountSettingsUserMFA by calling from_dict on the json representation
        account_settings_user_mfa_model = AccountSettingsUserMFA.from_dict(account_settings_user_mfa_model_json)
        assert account_settings_user_mfa_model != False

        # Construct a model instance of AccountSettingsUserMFA by calling from_dict on the json representation
        account_settings_user_mfa_model_dict = AccountSettingsUserMFA.from_dict(
            account_settings_user_mfa_model_json
        ).__dict__
        account_settings_user_mfa_model2 = AccountSettingsUserMFA(**account_settings_user_mfa_model_dict)

        # Verify the model instances are equivalent
        assert account_settings_user_mfa_model == account_settings_user_mfa_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_user_mfa_model_json2 = account_settings_user_mfa_model.to_dict()
        assert account_settings_user_mfa_model_json2 == account_settings_user_mfa_model_json


class TestModel_ActionControls:
    """
    Test Class for ActionControls
    """

    def test_action_controls_serialization(self):
        """
        Test serialization/deserialization for ActionControls
        """

        # Construct dict forms of any model objects needed in order to build this model.

        action_controls_identities_model = {}  # ActionControlsIdentities
        action_controls_identities_model['add'] = True
        action_controls_identities_model['remove'] = True

        action_controls_rules_model = {}  # ActionControlsRules
        action_controls_rules_model['add'] = True
        action_controls_rules_model['remove'] = True

        action_controls_policies_model = {}  # ActionControlsPolicies
        action_controls_policies_model['add'] = True
        action_controls_policies_model['remove'] = True

        # Construct a json representation of a ActionControls model
        action_controls_model_json = {}
        action_controls_model_json['identities'] = action_controls_identities_model
        action_controls_model_json['rules'] = action_controls_rules_model
        action_controls_model_json['policies'] = action_controls_policies_model

        # Construct a model instance of ActionControls by calling from_dict on the json representation
        action_controls_model = ActionControls.from_dict(action_controls_model_json)
        assert action_controls_model != False

        # Construct a model instance of ActionControls by calling from_dict on the json representation
        action_controls_model_dict = ActionControls.from_dict(action_controls_model_json).__dict__
        action_controls_model2 = ActionControls(**action_controls_model_dict)

        # Verify the model instances are equivalent
        assert action_controls_model == action_controls_model2

        # Convert model instance back to dict and verify no loss of data
        action_controls_model_json2 = action_controls_model.to_dict()
        assert action_controls_model_json2 == action_controls_model_json


class TestModel_ActionControlsIdentities:
    """
    Test Class for ActionControlsIdentities
    """

    def test_action_controls_identities_serialization(self):
        """
        Test serialization/deserialization for ActionControlsIdentities
        """

        # Construct a json representation of a ActionControlsIdentities model
        action_controls_identities_model_json = {}
        action_controls_identities_model_json['add'] = True
        action_controls_identities_model_json['remove'] = True

        # Construct a model instance of ActionControlsIdentities by calling from_dict on the json representation
        action_controls_identities_model = ActionControlsIdentities.from_dict(action_controls_identities_model_json)
        assert action_controls_identities_model != False

        # Construct a model instance of ActionControlsIdentities by calling from_dict on the json representation
        action_controls_identities_model_dict = ActionControlsIdentities.from_dict(
            action_controls_identities_model_json
        ).__dict__
        action_controls_identities_model2 = ActionControlsIdentities(**action_controls_identities_model_dict)

        # Verify the model instances are equivalent
        assert action_controls_identities_model == action_controls_identities_model2

        # Convert model instance back to dict and verify no loss of data
        action_controls_identities_model_json2 = action_controls_identities_model.to_dict()
        assert action_controls_identities_model_json2 == action_controls_identities_model_json


class TestModel_ActionControlsPolicies:
    """
    Test Class for ActionControlsPolicies
    """

    def test_action_controls_policies_serialization(self):
        """
        Test serialization/deserialization for ActionControlsPolicies
        """

        # Construct a json representation of a ActionControlsPolicies model
        action_controls_policies_model_json = {}
        action_controls_policies_model_json['add'] = True
        action_controls_policies_model_json['remove'] = True

        # Construct a model instance of ActionControlsPolicies by calling from_dict on the json representation
        action_controls_policies_model = ActionControlsPolicies.from_dict(action_controls_policies_model_json)
        assert action_controls_policies_model != False

        # Construct a model instance of ActionControlsPolicies by calling from_dict on the json representation
        action_controls_policies_model_dict = ActionControlsPolicies.from_dict(
            action_controls_policies_model_json
        ).__dict__
        action_controls_policies_model2 = ActionControlsPolicies(**action_controls_policies_model_dict)

        # Verify the model instances are equivalent
        assert action_controls_policies_model == action_controls_policies_model2

        # Convert model instance back to dict and verify no loss of data
        action_controls_policies_model_json2 = action_controls_policies_model.to_dict()
        assert action_controls_policies_model_json2 == action_controls_policies_model_json


class TestModel_ActionControlsRules:
    """
    Test Class for ActionControlsRules
    """

    def test_action_controls_rules_serialization(self):
        """
        Test serialization/deserialization for ActionControlsRules
        """

        # Construct a json representation of a ActionControlsRules model
        action_controls_rules_model_json = {}
        action_controls_rules_model_json['add'] = True
        action_controls_rules_model_json['remove'] = True

        # Construct a model instance of ActionControlsRules by calling from_dict on the json representation
        action_controls_rules_model = ActionControlsRules.from_dict(action_controls_rules_model_json)
        assert action_controls_rules_model != False

        # Construct a model instance of ActionControlsRules by calling from_dict on the json representation
        action_controls_rules_model_dict = ActionControlsRules.from_dict(action_controls_rules_model_json).__dict__
        action_controls_rules_model2 = ActionControlsRules(**action_controls_rules_model_dict)

        # Verify the model instances are equivalent
        assert action_controls_rules_model == action_controls_rules_model2

        # Convert model instance back to dict and verify no loss of data
        action_controls_rules_model_json2 = action_controls_rules_model.to_dict()
        assert action_controls_rules_model_json2 == action_controls_rules_model_json


class TestModel_Activity:
    """
    Test Class for Activity
    """

    def test_activity_serialization(self):
        """
        Test serialization/deserialization for Activity
        """

        # Construct a json representation of a Activity model
        activity_model_json = {}
        activity_model_json['last_authn'] = 'testString'
        activity_model_json['authn_count'] = 26

        # Construct a model instance of Activity by calling from_dict on the json representation
        activity_model = Activity.from_dict(activity_model_json)
        assert activity_model != False

        # Construct a model instance of Activity by calling from_dict on the json representation
        activity_model_dict = Activity.from_dict(activity_model_json).__dict__
        activity_model2 = Activity(**activity_model_dict)

        # Verify the model instances are equivalent
        assert activity_model == activity_model2

        # Convert model instance back to dict and verify no loss of data
        activity_model_json2 = activity_model.to_dict()
        assert activity_model_json2 == activity_model_json


class TestModel_ApiKey:
    """
    Test Class for ApiKey
    """

    def test_api_key_serialization(self):
        """
        Test serialization/deserialization for ApiKey
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        activity_model = {}  # Activity
        activity_model['last_authn'] = 'testString'
        activity_model['authn_count'] = 26

        # Construct a json representation of a ApiKey model
        api_key_model_json = {}
        api_key_model_json['context'] = response_context_model
        api_key_model_json['id'] = 'testString'
        api_key_model_json['entity_tag'] = 'testString'
        api_key_model_json['crn'] = 'testString'
        api_key_model_json['locked'] = True
        api_key_model_json['disabled'] = True
        api_key_model_json['created_at'] = '2019-01-01T12:00:00Z'
        api_key_model_json['created_by'] = 'testString'
        api_key_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        api_key_model_json['name'] = 'testString'
        api_key_model_json['support_sessions'] = True
        api_key_model_json['action_when_leaked'] = 'testString'
        api_key_model_json['description'] = 'testString'
        api_key_model_json['iam_id'] = 'testString'
        api_key_model_json['account_id'] = 'testString'
        api_key_model_json['apikey'] = 'testString'
        api_key_model_json['history'] = [enity_history_record_model]
        api_key_model_json['activity'] = activity_model

        # Construct a model instance of ApiKey by calling from_dict on the json representation
        api_key_model = ApiKey.from_dict(api_key_model_json)
        assert api_key_model != False

        # Construct a model instance of ApiKey by calling from_dict on the json representation
        api_key_model_dict = ApiKey.from_dict(api_key_model_json).__dict__
        api_key_model2 = ApiKey(**api_key_model_dict)

        # Verify the model instances are equivalent
        assert api_key_model == api_key_model2

        # Convert model instance back to dict and verify no loss of data
        api_key_model_json2 = api_key_model.to_dict()
        assert api_key_model_json2 == api_key_model_json


class TestModel_ApiKeyInsideCreateServiceIdRequest:
    """
    Test Class for ApiKeyInsideCreateServiceIdRequest
    """

    def test_api_key_inside_create_service_id_request_serialization(self):
        """
        Test serialization/deserialization for ApiKeyInsideCreateServiceIdRequest
        """

        # Construct a json representation of a ApiKeyInsideCreateServiceIdRequest model
        api_key_inside_create_service_id_request_model_json = {}
        api_key_inside_create_service_id_request_model_json['name'] = 'testString'
        api_key_inside_create_service_id_request_model_json['description'] = 'testString'
        api_key_inside_create_service_id_request_model_json['apikey'] = 'testString'
        api_key_inside_create_service_id_request_model_json['store_value'] = True

        # Construct a model instance of ApiKeyInsideCreateServiceIdRequest by calling from_dict on the json representation
        api_key_inside_create_service_id_request_model = ApiKeyInsideCreateServiceIdRequest.from_dict(
            api_key_inside_create_service_id_request_model_json
        )
        assert api_key_inside_create_service_id_request_model != False

        # Construct a model instance of ApiKeyInsideCreateServiceIdRequest by calling from_dict on the json representation
        api_key_inside_create_service_id_request_model_dict = ApiKeyInsideCreateServiceIdRequest.from_dict(
            api_key_inside_create_service_id_request_model_json
        ).__dict__
        api_key_inside_create_service_id_request_model2 = ApiKeyInsideCreateServiceIdRequest(
            **api_key_inside_create_service_id_request_model_dict
        )

        # Verify the model instances are equivalent
        assert api_key_inside_create_service_id_request_model == api_key_inside_create_service_id_request_model2

        # Convert model instance back to dict and verify no loss of data
        api_key_inside_create_service_id_request_model_json2 = api_key_inside_create_service_id_request_model.to_dict()
        assert (
            api_key_inside_create_service_id_request_model_json2 == api_key_inside_create_service_id_request_model_json
        )


class TestModel_ApiKeyList:
    """
    Test Class for ApiKeyList
    """

    def test_api_key_list_serialization(self):
        """
        Test serialization/deserialization for ApiKeyList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        activity_model = {}  # Activity
        activity_model['last_authn'] = 'testString'
        activity_model['authn_count'] = 26

        api_key_model = {}  # ApiKey
        api_key_model['context'] = response_context_model
        api_key_model['id'] = 'testString'
        api_key_model['entity_tag'] = 'testString'
        api_key_model['crn'] = 'testString'
        api_key_model['locked'] = True
        api_key_model['disabled'] = True
        api_key_model['created_at'] = '2019-01-01T12:00:00Z'
        api_key_model['created_by'] = 'testString'
        api_key_model['modified_at'] = '2019-01-01T12:00:00Z'
        api_key_model['name'] = 'testString'
        api_key_model['support_sessions'] = True
        api_key_model['action_when_leaked'] = 'testString'
        api_key_model['description'] = 'testString'
        api_key_model['iam_id'] = 'testString'
        api_key_model['account_id'] = 'testString'
        api_key_model['apikey'] = 'testString'
        api_key_model['history'] = [enity_history_record_model]
        api_key_model['activity'] = activity_model

        # Construct a json representation of a ApiKeyList model
        api_key_list_model_json = {}
        api_key_list_model_json['context'] = response_context_model
        api_key_list_model_json['offset'] = 26
        api_key_list_model_json['limit'] = 26
        api_key_list_model_json['first'] = 'testString'
        api_key_list_model_json['previous'] = 'testString'
        api_key_list_model_json['next'] = 'testString'
        api_key_list_model_json['apikeys'] = [api_key_model]

        # Construct a model instance of ApiKeyList by calling from_dict on the json representation
        api_key_list_model = ApiKeyList.from_dict(api_key_list_model_json)
        assert api_key_list_model != False

        # Construct a model instance of ApiKeyList by calling from_dict on the json representation
        api_key_list_model_dict = ApiKeyList.from_dict(api_key_list_model_json).__dict__
        api_key_list_model2 = ApiKeyList(**api_key_list_model_dict)

        # Verify the model instances are equivalent
        assert api_key_list_model == api_key_list_model2

        # Convert model instance back to dict and verify no loss of data
        api_key_list_model_json2 = api_key_list_model.to_dict()
        assert api_key_list_model_json2 == api_key_list_model_json


class TestModel_ApikeyActivity:
    """
    Test Class for ApikeyActivity
    """

    def test_apikey_activity_serialization(self):
        """
        Test serialization/deserialization for ApikeyActivity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        apikey_activity_serviceid_model = {}  # ApikeyActivityServiceid
        apikey_activity_serviceid_model['id'] = 'testString'
        apikey_activity_serviceid_model['name'] = 'testString'

        apikey_activity_user_model = {}  # ApikeyActivityUser
        apikey_activity_user_model['iam_id'] = 'testString'
        apikey_activity_user_model['name'] = 'testString'
        apikey_activity_user_model['username'] = 'testString'
        apikey_activity_user_model['email'] = 'testString'

        # Construct a json representation of a ApikeyActivity model
        apikey_activity_model_json = {}
        apikey_activity_model_json['id'] = 'testString'
        apikey_activity_model_json['name'] = 'testString'
        apikey_activity_model_json['type'] = 'testString'
        apikey_activity_model_json['serviceid'] = apikey_activity_serviceid_model
        apikey_activity_model_json['user'] = apikey_activity_user_model
        apikey_activity_model_json['last_authn'] = 'testString'

        # Construct a model instance of ApikeyActivity by calling from_dict on the json representation
        apikey_activity_model = ApikeyActivity.from_dict(apikey_activity_model_json)
        assert apikey_activity_model != False

        # Construct a model instance of ApikeyActivity by calling from_dict on the json representation
        apikey_activity_model_dict = ApikeyActivity.from_dict(apikey_activity_model_json).__dict__
        apikey_activity_model2 = ApikeyActivity(**apikey_activity_model_dict)

        # Verify the model instances are equivalent
        assert apikey_activity_model == apikey_activity_model2

        # Convert model instance back to dict and verify no loss of data
        apikey_activity_model_json2 = apikey_activity_model.to_dict()
        assert apikey_activity_model_json2 == apikey_activity_model_json


class TestModel_ApikeyActivityServiceid:
    """
    Test Class for ApikeyActivityServiceid
    """

    def test_apikey_activity_serviceid_serialization(self):
        """
        Test serialization/deserialization for ApikeyActivityServiceid
        """

        # Construct a json representation of a ApikeyActivityServiceid model
        apikey_activity_serviceid_model_json = {}
        apikey_activity_serviceid_model_json['id'] = 'testString'
        apikey_activity_serviceid_model_json['name'] = 'testString'

        # Construct a model instance of ApikeyActivityServiceid by calling from_dict on the json representation
        apikey_activity_serviceid_model = ApikeyActivityServiceid.from_dict(apikey_activity_serviceid_model_json)
        assert apikey_activity_serviceid_model != False

        # Construct a model instance of ApikeyActivityServiceid by calling from_dict on the json representation
        apikey_activity_serviceid_model_dict = ApikeyActivityServiceid.from_dict(
            apikey_activity_serviceid_model_json
        ).__dict__
        apikey_activity_serviceid_model2 = ApikeyActivityServiceid(**apikey_activity_serviceid_model_dict)

        # Verify the model instances are equivalent
        assert apikey_activity_serviceid_model == apikey_activity_serviceid_model2

        # Convert model instance back to dict and verify no loss of data
        apikey_activity_serviceid_model_json2 = apikey_activity_serviceid_model.to_dict()
        assert apikey_activity_serviceid_model_json2 == apikey_activity_serviceid_model_json


class TestModel_ApikeyActivityUser:
    """
    Test Class for ApikeyActivityUser
    """

    def test_apikey_activity_user_serialization(self):
        """
        Test serialization/deserialization for ApikeyActivityUser
        """

        # Construct a json representation of a ApikeyActivityUser model
        apikey_activity_user_model_json = {}
        apikey_activity_user_model_json['iam_id'] = 'testString'
        apikey_activity_user_model_json['name'] = 'testString'
        apikey_activity_user_model_json['username'] = 'testString'
        apikey_activity_user_model_json['email'] = 'testString'

        # Construct a model instance of ApikeyActivityUser by calling from_dict on the json representation
        apikey_activity_user_model = ApikeyActivityUser.from_dict(apikey_activity_user_model_json)
        assert apikey_activity_user_model != False

        # Construct a model instance of ApikeyActivityUser by calling from_dict on the json representation
        apikey_activity_user_model_dict = ApikeyActivityUser.from_dict(apikey_activity_user_model_json).__dict__
        apikey_activity_user_model2 = ApikeyActivityUser(**apikey_activity_user_model_dict)

        # Verify the model instances are equivalent
        assert apikey_activity_user_model == apikey_activity_user_model2

        # Convert model instance back to dict and verify no loss of data
        apikey_activity_user_model_json2 = apikey_activity_user_model.to_dict()
        assert apikey_activity_user_model_json2 == apikey_activity_user_model_json


class TestModel_CreateProfileLinkRequestLink:
    """
    Test Class for CreateProfileLinkRequestLink
    """

    def test_create_profile_link_request_link_serialization(self):
        """
        Test serialization/deserialization for CreateProfileLinkRequestLink
        """

        # Construct a json representation of a CreateProfileLinkRequestLink model
        create_profile_link_request_link_model_json = {}
        create_profile_link_request_link_model_json['crn'] = 'testString'
        create_profile_link_request_link_model_json['namespace'] = 'testString'
        create_profile_link_request_link_model_json['name'] = 'testString'

        # Construct a model instance of CreateProfileLinkRequestLink by calling from_dict on the json representation
        create_profile_link_request_link_model = CreateProfileLinkRequestLink.from_dict(
            create_profile_link_request_link_model_json
        )
        assert create_profile_link_request_link_model != False

        # Construct a model instance of CreateProfileLinkRequestLink by calling from_dict on the json representation
        create_profile_link_request_link_model_dict = CreateProfileLinkRequestLink.from_dict(
            create_profile_link_request_link_model_json
        ).__dict__
        create_profile_link_request_link_model2 = CreateProfileLinkRequestLink(
            **create_profile_link_request_link_model_dict
        )

        # Verify the model instances are equivalent
        assert create_profile_link_request_link_model == create_profile_link_request_link_model2

        # Convert model instance back to dict and verify no loss of data
        create_profile_link_request_link_model_json2 = create_profile_link_request_link_model.to_dict()
        assert create_profile_link_request_link_model_json2 == create_profile_link_request_link_model_json


class TestModel_EffectiveAccountSettingsResponse:
    """
    Test Class for EffectiveAccountSettingsResponse
    """

    def test_effective_account_settings_response_serialization(self):
        """
        Test serialization/deserialization for EffectiveAccountSettingsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        effective_account_settings_user_mfa_model = {}  # EffectiveAccountSettingsUserMFA
        effective_account_settings_user_mfa_model['iam_id'] = 'testString'
        effective_account_settings_user_mfa_model['mfa'] = 'NONE'
        effective_account_settings_user_mfa_model['name'] = 'testString'
        effective_account_settings_user_mfa_model['userName'] = 'testString'
        effective_account_settings_user_mfa_model['email'] = 'testString'
        effective_account_settings_user_mfa_model['description'] = 'testString'

        account_settings_effective_section_model = {}  # AccountSettingsEffectiveSection
        account_settings_effective_section_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_effective_section_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_effective_section_model['allowed_ip_addresses'] = 'testString'
        account_settings_effective_section_model['mfa'] = 'NONE'
        account_settings_effective_section_model['user_mfa'] = [effective_account_settings_user_mfa_model]
        account_settings_effective_section_model['session_expiration_in_seconds'] = '86400'
        account_settings_effective_section_model['session_invalidation_in_seconds'] = '7200'
        account_settings_effective_section_model['max_sessions_per_identity'] = 'testString'
        account_settings_effective_section_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_effective_section_model['system_refresh_token_expiration_in_seconds'] = '259200'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        account_settings_account_section_model = {}  # AccountSettingsAccountSection
        account_settings_account_section_model['account_id'] = 'testString'
        account_settings_account_section_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_account_section_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_account_section_model['allowed_ip_addresses'] = 'testString'
        account_settings_account_section_model['mfa'] = 'NONE'
        account_settings_account_section_model['user_mfa'] = [effective_account_settings_user_mfa_model]
        account_settings_account_section_model['history'] = [enity_history_record_model]
        account_settings_account_section_model['session_expiration_in_seconds'] = '86400'
        account_settings_account_section_model['session_invalidation_in_seconds'] = '7200'
        account_settings_account_section_model['max_sessions_per_identity'] = 'testString'
        account_settings_account_section_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_account_section_model['system_refresh_token_expiration_in_seconds'] = '259200'

        account_settings_assigned_templates_section_model = {}  # AccountSettingsAssignedTemplatesSection
        account_settings_assigned_templates_section_model['template_id'] = 'testString'
        account_settings_assigned_templates_section_model['template_version'] = 26
        account_settings_assigned_templates_section_model['template_name'] = 'testString'
        account_settings_assigned_templates_section_model['restrict_create_service_id'] = 'NOT_SET'
        account_settings_assigned_templates_section_model['restrict_create_platform_apikey'] = 'NOT_SET'
        account_settings_assigned_templates_section_model['allowed_ip_addresses'] = 'testString'
        account_settings_assigned_templates_section_model['mfa'] = 'NONE'
        account_settings_assigned_templates_section_model['user_mfa'] = [effective_account_settings_user_mfa_model]
        account_settings_assigned_templates_section_model['session_expiration_in_seconds'] = '86400'
        account_settings_assigned_templates_section_model['session_invalidation_in_seconds'] = '7200'
        account_settings_assigned_templates_section_model['max_sessions_per_identity'] = 'testString'
        account_settings_assigned_templates_section_model['system_access_token_expiration_in_seconds'] = '3600'
        account_settings_assigned_templates_section_model['system_refresh_token_expiration_in_seconds'] = '259200'

        # Construct a json representation of a EffectiveAccountSettingsResponse model
        effective_account_settings_response_model_json = {}
        effective_account_settings_response_model_json['context'] = response_context_model
        effective_account_settings_response_model_json['account_id'] = 'testString'
        effective_account_settings_response_model_json['effective'] = account_settings_effective_section_model
        effective_account_settings_response_model_json['account'] = account_settings_account_section_model
        effective_account_settings_response_model_json['assigned_templates'] = [
            account_settings_assigned_templates_section_model
        ]

        # Construct a model instance of EffectiveAccountSettingsResponse by calling from_dict on the json representation
        effective_account_settings_response_model = EffectiveAccountSettingsResponse.from_dict(
            effective_account_settings_response_model_json
        )
        assert effective_account_settings_response_model != False

        # Construct a model instance of EffectiveAccountSettingsResponse by calling from_dict on the json representation
        effective_account_settings_response_model_dict = EffectiveAccountSettingsResponse.from_dict(
            effective_account_settings_response_model_json
        ).__dict__
        effective_account_settings_response_model2 = EffectiveAccountSettingsResponse(
            **effective_account_settings_response_model_dict
        )

        # Verify the model instances are equivalent
        assert effective_account_settings_response_model == effective_account_settings_response_model2

        # Convert model instance back to dict and verify no loss of data
        effective_account_settings_response_model_json2 = effective_account_settings_response_model.to_dict()
        assert effective_account_settings_response_model_json2 == effective_account_settings_response_model_json


class TestModel_EffectiveAccountSettingsUserMFA:
    """
    Test Class for EffectiveAccountSettingsUserMFA
    """

    def test_effective_account_settings_user_mfa_serialization(self):
        """
        Test serialization/deserialization for EffectiveAccountSettingsUserMFA
        """

        # Construct a json representation of a EffectiveAccountSettingsUserMFA model
        effective_account_settings_user_mfa_model_json = {}
        effective_account_settings_user_mfa_model_json['iam_id'] = 'testString'
        effective_account_settings_user_mfa_model_json['mfa'] = 'NONE'
        effective_account_settings_user_mfa_model_json['name'] = 'testString'
        effective_account_settings_user_mfa_model_json['userName'] = 'testString'
        effective_account_settings_user_mfa_model_json['email'] = 'testString'
        effective_account_settings_user_mfa_model_json['description'] = 'testString'

        # Construct a model instance of EffectiveAccountSettingsUserMFA by calling from_dict on the json representation
        effective_account_settings_user_mfa_model = EffectiveAccountSettingsUserMFA.from_dict(
            effective_account_settings_user_mfa_model_json
        )
        assert effective_account_settings_user_mfa_model != False

        # Construct a model instance of EffectiveAccountSettingsUserMFA by calling from_dict on the json representation
        effective_account_settings_user_mfa_model_dict = EffectiveAccountSettingsUserMFA.from_dict(
            effective_account_settings_user_mfa_model_json
        ).__dict__
        effective_account_settings_user_mfa_model2 = EffectiveAccountSettingsUserMFA(
            **effective_account_settings_user_mfa_model_dict
        )

        # Verify the model instances are equivalent
        assert effective_account_settings_user_mfa_model == effective_account_settings_user_mfa_model2

        # Convert model instance back to dict and verify no loss of data
        effective_account_settings_user_mfa_model_json2 = effective_account_settings_user_mfa_model.to_dict()
        assert effective_account_settings_user_mfa_model_json2 == effective_account_settings_user_mfa_model_json


class TestModel_EnityHistoryRecord:
    """
    Test Class for EnityHistoryRecord
    """

    def test_enity_history_record_serialization(self):
        """
        Test serialization/deserialization for EnityHistoryRecord
        """

        # Construct a json representation of a EnityHistoryRecord model
        enity_history_record_model_json = {}
        enity_history_record_model_json['timestamp'] = 'testString'
        enity_history_record_model_json['iam_id'] = 'testString'
        enity_history_record_model_json['iam_id_account'] = 'testString'
        enity_history_record_model_json['action'] = 'testString'
        enity_history_record_model_json['params'] = ['testString']
        enity_history_record_model_json['message'] = 'testString'

        # Construct a model instance of EnityHistoryRecord by calling from_dict on the json representation
        enity_history_record_model = EnityHistoryRecord.from_dict(enity_history_record_model_json)
        assert enity_history_record_model != False

        # Construct a model instance of EnityHistoryRecord by calling from_dict on the json representation
        enity_history_record_model_dict = EnityHistoryRecord.from_dict(enity_history_record_model_json).__dict__
        enity_history_record_model2 = EnityHistoryRecord(**enity_history_record_model_dict)

        # Verify the model instances are equivalent
        assert enity_history_record_model == enity_history_record_model2

        # Convert model instance back to dict and verify no loss of data
        enity_history_record_model_json2 = enity_history_record_model.to_dict()
        assert enity_history_record_model_json2 == enity_history_record_model_json


class TestModel_EntityActivity:
    """
    Test Class for EntityActivity
    """

    def test_entity_activity_serialization(self):
        """
        Test serialization/deserialization for EntityActivity
        """

        # Construct a json representation of a EntityActivity model
        entity_activity_model_json = {}
        entity_activity_model_json['id'] = 'testString'
        entity_activity_model_json['name'] = 'testString'
        entity_activity_model_json['last_authn'] = 'testString'

        # Construct a model instance of EntityActivity by calling from_dict on the json representation
        entity_activity_model = EntityActivity.from_dict(entity_activity_model_json)
        assert entity_activity_model != False

        # Construct a model instance of EntityActivity by calling from_dict on the json representation
        entity_activity_model_dict = EntityActivity.from_dict(entity_activity_model_json).__dict__
        entity_activity_model2 = EntityActivity(**entity_activity_model_dict)

        # Verify the model instances are equivalent
        assert entity_activity_model == entity_activity_model2

        # Convert model instance back to dict and verify no loss of data
        entity_activity_model_json2 = entity_activity_model.to_dict()
        assert entity_activity_model_json2 == entity_activity_model_json


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
        error_model_json['message_code'] = 'testString'
        error_model_json['message'] = 'testString'
        error_model_json['details'] = 'testString'

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


class TestModel_ExceptionResponse:
    """
    Test Class for ExceptionResponse
    """

    def test_exception_response_serialization(self):
        """
        Test serialization/deserialization for ExceptionResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        error_model = {}  # Error
        error_model['code'] = 'testString'
        error_model['message_code'] = 'testString'
        error_model['message'] = 'testString'
        error_model['details'] = 'testString'

        # Construct a json representation of a ExceptionResponse model
        exception_response_model_json = {}
        exception_response_model_json['context'] = response_context_model
        exception_response_model_json['status_code'] = 'testString'
        exception_response_model_json['errors'] = [error_model]
        exception_response_model_json['trace'] = 'testString'

        # Construct a model instance of ExceptionResponse by calling from_dict on the json representation
        exception_response_model = ExceptionResponse.from_dict(exception_response_model_json)
        assert exception_response_model != False

        # Construct a model instance of ExceptionResponse by calling from_dict on the json representation
        exception_response_model_dict = ExceptionResponse.from_dict(exception_response_model_json).__dict__
        exception_response_model2 = ExceptionResponse(**exception_response_model_dict)

        # Verify the model instances are equivalent
        assert exception_response_model == exception_response_model2

        # Convert model instance back to dict and verify no loss of data
        exception_response_model_json2 = exception_response_model.to_dict()
        assert exception_response_model_json2 == exception_response_model_json


class TestModel_IdBasedMfaEnrollment:
    """
    Test Class for IdBasedMfaEnrollment
    """

    def test_id_based_mfa_enrollment_serialization(self):
        """
        Test serialization/deserialization for IdBasedMfaEnrollment
        """

        # Construct a json representation of a IdBasedMfaEnrollment model
        id_based_mfa_enrollment_model_json = {}
        id_based_mfa_enrollment_model_json['trait_account_default'] = 'NONE'
        id_based_mfa_enrollment_model_json['trait_user_specific'] = 'NONE'
        id_based_mfa_enrollment_model_json['trait_effective'] = 'NONE'
        id_based_mfa_enrollment_model_json['complies'] = True
        id_based_mfa_enrollment_model_json['comply_state'] = 'NO'

        # Construct a model instance of IdBasedMfaEnrollment by calling from_dict on the json representation
        id_based_mfa_enrollment_model = IdBasedMfaEnrollment.from_dict(id_based_mfa_enrollment_model_json)
        assert id_based_mfa_enrollment_model != False

        # Construct a model instance of IdBasedMfaEnrollment by calling from_dict on the json representation
        id_based_mfa_enrollment_model_dict = IdBasedMfaEnrollment.from_dict(id_based_mfa_enrollment_model_json).__dict__
        id_based_mfa_enrollment_model2 = IdBasedMfaEnrollment(**id_based_mfa_enrollment_model_dict)

        # Verify the model instances are equivalent
        assert id_based_mfa_enrollment_model == id_based_mfa_enrollment_model2

        # Convert model instance back to dict and verify no loss of data
        id_based_mfa_enrollment_model_json2 = id_based_mfa_enrollment_model.to_dict()
        assert id_based_mfa_enrollment_model_json2 == id_based_mfa_enrollment_model_json


class TestModel_MfaEnrollmentTypeStatus:
    """
    Test Class for MfaEnrollmentTypeStatus
    """

    def test_mfa_enrollment_type_status_serialization(self):
        """
        Test serialization/deserialization for MfaEnrollmentTypeStatus
        """

        # Construct a json representation of a MfaEnrollmentTypeStatus model
        mfa_enrollment_type_status_model_json = {}
        mfa_enrollment_type_status_model_json['required'] = True
        mfa_enrollment_type_status_model_json['enrolled'] = True

        # Construct a model instance of MfaEnrollmentTypeStatus by calling from_dict on the json representation
        mfa_enrollment_type_status_model = MfaEnrollmentTypeStatus.from_dict(mfa_enrollment_type_status_model_json)
        assert mfa_enrollment_type_status_model != False

        # Construct a model instance of MfaEnrollmentTypeStatus by calling from_dict on the json representation
        mfa_enrollment_type_status_model_dict = MfaEnrollmentTypeStatus.from_dict(
            mfa_enrollment_type_status_model_json
        ).__dict__
        mfa_enrollment_type_status_model2 = MfaEnrollmentTypeStatus(**mfa_enrollment_type_status_model_dict)

        # Verify the model instances are equivalent
        assert mfa_enrollment_type_status_model == mfa_enrollment_type_status_model2

        # Convert model instance back to dict and verify no loss of data
        mfa_enrollment_type_status_model_json2 = mfa_enrollment_type_status_model.to_dict()
        assert mfa_enrollment_type_status_model_json2 == mfa_enrollment_type_status_model_json


class TestModel_MfaEnrollments:
    """
    Test Class for MfaEnrollments
    """

    def test_mfa_enrollments_serialization(self):
        """
        Test serialization/deserialization for MfaEnrollments
        """

        # Construct dict forms of any model objects needed in order to build this model.

        id_based_mfa_enrollment_model = {}  # IdBasedMfaEnrollment
        id_based_mfa_enrollment_model['trait_account_default'] = 'NONE'
        id_based_mfa_enrollment_model['trait_user_specific'] = 'NONE'
        id_based_mfa_enrollment_model['trait_effective'] = 'NONE'
        id_based_mfa_enrollment_model['complies'] = True
        id_based_mfa_enrollment_model['comply_state'] = 'NO'

        mfa_enrollment_type_status_model = {}  # MfaEnrollmentTypeStatus
        mfa_enrollment_type_status_model['required'] = True
        mfa_enrollment_type_status_model['enrolled'] = True

        account_based_mfa_enrollment_model = {}  # AccountBasedMfaEnrollment
        account_based_mfa_enrollment_model['security_questions'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['totp'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['verisign'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['complies'] = True

        # Construct a json representation of a MfaEnrollments model
        mfa_enrollments_model_json = {}
        mfa_enrollments_model_json['effective_mfa_type'] = 'testString'
        mfa_enrollments_model_json['id_based_mfa'] = id_based_mfa_enrollment_model
        mfa_enrollments_model_json['account_based_mfa'] = account_based_mfa_enrollment_model

        # Construct a model instance of MfaEnrollments by calling from_dict on the json representation
        mfa_enrollments_model = MfaEnrollments.from_dict(mfa_enrollments_model_json)
        assert mfa_enrollments_model != False

        # Construct a model instance of MfaEnrollments by calling from_dict on the json representation
        mfa_enrollments_model_dict = MfaEnrollments.from_dict(mfa_enrollments_model_json).__dict__
        mfa_enrollments_model2 = MfaEnrollments(**mfa_enrollments_model_dict)

        # Verify the model instances are equivalent
        assert mfa_enrollments_model == mfa_enrollments_model2

        # Convert model instance back to dict and verify no loss of data
        mfa_enrollments_model_json2 = mfa_enrollments_model.to_dict()
        assert mfa_enrollments_model_json2 == mfa_enrollments_model_json


class TestModel_PolicyTemplateReference:
    """
    Test Class for PolicyTemplateReference
    """

    def test_policy_template_reference_serialization(self):
        """
        Test serialization/deserialization for PolicyTemplateReference
        """

        # Construct a json representation of a PolicyTemplateReference model
        policy_template_reference_model_json = {}
        policy_template_reference_model_json['id'] = 'testString'
        policy_template_reference_model_json['version'] = 'testString'

        # Construct a model instance of PolicyTemplateReference by calling from_dict on the json representation
        policy_template_reference_model = PolicyTemplateReference.from_dict(policy_template_reference_model_json)
        assert policy_template_reference_model != False

        # Construct a model instance of PolicyTemplateReference by calling from_dict on the json representation
        policy_template_reference_model_dict = PolicyTemplateReference.from_dict(
            policy_template_reference_model_json
        ).__dict__
        policy_template_reference_model2 = PolicyTemplateReference(**policy_template_reference_model_dict)

        # Verify the model instances are equivalent
        assert policy_template_reference_model == policy_template_reference_model2

        # Convert model instance back to dict and verify no loss of data
        policy_template_reference_model_json2 = policy_template_reference_model.to_dict()
        assert policy_template_reference_model_json2 == policy_template_reference_model_json


class TestModel_ProfileClaimRule:
    """
    Test Class for ProfileClaimRule
    """

    def test_profile_claim_rule_serialization(self):
        """
        Test serialization/deserialization for ProfileClaimRule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_claim_rule_conditions_model = {}  # ProfileClaimRuleConditions
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a json representation of a ProfileClaimRule model
        profile_claim_rule_model_json = {}
        profile_claim_rule_model_json['id'] = 'testString'
        profile_claim_rule_model_json['entity_tag'] = 'testString'
        profile_claim_rule_model_json['created_at'] = '2019-01-01T12:00:00Z'
        profile_claim_rule_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        profile_claim_rule_model_json['name'] = 'testString'
        profile_claim_rule_model_json['type'] = 'testString'
        profile_claim_rule_model_json['realm_name'] = 'testString'
        profile_claim_rule_model_json['expiration'] = 38
        profile_claim_rule_model_json['cr_type'] = 'testString'
        profile_claim_rule_model_json['conditions'] = [profile_claim_rule_conditions_model]

        # Construct a model instance of ProfileClaimRule by calling from_dict on the json representation
        profile_claim_rule_model = ProfileClaimRule.from_dict(profile_claim_rule_model_json)
        assert profile_claim_rule_model != False

        # Construct a model instance of ProfileClaimRule by calling from_dict on the json representation
        profile_claim_rule_model_dict = ProfileClaimRule.from_dict(profile_claim_rule_model_json).__dict__
        profile_claim_rule_model2 = ProfileClaimRule(**profile_claim_rule_model_dict)

        # Verify the model instances are equivalent
        assert profile_claim_rule_model == profile_claim_rule_model2

        # Convert model instance back to dict and verify no loss of data
        profile_claim_rule_model_json2 = profile_claim_rule_model.to_dict()
        assert profile_claim_rule_model_json2 == profile_claim_rule_model_json


class TestModel_ProfileClaimRuleConditions:
    """
    Test Class for ProfileClaimRuleConditions
    """

    def test_profile_claim_rule_conditions_serialization(self):
        """
        Test serialization/deserialization for ProfileClaimRuleConditions
        """

        # Construct a json representation of a ProfileClaimRuleConditions model
        profile_claim_rule_conditions_model_json = {}
        profile_claim_rule_conditions_model_json['claim'] = 'testString'
        profile_claim_rule_conditions_model_json['operator'] = 'testString'
        profile_claim_rule_conditions_model_json['value'] = 'testString'

        # Construct a model instance of ProfileClaimRuleConditions by calling from_dict on the json representation
        profile_claim_rule_conditions_model = ProfileClaimRuleConditions.from_dict(
            profile_claim_rule_conditions_model_json
        )
        assert profile_claim_rule_conditions_model != False

        # Construct a model instance of ProfileClaimRuleConditions by calling from_dict on the json representation
        profile_claim_rule_conditions_model_dict = ProfileClaimRuleConditions.from_dict(
            profile_claim_rule_conditions_model_json
        ).__dict__
        profile_claim_rule_conditions_model2 = ProfileClaimRuleConditions(**profile_claim_rule_conditions_model_dict)

        # Verify the model instances are equivalent
        assert profile_claim_rule_conditions_model == profile_claim_rule_conditions_model2

        # Convert model instance back to dict and verify no loss of data
        profile_claim_rule_conditions_model_json2 = profile_claim_rule_conditions_model.to_dict()
        assert profile_claim_rule_conditions_model_json2 == profile_claim_rule_conditions_model_json


class TestModel_ProfileClaimRuleList:
    """
    Test Class for ProfileClaimRuleList
    """

    def test_profile_claim_rule_list_serialization(self):
        """
        Test serialization/deserialization for ProfileClaimRuleList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        profile_claim_rule_conditions_model = {}  # ProfileClaimRuleConditions
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        profile_claim_rule_model = {}  # ProfileClaimRule
        profile_claim_rule_model['id'] = 'testString'
        profile_claim_rule_model['entity_tag'] = 'testString'
        profile_claim_rule_model['created_at'] = '2019-01-01T12:00:00Z'
        profile_claim_rule_model['modified_at'] = '2019-01-01T12:00:00Z'
        profile_claim_rule_model['name'] = 'testString'
        profile_claim_rule_model['type'] = 'testString'
        profile_claim_rule_model['realm_name'] = 'testString'
        profile_claim_rule_model['expiration'] = 38
        profile_claim_rule_model['cr_type'] = 'testString'
        profile_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        # Construct a json representation of a ProfileClaimRuleList model
        profile_claim_rule_list_model_json = {}
        profile_claim_rule_list_model_json['context'] = response_context_model
        profile_claim_rule_list_model_json['rules'] = [profile_claim_rule_model]

        # Construct a model instance of ProfileClaimRuleList by calling from_dict on the json representation
        profile_claim_rule_list_model = ProfileClaimRuleList.from_dict(profile_claim_rule_list_model_json)
        assert profile_claim_rule_list_model != False

        # Construct a model instance of ProfileClaimRuleList by calling from_dict on the json representation
        profile_claim_rule_list_model_dict = ProfileClaimRuleList.from_dict(profile_claim_rule_list_model_json).__dict__
        profile_claim_rule_list_model2 = ProfileClaimRuleList(**profile_claim_rule_list_model_dict)

        # Verify the model instances are equivalent
        assert profile_claim_rule_list_model == profile_claim_rule_list_model2

        # Convert model instance back to dict and verify no loss of data
        profile_claim_rule_list_model_json2 = profile_claim_rule_list_model.to_dict()
        assert profile_claim_rule_list_model_json2 == profile_claim_rule_list_model_json


class TestModel_ProfileIdentitiesResponse:
    """
    Test Class for ProfileIdentitiesResponse
    """

    def test_profile_identities_response_serialization(self):
        """
        Test serialization/deserialization for ProfileIdentitiesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_identity_response_model = {}  # ProfileIdentityResponse
        profile_identity_response_model['iam_id'] = 'testString'
        profile_identity_response_model['identifier'] = 'testString'
        profile_identity_response_model['type'] = 'user'
        profile_identity_response_model['accounts'] = ['testString']
        profile_identity_response_model['description'] = 'testString'

        # Construct a json representation of a ProfileIdentitiesResponse model
        profile_identities_response_model_json = {}
        profile_identities_response_model_json['entity_tag'] = 'testString'
        profile_identities_response_model_json['identities'] = [profile_identity_response_model]

        # Construct a model instance of ProfileIdentitiesResponse by calling from_dict on the json representation
        profile_identities_response_model = ProfileIdentitiesResponse.from_dict(profile_identities_response_model_json)
        assert profile_identities_response_model != False

        # Construct a model instance of ProfileIdentitiesResponse by calling from_dict on the json representation
        profile_identities_response_model_dict = ProfileIdentitiesResponse.from_dict(
            profile_identities_response_model_json
        ).__dict__
        profile_identities_response_model2 = ProfileIdentitiesResponse(**profile_identities_response_model_dict)

        # Verify the model instances are equivalent
        assert profile_identities_response_model == profile_identities_response_model2

        # Convert model instance back to dict and verify no loss of data
        profile_identities_response_model_json2 = profile_identities_response_model.to_dict()
        assert profile_identities_response_model_json2 == profile_identities_response_model_json


class TestModel_ProfileIdentityRequest:
    """
    Test Class for ProfileIdentityRequest
    """

    def test_profile_identity_request_serialization(self):
        """
        Test serialization/deserialization for ProfileIdentityRequest
        """

        # Construct a json representation of a ProfileIdentityRequest model
        profile_identity_request_model_json = {}
        profile_identity_request_model_json['identifier'] = 'testString'
        profile_identity_request_model_json['type'] = 'user'
        profile_identity_request_model_json['accounts'] = ['testString']
        profile_identity_request_model_json['description'] = 'testString'

        # Construct a model instance of ProfileIdentityRequest by calling from_dict on the json representation
        profile_identity_request_model = ProfileIdentityRequest.from_dict(profile_identity_request_model_json)
        assert profile_identity_request_model != False

        # Construct a model instance of ProfileIdentityRequest by calling from_dict on the json representation
        profile_identity_request_model_dict = ProfileIdentityRequest.from_dict(
            profile_identity_request_model_json
        ).__dict__
        profile_identity_request_model2 = ProfileIdentityRequest(**profile_identity_request_model_dict)

        # Verify the model instances are equivalent
        assert profile_identity_request_model == profile_identity_request_model2

        # Convert model instance back to dict and verify no loss of data
        profile_identity_request_model_json2 = profile_identity_request_model.to_dict()
        assert profile_identity_request_model_json2 == profile_identity_request_model_json


class TestModel_ProfileIdentityResponse:
    """
    Test Class for ProfileIdentityResponse
    """

    def test_profile_identity_response_serialization(self):
        """
        Test serialization/deserialization for ProfileIdentityResponse
        """

        # Construct a json representation of a ProfileIdentityResponse model
        profile_identity_response_model_json = {}
        profile_identity_response_model_json['iam_id'] = 'testString'
        profile_identity_response_model_json['identifier'] = 'testString'
        profile_identity_response_model_json['type'] = 'user'
        profile_identity_response_model_json['accounts'] = ['testString']
        profile_identity_response_model_json['description'] = 'testString'

        # Construct a model instance of ProfileIdentityResponse by calling from_dict on the json representation
        profile_identity_response_model = ProfileIdentityResponse.from_dict(profile_identity_response_model_json)
        assert profile_identity_response_model != False

        # Construct a model instance of ProfileIdentityResponse by calling from_dict on the json representation
        profile_identity_response_model_dict = ProfileIdentityResponse.from_dict(
            profile_identity_response_model_json
        ).__dict__
        profile_identity_response_model2 = ProfileIdentityResponse(**profile_identity_response_model_dict)

        # Verify the model instances are equivalent
        assert profile_identity_response_model == profile_identity_response_model2

        # Convert model instance back to dict and verify no loss of data
        profile_identity_response_model_json2 = profile_identity_response_model.to_dict()
        assert profile_identity_response_model_json2 == profile_identity_response_model_json


class TestModel_ProfileLink:
    """
    Test Class for ProfileLink
    """

    def test_profile_link_serialization(self):
        """
        Test serialization/deserialization for ProfileLink
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_link_link_model = {}  # ProfileLinkLink
        profile_link_link_model['crn'] = 'testString'
        profile_link_link_model['namespace'] = 'testString'
        profile_link_link_model['name'] = 'testString'

        # Construct a json representation of a ProfileLink model
        profile_link_model_json = {}
        profile_link_model_json['id'] = 'testString'
        profile_link_model_json['entity_tag'] = 'testString'
        profile_link_model_json['created_at'] = '2019-01-01T12:00:00Z'
        profile_link_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        profile_link_model_json['name'] = 'testString'
        profile_link_model_json['cr_type'] = 'testString'
        profile_link_model_json['link'] = profile_link_link_model

        # Construct a model instance of ProfileLink by calling from_dict on the json representation
        profile_link_model = ProfileLink.from_dict(profile_link_model_json)
        assert profile_link_model != False

        # Construct a model instance of ProfileLink by calling from_dict on the json representation
        profile_link_model_dict = ProfileLink.from_dict(profile_link_model_json).__dict__
        profile_link_model2 = ProfileLink(**profile_link_model_dict)

        # Verify the model instances are equivalent
        assert profile_link_model == profile_link_model2

        # Convert model instance back to dict and verify no loss of data
        profile_link_model_json2 = profile_link_model.to_dict()
        assert profile_link_model_json2 == profile_link_model_json


class TestModel_ProfileLinkLink:
    """
    Test Class for ProfileLinkLink
    """

    def test_profile_link_link_serialization(self):
        """
        Test serialization/deserialization for ProfileLinkLink
        """

        # Construct a json representation of a ProfileLinkLink model
        profile_link_link_model_json = {}
        profile_link_link_model_json['crn'] = 'testString'
        profile_link_link_model_json['namespace'] = 'testString'
        profile_link_link_model_json['name'] = 'testString'

        # Construct a model instance of ProfileLinkLink by calling from_dict on the json representation
        profile_link_link_model = ProfileLinkLink.from_dict(profile_link_link_model_json)
        assert profile_link_link_model != False

        # Construct a model instance of ProfileLinkLink by calling from_dict on the json representation
        profile_link_link_model_dict = ProfileLinkLink.from_dict(profile_link_link_model_json).__dict__
        profile_link_link_model2 = ProfileLinkLink(**profile_link_link_model_dict)

        # Verify the model instances are equivalent
        assert profile_link_link_model == profile_link_link_model2

        # Convert model instance back to dict and verify no loss of data
        profile_link_link_model_json2 = profile_link_link_model.to_dict()
        assert profile_link_link_model_json2 == profile_link_link_model_json


class TestModel_ProfileLinkList:
    """
    Test Class for ProfileLinkList
    """

    def test_profile_link_list_serialization(self):
        """
        Test serialization/deserialization for ProfileLinkList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_link_link_model = {}  # ProfileLinkLink
        profile_link_link_model['crn'] = 'testString'
        profile_link_link_model['namespace'] = 'testString'
        profile_link_link_model['name'] = 'testString'

        profile_link_model = {}  # ProfileLink
        profile_link_model['id'] = 'testString'
        profile_link_model['entity_tag'] = 'testString'
        profile_link_model['created_at'] = '2019-01-01T12:00:00Z'
        profile_link_model['modified_at'] = '2019-01-01T12:00:00Z'
        profile_link_model['name'] = 'testString'
        profile_link_model['cr_type'] = 'testString'
        profile_link_model['link'] = profile_link_link_model

        # Construct a json representation of a ProfileLinkList model
        profile_link_list_model_json = {}
        profile_link_list_model_json['links'] = [profile_link_model]

        # Construct a model instance of ProfileLinkList by calling from_dict on the json representation
        profile_link_list_model = ProfileLinkList.from_dict(profile_link_list_model_json)
        assert profile_link_list_model != False

        # Construct a model instance of ProfileLinkList by calling from_dict on the json representation
        profile_link_list_model_dict = ProfileLinkList.from_dict(profile_link_list_model_json).__dict__
        profile_link_list_model2 = ProfileLinkList(**profile_link_list_model_dict)

        # Verify the model instances are equivalent
        assert profile_link_list_model == profile_link_list_model2

        # Convert model instance back to dict and verify no loss of data
        profile_link_list_model_json2 = profile_link_list_model.to_dict()
        assert profile_link_list_model_json2 == profile_link_list_model_json


class TestModel_Report:
    """
    Test Class for Report
    """

    def test_report_serialization(self):
        """
        Test serialization/deserialization for Report
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_activity_model = {}  # UserActivity
        user_activity_model['iam_id'] = 'testString'
        user_activity_model['name'] = 'testString'
        user_activity_model['username'] = 'testString'
        user_activity_model['email'] = 'testString'
        user_activity_model['last_authn'] = 'testString'

        apikey_activity_serviceid_model = {}  # ApikeyActivityServiceid
        apikey_activity_serviceid_model['id'] = 'testString'
        apikey_activity_serviceid_model['name'] = 'testString'

        apikey_activity_user_model = {}  # ApikeyActivityUser
        apikey_activity_user_model['iam_id'] = 'testString'
        apikey_activity_user_model['name'] = 'testString'
        apikey_activity_user_model['username'] = 'testString'
        apikey_activity_user_model['email'] = 'testString'

        apikey_activity_model = {}  # ApikeyActivity
        apikey_activity_model['id'] = 'testString'
        apikey_activity_model['name'] = 'testString'
        apikey_activity_model['type'] = 'testString'
        apikey_activity_model['serviceid'] = apikey_activity_serviceid_model
        apikey_activity_model['user'] = apikey_activity_user_model
        apikey_activity_model['last_authn'] = 'testString'

        entity_activity_model = {}  # EntityActivity
        entity_activity_model['id'] = 'testString'
        entity_activity_model['name'] = 'testString'
        entity_activity_model['last_authn'] = 'testString'

        # Construct a json representation of a Report model
        report_model_json = {}
        report_model_json['created_by'] = 'testString'
        report_model_json['reference'] = 'testString'
        report_model_json['report_duration'] = 'testString'
        report_model_json['report_start_time'] = 'testString'
        report_model_json['report_end_time'] = 'testString'
        report_model_json['users'] = [user_activity_model]
        report_model_json['apikeys'] = [apikey_activity_model]
        report_model_json['serviceids'] = [entity_activity_model]
        report_model_json['profiles'] = [entity_activity_model]

        # Construct a model instance of Report by calling from_dict on the json representation
        report_model = Report.from_dict(report_model_json)
        assert report_model != False

        # Construct a model instance of Report by calling from_dict on the json representation
        report_model_dict = Report.from_dict(report_model_json).__dict__
        report_model2 = Report(**report_model_dict)

        # Verify the model instances are equivalent
        assert report_model == report_model2

        # Convert model instance back to dict and verify no loss of data
        report_model_json2 = report_model.to_dict()
        assert report_model_json2 == report_model_json


class TestModel_ReportMfaEnrollmentStatus:
    """
    Test Class for ReportMfaEnrollmentStatus
    """

    def test_report_mfa_enrollment_status_serialization(self):
        """
        Test serialization/deserialization for ReportMfaEnrollmentStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        id_based_mfa_enrollment_model = {}  # IdBasedMfaEnrollment
        id_based_mfa_enrollment_model['trait_account_default'] = 'NONE'
        id_based_mfa_enrollment_model['trait_user_specific'] = 'NONE'
        id_based_mfa_enrollment_model['trait_effective'] = 'NONE'
        id_based_mfa_enrollment_model['complies'] = True
        id_based_mfa_enrollment_model['comply_state'] = 'NO'

        mfa_enrollment_type_status_model = {}  # MfaEnrollmentTypeStatus
        mfa_enrollment_type_status_model['required'] = True
        mfa_enrollment_type_status_model['enrolled'] = True

        account_based_mfa_enrollment_model = {}  # AccountBasedMfaEnrollment
        account_based_mfa_enrollment_model['security_questions'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['totp'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['verisign'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['complies'] = True

        mfa_enrollments_model = {}  # MfaEnrollments
        mfa_enrollments_model['effective_mfa_type'] = 'testString'
        mfa_enrollments_model['id_based_mfa'] = id_based_mfa_enrollment_model
        mfa_enrollments_model['account_based_mfa'] = account_based_mfa_enrollment_model

        user_report_mfa_enrollment_status_model = {}  # UserReportMfaEnrollmentStatus
        user_report_mfa_enrollment_status_model['iam_id'] = 'testString'
        user_report_mfa_enrollment_status_model['name'] = 'testString'
        user_report_mfa_enrollment_status_model['username'] = 'testString'
        user_report_mfa_enrollment_status_model['email'] = 'testString'
        user_report_mfa_enrollment_status_model['enrollments'] = mfa_enrollments_model

        # Construct a json representation of a ReportMfaEnrollmentStatus model
        report_mfa_enrollment_status_model_json = {}
        report_mfa_enrollment_status_model_json['created_by'] = 'testString'
        report_mfa_enrollment_status_model_json['reference'] = 'testString'
        report_mfa_enrollment_status_model_json['report_time'] = 'testString'
        report_mfa_enrollment_status_model_json['account_id'] = 'testString'
        report_mfa_enrollment_status_model_json['ims_account_id'] = 'testString'
        report_mfa_enrollment_status_model_json['users'] = [user_report_mfa_enrollment_status_model]

        # Construct a model instance of ReportMfaEnrollmentStatus by calling from_dict on the json representation
        report_mfa_enrollment_status_model = ReportMfaEnrollmentStatus.from_dict(
            report_mfa_enrollment_status_model_json
        )
        assert report_mfa_enrollment_status_model != False

        # Construct a model instance of ReportMfaEnrollmentStatus by calling from_dict on the json representation
        report_mfa_enrollment_status_model_dict = ReportMfaEnrollmentStatus.from_dict(
            report_mfa_enrollment_status_model_json
        ).__dict__
        report_mfa_enrollment_status_model2 = ReportMfaEnrollmentStatus(**report_mfa_enrollment_status_model_dict)

        # Verify the model instances are equivalent
        assert report_mfa_enrollment_status_model == report_mfa_enrollment_status_model2

        # Convert model instance back to dict and verify no loss of data
        report_mfa_enrollment_status_model_json2 = report_mfa_enrollment_status_model.to_dict()
        assert report_mfa_enrollment_status_model_json2 == report_mfa_enrollment_status_model_json


class TestModel_ReportReference:
    """
    Test Class for ReportReference
    """

    def test_report_reference_serialization(self):
        """
        Test serialization/deserialization for ReportReference
        """

        # Construct a json representation of a ReportReference model
        report_reference_model_json = {}
        report_reference_model_json['reference'] = 'testString'

        # Construct a model instance of ReportReference by calling from_dict on the json representation
        report_reference_model = ReportReference.from_dict(report_reference_model_json)
        assert report_reference_model != False

        # Construct a model instance of ReportReference by calling from_dict on the json representation
        report_reference_model_dict = ReportReference.from_dict(report_reference_model_json).__dict__
        report_reference_model2 = ReportReference(**report_reference_model_dict)

        # Verify the model instances are equivalent
        assert report_reference_model == report_reference_model2

        # Convert model instance back to dict and verify no loss of data
        report_reference_model_json2 = report_reference_model.to_dict()
        assert report_reference_model_json2 == report_reference_model_json


class TestModel_ResponseContext:
    """
    Test Class for ResponseContext
    """

    def test_response_context_serialization(self):
        """
        Test serialization/deserialization for ResponseContext
        """

        # Construct a json representation of a ResponseContext model
        response_context_model_json = {}
        response_context_model_json['transaction_id'] = 'testString'
        response_context_model_json['operation'] = 'testString'
        response_context_model_json['user_agent'] = 'testString'
        response_context_model_json['url'] = 'testString'
        response_context_model_json['instance_id'] = 'testString'
        response_context_model_json['thread_id'] = 'testString'
        response_context_model_json['host'] = 'testString'
        response_context_model_json['start_time'] = 'testString'
        response_context_model_json['end_time'] = 'testString'
        response_context_model_json['elapsed_time'] = 'testString'
        response_context_model_json['cluster_name'] = 'testString'

        # Construct a model instance of ResponseContext by calling from_dict on the json representation
        response_context_model = ResponseContext.from_dict(response_context_model_json)
        assert response_context_model != False

        # Construct a model instance of ResponseContext by calling from_dict on the json representation
        response_context_model_dict = ResponseContext.from_dict(response_context_model_json).__dict__
        response_context_model2 = ResponseContext(**response_context_model_dict)

        # Verify the model instances are equivalent
        assert response_context_model == response_context_model2

        # Convert model instance back to dict and verify no loss of data
        response_context_model_json2 = response_context_model.to_dict()
        assert response_context_model_json2 == response_context_model_json


class TestModel_ServiceId:
    """
    Test Class for ServiceId
    """

    def test_service_id_serialization(self):
        """
        Test serialization/deserialization for ServiceId
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        activity_model = {}  # Activity
        activity_model['last_authn'] = 'testString'
        activity_model['authn_count'] = 26

        api_key_model = {}  # ApiKey
        api_key_model['context'] = response_context_model
        api_key_model['id'] = 'testString'
        api_key_model['entity_tag'] = 'testString'
        api_key_model['crn'] = 'testString'
        api_key_model['locked'] = True
        api_key_model['disabled'] = True
        api_key_model['created_at'] = '2019-01-01T12:00:00Z'
        api_key_model['created_by'] = 'testString'
        api_key_model['modified_at'] = '2019-01-01T12:00:00Z'
        api_key_model['name'] = 'testString'
        api_key_model['support_sessions'] = True
        api_key_model['action_when_leaked'] = 'testString'
        api_key_model['description'] = 'testString'
        api_key_model['iam_id'] = 'testString'
        api_key_model['account_id'] = 'testString'
        api_key_model['apikey'] = 'testString'
        api_key_model['history'] = [enity_history_record_model]
        api_key_model['activity'] = activity_model

        # Construct a json representation of a ServiceId model
        service_id_model_json = {}
        service_id_model_json['context'] = response_context_model
        service_id_model_json['id'] = 'testString'
        service_id_model_json['iam_id'] = 'testString'
        service_id_model_json['entity_tag'] = 'testString'
        service_id_model_json['crn'] = 'testString'
        service_id_model_json['locked'] = True
        service_id_model_json['created_at'] = '2019-01-01T12:00:00Z'
        service_id_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        service_id_model_json['account_id'] = 'testString'
        service_id_model_json['name'] = 'testString'
        service_id_model_json['description'] = 'testString'
        service_id_model_json['unique_instance_crns'] = ['testString']
        service_id_model_json['history'] = [enity_history_record_model]
        service_id_model_json['apikey'] = api_key_model
        service_id_model_json['activity'] = activity_model

        # Construct a model instance of ServiceId by calling from_dict on the json representation
        service_id_model = ServiceId.from_dict(service_id_model_json)
        assert service_id_model != False

        # Construct a model instance of ServiceId by calling from_dict on the json representation
        service_id_model_dict = ServiceId.from_dict(service_id_model_json).__dict__
        service_id_model2 = ServiceId(**service_id_model_dict)

        # Verify the model instances are equivalent
        assert service_id_model == service_id_model2

        # Convert model instance back to dict and verify no loss of data
        service_id_model_json2 = service_id_model.to_dict()
        assert service_id_model_json2 == service_id_model_json


class TestModel_ServiceIdList:
    """
    Test Class for ServiceIdList
    """

    def test_service_id_list_serialization(self):
        """
        Test serialization/deserialization for ServiceIdList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        activity_model = {}  # Activity
        activity_model['last_authn'] = 'testString'
        activity_model['authn_count'] = 26

        api_key_model = {}  # ApiKey
        api_key_model['context'] = response_context_model
        api_key_model['id'] = 'testString'
        api_key_model['entity_tag'] = 'testString'
        api_key_model['crn'] = 'testString'
        api_key_model['locked'] = True
        api_key_model['disabled'] = True
        api_key_model['created_at'] = '2019-01-01T12:00:00Z'
        api_key_model['created_by'] = 'testString'
        api_key_model['modified_at'] = '2019-01-01T12:00:00Z'
        api_key_model['name'] = 'testString'
        api_key_model['support_sessions'] = True
        api_key_model['action_when_leaked'] = 'testString'
        api_key_model['description'] = 'testString'
        api_key_model['iam_id'] = 'testString'
        api_key_model['account_id'] = 'testString'
        api_key_model['apikey'] = 'testString'
        api_key_model['history'] = [enity_history_record_model]
        api_key_model['activity'] = activity_model

        service_id_model = {}  # ServiceId
        service_id_model['context'] = response_context_model
        service_id_model['id'] = 'testString'
        service_id_model['iam_id'] = 'testString'
        service_id_model['entity_tag'] = 'testString'
        service_id_model['crn'] = 'testString'
        service_id_model['locked'] = True
        service_id_model['created_at'] = '2019-01-01T12:00:00Z'
        service_id_model['modified_at'] = '2019-01-01T12:00:00Z'
        service_id_model['account_id'] = 'testString'
        service_id_model['name'] = 'testString'
        service_id_model['description'] = 'testString'
        service_id_model['unique_instance_crns'] = ['testString']
        service_id_model['history'] = [enity_history_record_model]
        service_id_model['apikey'] = api_key_model
        service_id_model['activity'] = activity_model

        # Construct a json representation of a ServiceIdList model
        service_id_list_model_json = {}
        service_id_list_model_json['context'] = response_context_model
        service_id_list_model_json['offset'] = 26
        service_id_list_model_json['limit'] = 26
        service_id_list_model_json['first'] = 'testString'
        service_id_list_model_json['previous'] = 'testString'
        service_id_list_model_json['next'] = 'testString'
        service_id_list_model_json['serviceids'] = [service_id_model]

        # Construct a model instance of ServiceIdList by calling from_dict on the json representation
        service_id_list_model = ServiceIdList.from_dict(service_id_list_model_json)
        assert service_id_list_model != False

        # Construct a model instance of ServiceIdList by calling from_dict on the json representation
        service_id_list_model_dict = ServiceIdList.from_dict(service_id_list_model_json).__dict__
        service_id_list_model2 = ServiceIdList(**service_id_list_model_dict)

        # Verify the model instances are equivalent
        assert service_id_list_model == service_id_list_model2

        # Convert model instance back to dict and verify no loss of data
        service_id_list_model_json2 = service_id_list_model.to_dict()
        assert service_id_list_model_json2 == service_id_list_model_json


class TestModel_TemplateAssignmentListResponse:
    """
    Test Class for TemplateAssignmentListResponse
    """

    def test_template_assignment_list_response_serialization(self):
        """
        Test serialization/deserialization for TemplateAssignmentListResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        template_assignment_resource_model = {}  # TemplateAssignmentResource
        template_assignment_resource_model['id'] = 'testString'

        template_assignment_resource_error_model = {}  # TemplateAssignmentResourceError
        template_assignment_resource_error_model['name'] = 'testString'
        template_assignment_resource_error_model['errorCode'] = 'testString'
        template_assignment_resource_error_model['message'] = 'testString'
        template_assignment_resource_error_model['statusCode'] = 'testString'

        template_assignment_response_resource_detail_model = {}  # TemplateAssignmentResponseResourceDetail
        template_assignment_response_resource_detail_model['id'] = 'testString'
        template_assignment_response_resource_detail_model['version'] = 'testString'
        template_assignment_response_resource_detail_model['resource_created'] = template_assignment_resource_model
        template_assignment_response_resource_detail_model['error_message'] = template_assignment_resource_error_model
        template_assignment_response_resource_detail_model['status'] = 'testString'

        template_assignment_response_resource_model = {}  # TemplateAssignmentResponseResource
        template_assignment_response_resource_model['target'] = 'testString'
        template_assignment_response_resource_model['profile'] = template_assignment_response_resource_detail_model
        template_assignment_response_resource_model['account_settings'] = (
            template_assignment_response_resource_detail_model
        )
        template_assignment_response_resource_model['policy_template_refs'] = [
            template_assignment_response_resource_detail_model
        ]

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        template_assignment_response_model = {}  # TemplateAssignmentResponse
        template_assignment_response_model['context'] = response_context_model
        template_assignment_response_model['id'] = 'testString'
        template_assignment_response_model['account_id'] = 'testString'
        template_assignment_response_model['template_id'] = 'testString'
        template_assignment_response_model['template_version'] = 26
        template_assignment_response_model['target_type'] = 'testString'
        template_assignment_response_model['target'] = 'testString'
        template_assignment_response_model['status'] = 'testString'
        template_assignment_response_model['resources'] = [template_assignment_response_resource_model]
        template_assignment_response_model['history'] = [enity_history_record_model]
        template_assignment_response_model['href'] = 'testString'
        template_assignment_response_model['created_at'] = 'testString'
        template_assignment_response_model['created_by_id'] = 'testString'
        template_assignment_response_model['last_modified_at'] = 'testString'
        template_assignment_response_model['last_modified_by_id'] = 'testString'
        template_assignment_response_model['entity_tag'] = 'testString'

        # Construct a json representation of a TemplateAssignmentListResponse model
        template_assignment_list_response_model_json = {}
        template_assignment_list_response_model_json['context'] = response_context_model
        template_assignment_list_response_model_json['offset'] = 26
        template_assignment_list_response_model_json['limit'] = 26
        template_assignment_list_response_model_json['first'] = 'testString'
        template_assignment_list_response_model_json['previous'] = 'testString'
        template_assignment_list_response_model_json['next'] = 'testString'
        template_assignment_list_response_model_json['assignments'] = [template_assignment_response_model]

        # Construct a model instance of TemplateAssignmentListResponse by calling from_dict on the json representation
        template_assignment_list_response_model = TemplateAssignmentListResponse.from_dict(
            template_assignment_list_response_model_json
        )
        assert template_assignment_list_response_model != False

        # Construct a model instance of TemplateAssignmentListResponse by calling from_dict on the json representation
        template_assignment_list_response_model_dict = TemplateAssignmentListResponse.from_dict(
            template_assignment_list_response_model_json
        ).__dict__
        template_assignment_list_response_model2 = TemplateAssignmentListResponse(
            **template_assignment_list_response_model_dict
        )

        # Verify the model instances are equivalent
        assert template_assignment_list_response_model == template_assignment_list_response_model2

        # Convert model instance back to dict and verify no loss of data
        template_assignment_list_response_model_json2 = template_assignment_list_response_model.to_dict()
        assert template_assignment_list_response_model_json2 == template_assignment_list_response_model_json


class TestModel_TemplateAssignmentResource:
    """
    Test Class for TemplateAssignmentResource
    """

    def test_template_assignment_resource_serialization(self):
        """
        Test serialization/deserialization for TemplateAssignmentResource
        """

        # Construct a json representation of a TemplateAssignmentResource model
        template_assignment_resource_model_json = {}
        template_assignment_resource_model_json['id'] = 'testString'

        # Construct a model instance of TemplateAssignmentResource by calling from_dict on the json representation
        template_assignment_resource_model = TemplateAssignmentResource.from_dict(
            template_assignment_resource_model_json
        )
        assert template_assignment_resource_model != False

        # Construct a model instance of TemplateAssignmentResource by calling from_dict on the json representation
        template_assignment_resource_model_dict = TemplateAssignmentResource.from_dict(
            template_assignment_resource_model_json
        ).__dict__
        template_assignment_resource_model2 = TemplateAssignmentResource(**template_assignment_resource_model_dict)

        # Verify the model instances are equivalent
        assert template_assignment_resource_model == template_assignment_resource_model2

        # Convert model instance back to dict and verify no loss of data
        template_assignment_resource_model_json2 = template_assignment_resource_model.to_dict()
        assert template_assignment_resource_model_json2 == template_assignment_resource_model_json


class TestModel_TemplateAssignmentResourceError:
    """
    Test Class for TemplateAssignmentResourceError
    """

    def test_template_assignment_resource_error_serialization(self):
        """
        Test serialization/deserialization for TemplateAssignmentResourceError
        """

        # Construct a json representation of a TemplateAssignmentResourceError model
        template_assignment_resource_error_model_json = {}
        template_assignment_resource_error_model_json['name'] = 'testString'
        template_assignment_resource_error_model_json['errorCode'] = 'testString'
        template_assignment_resource_error_model_json['message'] = 'testString'
        template_assignment_resource_error_model_json['statusCode'] = 'testString'

        # Construct a model instance of TemplateAssignmentResourceError by calling from_dict on the json representation
        template_assignment_resource_error_model = TemplateAssignmentResourceError.from_dict(
            template_assignment_resource_error_model_json
        )
        assert template_assignment_resource_error_model != False

        # Construct a model instance of TemplateAssignmentResourceError by calling from_dict on the json representation
        template_assignment_resource_error_model_dict = TemplateAssignmentResourceError.from_dict(
            template_assignment_resource_error_model_json
        ).__dict__
        template_assignment_resource_error_model2 = TemplateAssignmentResourceError(
            **template_assignment_resource_error_model_dict
        )

        # Verify the model instances are equivalent
        assert template_assignment_resource_error_model == template_assignment_resource_error_model2

        # Convert model instance back to dict and verify no loss of data
        template_assignment_resource_error_model_json2 = template_assignment_resource_error_model.to_dict()
        assert template_assignment_resource_error_model_json2 == template_assignment_resource_error_model_json


class TestModel_TemplateAssignmentResponse:
    """
    Test Class for TemplateAssignmentResponse
    """

    def test_template_assignment_response_serialization(self):
        """
        Test serialization/deserialization for TemplateAssignmentResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        template_assignment_resource_model = {}  # TemplateAssignmentResource
        template_assignment_resource_model['id'] = 'testString'

        template_assignment_resource_error_model = {}  # TemplateAssignmentResourceError
        template_assignment_resource_error_model['name'] = 'testString'
        template_assignment_resource_error_model['errorCode'] = 'testString'
        template_assignment_resource_error_model['message'] = 'testString'
        template_assignment_resource_error_model['statusCode'] = 'testString'

        template_assignment_response_resource_detail_model = {}  # TemplateAssignmentResponseResourceDetail
        template_assignment_response_resource_detail_model['id'] = 'testString'
        template_assignment_response_resource_detail_model['version'] = 'testString'
        template_assignment_response_resource_detail_model['resource_created'] = template_assignment_resource_model
        template_assignment_response_resource_detail_model['error_message'] = template_assignment_resource_error_model
        template_assignment_response_resource_detail_model['status'] = 'testString'

        template_assignment_response_resource_model = {}  # TemplateAssignmentResponseResource
        template_assignment_response_resource_model['target'] = 'testString'
        template_assignment_response_resource_model['profile'] = template_assignment_response_resource_detail_model
        template_assignment_response_resource_model['account_settings'] = (
            template_assignment_response_resource_detail_model
        )
        template_assignment_response_resource_model['policy_template_refs'] = [
            template_assignment_response_resource_detail_model
        ]

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        # Construct a json representation of a TemplateAssignmentResponse model
        template_assignment_response_model_json = {}
        template_assignment_response_model_json['context'] = response_context_model
        template_assignment_response_model_json['id'] = 'testString'
        template_assignment_response_model_json['account_id'] = 'testString'
        template_assignment_response_model_json['template_id'] = 'testString'
        template_assignment_response_model_json['template_version'] = 26
        template_assignment_response_model_json['target_type'] = 'testString'
        template_assignment_response_model_json['target'] = 'testString'
        template_assignment_response_model_json['status'] = 'testString'
        template_assignment_response_model_json['resources'] = [template_assignment_response_resource_model]
        template_assignment_response_model_json['history'] = [enity_history_record_model]
        template_assignment_response_model_json['href'] = 'testString'
        template_assignment_response_model_json['created_at'] = 'testString'
        template_assignment_response_model_json['created_by_id'] = 'testString'
        template_assignment_response_model_json['last_modified_at'] = 'testString'
        template_assignment_response_model_json['last_modified_by_id'] = 'testString'
        template_assignment_response_model_json['entity_tag'] = 'testString'

        # Construct a model instance of TemplateAssignmentResponse by calling from_dict on the json representation
        template_assignment_response_model = TemplateAssignmentResponse.from_dict(
            template_assignment_response_model_json
        )
        assert template_assignment_response_model != False

        # Construct a model instance of TemplateAssignmentResponse by calling from_dict on the json representation
        template_assignment_response_model_dict = TemplateAssignmentResponse.from_dict(
            template_assignment_response_model_json
        ).__dict__
        template_assignment_response_model2 = TemplateAssignmentResponse(**template_assignment_response_model_dict)

        # Verify the model instances are equivalent
        assert template_assignment_response_model == template_assignment_response_model2

        # Convert model instance back to dict and verify no loss of data
        template_assignment_response_model_json2 = template_assignment_response_model.to_dict()
        assert template_assignment_response_model_json2 == template_assignment_response_model_json


class TestModel_TemplateAssignmentResponseResource:
    """
    Test Class for TemplateAssignmentResponseResource
    """

    def test_template_assignment_response_resource_serialization(self):
        """
        Test serialization/deserialization for TemplateAssignmentResponseResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        template_assignment_resource_model = {}  # TemplateAssignmentResource
        template_assignment_resource_model['id'] = 'testString'

        template_assignment_resource_error_model = {}  # TemplateAssignmentResourceError
        template_assignment_resource_error_model['name'] = 'testString'
        template_assignment_resource_error_model['errorCode'] = 'testString'
        template_assignment_resource_error_model['message'] = 'testString'
        template_assignment_resource_error_model['statusCode'] = 'testString'

        template_assignment_response_resource_detail_model = {}  # TemplateAssignmentResponseResourceDetail
        template_assignment_response_resource_detail_model['id'] = 'testString'
        template_assignment_response_resource_detail_model['version'] = 'testString'
        template_assignment_response_resource_detail_model['resource_created'] = template_assignment_resource_model
        template_assignment_response_resource_detail_model['error_message'] = template_assignment_resource_error_model
        template_assignment_response_resource_detail_model['status'] = 'testString'

        # Construct a json representation of a TemplateAssignmentResponseResource model
        template_assignment_response_resource_model_json = {}
        template_assignment_response_resource_model_json['target'] = 'testString'
        template_assignment_response_resource_model_json['profile'] = template_assignment_response_resource_detail_model
        template_assignment_response_resource_model_json['account_settings'] = (
            template_assignment_response_resource_detail_model
        )
        template_assignment_response_resource_model_json['policy_template_refs'] = [
            template_assignment_response_resource_detail_model
        ]

        # Construct a model instance of TemplateAssignmentResponseResource by calling from_dict on the json representation
        template_assignment_response_resource_model = TemplateAssignmentResponseResource.from_dict(
            template_assignment_response_resource_model_json
        )
        assert template_assignment_response_resource_model != False

        # Construct a model instance of TemplateAssignmentResponseResource by calling from_dict on the json representation
        template_assignment_response_resource_model_dict = TemplateAssignmentResponseResource.from_dict(
            template_assignment_response_resource_model_json
        ).__dict__
        template_assignment_response_resource_model2 = TemplateAssignmentResponseResource(
            **template_assignment_response_resource_model_dict
        )

        # Verify the model instances are equivalent
        assert template_assignment_response_resource_model == template_assignment_response_resource_model2

        # Convert model instance back to dict and verify no loss of data
        template_assignment_response_resource_model_json2 = template_assignment_response_resource_model.to_dict()
        assert template_assignment_response_resource_model_json2 == template_assignment_response_resource_model_json


class TestModel_TemplateAssignmentResponseResourceDetail:
    """
    Test Class for TemplateAssignmentResponseResourceDetail
    """

    def test_template_assignment_response_resource_detail_serialization(self):
        """
        Test serialization/deserialization for TemplateAssignmentResponseResourceDetail
        """

        # Construct dict forms of any model objects needed in order to build this model.

        template_assignment_resource_model = {}  # TemplateAssignmentResource
        template_assignment_resource_model['id'] = 'testString'

        template_assignment_resource_error_model = {}  # TemplateAssignmentResourceError
        template_assignment_resource_error_model['name'] = 'testString'
        template_assignment_resource_error_model['errorCode'] = 'testString'
        template_assignment_resource_error_model['message'] = 'testString'
        template_assignment_resource_error_model['statusCode'] = 'testString'

        # Construct a json representation of a TemplateAssignmentResponseResourceDetail model
        template_assignment_response_resource_detail_model_json = {}
        template_assignment_response_resource_detail_model_json['id'] = 'testString'
        template_assignment_response_resource_detail_model_json['version'] = 'testString'
        template_assignment_response_resource_detail_model_json['resource_created'] = template_assignment_resource_model
        template_assignment_response_resource_detail_model_json['error_message'] = (
            template_assignment_resource_error_model
        )
        template_assignment_response_resource_detail_model_json['status'] = 'testString'

        # Construct a model instance of TemplateAssignmentResponseResourceDetail by calling from_dict on the json representation
        template_assignment_response_resource_detail_model = TemplateAssignmentResponseResourceDetail.from_dict(
            template_assignment_response_resource_detail_model_json
        )
        assert template_assignment_response_resource_detail_model != False

        # Construct a model instance of TemplateAssignmentResponseResourceDetail by calling from_dict on the json representation
        template_assignment_response_resource_detail_model_dict = TemplateAssignmentResponseResourceDetail.from_dict(
            template_assignment_response_resource_detail_model_json
        ).__dict__
        template_assignment_response_resource_detail_model2 = TemplateAssignmentResponseResourceDetail(
            **template_assignment_response_resource_detail_model_dict
        )

        # Verify the model instances are equivalent
        assert template_assignment_response_resource_detail_model == template_assignment_response_resource_detail_model2

        # Convert model instance back to dict and verify no loss of data
        template_assignment_response_resource_detail_model_json2 = (
            template_assignment_response_resource_detail_model.to_dict()
        )
        assert (
            template_assignment_response_resource_detail_model_json2
            == template_assignment_response_resource_detail_model_json
        )


class TestModel_TemplateProfileComponentRequest:
    """
    Test Class for TemplateProfileComponentRequest
    """

    def test_template_profile_component_request_serialization(self):
        """
        Test serialization/deserialization for TemplateProfileComponentRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_claim_rule_conditions_model = {}  # ProfileClaimRuleConditions
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        trusted_profile_template_claim_rule_model = {}  # TrustedProfileTemplateClaimRule
        trusted_profile_template_claim_rule_model['name'] = 'testString'
        trusted_profile_template_claim_rule_model['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model['expiration'] = 38
        trusted_profile_template_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        profile_identity_request_model = {}  # ProfileIdentityRequest
        profile_identity_request_model['identifier'] = 'testString'
        profile_identity_request_model['type'] = 'user'
        profile_identity_request_model['accounts'] = ['testString']
        profile_identity_request_model['description'] = 'testString'

        # Construct a json representation of a TemplateProfileComponentRequest model
        template_profile_component_request_model_json = {}
        template_profile_component_request_model_json['name'] = 'testString'
        template_profile_component_request_model_json['description'] = 'testString'
        template_profile_component_request_model_json['rules'] = [trusted_profile_template_claim_rule_model]
        template_profile_component_request_model_json['identities'] = [profile_identity_request_model]

        # Construct a model instance of TemplateProfileComponentRequest by calling from_dict on the json representation
        template_profile_component_request_model = TemplateProfileComponentRequest.from_dict(
            template_profile_component_request_model_json
        )
        assert template_profile_component_request_model != False

        # Construct a model instance of TemplateProfileComponentRequest by calling from_dict on the json representation
        template_profile_component_request_model_dict = TemplateProfileComponentRequest.from_dict(
            template_profile_component_request_model_json
        ).__dict__
        template_profile_component_request_model2 = TemplateProfileComponentRequest(
            **template_profile_component_request_model_dict
        )

        # Verify the model instances are equivalent
        assert template_profile_component_request_model == template_profile_component_request_model2

        # Convert model instance back to dict and verify no loss of data
        template_profile_component_request_model_json2 = template_profile_component_request_model.to_dict()
        assert template_profile_component_request_model_json2 == template_profile_component_request_model_json


class TestModel_TemplateProfileComponentResponse:
    """
    Test Class for TemplateProfileComponentResponse
    """

    def test_template_profile_component_response_serialization(self):
        """
        Test serialization/deserialization for TemplateProfileComponentResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_claim_rule_conditions_model = {}  # ProfileClaimRuleConditions
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        trusted_profile_template_claim_rule_model = {}  # TrustedProfileTemplateClaimRule
        trusted_profile_template_claim_rule_model['name'] = 'testString'
        trusted_profile_template_claim_rule_model['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model['expiration'] = 38
        trusted_profile_template_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        profile_identity_response_model = {}  # ProfileIdentityResponse
        profile_identity_response_model['iam_id'] = 'testString'
        profile_identity_response_model['identifier'] = 'testString'
        profile_identity_response_model['type'] = 'user'
        profile_identity_response_model['accounts'] = ['testString']
        profile_identity_response_model['description'] = 'testString'

        # Construct a json representation of a TemplateProfileComponentResponse model
        template_profile_component_response_model_json = {}
        template_profile_component_response_model_json['name'] = 'testString'
        template_profile_component_response_model_json['description'] = 'testString'
        template_profile_component_response_model_json['rules'] = [trusted_profile_template_claim_rule_model]
        template_profile_component_response_model_json['identities'] = [profile_identity_response_model]

        # Construct a model instance of TemplateProfileComponentResponse by calling from_dict on the json representation
        template_profile_component_response_model = TemplateProfileComponentResponse.from_dict(
            template_profile_component_response_model_json
        )
        assert template_profile_component_response_model != False

        # Construct a model instance of TemplateProfileComponentResponse by calling from_dict on the json representation
        template_profile_component_response_model_dict = TemplateProfileComponentResponse.from_dict(
            template_profile_component_response_model_json
        ).__dict__
        template_profile_component_response_model2 = TemplateProfileComponentResponse(
            **template_profile_component_response_model_dict
        )

        # Verify the model instances are equivalent
        assert template_profile_component_response_model == template_profile_component_response_model2

        # Convert model instance back to dict and verify no loss of data
        template_profile_component_response_model_json2 = template_profile_component_response_model.to_dict()
        assert template_profile_component_response_model_json2 == template_profile_component_response_model_json


class TestModel_TrustedProfile:
    """
    Test Class for TrustedProfile
    """

    def test_trusted_profile_serialization(self):
        """
        Test serialization/deserialization for TrustedProfile
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        activity_model = {}  # Activity
        activity_model['last_authn'] = 'testString'
        activity_model['authn_count'] = 26

        # Construct a json representation of a TrustedProfile model
        trusted_profile_model_json = {}
        trusted_profile_model_json['context'] = response_context_model
        trusted_profile_model_json['id'] = 'testString'
        trusted_profile_model_json['entity_tag'] = 'testString'
        trusted_profile_model_json['crn'] = 'testString'
        trusted_profile_model_json['name'] = 'testString'
        trusted_profile_model_json['description'] = 'testString'
        trusted_profile_model_json['created_at'] = '2019-01-01T12:00:00Z'
        trusted_profile_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        trusted_profile_model_json['iam_id'] = 'testString'
        trusted_profile_model_json['account_id'] = 'testString'
        trusted_profile_model_json['template_id'] = 'testString'
        trusted_profile_model_json['assignment_id'] = 'testString'
        trusted_profile_model_json['ims_account_id'] = 26
        trusted_profile_model_json['ims_user_id'] = 26
        trusted_profile_model_json['history'] = [enity_history_record_model]
        trusted_profile_model_json['activity'] = activity_model

        # Construct a model instance of TrustedProfile by calling from_dict on the json representation
        trusted_profile_model = TrustedProfile.from_dict(trusted_profile_model_json)
        assert trusted_profile_model != False

        # Construct a model instance of TrustedProfile by calling from_dict on the json representation
        trusted_profile_model_dict = TrustedProfile.from_dict(trusted_profile_model_json).__dict__
        trusted_profile_model2 = TrustedProfile(**trusted_profile_model_dict)

        # Verify the model instances are equivalent
        assert trusted_profile_model == trusted_profile_model2

        # Convert model instance back to dict and verify no loss of data
        trusted_profile_model_json2 = trusted_profile_model.to_dict()
        assert trusted_profile_model_json2 == trusted_profile_model_json


class TestModel_TrustedProfileTemplateClaimRule:
    """
    Test Class for TrustedProfileTemplateClaimRule
    """

    def test_trusted_profile_template_claim_rule_serialization(self):
        """
        Test serialization/deserialization for TrustedProfileTemplateClaimRule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_claim_rule_conditions_model = {}  # ProfileClaimRuleConditions
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a json representation of a TrustedProfileTemplateClaimRule model
        trusted_profile_template_claim_rule_model_json = {}
        trusted_profile_template_claim_rule_model_json['name'] = 'testString'
        trusted_profile_template_claim_rule_model_json['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model_json['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model_json['expiration'] = 38
        trusted_profile_template_claim_rule_model_json['conditions'] = [profile_claim_rule_conditions_model]

        # Construct a model instance of TrustedProfileTemplateClaimRule by calling from_dict on the json representation
        trusted_profile_template_claim_rule_model = TrustedProfileTemplateClaimRule.from_dict(
            trusted_profile_template_claim_rule_model_json
        )
        assert trusted_profile_template_claim_rule_model != False

        # Construct a model instance of TrustedProfileTemplateClaimRule by calling from_dict on the json representation
        trusted_profile_template_claim_rule_model_dict = TrustedProfileTemplateClaimRule.from_dict(
            trusted_profile_template_claim_rule_model_json
        ).__dict__
        trusted_profile_template_claim_rule_model2 = TrustedProfileTemplateClaimRule(
            **trusted_profile_template_claim_rule_model_dict
        )

        # Verify the model instances are equivalent
        assert trusted_profile_template_claim_rule_model == trusted_profile_template_claim_rule_model2

        # Convert model instance back to dict and verify no loss of data
        trusted_profile_template_claim_rule_model_json2 = trusted_profile_template_claim_rule_model.to_dict()
        assert trusted_profile_template_claim_rule_model_json2 == trusted_profile_template_claim_rule_model_json


class TestModel_TrustedProfileTemplateList:
    """
    Test Class for TrustedProfileTemplateList
    """

    def test_trusted_profile_template_list_serialization(self):
        """
        Test serialization/deserialization for TrustedProfileTemplateList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        profile_claim_rule_conditions_model = {}  # ProfileClaimRuleConditions
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        trusted_profile_template_claim_rule_model = {}  # TrustedProfileTemplateClaimRule
        trusted_profile_template_claim_rule_model['name'] = 'testString'
        trusted_profile_template_claim_rule_model['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model['expiration'] = 38
        trusted_profile_template_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        profile_identity_response_model = {}  # ProfileIdentityResponse
        profile_identity_response_model['iam_id'] = 'testString'
        profile_identity_response_model['identifier'] = 'testString'
        profile_identity_response_model['type'] = 'user'
        profile_identity_response_model['accounts'] = ['testString']
        profile_identity_response_model['description'] = 'testString'

        template_profile_component_response_model = {}  # TemplateProfileComponentResponse
        template_profile_component_response_model['name'] = 'testString'
        template_profile_component_response_model['description'] = 'testString'
        template_profile_component_response_model['rules'] = [trusted_profile_template_claim_rule_model]
        template_profile_component_response_model['identities'] = [profile_identity_response_model]

        policy_template_reference_model = {}  # PolicyTemplateReference
        policy_template_reference_model['id'] = 'testString'
        policy_template_reference_model['version'] = 'testString'

        action_controls_identities_model = {}  # ActionControlsIdentities
        action_controls_identities_model['add'] = True
        action_controls_identities_model['remove'] = True

        action_controls_rules_model = {}  # ActionControlsRules
        action_controls_rules_model['add'] = True
        action_controls_rules_model['remove'] = True

        action_controls_policies_model = {}  # ActionControlsPolicies
        action_controls_policies_model['add'] = True
        action_controls_policies_model['remove'] = True

        action_controls_model = {}  # ActionControls
        action_controls_model['identities'] = action_controls_identities_model
        action_controls_model['rules'] = action_controls_rules_model
        action_controls_model['policies'] = action_controls_policies_model

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        trusted_profile_template_response_model = {}  # TrustedProfileTemplateResponse
        trusted_profile_template_response_model['id'] = 'testString'
        trusted_profile_template_response_model['version'] = 26
        trusted_profile_template_response_model['account_id'] = 'testString'
        trusted_profile_template_response_model['name'] = 'testString'
        trusted_profile_template_response_model['description'] = 'testString'
        trusted_profile_template_response_model['committed'] = True
        trusted_profile_template_response_model['profile'] = template_profile_component_response_model
        trusted_profile_template_response_model['policy_template_references'] = [policy_template_reference_model]
        trusted_profile_template_response_model['action_controls'] = action_controls_model
        trusted_profile_template_response_model['history'] = [enity_history_record_model]
        trusted_profile_template_response_model['entity_tag'] = 'testString'
        trusted_profile_template_response_model['crn'] = 'testString'
        trusted_profile_template_response_model['created_at'] = 'testString'
        trusted_profile_template_response_model['created_by_id'] = 'testString'
        trusted_profile_template_response_model['last_modified_at'] = 'testString'
        trusted_profile_template_response_model['last_modified_by_id'] = 'testString'

        # Construct a json representation of a TrustedProfileTemplateList model
        trusted_profile_template_list_model_json = {}
        trusted_profile_template_list_model_json['context'] = response_context_model
        trusted_profile_template_list_model_json['offset'] = 26
        trusted_profile_template_list_model_json['limit'] = 20
        trusted_profile_template_list_model_json['first'] = 'testString'
        trusted_profile_template_list_model_json['previous'] = 'testString'
        trusted_profile_template_list_model_json['next'] = 'testString'
        trusted_profile_template_list_model_json['profile_templates'] = [trusted_profile_template_response_model]

        # Construct a model instance of TrustedProfileTemplateList by calling from_dict on the json representation
        trusted_profile_template_list_model = TrustedProfileTemplateList.from_dict(
            trusted_profile_template_list_model_json
        )
        assert trusted_profile_template_list_model != False

        # Construct a model instance of TrustedProfileTemplateList by calling from_dict on the json representation
        trusted_profile_template_list_model_dict = TrustedProfileTemplateList.from_dict(
            trusted_profile_template_list_model_json
        ).__dict__
        trusted_profile_template_list_model2 = TrustedProfileTemplateList(**trusted_profile_template_list_model_dict)

        # Verify the model instances are equivalent
        assert trusted_profile_template_list_model == trusted_profile_template_list_model2

        # Convert model instance back to dict and verify no loss of data
        trusted_profile_template_list_model_json2 = trusted_profile_template_list_model.to_dict()
        assert trusted_profile_template_list_model_json2 == trusted_profile_template_list_model_json


class TestModel_TrustedProfileTemplateResponse:
    """
    Test Class for TrustedProfileTemplateResponse
    """

    def test_trusted_profile_template_response_serialization(self):
        """
        Test serialization/deserialization for TrustedProfileTemplateResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_claim_rule_conditions_model = {}  # ProfileClaimRuleConditions
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        trusted_profile_template_claim_rule_model = {}  # TrustedProfileTemplateClaimRule
        trusted_profile_template_claim_rule_model['name'] = 'testString'
        trusted_profile_template_claim_rule_model['type'] = 'Profile-SAML'
        trusted_profile_template_claim_rule_model['realm_name'] = 'testString'
        trusted_profile_template_claim_rule_model['expiration'] = 38
        trusted_profile_template_claim_rule_model['conditions'] = [profile_claim_rule_conditions_model]

        profile_identity_response_model = {}  # ProfileIdentityResponse
        profile_identity_response_model['iam_id'] = 'testString'
        profile_identity_response_model['identifier'] = 'testString'
        profile_identity_response_model['type'] = 'user'
        profile_identity_response_model['accounts'] = ['testString']
        profile_identity_response_model['description'] = 'testString'

        template_profile_component_response_model = {}  # TemplateProfileComponentResponse
        template_profile_component_response_model['name'] = 'testString'
        template_profile_component_response_model['description'] = 'testString'
        template_profile_component_response_model['rules'] = [trusted_profile_template_claim_rule_model]
        template_profile_component_response_model['identities'] = [profile_identity_response_model]

        policy_template_reference_model = {}  # PolicyTemplateReference
        policy_template_reference_model['id'] = 'testString'
        policy_template_reference_model['version'] = 'testString'

        action_controls_identities_model = {}  # ActionControlsIdentities
        action_controls_identities_model['add'] = True
        action_controls_identities_model['remove'] = True

        action_controls_rules_model = {}  # ActionControlsRules
        action_controls_rules_model['add'] = True
        action_controls_rules_model['remove'] = True

        action_controls_policies_model = {}  # ActionControlsPolicies
        action_controls_policies_model['add'] = True
        action_controls_policies_model['remove'] = True

        action_controls_model = {}  # ActionControls
        action_controls_model['identities'] = action_controls_identities_model
        action_controls_model['rules'] = action_controls_rules_model
        action_controls_model['policies'] = action_controls_policies_model

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        # Construct a json representation of a TrustedProfileTemplateResponse model
        trusted_profile_template_response_model_json = {}
        trusted_profile_template_response_model_json['id'] = 'testString'
        trusted_profile_template_response_model_json['version'] = 26
        trusted_profile_template_response_model_json['account_id'] = 'testString'
        trusted_profile_template_response_model_json['name'] = 'testString'
        trusted_profile_template_response_model_json['description'] = 'testString'
        trusted_profile_template_response_model_json['committed'] = True
        trusted_profile_template_response_model_json['profile'] = template_profile_component_response_model
        trusted_profile_template_response_model_json['policy_template_references'] = [policy_template_reference_model]
        trusted_profile_template_response_model_json['action_controls'] = action_controls_model
        trusted_profile_template_response_model_json['history'] = [enity_history_record_model]
        trusted_profile_template_response_model_json['entity_tag'] = 'testString'
        trusted_profile_template_response_model_json['crn'] = 'testString'
        trusted_profile_template_response_model_json['created_at'] = 'testString'
        trusted_profile_template_response_model_json['created_by_id'] = 'testString'
        trusted_profile_template_response_model_json['last_modified_at'] = 'testString'
        trusted_profile_template_response_model_json['last_modified_by_id'] = 'testString'

        # Construct a model instance of TrustedProfileTemplateResponse by calling from_dict on the json representation
        trusted_profile_template_response_model = TrustedProfileTemplateResponse.from_dict(
            trusted_profile_template_response_model_json
        )
        assert trusted_profile_template_response_model != False

        # Construct a model instance of TrustedProfileTemplateResponse by calling from_dict on the json representation
        trusted_profile_template_response_model_dict = TrustedProfileTemplateResponse.from_dict(
            trusted_profile_template_response_model_json
        ).__dict__
        trusted_profile_template_response_model2 = TrustedProfileTemplateResponse(
            **trusted_profile_template_response_model_dict
        )

        # Verify the model instances are equivalent
        assert trusted_profile_template_response_model == trusted_profile_template_response_model2

        # Convert model instance back to dict and verify no loss of data
        trusted_profile_template_response_model_json2 = trusted_profile_template_response_model.to_dict()
        assert trusted_profile_template_response_model_json2 == trusted_profile_template_response_model_json


class TestModel_TrustedProfilesList:
    """
    Test Class for TrustedProfilesList
    """

    def test_trusted_profiles_list_serialization(self):
        """
        Test serialization/deserialization for TrustedProfilesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {}  # ResponseContext
        response_context_model['transaction_id'] = 'testString'
        response_context_model['operation'] = 'testString'
        response_context_model['user_agent'] = 'testString'
        response_context_model['url'] = 'testString'
        response_context_model['instance_id'] = 'testString'
        response_context_model['thread_id'] = 'testString'
        response_context_model['host'] = 'testString'
        response_context_model['start_time'] = 'testString'
        response_context_model['end_time'] = 'testString'
        response_context_model['elapsed_time'] = 'testString'
        response_context_model['cluster_name'] = 'testString'

        enity_history_record_model = {}  # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        activity_model = {}  # Activity
        activity_model['last_authn'] = 'testString'
        activity_model['authn_count'] = 26

        trusted_profile_model = {}  # TrustedProfile
        trusted_profile_model['context'] = response_context_model
        trusted_profile_model['id'] = 'testString'
        trusted_profile_model['entity_tag'] = 'testString'
        trusted_profile_model['crn'] = 'testString'
        trusted_profile_model['name'] = 'testString'
        trusted_profile_model['description'] = 'testString'
        trusted_profile_model['created_at'] = '2019-01-01T12:00:00Z'
        trusted_profile_model['modified_at'] = '2019-01-01T12:00:00Z'
        trusted_profile_model['iam_id'] = 'testString'
        trusted_profile_model['account_id'] = 'testString'
        trusted_profile_model['template_id'] = 'testString'
        trusted_profile_model['assignment_id'] = 'testString'
        trusted_profile_model['ims_account_id'] = 26
        trusted_profile_model['ims_user_id'] = 26
        trusted_profile_model['history'] = [enity_history_record_model]
        trusted_profile_model['activity'] = activity_model

        # Construct a json representation of a TrustedProfilesList model
        trusted_profiles_list_model_json = {}
        trusted_profiles_list_model_json['context'] = response_context_model
        trusted_profiles_list_model_json['offset'] = 26
        trusted_profiles_list_model_json['limit'] = 26
        trusted_profiles_list_model_json['first'] = 'testString'
        trusted_profiles_list_model_json['previous'] = 'testString'
        trusted_profiles_list_model_json['next'] = 'testString'
        trusted_profiles_list_model_json['profiles'] = [trusted_profile_model]

        # Construct a model instance of TrustedProfilesList by calling from_dict on the json representation
        trusted_profiles_list_model = TrustedProfilesList.from_dict(trusted_profiles_list_model_json)
        assert trusted_profiles_list_model != False

        # Construct a model instance of TrustedProfilesList by calling from_dict on the json representation
        trusted_profiles_list_model_dict = TrustedProfilesList.from_dict(trusted_profiles_list_model_json).__dict__
        trusted_profiles_list_model2 = TrustedProfilesList(**trusted_profiles_list_model_dict)

        # Verify the model instances are equivalent
        assert trusted_profiles_list_model == trusted_profiles_list_model2

        # Convert model instance back to dict and verify no loss of data
        trusted_profiles_list_model_json2 = trusted_profiles_list_model.to_dict()
        assert trusted_profiles_list_model_json2 == trusted_profiles_list_model_json


class TestModel_UserActivity:
    """
    Test Class for UserActivity
    """

    def test_user_activity_serialization(self):
        """
        Test serialization/deserialization for UserActivity
        """

        # Construct a json representation of a UserActivity model
        user_activity_model_json = {}
        user_activity_model_json['iam_id'] = 'testString'
        user_activity_model_json['name'] = 'testString'
        user_activity_model_json['username'] = 'testString'
        user_activity_model_json['email'] = 'testString'
        user_activity_model_json['last_authn'] = 'testString'

        # Construct a model instance of UserActivity by calling from_dict on the json representation
        user_activity_model = UserActivity.from_dict(user_activity_model_json)
        assert user_activity_model != False

        # Construct a model instance of UserActivity by calling from_dict on the json representation
        user_activity_model_dict = UserActivity.from_dict(user_activity_model_json).__dict__
        user_activity_model2 = UserActivity(**user_activity_model_dict)

        # Verify the model instances are equivalent
        assert user_activity_model == user_activity_model2

        # Convert model instance back to dict and verify no loss of data
        user_activity_model_json2 = user_activity_model.to_dict()
        assert user_activity_model_json2 == user_activity_model_json


class TestModel_UserMfaEnrollments:
    """
    Test Class for UserMfaEnrollments
    """

    def test_user_mfa_enrollments_serialization(self):
        """
        Test serialization/deserialization for UserMfaEnrollments
        """

        # Construct dict forms of any model objects needed in order to build this model.

        id_based_mfa_enrollment_model = {}  # IdBasedMfaEnrollment
        id_based_mfa_enrollment_model['trait_account_default'] = 'NONE'
        id_based_mfa_enrollment_model['trait_user_specific'] = 'NONE'
        id_based_mfa_enrollment_model['trait_effective'] = 'NONE'
        id_based_mfa_enrollment_model['complies'] = True
        id_based_mfa_enrollment_model['comply_state'] = 'NO'

        mfa_enrollment_type_status_model = {}  # MfaEnrollmentTypeStatus
        mfa_enrollment_type_status_model['required'] = True
        mfa_enrollment_type_status_model['enrolled'] = True

        account_based_mfa_enrollment_model = {}  # AccountBasedMfaEnrollment
        account_based_mfa_enrollment_model['security_questions'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['totp'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['verisign'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['complies'] = True

        # Construct a json representation of a UserMfaEnrollments model
        user_mfa_enrollments_model_json = {}
        user_mfa_enrollments_model_json['iam_id'] = 'testString'
        user_mfa_enrollments_model_json['effective_mfa_type'] = 'testString'
        user_mfa_enrollments_model_json['id_based_mfa'] = id_based_mfa_enrollment_model
        user_mfa_enrollments_model_json['account_based_mfa'] = account_based_mfa_enrollment_model

        # Construct a model instance of UserMfaEnrollments by calling from_dict on the json representation
        user_mfa_enrollments_model = UserMfaEnrollments.from_dict(user_mfa_enrollments_model_json)
        assert user_mfa_enrollments_model != False

        # Construct a model instance of UserMfaEnrollments by calling from_dict on the json representation
        user_mfa_enrollments_model_dict = UserMfaEnrollments.from_dict(user_mfa_enrollments_model_json).__dict__
        user_mfa_enrollments_model2 = UserMfaEnrollments(**user_mfa_enrollments_model_dict)

        # Verify the model instances are equivalent
        assert user_mfa_enrollments_model == user_mfa_enrollments_model2

        # Convert model instance back to dict and verify no loss of data
        user_mfa_enrollments_model_json2 = user_mfa_enrollments_model.to_dict()
        assert user_mfa_enrollments_model_json2 == user_mfa_enrollments_model_json


class TestModel_UserReportMfaEnrollmentStatus:
    """
    Test Class for UserReportMfaEnrollmentStatus
    """

    def test_user_report_mfa_enrollment_status_serialization(self):
        """
        Test serialization/deserialization for UserReportMfaEnrollmentStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        id_based_mfa_enrollment_model = {}  # IdBasedMfaEnrollment
        id_based_mfa_enrollment_model['trait_account_default'] = 'NONE'
        id_based_mfa_enrollment_model['trait_user_specific'] = 'NONE'
        id_based_mfa_enrollment_model['trait_effective'] = 'NONE'
        id_based_mfa_enrollment_model['complies'] = True
        id_based_mfa_enrollment_model['comply_state'] = 'NO'

        mfa_enrollment_type_status_model = {}  # MfaEnrollmentTypeStatus
        mfa_enrollment_type_status_model['required'] = True
        mfa_enrollment_type_status_model['enrolled'] = True

        account_based_mfa_enrollment_model = {}  # AccountBasedMfaEnrollment
        account_based_mfa_enrollment_model['security_questions'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['totp'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['verisign'] = mfa_enrollment_type_status_model
        account_based_mfa_enrollment_model['complies'] = True

        mfa_enrollments_model = {}  # MfaEnrollments
        mfa_enrollments_model['effective_mfa_type'] = 'testString'
        mfa_enrollments_model['id_based_mfa'] = id_based_mfa_enrollment_model
        mfa_enrollments_model['account_based_mfa'] = account_based_mfa_enrollment_model

        # Construct a json representation of a UserReportMfaEnrollmentStatus model
        user_report_mfa_enrollment_status_model_json = {}
        user_report_mfa_enrollment_status_model_json['iam_id'] = 'testString'
        user_report_mfa_enrollment_status_model_json['name'] = 'testString'
        user_report_mfa_enrollment_status_model_json['username'] = 'testString'
        user_report_mfa_enrollment_status_model_json['email'] = 'testString'
        user_report_mfa_enrollment_status_model_json['enrollments'] = mfa_enrollments_model

        # Construct a model instance of UserReportMfaEnrollmentStatus by calling from_dict on the json representation
        user_report_mfa_enrollment_status_model = UserReportMfaEnrollmentStatus.from_dict(
            user_report_mfa_enrollment_status_model_json
        )
        assert user_report_mfa_enrollment_status_model != False

        # Construct a model instance of UserReportMfaEnrollmentStatus by calling from_dict on the json representation
        user_report_mfa_enrollment_status_model_dict = UserReportMfaEnrollmentStatus.from_dict(
            user_report_mfa_enrollment_status_model_json
        ).__dict__
        user_report_mfa_enrollment_status_model2 = UserReportMfaEnrollmentStatus(
            **user_report_mfa_enrollment_status_model_dict
        )

        # Verify the model instances are equivalent
        assert user_report_mfa_enrollment_status_model == user_report_mfa_enrollment_status_model2

        # Convert model instance back to dict and verify no loss of data
        user_report_mfa_enrollment_status_model_json2 = user_report_mfa_enrollment_status_model.to_dict()
        assert user_report_mfa_enrollment_status_model_json2 == user_report_mfa_enrollment_status_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
