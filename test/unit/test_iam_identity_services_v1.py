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
from platform_services.iam_identity_services_v1 import *


service = IamIdentityServicesV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://iam.test.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: IdentityOperations
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_api_keys
#-----------------------------------------------------------------------------
class TestListApiKeys():

    #--------------------------------------------------------
    # list_api_keys()
    #--------------------------------------------------------
    @responses.activate
    def test_list_api_keys_all_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys'
        mock_response = '{"context": {"requestId": "request_id", "requestType": "request_type", "userAgent": "user_agent", "clientIp": "client_ip", "url": "url", "instanceId": "instance_id", "threadId": "thread_id", "host": "host", "startTime": "start_time", "endTime": "end_time", "elapsedTime": "elapsed_time", "locale": "locale", "clusterName": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "apikeys": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        pagesize = 'testString'
        pagetoken = 'testString'

        # Invoke method
        response = service.list_api_keys(
            account_id=account_id,
            iam_id=iam_id,
            pagesize=pagesize,
            pagetoken=pagetoken
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'iam_id={}'.format(iam_id) in query_string
        assert 'pagesize={}'.format(pagesize) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string


    #--------------------------------------------------------
    # test_list_api_keys_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_api_keys_required_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys'
        mock_response = '{"context": {"requestId": "request_id", "requestType": "request_type", "userAgent": "user_agent", "clientIp": "client_ip", "url": "url", "instanceId": "instance_id", "threadId": "thread_id", "host": "host", "startTime": "start_time", "endTime": "end_time", "elapsedTime": "elapsed_time", "locale": "locale", "clusterName": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "apikeys": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}]}'
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


#-----------------------------------------------------------------------------
# Test Class for create_api_key
#-----------------------------------------------------------------------------
class TestCreateApiKey():

    #--------------------------------------------------------
    # create_api_key()
    #--------------------------------------------------------
    @responses.activate
    def test_create_api_key_all_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}'
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
        entity_lock = 'testString'

        # Invoke method
        response = service.create_api_key(
            name,
            iam_id,
            description=description,
            account_id=account_id,
            apikey=apikey,
            entity_lock=entity_lock
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['iam_id'] == iam_id
        assert req_body['description'] == description
        assert req_body['account_id'] == account_id
        assert req_body['apikey'] == apikey


    #--------------------------------------------------------
    # test_create_api_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_api_key_required_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}'
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

        # Invoke method
        response = service.create_api_key(
            name,
            iam_id,
            description=description,
            account_id=account_id,
            apikey=apikey,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['iam_id'] == iam_id
        assert req_body['description'] == description
        assert req_body['account_id'] == account_id
        assert req_body['apikey'] == apikey


#-----------------------------------------------------------------------------
# Test Class for get_api_key_details
#-----------------------------------------------------------------------------
class TestGetApiKeyDetails():

    #--------------------------------------------------------
    # get_api_key_details()
    #--------------------------------------------------------
    @responses.activate
    def test_get_api_key_details_all_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/details'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        iam_api_key = 'testString'

        # Invoke method
        response = service.get_api_key_details(
            iam_api_key=iam_api_key
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_api_key_details_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_api_key_details_required_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/details'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_api_key_details()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_api_key
#-----------------------------------------------------------------------------
class TestGetApiKey():

    #--------------------------------------------------------
    # get_api_key()
    #--------------------------------------------------------
    @responses.activate
    def test_get_api_key_all_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_api_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_api_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_api_key_required_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_api_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_api_key
#-----------------------------------------------------------------------------
class TestUpdateApiKey():

    #--------------------------------------------------------
    # update_api_key()
    #--------------------------------------------------------
    @responses.activate
    def test_update_api_key_all_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description


    #--------------------------------------------------------
    # test_update_api_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_api_key_required_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description


#-----------------------------------------------------------------------------
# Test Class for delete_api_key
#-----------------------------------------------------------------------------
class TestDeleteApiKey():

    #--------------------------------------------------------
    # delete_api_key()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_api_key_all_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_api_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_api_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_api_key_required_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_api_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for lock_api_key
#-----------------------------------------------------------------------------
class TestLockApiKey():

    #--------------------------------------------------------
    # lock_api_key()
    #--------------------------------------------------------
    @responses.activate
    def test_lock_api_key_all_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString/lock'
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.lock_api_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_lock_api_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_lock_api_key_required_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString/lock'
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.lock_api_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for unlock_api_key
#-----------------------------------------------------------------------------
class TestUnlockApiKey():

    #--------------------------------------------------------
    # unlock_api_key()
    #--------------------------------------------------------
    @responses.activate
    def test_unlock_api_key_all_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString/lock'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.unlock_api_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_unlock_api_key_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_unlock_api_key_required_params(self):
        # Set up mock
        url = base_url + '/v1/apikeys/testString/lock'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.unlock_api_key(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for list_service_ids
#-----------------------------------------------------------------------------
class TestListServiceIds():

    #--------------------------------------------------------
    # list_service_ids()
    #--------------------------------------------------------
    @responses.activate
    def test_list_service_ids_all_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids'
        mock_response = '{"context": {"requestId": "request_id", "requestType": "request_type", "userAgent": "user_agent", "clientIp": "client_ip", "url": "url", "instanceId": "instance_id", "threadId": "thread_id", "host": "host", "startTime": "start_time", "endTime": "end_time", "elapsedTime": "elapsed_time", "locale": "locale", "clusterName": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "serviceids": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        pagesize = 'testString'
        pagetoken = 'testString'
        sort = 'testString'
        order = 'testString'

        # Invoke method
        response = service.list_service_ids(
            account_id=account_id,
            name=name,
            pagesize=pagesize,
            pagetoken=pagetoken,
            sort=sort,
            order=order
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'pagesize={}'.format(pagesize) in query_string
        assert 'pagetoken={}'.format(pagetoken) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'order={}'.format(order) in query_string


    #--------------------------------------------------------
    # test_list_service_ids_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_service_ids_required_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids'
        mock_response = '{"context": {"requestId": "request_id", "requestType": "request_type", "userAgent": "user_agent", "clientIp": "client_ip", "url": "url", "instanceId": "instance_id", "threadId": "thread_id", "host": "host", "startTime": "start_time", "endTime": "end_time", "elapsedTime": "elapsed_time", "locale": "locale", "clusterName": "cluster_name"}, "offset": 6, "limit": 5, "first": "first", "previous": "previous", "next": "next", "serviceids": [{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}]}'
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


#-----------------------------------------------------------------------------
# Test Class for create_service_id
#-----------------------------------------------------------------------------
class TestCreateServiceId():

    #--------------------------------------------------------
    # create_service_id()
    #--------------------------------------------------------
    @responses.activate
    def test_create_service_id_all_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CreateApiKeyRequest model
        create_api_key_request_model = {}
        create_api_key_request_model['name'] = 'testString' 
        create_api_key_request_model['description'] = 'testString' 
        create_api_key_request_model['iam_id'] = 'testString' 
        create_api_key_request_model['account_id'] = 'testString' 
        create_api_key_request_model['apikey'] = 'testString' 

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        unique_instance_crns = ['testString']
        apikey = create_api_key_request_model
        entity_lock = 'testString'

        # Invoke method
        response = service.create_service_id(
            account_id,
            name,
            description=description,
            unique_instance_crns=unique_instance_crns,
            apikey=apikey,
            entity_lock=entity_lock
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == account_id
        assert req_body['name'] == name
        assert req_body['description'] == description
        assert req_body['unique_instance_crns'] == unique_instance_crns
        assert req_body['apikey'] == apikey


    #--------------------------------------------------------
    # test_create_service_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_service_id_required_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CreateApiKeyRequest model
        create_api_key_request_model = {}
        create_api_key_request_model['name'] = 'testString' 
        create_api_key_request_model['description'] = 'testString' 
        create_api_key_request_model['iam_id'] = 'testString' 
        create_api_key_request_model['account_id'] = 'testString' 
        create_api_key_request_model['apikey'] = 'testString' 

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        unique_instance_crns = ['testString']
        apikey = create_api_key_request_model

        # Invoke method
        response = service.create_service_id(
            account_id,
            name,
            description=description,
            unique_instance_crns=unique_instance_crns,
            apikey=apikey,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == account_id
        assert req_body['name'] == name
        assert req_body['description'] == description
        assert req_body['unique_instance_crns'] == unique_instance_crns
        assert req_body['apikey'] == apikey


#-----------------------------------------------------------------------------
# Test Class for get_service_id
#-----------------------------------------------------------------------------
class TestGetServiceId():

    #--------------------------------------------------------
    # get_service_id()
    #--------------------------------------------------------
    @responses.activate
    def test_get_service_id_all_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_service_id(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_service_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_service_id_required_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_service_id(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_service_id
#-----------------------------------------------------------------------------
class TestUpdateServiceId():

    #--------------------------------------------------------
    # update_service_id()
    #--------------------------------------------------------
    @responses.activate
    def test_update_service_id_all_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description
        assert req_body['unique_instance_crns'] == unique_instance_crns


    #--------------------------------------------------------
    # test_update_service_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_service_id_required_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description
        assert req_body['unique_instance_crns'] == unique_instance_crns


#-----------------------------------------------------------------------------
# Test Class for delete_service_id
#-----------------------------------------------------------------------------
class TestDeleteServiceId():

    #--------------------------------------------------------
    # delete_service_id()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_id_all_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_service_id(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_service_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_service_id_required_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_service_id(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for lock_service_id
#-----------------------------------------------------------------------------
class TestLockServiceId():

    #--------------------------------------------------------
    # lock_service_id()
    #--------------------------------------------------------
    @responses.activate
    def test_lock_service_id_all_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString/lock'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.lock_service_id(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_lock_service_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_lock_service_id_required_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString/lock'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.lock_service_id(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for unlock_service_id
#-----------------------------------------------------------------------------
class TestUnlockServiceId():

    #--------------------------------------------------------
    # unlock_service_id()
    #--------------------------------------------------------
    @responses.activate
    def test_unlock_service_id_all_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString/lock'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.unlock_service_id(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_unlock_service_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_unlock_service_id_required_params(self):
        # Set up mock
        url = base_url + '/v1/serviceids/testString/lock'
        mock_response = '{"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "iam_id": "iam_id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "account_id": "account_id", "name": "name", "description": "description", "unique_instance_crns": ["unique_instance_crns"], "apikey": {"context": {"transaction_id": "transaction_id", "operation": "operation", "user_agent": "user_agent", "client_ip": "client_ip", "url": "url", "instance_id": "instance_id", "thread_id": "thread_id", "host": "host", "start_time": "start_time", "end_time": "end_time", "elapsed_time": "elapsed_time", "cluster_name": "cluster_name"}, "id": "id", "entity_tag": "entity_tag", "crn": "crn", "locked": true, "created_at": "2019-01-01T12:00:00", "modified_at": "2019-01-01T12:00:00", "name": "name", "description": "description", "iam_id": "iam_id", "account_id": "account_id", "apikey": "apikey"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.unlock_service_id(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: IdentityOperations
##############################################################################

