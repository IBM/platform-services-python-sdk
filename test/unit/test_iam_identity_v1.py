# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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


_service = IamIdentityV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://iam.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: APIKeyOperations
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
            )

class TestListApiKeys():
    """
    Test Class for list_api_keys
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
    def test_list_api_keys_all_params(self):
        """
        list_api_keys()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "apikeys": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
        assert 'pagesize={}'.format(pagesize) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'scope={}'.format(scope) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string


    @responses.activate
    def test_list_api_keys_required_params(self):
        """
        test_list_api_keys_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "apikeys": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_api_keys()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateApiKey():
    """
    Test Class for create_api_key
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
    def test_create_api_key_all_params(self):
        """
        create_api_key()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        iam_id = 'testString'
        description = 'testString'
        account_id = 'testString'
        apikey = 'testString'
        store_value = True
        entity_lock = 'false'

        # Invoke method
        response = _service.create_api_key(
            name,
            iam_id,
            description=description,
            account_id=account_id,
            apikey=apikey,
            store_value=store_value,
            entity_lock=entity_lock,
            headers={}
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


    @responses.activate
    def test_create_api_key_required_params(self):
        """
        test_create_api_key_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        iam_id = 'testString'
        description = 'testString'
        account_id = 'testString'
        apikey = 'testString'
        store_value = True

        # Invoke method
        response = _service.create_api_key(
            name,
            iam_id,
            description=description,
            account_id=account_id,
            apikey=apikey,
            store_value=store_value,
            headers={}
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


    @responses.activate
    def test_create_api_key_value_error(self):
        """
        test_create_api_key_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        iam_id = 'testString'
        description = 'testString'
        account_id = 'testString'
        apikey = 'testString'
        store_value = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_api_key(**req_copy)



class TestGetApiKeysDetails():
    """
    Test Class for get_api_keys_details
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
    def test_get_api_keys_details_all_params(self):
        """
        get_api_keys_details()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/details')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        iam_api_key = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_api_keys_details(
            iam_api_key=iam_api_key,
            include_history=include_history,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string


    @responses.activate
    def test_get_api_keys_details_required_params(self):
        """
        test_get_api_keys_details_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/details')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_api_keys_details()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetApiKey():
    """
    Test Class for get_api_key
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
    def test_get_api_key_all_params(self):
        """
        get_api_key()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_api_key(
            id,
            include_history=include_history,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string


    @responses.activate
    def test_get_api_key_required_params(self):
        """
        test_get_api_key_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_api_key(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_api_key_value_error(self):
        """
        test_get_api_key_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_api_key(**req_copy)



class TestUpdateApiKey():
    """
    Test Class for update_api_key
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
    def test_update_api_key_all_params(self):
        """
        update_api_key()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.update_api_key(
            id,
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
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'


    @responses.activate
    def test_update_api_key_value_error(self):
        """
        test_update_api_key_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_api_key(**req_copy)



class TestDeleteApiKey():
    """
    Test Class for delete_api_key
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
    def test_delete_api_key_all_params(self):
        """
        delete_api_key()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_api_key(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_api_key_value_error(self):
        """
        test_delete_api_key_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_api_key(**req_copy)



class TestLockApiKey():
    """
    Test Class for lock_api_key
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
    def test_lock_api_key_all_params(self):
        """
        lock_api_key()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString/lock')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.lock_api_key(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_lock_api_key_value_error(self):
        """
        test_lock_api_key_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString/lock')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.lock_api_key(**req_copy)



class TestUnlockApiKey():
    """
    Test Class for unlock_api_key
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
    def test_unlock_api_key_all_params(self):
        """
        unlock_api_key()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString/lock')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.unlock_api_key(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_unlock_api_key_value_error(self):
        """
        test_unlock_api_key_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/apikeys/testString/lock')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.unlock_api_key(**req_copy)



# endregion
##############################################################################
# End of Service: APIKeyOperations
##############################################################################

##############################################################################
# Start of Service: ServiceIDOperations
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
            )

class TestListServiceIds():
    """
    Test Class for list_service_ids
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
    def test_list_service_ids_all_params(self):
        """
        list_service_ids()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "serviceids": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'pagesize={}'.format(pagesize) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string


    @responses.activate
    def test_list_service_ids_required_params(self):
        """
        test_list_service_ids_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "serviceids": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_service_ids()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateServiceId():
    """
    Test Class for create_service_id
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
    def test_create_service_id_all_params(self):
        """
        create_service_id()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

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
            headers={}
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


    @responses.activate
    def test_create_service_id_required_params(self):
        """
        test_create_service_id_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

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
            headers={}
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


    @responses.activate
    def test_create_service_id_value_error(self):
        """
        test_create_service_id_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_service_id(**req_copy)



class TestGetServiceId():
    """
    Test Class for get_service_id
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
    def test_get_service_id_all_params(self):
        """
        get_service_id()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_service_id(
            id,
            include_history=include_history,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string


    @responses.activate
    def test_get_service_id_required_params(self):
        """
        test_get_service_id_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_service_id(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_service_id_value_error(self):
        """
        test_get_service_id_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_service_id(**req_copy)



class TestUpdateServiceId():
    """
    Test Class for update_service_id
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
    def test_update_service_id_all_params(self):
        """
        update_service_id()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['unique_instance_crns'] == ['testString']


    @responses.activate
    def test_update_service_id_value_error(self):
        """
        test_update_service_id_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_service_id(**req_copy)



class TestDeleteServiceId():
    """
    Test Class for delete_service_id
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
    def test_delete_service_id_all_params(self):
        """
        delete_service_id()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_service_id(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_service_id_value_error(self):
        """
        test_delete_service_id_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_service_id(**req_copy)



class TestLockServiceId():
    """
    Test Class for lock_service_id
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
    def test_lock_service_id_all_params(self):
        """
        lock_service_id()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString/lock')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.lock_service_id(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_lock_service_id_value_error(self):
        """
        test_lock_service_id_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString/lock')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.lock_service_id(**req_copy)



class TestUnlockServiceId():
    """
    Test Class for unlock_service_id
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
    def test_unlock_service_id_all_params(self):
        """
        unlock_service_id()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString/lock')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.unlock_service_id(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_unlock_service_id_value_error(self):
        """
        test_unlock_service_id_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/serviceids/testString/lock')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.unlock_service_id(**req_copy)



# endregion
##############################################################################
# End of Service: ServiceIDOperations
##############################################################################

##############################################################################
# Start of Service: TrustedProfilesOperations
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
            )

class TestCreateProfile():
    """
    Test Class for create_profile
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
    def test_create_profile_all_params(self):
        """
        create_profile()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        account_id = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.create_profile(
            name,
            account_id,
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
        assert req_body['description'] == 'testString'


    @responses.activate
    def test_create_profile_value_error(self):
        """
        test_create_profile_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_profile(**req_copy)



class TestListProfiles():
    """
    Test Class for list_profiles
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
    def test_list_profiles_all_params(self):
        """
        list_profiles()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "profiles": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'pagesize={}'.format(pagesize) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string


    @responses.activate
    def test_list_profiles_required_params(self):
        """
        test_list_profiles_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "profiles": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_profiles(
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


    @responses.activate
    def test_list_profiles_value_error(self):
        """
        test_list_profiles_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "profiles": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}]}'
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
                _service.list_profiles(**req_copy)



class TestGetProfile():
    """
    Test Class for get_profile
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
    def test_get_profile_all_params(self):
        """
        get_profile()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'

        # Invoke method
        response = _service.get_profile(
            profile_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_profile_value_error(self):
        """
        test_get_profile_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_profile(**req_copy)



class TestUpdateProfile():
    """
    Test Class for update_profile
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
    def test_update_profile_all_params(self):
        """
        update_profile()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'


    @responses.activate
    def test_update_profile_value_error(self):
        """
        test_update_profile_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "name": "name", "description": "description", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "iam_id": "iam_id", "account_id": "account_id", "ims_account_id": 14, "ims_user_id": 11, "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_profile(**req_copy)



class TestDeleteProfile():
    """
    Test Class for delete_profile
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
    def test_delete_profile_all_params(self):
        """
        delete_profile()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        profile_id = 'testString'

        # Invoke method
        response = _service.delete_profile(
            profile_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_profile_value_error(self):
        """
        test_delete_profile_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_profile(**req_copy)



class TestCreateClaimRule():
    """
    Test Class for create_claim_rule
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
    def test_create_claim_rule_all_params(self):
        """
        create_claim_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

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
            headers={}
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


    @responses.activate
    def test_create_claim_rule_value_error(self):
        """
        test_create_claim_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_claim_rule(**req_copy)



class TestListClaimRules():
    """
    Test Class for list_claim_rules
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
    def test_list_claim_rules_all_params(self):
        """
        list_claim_rules()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "rules": [{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'

        # Invoke method
        response = _service.list_claim_rules(
            profile_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_claim_rules_value_error(self):
        """
        test_list_claim_rules_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "rules": [{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_claim_rules(**req_copy)



class TestGetClaimRule():
    """
    Test Class for get_claim_rule
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
    def test_get_claim_rule_all_params(self):
        """
        get_claim_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.get_claim_rule(
            profile_id,
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_claim_rule_value_error(self):
        """
        test_get_claim_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_claim_rule(**req_copy)



class TestUpdateClaimRule():
    """
    Test Class for update_claim_rule
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
    def test_update_claim_rule_all_params(self):
        """
        update_claim_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            headers={}
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


    @responses.activate
    def test_update_claim_rule_value_error(self):
        """
        test_update_claim_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "type": "type", "realm_name": "realm_name", "expiration": 10, "cr_type": "cr_type", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_claim_rule(**req_copy)



class TestDeleteClaimRule():
    """
    Test Class for delete_claim_rule
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
    def test_delete_claim_rule_all_params(self):
        """
        delete_claim_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.delete_claim_rule(
            profile_id,
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_claim_rule_value_error(self):
        """
        test_delete_claim_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        profile_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_claim_rule(**req_copy)



class TestCreateLink():
    """
    Test Class for create_link
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
    def test_create_link_all_params(self):
        """
        create_link()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/links')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cr_type'] == 'testString'
        assert req_body['link'] == create_profile_link_request_link_model
        assert req_body['name'] == 'testString'


    @responses.activate
    def test_create_link_value_error(self):
        """
        test_create_link_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/links')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_link(**req_copy)



class TestListLinks():
    """
    Test Class for list_links
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
    def test_list_links_all_params(self):
        """
        list_links()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/links')
        mock_response = '{"links": [{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'

        # Invoke method
        response = _service.list_links(
            profile_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_links_value_error(self):
        """
        test_list_links_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/links')
        mock_response = '{"links": [{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_links(**req_copy)



class TestGetLink():
    """
    Test Class for get_link
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
    def test_get_link_all_params(self):
        """
        get_link()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/links/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'
        link_id = 'testString'

        # Invoke method
        response = _service.get_link(
            profile_id,
            link_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_link_value_error(self):
        """
        test_get_link_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/links/testString')
        mock_response = '{"id": "id", "entity_tag": "entity_tag", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "cr_type": "cr_type", "link": {"crn": "crn", "namespace": "namespace", "name": "name"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        profile_id = 'testString'
        link_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "link_id": link_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_link(**req_copy)



class TestDeleteLink():
    """
    Test Class for delete_link
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
    def test_delete_link_all_params(self):
        """
        delete_link()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/links/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        profile_id = 'testString'
        link_id = 'testString'

        # Invoke method
        response = _service.delete_link(
            profile_id,
            link_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_link_value_error(self):
        """
        test_delete_link_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/profiles/testString/links/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        profile_id = 'testString'
        link_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_id": profile_id,
            "link_id": link_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_link(**req_copy)



# endregion
##############################################################################
# End of Service: TrustedProfilesOperations
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
        url = self.preprocess_url(_base_url + '/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        include_history = False

        # Invoke method
        response = _service.get_account_settings(
            account_id,
            include_history=include_history,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_history={}'.format('true' if include_history else 'false') in query_string


    @responses.activate
    def test_get_account_settings_required_params(self):
        """
        test_get_account_settings_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity"}'
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


    @responses.activate
    def test_get_account_settings_value_error(self):
        """
        test_get_account_settings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity"}'
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
        url = self.preprocess_url(_base_url + '/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        if_match = 'testString'
        account_id = 'testString'
        restrict_create_service_id = 'RESTRICTED'
        restrict_create_platform_apikey = 'RESTRICTED'
        allowed_ip_addresses = 'testString'
        mfa = 'NONE'
        session_expiration_in_seconds = '86400'
        session_invalidation_in_seconds = '7200'
        max_sessions_per_identity = 'testString'

        # Invoke method
        response = _service.update_account_settings(
            if_match,
            account_id,
            restrict_create_service_id=restrict_create_service_id,
            restrict_create_platform_apikey=restrict_create_platform_apikey,
            allowed_ip_addresses=allowed_ip_addresses,
            mfa=mfa,
            session_expiration_in_seconds=session_expiration_in_seconds,
            session_invalidation_in_seconds=session_invalidation_in_seconds,
            max_sessions_per_identity=max_sessions_per_identity,
            headers={}
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
        assert req_body['session_expiration_in_seconds'] == '86400'
        assert req_body['session_invalidation_in_seconds'] == '7200'
        assert req_body['max_sessions_per_identity'] == 'testString'


    @responses.activate
    def test_update_account_settings_value_error(self):
        """
        test_update_account_settings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/accounts/testString/settings/identity')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "account_id": "account_id", "restrict_create_service_id": "NOT_SET", "restrict_create_platform_apikey": "NOT_SET", "allowed_ip_addresses": "allowed_ip_addresses", "entity_tag": "entity_tag", "mfa": "NONE", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "session_expiration_in_seconds": "86400", "session_invalidation_in_seconds": "7200", "max_sessions_per_identity": "max_sessions_per_identity"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        if_match = 'testString'
        account_id = 'testString'
        restrict_create_service_id = 'RESTRICTED'
        restrict_create_platform_apikey = 'RESTRICTED'
        allowed_ip_addresses = 'testString'
        mfa = 'NONE'
        session_expiration_in_seconds = '86400'
        session_invalidation_in_seconds = '7200'
        max_sessions_per_identity = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "if_match": if_match,
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_account_settings(**req_copy)



# endregion
##############################################################################
# End of Service: AccountSettings
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AccountSettingsResponse():
    """
    Test Class for AccountSettingsResponse
    """

    def test_account_settings_response_serialization(self):
        """
        Test serialization/deserialization for AccountSettingsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {} # ResponseContext
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

        enity_history_record_model = {} # EnityHistoryRecord
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
        account_settings_response_model_json['history'] = [enity_history_record_model]
        account_settings_response_model_json['session_expiration_in_seconds'] = '86400'
        account_settings_response_model_json['session_invalidation_in_seconds'] = '7200'
        account_settings_response_model_json['max_sessions_per_identity'] = 'testString'

        # Construct a model instance of AccountSettingsResponse by calling from_dict on the json representation
        account_settings_response_model = AccountSettingsResponse.from_dict(account_settings_response_model_json)
        assert account_settings_response_model != False

        # Construct a model instance of AccountSettingsResponse by calling from_dict on the json representation
        account_settings_response_model_dict = AccountSettingsResponse.from_dict(account_settings_response_model_json).__dict__
        account_settings_response_model2 = AccountSettingsResponse(**account_settings_response_model_dict)

        # Verify the model instances are equivalent
        assert account_settings_response_model == account_settings_response_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_response_model_json2 = account_settings_response_model.to_dict()
        assert account_settings_response_model_json2 == account_settings_response_model_json

class TestModel_ApiKey():
    """
    Test Class for ApiKey
    """

    def test_api_key_serialization(self):
        """
        Test serialization/deserialization for ApiKey
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {} # ResponseContext
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

        enity_history_record_model = {} # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        # Construct a json representation of a ApiKey model
        api_key_model_json = {}
        api_key_model_json['context'] = response_context_model
        api_key_model_json['id'] = 'testString'
        api_key_model_json['entity_tag'] = 'testString'
        api_key_model_json['crn'] = 'testString'
        api_key_model_json['locked'] = True
        api_key_model_json['created_at'] = "2019-01-01T12:00:00Z"
        api_key_model_json['created_by'] = 'testString'
        api_key_model_json['modified_at'] = "2019-01-01T12:00:00Z"
        api_key_model_json['name'] = 'testString'
        api_key_model_json['description'] = 'testString'
        api_key_model_json['iam_id'] = 'testString'
        api_key_model_json['account_id'] = 'testString'
        api_key_model_json['apikey'] = 'testString'
        api_key_model_json['history'] = [enity_history_record_model]

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

class TestModel_ApiKeyInsideCreateServiceIdRequest():
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
        api_key_inside_create_service_id_request_model = ApiKeyInsideCreateServiceIdRequest.from_dict(api_key_inside_create_service_id_request_model_json)
        assert api_key_inside_create_service_id_request_model != False

        # Construct a model instance of ApiKeyInsideCreateServiceIdRequest by calling from_dict on the json representation
        api_key_inside_create_service_id_request_model_dict = ApiKeyInsideCreateServiceIdRequest.from_dict(api_key_inside_create_service_id_request_model_json).__dict__
        api_key_inside_create_service_id_request_model2 = ApiKeyInsideCreateServiceIdRequest(**api_key_inside_create_service_id_request_model_dict)

        # Verify the model instances are equivalent
        assert api_key_inside_create_service_id_request_model == api_key_inside_create_service_id_request_model2

        # Convert model instance back to dict and verify no loss of data
        api_key_inside_create_service_id_request_model_json2 = api_key_inside_create_service_id_request_model.to_dict()
        assert api_key_inside_create_service_id_request_model_json2 == api_key_inside_create_service_id_request_model_json

class TestModel_ApiKeyList():
    """
    Test Class for ApiKeyList
    """

    def test_api_key_list_serialization(self):
        """
        Test serialization/deserialization for ApiKeyList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {} # ResponseContext
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

        enity_history_record_model = {} # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        api_key_model = {} # ApiKey
        api_key_model['context'] = response_context_model
        api_key_model['id'] = 'testString'
        api_key_model['entity_tag'] = 'testString'
        api_key_model['crn'] = 'testString'
        api_key_model['locked'] = True
        api_key_model['created_at'] = "2019-01-01T12:00:00Z"
        api_key_model['created_by'] = 'testString'
        api_key_model['modified_at'] = "2019-01-01T12:00:00Z"
        api_key_model['name'] = 'testString'
        api_key_model['description'] = 'testString'
        api_key_model['iam_id'] = 'testString'
        api_key_model['account_id'] = 'testString'
        api_key_model['apikey'] = 'testString'
        api_key_model['history'] = [enity_history_record_model]

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

class TestModel_CreateProfileLinkRequestLink():
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
        create_profile_link_request_link_model = CreateProfileLinkRequestLink.from_dict(create_profile_link_request_link_model_json)
        assert create_profile_link_request_link_model != False

        # Construct a model instance of CreateProfileLinkRequestLink by calling from_dict on the json representation
        create_profile_link_request_link_model_dict = CreateProfileLinkRequestLink.from_dict(create_profile_link_request_link_model_json).__dict__
        create_profile_link_request_link_model2 = CreateProfileLinkRequestLink(**create_profile_link_request_link_model_dict)

        # Verify the model instances are equivalent
        assert create_profile_link_request_link_model == create_profile_link_request_link_model2

        # Convert model instance back to dict and verify no loss of data
        create_profile_link_request_link_model_json2 = create_profile_link_request_link_model.to_dict()
        assert create_profile_link_request_link_model_json2 == create_profile_link_request_link_model_json

class TestModel_EnityHistoryRecord():
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

class TestModel_ProfileClaimRule():
    """
    Test Class for ProfileClaimRule
    """

    def test_profile_claim_rule_serialization(self):
        """
        Test serialization/deserialization for ProfileClaimRule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_claim_rule_conditions_model = {} # ProfileClaimRuleConditions
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        # Construct a json representation of a ProfileClaimRule model
        profile_claim_rule_model_json = {}
        profile_claim_rule_model_json['id'] = 'testString'
        profile_claim_rule_model_json['entity_tag'] = 'testString'
        profile_claim_rule_model_json['created_at'] = "2019-01-01T12:00:00Z"
        profile_claim_rule_model_json['modified_at'] = "2019-01-01T12:00:00Z"
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

class TestModel_ProfileClaimRuleConditions():
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
        profile_claim_rule_conditions_model = ProfileClaimRuleConditions.from_dict(profile_claim_rule_conditions_model_json)
        assert profile_claim_rule_conditions_model != False

        # Construct a model instance of ProfileClaimRuleConditions by calling from_dict on the json representation
        profile_claim_rule_conditions_model_dict = ProfileClaimRuleConditions.from_dict(profile_claim_rule_conditions_model_json).__dict__
        profile_claim_rule_conditions_model2 = ProfileClaimRuleConditions(**profile_claim_rule_conditions_model_dict)

        # Verify the model instances are equivalent
        assert profile_claim_rule_conditions_model == profile_claim_rule_conditions_model2

        # Convert model instance back to dict and verify no loss of data
        profile_claim_rule_conditions_model_json2 = profile_claim_rule_conditions_model.to_dict()
        assert profile_claim_rule_conditions_model_json2 == profile_claim_rule_conditions_model_json

class TestModel_ProfileClaimRuleList():
    """
    Test Class for ProfileClaimRuleList
    """

    def test_profile_claim_rule_list_serialization(self):
        """
        Test serialization/deserialization for ProfileClaimRuleList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {} # ResponseContext
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

        profile_claim_rule_conditions_model = {} # ProfileClaimRuleConditions
        profile_claim_rule_conditions_model['claim'] = 'testString'
        profile_claim_rule_conditions_model['operator'] = 'testString'
        profile_claim_rule_conditions_model['value'] = 'testString'

        profile_claim_rule_model = {} # ProfileClaimRule
        profile_claim_rule_model['id'] = 'testString'
        profile_claim_rule_model['entity_tag'] = 'testString'
        profile_claim_rule_model['created_at'] = "2019-01-01T12:00:00Z"
        profile_claim_rule_model['modified_at'] = "2019-01-01T12:00:00Z"
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

class TestModel_ProfileLink():
    """
    Test Class for ProfileLink
    """

    def test_profile_link_serialization(self):
        """
        Test serialization/deserialization for ProfileLink
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_link_link_model = {} # ProfileLinkLink
        profile_link_link_model['crn'] = 'testString'
        profile_link_link_model['namespace'] = 'testString'
        profile_link_link_model['name'] = 'testString'

        # Construct a json representation of a ProfileLink model
        profile_link_model_json = {}
        profile_link_model_json['id'] = 'testString'
        profile_link_model_json['entity_tag'] = 'testString'
        profile_link_model_json['created_at'] = "2019-01-01T12:00:00Z"
        profile_link_model_json['modified_at'] = "2019-01-01T12:00:00Z"
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

class TestModel_ProfileLinkLink():
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

class TestModel_ProfileLinkList():
    """
    Test Class for ProfileLinkList
    """

    def test_profile_link_list_serialization(self):
        """
        Test serialization/deserialization for ProfileLinkList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        profile_link_link_model = {} # ProfileLinkLink
        profile_link_link_model['crn'] = 'testString'
        profile_link_link_model['namespace'] = 'testString'
        profile_link_link_model['name'] = 'testString'

        profile_link_model = {} # ProfileLink
        profile_link_model['id'] = 'testString'
        profile_link_model['entity_tag'] = 'testString'
        profile_link_model['created_at'] = "2019-01-01T12:00:00Z"
        profile_link_model['modified_at'] = "2019-01-01T12:00:00Z"
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

class TestModel_ResponseContext():
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

class TestModel_ServiceId():
    """
    Test Class for ServiceId
    """

    def test_service_id_serialization(self):
        """
        Test serialization/deserialization for ServiceId
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {} # ResponseContext
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

        enity_history_record_model = {} # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        api_key_model = {} # ApiKey
        api_key_model['context'] = response_context_model
        api_key_model['id'] = 'testString'
        api_key_model['entity_tag'] = 'testString'
        api_key_model['crn'] = 'testString'
        api_key_model['locked'] = True
        api_key_model['created_at'] = "2019-01-01T12:00:00Z"
        api_key_model['created_by'] = 'testString'
        api_key_model['modified_at'] = "2019-01-01T12:00:00Z"
        api_key_model['name'] = 'testString'
        api_key_model['description'] = 'testString'
        api_key_model['iam_id'] = 'testString'
        api_key_model['account_id'] = 'testString'
        api_key_model['apikey'] = 'testString'
        api_key_model['history'] = [enity_history_record_model]

        # Construct a json representation of a ServiceId model
        service_id_model_json = {}
        service_id_model_json['context'] = response_context_model
        service_id_model_json['id'] = 'testString'
        service_id_model_json['iam_id'] = 'testString'
        service_id_model_json['entity_tag'] = 'testString'
        service_id_model_json['crn'] = 'testString'
        service_id_model_json['locked'] = True
        service_id_model_json['created_at'] = "2019-01-01T12:00:00Z"
        service_id_model_json['modified_at'] = "2019-01-01T12:00:00Z"
        service_id_model_json['account_id'] = 'testString'
        service_id_model_json['name'] = 'testString'
        service_id_model_json['description'] = 'testString'
        service_id_model_json['unique_instance_crns'] = ['testString']
        service_id_model_json['history'] = [enity_history_record_model]
        service_id_model_json['apikey'] = api_key_model

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

class TestModel_ServiceIdList():
    """
    Test Class for ServiceIdList
    """

    def test_service_id_list_serialization(self):
        """
        Test serialization/deserialization for ServiceIdList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {} # ResponseContext
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

        enity_history_record_model = {} # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        api_key_model = {} # ApiKey
        api_key_model['context'] = response_context_model
        api_key_model['id'] = 'testString'
        api_key_model['entity_tag'] = 'testString'
        api_key_model['crn'] = 'testString'
        api_key_model['locked'] = True
        api_key_model['created_at'] = "2019-01-01T12:00:00Z"
        api_key_model['created_by'] = 'testString'
        api_key_model['modified_at'] = "2019-01-01T12:00:00Z"
        api_key_model['name'] = 'testString'
        api_key_model['description'] = 'testString'
        api_key_model['iam_id'] = 'testString'
        api_key_model['account_id'] = 'testString'
        api_key_model['apikey'] = 'testString'
        api_key_model['history'] = [enity_history_record_model]

        service_id_model = {} # ServiceId
        service_id_model['context'] = response_context_model
        service_id_model['id'] = 'testString'
        service_id_model['iam_id'] = 'testString'
        service_id_model['entity_tag'] = 'testString'
        service_id_model['crn'] = 'testString'
        service_id_model['locked'] = True
        service_id_model['created_at'] = "2019-01-01T12:00:00Z"
        service_id_model['modified_at'] = "2019-01-01T12:00:00Z"
        service_id_model['account_id'] = 'testString'
        service_id_model['name'] = 'testString'
        service_id_model['description'] = 'testString'
        service_id_model['unique_instance_crns'] = ['testString']
        service_id_model['history'] = [enity_history_record_model]
        service_id_model['apikey'] = api_key_model

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

class TestModel_TrustedProfile():
    """
    Test Class for TrustedProfile
    """

    def test_trusted_profile_serialization(self):
        """
        Test serialization/deserialization for TrustedProfile
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {} # ResponseContext
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

        enity_history_record_model = {} # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        # Construct a json representation of a TrustedProfile model
        trusted_profile_model_json = {}
        trusted_profile_model_json['context'] = response_context_model
        trusted_profile_model_json['id'] = 'testString'
        trusted_profile_model_json['entity_tag'] = 'testString'
        trusted_profile_model_json['crn'] = 'testString'
        trusted_profile_model_json['name'] = 'testString'
        trusted_profile_model_json['description'] = 'testString'
        trusted_profile_model_json['created_at'] = "2019-01-01T12:00:00Z"
        trusted_profile_model_json['modified_at'] = "2019-01-01T12:00:00Z"
        trusted_profile_model_json['iam_id'] = 'testString'
        trusted_profile_model_json['account_id'] = 'testString'
        trusted_profile_model_json['ims_account_id'] = 26
        trusted_profile_model_json['ims_user_id'] = 26
        trusted_profile_model_json['history'] = [enity_history_record_model]

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

class TestModel_TrustedProfilesList():
    """
    Test Class for TrustedProfilesList
    """

    def test_trusted_profiles_list_serialization(self):
        """
        Test serialization/deserialization for TrustedProfilesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_context_model = {} # ResponseContext
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

        enity_history_record_model = {} # EnityHistoryRecord
        enity_history_record_model['timestamp'] = 'testString'
        enity_history_record_model['iam_id'] = 'testString'
        enity_history_record_model['iam_id_account'] = 'testString'
        enity_history_record_model['action'] = 'testString'
        enity_history_record_model['params'] = ['testString']
        enity_history_record_model['message'] = 'testString'

        trusted_profile_model = {} # TrustedProfile
        trusted_profile_model['context'] = response_context_model
        trusted_profile_model['id'] = 'testString'
        trusted_profile_model['entity_tag'] = 'testString'
        trusted_profile_model['crn'] = 'testString'
        trusted_profile_model['name'] = 'testString'
        trusted_profile_model['description'] = 'testString'
        trusted_profile_model['created_at'] = "2019-01-01T12:00:00Z"
        trusted_profile_model['modified_at'] = "2019-01-01T12:00:00Z"
        trusted_profile_model['iam_id'] = 'testString'
        trusted_profile_model['account_id'] = 'testString'
        trusted_profile_model['ims_account_id'] = 26
        trusted_profile_model['ims_user_id'] = 26
        trusted_profile_model['history'] = [enity_history_record_model]

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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
