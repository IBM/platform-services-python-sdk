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

"""
Unit Tests for IamIdentityV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.iam_identity_v1 import *


service = IamIdentityV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://iam.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: IdentityOperations
##############################################################################
# region

class TestListApiKeys():
    """
    Test Class for list_api_keys
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "apikeys": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}]}'
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
        include_history = True

        # Invoke method
        response = service.list_api_keys(
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
        url = self.preprocess_url(base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "apikeys": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_api_keys()


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
        url = self.preprocess_url(base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
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
        entity_lock = 'testString'

        # Invoke method
        response = service.create_api_key(
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
        url = self.preprocess_url(base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
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
        response = service.create_api_key(
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
        url = self.preprocess_url(base_url + '/v1/apikeys')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
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
                service.create_api_key(**req_copy)



class TestGetApiKeysDetails():
    """
    Test Class for get_api_keys_details
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/apikeys/details')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        iam_api_key = 'testString'
        include_history = True

        # Invoke method
        response = service.get_api_keys_details(
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
        url = self.preprocess_url(base_url + '/v1/apikeys/details')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_api_keys_details()


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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        include_history = True

        # Invoke method
        response = service.get_api_key(
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_api_key(
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
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
                service.get_api_key(**req_copy)



class TestUpdateApiKey():
    """
    Test Class for update_api_key
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
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
        response = service.update_api_key(
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}'
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
                service.update_api_key(**req_copy)



class TestDeleteApiKey():
    """
    Test Class for delete_api_key
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_api_key(
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString')
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
                service.delete_api_key(**req_copy)



class TestLockApiKey():
    """
    Test Class for lock_api_key
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString/lock')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.lock_api_key(
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString/lock')
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
                service.lock_api_key(**req_copy)



class TestUnlockApiKey():
    """
    Test Class for unlock_api_key
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString/lock')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.unlock_api_key(
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
        url = self.preprocess_url(base_url + '/v1/apikeys/testString/lock')
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
                service.unlock_api_key(**req_copy)



class TestListServiceIds():
    """
    Test Class for list_service_ids
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "serviceids": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}]}'
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
        include_history = True

        # Invoke method
        response = service.list_service_ids(
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
        url = self.preprocess_url(base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "serviceids": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_service_ids()


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
        url = self.preprocess_url(base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
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
        entity_lock = 'testString'

        # Invoke method
        response = service.create_service_id(
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
        url = self.preprocess_url(base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
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
        response = service.create_service_id(
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
        url = self.preprocess_url(base_url + '/v1/serviceids/')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
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
                service.create_service_id(**req_copy)



class TestGetServiceId():
    """
    Test Class for get_service_id
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        include_history = True

        # Invoke method
        response = service.get_service_id(
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_service_id(
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
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
                service.get_service_id(**req_copy)



class TestUpdateServiceId():
    """
    Test Class for update_service_id
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
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
        response = service.update_service_id(
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString')
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey", "history": [{"timestamp": "timestamp", "iam_id": "iam_id", "iam_id_account": "iam_id_account", "action": "action", "params": ["params"], "message": "message"}]}}'
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
                service.update_service_id(**req_copy)



class TestDeleteServiceId():
    """
    Test Class for delete_service_id
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_service_id(
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString')
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
                service.delete_service_id(**req_copy)



class TestLockServiceId():
    """
    Test Class for lock_service_id
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString/lock')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.lock_service_id(
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString/lock')
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
                service.lock_service_id(**req_copy)



class TestUnlockServiceId():
    """
    Test Class for unlock_service_id
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString/lock')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.unlock_service_id(
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
        url = self.preprocess_url(base_url + '/v1/serviceids/testString/lock')
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
                service.unlock_service_id(**req_copy)



# endregion
##############################################################################
# End of Service: IdentityOperations
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestApiKey():
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
        api_key_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        api_key_model_json['created_by'] = 'testString'
        api_key_model_json['modified_at'] = '2020-01-28T18:40:40.123456Z'
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

class TestApiKeyInsideCreateServiceIdRequest():
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

class TestApiKeyList():
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
        api_key_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        api_key_model['created_by'] = 'testString'
        api_key_model['modified_at'] = '2020-01-28T18:40:40.123456Z'
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

class TestEnityHistoryRecord():
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

class TestResponseContext():
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

class TestServiceId():
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
        api_key_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        api_key_model['created_by'] = 'testString'
        api_key_model['modified_at'] = '2020-01-28T18:40:40.123456Z'
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
        service_id_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        service_id_model_json['modified_at'] = '2020-01-28T18:40:40.123456Z'
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

class TestServiceIdList():
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
        api_key_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        api_key_model['created_by'] = 'testString'
        api_key_model['modified_at'] = '2020-01-28T18:40:40.123456Z'
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
        service_id_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        service_id_model['modified_at'] = '2020-01-28T18:40:40.123456Z'
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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
