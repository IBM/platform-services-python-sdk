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
from platform_services.iam_access_groups_v2 import *


service = IamAccessGroupsV2(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://iam.cloud.ibm.com/v2'
service.set_service_url(base_url)

##############################################################################
# Start of Service: AccessGroupOperations
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_access_group
#-----------------------------------------------------------------------------
class TestCreateAccessGroup():

    #--------------------------------------------------------
    # create_access_group()
    #--------------------------------------------------------
    @responses.activate
    def test_create_access_group_all_params(self):
        # Set up mock
        url = base_url + '/groups'
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        description = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.create_access_group(
            account_id,
            name,
            description=description,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description


    #--------------------------------------------------------
    # test_create_access_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_access_group_required_params(self):
        # Set up mock
        url = base_url + '/groups'
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = service.create_access_group(
            account_id,
            name,
            description=description,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description


#-----------------------------------------------------------------------------
# Test Class for list_access_groups
#-----------------------------------------------------------------------------
class TestListAccessGroups():

    #--------------------------------------------------------
    # list_access_groups()
    #--------------------------------------------------------
    @responses.activate
    def test_list_access_groups_all_params(self):
        # Set up mock
        url = base_url + '/groups'
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups": [{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'
        iam_id = 'testString'
        limit = 38
        offset = 38
        sort = 'testString'
        show_federated = True
        hide_public_access = True

        # Invoke method
        response = service.list_access_groups(
            account_id,
            transaction_id=transaction_id,
            iam_id=iam_id,
            limit=limit,
            offset=offset,
            sort=sort,
            show_federated=show_federated,
            hide_public_access=hide_public_access
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'iam_id={}'.format(iam_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'show_federated={}'.format('true' if show_federated else 'false') in query_string
        assert 'hide_public_access={}'.format('true' if hide_public_access else 'false') in query_string


    #--------------------------------------------------------
    # test_list_access_groups_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_access_groups_required_params(self):
        # Set up mock
        url = base_url + '/groups'
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "groups": [{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.list_access_groups(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string


#-----------------------------------------------------------------------------
# Test Class for get_access_group
#-----------------------------------------------------------------------------
class TestGetAccessGroup():

    #--------------------------------------------------------
    # get_access_group()
    #--------------------------------------------------------
    @responses.activate
    def test_get_access_group_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString'
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'
        show_federated = True

        # Invoke method
        response = service.get_access_group(
            access_group_id,
            transaction_id=transaction_id,
            show_federated=show_federated
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'show_federated={}'.format('true' if show_federated else 'false') in query_string


    #--------------------------------------------------------
    # test_get_access_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_access_group_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString'
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = service.get_access_group(
            access_group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_access_group
#-----------------------------------------------------------------------------
class TestUpdateAccessGroup():

    #--------------------------------------------------------
    # update_access_group()
    #--------------------------------------------------------
    @responses.activate
    def test_update_access_group_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString'
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.update_access_group(
            access_group_id,
            if_match,
            name=name,
            description=description,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description


    #--------------------------------------------------------
    # test_update_access_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_access_group_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString'
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "href": "href", "is_federated": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        if_match = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = service.update_access_group(
            access_group_id,
            if_match,
            name=name,
            description=description,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description


#-----------------------------------------------------------------------------
# Test Class for delete_access_group
#-----------------------------------------------------------------------------
class TestDeleteAccessGroup():

    #--------------------------------------------------------
    # delete_access_group()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_access_group_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'
        force = True

        # Invoke method
        response = service.delete_access_group(
            access_group_id,
            transaction_id=transaction_id,
            force=force
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'force={}'.format('true' if force else 'false') in query_string


    #--------------------------------------------------------
    # test_delete_access_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_access_group_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = service.delete_access_group(
            access_group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


# endregion
##############################################################################
# End of Service: AccessGroupOperations
##############################################################################

##############################################################################
# Start of Service: AccountSettings
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_account_settings
#-----------------------------------------------------------------------------
class TestGetAccountSettings():

    #--------------------------------------------------------
    # get_account_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_settings_all_params(self):
        # Set up mock
        url = base_url + '/groups/settings'
        mock_response = '{"account_id": "account_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.get_account_settings(
            account_id,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string


    #--------------------------------------------------------
    # test_get_account_settings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_settings_required_params(self):
        # Set up mock
        url = base_url + '/groups/settings'
        mock_response = '{"account_id": "account_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.get_account_settings(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string


#-----------------------------------------------------------------------------
# Test Class for update_account_settings
#-----------------------------------------------------------------------------
class TestUpdateAccountSettings():

    #--------------------------------------------------------
    # update_account_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_settings_all_params(self):
        # Set up mock
        url = base_url + '/groups/settings'
        mock_response = '{"account_id": "account_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        public_access_enabled = True
        transaction_id = 'testString'

        # Invoke method
        response = service.update_account_settings(
            account_id,
            public_access_enabled=public_access_enabled,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['public_access_enabled'] == public_access_enabled


    #--------------------------------------------------------
    # test_update_account_settings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_settings_required_params(self):
        # Set up mock
        url = base_url + '/groups/settings'
        mock_response = '{"account_id": "account_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id", "public_access_enabled": false}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        public_access_enabled = True

        # Invoke method
        response = service.update_account_settings(
            account_id,
            public_access_enabled=public_access_enabled,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['public_access_enabled'] == public_access_enabled


# endregion
##############################################################################
# End of Service: AccountSettings
##############################################################################

##############################################################################
# Start of Service: MembershipOperations
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for is_member_of_access_group
#-----------------------------------------------------------------------------
class TestIsMemberOfAccessGroup():

    #--------------------------------------------------------
    # is_member_of_access_group()
    #--------------------------------------------------------
    @responses.activate
    def test_is_member_of_access_group_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members/testString'
        responses.add(responses.HEAD,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.is_member_of_access_group(
            access_group_id,
            iam_id,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_is_member_of_access_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_is_member_of_access_group_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members/testString'
        responses.add(responses.HEAD,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.is_member_of_access_group(
            access_group_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for add_members_to_access_group
#-----------------------------------------------------------------------------
class TestAddMembersToAccessGroup():

    #--------------------------------------------------------
    # add_members_to_access_group()
    #--------------------------------------------------------
    @responses.activate
    def test_add_members_to_access_group_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members'
        mock_response = '{"members": [{"iam_id": "iam_id", "type": "type", "created_at": "created_at", "created_by_id": "created_by_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Construct a dict representation of a AddGroupMembersRequestMembersItem model
        add_group_members_request_members_item_model = {}
        add_group_members_request_members_item_model['iam_id'] = 'testString' 
        add_group_members_request_members_item_model['type'] = 'testString' 

        # Set up parameter values
        access_group_id = 'testString'
        members = [add_group_members_request_members_item_model]
        transaction_id = 'testString'

        # Invoke method
        response = service.add_members_to_access_group(
            access_group_id,
            members=members,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['members'] == members


    #--------------------------------------------------------
    # test_add_members_to_access_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_add_members_to_access_group_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members'
        mock_response = '{"members": [{"iam_id": "iam_id", "type": "type", "created_at": "created_at", "created_by_id": "created_by_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Construct a dict representation of a AddGroupMembersRequestMembersItem model
        add_group_members_request_members_item_model = {}
        add_group_members_request_members_item_model['iam_id'] = 'testString' 
        add_group_members_request_members_item_model['type'] = 'testString' 

        # Set up parameter values
        access_group_id = 'testString'
        members = [add_group_members_request_members_item_model]

        # Invoke method
        response = service.add_members_to_access_group(
            access_group_id,
            members=members,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['members'] == members


#-----------------------------------------------------------------------------
# Test Class for list_access_group_members
#-----------------------------------------------------------------------------
class TestListAccessGroupMembers():

    #--------------------------------------------------------
    # list_access_group_members()
    #--------------------------------------------------------
    @responses.activate
    def test_list_access_group_members_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members'
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "members": [{"iam_id": "iam_id", "type": "type", "name": "name", "email": "email", "description": "description", "href": "href", "created_at": "created_at", "created_by_id": "created_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'
        limit = 36.0
        offset = 36.0
        type = 'testString'
        verbose = True
        sort = 'testString'

        # Invoke method
        response = service.list_access_group_members(
            access_group_id,
            transaction_id=transaction_id,
            limit=limit,
            offset=offset,
            type=type,
            verbose=verbose,
            sort=sort
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string


    #--------------------------------------------------------
    # test_list_access_group_members_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_access_group_members_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members'
        mock_response = '{"limit": 5, "offset": 6, "total_count": 11, "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}, "members": [{"iam_id": "iam_id", "type": "type", "name": "name", "email": "email", "description": "description", "href": "href", "created_at": "created_at", "created_by_id": "created_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = service.list_access_group_members(
            access_group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for remove_member_from_access_group
#-----------------------------------------------------------------------------
class TestRemoveMemberFromAccessGroup():

    #--------------------------------------------------------
    # remove_member_from_access_group()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_member_from_access_group_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.remove_member_from_access_group(
            access_group_id,
            iam_id,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_remove_member_from_access_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_member_from_access_group_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.remove_member_from_access_group(
            access_group_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for remove_members_from_access_group
#-----------------------------------------------------------------------------
class TestRemoveMembersFromAccessGroup():

    #--------------------------------------------------------
    # remove_members_from_access_group()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_members_from_access_group_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members/delete'
        mock_response = '{"access_group_id": "access_group_id", "members": [{"iam_id": "iam_id", "trace": "trace", "status_code": 11, "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        access_group_id = 'testString'
        members = ['testString']
        transaction_id = 'testString'

        # Invoke method
        response = service.remove_members_from_access_group(
            access_group_id,
            members=members,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['members'] == members


    #--------------------------------------------------------
    # test_remove_members_from_access_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_members_from_access_group_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/members/delete'
        mock_response = '{"access_group_id": "access_group_id", "members": [{"iam_id": "iam_id", "trace": "trace", "status_code": 11, "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        access_group_id = 'testString'
        members = ['testString']

        # Invoke method
        response = service.remove_members_from_access_group(
            access_group_id,
            members=members,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['members'] == members


#-----------------------------------------------------------------------------
# Test Class for remove_member_from_all_access_groups
#-----------------------------------------------------------------------------
class TestRemoveMemberFromAllAccessGroups():

    #--------------------------------------------------------
    # remove_member_from_all_access_groups()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_member_from_all_access_groups_all_params(self):
        # Set up mock
        url = base_url + '/groups/_allgroups/members/testString'
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.remove_member_from_all_access_groups(
            account_id,
            iam_id,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string


    #--------------------------------------------------------
    # test_remove_member_from_all_access_groups_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_member_from_all_access_groups_required_params(self):
        # Set up mock
        url = base_url + '/groups/_allgroups/members/testString'
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.remove_member_from_all_access_groups(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string


#-----------------------------------------------------------------------------
# Test Class for add_member_to_multiple_access_groups
#-----------------------------------------------------------------------------
class TestAddMemberToMultipleAccessGroups():

    #--------------------------------------------------------
    # add_member_to_multiple_access_groups()
    #--------------------------------------------------------
    @responses.activate
    def test_add_member_to_multiple_access_groups_all_params(self):
        # Set up mock
        url = base_url + '/groups/_allgroups/members/testString'
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        type = 'testString'
        groups = ['testString']
        transaction_id = 'testString'

        # Invoke method
        response = service.add_member_to_multiple_access_groups(
            account_id,
            iam_id,
            type=type,
            groups=groups,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['groups'] == groups


    #--------------------------------------------------------
    # test_add_member_to_multiple_access_groups_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_add_member_to_multiple_access_groups_required_params(self):
        # Set up mock
        url = base_url + '/groups/_allgroups/members/testString'
        mock_response = '{"iam_id": "iam_id", "groups": [{"access_group_id": "access_group_id", "status_code": 11, "trace": "trace", "errors": [{"code": "code", "message": "message"}]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=207)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        type = 'testString'
        groups = ['testString']

        # Invoke method
        response = service.add_member_to_multiple_access_groups(
            account_id,
            iam_id,
            type=type,
            groups=groups,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 207
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['groups'] == groups


# endregion
##############################################################################
# End of Service: MembershipOperations
##############################################################################

##############################################################################
# Start of Service: RuleOperations
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for add_access_group_rule
#-----------------------------------------------------------------------------
class TestAddAccessGroupRule():

    #--------------------------------------------------------
    # add_access_group_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_add_access_group_rule_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules'
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'testString' 
        rule_conditions_model['operator'] = 'testString' 
        rule_conditions_model['value'] = 'testString' 

        # Set up parameter values
        access_group_id = 'testString'
        expiration = 38
        realm_name = 'testString'
        conditions = [rule_conditions_model]
        name = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.add_access_group_rule(
            access_group_id,
            expiration,
            realm_name,
            conditions,
            name=name,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expiration'] == expiration
        assert req_body['realm_name'] == realm_name
        assert req_body['conditions'] == conditions
        assert req_body['name'] == name


    #--------------------------------------------------------
    # test_add_access_group_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_add_access_group_rule_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules'
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'testString' 
        rule_conditions_model['operator'] = 'testString' 
        rule_conditions_model['value'] = 'testString' 

        # Set up parameter values
        access_group_id = 'testString'
        expiration = 38
        realm_name = 'testString'
        conditions = [rule_conditions_model]
        name = 'testString'

        # Invoke method
        response = service.add_access_group_rule(
            access_group_id,
            expiration,
            realm_name,
            conditions,
            name=name,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expiration'] == expiration
        assert req_body['realm_name'] == realm_name
        assert req_body['conditions'] == conditions
        assert req_body['name'] == name


#-----------------------------------------------------------------------------
# Test Class for list_access_group_rules
#-----------------------------------------------------------------------------
class TestListAccessGroupRules():

    #--------------------------------------------------------
    # list_access_group_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_access_group_rules_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules'
        mock_response = '{"rules": [{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.list_access_group_rules(
            access_group_id,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_access_group_rules_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_access_group_rules_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules'
        mock_response = '{"rules": [{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'

        # Invoke method
        response = service.list_access_group_rules(
            access_group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_access_group_rule
#-----------------------------------------------------------------------------
class TestGetAccessGroupRule():

    #--------------------------------------------------------
    # get_access_group_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_access_group_rule_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules/testString'
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.get_access_group_rule(
            access_group_id,
            rule_id,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_access_group_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_access_group_rule_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules/testString'
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = service.get_access_group_rule(
            access_group_id,
            rule_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for replace_access_group_rule
#-----------------------------------------------------------------------------
class TestReplaceAccessGroupRule():

    #--------------------------------------------------------
    # replace_access_group_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_access_group_rule_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules/testString'
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'testString' 
        rule_conditions_model['operator'] = 'testString' 
        rule_conditions_model['value'] = 'testString' 

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        if_match = 'testString'
        expiration = 38
        realm_name = 'testString'
        conditions = [rule_conditions_model]
        name = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.replace_access_group_rule(
            access_group_id,
            rule_id,
            if_match,
            expiration,
            realm_name,
            conditions,
            name=name,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expiration'] == expiration
        assert req_body['realm_name'] == realm_name
        assert req_body['conditions'] == conditions
        assert req_body['name'] == name


    #--------------------------------------------------------
    # test_replace_access_group_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_access_group_rule_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules/testString'
        mock_response = '{"id": "id", "name": "name", "expiration": 10, "realm_name": "realm_name", "access_group_id": "access_group_id", "account_id": "account_id", "conditions": [{"claim": "claim", "operator": "operator", "value": "value"}], "created_at": "created_at", "created_by_id": "created_by_id", "last_modified_at": "last_modified_at", "last_modified_by_id": "last_modified_by_id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuleConditions model
        rule_conditions_model = {}
        rule_conditions_model['claim'] = 'testString' 
        rule_conditions_model['operator'] = 'testString' 
        rule_conditions_model['value'] = 'testString' 

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        if_match = 'testString'
        expiration = 38
        realm_name = 'testString'
        conditions = [rule_conditions_model]
        name = 'testString'

        # Invoke method
        response = service.replace_access_group_rule(
            access_group_id,
            rule_id,
            if_match,
            expiration,
            realm_name,
            conditions,
            name=name,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expiration'] == expiration
        assert req_body['realm_name'] == realm_name
        assert req_body['conditions'] == conditions
        assert req_body['name'] == name


#-----------------------------------------------------------------------------
# Test Class for remove_access_group_rule
#-----------------------------------------------------------------------------
class TestRemoveAccessGroupRule():

    #--------------------------------------------------------
    # remove_access_group_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_access_group_rule_all_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.remove_access_group_rule(
            access_group_id,
            rule_id,
            transaction_id=transaction_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_remove_access_group_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_access_group_rule_required_params(self):
        # Set up mock
        url = base_url + '/groups/testString/rules/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        access_group_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = service.remove_access_group_rule(
            access_group_id,
            rule_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


# endregion
##############################################################################
# End of Service: RuleOperations
##############################################################################

