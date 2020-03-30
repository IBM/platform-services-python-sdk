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
from platform_services.enterprise_management_v1 import *


service = EnterpriseManagementV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://enterprise.test.cloud.ibm.com/v1'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == parent
        assert req_body['name'] == name
        assert req_body['primary_contact_iam_id'] == primary_contact_iam_id


    #--------------------------------------------------------
    # test_create_account_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_group_required_params(self):
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == parent
        assert req_body['name'] == name
        assert req_body['primary_contact_iam_id'] == primary_contact_iam_id


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
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}]}'
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
            limit=limit
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
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}]}'
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
# Test Class for get_account_group_by_id
#-----------------------------------------------------------------------------
class TestGetAccountGroupById():

    #--------------------------------------------------------
    # get_account_group_by_id()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_group_by_id_all_params(self):
        # Set up mock
        url = base_url + '/account-groups/testString'
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_group_id = 'testString'

        # Invoke method
        response = service.get_account_group_by_id(
            account_group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_account_group_by_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_group_by_id_required_params(self):
        # Set up mock
        url = base_url + '/account-groups/testString'
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_group_id = 'testString'

        # Invoke method
        response = service.get_account_group_by_id(
            account_group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['primary_contact_iam_id'] == primary_contact_iam_id


    #--------------------------------------------------------
    # test_update_account_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_group_required_params(self):
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['primary_contact_iam_id'] == primary_contact_iam_id


#-----------------------------------------------------------------------------
# Test Class for get_account_group_permissible_actions
#-----------------------------------------------------------------------------
class TestGetAccountGroupPermissibleActions():

    #--------------------------------------------------------
    # get_account_group_permissible_actions()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_group_permissible_actions_all_params(self):
        # Set up mock
        url = base_url + '/account-groups/testString/permissible-actions'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        account_group_id = 'testString'
        actions = ['testString']

        # Invoke method
        response = service.get_account_group_permissible_actions(
            account_group_id,
            actions=actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['actions'] == actions


    #--------------------------------------------------------
    # test_get_account_group_permissible_actions_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_group_permissible_actions_required_params(self):
        # Set up mock
        url = base_url + '/account-groups/testString/permissible-actions'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        account_group_id = 'testString'
        actions = ['testString']

        # Invoke method
        response = service.get_account_group_permissible_actions(
            account_group_id,
            actions=actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['actions'] == actions


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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == parent
        assert req_body['billing_unit_id'] == billing_unit_id


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
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


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
        mock_response = '{"account_group_id": "account_group_id"}'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == parent
        assert req_body['name'] == name
        assert req_body['owner_iam_id'] == owner_iam_id


    #--------------------------------------------------------
    # test_create_account_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_required_params(self):
        # Set up mock
        url = base_url + '/accounts'
        mock_response = '{"account_group_id": "account_group_id"}'
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == parent
        assert req_body['name'] == name
        assert req_body['owner_iam_id'] == owner_iam_id


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
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}]}'
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
            limit=limit
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
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}]}'
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
# Test Class for get_account_by_id
#-----------------------------------------------------------------------------
class TestGetAccountById():

    #--------------------------------------------------------
    # get_account_by_id()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_by_id_all_params(self):
        # Set up mock
        url = base_url + '/accounts/testString'
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.get_account_by_id(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_account_by_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_by_id_required_params(self):
        # Set up mock
        url = base_url + '/accounts/testString'
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.get_account_by_id(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == parent


    #--------------------------------------------------------
    # test_update_account_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_required_params(self):
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == parent


#-----------------------------------------------------------------------------
# Test Class for get_account_permissible_actions
#-----------------------------------------------------------------------------
class TestGetAccountPermissibleActions():

    #--------------------------------------------------------
    # get_account_permissible_actions()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_permissible_actions_all_params(self):
        # Set up mock
        url = base_url + '/accounts/testString/permissible-actions'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        actions = ['testString']

        # Invoke method
        response = service.get_account_permissible_actions(
            account_id,
            actions=actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['actions'] == actions


    #--------------------------------------------------------
    # test_get_account_permissible_actions_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_permissible_actions_required_params(self):
        # Set up mock
        url = base_url + '/accounts/testString/permissible-actions'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        actions = ['testString']

        # Invoke method
        response = service.get_account_permissible_actions(
            account_id,
            actions=actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['actions'] == actions


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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source_account_id'] == source_account_id
        assert req_body['name'] == name
        assert req_body['primary_contact_iam_id'] == primary_contact_iam_id
        assert req_body['domain'] == domain


    #--------------------------------------------------------
    # test_create_enterprise_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_enterprise_required_params(self):
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source_account_id'] == source_account_id
        assert req_body['name'] == name
        assert req_body['primary_contact_iam_id'] == primary_contact_iam_id
        assert req_body['domain'] == domain


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
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}]}'
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
            limit=limit
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
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}]}'
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
        mock_response = '{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Invoke method
        response = service.get_enterprise(
            enterprise_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_enterprise_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enterprise_required_params(self):
        # Set up mock
        url = base_url + '/enterprises/testString'
        mock_response = '{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "created_at", "created_by": "created_by", "updated_at": "updated_at", "updated_by": "updated_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Invoke method
        response = service.get_enterprise(
            enterprise_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['domain'] == domain
        assert req_body['primary_contact_iam_id'] == primary_contact_iam_id


    #--------------------------------------------------------
    # test_update_enterprise_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_enterprise_required_params(self):
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['domain'] == domain
        assert req_body['primary_contact_iam_id'] == primary_contact_iam_id


#-----------------------------------------------------------------------------
# Test Class for get_enterprise_permissible_actions
#-----------------------------------------------------------------------------
class TestGetEnterprisePermissibleActions():

    #--------------------------------------------------------
    # get_enterprise_permissible_actions()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enterprise_permissible_actions_all_params(self):
        # Set up mock
        url = base_url + '/enterprises/testString/permissible-actions'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'
        actions = ['testString']

        # Invoke method
        response = service.get_enterprise_permissible_actions(
            enterprise_id,
            actions=actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['actions'] == actions


    #--------------------------------------------------------
    # test_get_enterprise_permissible_actions_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enterprise_permissible_actions_required_params(self):
        # Set up mock
        url = base_url + '/enterprises/testString/permissible-actions'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'
        actions = ['testString']

        # Invoke method
        response = service.get_enterprise_permissible_actions(
            enterprise_id,
            actions=actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['actions'] == actions


# endregion
##############################################################################
# End of Service: EnterpriseOperations
##############################################################################

