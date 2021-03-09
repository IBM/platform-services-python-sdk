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
Unit Tests for PostureManagementV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.posture_management_v1 import *


service = PostureManagementV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://fake'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Scans
##############################################################################
# region

class TestCreateValidationScan():
    """
    Test Class for create_validation_scan
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
    def test_create_validation_scan_all_params(self):
        """
        create_validation_scan()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/posture/v1/scans/validation')
        mock_response = '{"result": true, "message": "message"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        scope_id = 1
        profile_id = 6
        group_profile_id = 13

        # Invoke method
        response = service.create_validation_scan(
            account_id,
            scope_id=scope_id,
            profile_id=profile_id,
            group_profile_id=group_profile_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['scope_id'] == 1
        assert req_body['profile_id'] == 6
        assert req_body['group_profile_id'] == 13


    @responses.activate
    def test_create_validation_scan_value_error(self):
        """
        test_create_validation_scan_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/posture/v1/scans/validation')
        mock_response = '{"result": true, "message": "message"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        scope_id = 1
        profile_id = 6
        group_profile_id = 13

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_validation_scan(**req_copy)



# endregion
##############################################################################
# End of Service: Scans
##############################################################################

##############################################################################
# Start of Service: Profiles
##############################################################################
# region

class TestListProfile():
    """
    Test Class for list_profile
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
    def test_list_profile_all_params(self):
        """
        list_profile()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/posture/v1/profiles')
        mock_response = '{"profiles": [{"name": "CIS IBM Foundations Benchmark 1.0.0", "no_of_goals": 58, "description": "CIS IBM Foundations Benchmark 1.0.0", "version": 1, "created_by": "IBMid-5500081P68", "modified_by": "IBMid-5500081P68", "reason_for_delete": "reason_for_delete", "applicability_criteria": {"environment": ["[IBM Cloud]"], "resource": ["[My_example_bucket]"], "environment_category": ["[Cloud]"], "resource_category": ["[Storage]"], "resource_type": ["Bucket"], "software_details": {"anyKey": "anyValue"}, "os_details": {"anyKey": "anyValue"}, "additional_details": {"anyKey": "anyValue"}, "environment_category_description": {"mapKey": "Cloud"}, "environment_description": {"mapKey": "IBM Cloud"}, "resource_category_description": {"mapKey": "Storage"}, "resource_type_description": {"mapKey": "Bucket"}, "resource_description": {"mapKey": "My_specific_bucket"}}, "profile_id": 3045, "base_profile": "CIS IBM Foundations Benchmark 1.0.0", "profile_type": "predefined", "created_time": "2021-02-26T04:07:25Z", "modified_time": "2021-02-26T04:07:25Z", "enabled": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'

        # Invoke method
        response = service.list_profile(
            account_id,
            name=name,
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


    @responses.activate
    def test_list_profile_required_params(self):
        """
        test_list_profile_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/posture/v1/profiles')
        mock_response = '{"profiles": [{"name": "CIS IBM Foundations Benchmark 1.0.0", "no_of_goals": 58, "description": "CIS IBM Foundations Benchmark 1.0.0", "version": 1, "created_by": "IBMid-5500081P68", "modified_by": "IBMid-5500081P68", "reason_for_delete": "reason_for_delete", "applicability_criteria": {"environment": ["[IBM Cloud]"], "resource": ["[My_example_bucket]"], "environment_category": ["[Cloud]"], "resource_category": ["[Storage]"], "resource_type": ["Bucket"], "software_details": {"anyKey": "anyValue"}, "os_details": {"anyKey": "anyValue"}, "additional_details": {"anyKey": "anyValue"}, "environment_category_description": {"mapKey": "Cloud"}, "environment_description": {"mapKey": "IBM Cloud"}, "resource_category_description": {"mapKey": "Storage"}, "resource_type_description": {"mapKey": "Bucket"}, "resource_description": {"mapKey": "My_specific_bucket"}}, "profile_id": 3045, "base_profile": "CIS IBM Foundations Benchmark 1.0.0", "profile_type": "predefined", "created_time": "2021-02-26T04:07:25Z", "modified_time": "2021-02-26T04:07:25Z", "enabled": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.list_profile(
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
    def test_list_profile_value_error(self):
        """
        test_list_profile_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/posture/v1/profiles')
        mock_response = '{"profiles": [{"name": "CIS IBM Foundations Benchmark 1.0.0", "no_of_goals": 58, "description": "CIS IBM Foundations Benchmark 1.0.0", "version": 1, "created_by": "IBMid-5500081P68", "modified_by": "IBMid-5500081P68", "reason_for_delete": "reason_for_delete", "applicability_criteria": {"environment": ["[IBM Cloud]"], "resource": ["[My_example_bucket]"], "environment_category": ["[Cloud]"], "resource_category": ["[Storage]"], "resource_type": ["Bucket"], "software_details": {"anyKey": "anyValue"}, "os_details": {"anyKey": "anyValue"}, "additional_details": {"anyKey": "anyValue"}, "environment_category_description": {"mapKey": "Cloud"}, "environment_description": {"mapKey": "IBM Cloud"}, "resource_category_description": {"mapKey": "Storage"}, "resource_type_description": {"mapKey": "Bucket"}, "resource_description": {"mapKey": "My_specific_bucket"}}, "profile_id": 3045, "base_profile": "CIS IBM Foundations Benchmark 1.0.0", "profile_type": "predefined", "created_time": "2021-02-26T04:07:25Z", "modified_time": "2021-02-26T04:07:25Z", "enabled": true}]}'
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
                service.list_profile(**req_copy)



# endregion
##############################################################################
# End of Service: Profiles
##############################################################################

##############################################################################
# Start of Service: Scopes
##############################################################################
# region

class TestListScopes():
    """
    Test Class for list_scopes
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
    def test_list_scopes_all_params(self):
        """
        list_scopes()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/posture/v1/scopes')
        mock_response = '{"scopes": [{"description": "This scope targets all of the resources that are available in our IBM Cloud staging environment.", "created_by": "IBMid-5500081P68", "modified_by": "IBMid-5500081P68", "scope_id": 1, "name": "My_Example_Scope", "enabled": true, "environment_type": "ibm", "created_time": "2021-02-26T04:07:25Z", "modified_time": "2021-02-26T04:07:25Z", "last_scan_type": "fact_collection", "last_scan_type_description": "Fact collection", "last_scan_status_updated_time": "2021-02-26T04:07:25Z", "collectors_id": [13], "scans": [{"scan_id": 235, "discover_id": 49, "status": "validation_completed", "status_message": "The collector aborted the task during upgrade."}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'

        # Invoke method
        response = service.list_scopes(
            account_id,
            name=name,
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


    @responses.activate
    def test_list_scopes_required_params(self):
        """
        test_list_scopes_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/posture/v1/scopes')
        mock_response = '{"scopes": [{"description": "This scope targets all of the resources that are available in our IBM Cloud staging environment.", "created_by": "IBMid-5500081P68", "modified_by": "IBMid-5500081P68", "scope_id": 1, "name": "My_Example_Scope", "enabled": true, "environment_type": "ibm", "created_time": "2021-02-26T04:07:25Z", "modified_time": "2021-02-26T04:07:25Z", "last_scan_type": "fact_collection", "last_scan_type_description": "Fact collection", "last_scan_status_updated_time": "2021-02-26T04:07:25Z", "collectors_id": [13], "scans": [{"scan_id": 235, "discover_id": 49, "status": "validation_completed", "status_message": "The collector aborted the task during upgrade."}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.list_scopes(
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
    def test_list_scopes_value_error(self):
        """
        test_list_scopes_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/posture/v1/scopes')
        mock_response = '{"scopes": [{"description": "This scope targets all of the resources that are available in our IBM Cloud staging environment.", "created_by": "IBMid-5500081P68", "modified_by": "IBMid-5500081P68", "scope_id": 1, "name": "My_Example_Scope", "enabled": true, "environment_type": "ibm", "created_time": "2021-02-26T04:07:25Z", "modified_time": "2021-02-26T04:07:25Z", "last_scan_type": "fact_collection", "last_scan_type_description": "Fact collection", "last_scan_status_updated_time": "2021-02-26T04:07:25Z", "collectors_id": [13], "scans": [{"scan_id": 235, "discover_id": 49, "status": "validation_completed", "status_message": "The collector aborted the task during upgrade."}]}]}'
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
                service.list_scopes(**req_copy)



# endregion
##############################################################################
# End of Service: Scopes
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestApplicabilityCriteria():
    """
    Test Class for ApplicabilityCriteria
    """

    def test_applicability_criteria_serialization(self):
        """
        Test serialization/deserialization for ApplicabilityCriteria
        """

        # Construct a json representation of a ApplicabilityCriteria model
        applicability_criteria_model_json = {}
        applicability_criteria_model_json['environment'] = ['IBM Cloud']
        applicability_criteria_model_json['resource'] = ['My_example_bucket']
        applicability_criteria_model_json['environment_category'] = ['Cloud']
        applicability_criteria_model_json['resource_category'] = ['Storage']
        applicability_criteria_model_json['resource_type'] = ['Bucket']
        applicability_criteria_model_json['software_details'] = { 'foo': 'bar' }
        applicability_criteria_model_json['os_details'] = { 'foo': 'bar' }
        applicability_criteria_model_json['additional_details'] = { 'foo': 'bar' }
        applicability_criteria_model_json['environment_category_description'] = {}
        applicability_criteria_model_json['environment_description'] = {}
        applicability_criteria_model_json['resource_category_description'] = {}
        applicability_criteria_model_json['resource_type_description'] = {}
        applicability_criteria_model_json['resource_description'] = {}

        # Construct a model instance of ApplicabilityCriteria by calling from_dict on the json representation
        applicability_criteria_model = ApplicabilityCriteria.from_dict(applicability_criteria_model_json)
        assert applicability_criteria_model != False

        # Construct a model instance of ApplicabilityCriteria by calling from_dict on the json representation
        applicability_criteria_model_dict = ApplicabilityCriteria.from_dict(applicability_criteria_model_json).__dict__
        applicability_criteria_model2 = ApplicabilityCriteria(**applicability_criteria_model_dict)

        # Verify the model instances are equivalent
        assert applicability_criteria_model == applicability_criteria_model2

        # Convert model instance back to dict and verify no loss of data
        applicability_criteria_model_json2 = applicability_criteria_model.to_dict()
        assert applicability_criteria_model_json2 == applicability_criteria_model_json

class TestProfile():
    """
    Test Class for Profile
    """

    def test_profile_serialization(self):
        """
        Test serialization/deserialization for Profile
        """

        # Construct dict forms of any model objects needed in order to build this model.

        applicability_criteria_model = {} # ApplicabilityCriteria
        applicability_criteria_model['environment'] = ['IBM Cloud']
        applicability_criteria_model['resource'] = ['My_example_bucket']
        applicability_criteria_model['environment_category'] = ['Cloud']
        applicability_criteria_model['resource_category'] = ['Storage']
        applicability_criteria_model['resource_type'] = ['Bucket']
        applicability_criteria_model['software_details'] = { 'foo': 'bar' }
        applicability_criteria_model['os_details'] = { 'foo': 'bar' }
        applicability_criteria_model['additional_details'] = { 'foo': 'bar' }
        applicability_criteria_model['environment_category_description'] = {}
        applicability_criteria_model['environment_description'] = {}
        applicability_criteria_model['resource_category_description'] = {}
        applicability_criteria_model['resource_type_description'] = {}
        applicability_criteria_model['resource_description'] = {}

        # Construct a json representation of a Profile model
        profile_model_json = {}
        profile_model_json['name'] = 'CIS IBM Foundations Benchmark 1.0.0'
        profile_model_json['no_of_goals'] = 58
        profile_model_json['description'] = 'CIS IBM Foundations Benchmark 1.0.0'
        profile_model_json['version'] = 1
        profile_model_json['created_by'] = 'IBMid-5500081P68'
        profile_model_json['modified_by'] = 'IBMid-5500081P68'
        profile_model_json['reason_for_delete'] = 'testString'
        profile_model_json['applicability_criteria'] = applicability_criteria_model
        profile_model_json['profile_id'] = 3045
        profile_model_json['base_profile'] = 'CIS IBM Foundations Benchmark 1.0.0'
        profile_model_json['profile_type'] = 'predefined'
        profile_model_json['created_time'] = '2021-02-26T04:07:25Z'
        profile_model_json['modified_time'] = '2021-02-26T04:07:25Z'
        profile_model_json['enabled'] = True

        # Construct a model instance of Profile by calling from_dict on the json representation
        profile_model = Profile.from_dict(profile_model_json)
        assert profile_model != False

        # Construct a model instance of Profile by calling from_dict on the json representation
        profile_model_dict = Profile.from_dict(profile_model_json).__dict__
        profile_model2 = Profile(**profile_model_dict)

        # Verify the model instances are equivalent
        assert profile_model == profile_model2

        # Convert model instance back to dict and verify no loss of data
        profile_model_json2 = profile_model.to_dict()
        assert profile_model_json2 == profile_model_json

class TestProfilesList():
    """
    Test Class for ProfilesList
    """

    def test_profiles_list_serialization(self):
        """
        Test serialization/deserialization for ProfilesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        applicability_criteria_model = {} # ApplicabilityCriteria
        applicability_criteria_model['environment'] = ['IBM Cloud']
        applicability_criteria_model['resource'] = ['My_example_bucket']
        applicability_criteria_model['environment_category'] = ['Cloud']
        applicability_criteria_model['resource_category'] = ['Storage']
        applicability_criteria_model['resource_type'] = ['Bucket']
        applicability_criteria_model['software_details'] = { 'foo': 'bar' }
        applicability_criteria_model['os_details'] = { 'foo': 'bar' }
        applicability_criteria_model['additional_details'] = { 'foo': 'bar' }
        applicability_criteria_model['environment_category_description'] = {}
        applicability_criteria_model['environment_description'] = {}
        applicability_criteria_model['resource_category_description'] = {}
        applicability_criteria_model['resource_type_description'] = {}
        applicability_criteria_model['resource_description'] = {}

        profile_model = {} # Profile
        profile_model['name'] = 'CIS IBM Foundations Benchmark 1.0.0'
        profile_model['no_of_goals'] = 58
        profile_model['description'] = 'CIS IBM Foundations Benchmark 1.0.0'
        profile_model['version'] = 1
        profile_model['created_by'] = 'IBMid-5500081P68'
        profile_model['modified_by'] = 'IBMid-5500081P68'
        profile_model['reason_for_delete'] = 'testString'
        profile_model['applicability_criteria'] = applicability_criteria_model
        profile_model['profile_id'] = 3045
        profile_model['base_profile'] = 'CIS IBM Foundations Benchmark 1.0.0'
        profile_model['profile_type'] = 'predefined'
        profile_model['created_time'] = '2021-02-26T04:07:25Z'
        profile_model['modified_time'] = '2021-02-26T04:07:25Z'
        profile_model['enabled'] = True

        # Construct a json representation of a ProfilesList model
        profiles_list_model_json = {}
        profiles_list_model_json['profiles'] = [profile_model]

        # Construct a model instance of ProfilesList by calling from_dict on the json representation
        profiles_list_model = ProfilesList.from_dict(profiles_list_model_json)
        assert profiles_list_model != False

        # Construct a model instance of ProfilesList by calling from_dict on the json representation
        profiles_list_model_dict = ProfilesList.from_dict(profiles_list_model_json).__dict__
        profiles_list_model2 = ProfilesList(**profiles_list_model_dict)

        # Verify the model instances are equivalent
        assert profiles_list_model == profiles_list_model2

        # Convert model instance back to dict and verify no loss of data
        profiles_list_model_json2 = profiles_list_model.to_dict()
        assert profiles_list_model_json2 == profiles_list_model_json

class TestResult():
    """
    Test Class for Result
    """

    def test_result_serialization(self):
        """
        Test serialization/deserialization for Result
        """

        # Construct a json representation of a Result model
        result_model_json = {}
        result_model_json['result'] = True
        result_model_json['message'] = 'testString'

        # Construct a model instance of Result by calling from_dict on the json representation
        result_model = Result.from_dict(result_model_json)
        assert result_model != False

        # Construct a model instance of Result by calling from_dict on the json representation
        result_model_dict = Result.from_dict(result_model_json).__dict__
        result_model2 = Result(**result_model_dict)

        # Verify the model instances are equivalent
        assert result_model == result_model2

        # Convert model instance back to dict and verify no loss of data
        result_model_json2 = result_model.to_dict()
        assert result_model_json2 == result_model_json

class TestScan():
    """
    Test Class for Scan
    """

    def test_scan_serialization(self):
        """
        Test serialization/deserialization for Scan
        """

        # Construct a json representation of a Scan model
        scan_model_json = {}
        scan_model_json['scan_id'] = 235
        scan_model_json['discover_id'] = 49
        scan_model_json['status'] = 'validation_completed'
        scan_model_json['status_message'] = 'The collector aborted the task during upgrade.'

        # Construct a model instance of Scan by calling from_dict on the json representation
        scan_model = Scan.from_dict(scan_model_json)
        assert scan_model != False

        # Construct a model instance of Scan by calling from_dict on the json representation
        scan_model_dict = Scan.from_dict(scan_model_json).__dict__
        scan_model2 = Scan(**scan_model_dict)

        # Verify the model instances are equivalent
        assert scan_model == scan_model2

        # Convert model instance back to dict and verify no loss of data
        scan_model_json2 = scan_model.to_dict()
        assert scan_model_json2 == scan_model_json

class TestScope():
    """
    Test Class for Scope
    """

    def test_scope_serialization(self):
        """
        Test serialization/deserialization for Scope
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scan_model = {} # Scan
        scan_model['scan_id'] = 235
        scan_model['discover_id'] = 49
        scan_model['status'] = 'validation_completed'
        scan_model['status_message'] = 'The collector aborted the task during upgrade.'

        # Construct a json representation of a Scope model
        scope_model_json = {}
        scope_model_json['description'] = 'This scope targets all of the resources that are available in our IBM Cloud staging environment.'
        scope_model_json['created_by'] = 'IBMid-5500081P68'
        scope_model_json['modified_by'] = 'IBMid-5500081P68'
        scope_model_json['scope_id'] = 1
        scope_model_json['name'] = 'My_Example_Scope'
        scope_model_json['enabled'] = True
        scope_model_json['environment_type'] = 'ibm'
        scope_model_json['created_time'] = '2021-02-26T04:07:25Z'
        scope_model_json['modified_time'] = '2021-02-26T04:07:25Z'
        scope_model_json['last_scan_type'] = 'fact_collection'
        scope_model_json['last_scan_type_description'] = 'Fact collection'
        scope_model_json['last_scan_status_updated_time'] = '2021-02-26T04:07:25Z'
        scope_model_json['collectors_id'] = [2, 1]
        scope_model_json['scans'] = [scan_model]

        # Construct a model instance of Scope by calling from_dict on the json representation
        scope_model = Scope.from_dict(scope_model_json)
        assert scope_model != False

        # Construct a model instance of Scope by calling from_dict on the json representation
        scope_model_dict = Scope.from_dict(scope_model_json).__dict__
        scope_model2 = Scope(**scope_model_dict)

        # Verify the model instances are equivalent
        assert scope_model == scope_model2

        # Convert model instance back to dict and verify no loss of data
        scope_model_json2 = scope_model.to_dict()
        assert scope_model_json2 == scope_model_json

class TestScopesList():
    """
    Test Class for ScopesList
    """

    def test_scopes_list_serialization(self):
        """
        Test serialization/deserialization for ScopesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scan_model = {} # Scan
        scan_model['scan_id'] = 235
        scan_model['discover_id'] = 49
        scan_model['status'] = 'validation_completed'
        scan_model['status_message'] = 'The collector aborted the task during upgrade.'

        scope_model = {} # Scope
        scope_model['description'] = 'This scope targets all of the resources that are available in our IBM Cloud staging environment.'
        scope_model['created_by'] = 'IBMid-5500081P68'
        scope_model['modified_by'] = 'IBMid-5500081P68'
        scope_model['scope_id'] = 1
        scope_model['name'] = 'My_Example_Scope'
        scope_model['enabled'] = True
        scope_model['environment_type'] = 'ibm'
        scope_model['created_time'] = '2021-02-26T04:07:25Z'
        scope_model['modified_time'] = '2021-02-26T04:07:25Z'
        scope_model['last_scan_type'] = 'fact_collection'
        scope_model['last_scan_type_description'] = 'Fact collection'
        scope_model['last_scan_status_updated_time'] = '2021-02-26T04:07:25Z'
        scope_model['collectors_id'] = [2, 1]
        scope_model['scans'] = [scan_model]

        # Construct a json representation of a ScopesList model
        scopes_list_model_json = {}
        scopes_list_model_json['scopes'] = [scope_model]

        # Construct a model instance of ScopesList by calling from_dict on the json representation
        scopes_list_model = ScopesList.from_dict(scopes_list_model_json)
        assert scopes_list_model != False

        # Construct a model instance of ScopesList by calling from_dict on the json representation
        scopes_list_model_dict = ScopesList.from_dict(scopes_list_model_json).__dict__
        scopes_list_model2 = ScopesList(**scopes_list_model_dict)

        # Verify the model instances are equivalent
        assert scopes_list_model == scopes_list_model2

        # Convert model instance back to dict and verify no loss of data
        scopes_list_model_json2 = scopes_list_model.to_dict()
        assert scopes_list_model_json2 == scopes_list_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
