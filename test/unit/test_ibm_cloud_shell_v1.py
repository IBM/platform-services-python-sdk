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
Unit Tests for IbmCloudShellV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import responses
import urllib
from ibm_platform_services.ibm_cloud_shell_v1 import *


_service = IbmCloudShellV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://api.shell.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: AccountSettings
##############################################################################
# region

class TestGetAccountSettings():
    """
    Test Class for get_account_settings
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
    def test_get_account_settings_all_params(self):
        """
        get_account_settings()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/api/v1/user/accounts/12345678-abcd-1a2b-a1b2-1234567890ab/settings')
        mock_response = '{"_id": "id", "_rev": "rev", "account_id": "account_id", "created_at": 10, "created_by": "created_by", "default_enable_new_features": false, "default_enable_new_regions": true, "enabled": false, "features": [{"enabled": false, "key": "key"}], "regions": [{"enabled": false, "key": "key"}], "type": "type", "updated_at": 10, "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = '12345678-abcd-1a2b-a1b2-1234567890ab'

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
        url = self.preprocess_url(_base_url + '/api/v1/user/accounts/12345678-abcd-1a2b-a1b2-1234567890ab/settings')
        mock_response = '{"_id": "id", "_rev": "rev", "account_id": "account_id", "created_at": 10, "created_by": "created_by", "default_enable_new_features": false, "default_enable_new_regions": true, "enabled": false, "features": [{"enabled": false, "key": "key"}], "regions": [{"enabled": false, "key": "key"}], "type": "type", "updated_at": 10, "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = '12345678-abcd-1a2b-a1b2-1234567890ab'

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
        url = self.preprocess_url(_base_url + '/api/v1/user/accounts/12345678-abcd-1a2b-a1b2-1234567890ab/settings')
        mock_response = '{"_id": "id", "_rev": "rev", "account_id": "account_id", "created_at": 10, "created_by": "created_by", "default_enable_new_features": false, "default_enable_new_regions": true, "enabled": false, "features": [{"enabled": false, "key": "key"}], "regions": [{"enabled": false, "key": "key"}], "type": "type", "updated_at": 10, "updated_by": "updated_by"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Feature model
        feature_model = [{
            'enabled': True,
            'key': 'server.file_manager',
        },
        {
            'enabled': True,
            'key': 'server.web_preview',
        }]

        # Construct a dict representation of a RegionSetting model
        region_setting_model = [{
            'enabled': True,
            'key': 'eu-de',
        },
        {
            'enabled': True,
            'key': 'jp-tok',
        },
        {
            'enabled': True,
            'key': 'us-south',
        }]

        # Set up parameter values
        account_id = '12345678-abcd-1a2b-a1b2-1234567890ab'
        rev = '130-12345678-abcd-1a2b-a1b2-1234567890ab'
        default_enable_new_features = True
        default_enable_new_regions = True
        enabled = True
        features = feature_model
        regions = region_setting_model

        # Invoke method
        response = _service.update_account_settings(
            account_id,
            rev=rev,
            default_enable_new_features=default_enable_new_features,
            default_enable_new_regions=default_enable_new_regions,
            enabled=enabled,
            features=features,
            regions=regions,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['_rev'] == '130-12345678-abcd-1a2b-a1b2-1234567890ab'
        assert req_body['default_enable_new_features'] == True
        assert req_body['default_enable_new_regions'] == True
        assert req_body['enabled'] == True
        assert req_body['features'] == feature_model
        assert req_body['regions'] == region_setting_model


    @responses.activate
    def test_update_account_settings_value_error(self):
        """
        test_update_account_settings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/api/v1/user/accounts/12345678-abcd-1a2b-a1b2-1234567890ab/settings')
        mock_response = '{"_id": "id", "_rev": "rev", "account_id": "account_id", "created_at": 10, "created_by": "created_by", "default_enable_new_features": false, "default_enable_new_regions": true, "enabled": false, "features": [{"enabled": false, "key": "key"}], "regions": [{"enabled": false, "key": "key"}], "type": "type", "updated_at": 10, "updated_by": "updated_by"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Feature model
        feature_model = [{
            'enabled': True,
            'key': 'server.file_manager',
        },
        {
            'enabled': True,
            'key': 'server.web_preview',
        }]

        # Construct a dict representation of a RegionSetting model
        region_setting_model = [{
            'enabled': True,
            'key': 'eu-de',
        },
        {
            'enabled': True,
            'key': 'jp-tok',
        },
        {
            'enabled': True,
            'key': 'us-south',
        }]

        # Set up parameter values
        account_id = '12345678-abcd-1a2b-a1b2-1234567890ab'
        rev = '130-12345678-abcd-1a2b-a1b2-1234567890ab'
        default_enable_new_features = True
        default_enable_new_regions = True
        enabled = True
        features = [feature_model]
        regions = [region_setting_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
class AccountSettingsUnitTests():
    """
    Test Class for AccountSettings
    """

    def test_account_settings_serialization(self):
        """
        Test serialization/deserialization for AccountSettings
        """

        # Construct dict forms of any model objects needed in order to build this model.
        feature_model = [{
            'enabled': True,
            'key': 'server.file_manager',
        },
        {
            'enabled': True,
            'key': 'server.web_preview',
        }]

        region_setting_model = [{
            'enabled': True,
            'key': 'eu-de',
        },
        {
            'enabled': True,
            'key': 'jp-tok',
        },
        {
            'enabled': True,
            'key': 'us-south',
        }]

        # Construct a json representation of a AccountSettings model
        account_settings_model_json = {}
        account_settings_model_json['_id'] = 'ac-12345678-abcd-1a2b-a1b2-1234567890ab'
        account_settings_model_json['_rev'] = '130-12345678-abcd-1a2b-a1b2-1234567890ab'
        account_settings_model_json['account_id'] = '12345678-abcd-1a2b-a1b2-1234567890ab'
        account_settings_model_json['created_at'] = 1600079615
        account_settings_model_json['created_by'] = 'IBMid-1000000000'
        account_settings_model_json['default_enable_new_features'] = True
        account_settings_model_json['default_enable_new_regions'] = True
        account_settings_model_json['enabled'] = True
        account_settings_model_json['features'] = feature_model
        account_settings_model_json['regions'] = region_setting_model
        account_settings_model_json['type'] = 'account_settings'
        account_settings_model_json['updated_at'] = 1624359948
        account_settings_model_json['updated_by'] = 'IBMid-1000000000'

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

class FeatureUnitTests():
    """
    Test Class for Feature
    """

    def test_feature_serialization(self):
        """
        Test serialization/deserialization for Feature
        """

        # Construct a json representation of a Feature model
        feature_model_json = {}
        feature_model_json['enabled'] = True
        feature_model_json['key'] = 'server.file_manager'

        # Construct a model instance of Feature by calling from_dict on the json representation
        feature_model = Feature.from_dict(feature_model_json)
        assert feature_model != False

        # Construct a model instance of Feature by calling from_dict on the json representation
        feature_model_dict = Feature.from_dict(feature_model_json).__dict__
        feature_model2 = Feature(**feature_model_dict)

        # Verify the model instances are equivalent
        assert feature_model == feature_model2

        # Convert model instance back to dict and verify no loss of data
        feature_model_json2 = feature_model.to_dict()
        assert feature_model_json2 == feature_model_json

class RegionSettingUnitTests():
    """
    Test Class for RegionSetting
    """

    def test_region_setting_serialization(self):
        """
        Test serialization/deserialization for RegionSetting
        """

        # Construct a json representation of a RegionSetting model
        region_setting_model_json = {}
        region_setting_model_json['enabled'] = True
        region_setting_model_json['key'] = 'eu-de'

        # Construct a model instance of RegionSetting by calling from_dict on the json representation
        region_setting_model = RegionSetting.from_dict(region_setting_model_json)
        assert region_setting_model != False

        # Construct a model instance of RegionSetting by calling from_dict on the json representation
        region_setting_model_dict = RegionSetting.from_dict(region_setting_model_json).__dict__
        region_setting_model2 = RegionSetting(**region_setting_model_dict)

        # Verify the model instances are equivalent
        assert region_setting_model == region_setting_model2

        # Convert model instance back to dict and verify no loss of data
        region_setting_model_json2 = region_setting_model.to_dict()
        assert region_setting_model_json2 == region_setting_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
