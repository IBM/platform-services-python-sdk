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
from ibm_platform_services.enterprise_management_v1 import *


service = EnterpriseManagementV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://enterprise.cloud.ibm.com/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: AccountGroupOperations
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_account_group
#-----------------------------------------------------------------------------
class TestCreateAccountGroup():

    #--------------------------------------------------------
    # create_account_group()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_group_all_params(self):
        # Set up mock
        url = base_url + '/account-groups'
        mock_response = '{"account_group_id": "account_group_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        parent = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'

        # Invoke method
        response = service.create_account_group(
            parent,
            name,
            primary_contact_iam_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['primary_contact_iam_id'] == 'testString'


    #--------------------------------------------------------
    # test_create_account_group_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_group_value_error(self):
        # Set up mock
        url = base_url + '/account-groups'
        mock_response = '{"account_group_id": "account_group_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        parent = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "parent": parent,
            "name": name,
            "primary_contact_iam_id": primary_contact_iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_account_group(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_account_groups
#-----------------------------------------------------------------------------
class TestListAccountGroups():

    #--------------------------------------------------------
    # list_account_groups()
    #--------------------------------------------------------
    @responses.activate
    def test_list_account_groups_all_params(self):
        # Set up mock
        url = base_url + '/account-groups'
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'
        parent_account_group_id = 'testString'
        parent = 'testString'
        limit = 38

        # Invoke method
        response = service.list_account_groups(
            enterprise_id=enterprise_id,
            parent_account_group_id=parent_account_group_id,
            parent=parent,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'enterprise_id={}'.format(enterprise_id) in query_string
        assert 'parent_account_group_id={}'.format(parent_account_group_id) in query_string
        assert 'parent={}'.format(parent) in query_string
        assert 'limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_list_account_groups_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_account_groups_required_params(self):
        # Set up mock
        url = base_url + '/account-groups'
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_account_groups()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_account_group
#-----------------------------------------------------------------------------
class TestGetAccountGroup():

    #--------------------------------------------------------
    # get_account_group()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_group_all_params(self):
        # Set up mock
        url = base_url + '/account-groups/testString'
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_group_id = 'testString'

        # Invoke method
        response = service.get_account_group(
            account_group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_account_group_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_group_value_error(self):
        # Set up mock
        url = base_url + '/account-groups/testString'
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_group_id": account_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_account_group(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_account_group
#-----------------------------------------------------------------------------
class TestUpdateAccountGroup():

    #--------------------------------------------------------
    # update_account_group()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_group_all_params(self):
        # Set up mock
        url = base_url + '/account-groups/testString'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        account_group_id = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'

        # Invoke method
        response = service.update_account_group(
            account_group_id,
            name=name,
            primary_contact_iam_id=primary_contact_iam_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['primary_contact_iam_id'] == 'testString'


    #--------------------------------------------------------
    # test_update_account_group_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_group_value_error(self):
        # Set up mock
        url = base_url + '/account-groups/testString'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        account_group_id = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_group_id": account_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_account_group(**req_copy)



# endregion
##############################################################################
# End of Service: AccountGroupOperations
##############################################################################

##############################################################################
# Start of Service: AccountOperations
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for import_account_to_enterprise
#-----------------------------------------------------------------------------
class TestImportAccountToEnterprise():

    #--------------------------------------------------------
    # import_account_to_enterprise()
    #--------------------------------------------------------
    @responses.activate
    def test_import_account_to_enterprise_all_params(self):
        # Set up mock
        url = base_url + '/enterprises/testString/import/accounts/testString'
        responses.add(responses.PUT,
                      url,
                      status=202)

        # Set up parameter values
        enterprise_id = 'testString'
        account_id = 'testString'
        parent = 'testString'
        billing_unit_id = 'testString'

        # Invoke method
        response = service.import_account_to_enterprise(
            enterprise_id,
            account_id,
            parent=parent,
            billing_unit_id=billing_unit_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == 'testString'
        assert req_body['billing_unit_id'] == 'testString'


    #--------------------------------------------------------
    # test_import_account_to_enterprise_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_import_account_to_enterprise_required_params(self):
        # Set up mock
        url = base_url + '/enterprises/testString/import/accounts/testString'
        responses.add(responses.PUT,
                      url,
                      status=202)

        # Set up parameter values
        enterprise_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = service.import_account_to_enterprise(
            enterprise_id,
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_import_account_to_enterprise_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_import_account_to_enterprise_value_error(self):
        # Set up mock
        url = base_url + '/enterprises/testString/import/accounts/testString'
        responses.add(responses.PUT,
                      url,
                      status=202)

        # Set up parameter values
        enterprise_id = 'testString'
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "enterprise_id": enterprise_id,
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.import_account_to_enterprise(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_account
#-----------------------------------------------------------------------------
class TestCreateAccount():

    #--------------------------------------------------------
    # create_account()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_all_params(self):
        # Set up mock
        url = base_url + '/accounts'
        mock_response = '{"account_id": "account_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        parent = 'testString'
        name = 'testString'
        owner_iam_id = 'testString'

        # Invoke method
        response = service.create_account(
            parent,
            name,
            owner_iam_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['owner_iam_id'] == 'testString'


    #--------------------------------------------------------
    # test_create_account_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_value_error(self):
        # Set up mock
        url = base_url + '/accounts'
        mock_response = '{"account_id": "account_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        parent = 'testString'
        name = 'testString'
        owner_iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "parent": parent,
            "name": name,
            "owner_iam_id": owner_iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_account(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_accounts
#-----------------------------------------------------------------------------
class TestListAccounts():

    #--------------------------------------------------------
    # list_accounts()
    #--------------------------------------------------------
    @responses.activate
    def test_list_accounts_all_params(self):
        # Set up mock
        url = base_url + '/accounts'
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'
        account_group_id = 'testString'
        parent = 'testString'
        limit = 38

        # Invoke method
        response = service.list_accounts(
            enterprise_id=enterprise_id,
            account_group_id=account_group_id,
            parent=parent,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'enterprise_id={}'.format(enterprise_id) in query_string
        assert 'account_group_id={}'.format(account_group_id) in query_string
        assert 'parent={}'.format(parent) in query_string
        assert 'limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_list_accounts_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_accounts_required_params(self):
        # Set up mock
        url = base_url + '/accounts'
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_accounts()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_account
#-----------------------------------------------------------------------------
class TestGetAccount():

    #--------------------------------------------------------
    # get_account()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_all_params(self):
        # Set up mock
        url = base_url + '/accounts/testString'
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.get_account(
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_account_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_value_error(self):
        # Set up mock
        url = base_url + '/accounts/testString'
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}'
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
                service.get_account(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_account
#-----------------------------------------------------------------------------
class TestUpdateAccount():

    #--------------------------------------------------------
    # update_account()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_all_params(self):
        # Set up mock
        url = base_url + '/accounts/testString'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        parent = 'testString'

        # Invoke method
        response = service.update_account(
            account_id,
            parent,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == 'testString'


    #--------------------------------------------------------
    # test_update_account_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_value_error(self):
        # Set up mock
        url = base_url + '/accounts/testString'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        parent = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "parent": parent,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_account(**req_copy)



# endregion
##############################################################################
# End of Service: AccountOperations
##############################################################################

##############################################################################
# Start of Service: EnterpriseOperations
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_enterprise
#-----------------------------------------------------------------------------
class TestCreateEnterprise():

    #--------------------------------------------------------
    # create_enterprise()
    #--------------------------------------------------------
    @responses.activate
    def test_create_enterprise_all_params(self):
        # Set up mock
        url = base_url + '/enterprises'
        mock_response = '{"enterprise_id": "enterprise_id", "enterprise_account_id": "enterprise_account_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        source_account_id = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'
        domain = 'testString'

        # Invoke method
        response = service.create_enterprise(
            source_account_id,
            name,
            primary_contact_iam_id,
            domain=domain,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source_account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['primary_contact_iam_id'] == 'testString'
        assert req_body['domain'] == 'testString'


    #--------------------------------------------------------
    # test_create_enterprise_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_enterprise_value_error(self):
        # Set up mock
        url = base_url + '/enterprises'
        mock_response = '{"enterprise_id": "enterprise_id", "enterprise_account_id": "enterprise_account_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        source_account_id = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'
        domain = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "source_account_id": source_account_id,
            "name": name,
            "primary_contact_iam_id": primary_contact_iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_enterprise(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_enterprises
#-----------------------------------------------------------------------------
class TestListEnterprises():

    #--------------------------------------------------------
    # list_enterprises()
    #--------------------------------------------------------
    @responses.activate
    def test_list_enterprises_all_params(self):
        # Set up mock
        url = base_url + '/enterprises'
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_account_id = 'testString'
        account_group_id = 'testString'
        account_id = 'testString'
        limit = 38

        # Invoke method
        response = service.list_enterprises(
            enterprise_account_id=enterprise_account_id,
            account_group_id=account_group_id,
            account_id=account_id,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'enterprise_account_id={}'.format(enterprise_account_id) in query_string
        assert 'account_group_id={}'.format(account_group_id) in query_string
        assert 'account_id={}'.format(account_id) in query_string
        assert 'limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_list_enterprises_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_enterprises_required_params(self):
        # Set up mock
        url = base_url + '/enterprises'
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_enterprises()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_enterprise
#-----------------------------------------------------------------------------
class TestGetEnterprise():

    #--------------------------------------------------------
    # get_enterprise()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enterprise_all_params(self):
        # Set up mock
        url = base_url + '/enterprises/testString'
        mock_response = '{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Invoke method
        response = service.get_enterprise(
            enterprise_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_enterprise_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enterprise_value_error(self):
        # Set up mock
        url = base_url + '/enterprises/testString'
        mock_response = '{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "enterprise_id": enterprise_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_enterprise(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_enterprise
#-----------------------------------------------------------------------------
class TestUpdateEnterprise():

    #--------------------------------------------------------
    # update_enterprise()
    #--------------------------------------------------------
    @responses.activate
    def test_update_enterprise_all_params(self):
        # Set up mock
        url = base_url + '/enterprises/testString'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        enterprise_id = 'testString'
        name = 'testString'
        domain = 'testString'
        primary_contact_iam_id = 'testString'

        # Invoke method
        response = service.update_enterprise(
            enterprise_id,
            name=name,
            domain=domain,
            primary_contact_iam_id=primary_contact_iam_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['domain'] == 'testString'
        assert req_body['primary_contact_iam_id'] == 'testString'


    #--------------------------------------------------------
    # test_update_enterprise_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_enterprise_value_error(self):
        # Set up mock
        url = base_url + '/enterprises/testString'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        enterprise_id = 'testString'
        name = 'testString'
        domain = 'testString'
        primary_contact_iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "enterprise_id": enterprise_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_enterprise(**req_copy)



# endregion
##############################################################################
# End of Service: EnterpriseOperations
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for Account
#-----------------------------------------------------------------------------
class TestAccount():

    #--------------------------------------------------------
    # Test serialization/deserialization for Account
    #--------------------------------------------------------
    def test_account_serialization(self):

        # Construct a json representation of a Account model
        account_model_json = {}
        account_model_json['url'] = 'testString'
        account_model_json['id'] = 'testString'
        account_model_json['crn'] = 'testString'
        account_model_json['parent'] = 'testString'
        account_model_json['enterprise_account_id'] = 'testString'
        account_model_json['enterprise_id'] = 'testString'
        account_model_json['enterprise_path'] = 'testString'
        account_model_json['name'] = 'testString'
        account_model_json['state'] = 'testString'
        account_model_json['owner_iam_id'] = 'testString'
        account_model_json['paid'] = True
        account_model_json['owner_email'] = 'testString'
        account_model_json['is_enterprise_account'] = True
        account_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        account_model_json['created_by'] = 'testString'
        account_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'
        account_model_json['updated_by'] = 'testString'

        # Construct a model instance of Account by calling from_dict on the json representation
        account_model = Account.from_dict(account_model_json)
        assert account_model != False

        # Construct a model instance of Account by calling from_dict on the json representation
        account_model_dict = Account.from_dict(account_model_json).__dict__
        account_model2 = Account(**account_model_dict)

        # Verify the model instances are equivalent
        assert account_model == account_model2

        # Convert model instance back to dict and verify no loss of data
        account_model_json2 = account_model.to_dict()
        assert account_model_json2 == account_model_json

#-----------------------------------------------------------------------------
# Test Class for AccountGroup
#-----------------------------------------------------------------------------
class TestAccountGroup():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccountGroup
    #--------------------------------------------------------
    def test_account_group_serialization(self):

        # Construct a json representation of a AccountGroup model
        account_group_model_json = {}
        account_group_model_json['url'] = 'testString'
        account_group_model_json['id'] = 'testString'
        account_group_model_json['crn'] = 'testString'
        account_group_model_json['parent'] = 'testString'
        account_group_model_json['enterprise_account_id'] = 'testString'
        account_group_model_json['enterprise_id'] = 'testString'
        account_group_model_json['enterprise_path'] = 'testString'
        account_group_model_json['name'] = 'testString'
        account_group_model_json['state'] = 'testString'
        account_group_model_json['primary_contact_iam_id'] = 'testString'
        account_group_model_json['primary_contact_email'] = 'testString'
        account_group_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        account_group_model_json['created_by'] = 'testString'
        account_group_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'
        account_group_model_json['updated_by'] = 'testString'

        # Construct a model instance of AccountGroup by calling from_dict on the json representation
        account_group_model = AccountGroup.from_dict(account_group_model_json)
        assert account_group_model != False

        # Construct a model instance of AccountGroup by calling from_dict on the json representation
        account_group_model_dict = AccountGroup.from_dict(account_group_model_json).__dict__
        account_group_model2 = AccountGroup(**account_group_model_dict)

        # Verify the model instances are equivalent
        assert account_group_model == account_group_model2

        # Convert model instance back to dict and verify no loss of data
        account_group_model_json2 = account_group_model.to_dict()
        assert account_group_model_json2 == account_group_model_json

#-----------------------------------------------------------------------------
# Test Class for CreateAccountGroupResponse
#-----------------------------------------------------------------------------
class TestCreateAccountGroupResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for CreateAccountGroupResponse
    #--------------------------------------------------------
    def test_create_account_group_response_serialization(self):

        # Construct a json representation of a CreateAccountGroupResponse model
        create_account_group_response_model_json = {}
        create_account_group_response_model_json['account_group_id'] = 'testString'

        # Construct a model instance of CreateAccountGroupResponse by calling from_dict on the json representation
        create_account_group_response_model = CreateAccountGroupResponse.from_dict(create_account_group_response_model_json)
        assert create_account_group_response_model != False

        # Construct a model instance of CreateAccountGroupResponse by calling from_dict on the json representation
        create_account_group_response_model_dict = CreateAccountGroupResponse.from_dict(create_account_group_response_model_json).__dict__
        create_account_group_response_model2 = CreateAccountGroupResponse(**create_account_group_response_model_dict)

        # Verify the model instances are equivalent
        assert create_account_group_response_model == create_account_group_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_account_group_response_model_json2 = create_account_group_response_model.to_dict()
        assert create_account_group_response_model_json2 == create_account_group_response_model_json

#-----------------------------------------------------------------------------
# Test Class for CreateAccountResponse
#-----------------------------------------------------------------------------
class TestCreateAccountResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for CreateAccountResponse
    #--------------------------------------------------------
    def test_create_account_response_serialization(self):

        # Construct a json representation of a CreateAccountResponse model
        create_account_response_model_json = {}
        create_account_response_model_json['account_id'] = 'testString'

        # Construct a model instance of CreateAccountResponse by calling from_dict on the json representation
        create_account_response_model = CreateAccountResponse.from_dict(create_account_response_model_json)
        assert create_account_response_model != False

        # Construct a model instance of CreateAccountResponse by calling from_dict on the json representation
        create_account_response_model_dict = CreateAccountResponse.from_dict(create_account_response_model_json).__dict__
        create_account_response_model2 = CreateAccountResponse(**create_account_response_model_dict)

        # Verify the model instances are equivalent
        assert create_account_response_model == create_account_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_account_response_model_json2 = create_account_response_model.to_dict()
        assert create_account_response_model_json2 == create_account_response_model_json

#-----------------------------------------------------------------------------
# Test Class for CreateEnterpriseResponse
#-----------------------------------------------------------------------------
class TestCreateEnterpriseResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for CreateEnterpriseResponse
    #--------------------------------------------------------
    def test_create_enterprise_response_serialization(self):

        # Construct a json representation of a CreateEnterpriseResponse model
        create_enterprise_response_model_json = {}
        create_enterprise_response_model_json['enterprise_id'] = 'testString'
        create_enterprise_response_model_json['enterprise_account_id'] = 'testString'

        # Construct a model instance of CreateEnterpriseResponse by calling from_dict on the json representation
        create_enterprise_response_model = CreateEnterpriseResponse.from_dict(create_enterprise_response_model_json)
        assert create_enterprise_response_model != False

        # Construct a model instance of CreateEnterpriseResponse by calling from_dict on the json representation
        create_enterprise_response_model_dict = CreateEnterpriseResponse.from_dict(create_enterprise_response_model_json).__dict__
        create_enterprise_response_model2 = CreateEnterpriseResponse(**create_enterprise_response_model_dict)

        # Verify the model instances are equivalent
        assert create_enterprise_response_model == create_enterprise_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_enterprise_response_model_json2 = create_enterprise_response_model.to_dict()
        assert create_enterprise_response_model_json2 == create_enterprise_response_model_json

#-----------------------------------------------------------------------------
# Test Class for Enterprise
#-----------------------------------------------------------------------------
class TestEnterprise():

    #--------------------------------------------------------
    # Test serialization/deserialization for Enterprise
    #--------------------------------------------------------
    def test_enterprise_serialization(self):

        # Construct a json representation of a Enterprise model
        enterprise_model_json = {}
        enterprise_model_json['url'] = 'testString'
        enterprise_model_json['id'] = 'testString'
        enterprise_model_json['enterprise_account_id'] = 'testString'
        enterprise_model_json['crn'] = 'testString'
        enterprise_model_json['name'] = 'testString'
        enterprise_model_json['domain'] = 'testString'
        enterprise_model_json['state'] = 'testString'
        enterprise_model_json['primary_contact_iam_id'] = 'testString'
        enterprise_model_json['primary_contact_email'] = 'testString'
        enterprise_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        enterprise_model_json['created_by'] = 'testString'
        enterprise_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'
        enterprise_model_json['updated_by'] = 'testString'

        # Construct a model instance of Enterprise by calling from_dict on the json representation
        enterprise_model = Enterprise.from_dict(enterprise_model_json)
        assert enterprise_model != False

        # Construct a model instance of Enterprise by calling from_dict on the json representation
        enterprise_model_dict = Enterprise.from_dict(enterprise_model_json).__dict__
        enterprise_model2 = Enterprise(**enterprise_model_dict)

        # Verify the model instances are equivalent
        assert enterprise_model == enterprise_model2

        # Convert model instance back to dict and verify no loss of data
        enterprise_model_json2 = enterprise_model.to_dict()
        assert enterprise_model_json2 == enterprise_model_json

#-----------------------------------------------------------------------------
# Test Class for ListAccountGroupsResponse
#-----------------------------------------------------------------------------
class TestListAccountGroupsResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListAccountGroupsResponse
    #--------------------------------------------------------
    def test_list_account_groups_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        account_group_model = {} # AccountGroup
        account_group_model['url'] = 'testString'
        account_group_model['id'] = 'testString'
        account_group_model['crn'] = 'testString'
        account_group_model['parent'] = 'testString'
        account_group_model['enterprise_account_id'] = 'testString'
        account_group_model['enterprise_id'] = 'testString'
        account_group_model['enterprise_path'] = 'testString'
        account_group_model['name'] = 'testString'
        account_group_model['state'] = 'testString'
        account_group_model['primary_contact_iam_id'] = 'testString'
        account_group_model['primary_contact_email'] = 'testString'
        account_group_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        account_group_model['created_by'] = 'testString'
        account_group_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        account_group_model['updated_by'] = 'testString'

        # Construct a json representation of a ListAccountGroupsResponse model
        list_account_groups_response_model_json = {}
        list_account_groups_response_model_json['rows_count'] = 38
        list_account_groups_response_model_json['next_url'] = 'testString'
        list_account_groups_response_model_json['resources'] = [account_group_model]

        # Construct a model instance of ListAccountGroupsResponse by calling from_dict on the json representation
        list_account_groups_response_model = ListAccountGroupsResponse.from_dict(list_account_groups_response_model_json)
        assert list_account_groups_response_model != False

        # Construct a model instance of ListAccountGroupsResponse by calling from_dict on the json representation
        list_account_groups_response_model_dict = ListAccountGroupsResponse.from_dict(list_account_groups_response_model_json).__dict__
        list_account_groups_response_model2 = ListAccountGroupsResponse(**list_account_groups_response_model_dict)

        # Verify the model instances are equivalent
        assert list_account_groups_response_model == list_account_groups_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_account_groups_response_model_json2 = list_account_groups_response_model.to_dict()
        assert list_account_groups_response_model_json2 == list_account_groups_response_model_json

#-----------------------------------------------------------------------------
# Test Class for ListAccountsResponse
#-----------------------------------------------------------------------------
class TestListAccountsResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListAccountsResponse
    #--------------------------------------------------------
    def test_list_accounts_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        account_model = {} # Account
        account_model['url'] = 'testString'
        account_model['id'] = 'testString'
        account_model['crn'] = 'testString'
        account_model['parent'] = 'testString'
        account_model['enterprise_account_id'] = 'testString'
        account_model['enterprise_id'] = 'testString'
        account_model['enterprise_path'] = 'testString'
        account_model['name'] = 'testString'
        account_model['state'] = 'testString'
        account_model['owner_iam_id'] = 'testString'
        account_model['paid'] = True
        account_model['owner_email'] = 'testString'
        account_model['is_enterprise_account'] = True
        account_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        account_model['created_by'] = 'testString'
        account_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        account_model['updated_by'] = 'testString'

        # Construct a json representation of a ListAccountsResponse model
        list_accounts_response_model_json = {}
        list_accounts_response_model_json['rows_count'] = 38
        list_accounts_response_model_json['next_url'] = 'testString'
        list_accounts_response_model_json['resources'] = [account_model]

        # Construct a model instance of ListAccountsResponse by calling from_dict on the json representation
        list_accounts_response_model = ListAccountsResponse.from_dict(list_accounts_response_model_json)
        assert list_accounts_response_model != False

        # Construct a model instance of ListAccountsResponse by calling from_dict on the json representation
        list_accounts_response_model_dict = ListAccountsResponse.from_dict(list_accounts_response_model_json).__dict__
        list_accounts_response_model2 = ListAccountsResponse(**list_accounts_response_model_dict)

        # Verify the model instances are equivalent
        assert list_accounts_response_model == list_accounts_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_accounts_response_model_json2 = list_accounts_response_model.to_dict()
        assert list_accounts_response_model_json2 == list_accounts_response_model_json

#-----------------------------------------------------------------------------
# Test Class for ListEnterprisesResponse
#-----------------------------------------------------------------------------
class TestListEnterprisesResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListEnterprisesResponse
    #--------------------------------------------------------
    def test_list_enterprises_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        enterprise_model = {} # Enterprise
        enterprise_model['url'] = 'testString'
        enterprise_model['id'] = 'testString'
        enterprise_model['enterprise_account_id'] = 'testString'
        enterprise_model['crn'] = 'testString'
        enterprise_model['name'] = 'testString'
        enterprise_model['domain'] = 'testString'
        enterprise_model['state'] = 'testString'
        enterprise_model['primary_contact_iam_id'] = 'testString'
        enterprise_model['primary_contact_email'] = 'testString'
        enterprise_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        enterprise_model['created_by'] = 'testString'
        enterprise_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        enterprise_model['updated_by'] = 'testString'

        # Construct a json representation of a ListEnterprisesResponse model
        list_enterprises_response_model_json = {}
        list_enterprises_response_model_json['rows_count'] = 38
        list_enterprises_response_model_json['next_url'] = 'testString'
        list_enterprises_response_model_json['resources'] = [enterprise_model]

        # Construct a model instance of ListEnterprisesResponse by calling from_dict on the json representation
        list_enterprises_response_model = ListEnterprisesResponse.from_dict(list_enterprises_response_model_json)
        assert list_enterprises_response_model != False

        # Construct a model instance of ListEnterprisesResponse by calling from_dict on the json representation
        list_enterprises_response_model_dict = ListEnterprisesResponse.from_dict(list_enterprises_response_model_json).__dict__
        list_enterprises_response_model2 = ListEnterprisesResponse(**list_enterprises_response_model_dict)

        # Verify the model instances are equivalent
        assert list_enterprises_response_model == list_enterprises_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_enterprises_response_model_json2 = list_enterprises_response_model.to_dict()
        assert list_enterprises_response_model_json2 == list_enterprises_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
