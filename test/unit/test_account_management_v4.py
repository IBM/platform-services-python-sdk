# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
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
Unit Tests for AccountManagementV4
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_platform_services.account_management_v4 import *


_service = AccountManagementV4(authenticator=NoAuthAuthenticator())

_base_url = 'https://accounts.test.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Default
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

        service = AccountManagementV4.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AccountManagementV4)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AccountManagementV4.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetAccount:
    """
    Test Class for get_account
    """

    @responses.activate
    def test_get_account_all_params(self):
        """
        get_account()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString')
        mock_response = '{"name": "name", "id": "id", "owner": "owner", "owner_userid": "owner_userid", "owner_iamid": "owner_iamid", "type": "type", "status": "status", "linked_softlayer_account": "linked_softlayer_account", "team_directory_enabled": true, "traits": {"eu_supported": true, "poc": false, "hippa": false}}'
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
        response = _service.get_account(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_account_all_params_with_retries(self):
        # Enable retries and run test_get_account_all_params.
        _service.enable_retries()
        self.test_get_account_all_params()

        # Disable retries and run test_get_account_all_params.
        _service.disable_retries()
        self.test_get_account_all_params()

    @responses.activate
    def test_get_account_value_error(self):
        """
        test_get_account_value_error()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString')
        mock_response = '{"name": "name", "id": "id", "owner": "owner", "owner_userid": "owner_userid", "owner_iamid": "owner_iamid", "type": "type", "status": "status", "linked_softlayer_account": "linked_softlayer_account", "team_directory_enabled": true, "traits": {"eu_supported": true, "poc": false, "hippa": false}}'
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
                _service.get_account(**req_copy)

    def test_get_account_value_error_with_retries(self):
        # Enable retries and run test_get_account_value_error.
        _service.enable_retries()
        self.test_get_account_value_error()

        # Disable retries and run test_get_account_value_error.
        _service.disable_retries()
        self.test_get_account_value_error()


# endregion
##############################################################################
# End of Service: Default
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AccountResponseTraits:
    """
    Test Class for AccountResponseTraits
    """

    def test_account_response_traits_serialization(self):
        """
        Test serialization/deserialization for AccountResponseTraits
        """

        # Construct a json representation of a AccountResponseTraits model
        account_response_traits_model_json = {}
        account_response_traits_model_json['eu_supported'] = True
        account_response_traits_model_json['poc'] = True
        account_response_traits_model_json['hippa'] = True

        # Construct a model instance of AccountResponseTraits by calling from_dict on the json representation
        account_response_traits_model = AccountResponseTraits.from_dict(account_response_traits_model_json)
        assert account_response_traits_model != False

        # Construct a model instance of AccountResponseTraits by calling from_dict on the json representation
        account_response_traits_model_dict = AccountResponseTraits.from_dict(
            account_response_traits_model_json
        ).__dict__
        account_response_traits_model2 = AccountResponseTraits(**account_response_traits_model_dict)

        # Verify the model instances are equivalent
        assert account_response_traits_model == account_response_traits_model2

        # Convert model instance back to dict and verify no loss of data
        account_response_traits_model_json2 = account_response_traits_model.to_dict()
        assert account_response_traits_model_json2 == account_response_traits_model_json


class TestModel_AccountResponse:
    """
    Test Class for AccountResponse
    """

    def test_account_response_serialization(self):
        """
        Test serialization/deserialization for AccountResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_response_traits_model = {}  # AccountResponseTraits
        account_response_traits_model['eu_supported'] = True
        account_response_traits_model['poc'] = True
        account_response_traits_model['hippa'] = True

        # Construct a json representation of a AccountResponse model
        account_response_model_json = {}
        account_response_model_json['name'] = 'testString'
        account_response_model_json['id'] = 'testString'
        account_response_model_json['owner'] = 'testString'
        account_response_model_json['owner_userid'] = 'testString'
        account_response_model_json['owner_iamid'] = 'testString'
        account_response_model_json['type'] = 'testString'
        account_response_model_json['status'] = 'testString'
        account_response_model_json['linked_softlayer_account'] = 'testString'
        account_response_model_json['team_directory_enabled'] = True
        account_response_model_json['traits'] = account_response_traits_model

        # Construct a model instance of AccountResponse by calling from_dict on the json representation
        account_response_model = AccountResponse.from_dict(account_response_model_json)
        assert account_response_model != False

        # Construct a model instance of AccountResponse by calling from_dict on the json representation
        account_response_model_dict = AccountResponse.from_dict(account_response_model_json).__dict__
        account_response_model2 = AccountResponse(**account_response_model_dict)

        # Verify the model instances are equivalent
        assert account_response_model == account_response_model2

        # Convert model instance back to dict and verify no loss of data
        account_response_model_json2 = account_response_model.to_dict()
        assert account_response_model_json2 == account_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
