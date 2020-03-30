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
from platform_services.user_management_v1 import *


service = UserManagementV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://user-management.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: UserLinkages
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_user_linkages
#-----------------------------------------------------------------------------
class TestGetUserLinkages():

    #--------------------------------------------------------
    # get_user_linkages()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_linkages_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/linkages'
        mock_response = '{"linkages": [{"origin": "origin", "id": "id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.get_user_linkages(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_user_linkages_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_linkages_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/linkages'
        mock_response = '{"linkages": [{"origin": "origin", "id": "id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.get_user_linkages(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_user_linkages
#-----------------------------------------------------------------------------
class TestCreateUserLinkages():

    #--------------------------------------------------------
    # create_user_linkages()
    #--------------------------------------------------------
    @responses.activate
    def test_create_user_linkages_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/linkages/testString/testString'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        origin = 'testString'
        id_from_origin = 'testString'

        # Invoke method
        response = service.create_user_linkages(
            account_id,
            iam_id,
            origin,
            id_from_origin
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_create_user_linkages_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_user_linkages_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/linkages/testString/testString'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        origin = 'testString'
        id_from_origin = 'testString'

        # Invoke method
        response = service.create_user_linkages(
            account_id,
            iam_id,
            origin,
            id_from_origin
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for remove_user_linkages
#-----------------------------------------------------------------------------
class TestRemoveUserLinkages():

    #--------------------------------------------------------
    # remove_user_linkages()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_user_linkages_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/linkages/testString/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        origin = 'testString'
        id_from_origin = 'testString'

        # Invoke method
        response = service.remove_user_linkages(
            account_id,
            iam_id,
            origin,
            id_from_origin
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_remove_user_linkages_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_user_linkages_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/linkages/testString/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        origin = 'testString'
        id_from_origin = 'testString'

        # Invoke method
        response = service.remove_user_linkages(
            account_id,
            iam_id,
            origin,
            id_from_origin
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


# endregion
##############################################################################
# End of Service: UserLinkages
##############################################################################

##############################################################################
# Start of Service: UserProfile
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_user_profile
#-----------------------------------------------------------------------------
class TestGetUserProfile():

    #--------------------------------------------------------
    # get_user_profile()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_profile_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString'
        mock_response = '{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "linkages": [{"origin": "origin", "id": "id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        include_linkages = True

        # Invoke method
        response = service.get_user_profile(
            account_id,
            iam_id,
            include_linkages=include_linkages
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'include_linkages={}'.format('true' if include_linkages else 'false') in query_string


    #--------------------------------------------------------
    # test_get_user_profile_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_profile_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString'
        mock_response = '{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "linkages": [{"origin": "origin", "id": "id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.get_user_profile(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_user_profile
#-----------------------------------------------------------------------------
class TestCreateUserProfile():

    #--------------------------------------------------------
    # create_user_profile()
    #--------------------------------------------------------
    @responses.activate
    def test_create_user_profile_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        realm = 'IBMid'
        user_id = 'example@ibm.com'
        firstname = 'testString'
        lastname = 'testString'
        state = 'testString'
        email = 'testString'
        phonenumber = 'testString'
        altphonenumber = 'testString'
        photo = 'testString'

        # Invoke method
        response = service.create_user_profile(
            account_id,
            iam_id,
            realm=realm,
            user_id=user_id,
            firstname=firstname,
            lastname=lastname,
            state=state,
            email=email,
            phonenumber=phonenumber,
            altphonenumber=altphonenumber,
            photo=photo,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['realm'] == realm
        assert req_body['user_id'] == user_id
        assert req_body['firstname'] == firstname
        assert req_body['lastname'] == lastname
        assert req_body['state'] == state
        assert req_body['email'] == email
        assert req_body['phonenumber'] == phonenumber
        assert req_body['altphonenumber'] == altphonenumber
        assert req_body['photo'] == photo


    #--------------------------------------------------------
    # test_create_user_profile_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_user_profile_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.create_user_profile(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for update_user_profile
#-----------------------------------------------------------------------------
class TestUpdateUserProfile():

    #--------------------------------------------------------
    # update_user_profile()
    #--------------------------------------------------------
    @responses.activate
    def test_update_user_profile_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        user_id = 'testString'
        firstname = 'testString'
        lastname = 'testString'
        state = 'testString'
        email = 'testString'
        phonenumber = 'testString'
        altphonenumber = 'testString'
        photo = 'testString'

        # Invoke method
        response = service.update_user_profile(
            account_id,
            iam_id,
            user_id=user_id,
            firstname=firstname,
            lastname=lastname,
            state=state,
            email=email,
            phonenumber=phonenumber,
            altphonenumber=altphonenumber,
            photo=photo,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['user_id'] == user_id
        assert req_body['firstname'] == firstname
        assert req_body['lastname'] == lastname
        assert req_body['state'] == state
        assert req_body['email'] == email
        assert req_body['phonenumber'] == phonenumber
        assert req_body['altphonenumber'] == altphonenumber
        assert req_body['photo'] == photo


    #--------------------------------------------------------
    # test_update_user_profile_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_user_profile_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.update_user_profile(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


# endregion
##############################################################################
# End of Service: UserProfile
##############################################################################

##############################################################################
# Start of Service: UserSettings
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_user_settings
#-----------------------------------------------------------------------------
class TestGetUserSettings():

    #--------------------------------------------------------
    # get_user_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_settings_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/settings'
        mock_response = '{"language": "language", "notification_language": "notification_language", "allowed_ip_addresses": "32.96.110.50,172.16.254.1", "self_manage": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.get_user_settings(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_user_settings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_settings_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/settings'
        mock_response = '{"language": "language", "notification_language": "notification_language", "allowed_ip_addresses": "32.96.110.50,172.16.254.1", "self_manage": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.get_user_settings(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_user_settings
#-----------------------------------------------------------------------------
class TestUpdateUserSettings():

    #--------------------------------------------------------
    # update_user_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_update_user_settings_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/settings'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        language = 'testString'
        notification_language = 'testString'
        allowed_ip_addresses = '32.96.110.50,172.16.254.1'
        self_manage = True

        # Invoke method
        response = service.update_user_settings(
            account_id,
            iam_id,
            language=language,
            notification_language=notification_language,
            allowed_ip_addresses=allowed_ip_addresses,
            self_manage=self_manage,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['language'] == language
        assert req_body['notification_language'] == notification_language
        assert req_body['allowed_ip_addresses'] == allowed_ip_addresses
        assert req_body['self_manage'] == self_manage


    #--------------------------------------------------------
    # test_update_user_settings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_user_settings_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString/settings'
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.update_user_settings(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


# endregion
##############################################################################
# End of Service: UserSettings
##############################################################################

##############################################################################
# Start of Service: Users
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for remove_user_from_account
#-----------------------------------------------------------------------------
class TestRemoveUserFromAccount():

    #--------------------------------------------------------
    # remove_user_from_account()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_user_from_account_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.remove_user_from_account(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_remove_user_from_account_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_user_from_account_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = service.remove_user_from_account(
            account_id,
            iam_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for list_users
#-----------------------------------------------------------------------------
class TestListUsers():

    #--------------------------------------------------------
    # list_users()
    #--------------------------------------------------------
    @responses.activate
    def test_list_users_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users'
        mock_response = '{"total_results": 13, "limit": 5, "first_url": "first_url", "next_url": "next_url", "resources": [{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "linkages": [{"origin": "origin", "id": "id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        ia_mid = 'testString'
        firstname = 'testString'
        lastname = 'testString'
        email = 'testString'
        state = 'testString'
        realm = 'testString'

        # Invoke method
        response = service.list_users(
            account_id,
            ia_mid=ia_mid,
            firstname=firstname,
            lastname=lastname,
            email=email,
            state=state,
            realm=realm
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'IAMid={}'.format(ia_mid) in query_string
        assert 'firstname={}'.format(firstname) in query_string
        assert 'lastname={}'.format(lastname) in query_string
        assert 'email={}'.format(email) in query_string
        assert 'state={}'.format(state) in query_string
        assert 'realm={}'.format(realm) in query_string


    #--------------------------------------------------------
    # test_list_users_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_users_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users'
        mock_response = '{"total_results": 13, "limit": 5, "first_url": "first_url", "next_url": "next_url", "resources": [{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "linkages": [{"origin": "origin", "id": "id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.list_users(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for invite_users
#-----------------------------------------------------------------------------
class TestInviteUsers():

    #--------------------------------------------------------
    # invite_users()
    #--------------------------------------------------------
    @responses.activate
    def test_invite_users_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users'
        responses.add(responses.POST,
                      url,
                      status=202)

        # Construct a dict representation of a InviteUser model
        invite_user_model = {}
        invite_user_model['email'] = 'testString' 

        # Set up parameter values
        account_id = 'testString'
        users = [invite_user_model]

        # Invoke method
        response = service.invite_users(
            account_id,
            users=users,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['users'] == users


    #--------------------------------------------------------
    # test_invite_users_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_invite_users_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/users'
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.invite_users(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


#-----------------------------------------------------------------------------
# Test Class for get_ims_users
#-----------------------------------------------------------------------------
class TestGetImsUsers():

    #--------------------------------------------------------
    # get_ims_users()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ims_users_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/ims/users'
        mock_response = '{"total_results": 13, "limit": 5, "first_url": "first_url", "next_url": "next_url", "resources": [{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "linkages": [{"origin": "origin", "id": "id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        ia_mid = 'testString'
        firstname = 'testString'
        lastname = 'testString'
        email = 'testString'
        state = 'testString'

        # Invoke method
        response = service.get_ims_users(
            account_id,
            ia_mid=ia_mid,
            firstname=firstname,
            lastname=lastname,
            email=email,
            state=state
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'IAMid={}'.format(ia_mid) in query_string
        assert 'firstname={}'.format(firstname) in query_string
        assert 'lastname={}'.format(lastname) in query_string
        assert 'email={}'.format(email) in query_string
        assert 'state={}'.format(state) in query_string


    #--------------------------------------------------------
    # test_get_ims_users_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ims_users_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/ims/users'
        mock_response = '{"total_results": 13, "limit": 5, "first_url": "first_url", "next_url": "next_url", "resources": [{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "linkages": [{"origin": "origin", "id": "id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.get_ims_users(
            account_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_cf_users
#-----------------------------------------------------------------------------
class TestGetCfUsers():

    #--------------------------------------------------------
    # get_cf_users()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cf_users_all_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/organizations/testString/users'
        mock_response = '{"total_results": 13, "limit": 5, "first_url": "first_url", "next_url": "next_url", "resources": [{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "linkages": [{"origin": "origin", "id": "id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_guid = 'testString'

        # Invoke method
        response = service.get_cf_users(
            account_id,
            organization_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_cf_users_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cf_users_required_params(self):
        # Set up mock
        url = base_url + '/v2/accounts/testString/organizations/testString/users'
        mock_response = '{"total_results": 13, "limit": 5, "first_url": "first_url", "next_url": "next_url", "resources": [{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "linkages": [{"origin": "origin", "id": "id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_guid = 'testString'

        # Invoke method
        response = service.get_cf_users(
            account_id,
            organization_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Users
##############################################################################

