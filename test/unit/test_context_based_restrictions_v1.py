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
Unit Tests for ContextBasedRestrictionsV1
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
from ibm_platform_services.context_based_restrictions_v1 import *

_service = ContextBasedRestrictionsV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://cbr.cloud.ibm.com'
_service.set_service_url(_base_url)


##############################################################################
# Start of Service: Zones
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

        service = ContextBasedRestrictionsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ContextBasedRestrictionsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ContextBasedRestrictionsV1.new_instance(
            )


class TestCreateZone():
    """
    Test Class for create_zone
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_zone_all_params(self):
        """
        create_zone()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones')
        mock_response = '{"id": "id", "crn": "crn", "name": "name", "account_id": "account_id", "description": "description", "addresses": [{"type": "ipAddress", "value": "value"}], "excluded": [{"type": "ipAddress", "value": "value"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a AddressIPAddress model
        address_model = {}
        address_model['type'] = 'ipAddress'
        address_model['value'] = '169.23.56.234'

        # Set up parameter values
        name = 'an example of zone'
        account_id = '12ab34cd56ef78ab90cd12ef34ab56cd'
        addresses = [address_model]
        description = 'this is an example of zone'
        excluded = [address_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_zone(
            name=name,
            account_id=account_id,
            addresses=addresses,
            description=description,
            excluded=excluded,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'an example of zone'
        assert req_body['account_id'] == '12ab34cd56ef78ab90cd12ef34ab56cd'
        assert req_body['addresses'] == [address_model]
        assert req_body['description'] == 'this is an example of zone'
        assert req_body['excluded'] == [address_model]

    def test_create_zone_all_params_with_retries(self):
        # Enable retries and run test_create_zone_all_params.
        _service.enable_retries()
        self.test_create_zone_all_params()

        # Disable retries and run test_create_zone_all_params.
        _service.disable_retries()
        self.test_create_zone_all_params()

    @responses.activate
    def test_create_zone_required_params(self):
        """
        test_create_zone_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones')
        mock_response = '{"id": "id", "crn": "crn", "name": "name", "account_id": "account_id", "description": "description", "addresses": [{"type": "ipAddress", "value": "value"}], "excluded": [{"type": "ipAddress", "value": "value"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Invoke method
        response = _service.create_zone()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_zone_required_params_with_retries(self):
        # Enable retries and run test_create_zone_required_params.
        _service.enable_retries()
        self.test_create_zone_required_params()

        # Disable retries and run test_create_zone_required_params.
        _service.disable_retries()
        self.test_create_zone_required_params()


class TestListZones():
    """
    Test Class for list_zones
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_zones_all_params(self):
        """
        list_zones()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones')
        mock_response = '{"count": 5, "zones": [{"id": "id", "crn": "crn", "name": "name", "description": "description", "addresses_preview": [{"type": "ipAddress", "value": "value"}], "address_count": 13, "excluded_count": 14, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'
        name = 'testString'
        sort = 'testString'

        # Invoke method
        response = _service.list_zones(
            account_id,
            transaction_id=transaction_id,
            name=name,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'sort={}'.format(sort) in query_string

    def test_list_zones_all_params_with_retries(self):
        # Enable retries and run test_list_zones_all_params.
        _service.enable_retries()
        self.test_list_zones_all_params()

        # Disable retries and run test_list_zones_all_params.
        _service.disable_retries()
        self.test_list_zones_all_params()

    @responses.activate
    def test_list_zones_required_params(self):
        """
        test_list_zones_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones')
        mock_response = '{"count": 5, "zones": [{"id": "id", "crn": "crn", "name": "name", "description": "description", "addresses_preview": [{"type": "ipAddress", "value": "value"}], "address_count": 13, "excluded_count": 14, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_zones(
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_list_zones_required_params_with_retries(self):
        # Enable retries and run test_list_zones_required_params.
        _service.enable_retries()
        self.test_list_zones_required_params()

        # Disable retries and run test_list_zones_required_params.
        _service.disable_retries()
        self.test_list_zones_required_params()

    @responses.activate
    def test_list_zones_value_error(self):
        """
        test_list_zones_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones')
        mock_response = '{"count": 5, "zones": [{"id": "id", "crn": "crn", "name": "name", "description": "description", "addresses_preview": [{"type": "ipAddress", "value": "value"}], "address_count": 13, "excluded_count": 14, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_zones(**req_copy)

    def test_list_zones_value_error_with_retries(self):
        # Enable retries and run test_list_zones_value_error.
        _service.enable_retries()
        self.test_list_zones_value_error()

        # Disable retries and run test_list_zones_value_error.
        _service.disable_retries()
        self.test_list_zones_value_error()


class TestGetZone():
    """
    Test Class for get_zone
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_zone_all_params(self):
        """
        get_zone()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/testString')
        mock_response = '{"id": "id", "crn": "crn", "name": "name", "account_id": "account_id", "description": "description", "addresses": [{"type": "ipAddress", "value": "value"}], "excluded": [{"type": "ipAddress", "value": "value"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_zone(
            zone_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_all_params_with_retries(self):
        # Enable retries and run test_get_zone_all_params.
        _service.enable_retries()
        self.test_get_zone_all_params()

        # Disable retries and run test_get_zone_all_params.
        _service.disable_retries()
        self.test_get_zone_all_params()

    @responses.activate
    def test_get_zone_required_params(self):
        """
        test_get_zone_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/testString')
        mock_response = '{"id": "id", "crn": "crn", "name": "name", "account_id": "account_id", "description": "description", "addresses": [{"type": "ipAddress", "value": "value"}], "excluded": [{"type": "ipAddress", "value": "value"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_id = 'testString'

        # Invoke method
        response = _service.get_zone(
            zone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_required_params_with_retries(self):
        # Enable retries and run test_get_zone_required_params.
        _service.enable_retries()
        self.test_get_zone_required_params()

        # Disable retries and run test_get_zone_required_params.
        _service.disable_retries()
        self.test_get_zone_required_params()

    @responses.activate
    def test_get_zone_value_error(self):
        """
        test_get_zone_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/testString')
        mock_response = '{"id": "id", "crn": "crn", "name": "name", "account_id": "account_id", "description": "description", "addresses": [{"type": "ipAddress", "value": "value"}], "excluded": [{"type": "ipAddress", "value": "value"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone(**req_copy)

    def test_get_zone_value_error_with_retries(self):
        # Enable retries and run test_get_zone_value_error.
        _service.enable_retries()
        self.test_get_zone_value_error()

        # Disable retries and run test_get_zone_value_error.
        _service.disable_retries()
        self.test_get_zone_value_error()


class TestReplaceZone():
    """
    Test Class for replace_zone
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_zone_all_params(self):
        """
        replace_zone()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/testString')
        mock_response = '{"id": "id", "crn": "crn", "name": "name", "account_id": "account_id", "description": "description", "addresses": [{"type": "ipAddress", "value": "value"}], "excluded": [{"type": "ipAddress", "value": "value"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AddressIPAddress model
        address_model = {}
        address_model['type'] = 'ipAddress'
        address_model['value'] = '169.23.56.234'

        # Set up parameter values
        zone_id = 'testString'
        if_match = 'testString'
        name = 'an example of zone'
        account_id = '12ab34cd56ef78ab90cd12ef34ab56cd'
        addresses = [address_model]
        description = 'this is an example of zone'
        excluded = [address_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.replace_zone(
            zone_id,
            if_match,
            name=name,
            account_id=account_id,
            addresses=addresses,
            description=description,
            excluded=excluded,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'an example of zone'
        assert req_body['account_id'] == '12ab34cd56ef78ab90cd12ef34ab56cd'
        assert req_body['addresses'] == [address_model]
        assert req_body['description'] == 'this is an example of zone'
        assert req_body['excluded'] == [address_model]

    def test_replace_zone_all_params_with_retries(self):
        # Enable retries and run test_replace_zone_all_params.
        _service.enable_retries()
        self.test_replace_zone_all_params()

        # Disable retries and run test_replace_zone_all_params.
        _service.disable_retries()
        self.test_replace_zone_all_params()

    @responses.activate
    def test_replace_zone_required_params(self):
        """
        test_replace_zone_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/testString')
        mock_response = '{"id": "id", "crn": "crn", "name": "name", "account_id": "account_id", "description": "description", "addresses": [{"type": "ipAddress", "value": "value"}], "excluded": [{"type": "ipAddress", "value": "value"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_id = 'testString'
        if_match = 'testString'

        # Invoke method
        response = _service.replace_zone(
            zone_id,
            if_match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_replace_zone_required_params_with_retries(self):
        # Enable retries and run test_replace_zone_required_params.
        _service.enable_retries()
        self.test_replace_zone_required_params()

        # Disable retries and run test_replace_zone_required_params.
        _service.disable_retries()
        self.test_replace_zone_required_params()

    @responses.activate
    def test_replace_zone_value_error(self):
        """
        test_replace_zone_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/testString')
        mock_response = '{"id": "id", "crn": "crn", "name": "name", "account_id": "account_id", "description": "description", "addresses": [{"type": "ipAddress", "value": "value"}], "excluded": [{"type": "ipAddress", "value": "value"}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        zone_id = 'testString'
        if_match = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_zone(**req_copy)

    def test_replace_zone_value_error_with_retries(self):
        # Enable retries and run test_replace_zone_value_error.
        _service.enable_retries()
        self.test_replace_zone_value_error()

        # Disable retries and run test_replace_zone_value_error.
        _service.disable_retries()
        self.test_replace_zone_value_error()


class TestDeleteZone():
    """
    Test Class for delete_zone
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_zone_all_params(self):
        """
        delete_zone()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        zone_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_zone(
            zone_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_zone_all_params_with_retries(self):
        # Enable retries and run test_delete_zone_all_params.
        _service.enable_retries()
        self.test_delete_zone_all_params()

        # Disable retries and run test_delete_zone_all_params.
        _service.disable_retries()
        self.test_delete_zone_all_params()

    @responses.activate
    def test_delete_zone_required_params(self):
        """
        test_delete_zone_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        zone_id = 'testString'

        # Invoke method
        response = _service.delete_zone(
            zone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_zone_required_params_with_retries(self):
        # Enable retries and run test_delete_zone_required_params.
        _service.enable_retries()
        self.test_delete_zone_required_params()

        # Disable retries and run test_delete_zone_required_params.
        _service.disable_retries()
        self.test_delete_zone_required_params()

    @responses.activate
    def test_delete_zone_value_error(self):
        """
        test_delete_zone_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        zone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_zone(**req_copy)

    def test_delete_zone_value_error_with_retries(self):
        # Enable retries and run test_delete_zone_value_error.
        _service.enable_retries()
        self.test_delete_zone_value_error()

        # Disable retries and run test_delete_zone_value_error.
        _service.disable_retries()
        self.test_delete_zone_value_error()


class TestListAvailableServicerefTargets():
    """
    Test Class for list_available_serviceref_targets
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_available_serviceref_targets_all_params(self):
        """
        list_available_serviceref_targets()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/serviceref_targets')
        mock_response = '{"count": 5, "targets": [{"service_name": "service_name", "service_type": "service_type"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'all'

        # Invoke method
        response = _service.list_available_serviceref_targets(
            type=type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string

    def test_list_available_serviceref_targets_all_params_with_retries(self):
        # Enable retries and run test_list_available_serviceref_targets_all_params.
        _service.enable_retries()
        self.test_list_available_serviceref_targets_all_params()

        # Disable retries and run test_list_available_serviceref_targets_all_params.
        _service.disable_retries()
        self.test_list_available_serviceref_targets_all_params()

    @responses.activate
    def test_list_available_serviceref_targets_required_params(self):
        """
        test_list_available_serviceref_targets_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/zones/serviceref_targets')
        mock_response = '{"count": 5, "targets": [{"service_name": "service_name", "service_type": "service_type"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_available_serviceref_targets()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_available_serviceref_targets_required_params_with_retries(self):
        # Enable retries and run test_list_available_serviceref_targets_required_params.
        _service.enable_retries()
        self.test_list_available_serviceref_targets_required_params()

        # Disable retries and run test_list_available_serviceref_targets_required_params.
        _service.disable_retries()
        self.test_list_available_serviceref_targets_required_params()


# endregion
##############################################################################
# End of Service: Zones
##############################################################################

##############################################################################
# Start of Service: Rules
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

        service = ContextBasedRestrictionsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ContextBasedRestrictionsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ContextBasedRestrictionsV1.new_instance(
            )


class TestCreateRule():
    """
    Test Class for create_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_rule_all_params(self):
        """
        create_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules')
        mock_response = '{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {}
        rule_context_attribute_model['name'] = 'networkZoneId'
        rule_context_attribute_model['value'] = '65810ac762004f22ac19f8f8edf70a34'

        # Construct a dict representation of a RuleContext model
        rule_context_model = {}
        rule_context_model['attributes'] = [rule_context_attribute_model]

        # Construct a dict representation of a ResourceAttribute model
        resource_attribute_model = {}
        resource_attribute_model['name'] = 'accountId'
        resource_attribute_model['value'] = '12ab34cd56ef78ab90cd12ef34ab56cd'
        resource_attribute_model['operator'] = 'testString'

        # Construct a dict representation of a ResourceTagAttribute model
        resource_tag_attribute_model = {}
        resource_tag_attribute_model['name'] = 'testString'
        resource_tag_attribute_model['value'] = 'testString'
        resource_tag_attribute_model['operator'] = 'testString'

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['attributes'] = [resource_attribute_model]
        resource_model['tags'] = [resource_tag_attribute_model]

        # Set up parameter values
        contexts = [rule_context_model]
        resources = [resource_model]
        description = 'this is an example of rule'
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_rule(
            contexts=contexts,
            resources=resources,
            description=description,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['contexts'] == [rule_context_model]
        assert req_body['resources'] == [resource_model]
        assert req_body['description'] == 'this is an example of rule'

    def test_create_rule_all_params_with_retries(self):
        # Enable retries and run test_create_rule_all_params.
        _service.enable_retries()
        self.test_create_rule_all_params()

        # Disable retries and run test_create_rule_all_params.
        _service.disable_retries()
        self.test_create_rule_all_params()

    @responses.activate
    def test_create_rule_required_params(self):
        """
        test_create_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules')
        mock_response = '{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Invoke method
        response = _service.create_rule()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_rule_required_params_with_retries(self):
        # Enable retries and run test_create_rule_required_params.
        _service.enable_retries()
        self.test_create_rule_required_params()

        # Disable retries and run test_create_rule_required_params.
        _service.disable_retries()
        self.test_create_rule_required_params()


class TestListRules():
    """
    Test Class for list_rules
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_rules_all_params(self):
        """
        list_rules()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules')
        mock_response = '{"count": 5, "rules": [{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'
        region = 'testString'
        resource = 'testString'
        resource_type = 'testString'
        service_instance = 'testString'
        service_name = 'testString'
        service_type = 'testString'
        zone_id = 'testString'
        sort = 'testString'

        # Invoke method
        response = _service.list_rules(
            account_id,
            transaction_id=transaction_id,
            region=region,
            resource=resource,
            resource_type=resource_type,
            service_instance=service_instance,
            service_name=service_name,
            service_type=service_type,
            zone_id=zone_id,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'resource={}'.format(resource) in query_string
        assert 'resource_type={}'.format(resource_type) in query_string
        assert 'service_instance={}'.format(service_instance) in query_string
        assert 'service_name={}'.format(service_name) in query_string
        assert 'service_type={}'.format(service_type) in query_string
        assert 'zone_id={}'.format(zone_id) in query_string
        assert 'sort={}'.format(sort) in query_string

    def test_list_rules_all_params_with_retries(self):
        # Enable retries and run test_list_rules_all_params.
        _service.enable_retries()
        self.test_list_rules_all_params()

        # Disable retries and run test_list_rules_all_params.
        _service.disable_retries()
        self.test_list_rules_all_params()

    @responses.activate
    def test_list_rules_required_params(self):
        """
        test_list_rules_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules')
        mock_response = '{"count": 5, "rules": [{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_rules(
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_list_rules_required_params_with_retries(self):
        # Enable retries and run test_list_rules_required_params.
        _service.enable_retries()
        self.test_list_rules_required_params()

        # Disable retries and run test_list_rules_required_params.
        _service.disable_retries()
        self.test_list_rules_required_params()

    @responses.activate
    def test_list_rules_value_error(self):
        """
        test_list_rules_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules')
        mock_response = '{"count": 5, "rules": [{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}]}'
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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_rules(**req_copy)

    def test_list_rules_value_error_with_retries(self):
        # Enable retries and run test_list_rules_value_error.
        _service.enable_retries()
        self.test_list_rules_value_error()

        # Disable retries and run test_list_rules_value_error.
        _service.disable_retries()
        self.test_list_rules_value_error()


class TestGetRule():
    """
    Test Class for get_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_rule_all_params(self):
        """
        get_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules/testString')
        mock_response = '{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_rule(
            rule_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_rule_all_params_with_retries(self):
        # Enable retries and run test_get_rule_all_params.
        _service.enable_retries()
        self.test_get_rule_all_params()

        # Disable retries and run test_get_rule_all_params.
        _service.disable_retries()
        self.test_get_rule_all_params()

    @responses.activate
    def test_get_rule_required_params(self):
        """
        test_get_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules/testString')
        mock_response = '{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = _service.get_rule(
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_rule_required_params_with_retries(self):
        # Enable retries and run test_get_rule_required_params.
        _service.enable_retries()
        self.test_get_rule_required_params()

        # Disable retries and run test_get_rule_required_params.
        _service.disable_retries()
        self.test_get_rule_required_params()

    @responses.activate
    def test_get_rule_value_error(self):
        """
        test_get_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules/testString')
        mock_response = '{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_rule(**req_copy)

    def test_get_rule_value_error_with_retries(self):
        # Enable retries and run test_get_rule_value_error.
        _service.enable_retries()
        self.test_get_rule_value_error()

        # Disable retries and run test_get_rule_value_error.
        _service.disable_retries()
        self.test_get_rule_value_error()


class TestReplaceRule():
    """
    Test Class for replace_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_rule_all_params(self):
        """
        replace_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules/testString')
        mock_response = '{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {}
        rule_context_attribute_model['name'] = 'networkZoneId'
        rule_context_attribute_model['value'] = '76921bd873115033bd2a0909fe081b45'

        # Construct a dict representation of a RuleContext model
        rule_context_model = {}
        rule_context_model['attributes'] = [rule_context_attribute_model]

        # Construct a dict representation of a ResourceAttribute model
        resource_attribute_model = {}
        resource_attribute_model['name'] = 'accountId'
        resource_attribute_model['value'] = '12ab34cd56ef78ab90cd12ef34ab56cd'
        resource_attribute_model['operator'] = 'testString'

        # Construct a dict representation of a ResourceTagAttribute model
        resource_tag_attribute_model = {}
        resource_tag_attribute_model['name'] = 'testString'
        resource_tag_attribute_model['value'] = 'testString'
        resource_tag_attribute_model['operator'] = 'testString'

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['attributes'] = [resource_attribute_model]
        resource_model['tags'] = [resource_tag_attribute_model]

        # Set up parameter values
        rule_id = 'testString'
        if_match = 'testString'
        contexts = [rule_context_model]
        resources = [resource_model]
        description = 'this is an example of rule'
        transaction_id = 'testString'

        # Invoke method
        response = _service.replace_rule(
            rule_id,
            if_match,
            contexts=contexts,
            resources=resources,
            description=description,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['contexts'] == [rule_context_model]
        assert req_body['resources'] == [resource_model]
        assert req_body['description'] == 'this is an example of rule'

    def test_replace_rule_all_params_with_retries(self):
        # Enable retries and run test_replace_rule_all_params.
        _service.enable_retries()
        self.test_replace_rule_all_params()

        # Disable retries and run test_replace_rule_all_params.
        _service.disable_retries()
        self.test_replace_rule_all_params()

    @responses.activate
    def test_replace_rule_required_params(self):
        """
        test_replace_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules/testString')
        mock_response = '{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'
        if_match = 'testString'

        # Invoke method
        response = _service.replace_rule(
            rule_id,
            if_match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_replace_rule_required_params_with_retries(self):
        # Enable retries and run test_replace_rule_required_params.
        _service.enable_retries()
        self.test_replace_rule_required_params()

        # Disable retries and run test_replace_rule_required_params.
        _service.disable_retries()
        self.test_replace_rule_required_params()

    @responses.activate
    def test_replace_rule_value_error(self):
        """
        test_replace_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules/testString')
        mock_response = '{"id": "id", "crn": "crn", "description": "description", "contexts": [{"attributes": [{"name": "name", "value": "value"}]}], "resources": [{"attributes": [{"name": "name", "value": "value", "operator": "operator"}], "tags": [{"name": "name", "value": "value", "operator": "operator"}]}], "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'
        if_match = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_rule(**req_copy)

    def test_replace_rule_value_error_with_retries(self):
        # Enable retries and run test_replace_rule_value_error.
        _service.enable_retries()
        self.test_replace_rule_value_error()

        # Disable retries and run test_replace_rule_value_error.
        _service.disable_retries()
        self.test_replace_rule_value_error()


class TestDeleteRule():
    """
    Test Class for delete_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_rule_all_params(self):
        """
        delete_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_rule(
            rule_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_rule_all_params_with_retries(self):
        # Enable retries and run test_delete_rule_all_params.
        _service.enable_retries()
        self.test_delete_rule_all_params()

        # Disable retries and run test_delete_rule_all_params.
        _service.disable_retries()
        self.test_delete_rule_all_params()

    @responses.activate
    def test_delete_rule_required_params(self):
        """
        test_delete_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = _service.delete_rule(
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_rule_required_params_with_retries(self):
        # Enable retries and run test_delete_rule_required_params.
        _service.enable_retries()
        self.test_delete_rule_required_params()

        # Disable retries and run test_delete_rule_required_params.
        _service.disable_retries()
        self.test_delete_rule_required_params()

    @responses.activate
    def test_delete_rule_value_error(self):
        """
        test_delete_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_rule(**req_copy)

    def test_delete_rule_value_error_with_retries(self):
        # Enable retries and run test_delete_rule_value_error.
        _service.enable_retries()
        self.test_delete_rule_value_error()

        # Disable retries and run test_delete_rule_value_error.
        _service.disable_retries()
        self.test_delete_rule_value_error()


# endregion
##############################################################################
# End of Service: Rules
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

        service = ContextBasedRestrictionsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ContextBasedRestrictionsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ContextBasedRestrictionsV1.new_instance(
            )


class TestGetAccountSettings():
    """
    Test Class for get_account_settings
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url)  # don't double-encode if already encoded
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
        url = self.preprocess_url(_base_url + '/v1/account_settings/testString')
        mock_response = '{"id": "id", "crn": "crn", "rule_count_limit": 16, "zone_count_limit": 16, "current_rule_count": 18, "current_zone_count": 18, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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
        url = self.preprocess_url(_base_url + '/v1/account_settings/testString')
        mock_response = '{"id": "id", "crn": "crn", "rule_count_limit": 16, "zone_count_limit": 16, "current_rule_count": 18, "current_zone_count": 18, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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
        url = self.preprocess_url(_base_url + '/v1/account_settings/testString')
        mock_response = '{"id": "id", "crn": "crn", "rule_count_limit": 16, "zone_count_limit": 16, "current_rule_count": 18, "current_zone_count": 18, "href": "href", "created_at": "2019-01-01T12:00:00.000Z", "created_by_id": "created_by_id", "last_modified_at": "2019-01-01T12:00:00.000Z", "last_modified_by_id": "last_modified_by_id"}'
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
        account_settings_model_json['id'] = 'testString'
        account_settings_model_json['crn'] = 'testString'
        account_settings_model_json['rule_count_limit'] = 38
        account_settings_model_json['zone_count_limit'] = 38
        account_settings_model_json['current_rule_count'] = 38
        account_settings_model_json['current_zone_count'] = 38
        account_settings_model_json['href'] = 'testString'
        account_settings_model_json['created_at'] = "2019-01-01T12:00:00Z"
        account_settings_model_json['created_by_id'] = 'testString'
        account_settings_model_json['last_modified_at'] = "2019-01-01T12:00:00Z"
        account_settings_model_json['last_modified_by_id'] = 'testString'

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


class TestModel_Resource():
    """
    Test Class for Resource
    """

    def test_resource_serialization(self):
        """
        Test serialization/deserialization for Resource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_attribute_model = {}  # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_attribute_model = {}  # ResourceTagAttribute
        resource_tag_attribute_model['name'] = 'testString'
        resource_tag_attribute_model['value'] = 'testString'
        resource_tag_attribute_model['operator'] = 'testString'

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['attributes'] = [resource_attribute_model]
        resource_model_json['tags'] = [resource_tag_attribute_model]

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model = Resource.from_dict(resource_model_json)
        assert resource_model != False

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model_dict = Resource.from_dict(resource_model_json).__dict__
        resource_model2 = Resource(**resource_model_dict)

        # Verify the model instances are equivalent
        assert resource_model == resource_model2

        # Convert model instance back to dict and verify no loss of data
        resource_model_json2 = resource_model.to_dict()
        assert resource_model_json2 == resource_model_json


class TestModel_ResourceAttribute():
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


class TestModel_ResourceTagAttribute():
    """
    Test Class for ResourceTagAttribute
    """

    def test_resource_tag_attribute_serialization(self):
        """
        Test serialization/deserialization for ResourceTagAttribute
        """

        # Construct a json representation of a ResourceTagAttribute model
        resource_tag_attribute_model_json = {}
        resource_tag_attribute_model_json['name'] = 'testString'
        resource_tag_attribute_model_json['value'] = 'testString'
        resource_tag_attribute_model_json['operator'] = 'testString'

        # Construct a model instance of ResourceTagAttribute by calling from_dict on the json representation
        resource_tag_attribute_model = ResourceTagAttribute.from_dict(resource_tag_attribute_model_json)
        assert resource_tag_attribute_model != False

        # Construct a model instance of ResourceTagAttribute by calling from_dict on the json representation
        resource_tag_attribute_model_dict = ResourceTagAttribute.from_dict(resource_tag_attribute_model_json).__dict__
        resource_tag_attribute_model2 = ResourceTagAttribute(**resource_tag_attribute_model_dict)

        # Verify the model instances are equivalent
        assert resource_tag_attribute_model == resource_tag_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        resource_tag_attribute_model_json2 = resource_tag_attribute_model.to_dict()
        assert resource_tag_attribute_model_json2 == resource_tag_attribute_model_json


class TestModel_Rule():
    """
    Test Class for Rule
    """

    def test_rule_serialization(self):
        """
        Test serialization/deserialization for Rule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_context_attribute_model = {}  # RuleContextAttribute
        rule_context_attribute_model['name'] = 'testString'
        rule_context_attribute_model['value'] = 'testString'

        rule_context_model = {}  # RuleContext
        rule_context_model['attributes'] = [rule_context_attribute_model]

        resource_attribute_model = {}  # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_attribute_model = {}  # ResourceTagAttribute
        resource_tag_attribute_model['name'] = 'testString'
        resource_tag_attribute_model['value'] = 'testString'
        resource_tag_attribute_model['operator'] = 'testString'

        resource_model = {}  # Resource
        resource_model['attributes'] = [resource_attribute_model]
        resource_model['tags'] = [resource_tag_attribute_model]

        # Construct a json representation of a Rule model
        rule_model_json = {}
        rule_model_json['id'] = 'testString'
        rule_model_json['crn'] = 'testString'
        rule_model_json['description'] = 'testString'
        rule_model_json['contexts'] = [rule_context_model]
        rule_model_json['resources'] = [resource_model]
        rule_model_json['href'] = 'testString'
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


class TestModel_RuleContext():
    """
    Test Class for RuleContext
    """

    def test_rule_context_serialization(self):
        """
        Test serialization/deserialization for RuleContext
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_context_attribute_model = {}  # RuleContextAttribute
        rule_context_attribute_model['name'] = 'testString'
        rule_context_attribute_model['value'] = 'testString'

        # Construct a json representation of a RuleContext model
        rule_context_model_json = {}
        rule_context_model_json['attributes'] = [rule_context_attribute_model]

        # Construct a model instance of RuleContext by calling from_dict on the json representation
        rule_context_model = RuleContext.from_dict(rule_context_model_json)
        assert rule_context_model != False

        # Construct a model instance of RuleContext by calling from_dict on the json representation
        rule_context_model_dict = RuleContext.from_dict(rule_context_model_json).__dict__
        rule_context_model2 = RuleContext(**rule_context_model_dict)

        # Verify the model instances are equivalent
        assert rule_context_model == rule_context_model2

        # Convert model instance back to dict and verify no loss of data
        rule_context_model_json2 = rule_context_model.to_dict()
        assert rule_context_model_json2 == rule_context_model_json


class TestModel_RuleContextAttribute():
    """
    Test Class for RuleContextAttribute
    """

    def test_rule_context_attribute_serialization(self):
        """
        Test serialization/deserialization for RuleContextAttribute
        """

        # Construct a json representation of a RuleContextAttribute model
        rule_context_attribute_model_json = {}
        rule_context_attribute_model_json['name'] = 'testString'
        rule_context_attribute_model_json['value'] = 'testString'

        # Construct a model instance of RuleContextAttribute by calling from_dict on the json representation
        rule_context_attribute_model = RuleContextAttribute.from_dict(rule_context_attribute_model_json)
        assert rule_context_attribute_model != False

        # Construct a model instance of RuleContextAttribute by calling from_dict on the json representation
        rule_context_attribute_model_dict = RuleContextAttribute.from_dict(rule_context_attribute_model_json).__dict__
        rule_context_attribute_model2 = RuleContextAttribute(**rule_context_attribute_model_dict)

        # Verify the model instances are equivalent
        assert rule_context_attribute_model == rule_context_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        rule_context_attribute_model_json2 = rule_context_attribute_model.to_dict()
        assert rule_context_attribute_model_json2 == rule_context_attribute_model_json


class TestModel_RuleList():
    """
    Test Class for RuleList
    """

    def test_rule_list_serialization(self):
        """
        Test serialization/deserialization for RuleList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_context_attribute_model = {}  # RuleContextAttribute
        rule_context_attribute_model['name'] = 'testString'
        rule_context_attribute_model['value'] = 'testString'

        rule_context_model = {}  # RuleContext
        rule_context_model['attributes'] = [rule_context_attribute_model]

        resource_attribute_model = {}  # ResourceAttribute
        resource_attribute_model['name'] = 'testString'
        resource_attribute_model['value'] = 'testString'
        resource_attribute_model['operator'] = 'testString'

        resource_tag_attribute_model = {}  # ResourceTagAttribute
        resource_tag_attribute_model['name'] = 'testString'
        resource_tag_attribute_model['value'] = 'testString'
        resource_tag_attribute_model['operator'] = 'testString'

        resource_model = {}  # Resource
        resource_model['attributes'] = [resource_attribute_model]
        resource_model['tags'] = [resource_tag_attribute_model]

        rule_model = {}  # Rule
        rule_model['id'] = 'testString'
        rule_model['crn'] = 'testString'
        rule_model['description'] = 'testString'
        rule_model['contexts'] = [rule_context_model]
        rule_model['resources'] = [resource_model]
        rule_model['href'] = 'testString'
        rule_model['created_at'] = "2019-01-01T12:00:00Z"
        rule_model['created_by_id'] = 'testString'
        rule_model['last_modified_at'] = "2019-01-01T12:00:00Z"
        rule_model['last_modified_by_id'] = 'testString'

        # Construct a json representation of a RuleList model
        rule_list_model_json = {}
        rule_list_model_json['count'] = 38
        rule_list_model_json['rules'] = [rule_model]

        # Construct a model instance of RuleList by calling from_dict on the json representation
        rule_list_model = RuleList.from_dict(rule_list_model_json)
        assert rule_list_model != False

        # Construct a model instance of RuleList by calling from_dict on the json representation
        rule_list_model_dict = RuleList.from_dict(rule_list_model_json).__dict__
        rule_list_model2 = RuleList(**rule_list_model_dict)

        # Verify the model instances are equivalent
        assert rule_list_model == rule_list_model2

        # Convert model instance back to dict and verify no loss of data
        rule_list_model_json2 = rule_list_model.to_dict()
        assert rule_list_model_json2 == rule_list_model_json


class TestModel_ServiceRefTarget():
    """
    Test Class for ServiceRefTarget
    """

    def test_service_ref_target_serialization(self):
        """
        Test serialization/deserialization for ServiceRefTarget
        """

        # Construct a json representation of a ServiceRefTarget model
        service_ref_target_model_json = {}
        service_ref_target_model_json['service_name'] = 'testString'
        service_ref_target_model_json['service_type'] = 'testString'

        # Construct a model instance of ServiceRefTarget by calling from_dict on the json representation
        service_ref_target_model = ServiceRefTarget.from_dict(service_ref_target_model_json)
        assert service_ref_target_model != False

        # Construct a model instance of ServiceRefTarget by calling from_dict on the json representation
        service_ref_target_model_dict = ServiceRefTarget.from_dict(service_ref_target_model_json).__dict__
        service_ref_target_model2 = ServiceRefTarget(**service_ref_target_model_dict)

        # Verify the model instances are equivalent
        assert service_ref_target_model == service_ref_target_model2

        # Convert model instance back to dict and verify no loss of data
        service_ref_target_model_json2 = service_ref_target_model.to_dict()
        assert service_ref_target_model_json2 == service_ref_target_model_json


class TestModel_ServiceRefTargetList():
    """
    Test Class for ServiceRefTargetList
    """

    def test_service_ref_target_list_serialization(self):
        """
        Test serialization/deserialization for ServiceRefTargetList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        service_ref_target_model = {}  # ServiceRefTarget
        service_ref_target_model['service_name'] = 'testString'
        service_ref_target_model['service_type'] = 'testString'

        # Construct a json representation of a ServiceRefTargetList model
        service_ref_target_list_model_json = {}
        service_ref_target_list_model_json['count'] = 38
        service_ref_target_list_model_json['targets'] = [service_ref_target_model]

        # Construct a model instance of ServiceRefTargetList by calling from_dict on the json representation
        service_ref_target_list_model = ServiceRefTargetList.from_dict(service_ref_target_list_model_json)
        assert service_ref_target_list_model != False

        # Construct a model instance of ServiceRefTargetList by calling from_dict on the json representation
        service_ref_target_list_model_dict = ServiceRefTargetList.from_dict(service_ref_target_list_model_json).__dict__
        service_ref_target_list_model2 = ServiceRefTargetList(**service_ref_target_list_model_dict)

        # Verify the model instances are equivalent
        assert service_ref_target_list_model == service_ref_target_list_model2

        # Convert model instance back to dict and verify no loss of data
        service_ref_target_list_model_json2 = service_ref_target_list_model.to_dict()
        assert service_ref_target_list_model_json2 == service_ref_target_list_model_json


class TestModel_ServiceRefValue():
    """
    Test Class for ServiceRefValue
    """

    def test_service_ref_value_serialization(self):
        """
        Test serialization/deserialization for ServiceRefValue
        """

        # Construct a json representation of a ServiceRefValue model
        service_ref_value_model_json = {}
        service_ref_value_model_json['account_id'] = 'testString'
        service_ref_value_model_json['service_type'] = 'testString'
        service_ref_value_model_json['service_name'] = 'testString'
        service_ref_value_model_json['service_instance'] = 'testString'

        # Construct a model instance of ServiceRefValue by calling from_dict on the json representation
        service_ref_value_model = ServiceRefValue.from_dict(service_ref_value_model_json)
        assert service_ref_value_model != False

        # Construct a model instance of ServiceRefValue by calling from_dict on the json representation
        service_ref_value_model_dict = ServiceRefValue.from_dict(service_ref_value_model_json).__dict__
        service_ref_value_model2 = ServiceRefValue(**service_ref_value_model_dict)

        # Verify the model instances are equivalent
        assert service_ref_value_model == service_ref_value_model2

        # Convert model instance back to dict and verify no loss of data
        service_ref_value_model_json2 = service_ref_value_model.to_dict()
        assert service_ref_value_model_json2 == service_ref_value_model_json


class TestModel_Zone():
    """
    Test Class for Zone
    """

    def test_zone_serialization(self):
        """
        Test serialization/deserialization for Zone
        """

        # Construct dict forms of any model objects needed in order to build this model.

        address_model = {}  # AddressIPAddress
        address_model['type'] = 'ipAddress'
        address_model['value'] = 'testString'

        # Construct a json representation of a Zone model
        zone_model_json = {}
        zone_model_json['id'] = 'testString'
        zone_model_json['crn'] = 'testString'
        zone_model_json['name'] = 'testString'
        zone_model_json['account_id'] = 'testString'
        zone_model_json['description'] = 'testString'
        zone_model_json['addresses'] = [address_model]
        zone_model_json['excluded'] = [address_model]
        zone_model_json['href'] = 'testString'
        zone_model_json['created_at'] = "2019-01-01T12:00:00Z"
        zone_model_json['created_by_id'] = 'testString'
        zone_model_json['last_modified_at'] = "2019-01-01T12:00:00Z"
        zone_model_json['last_modified_by_id'] = 'testString'

        # Construct a model instance of Zone by calling from_dict on the json representation
        zone_model = Zone.from_dict(zone_model_json)
        assert zone_model != False

        # Construct a model instance of Zone by calling from_dict on the json representation
        zone_model_dict = Zone.from_dict(zone_model_json).__dict__
        zone_model2 = Zone(**zone_model_dict)

        # Verify the model instances are equivalent
        assert zone_model == zone_model2

        # Convert model instance back to dict and verify no loss of data
        zone_model_json2 = zone_model.to_dict()
        assert zone_model_json2 == zone_model_json


class TestModel_ZoneList():
    """
    Test Class for ZoneList
    """

    def test_zone_list_serialization(self):
        """
        Test serialization/deserialization for ZoneList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        address_model = {}  # AddressIPAddress
        address_model['type'] = 'ipAddress'
        address_model['value'] = 'testString'

        zone_summary_model = {}  # ZoneSummary
        zone_summary_model['id'] = 'testString'
        zone_summary_model['crn'] = 'testString'
        zone_summary_model['name'] = 'testString'
        zone_summary_model['description'] = 'testString'
        zone_summary_model['addresses_preview'] = [address_model]
        zone_summary_model['address_count'] = 38
        zone_summary_model['excluded_count'] = 38
        zone_summary_model['href'] = 'testString'
        zone_summary_model['created_at'] = "2019-01-01T12:00:00Z"
        zone_summary_model['created_by_id'] = 'testString'
        zone_summary_model['last_modified_at'] = "2019-01-01T12:00:00Z"
        zone_summary_model['last_modified_by_id'] = 'testString'

        # Construct a json representation of a ZoneList model
        zone_list_model_json = {}
        zone_list_model_json['count'] = 38
        zone_list_model_json['zones'] = [zone_summary_model]

        # Construct a model instance of ZoneList by calling from_dict on the json representation
        zone_list_model = ZoneList.from_dict(zone_list_model_json)
        assert zone_list_model != False

        # Construct a model instance of ZoneList by calling from_dict on the json representation
        zone_list_model_dict = ZoneList.from_dict(zone_list_model_json).__dict__
        zone_list_model2 = ZoneList(**zone_list_model_dict)

        # Verify the model instances are equivalent
        assert zone_list_model == zone_list_model2

        # Convert model instance back to dict and verify no loss of data
        zone_list_model_json2 = zone_list_model.to_dict()
        assert zone_list_model_json2 == zone_list_model_json


class TestModel_ZoneSummary():
    """
    Test Class for ZoneSummary
    """

    def test_zone_summary_serialization(self):
        """
        Test serialization/deserialization for ZoneSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        address_model = {}  # AddressIPAddress
        address_model['type'] = 'ipAddress'
        address_model['value'] = 'testString'

        # Construct a json representation of a ZoneSummary model
        zone_summary_model_json = {}
        zone_summary_model_json['id'] = 'testString'
        zone_summary_model_json['crn'] = 'testString'
        zone_summary_model_json['name'] = 'testString'
        zone_summary_model_json['description'] = 'testString'
        zone_summary_model_json['addresses_preview'] = [address_model]
        zone_summary_model_json['address_count'] = 38
        zone_summary_model_json['excluded_count'] = 38
        zone_summary_model_json['href'] = 'testString'
        zone_summary_model_json['created_at'] = "2019-01-01T12:00:00Z"
        zone_summary_model_json['created_by_id'] = 'testString'
        zone_summary_model_json['last_modified_at'] = "2019-01-01T12:00:00Z"
        zone_summary_model_json['last_modified_by_id'] = 'testString'

        # Construct a model instance of ZoneSummary by calling from_dict on the json representation
        zone_summary_model = ZoneSummary.from_dict(zone_summary_model_json)
        assert zone_summary_model != False

        # Construct a model instance of ZoneSummary by calling from_dict on the json representation
        zone_summary_model_dict = ZoneSummary.from_dict(zone_summary_model_json).__dict__
        zone_summary_model2 = ZoneSummary(**zone_summary_model_dict)

        # Verify the model instances are equivalent
        assert zone_summary_model == zone_summary_model2

        # Convert model instance back to dict and verify no loss of data
        zone_summary_model_json2 = zone_summary_model.to_dict()
        assert zone_summary_model_json2 == zone_summary_model_json


class TestModel_AddressIPAddress():
    """
    Test Class for AddressIPAddress
    """

    def test_address_ip_address_serialization(self):
        """
        Test serialization/deserialization for AddressIPAddress
        """

        # Construct a json representation of a AddressIPAddress model
        address_ip_address_model_json = {}
        address_ip_address_model_json['type'] = 'ipAddress'
        address_ip_address_model_json['value'] = 'testString'

        # Construct a model instance of AddressIPAddress by calling from_dict on the json representation
        address_ip_address_model = AddressIPAddress.from_dict(address_ip_address_model_json)
        assert address_ip_address_model != False

        # Construct a model instance of AddressIPAddress by calling from_dict on the json representation
        address_ip_address_model_dict = AddressIPAddress.from_dict(address_ip_address_model_json).__dict__
        address_ip_address_model2 = AddressIPAddress(**address_ip_address_model_dict)

        # Verify the model instances are equivalent
        assert address_ip_address_model == address_ip_address_model2

        # Convert model instance back to dict and verify no loss of data
        address_ip_address_model_json2 = address_ip_address_model.to_dict()
        assert address_ip_address_model_json2 == address_ip_address_model_json


class TestModel_AddressIPAddressRange():
    """
    Test Class for AddressIPAddressRange
    """

    def test_address_ip_address_range_serialization(self):
        """
        Test serialization/deserialization for AddressIPAddressRange
        """

        # Construct a json representation of a AddressIPAddressRange model
        address_ip_address_range_model_json = {}
        address_ip_address_range_model_json['type'] = 'ipRange'
        address_ip_address_range_model_json['value'] = 'testString'

        # Construct a model instance of AddressIPAddressRange by calling from_dict on the json representation
        address_ip_address_range_model = AddressIPAddressRange.from_dict(address_ip_address_range_model_json)
        assert address_ip_address_range_model != False

        # Construct a model instance of AddressIPAddressRange by calling from_dict on the json representation
        address_ip_address_range_model_dict = AddressIPAddressRange.from_dict(
            address_ip_address_range_model_json).__dict__
        address_ip_address_range_model2 = AddressIPAddressRange(**address_ip_address_range_model_dict)

        # Verify the model instances are equivalent
        assert address_ip_address_range_model == address_ip_address_range_model2

        # Convert model instance back to dict and verify no loss of data
        address_ip_address_range_model_json2 = address_ip_address_range_model.to_dict()
        assert address_ip_address_range_model_json2 == address_ip_address_range_model_json


class TestModel_AddressServiceRef():
    """
    Test Class for AddressServiceRef
    """

    def test_address_service_ref_serialization(self):
        """
        Test serialization/deserialization for AddressServiceRef
        """

        # Construct dict forms of any model objects needed in order to build this model.

        service_ref_value_model = {}  # ServiceRefValue
        service_ref_value_model['account_id'] = 'testString'
        service_ref_value_model['service_type'] = 'testString'
        service_ref_value_model['service_name'] = 'testString'
        service_ref_value_model['service_instance'] = 'testString'

        # Construct a json representation of a AddressServiceRef model
        address_service_ref_model_json = {}
        address_service_ref_model_json['type'] = 'serviceRef'
        address_service_ref_model_json['ref'] = service_ref_value_model

        # Construct a model instance of AddressServiceRef by calling from_dict on the json representation
        address_service_ref_model = AddressServiceRef.from_dict(address_service_ref_model_json)
        assert address_service_ref_model != False

        # Construct a model instance of AddressServiceRef by calling from_dict on the json representation
        address_service_ref_model_dict = AddressServiceRef.from_dict(address_service_ref_model_json).__dict__
        address_service_ref_model2 = AddressServiceRef(**address_service_ref_model_dict)

        # Verify the model instances are equivalent
        assert address_service_ref_model == address_service_ref_model2

        # Convert model instance back to dict and verify no loss of data
        address_service_ref_model_json2 = address_service_ref_model.to_dict()
        assert address_service_ref_model_json2 == address_service_ref_model_json


class TestModel_AddressSubnet():
    """
    Test Class for AddressSubnet
    """

    def test_address_subnet_serialization(self):
        """
        Test serialization/deserialization for AddressSubnet
        """

        # Construct a json representation of a AddressSubnet model
        address_subnet_model_json = {}
        address_subnet_model_json['type'] = 'subnet'
        address_subnet_model_json['value'] = 'testString'

        # Construct a model instance of AddressSubnet by calling from_dict on the json representation
        address_subnet_model = AddressSubnet.from_dict(address_subnet_model_json)
        assert address_subnet_model != False

        # Construct a model instance of AddressSubnet by calling from_dict on the json representation
        address_subnet_model_dict = AddressSubnet.from_dict(address_subnet_model_json).__dict__
        address_subnet_model2 = AddressSubnet(**address_subnet_model_dict)

        # Verify the model instances are equivalent
        assert address_subnet_model == address_subnet_model2

        # Convert model instance back to dict and verify no loss of data
        address_subnet_model_json2 = address_subnet_model.to_dict()
        assert address_subnet_model_json2 == address_subnet_model_json


class TestModel_AddressVPC():
    """
    Test Class for AddressVPC
    """

    def test_address_vpc_serialization(self):
        """
        Test serialization/deserialization for AddressVPC
        """

        # Construct a json representation of a AddressVPC model
        address_vpc_model_json = {}
        address_vpc_model_json['type'] = 'vpc'
        address_vpc_model_json['value'] = 'testString'

        # Construct a model instance of AddressVPC by calling from_dict on the json representation
        address_vpc_model = AddressVPC.from_dict(address_vpc_model_json)
        assert address_vpc_model != False

        # Construct a model instance of AddressVPC by calling from_dict on the json representation
        address_vpc_model_dict = AddressVPC.from_dict(address_vpc_model_json).__dict__
        address_vpc_model2 = AddressVPC(**address_vpc_model_dict)

        # Verify the model instances are equivalent
        assert address_vpc_model == address_vpc_model2

        # Convert model instance back to dict and verify no loss of data
        address_vpc_model_json2 = address_vpc_model.to_dict()
        assert address_vpc_model_json2 == address_vpc_model_json

# endregion
##############################################################################
# End of Model Tests
##############################################################################
