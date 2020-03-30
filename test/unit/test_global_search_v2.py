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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from platform_services.global_search_v2 import *


service = GlobalSearchV2(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://api.global-search-tagging.cloud.ibm.com/'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ResourceFinder
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for search
#-----------------------------------------------------------------------------
class TestSearch():

    #--------------------------------------------------------
    # search()
    #--------------------------------------------------------
    @responses.activate
    def test_search_all_params(self):
        # Set up mock
        url = base_url + '/v3/resources/search'
        mock_response = '{"search_cursor": "search_cursor", "limit": 5, "items": [{"crn": "crn"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        query = 'testString'
        fields = ['testString']
        search_cursor = 'testString'
        transaction_id = 'testString'
        account_id = 'testString'
        limit = 38
        timeout = 38
        sort = ['testString']

        # Invoke method
        response = service.search(
            query=query,
            fields=fields,
            search_cursor=search_cursor,
            transaction_id=transaction_id,
            account_id=account_id,
            limit=limit,
            timeout=timeout,
            sort=sort
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'timeout={}'.format(timeout) in query_string
        assert 'sort={}'.format(','.join(sort)) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == query
        assert req_body['fields'] == fields
        assert req_body['search_cursor'] == search_cursor


    #--------------------------------------------------------
    # test_search_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_search_required_params(self):
        # Set up mock
        url = base_url + '/v3/resources/search'
        mock_response = '{"search_cursor": "search_cursor", "limit": 5, "items": [{"crn": "crn"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        query = 'testString'
        fields = ['testString']
        search_cursor = 'testString'

        # Invoke method
        response = service.search(
            query=query,
            fields=fields,
            search_cursor=search_cursor,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == query
        assert req_body['fields'] == fields
        assert req_body['search_cursor'] == search_cursor


# endregion
##############################################################################
# End of Service: ResourceFinder
##############################################################################

##############################################################################
# Start of Service: ResourceTypes
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_supported_types
#-----------------------------------------------------------------------------
class TestGetSupportedTypes():

    #--------------------------------------------------------
    # get_supported_types()
    #--------------------------------------------------------
    @responses.activate
    def test_get_supported_types_all_params(self):
        # Set up mock
        url = base_url + '/v2/resources/supported_types'
        mock_response = '{"supported_types": ["supported_types"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_supported_types()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_supported_types_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_supported_types_required_params(self):
        # Set up mock
        url = base_url + '/v2/resources/supported_types'
        mock_response = '{"supported_types": ["supported_types"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_supported_types()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ResourceTypes
##############################################################################

