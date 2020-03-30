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
from platform_services.resource_manager_v2 import *


service = ResourceManagerV2(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://resource-controller.test.cloud.ibm.com/v2'
service.set_service_url(base_url)

##############################################################################
# Start of Service: AccountQuotas
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_account_quota_list
#-----------------------------------------------------------------------------
class TestGetAccountQuotaList():

    #--------------------------------------------------------
    # get_account_quota_list()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_quota_list_all_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/accounts/testString'
        mock_response = '{"id": "id", "name": "name", "type": "type", "number_of_apps": 14, "number_of_service_instances": 27, "default_number_of_instances_per_lite_plan": 41, "instances_per_app": 17, "instance_memory": "instance_memory", "total_app_memory": "total_app_memory", "vsi_limit": 9, "resource_quotas": {"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}, "created_at": "created_at", "updated_at": "updated_at"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.get_account_quota_list(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_account_quota_list_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_quota_list_required_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/accounts/testString'
        mock_response = '{"id": "id", "name": "name", "type": "type", "number_of_apps": 14, "number_of_service_instances": 27, "default_number_of_instances_per_lite_plan": 41, "instances_per_app": 17, "instance_memory": "instance_memory", "total_app_memory": "total_app_memory", "vsi_limit": 9, "resource_quotas": {"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}, "created_at": "created_at", "updated_at": "updated_at"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.get_account_quota_list(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_resource_quota
#-----------------------------------------------------------------------------
class TestGetResourceQuota():

    #--------------------------------------------------------
    # get_resource_quota()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_quota_all_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/accounts/testString/resource_types/testString'
        mock_response = '{"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_type = 'testString'

        # Invoke method
        response = service.get_resource_quota(
            account_id,
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_quota_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_quota_required_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/accounts/testString/resource_types/testString'
        mock_response = '{"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_type = 'testString'

        # Invoke method
        response = service.get_resource_quota(
            account_id,
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_resource_quota
#-----------------------------------------------------------------------------
class TestUpdateResourceQuota():

    #--------------------------------------------------------
    # update_resource_quota()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_quota_all_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/accounts/testString/resource_types/testString'
        mock_response = '{"error_code": "RG-CloudResourceGroupErrorResponse", "message": "message", "status_code": "status_code", "transaction_id": "transaction_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_type = 'testString'

        # Invoke method
        response = service.update_resource_quota(
            account_id,
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_resource_quota_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_quota_required_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/accounts/testString/resource_types/testString'
        mock_response = '{"error_code": "RG-CloudResourceGroupErrorResponse", "message": "message", "status_code": "status_code", "transaction_id": "transaction_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_type = 'testString'

        # Invoke method
        response = service.update_resource_quota(
            account_id,
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_resource_quota
#-----------------------------------------------------------------------------
class TestDeleteResourceQuota():

    #--------------------------------------------------------
    # delete_resource_quota()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_quota_all_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/accounts/testString/resource_types/testString'
        mock_response = '{"error_code": "RG-CloudResourceGroupErrorResponse", "message": "message", "status_code": "status_code", "transaction_id": "transaction_id"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_type = 'testString'

        # Invoke method
        response = service.delete_resource_quota(
            account_id,
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_resource_quota_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_quota_required_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/accounts/testString/resource_types/testString'
        mock_response = '{"error_code": "RG-CloudResourceGroupErrorResponse", "message": "message", "status_code": "status_code", "transaction_id": "transaction_id"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_type = 'testString'

        # Invoke method
        response = service.delete_resource_quota(
            account_id,
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_default_resource_quota
#-----------------------------------------------------------------------------
class TestCreateDefaultResourceQuota():

    #--------------------------------------------------------
    # create_default_resource_quota()
    #--------------------------------------------------------
    @responses.activate
    def test_create_default_resource_quota_all_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/resource_types/testString'
        mock_response = '{"error_code": "RG-CloudResourceGroupErrorResponse", "message": "message", "status_code": "status_code", "transaction_id": "transaction_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_type = 'testString'

        # Invoke method
        response = service.create_default_resource_quota(
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_default_resource_quota_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_default_resource_quota_required_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/resource_types/testString'
        mock_response = '{"error_code": "RG-CloudResourceGroupErrorResponse", "message": "message", "status_code": "status_code", "transaction_id": "transaction_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_type = 'testString'

        # Invoke method
        response = service.create_default_resource_quota(
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_schema
#-----------------------------------------------------------------------------
class TestCreateSchema():

    #--------------------------------------------------------
    # create_schema()
    #--------------------------------------------------------
    @responses.activate
    def test_create_schema_all_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/resource_types/testString/schemas'
        mock_response = '{"error_code": "RG-CloudResourceGroupErrorResponse", "message": "message", "status_code": "status_code", "transaction_id": "transaction_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_type = 'testString'

        # Invoke method
        response = service.create_schema(
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_schema_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_schema_required_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/resource_types/testString/schemas'
        mock_response = '{"error_code": "RG-CloudResourceGroupErrorResponse", "message": "message", "status_code": "status_code", "transaction_id": "transaction_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_type = 'testString'

        # Invoke method
        response = service.create_schema(
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_schema
#-----------------------------------------------------------------------------
class TestGetSchema():

    #--------------------------------------------------------
    # get_schema()
    #--------------------------------------------------------
    @responses.activate
    def test_get_schema_all_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/resource_types/testString/schemas'
        mock_response = '{"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_type = 'testString'

        # Invoke method
        response = service.get_schema(
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_schema_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_schema_required_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/resource_types/testString/schemas'
        mock_response = '{"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_type = 'testString'

        # Invoke method
        response = service.get_schema(
            resource_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: AccountQuotas
##############################################################################

##############################################################################
# Start of Service: QuotaDefinition
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_quota_definitions
#-----------------------------------------------------------------------------
class TestListQuotaDefinitions():

    #--------------------------------------------------------
    # list_quota_definitions()
    #--------------------------------------------------------
    @responses.activate
    def test_list_quota_definitions_all_params(self):
        # Set up mock
        url = base_url + '/quota_definitions'
        mock_response = '{"resources": [{"id": "id", "name": "name", "type": "type", "number_of_apps": 14, "number_of_service_instances": 27, "default_number_of_instances_per_lite_plan": 41, "instances_per_app": 17, "instance_memory": "instance_memory", "total_app_memory": "total_app_memory", "vsi_limit": 9, "resource_quotas": {"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}, "created_at": "created_at", "updated_at": "updated_at"}]}'
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


    #--------------------------------------------------------
    # test_list_quota_definitions_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_quota_definitions_required_params(self):
        # Set up mock
        url = base_url + '/quota_definitions'
        mock_response = '{"resources": [{"id": "id", "name": "name", "type": "type", "number_of_apps": 14, "number_of_service_instances": 27, "default_number_of_instances_per_lite_plan": 41, "instances_per_app": 17, "instance_memory": "instance_memory", "total_app_memory": "total_app_memory", "vsi_limit": 9, "resource_quotas": {"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}, "created_at": "created_at", "updated_at": "updated_at"}]}'
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


#-----------------------------------------------------------------------------
# Test Class for get_quota_definition
#-----------------------------------------------------------------------------
class TestGetQuotaDefinition():

    #--------------------------------------------------------
    # get_quota_definition()
    #--------------------------------------------------------
    @responses.activate
    def test_get_quota_definition_all_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/testString'
        mock_response = '{"id": "id", "name": "name", "type": "type", "number_of_apps": 14, "number_of_service_instances": 27, "default_number_of_instances_per_lite_plan": 41, "instances_per_app": 17, "instance_memory": "instance_memory", "total_app_memory": "total_app_memory", "vsi_limit": 9, "resource_quotas": {"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}, "created_at": "created_at", "updated_at": "updated_at"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_quota_definition(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_quota_definition_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_quota_definition_required_params(self):
        # Set up mock
        url = base_url + '/quota_definitions/testString'
        mock_response = '{"id": "id", "name": "name", "type": "type", "number_of_apps": 14, "number_of_service_instances": 27, "default_number_of_instances_per_lite_plan": 41, "instances_per_app": 17, "instance_memory": "instance_memory", "total_app_memory": "total_app_memory", "vsi_limit": 9, "resource_quotas": {"_id": "id", "resource_id": "resource_id", "crn": "crn", "limit": 5}, "created_at": "created_at", "updated_at": "updated_at"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_quota_definition(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: QuotaDefinition
##############################################################################

##############################################################################
# Start of Service: ResourceGroup
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_resource_groups
#-----------------------------------------------------------------------------
class TestListResourceGroups():

    #--------------------------------------------------------
    # list_resource_groups()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_groups_all_params(self):
        # Set up mock
        url = base_url + '/resource_groups'
        mock_response = '{"resources": [{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "created_at", "updated_at": "updated_at"}]}'
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
            date=date
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'date={}'.format(date) in query_string


    #--------------------------------------------------------
    # test_list_resource_groups_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_groups_required_params(self):
        # Set up mock
        url = base_url + '/resource_groups'
        mock_response = '{"resources": [{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "created_at", "updated_at": "updated_at"}]}'
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


#-----------------------------------------------------------------------------
# Test Class for create_resource_group
#-----------------------------------------------------------------------------
class TestCreateResourceGroup():

    #--------------------------------------------------------
    # create_resource_group()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_group_all_params(self):
        # Set up mock
        url = base_url + '/resource_groups'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['account_id'] == account_id


    #--------------------------------------------------------
    # test_create_resource_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_group_required_params(self):
        # Set up mock
        url = base_url + '/resource_groups'
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


#-----------------------------------------------------------------------------
# Test Class for get_resource_group
#-----------------------------------------------------------------------------
class TestGetResourceGroup():

    #--------------------------------------------------------
    # get_resource_group()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_group_all_params(self):
        # Set up mock
        url = base_url + '/resource_groups/testString'
        mock_response = '{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "created_at", "updated_at": "updated_at"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_group(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_group_required_params(self):
        # Set up mock
        url = base_url + '/resource_groups/testString'
        mock_response = '{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "created_at", "updated_at": "updated_at"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_resource_group(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_resource_group
#-----------------------------------------------------------------------------
class TestUpdateResourceGroup():

    #--------------------------------------------------------
    # update_resource_group()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_group_all_params(self):
        # Set up mock
        url = base_url + '/resource_groups/testString'
        mock_response = '{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "created_at", "updated_at": "updated_at"}'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['state'] == state


    #--------------------------------------------------------
    # test_update_resource_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_resource_group_required_params(self):
        # Set up mock
        url = base_url + '/resource_groups/testString'
        mock_response = '{"id": "id", "crn": "crn", "account_id": "account_id", "name": "name", "state": "state", "default": false, "quota_id": "quota_id", "quota_url": "quota_url", "payment_methods_url": "payment_methods_url", "resource_linkages": [{"anyKey": "anyValue"}], "teams_url": "teams_url", "created_at": "created_at", "updated_at": "updated_at"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.update_resource_group(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_resource_group
#-----------------------------------------------------------------------------
class TestDeleteResourceGroup():

    #--------------------------------------------------------
    # delete_resource_group()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_group_all_params(self):
        # Set up mock
        url = base_url + '/resource_groups/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_group(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_resource_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_resource_group_required_params(self):
        # Set up mock
        url = base_url + '/resource_groups/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_resource_group(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


# endregion
##############################################################################
# End of Service: ResourceGroup
##############################################################################

