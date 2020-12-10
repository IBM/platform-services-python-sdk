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
Unit Tests for GlobalSearchV2
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.global_search_v2 import *


service = GlobalSearchV2(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://api.global-search-tagging.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Search
##############################################################################
# region

class TestSearch():
    """
    Test Class for search
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
    def test_search_all_params(self):
        """
        search()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v3/resources/search')
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
        limit = 1
        timeout = 0
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
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'timeout={}'.format(timeout) in query_string
        assert 'sort={}'.format(','.join(sort)) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == 'testString'
        assert req_body['fields'] == ['testString']
        assert req_body['search_cursor'] == 'testString'


    @responses.activate
    def test_search_required_params(self):
        """
        test_search_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v3/resources/search')
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == 'testString'
        assert req_body['fields'] == ['testString']
        assert req_body['search_cursor'] == 'testString'


# endregion
##############################################################################
# End of Service: Search
##############################################################################

##############################################################################
# Start of Service: ResourceTypes
##############################################################################
# region

class TestGetSupportedTypes():
    """
    Test Class for get_supported_types
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
    def test_get_supported_types_all_params(self):
        """
        get_supported_types()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/resources/supported_types')
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


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestResultItem():
    """
    Test Class for ResultItem
    """

    def test_result_item_serialization(self):
        """
        Test serialization/deserialization for ResultItem
        """

        # Construct a json representation of a ResultItem model
        result_item_model_json = {}
        result_item_model_json['crn'] = 'testString'
        result_item_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of ResultItem by calling from_dict on the json representation
        result_item_model = ResultItem.from_dict(result_item_model_json)
        assert result_item_model != False

        # Construct a model instance of ResultItem by calling from_dict on the json representation
        result_item_model_dict = ResultItem.from_dict(result_item_model_json).__dict__
        result_item_model2 = ResultItem(**result_item_model_dict)

        # Verify the model instances are equivalent
        assert result_item_model == result_item_model2

        # Convert model instance back to dict and verify no loss of data
        result_item_model_json2 = result_item_model.to_dict()
        assert result_item_model_json2 == result_item_model_json

class TestScanResult():
    """
    Test Class for ScanResult
    """

    def test_scan_result_serialization(self):
        """
        Test serialization/deserialization for ScanResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        result_item_model = {} # ResultItem
        result_item_model['crn'] = 'testString'
        result_item_model['foo'] = { 'foo': 'bar' }

        # Construct a json representation of a ScanResult model
        scan_result_model_json = {}
        scan_result_model_json['search_cursor'] = 'testString'
        scan_result_model_json['limit'] = 38
        scan_result_model_json['items'] = [result_item_model]

        # Construct a model instance of ScanResult by calling from_dict on the json representation
        scan_result_model = ScanResult.from_dict(scan_result_model_json)
        assert scan_result_model != False

        # Construct a model instance of ScanResult by calling from_dict on the json representation
        scan_result_model_dict = ScanResult.from_dict(scan_result_model_json).__dict__
        scan_result_model2 = ScanResult(**scan_result_model_dict)

        # Verify the model instances are equivalent
        assert scan_result_model == scan_result_model2

        # Convert model instance back to dict and verify no loss of data
        scan_result_model_json2 = scan_result_model.to_dict()
        assert scan_result_model_json2 == scan_result_model_json

class TestSupportedTypesList():
    """
    Test Class for SupportedTypesList
    """

    def test_supported_types_list_serialization(self):
        """
        Test serialization/deserialization for SupportedTypesList
        """

        # Construct a json representation of a SupportedTypesList model
        supported_types_list_model_json = {}
        supported_types_list_model_json['supported_types'] = ['testString']

        # Construct a model instance of SupportedTypesList by calling from_dict on the json representation
        supported_types_list_model = SupportedTypesList.from_dict(supported_types_list_model_json)
        assert supported_types_list_model != False

        # Construct a model instance of SupportedTypesList by calling from_dict on the json representation
        supported_types_list_model_dict = SupportedTypesList.from_dict(supported_types_list_model_json).__dict__
        supported_types_list_model2 = SupportedTypesList(**supported_types_list_model_dict)

        # Verify the model instances are equivalent
        assert supported_types_list_model == supported_types_list_model2

        # Convert model instance back to dict and verify no loss of data
        supported_types_list_model_json2 = supported_types_list_model.to_dict()
        assert supported_types_list_model_json2 == supported_types_list_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
