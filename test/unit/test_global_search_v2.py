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
Unit Tests for GlobalSearchV2
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.global_search_v2 import *


_service = GlobalSearchV2(authenticator=NoAuthAuthenticator())

_base_url = 'https://api.global-search-tagging.cloud.ibm.com'
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
# Start of Service: Search
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

        service = GlobalSearchV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, GlobalSearchV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = GlobalSearchV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestSearch:
    """
    Test Class for search
    """

    @responses.activate
    def test_search_all_params(self):
        """
        search()
        """
        # Set up mock
        url = preprocess_url('/v3/resources/search')
        mock_response = '{"search_cursor": "search_cursor", "limit": 5, "items": [{"crn": "crn"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        query = 'testString'
        fields = ['testString']
        search_cursor = 'testString'
        transaction_id = 'testString'
        account_id = 'testString'
        limit = 1
        timeout = 0
        sort = ['testString']
        is_deleted = 'false'
        is_reclaimed = 'false'
        is_public = 'false'
        impersonate_user = 'testString'
        can_tag = 'false'

        # Invoke method
        response = _service.search(
            query=query,
            fields=fields,
            search_cursor=search_cursor,
            transaction_id=transaction_id,
            account_id=account_id,
            limit=limit,
            timeout=timeout,
            sort=sort,
            is_deleted=is_deleted,
            is_reclaimed=is_reclaimed,
            is_public=is_public,
            impersonate_user=impersonate_user,
            can_tag=can_tag,
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
        assert 'timeout={}'.format(timeout) in query_string
        assert 'sort={}'.format(','.join(sort)) in query_string
        assert 'is_deleted={}'.format(is_deleted) in query_string
        assert 'is_reclaimed={}'.format(is_reclaimed) in query_string
        assert 'is_public={}'.format(is_public) in query_string
        assert 'impersonate_user={}'.format(impersonate_user) in query_string
        assert 'can_tag={}'.format(can_tag) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == 'testString'
        assert req_body['fields'] == ['testString']
        assert req_body['search_cursor'] == 'testString'

    def test_search_all_params_with_retries(self):
        # Enable retries and run test_search_all_params.
        _service.enable_retries()
        self.test_search_all_params()

        # Disable retries and run test_search_all_params.
        _service.disable_retries()
        self.test_search_all_params()

    @responses.activate
    def test_search_required_params(self):
        """
        test_search_required_params()
        """
        # Set up mock
        url = preprocess_url('/v3/resources/search')
        mock_response = '{"search_cursor": "search_cursor", "limit": 5, "items": [{"crn": "crn"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        query = 'testString'
        fields = ['testString']
        search_cursor = 'testString'

        # Invoke method
        response = _service.search(
            query=query,
            fields=fields,
            search_cursor=search_cursor,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == 'testString'
        assert req_body['fields'] == ['testString']
        assert req_body['search_cursor'] == 'testString'

    def test_search_required_params_with_retries(self):
        # Enable retries and run test_search_required_params.
        _service.enable_retries()
        self.test_search_required_params()

        # Disable retries and run test_search_required_params.
        _service.disable_retries()
        self.test_search_required_params()


# endregion
##############################################################################
# End of Service: Search
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_ResultItem:
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
        result_item_model_json['foo'] = 'testString'

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

        # Test get_properties and set_properties methods.
        result_item_model.set_properties({})
        actual_dict = result_item_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        result_item_model.set_properties(expected_dict)
        actual_dict = result_item_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_ScanResult:
    """
    Test Class for ScanResult
    """

    def test_scan_result_serialization(self):
        """
        Test serialization/deserialization for ScanResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        result_item_model = {}  # ResultItem
        result_item_model['crn'] = 'testString'
        result_item_model['foo'] = 'testString'

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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
