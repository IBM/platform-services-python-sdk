# coding: utf-8

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
Manage lifecycle of your cloud users using User Management APIs.
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class UserManagementV1(BaseService):
    """The User Management V1 service."""

    DEFAULT_SERVICE_URL = 'https://user-management.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'user_management'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'UserManagementV1':
        """
        Return a new client for the User Management service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the User Management service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # userLinkages
    #########################


    def get_user_linkages(self, account_id: str, iam_id: str, **kwargs) -> DetailedResponse:
        """
        Get user linkages.

        Retrieve a user's linkages by user's iam id.

        :param str account_id: The account id.
        :param str iam_id: The user's iam id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UserLinkages` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_user_linkages')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users/{1}/linkages'.format(*self.encode_path_vars(account_id, iam_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_user_linkages(self, account_id: str, iam_id: str, origin: str, id_from_origin: str, **kwargs) -> DetailedResponse:
        """
        create user linkages.

        create a linakge for user by user's iam id.It's a system operation, only with
        System role/policy can invoke this api.

        :param str account_id: The account id.
        :param str iam_id: The user's iam id.
        :param str origin: origin is "IMS" OR "UAA".
        :param str id_from_origin: An alpha-numeric value identifying the origin.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        if origin is None:
            raise ValueError('origin must be provided')
        if id_from_origin is None:
            raise ValueError('id_from_origin must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_user_linkages')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users/{1}/linkages/{2}/{3}'.format(*self.encode_path_vars(account_id, iam_id, origin, id_from_origin))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def remove_user_linkages(self, account_id: str, iam_id: str, origin: str, id_from_origin: str, **kwargs) -> DetailedResponse:
        """
        remove a user linkages.

        remove a user's linkage by user's iam id.It's a system operation, only with System
        role/policy can invoke this api.

        :param str account_id: The account id.
        :param str iam_id: The user's iam id.
        :param str origin: origin is "IMS" OR "UAA".
        :param str id_from_origin: An alpha-numeric value identifying the origin.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        if origin is None:
            raise ValueError('origin must be provided')
        if id_from_origin is None:
            raise ValueError('id_from_origin must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='remove_user_linkages')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users/{1}/linkages/{2}/{3}'.format(*self.encode_path_vars(account_id, iam_id, origin, id_from_origin))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # userProfile
    #########################


    def get_user_profile(self, account_id: str, iam_id: str, *, include_linkages: bool = None, **kwargs) -> DetailedResponse:
        """
        Get user profile.

        Retrieve a user profile by user's iam id or cloudant guid.

        :param str account_id: The account id.
        :param str iam_id: The user's iam id.
        :param bool include_linkages: (optional) Indicate include linkages.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UserProfile` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_user_profile')
        headers.update(sdk_headers)

        params = {
            'include_linkages': include_linkages
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users/{1}'.format(*self.encode_path_vars(account_id, iam_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_user_profile(self, account_id: str, iam_id: str, *, realm: str = None, user_id: str = None, firstname: str = None, lastname: str = None, state: str = None, email: str = None, phonenumber: str = None, altphonenumber: str = None, photo: str = None, **kwargs) -> DetailedResponse:
        """
        create or replace user profile.

        Create a new user or replace user if user already exist by user's iam id.We
        enforce schema validation, some fields are required.Only allow System to call to
        create user and sync user as a whole object. User update need to use Partial
        update user profile.

        :param str account_id: The account id.
        :param str iam_id: The user's iam id.
        :param str realm: (optional) The real of the user, only for new user, this
               field can not be updated.
        :param str user_id: (optional) The user id of the user.
        :param str firstname: (optional) The first name of the user.
        :param str lastname: (optional) The last name of the user.
        :param str state: (optional) The state of the user,Possible values
               "PROCESSING" | "PENDING" | "ACTIVE" | "DISABLED" | "VPN_ONLY".
        :param str email: (optional) The email of the user.
        :param str phonenumber: (optional) The phone number of the user.
        :param str altphonenumber: (optional) The altphonenumber of the user, new
               field to add (optional).
        :param str photo: (optional) The phone link of the user.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_user_profile')
        headers.update(sdk_headers)

        data = {
            'realm': realm,
            'user_id': user_id,
            'firstname': firstname,
            'lastname': lastname,
            'state': state,
            'email': email,
            'phonenumber': phonenumber,
            'altphonenumber': altphonenumber,
            'photo': photo
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users/{1}'.format(*self.encode_path_vars(account_id, iam_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def update_user_profile(self, account_id: str, iam_id: str, *, user_id: str = None, firstname: str = None, lastname: str = None, state: str = None, email: str = None, phonenumber: str = None, altphonenumber: str = None, photo: str = None, **kwargs) -> DetailedResponse:
        """
        partial update user profile.

        Partial update a user's profile by user's iam id.We enforce schema
        validations.User can disable/activate another user, as long as the user has
        user-management access, but user can not change state to "PROCESSING" or
        "PENDING", which are system states.

        :param str account_id: The account id.
        :param str iam_id: The user's iam id.
        :param str user_id: (optional) The user id of the user.
        :param str firstname: (optional) The first name of the user.
        :param str lastname: (optional) The last name of the user.
        :param str state: (optional) The state of the user,Possible values
               "PROCESSING" | "PENDING" | "ACTIVE" | "DISABLED" | "VPN_ONLY".
        :param str email: (optional) The email of the user.
        :param str phonenumber: (optional) The phone number of the user.
        :param str altphonenumber: (optional) The altphonenumber of the user, new
               field to add (optional).
        :param str photo: (optional) The phone link of the user.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_user_profile')
        headers.update(sdk_headers)

        data = {
            'user_id': user_id,
            'firstname': firstname,
            'lastname': lastname,
            'state': state,
            'email': email,
            'phonenumber': phonenumber,
            'altphonenumber': altphonenumber,
            'photo': photo
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users/{1}'.format(*self.encode_path_vars(account_id, iam_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # userSettings
    #########################


    def get_user_settings(self, account_id: str, iam_id: str, **kwargs) -> DetailedResponse:
        """
        Get user settings.

        Retrieve a user's settings by user's iam id.

        :param str account_id: The account id.
        :param str iam_id: The user's iam id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UserSettings` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_user_settings')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users/{1}/settings'.format(*self.encode_path_vars(account_id, iam_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_user_settings(self, account_id: str, iam_id: str, *, language: str = None, notification_language: str = None, allowed_ip_addresses: str = None, self_manage: bool = None, **kwargs) -> DetailedResponse:
        """
        Partial update user settings.

        Update a user's settings by user's iam id.User can update "language",
        "notification_language" and can update "allowed_ip_addresses" if "self_manage" is
        true, but user can not update "allowed_ip_addresses" if "self_manage" is false.And
        Update "self_manage" requires user-management policy.

        :param str account_id: The account id.
        :param str iam_id: The user's iam id.
        :param str language: (optional) UI language, default value empty.
        :param str notification_language: (optional) For email, phone notification,
               default value empty.
        :param str allowed_ip_addresses: (optional) Ip address string use comma to
               separate string.
        :param bool self_manage: (optional) a field set for user be able to self
               manage or not, default false.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_user_settings')
        headers.update(sdk_headers)

        data = {
            'language': language,
            'notification_language': notification_language,
            'allowed_ip_addresses': allowed_ip_addresses,
            'self_manage': self_manage
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users/{1}/settings'.format(*self.encode_path_vars(account_id, iam_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # users
    #########################


    def remove_user_from_account(self, account_id: str, iam_id: str, **kwargs) -> DetailedResponse:
        """
        remove user from account.

        IAM user management policy is required to perform this action.If the caller does
        not have proper IAM user management policy, then if the user is a decendent of the
        caller in IMS heirarchy, then allow as well.Do not support self delete.

        :param str account_id: The account id.
        :param str iam_id: The user's iam id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='remove_user_from_account')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users/{1}'.format(*self.encode_path_vars(account_id, iam_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_users(self, account_id: str, *, ia_mid: str = None, firstname: str = None, lastname: str = None, email: str = None, state: str = None, realm: str = None, **kwargs) -> DetailedResponse:
        """
        Get users.

        Retrieve users in the account.If team directory enabled, return all users in the
        account.If team directory disbaled, and user has IAM viewer role on
        user-management service, then return all users in the account.If team directory
        disabled, and user does not have IAM viewer role on user-management service, then
        return only current user.

        :param str account_id: The account id.
        :param str ia_mid: (optional) The realm of the user.
        :param str firstname: (optional) The firstname of user.
        :param str lastname: (optional) The lastname of user.
        :param str email: (optional) The email of user.
        :param str state: (optional) The state.
        :param str realm: (optional) The realm of the user.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UserList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_users')
        headers.update(sdk_headers)

        params = {
            'IAMid': ia_mid,
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'state': state,
            'realm': realm
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users'.format(*self.encode_path_vars(account_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def invite_users(self, account_id: str, *, users: List['InviteUser'] = None, **kwargs) -> DetailedResponse:
        """
        Invite users.

        Invite users to the account.

        :param str account_id: The account id.
        :param List[InviteUser] users: (optional) list of users to be invited.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if users is not None:
            users = [ convert_model(x) for x in users ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='invite_users')
        headers.update(sdk_headers)

        data = {
            'users': users
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/users'.format(*self.encode_path_vars(account_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_ims_users(self, account_id: str, *, ia_mid: str = None, firstname: str = None, lastname: str = None, email: str = None, state: str = None, **kwargs) -> DetailedResponse:
        """
        Get users in account and filtering results based on IMS user heirarchy.

        Retrieve a user profile by user's iam id or cloudant guid.

        :param str account_id: The account id.
        :param str ia_mid: (optional) The realm of the user.
        :param str firstname: (optional) The firstname of user.
        :param str lastname: (optional) The lastname of user.
        :param str email: (optional) The email of user.
        :param str state: (optional) The state.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UserList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_ims_users')
        headers.update(sdk_headers)

        params = {
            'IAMid': ia_mid,
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'state': state
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/ims/users'.format(*self.encode_path_vars(account_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_cf_users(self, account_id: str, organization_guid: str, **kwargs) -> DetailedResponse:
        """
        Get users.

        Get CF organizations Users in account organization.

        :param str account_id: The account id.
        :param str organization_guid: The organization id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UserList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if organization_guid is None:
            raise ValueError('organization_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_cf_users')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/accounts/{0}/organizations/{1}/users'.format(*self.encode_path_vars(account_id, organization_guid))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class UserLinkages():
    """
    The returned list of user linkages.

    :attr List[Linkage] linkages: (optional) shows the origin of the user and id of
          that origin.
    """

    def __init__(self, *, linkages: List['Linkage'] = None) -> None:
        """
        Initialize a UserLinkages object.

        :param List[Linkage] linkages: (optional) shows the origin of the user and
               id of that origin.
        """
        self.linkages = linkages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UserLinkages':
        """Initialize a UserLinkages object from a json dictionary."""
        args = {}
        if 'linkages' in _dict:
            args['linkages'] = [Linkage.from_dict(x) for x in _dict.get('linkages')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UserLinkages object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'linkages') and self.linkages is not None:
            _dict['linkages'] = [x.to_dict() for x in self.linkages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UserLinkages object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UserLinkages') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UserLinkages') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UserList():
    """
    The returned list of users.

    :attr float total_results: (optional) the number of users returned.
    :attr float limit: (optional) limit of the users returned in a page.
    :attr str first_url: (optional) the first url of the get users api.
    :attr str next_url: (optional) the next url of the get users api.
    :attr List[UserProfile] resources: (optional) shows the users in the account.
    """

    def __init__(self, *, total_results: float = None, limit: float = None, first_url: str = None, next_url: str = None, resources: List['UserProfile'] = None) -> None:
        """
        Initialize a UserList object.

        :param float total_results: (optional) the number of users returned.
        :param float limit: (optional) limit of the users returned in a page.
        :param str first_url: (optional) the first url of the get users api.
        :param str next_url: (optional) the next url of the get users api.
        :param List[UserProfile] resources: (optional) shows the users in the
               account.
        """
        self.total_results = total_results
        self.limit = limit
        self.first_url = first_url
        self.next_url = next_url
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UserList':
        """Initialize a UserList object from a json dictionary."""
        args = {}
        if 'total_results' in _dict:
            args['total_results'] = _dict.get('total_results')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'first_url' in _dict:
            args['first_url'] = _dict.get('first_url')
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        if 'resources' in _dict:
            args['resources'] = [UserProfile.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UserList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_results') and self.total_results is not None:
            _dict['total_results'] = self.total_results
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first_url') and self.first_url is not None:
            _dict['first_url'] = self.first_url
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UserList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UserList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UserList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UserProfile():
    """
    The returned user profile.

    :attr str id: (optional) An alpha-numeric value identifying the user profile.
    :attr str iam_id: (optional) An alpha-numeric value identifying the user's iam
          id.
    :attr str realm: (optional) The value would be IBMid or SL.
    :attr str user_id: (optional) The user id used for login.
    :attr str firstname: (optional) The first name of the user.
    :attr str lastname: (optional) The last name of the user.
    :attr str state: (optional) The state of the user, Possible value:"PROCESSING" |
          "PENDING" | "ACTIVE" | "DISABLED" | "VPN_ONLY".
    :attr str email: (optional) The email of the user.
    :attr str phonenumber: (optional) The phone for the user.
    :attr str altphonenumber: (optional) The altphonenumber of the user.
    :attr str photo: (optional) The link of the photo of user.
    :attr str account_id: (optional) An alpha-numeric value identifying the account
          ID.
    :attr List[Linkage] linkages: (optional) shows the origin of the user and id of
          that origin.
    """

    def __init__(self, *, id: str = None, iam_id: str = None, realm: str = None, user_id: str = None, firstname: str = None, lastname: str = None, state: str = None, email: str = None, phonenumber: str = None, altphonenumber: str = None, photo: str = None, account_id: str = None, linkages: List['Linkage'] = None) -> None:
        """
        Initialize a UserProfile object.

        :param str id: (optional) An alpha-numeric value identifying the user
               profile.
        :param str iam_id: (optional) An alpha-numeric value identifying the user's
               iam id.
        :param str realm: (optional) The value would be IBMid or SL.
        :param str user_id: (optional) The user id used for login.
        :param str firstname: (optional) The first name of the user.
        :param str lastname: (optional) The last name of the user.
        :param str state: (optional) The state of the user, Possible
               value:"PROCESSING" | "PENDING" | "ACTIVE" | "DISABLED" | "VPN_ONLY".
        :param str email: (optional) The email of the user.
        :param str phonenumber: (optional) The phone for the user.
        :param str altphonenumber: (optional) The altphonenumber of the user.
        :param str photo: (optional) The link of the photo of user.
        :param str account_id: (optional) An alpha-numeric value identifying the
               account ID.
        :param List[Linkage] linkages: (optional) shows the origin of the user and
               id of that origin.
        """
        self.id = id
        self.iam_id = iam_id
        self.realm = realm
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.state = state
        self.email = email
        self.phonenumber = phonenumber
        self.altphonenumber = altphonenumber
        self.photo = photo
        self.account_id = account_id
        self.linkages = linkages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UserProfile':
        """Initialize a UserProfile object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        if 'realm' in _dict:
            args['realm'] = _dict.get('realm')
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        if 'firstname' in _dict:
            args['firstname'] = _dict.get('firstname')
        if 'lastname' in _dict:
            args['lastname'] = _dict.get('lastname')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'email' in _dict:
            args['email'] = _dict.get('email')
        if 'phonenumber' in _dict:
            args['phonenumber'] = _dict.get('phonenumber')
        if 'altphonenumber' in _dict:
            args['altphonenumber'] = _dict.get('altphonenumber')
        if 'photo' in _dict:
            args['photo'] = _dict.get('photo')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'linkages' in _dict:
            args['linkages'] = [Linkage.from_dict(x) for x in _dict.get('linkages')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UserProfile object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'realm') and self.realm is not None:
            _dict['realm'] = self.realm
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        if hasattr(self, 'firstname') and self.firstname is not None:
            _dict['firstname'] = self.firstname
        if hasattr(self, 'lastname') and self.lastname is not None:
            _dict['lastname'] = self.lastname
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = self.email
        if hasattr(self, 'phonenumber') and self.phonenumber is not None:
            _dict['phonenumber'] = self.phonenumber
        if hasattr(self, 'altphonenumber') and self.altphonenumber is not None:
            _dict['altphonenumber'] = self.altphonenumber
        if hasattr(self, 'photo') and self.photo is not None:
            _dict['photo'] = self.photo
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'linkages') and self.linkages is not None:
            _dict['linkages'] = [x.to_dict() for x in self.linkages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UserProfile object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UserProfile') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UserProfile') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UserSettings():
    """
    The returned user settings.

    :attr str language: (optional) UI language, default value empty.
    :attr str notification_language: (optional) For email, phone notification,
          default value empty.
    :attr str allowed_ip_addresses: (optional) Ip address string use comma to
          separate string.
    :attr bool self_manage: (optional) a field set for user be able to self manage
          or not, default false.
    """

    def __init__(self, *, language: str = None, notification_language: str = None, allowed_ip_addresses: str = None, self_manage: bool = None) -> None:
        """
        Initialize a UserSettings object.

        :param str language: (optional) UI language, default value empty.
        :param str notification_language: (optional) For email, phone notification,
               default value empty.
        :param str allowed_ip_addresses: (optional) Ip address string use comma to
               separate string.
        :param bool self_manage: (optional) a field set for user be able to self
               manage or not, default false.
        """
        self.language = language
        self.notification_language = notification_language
        self.allowed_ip_addresses = allowed_ip_addresses
        self.self_manage = self_manage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UserSettings':
        """Initialize a UserSettings object from a json dictionary."""
        args = {}
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'notification_language' in _dict:
            args['notification_language'] = _dict.get('notification_language')
        if 'allowed_ip_addresses' in _dict:
            args['allowed_ip_addresses'] = _dict.get('allowed_ip_addresses')
        if 'self_manage' in _dict:
            args['self_manage'] = _dict.get('self_manage')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UserSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'notification_language') and self.notification_language is not None:
            _dict['notification_language'] = self.notification_language
        if hasattr(self, 'allowed_ip_addresses') and self.allowed_ip_addresses is not None:
            _dict['allowed_ip_addresses'] = self.allowed_ip_addresses
        if hasattr(self, 'self_manage') and self.self_manage is not None:
            _dict['self_manage'] = self.self_manage
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UserSettings object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UserSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UserSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class InviteUser():
    """
    Invite a user.

    :attr str email: (optional) An email of the user to be invited.
    """

    def __init__(self, *, email: str = None) -> None:
        """
        Initialize a InviteUser object.

        :param str email: (optional) An email of the user to be invited.
        """
        self.email = email

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InviteUser':
        """Initialize a InviteUser object from a json dictionary."""
        args = {}
        if 'email' in _dict:
            args['email'] = _dict.get('email')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InviteUser object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = self.email
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InviteUser object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InviteUser') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InviteUser') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Linkage():
    """
    Origin of the user and its id.

    :attr str origin: (optional) A string shows the name of the origin.
    :attr str id: (optional) An alpha-numeric value identifying the origin.
    """

    def __init__(self, *, origin: str = None, id: str = None) -> None:
        """
        Initialize a Linkage object.

        :param str origin: (optional) A string shows the name of the origin.
        :param str id: (optional) An alpha-numeric value identifying the origin.
        """
        self.origin = origin
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Linkage':
        """Initialize a Linkage object from a json dictionary."""
        args = {}
        if 'origin' in _dict:
            args['origin'] = _dict.get('origin')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Linkage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'origin') and self.origin is not None:
            _dict['origin'] = self.origin
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Linkage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Linkage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Linkage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


