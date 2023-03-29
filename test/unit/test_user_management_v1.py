# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
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
Unit Tests for UserManagementV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.user_management_v1 import *


_service = UserManagementV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://user-management.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Users
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

        service = UserManagementV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, UserManagementV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = UserManagementV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListUsers:
    """
    Test Class for list_users
    """

    @responses.activate
    def test_list_users_all_params(self):
        """
        list_users()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users')
        mock_response = '{"total_results": 13, "limit": 5, "first_url": "first_url", "next_url": "next_url", "resources": [{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "added_on": "added_on"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        limit = 100
        start = 'testString'
        user_id = 'testString'

        # Invoke method
        response = _service.list_users(account_id, limit=limit, start=start, user_id=user_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert '_start={}'.format(start) in query_string
        assert 'user_id={}'.format(user_id) in query_string

    def test_list_users_all_params_with_retries(self):
        # Enable retries and run test_list_users_all_params.
        _service.enable_retries()
        self.test_list_users_all_params()

        # Disable retries and run test_list_users_all_params.
        _service.disable_retries()
        self.test_list_users_all_params()

    @responses.activate
    def test_list_users_required_params(self):
        """
        test_list_users_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users')
        mock_response = '{"total_results": 13, "limit": 5, "first_url": "first_url", "next_url": "next_url", "resources": [{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "added_on": "added_on"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_users(account_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_users_required_params_with_retries(self):
        # Enable retries and run test_list_users_required_params.
        _service.enable_retries()
        self.test_list_users_required_params()

        # Disable retries and run test_list_users_required_params.
        _service.disable_retries()
        self.test_list_users_required_params()

    @responses.activate
    def test_list_users_value_error(self):
        """
        test_list_users_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users')
        mock_response = '{"total_results": 13, "limit": 5, "first_url": "first_url", "next_url": "next_url", "resources": [{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "added_on": "added_on"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_users(**req_copy)

    def test_list_users_value_error_with_retries(self):
        # Enable retries and run test_list_users_value_error.
        _service.enable_retries()
        self.test_list_users_value_error()

        # Disable retries and run test_list_users_value_error.
        _service.disable_retries()
        self.test_list_users_value_error()

    @responses.activate
    def test_list_users_with_pager_get_next(self):
        """
        test_list_users_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/accounts/testString/users')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?_start=1","resources":[{"id":"id","iam_id":"iam_id","realm":"realm","user_id":"user_id","firstname":"firstname","lastname":"lastname","state":"state","email":"email","phonenumber":"phonenumber","altphonenumber":"altphonenumber","photo":"photo","account_id":"account_id","added_on":"added_on"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","iam_id":"iam_id","realm":"realm","user_id":"user_id","firstname":"firstname","lastname":"lastname","state":"state","email":"email","phonenumber":"phonenumber","altphonenumber":"altphonenumber","photo":"photo","account_id":"account_id","added_on":"added_on"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = UsersPager(
            client=_service,
            account_id='testString',
            limit=10,
            user_id='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_users_with_pager_get_all(self):
        """
        test_list_users_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/accounts/testString/users')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?_start=1","resources":[{"id":"id","iam_id":"iam_id","realm":"realm","user_id":"user_id","firstname":"firstname","lastname":"lastname","state":"state","email":"email","phonenumber":"phonenumber","altphonenumber":"altphonenumber","photo":"photo","account_id":"account_id","added_on":"added_on"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","iam_id":"iam_id","realm":"realm","user_id":"user_id","firstname":"firstname","lastname":"lastname","state":"state","email":"email","phonenumber":"phonenumber","altphonenumber":"altphonenumber","photo":"photo","account_id":"account_id","added_on":"added_on"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = UsersPager(
            client=_service,
            account_id='testString',
            limit=10,
            user_id='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestInviteUsers:
    """
    Test Class for invite_users
    """

    @responses.activate
    def test_invite_users_all_params(self):
        """
        invite_users()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users')
        mock_response = '{"resources": [{"email": "email", "id": "id", "state": "state"}]}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Construct a dict representation of a InviteUser model
        invite_user_model = {}
        invite_user_model['email'] = 'testString'
        invite_user_model['account_role'] = 'testString'

        # Construct a dict representation of a Role model
        role_model = {}
        role_model['role_id'] = 'testString'

        # Construct a dict representation of a Attribute model
        attribute_model = {}
        attribute_model['name'] = 'testString'
        attribute_model['value'] = 'testString'

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['attributes'] = [attribute_model]

        # Construct a dict representation of a InviteUserIamPolicy model
        invite_user_iam_policy_model = {}
        invite_user_iam_policy_model['type'] = 'testString'
        invite_user_iam_policy_model['roles'] = [role_model]
        invite_user_iam_policy_model['resources'] = [resource_model]

        # Set up parameter values
        account_id = 'testString'
        users = [invite_user_model]
        iam_policy = [invite_user_iam_policy_model]
        access_groups = ['testString']

        # Invoke method
        response = _service.invite_users(
            account_id, users=users, iam_policy=iam_policy, access_groups=access_groups, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['users'] == [invite_user_model]
        assert req_body['iam_policy'] == [invite_user_iam_policy_model]
        assert req_body['access_groups'] == ['testString']

    def test_invite_users_all_params_with_retries(self):
        # Enable retries and run test_invite_users_all_params.
        _service.enable_retries()
        self.test_invite_users_all_params()

        # Disable retries and run test_invite_users_all_params.
        _service.disable_retries()
        self.test_invite_users_all_params()

    @responses.activate
    def test_invite_users_required_params(self):
        """
        test_invite_users_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users')
        mock_response = '{"resources": [{"email": "email", "id": "id", "state": "state"}]}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.invite_users(account_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_invite_users_required_params_with_retries(self):
        # Enable retries and run test_invite_users_required_params.
        _service.enable_retries()
        self.test_invite_users_required_params()

        # Disable retries and run test_invite_users_required_params.
        _service.disable_retries()
        self.test_invite_users_required_params()

    @responses.activate
    def test_invite_users_value_error(self):
        """
        test_invite_users_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users')
        mock_response = '{"resources": [{"email": "email", "id": "id", "state": "state"}]}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.invite_users(**req_copy)

    def test_invite_users_value_error_with_retries(self):
        # Enable retries and run test_invite_users_value_error.
        _service.enable_retries()
        self.test_invite_users_value_error()

        # Disable retries and run test_invite_users_value_error.
        _service.disable_retries()
        self.test_invite_users_value_error()


class TestGetUserProfile:
    """
    Test Class for get_user_profile
    """

    @responses.activate
    def test_get_user_profile_all_params(self):
        """
        get_user_profile()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString')
        mock_response = '{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "added_on": "added_on"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        include_activity = 'testString'

        # Invoke method
        response = _service.get_user_profile(account_id, iam_id, include_activity=include_activity, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_activity={}'.format(include_activity) in query_string

    def test_get_user_profile_all_params_with_retries(self):
        # Enable retries and run test_get_user_profile_all_params.
        _service.enable_retries()
        self.test_get_user_profile_all_params()

        # Disable retries and run test_get_user_profile_all_params.
        _service.disable_retries()
        self.test_get_user_profile_all_params()

    @responses.activate
    def test_get_user_profile_required_params(self):
        """
        test_get_user_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString')
        mock_response = '{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "added_on": "added_on"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.get_user_profile(account_id, iam_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_user_profile_required_params_with_retries(self):
        # Enable retries and run test_get_user_profile_required_params.
        _service.enable_retries()
        self.test_get_user_profile_required_params()

        # Disable retries and run test_get_user_profile_required_params.
        _service.disable_retries()
        self.test_get_user_profile_required_params()

    @responses.activate
    def test_get_user_profile_value_error(self):
        """
        test_get_user_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString')
        mock_response = '{"id": "id", "iam_id": "iam_id", "realm": "realm", "user_id": "user_id", "firstname": "firstname", "lastname": "lastname", "state": "state", "email": "email", "phonenumber": "phonenumber", "altphonenumber": "altphonenumber", "photo": "photo", "account_id": "account_id", "added_on": "added_on"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_user_profile(**req_copy)

    def test_get_user_profile_value_error_with_retries(self):
        # Enable retries and run test_get_user_profile_value_error.
        _service.enable_retries()
        self.test_get_user_profile_value_error()

        # Disable retries and run test_get_user_profile_value_error.
        _service.disable_retries()
        self.test_get_user_profile_value_error()


class TestUpdateUserProfile:
    """
    Test Class for update_user_profile
    """

    @responses.activate
    def test_update_user_profile_all_params(self):
        """
        update_user_profile()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        firstname = 'testString'
        lastname = 'testString'
        state = 'testString'
        email = 'testString'
        phonenumber = 'testString'
        altphonenumber = 'testString'
        photo = 'testString'
        include_activity = 'testString'

        # Invoke method
        response = _service.update_user_profile(
            account_id,
            iam_id,
            firstname=firstname,
            lastname=lastname,
            state=state,
            email=email,
            phonenumber=phonenumber,
            altphonenumber=altphonenumber,
            photo=photo,
            include_activity=include_activity,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_activity={}'.format(include_activity) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['firstname'] == 'testString'
        assert req_body['lastname'] == 'testString'
        assert req_body['state'] == 'testString'
        assert req_body['email'] == 'testString'
        assert req_body['phonenumber'] == 'testString'
        assert req_body['altphonenumber'] == 'testString'
        assert req_body['photo'] == 'testString'

    def test_update_user_profile_all_params_with_retries(self):
        # Enable retries and run test_update_user_profile_all_params.
        _service.enable_retries()
        self.test_update_user_profile_all_params()

        # Disable retries and run test_update_user_profile_all_params.
        _service.disable_retries()
        self.test_update_user_profile_all_params()

    @responses.activate
    def test_update_user_profile_required_params(self):
        """
        test_update_user_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.update_user_profile(account_id, iam_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_update_user_profile_required_params_with_retries(self):
        # Enable retries and run test_update_user_profile_required_params.
        _service.enable_retries()
        self.test_update_user_profile_required_params()

        # Disable retries and run test_update_user_profile_required_params.
        _service.disable_retries()
        self.test_update_user_profile_required_params()

    @responses.activate
    def test_update_user_profile_value_error(self):
        """
        test_update_user_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_user_profile(**req_copy)

    def test_update_user_profile_value_error_with_retries(self):
        # Enable retries and run test_update_user_profile_value_error.
        _service.enable_retries()
        self.test_update_user_profile_value_error()

        # Disable retries and run test_update_user_profile_value_error.
        _service.disable_retries()
        self.test_update_user_profile_value_error()


class TestRemoveUser:
    """
    Test Class for remove_user
    """

    @responses.activate
    def test_remove_user_all_params(self):
        """
        remove_user()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        include_activity = 'testString'

        # Invoke method
        response = _service.remove_user(account_id, iam_id, include_activity=include_activity, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_activity={}'.format(include_activity) in query_string

    def test_remove_user_all_params_with_retries(self):
        # Enable retries and run test_remove_user_all_params.
        _service.enable_retries()
        self.test_remove_user_all_params()

        # Disable retries and run test_remove_user_all_params.
        _service.disable_retries()
        self.test_remove_user_all_params()

    @responses.activate
    def test_remove_user_required_params(self):
        """
        test_remove_user_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.remove_user(account_id, iam_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_remove_user_required_params_with_retries(self):
        # Enable retries and run test_remove_user_required_params.
        _service.enable_retries()
        self.test_remove_user_required_params()

        # Disable retries and run test_remove_user_required_params.
        _service.disable_retries()
        self.test_remove_user_required_params()

    @responses.activate
    def test_remove_user_value_error(self):
        """
        test_remove_user_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.remove_user(**req_copy)

    def test_remove_user_value_error_with_retries(self):
        # Enable retries and run test_remove_user_value_error.
        _service.enable_retries()
        self.test_remove_user_value_error()

        # Disable retries and run test_remove_user_value_error.
        _service.disable_retries()
        self.test_remove_user_value_error()


class TestAccept:
    """
    Test Class for accept
    """

    @responses.activate
    def test_accept_all_params(self):
        """
        accept()
        """
        # Set up mock
        url = preprocess_url('/v2/users/accept')
        responses.add(responses.POST, url, status=202)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.accept(account_id=account_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'testString'

    def test_accept_all_params_with_retries(self):
        # Enable retries and run test_accept_all_params.
        _service.enable_retries()
        self.test_accept_all_params()

        # Disable retries and run test_accept_all_params.
        _service.disable_retries()
        self.test_accept_all_params()

    @responses.activate
    def test_accept_required_params(self):
        """
        test_accept_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/users/accept')
        responses.add(responses.POST, url, status=202)

        # Invoke method
        response = _service.accept()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_accept_required_params_with_retries(self):
        # Enable retries and run test_accept_required_params.
        _service.enable_retries()
        self.test_accept_required_params()

        # Disable retries and run test_accept_required_params.
        _service.disable_retries()
        self.test_accept_required_params()


class TestV3RemoveUser:
    """
    Test Class for v3_remove_user
    """

    @responses.activate
    def test_v3_remove_user_all_params(self):
        """
        v3_remove_user()
        """
        # Set up mock
        url = preprocess_url('/v3/accounts/testString/users/testString')
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.v3_remove_user(account_id, iam_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_v3_remove_user_all_params_with_retries(self):
        # Enable retries and run test_v3_remove_user_all_params.
        _service.enable_retries()
        self.test_v3_remove_user_all_params()

        # Disable retries and run test_v3_remove_user_all_params.
        _service.disable_retries()
        self.test_v3_remove_user_all_params()

    @responses.activate
    def test_v3_remove_user_value_error(self):
        """
        test_v3_remove_user_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/accounts/testString/users/testString')
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.v3_remove_user(**req_copy)

    def test_v3_remove_user_value_error_with_retries(self):
        # Enable retries and run test_v3_remove_user_value_error.
        _service.enable_retries()
        self.test_v3_remove_user_value_error()

        # Disable retries and run test_v3_remove_user_value_error.
        _service.disable_retries()
        self.test_v3_remove_user_value_error()


# endregion
##############################################################################
# End of Service: Users
##############################################################################

##############################################################################
# Start of Service: UserSettings
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

        service = UserManagementV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, UserManagementV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = UserManagementV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetUserSettings:
    """
    Test Class for get_user_settings
    """

    @responses.activate
    def test_get_user_settings_all_params(self):
        """
        get_user_settings()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString/settings')
        mock_response = '{"language": "language", "notification_language": "notification_language", "allowed_ip_addresses": "32.96.110.50,172.16.254.1", "self_manage": false}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.get_user_settings(account_id, iam_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_user_settings_all_params_with_retries(self):
        # Enable retries and run test_get_user_settings_all_params.
        _service.enable_retries()
        self.test_get_user_settings_all_params()

        # Disable retries and run test_get_user_settings_all_params.
        _service.disable_retries()
        self.test_get_user_settings_all_params()

    @responses.activate
    def test_get_user_settings_value_error(self):
        """
        test_get_user_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString/settings')
        mock_response = '{"language": "language", "notification_language": "notification_language", "allowed_ip_addresses": "32.96.110.50,172.16.254.1", "self_manage": false}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_user_settings(**req_copy)

    def test_get_user_settings_value_error_with_retries(self):
        # Enable retries and run test_get_user_settings_value_error.
        _service.enable_retries()
        self.test_get_user_settings_value_error()

        # Disable retries and run test_get_user_settings_value_error.
        _service.disable_retries()
        self.test_get_user_settings_value_error()


class TestUpdateUserSettings:
    """
    Test Class for update_user_settings
    """

    @responses.activate
    def test_update_user_settings_all_params(self):
        """
        update_user_settings()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString/settings')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'
        language = 'testString'
        notification_language = 'testString'
        allowed_ip_addresses = '32.96.110.50,172.16.254.1'
        self_manage = True

        # Invoke method
        response = _service.update_user_settings(
            account_id,
            iam_id,
            language=language,
            notification_language=notification_language,
            allowed_ip_addresses=allowed_ip_addresses,
            self_manage=self_manage,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['language'] == 'testString'
        assert req_body['notification_language'] == 'testString'
        assert req_body['allowed_ip_addresses'] == '32.96.110.50,172.16.254.1'
        assert req_body['self_manage'] == True

    def test_update_user_settings_all_params_with_retries(self):
        # Enable retries and run test_update_user_settings_all_params.
        _service.enable_retries()
        self.test_update_user_settings_all_params()

        # Disable retries and run test_update_user_settings_all_params.
        _service.disable_retries()
        self.test_update_user_settings_all_params()

    @responses.activate
    def test_update_user_settings_required_params(self):
        """
        test_update_user_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString/settings')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Invoke method
        response = _service.update_user_settings(account_id, iam_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_update_user_settings_required_params_with_retries(self):
        # Enable retries and run test_update_user_settings_required_params.
        _service.enable_retries()
        self.test_update_user_settings_required_params()

        # Disable retries and run test_update_user_settings_required_params.
        _service.disable_retries()
        self.test_update_user_settings_required_params()

    @responses.activate
    def test_update_user_settings_value_error(self):
        """
        test_update_user_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/accounts/testString/users/testString/settings')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        account_id = 'testString'
        iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_user_settings(**req_copy)

    def test_update_user_settings_value_error_with_retries(self):
        # Enable retries and run test_update_user_settings_value_error.
        _service.enable_retries()
        self.test_update_user_settings_value_error()

        # Disable retries and run test_update_user_settings_value_error.
        _service.disable_retries()
        self.test_update_user_settings_value_error()


# endregion
##############################################################################
# End of Service: UserSettings
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_InvitedUser:
    """
    Test Class for InvitedUser
    """

    def test_invited_user_serialization(self):
        """
        Test serialization/deserialization for InvitedUser
        """

        # Construct a json representation of a InvitedUser model
        invited_user_model_json = {}
        invited_user_model_json['email'] = 'testString'
        invited_user_model_json['id'] = 'testString'
        invited_user_model_json['state'] = 'testString'

        # Construct a model instance of InvitedUser by calling from_dict on the json representation
        invited_user_model = InvitedUser.from_dict(invited_user_model_json)
        assert invited_user_model != False

        # Construct a model instance of InvitedUser by calling from_dict on the json representation
        invited_user_model_dict = InvitedUser.from_dict(invited_user_model_json).__dict__
        invited_user_model2 = InvitedUser(**invited_user_model_dict)

        # Verify the model instances are equivalent
        assert invited_user_model == invited_user_model2

        # Convert model instance back to dict and verify no loss of data
        invited_user_model_json2 = invited_user_model.to_dict()
        assert invited_user_model_json2 == invited_user_model_json


class TestModel_InvitedUserList:
    """
    Test Class for InvitedUserList
    """

    def test_invited_user_list_serialization(self):
        """
        Test serialization/deserialization for InvitedUserList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        invited_user_model = {}  # InvitedUser
        invited_user_model['email'] = 'testString'
        invited_user_model['id'] = 'testString'
        invited_user_model['state'] = 'testString'

        # Construct a json representation of a InvitedUserList model
        invited_user_list_model_json = {}
        invited_user_list_model_json['resources'] = [invited_user_model]

        # Construct a model instance of InvitedUserList by calling from_dict on the json representation
        invited_user_list_model = InvitedUserList.from_dict(invited_user_list_model_json)
        assert invited_user_list_model != False

        # Construct a model instance of InvitedUserList by calling from_dict on the json representation
        invited_user_list_model_dict = InvitedUserList.from_dict(invited_user_list_model_json).__dict__
        invited_user_list_model2 = InvitedUserList(**invited_user_list_model_dict)

        # Verify the model instances are equivalent
        assert invited_user_list_model == invited_user_list_model2

        # Convert model instance back to dict and verify no loss of data
        invited_user_list_model_json2 = invited_user_list_model.to_dict()
        assert invited_user_list_model_json2 == invited_user_list_model_json


class TestModel_UserList:
    """
    Test Class for UserList
    """

    def test_user_list_serialization(self):
        """
        Test serialization/deserialization for UserList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_profile_model = {}  # UserProfile
        user_profile_model['id'] = 'testString'
        user_profile_model['iam_id'] = 'testString'
        user_profile_model['realm'] = 'testString'
        user_profile_model['user_id'] = 'testString'
        user_profile_model['firstname'] = 'testString'
        user_profile_model['lastname'] = 'testString'
        user_profile_model['state'] = 'testString'
        user_profile_model['email'] = 'testString'
        user_profile_model['phonenumber'] = 'testString'
        user_profile_model['altphonenumber'] = 'testString'
        user_profile_model['photo'] = 'testString'
        user_profile_model['account_id'] = 'testString'
        user_profile_model['added_on'] = 'testString'

        # Construct a json representation of a UserList model
        user_list_model_json = {}
        user_list_model_json['total_results'] = 38
        user_list_model_json['limit'] = 38
        user_list_model_json['first_url'] = 'testString'
        user_list_model_json['next_url'] = 'testString'
        user_list_model_json['resources'] = [user_profile_model]

        # Construct a model instance of UserList by calling from_dict on the json representation
        user_list_model = UserList.from_dict(user_list_model_json)
        assert user_list_model != False

        # Construct a model instance of UserList by calling from_dict on the json representation
        user_list_model_dict = UserList.from_dict(user_list_model_json).__dict__
        user_list_model2 = UserList(**user_list_model_dict)

        # Verify the model instances are equivalent
        assert user_list_model == user_list_model2

        # Convert model instance back to dict and verify no loss of data
        user_list_model_json2 = user_list_model.to_dict()
        assert user_list_model_json2 == user_list_model_json


class TestModel_UserProfile:
    """
    Test Class for UserProfile
    """

    def test_user_profile_serialization(self):
        """
        Test serialization/deserialization for UserProfile
        """

        # Construct a json representation of a UserProfile model
        user_profile_model_json = {}
        user_profile_model_json['id'] = 'testString'
        user_profile_model_json['iam_id'] = 'testString'
        user_profile_model_json['realm'] = 'testString'
        user_profile_model_json['user_id'] = 'testString'
        user_profile_model_json['firstname'] = 'testString'
        user_profile_model_json['lastname'] = 'testString'
        user_profile_model_json['state'] = 'testString'
        user_profile_model_json['email'] = 'testString'
        user_profile_model_json['phonenumber'] = 'testString'
        user_profile_model_json['altphonenumber'] = 'testString'
        user_profile_model_json['photo'] = 'testString'
        user_profile_model_json['account_id'] = 'testString'
        user_profile_model_json['added_on'] = 'testString'

        # Construct a model instance of UserProfile by calling from_dict on the json representation
        user_profile_model = UserProfile.from_dict(user_profile_model_json)
        assert user_profile_model != False

        # Construct a model instance of UserProfile by calling from_dict on the json representation
        user_profile_model_dict = UserProfile.from_dict(user_profile_model_json).__dict__
        user_profile_model2 = UserProfile(**user_profile_model_dict)

        # Verify the model instances are equivalent
        assert user_profile_model == user_profile_model2

        # Convert model instance back to dict and verify no loss of data
        user_profile_model_json2 = user_profile_model.to_dict()
        assert user_profile_model_json2 == user_profile_model_json


class TestModel_UserSettings:
    """
    Test Class for UserSettings
    """

    def test_user_settings_serialization(self):
        """
        Test serialization/deserialization for UserSettings
        """

        # Construct a json representation of a UserSettings model
        user_settings_model_json = {}
        user_settings_model_json['language'] = 'testString'
        user_settings_model_json['notification_language'] = 'testString'
        user_settings_model_json['allowed_ip_addresses'] = '32.96.110.50,172.16.254.1'
        user_settings_model_json['self_manage'] = True

        # Construct a model instance of UserSettings by calling from_dict on the json representation
        user_settings_model = UserSettings.from_dict(user_settings_model_json)
        assert user_settings_model != False

        # Construct a model instance of UserSettings by calling from_dict on the json representation
        user_settings_model_dict = UserSettings.from_dict(user_settings_model_json).__dict__
        user_settings_model2 = UserSettings(**user_settings_model_dict)

        # Verify the model instances are equivalent
        assert user_settings_model == user_settings_model2

        # Convert model instance back to dict and verify no loss of data
        user_settings_model_json2 = user_settings_model.to_dict()
        assert user_settings_model_json2 == user_settings_model_json


class TestModel_Attribute:
    """
    Test Class for Attribute
    """

    def test_attribute_serialization(self):
        """
        Test serialization/deserialization for Attribute
        """

        # Construct a json representation of a Attribute model
        attribute_model_json = {}
        attribute_model_json['name'] = 'testString'
        attribute_model_json['value'] = 'testString'

        # Construct a model instance of Attribute by calling from_dict on the json representation
        attribute_model = Attribute.from_dict(attribute_model_json)
        assert attribute_model != False

        # Construct a model instance of Attribute by calling from_dict on the json representation
        attribute_model_dict = Attribute.from_dict(attribute_model_json).__dict__
        attribute_model2 = Attribute(**attribute_model_dict)

        # Verify the model instances are equivalent
        assert attribute_model == attribute_model2

        # Convert model instance back to dict and verify no loss of data
        attribute_model_json2 = attribute_model.to_dict()
        assert attribute_model_json2 == attribute_model_json


class TestModel_InviteUser:
    """
    Test Class for InviteUser
    """

    def test_invite_user_serialization(self):
        """
        Test serialization/deserialization for InviteUser
        """

        # Construct a json representation of a InviteUser model
        invite_user_model_json = {}
        invite_user_model_json['email'] = 'testString'
        invite_user_model_json['account_role'] = 'testString'

        # Construct a model instance of InviteUser by calling from_dict on the json representation
        invite_user_model = InviteUser.from_dict(invite_user_model_json)
        assert invite_user_model != False

        # Construct a model instance of InviteUser by calling from_dict on the json representation
        invite_user_model_dict = InviteUser.from_dict(invite_user_model_json).__dict__
        invite_user_model2 = InviteUser(**invite_user_model_dict)

        # Verify the model instances are equivalent
        assert invite_user_model == invite_user_model2

        # Convert model instance back to dict and verify no loss of data
        invite_user_model_json2 = invite_user_model.to_dict()
        assert invite_user_model_json2 == invite_user_model_json


class TestModel_InviteUserIamPolicy:
    """
    Test Class for InviteUserIamPolicy
    """

    def test_invite_user_iam_policy_serialization(self):
        """
        Test serialization/deserialization for InviteUserIamPolicy
        """

        # Construct dict forms of any model objects needed in order to build this model.

        role_model = {}  # Role
        role_model['role_id'] = 'testString'

        attribute_model = {}  # Attribute
        attribute_model['name'] = 'testString'
        attribute_model['value'] = 'testString'

        resource_model = {}  # Resource
        resource_model['attributes'] = [attribute_model]

        # Construct a json representation of a InviteUserIamPolicy model
        invite_user_iam_policy_model_json = {}
        invite_user_iam_policy_model_json['type'] = 'testString'
        invite_user_iam_policy_model_json['roles'] = [role_model]
        invite_user_iam_policy_model_json['resources'] = [resource_model]

        # Construct a model instance of InviteUserIamPolicy by calling from_dict on the json representation
        invite_user_iam_policy_model = InviteUserIamPolicy.from_dict(invite_user_iam_policy_model_json)
        assert invite_user_iam_policy_model != False

        # Construct a model instance of InviteUserIamPolicy by calling from_dict on the json representation
        invite_user_iam_policy_model_dict = InviteUserIamPolicy.from_dict(invite_user_iam_policy_model_json).__dict__
        invite_user_iam_policy_model2 = InviteUserIamPolicy(**invite_user_iam_policy_model_dict)

        # Verify the model instances are equivalent
        assert invite_user_iam_policy_model == invite_user_iam_policy_model2

        # Convert model instance back to dict and verify no loss of data
        invite_user_iam_policy_model_json2 = invite_user_iam_policy_model.to_dict()
        assert invite_user_iam_policy_model_json2 == invite_user_iam_policy_model_json


class TestModel_Resource:
    """
    Test Class for Resource
    """

    def test_resource_serialization(self):
        """
        Test serialization/deserialization for Resource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attribute_model = {}  # Attribute
        attribute_model['name'] = 'testString'
        attribute_model['value'] = 'testString'

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['attributes'] = [attribute_model]

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


class TestModel_Role:
    """
    Test Class for Role
    """

    def test_role_serialization(self):
        """
        Test serialization/deserialization for Role
        """

        # Construct a json representation of a Role model
        role_model_json = {}
        role_model_json['role_id'] = 'testString'

        # Construct a model instance of Role by calling from_dict on the json representation
        role_model = Role.from_dict(role_model_json)
        assert role_model != False

        # Construct a model instance of Role by calling from_dict on the json representation
        role_model_dict = Role.from_dict(role_model_json).__dict__
        role_model2 = Role(**role_model_dict)

        # Verify the model instances are equivalent
        assert role_model == role_model2

        # Convert model instance back to dict and verify no loss of data
        role_model_json2 = role_model.to_dict()
        assert role_model_json2 == role_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
