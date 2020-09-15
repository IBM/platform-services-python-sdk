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
Unit Tests for ResourceManagerV2
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
from ibm_platform_services.resource_manager_v2 import *


service = ResourceManagerV2(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://resource-controller.cloud.ibm.com/v2'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ResourceGroup
##############################################################################
# region

class TestListResourceGroups():
    """
    Test Class for list_resource_groups
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
    def test_list_resource_groups_all_params(self):
        """
        list_resource_groups()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups')
        mock_response = '{"resources": [{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        date = 'testString'

        # Invoke method
        response = service.list_resource_groups(
            account_id=account_id,
            date=date,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'date={}'.format(date) in query_string


    @responses.activate
    def test_list_resource_groups_required_params(self):
        """
        test_list_resource_groups_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups')
        mock_response = '{"resources": [{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_resource_groups()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateResourceGroup():
    """
    Test Class for create_resource_group
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
    def test_create_resource_group_all_params(self):
        """
        create_resource_group()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups')
        mock_response = '{"id": "id", "crn": "crn"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'test1'
        account_id = '25eba2a9-beef-450b-82cf-f5ad5e36c6dd'

        # Invoke method
        response = service.create_resource_group(
            name=name,
            account_id=account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'test1'
        assert req_body['account_id'] == '25eba2a9-beef-450b-82cf-f5ad5e36c6dd'


    @responses.activate
    def test_create_resource_group_required_params(self):
        """
        test_create_resource_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups')
        mock_response = '{"id": "id", "crn": "crn"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Invoke method
        response = service.create_resource_group()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


class TestGetResourceGroup():
    """
    Test Class for get_resource_group
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
    def test_get_resource_group_all_params(self):
        """
        get_resource_group()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups/testString')
        mock_response = '{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_group(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_resource_group_value_error(self):
        """
        test_get_resource_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups/testString')
        mock_response = '{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}'
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
                service.get_resource_group(**req_copy)



class TestUpdateResourceGroup():
    """
    Test Class for update_resource_group
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
    def test_update_resource_group_all_params(self):
        """
        update_resource_group()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups/testString')
        mock_response = '{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        state = 'testString'

        # Invoke method
        response = service.update_resource_group(
            id,
            name=name,
            state=state,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['state'] == 'testString'


    @responses.activate
    def test_update_resource_group_required_params(self):
        """
        test_update_resource_group_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups/testString')
        mock_response = '{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.update_resource_group(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_resource_group_value_error(self):
        """
        test_update_resource_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups/testString')
        mock_response = '{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PATCH,
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
                service.update_resource_group(**req_copy)



class TestDeleteResourceGroup():
    """
    Test Class for delete_resource_group
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
    def test_delete_resource_group_all_params(self):
        """
        delete_resource_group()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_group(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_resource_group_value_error(self):
        """
        test_delete_resource_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/resource_groups/testString')
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
                service.delete_resource_group(**req_copy)



# endregion
##############################################################################
# End of Service: ResourceGroup
##############################################################################

##############################################################################
# Start of Service: QuotaDefinition
##############################################################################
# region

class TestListQuotaDefinitions():
    """
    Test Class for list_quota_definitions
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
    def test_list_quota_definitions_all_params(self):
        """
        list_quota_definitions()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/quota_definitions')
        mock_response = '{"resources": [{"id": "id", "name": "name", "type": "type", "number_of_apps": 14, "number_of_service_instances": 27, "default_number_of_instances_per_lite_plan": 41, "instances_per_app": 17, "instance_memory": "instance_memory", "total_app_memory": "total_app_memory", "vsi_limit": 9, "resource_quotas": [{"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}], "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_quota_definitions()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetQuotaDefinition():
    """
    Test Class for get_quota_definition
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
    def test_get_quota_definition_all_params(self):
        """
        get_quota_definition()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/quota_definitions/testString')
        mock_response = '{"id": "id", "name": "name", "type": "type", "number_of_apps": 14, "number_of_service_instances": 27, "default_number_of_instances_per_lite_plan": 41, "instances_per_app": 17, "instance_memory": "instance_memory", "total_app_memory": "total_app_memory", "vsi_limit": 9, "resource_quotas": [{"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}], "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_quota_definition(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_quota_definition_value_error(self):
        """
        test_get_quota_definition_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/quota_definitions/testString')
        mock_response = '{"id": "id", "name": "name", "type": "type", "number_of_apps": 14, "number_of_service_instances": 27, "default_number_of_instances_per_lite_plan": 41, "instances_per_app": 17, "instance_memory": "instance_memory", "total_app_memory": "total_app_memory", "vsi_limit": 9, "resource_quotas": [{"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}], "created_at": "2019-01-01T12:00:00", "updated_at": "2019-01-01T12:00:00"}'
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
                service.get_quota_definition(**req_copy)



# endregion
##############################################################################
# End of Service: QuotaDefinition
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestQuotaDefinition():
    """
    Test Class for QuotaDefinition
    """

    def test_quota_definition_serialization(self):
        """
        Test serialization/deserialization for QuotaDefinition
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_quota_model = {} # ResourceQuota
        resource_quota_model['_id'] = 'testString'
        resource_quota_model['resource_id'] = 'testString'
        resource_quota_model['crn'] = 'testString'
        resource_quota_model['limit'] = 72.5

        # Construct a json representation of a QuotaDefinition model
        quota_definition_model_json = {}
        quota_definition_model_json['id'] = 'testString'
        quota_definition_model_json['name'] = 'testString'
        quota_definition_model_json['type'] = 'testString'
        quota_definition_model_json['number_of_apps'] = 72.5
        quota_definition_model_json['number_of_service_instances'] = 72.5
        quota_definition_model_json['default_number_of_instances_per_lite_plan'] = 72.5
        quota_definition_model_json['instances_per_app'] = 72.5
        quota_definition_model_json['instance_memory'] = 'testString'
        quota_definition_model_json['total_app_memory'] = 'testString'
        quota_definition_model_json['vsi_limit'] = 72.5
        quota_definition_model_json['resource_quotas'] = [resource_quota_model]
        quota_definition_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        quota_definition_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of QuotaDefinition by calling from_dict on the json representation
        quota_definition_model = QuotaDefinition.from_dict(quota_definition_model_json)
        assert quota_definition_model != False

        # Construct a model instance of QuotaDefinition by calling from_dict on the json representation
        quota_definition_model_dict = QuotaDefinition.from_dict(quota_definition_model_json).__dict__
        quota_definition_model2 = QuotaDefinition(**quota_definition_model_dict)

        # Verify the model instances are equivalent
        assert quota_definition_model == quota_definition_model2

        # Convert model instance back to dict and verify no loss of data
        quota_definition_model_json2 = quota_definition_model.to_dict()
        assert quota_definition_model_json2 == quota_definition_model_json

class TestQuotaDefinitionList():
    """
    Test Class for QuotaDefinitionList
    """

    def test_quota_definition_list_serialization(self):
        """
        Test serialization/deserialization for QuotaDefinitionList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_quota_model = {} # ResourceQuota
        resource_quota_model['_id'] = 'testString'
        resource_quota_model['resource_id'] = 'testString'
        resource_quota_model['crn'] = 'testString'
        resource_quota_model['limit'] = 72.5

        quota_definition_model = {} # QuotaDefinition
        quota_definition_model['id'] = 'testString'
        quota_definition_model['name'] = 'testString'
        quota_definition_model['type'] = 'testString'
        quota_definition_model['number_of_apps'] = 72.5
        quota_definition_model['number_of_service_instances'] = 72.5
        quota_definition_model['default_number_of_instances_per_lite_plan'] = 72.5
        quota_definition_model['instances_per_app'] = 72.5
        quota_definition_model['instance_memory'] = 'testString'
        quota_definition_model['total_app_memory'] = 'testString'
        quota_definition_model['vsi_limit'] = 72.5
        quota_definition_model['resource_quotas'] = [resource_quota_model]
        quota_definition_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        quota_definition_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a QuotaDefinitionList model
        quota_definition_list_model_json = {}
        quota_definition_list_model_json['resources'] = [quota_definition_model]

        # Construct a model instance of QuotaDefinitionList by calling from_dict on the json representation
        quota_definition_list_model = QuotaDefinitionList.from_dict(quota_definition_list_model_json)
        assert quota_definition_list_model != False

        # Construct a model instance of QuotaDefinitionList by calling from_dict on the json representation
        quota_definition_list_model_dict = QuotaDefinitionList.from_dict(quota_definition_list_model_json).__dict__
        quota_definition_list_model2 = QuotaDefinitionList(**quota_definition_list_model_dict)

        # Verify the model instances are equivalent
        assert quota_definition_list_model == quota_definition_list_model2

        # Convert model instance back to dict and verify no loss of data
        quota_definition_list_model_json2 = quota_definition_list_model.to_dict()
        assert quota_definition_list_model_json2 == quota_definition_list_model_json

class TestResCreateResourceGroup():
    """
    Test Class for ResCreateResourceGroup
    """

    def test_res_create_resource_group_serialization(self):
        """
        Test serialization/deserialization for ResCreateResourceGroup
        """

        # Construct a json representation of a ResCreateResourceGroup model
        res_create_resource_group_model_json = {}
        res_create_resource_group_model_json['id'] = 'testString'
        res_create_resource_group_model_json['crn'] = 'testString'

        # Construct a model instance of ResCreateResourceGroup by calling from_dict on the json representation
        res_create_resource_group_model = ResCreateResourceGroup.from_dict(res_create_resource_group_model_json)
        assert res_create_resource_group_model != False

        # Construct a model instance of ResCreateResourceGroup by calling from_dict on the json representation
        res_create_resource_group_model_dict = ResCreateResourceGroup.from_dict(res_create_resource_group_model_json).__dict__
        res_create_resource_group_model2 = ResCreateResourceGroup(**res_create_resource_group_model_dict)

        # Verify the model instances are equivalent
        assert res_create_resource_group_model == res_create_resource_group_model2

        # Convert model instance back to dict and verify no loss of data
        res_create_resource_group_model_json2 = res_create_resource_group_model.to_dict()
        assert res_create_resource_group_model_json2 == res_create_resource_group_model_json

class TestResourceGroup():
    """
    Test Class for ResourceGroup
    """

    def test_resource_group_serialization(self):
        """
        Test serialization/deserialization for ResourceGroup
        """

        # Construct a json representation of a ResourceGroup model
        resource_group_model_json = {}
        resource_group_model_json['id'] = 'testString'
        resource_group_model_json['crn'] = 'testString'
        resource_group_model_json['account_id'] = 'testString'
        resource_group_model_json['name'] = 'testString'
        resource_group_model_json['state'] = 'testString'
        resource_group_model_json['default'] = True
        resource_group_model_json['quota_id'] = 'testString'
        resource_group_model_json['quota_url'] = 'testString'
        resource_group_model_json['payment_methods_url'] = 'testString'
        resource_group_model_json['resource_linkages'] = [{ 'foo': 'bar' }]
        resource_group_model_json['teams_url'] = 'testString'
        resource_group_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        resource_group_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of ResourceGroup by calling from_dict on the json representation
        resource_group_model = ResourceGroup.from_dict(resource_group_model_json)
        assert resource_group_model != False

        # Construct a model instance of ResourceGroup by calling from_dict on the json representation
        resource_group_model_dict = ResourceGroup.from_dict(resource_group_model_json).__dict__
        resource_group_model2 = ResourceGroup(**resource_group_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_model == resource_group_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_model_json2 = resource_group_model.to_dict()
        assert resource_group_model_json2 == resource_group_model_json

class TestResourceGroupList():
    """
    Test Class for ResourceGroupList
    """

    def test_resource_group_list_serialization(self):
        """
        Test serialization/deserialization for ResourceGroupList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_group_model = {} # ResourceGroup
        resource_group_model['id'] = 'testString'
        resource_group_model['crn'] = 'testString'
        resource_group_model['account_id'] = 'testString'
        resource_group_model['name'] = 'testString'
        resource_group_model['state'] = 'testString'
        resource_group_model['default'] = True
        resource_group_model['quota_id'] = 'testString'
        resource_group_model['quota_url'] = 'testString'
        resource_group_model['payment_methods_url'] = 'testString'
        resource_group_model['resource_linkages'] = [{ 'foo': 'bar' }]
        resource_group_model['teams_url'] = 'testString'
        resource_group_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        resource_group_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ResourceGroupList model
        resource_group_list_model_json = {}
        resource_group_list_model_json['resources'] = [resource_group_model]

        # Construct a model instance of ResourceGroupList by calling from_dict on the json representation
        resource_group_list_model = ResourceGroupList.from_dict(resource_group_list_model_json)
        assert resource_group_list_model != False

        # Construct a model instance of ResourceGroupList by calling from_dict on the json representation
        resource_group_list_model_dict = ResourceGroupList.from_dict(resource_group_list_model_json).__dict__
        resource_group_list_model2 = ResourceGroupList(**resource_group_list_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_list_model == resource_group_list_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_list_model_json2 = resource_group_list_model.to_dict()
        assert resource_group_list_model_json2 == resource_group_list_model_json

class TestResourceQuota():
    """
    Test Class for ResourceQuota
    """

    def test_resource_quota_serialization(self):
        """
        Test serialization/deserialization for ResourceQuota
        """

        # Construct a json representation of a ResourceQuota model
        resource_quota_model_json = {}
        resource_quota_model_json['_id'] = 'testString'
        resource_quota_model_json['resource_id'] = 'testString'
        resource_quota_model_json['crn'] = 'testString'
        resource_quota_model_json['limit'] = 72.5

        # Construct a model instance of ResourceQuota by calling from_dict on the json representation
        resource_quota_model = ResourceQuota.from_dict(resource_quota_model_json)
        assert resource_quota_model != False

        # Construct a model instance of ResourceQuota by calling from_dict on the json representation
        resource_quota_model_dict = ResourceQuota.from_dict(resource_quota_model_json).__dict__
        resource_quota_model2 = ResourceQuota(**resource_quota_model_dict)

        # Verify the model instances are equivalent
        assert resource_quota_model == resource_quota_model2

        # Convert model instance back to dict and verify no loss of data
        resource_quota_model_json2 = resource_quota_model.to_dict()
        assert resource_quota_model_json2 == resource_quota_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
