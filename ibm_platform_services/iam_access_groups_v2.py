# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.34.1-ad041667-20210617-195430
 
"""
The IAM Access Groups API allows for the management of access groups (Create, Read,
Update, Delete) as well as the management of memberships and rules within the group
container.
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class IamAccessGroupsV2(BaseService):
    """The iam-access-groups V2 service."""

    DEFAULT_SERVICE_URL = 'https://iam.cloud.ibm.com/v2'
    DEFAULT_SERVICE_NAME = 'iam_access_groups'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'IamAccessGroupsV2':
        """
        Return a new client for the iam-access-groups service using the specified
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
        Construct a new client for the iam-access-groups service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Access group operations
    #########################


    def create_access_group(self,
        account_id: str,
        name: str,
        *,
        description: str = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create an access group.

        Create a new access group to assign multiple users and service ids to multiple
        policies. The group will be created in the account specified by the `account_id`
        parameter. The group name is a required field, but a description is optional.
        Because the group's name does not have to be unique, it is possible to create
        multiple groups with the same name.

        :param str account_id: Account ID of the API keys(s) to query. If a service
               IAM ID is specified in iam_id then account_id must match the account of the
               IAM ID. If a user IAM ID is specified in iam_id then then account_id must
               match the account of the Authorization token.
        :param str name: Assign the specified name to the access group. This field
               is case-insensitive and has a limit of 100 characters. The group name has
               to be unique within an account.
        :param str description: (optional) Assign an optional description for the
               access group. This field has a limit of 250 characters.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Group` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_access_group')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id
        }

        data = {
            'name': name,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/groups'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def list_access_groups(self,
        account_id: str,
        *,
        transaction_id: str = None,
        iam_id: str = None,
        limit: int = None,
        offset: int = None,
        sort: str = None,
        show_federated: bool = None,
        hide_public_access: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List access groups.

        This API lists access groups within an account. Parameters for pagination and
        sorting can be used to filter the results. The `account_id` query parameter
        determines which account to retrieve groups from. Only the groups you have access
        to are returned (either because of a policy on a specific group or account level
        access (admin, editor, or viewer)). There may be more groups in the account that
        aren't shown if you lack the aforementioned permissions.

        :param str account_id: Account ID of the API keys(s) to query. If a service
               IAM ID is specified in iam_id then account_id must match the account of the
               IAM ID. If a user IAM ID is specified in iam_id then then account_id must
               match the account of the Authorization token.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param str iam_id: (optional) Return groups for member id (IBMid or Service
               Id).
        :param int limit: (optional) Return up to this limit of results where limit
               is between 0 and 100.
        :param int offset: (optional) The offset of the first result item to be
               returned.
        :param str sort: (optional) Sort the results by id, name, description, or
               is_federated flag.
        :param bool show_federated: (optional) If show_federated is true, each
               group listed will return an is_federated value that is set to true if rules
               exist for the group.
        :param bool hide_public_access: (optional) If hide_public_access is true,
               do not include the Public Access Group in the results.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GroupsList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_access_groups')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'iam_id': iam_id,
            'limit': limit,
            'offset': offset,
            'sort': sort,
            'show_federated': show_federated,
            'hide_public_access': hide_public_access
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/groups'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_access_group(self,
        access_group_id: str,
        *,
        transaction_id: str = None,
        show_federated: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get an access group.

        Retrieve an access group by its `access_group_id`. Only the groups data is
        returned (group name, description, account_id, ...), not membership or rule
        information. A revision number is returned in the `ETag` header, which is needed
        when updating the access group.

        :param str access_group_id: The access group identifier.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param bool show_federated: (optional) If show_federated is true, the group
               will return an is_federated value that is set to true if rules exist for
               the group.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Group` object
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_access_group')
        headers.update(sdk_headers)

        params = {
            'show_federated': show_federated
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['access_group_id']
        path_param_values = self.encode_path_vars(access_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def update_access_group(self,
        access_group_id: str,
        if_match: str,
        *,
        name: str = None,
        description: str = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update an access group.

        Update the group name or description of an existing access group using this API.
        An `If-Match` header must be populated with the group's most recent revision
        number (which can be acquired in the `Get an access group` API).

        :param str access_group_id: The access group identifier.
        :param str if_match: The current revision number of the group being
               updated. This can be found in the Create/Get access group response ETag
               header.
        :param str name: (optional) Assign the specified name to the access group.
               This field is case-insensitive and has a limit of 100 characters. The group
               name has to be unique within an account.
        :param str description: (optional) Assign an optional description for the
               access group. This field has a limit of 250 characters.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Group` object
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        headers = {
            'If-Match': if_match,
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_access_group')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['access_group_id']
        path_param_values = self.encode_path_vars(access_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_access_group(self,
        access_group_id: str,
        *,
        transaction_id: str = None,
        force: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an access group.

        This API is used for deleting an access group. If the access group has no members
        or rules associated with it, the group and its policies will be deleted. However,
        if rules or members do exist, set the `force` parameter to true to delete the
        group as well as its associated members, rules, and policies.

        :param str access_group_id: The access group identifier.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param bool force: (optional) If force is true, delete the group as well as
               its associated members and rules.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_access_group')
        headers.update(sdk_headers)

        params = {
            'force': force
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['access_group_id']
        path_param_values = self.encode_path_vars(access_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Membership operations
    #########################


    def is_member_of_access_group(self,
        access_group_id: str,
        iam_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Check membership in an access group.

        This HEAD operation determines if a given `iam_id` is present in a group. No
        response body is returned with this request. If the membership exists, a `204 - No
        Content` status code is returned. If the membership or the group does not exist, a
        `404 - Not Found` status code is returned.

        :param str access_group_id: The access group identifier.
        :param str iam_id: The IAM identifier.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='is_member_of_access_group')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['access_group_id', 'iam_id']
        path_param_values = self.encode_path_vars(access_group_id, iam_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/members/{iam_id}'.format(**path_param_dict)
        request = self.prepare_request(method='HEAD',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def add_members_to_access_group(self,
        access_group_id: str,
        *,
        members: List['AddGroupMembersRequestMembersItem'] = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Add members to an access group.

        Use this API to add users (`IBMid-...`) or service IDs (`iam-ServiceId-...`) to an
        access group. Any member added gains access to resources defined in the group's
        policies. To revoke a given user's access, simply remove them from the group.
        There is no limit to the number of members one group can have, but each `iam_id`
        can only be added to 50 groups. Additionally, this API request payload can add up
        to 50 members per call.

        :param str access_group_id: The access group identifier.
        :param List[AddGroupMembersRequestMembersItem] members: (optional) An array
               of member objects to add to an access group.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AddGroupMembersResponse` object
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        if members is not None:
            members = [convert_model(x) for x in members]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='add_members_to_access_group')
        headers.update(sdk_headers)

        data = {
            'members': members
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['access_group_id']
        path_param_values = self.encode_path_vars(access_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/members'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_access_group_members(self,
        access_group_id: str,
        *,
        transaction_id: str = None,
        limit: int = None,
        offset: int = None,
        type: str = None,
        verbose: bool = None,
        sort: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List access group members.

        List all members of a given group using this API. Parameters for pagination and
        sorting can be used to filter the results. The most useful query parameter may be
        the `verbose` flag. If `verbose=true`, user and service ID names will be retrieved
        for each `iam_id`. If performance is a concern, leave the `verbose` parameter off
        so that name information does not get retrieved.

        :param str access_group_id: The access group identifier.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param int limit: (optional) Return up to this limit of results where limit
               is between 0 and 100.
        :param int offset: (optional) The offset of the first result item to be
               returned.
        :param str type: (optional) Filter the results by member type.
        :param bool verbose: (optional) Return user's email and name for each user
               id or the name for each service id.
        :param str sort: (optional) If verbose is true, sort the results by id,
               name, or email.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GroupMembersList` object
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_access_group_members')
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'offset': offset,
            'type': type,
            'verbose': verbose,
            'sort': sort
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['access_group_id']
        path_param_values = self.encode_path_vars(access_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/members'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def remove_member_from_access_group(self,
        access_group_id: str,
        iam_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete member from an access group.

        Remove one member from a group using this API. If the operation is successful,
        only a `204 - No Content` response with no body is returned. However, if any error
        occurs, the standard error format will be returned.

        :param str access_group_id: The access group identifier.
        :param str iam_id: The IAM identifier.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='remove_member_from_access_group')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['access_group_id', 'iam_id']
        path_param_values = self.encode_path_vars(access_group_id, iam_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/members/{iam_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def remove_members_from_access_group(self,
        access_group_id: str,
        *,
        members: List[str] = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete members from an access group.

        Remove multiple members from a group using this API. On a successful call, this
        API will always return 207. It is the caller's responsibility to iterate across
        the body to determine successful deletion of each member. This API request payload
        can delete up to 50 members per call.

        :param str access_group_id: The access group identifier.
        :param List[str] members: (optional) The `iam_id`s to remove from the
               access group. This field has a limit of 50 `iam_id`s.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteGroupBulkMembersResponse` object
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='remove_members_from_access_group')
        headers.update(sdk_headers)

        data = {
            'members': members
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['access_group_id']
        path_param_values = self.encode_path_vars(access_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/members/delete'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def remove_member_from_all_access_groups(self,
        account_id: str,
        iam_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete member from all access groups.

        This API removes a given member from every group they are a member of within the
        specified account. By using one operation, you can revoke one member's access to
        all access groups in the account. If a partial failure occurs on deletion, the
        response will be shown in the body.

        :param str account_id: Account ID of the API keys(s) to query. If a service
               IAM ID is specified in iam_id then account_id must match the account of the
               IAM ID. If a user IAM ID is specified in iam_id then then account_id must
               match the account of the Authorization token.
        :param str iam_id: The IAM identifier.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteFromAllGroupsResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='remove_member_from_all_access_groups')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['iam_id']
        path_param_values = self.encode_path_vars(iam_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/_allgroups/members/{iam_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def add_member_to_multiple_access_groups(self,
        account_id: str,
        iam_id: str,
        *,
        type: str = None,
        groups: List[str] = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Add member to multiple access groups.

        This API will add a member to multiple access groups in an account. The limit of
        how many groups that can be in the request is 50. The response is a list of
        results that show if adding the member to each group was successful or not.

        :param str account_id: Account ID of the API keys(s) to query. If a service
               IAM ID is specified in iam_id then account_id must match the account of the
               IAM ID. If a user IAM ID is specified in iam_id then then account_id must
               match the account of the Authorization token.
        :param str iam_id: The IAM identifier.
        :param str type: (optional) The type of the member, must be either "user"
               or "service".
        :param List[str] groups: (optional) The ids of the access groups a given
               member is to be added to.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AddMembershipMultipleGroupsResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='add_member_to_multiple_access_groups')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id
        }

        data = {
            'type': type,
            'groups': groups
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['iam_id']
        path_param_values = self.encode_path_vars(iam_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/_allgroups/members/{iam_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Rule operations
    #########################


    def add_access_group_rule(self,
        access_group_id: str,
        expiration: int,
        realm_name: str,
        conditions: List['RuleConditions'],
        *,
        name: str = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create rule for an access group.

        Rules can be used to dynamically add users to an access group. If a user's SAML
        assertions match the rule's conditions during login, the user will be dynamically
        added to the group. The duration of the user's access to the group is determined
        by the `expiration` field. After access expires, the user will need to log in
        again to regain access. Note that the condition's value field must be a
        stringified JSON value. [Consult this documentation for further explanation of
        dynamic rules.](/docs/iam/accessgroup_rules.html#rules).

        :param str access_group_id: The access group identifier.
        :param int expiration: The number of hours that the rule lives for.
        :param str realm_name: The url of the identity provider.
        :param List[RuleConditions] conditions: A list of conditions the rule must
               satisfy.
        :param str name: (optional) The name of the rule.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        if expiration is None:
            raise ValueError('expiration must be provided')
        if realm_name is None:
            raise ValueError('realm_name must be provided')
        if conditions is None:
            raise ValueError('conditions must be provided')
        conditions = [convert_model(x) for x in conditions]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='add_access_group_rule')
        headers.update(sdk_headers)

        data = {
            'expiration': expiration,
            'realm_name': realm_name,
            'conditions': conditions,
            'name': name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['access_group_id']
        path_param_values = self.encode_path_vars(access_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/rules'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_access_group_rules(self,
        access_group_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List access group rules.

        This API lists all rules in a given access group. Because only a few rules are
        created on each group, there is no pagination or sorting support on this API.

        :param str access_group_id: The access group identifier.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesList` object
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_access_group_rules')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['access_group_id']
        path_param_values = self.encode_path_vars(access_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/rules'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_access_group_rule(self,
        access_group_id: str,
        rule_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get an access group rule.

        Retrieve a rule from an access group. A revision number is returned in the `ETag`
        header, which is needed when updating the rule.

        :param str access_group_id: The access group identifier.
        :param str rule_id: The rule to get.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_access_group_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['access_group_id', 'rule_id']
        path_param_values = self.encode_path_vars(access_group_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def replace_access_group_rule(self,
        access_group_id: str,
        rule_id: str,
        if_match: str,
        expiration: int,
        realm_name: str,
        conditions: List['RuleConditions'],
        *,
        name: str = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Replace an access group rule.

        Update the body of an existing rule using this API. An `If-Match` header must be
        populated with the rule's most recent revision number (which can be acquired in
        the `Get an access group rule` API).

        :param str access_group_id: The access group identifier.
        :param str rule_id: The rule to get.
        :param str if_match: The current revision number of the rule being updated.
               This can be found in the Get Rule response ETag header.
        :param int expiration: The number of hours that the rule lives for.
        :param str realm_name: The url of the identity provider.
        :param List[RuleConditions] conditions: A list of conditions the rule must
               satisfy.
        :param str name: (optional) The name of the rule.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        if expiration is None:
            raise ValueError('expiration must be provided')
        if realm_name is None:
            raise ValueError('realm_name must be provided')
        if conditions is None:
            raise ValueError('conditions must be provided')
        conditions = [convert_model(x) for x in conditions]
        headers = {
            'If-Match': if_match,
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='replace_access_group_rule')
        headers.update(sdk_headers)

        data = {
            'expiration': expiration,
            'realm_name': realm_name,
            'conditions': conditions,
            'name': name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['access_group_id', 'rule_id']
        path_param_values = self.encode_path_vars(access_group_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def remove_access_group_rule(self,
        access_group_id: str,
        rule_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an access group rule.

        Remove one rule from a group using this API. If the operation is successful, only
        a `204 - No Content` response with no body is returned. However, if any error
        occurs, the standard error format will be returned.

        :param str access_group_id: The access group identifier.
        :param str rule_id: The rule to get.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if access_group_id is None:
            raise ValueError('access_group_id must be provided')
        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='remove_access_group_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['access_group_id', 'rule_id']
        path_param_values = self.encode_path_vars(access_group_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/groups/{access_group_id}/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Account settings
    #########################


    def get_account_settings(self,
        account_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get account settings.

        Retrieve the access groups settings for a specific account.

        :param str account_id: Account ID of the API keys(s) to query. If a service
               IAM ID is specified in iam_id then account_id must match the account of the
               IAM ID. If a user IAM ID is specified in iam_id then then account_id must
               match the account of the Authorization token.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountSettings` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_account_settings')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/groups/settings'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def update_account_settings(self,
        account_id: str,
        *,
        public_access_enabled: bool = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update account settings.

        Update the access groups settings for a specific account. Note: When the
        `public_access_enabled` setting is set to false, all policies within the account
        attached to the Public Access group will be deleted. Only set
        `public_access_enabled` to false if you are sure that you want those policies to
        be removed.

        :param str account_id: Account ID of the API keys(s) to query. If a service
               IAM ID is specified in iam_id then account_id must match the account of the
               IAM ID. If a user IAM ID is specified in iam_id then then account_id must
               match the account of the Authorization token.
        :param bool public_access_enabled: (optional) This flag controls the public
               access feature within the account. It is set to true by default. Note: When
               this flag is set to false, all policies within the account attached to the
               Public Access group will be deleted.
        :param str transaction_id: (optional) An optional transaction ID can be
               passed to your request, which can be useful for tracking calls through
               multiple services by using one identifier. The header key must be set to
               Transaction-Id and the value is anything that you choose. If no transaction
               ID is passed in, then a random ID is generated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountSettings` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_account_settings')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id
        }

        data = {
            'public_access_enabled': public_access_enabled
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/groups/settings'
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class AccountSettings():
    """
    The access groups settings for a specific account.

    :attr str account_id: (optional) The account id of the settings being shown.
    :attr datetime last_modified_at: (optional) The timestamp the settings were last
          edited at.
    :attr str last_modified_by_id: (optional) The `iam_id` of the entity that last
          modified the settings.
    :attr bool public_access_enabled: (optional) This flag controls the public
          access feature within the account. It is set to true by default. Note: When this
          flag is set to false, all policies within the account attached to the Public
          Access group will be deleted.
    """

    def __init__(self,
                 *,
                 account_id: str = None,
                 last_modified_at: datetime = None,
                 last_modified_by_id: str = None,
                 public_access_enabled: bool = None) -> None:
        """
        Initialize a AccountSettings object.

        :param str account_id: (optional) The account id of the settings being
               shown.
        :param datetime last_modified_at: (optional) The timestamp the settings
               were last edited at.
        :param str last_modified_by_id: (optional) The `iam_id` of the entity that
               last modified the settings.
        :param bool public_access_enabled: (optional) This flag controls the public
               access feature within the account. It is set to true by default. Note: When
               this flag is set to false, all policies within the account attached to the
               Public Access group will be deleted.
        """
        self.account_id = account_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id
        self.public_access_enabled = public_access_enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountSettings':
        """Initialize a AccountSettings object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'last_modified_at' in _dict:
            args['last_modified_at'] = string_to_datetime(_dict.get('last_modified_at'))
        if 'last_modified_by_id' in _dict:
            args['last_modified_by_id'] = _dict.get('last_modified_by_id')
        if 'public_access_enabled' in _dict:
            args['public_access_enabled'] = _dict.get('public_access_enabled')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'last_modified_at') and self.last_modified_at is not None:
            _dict['last_modified_at'] = datetime_to_string(self.last_modified_at)
        if hasattr(self, 'last_modified_by_id') and self.last_modified_by_id is not None:
            _dict['last_modified_by_id'] = self.last_modified_by_id
        if hasattr(self, 'public_access_enabled') and self.public_access_enabled is not None:
            _dict['public_access_enabled'] = self.public_access_enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountSettings object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AddGroupMembersRequestMembersItem():
    """
    AddGroupMembersRequestMembersItem.

    :attr str iam_id: The IBMid or Service Id of the member.
    :attr str type: The type of the member, must be either "user" or "service".
    """

    def __init__(self,
                 iam_id: str,
                 type: str) -> None:
        """
        Initialize a AddGroupMembersRequestMembersItem object.

        :param str iam_id: The IBMid or Service Id of the member.
        :param str type: The type of the member, must be either "user" or
               "service".
        """
        self.iam_id = iam_id
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddGroupMembersRequestMembersItem':
        """Initialize a AddGroupMembersRequestMembersItem object from a json dictionary."""
        args = {}
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in AddGroupMembersRequestMembersItem JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in AddGroupMembersRequestMembersItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddGroupMembersRequestMembersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddGroupMembersRequestMembersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddGroupMembersRequestMembersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddGroupMembersRequestMembersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AddGroupMembersResponse():
    """
    The members added to an access group.

    :attr List[AddGroupMembersResponseMembersItem] members: (optional) The members
          added to an access group.
    """

    def __init__(self,
                 *,
                 members: List['AddGroupMembersResponseMembersItem'] = None) -> None:
        """
        Initialize a AddGroupMembersResponse object.

        :param List[AddGroupMembersResponseMembersItem] members: (optional) The
               members added to an access group.
        """
        self.members = members

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddGroupMembersResponse':
        """Initialize a AddGroupMembersResponse object from a json dictionary."""
        args = {}
        if 'members' in _dict:
            args['members'] = [AddGroupMembersResponseMembersItem.from_dict(x) for x in _dict.get('members')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddGroupMembersResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'members') and self.members is not None:
            _dict['members'] = [x.to_dict() for x in self.members]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddGroupMembersResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddGroupMembersResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddGroupMembersResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AddGroupMembersResponseMembersItem():
    """
    AddGroupMembersResponseMembersItem.

    :attr str iam_id: (optional) The IBMid or Service Id of the member.
    :attr str type: (optional) The member type - either `user` or `service`.
    :attr datetime created_at: (optional) The timestamp the membership was created
          at.
    :attr str created_by_id: (optional) The `iam_id` of the entity that created the
          membership.
    :attr int status_code: (optional) The outcome of the operation on this `iam_id`.
    :attr str trace: (optional) A transaction-id that can be used for debugging
          purposes.
    :attr List[Error] errors: (optional) A list of errors that occurred when trying
          to add members to a group.
    """

    def __init__(self,
                 *,
                 iam_id: str = None,
                 type: str = None,
                 created_at: datetime = None,
                 created_by_id: str = None,
                 status_code: int = None,
                 trace: str = None,
                 errors: List['Error'] = None) -> None:
        """
        Initialize a AddGroupMembersResponseMembersItem object.

        :param str iam_id: (optional) The IBMid or Service Id of the member.
        :param str type: (optional) The member type - either `user` or `service`.
        :param datetime created_at: (optional) The timestamp the membership was
               created at.
        :param str created_by_id: (optional) The `iam_id` of the entity that
               created the membership.
        :param int status_code: (optional) The outcome of the operation on this
               `iam_id`.
        :param str trace: (optional) A transaction-id that can be used for
               debugging purposes.
        :param List[Error] errors: (optional) A list of errors that occurred when
               trying to add members to a group.
        """
        self.iam_id = iam_id
        self.type = type
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.status_code = status_code
        self.trace = trace
        self.errors = errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddGroupMembersResponseMembersItem':
        """Initialize a AddGroupMembersResponseMembersItem object from a json dictionary."""
        args = {}
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        if 'trace' in _dict:
            args['trace'] = _dict.get('trace')
        if 'errors' in _dict:
            args['errors'] = [Error.from_dict(x) for x in _dict.get('errors')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddGroupMembersResponseMembersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'created_by_id') and self.created_by_id is not None:
            _dict['created_by_id'] = self.created_by_id
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddGroupMembersResponseMembersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddGroupMembersResponseMembersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddGroupMembersResponseMembersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AddMembershipMultipleGroupsResponse():
    """
    The response from the add member to multiple access groups request.

    :attr str iam_id: (optional) The iam_id of a member.
    :attr List[AddMembershipMultipleGroupsResponseGroupsItem] groups: (optional) The
          list of access groups a member was added to.
    """

    def __init__(self,
                 *,
                 iam_id: str = None,
                 groups: List['AddMembershipMultipleGroupsResponseGroupsItem'] = None) -> None:
        """
        Initialize a AddMembershipMultipleGroupsResponse object.

        :param str iam_id: (optional) The iam_id of a member.
        :param List[AddMembershipMultipleGroupsResponseGroupsItem] groups:
               (optional) The list of access groups a member was added to.
        """
        self.iam_id = iam_id
        self.groups = groups

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddMembershipMultipleGroupsResponse':
        """Initialize a AddMembershipMultipleGroupsResponse object from a json dictionary."""
        args = {}
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        if 'groups' in _dict:
            args['groups'] = [AddMembershipMultipleGroupsResponseGroupsItem.from_dict(x) for x in _dict.get('groups')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddMembershipMultipleGroupsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'groups') and self.groups is not None:
            _dict['groups'] = [x.to_dict() for x in self.groups]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddMembershipMultipleGroupsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddMembershipMultipleGroupsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddMembershipMultipleGroupsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AddMembershipMultipleGroupsResponseGroupsItem():
    """
    AddMembershipMultipleGroupsResponseGroupsItem.

    :attr str access_group_id: (optional) The access group that the member is to be
          added to.
    :attr int status_code: (optional) The outcome of the add membership operation on
          this `access_group_id`.
    :attr str trace: (optional) A transaction-id that can be used for debugging
          purposes.
    :attr List[Error] errors: (optional) List of errors encountered when adding
          member to access group.
    """

    def __init__(self,
                 *,
                 access_group_id: str = None,
                 status_code: int = None,
                 trace: str = None,
                 errors: List['Error'] = None) -> None:
        """
        Initialize a AddMembershipMultipleGroupsResponseGroupsItem object.

        :param str access_group_id: (optional) The access group that the member is
               to be added to.
        :param int status_code: (optional) The outcome of the add membership
               operation on this `access_group_id`.
        :param str trace: (optional) A transaction-id that can be used for
               debugging purposes.
        :param List[Error] errors: (optional) List of errors encountered when
               adding member to access group.
        """
        self.access_group_id = access_group_id
        self.status_code = status_code
        self.trace = trace
        self.errors = errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddMembershipMultipleGroupsResponseGroupsItem':
        """Initialize a AddMembershipMultipleGroupsResponseGroupsItem object from a json dictionary."""
        args = {}
        if 'access_group_id' in _dict:
            args['access_group_id'] = _dict.get('access_group_id')
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        if 'trace' in _dict:
            args['trace'] = _dict.get('trace')
        if 'errors' in _dict:
            args['errors'] = [Error.from_dict(x) for x in _dict.get('errors')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddMembershipMultipleGroupsResponseGroupsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'access_group_id') and self.access_group_id is not None:
            _dict['access_group_id'] = self.access_group_id
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddMembershipMultipleGroupsResponseGroupsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddMembershipMultipleGroupsResponseGroupsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddMembershipMultipleGroupsResponseGroupsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteFromAllGroupsResponse():
    """
    The response from the delete member from access groups request.

    :attr str iam_id: (optional) The `iam_id` of the member to removed from groups.
    :attr List[DeleteFromAllGroupsResponseGroupsItem] groups: (optional) The groups
          the member was removed from.
    """

    def __init__(self,
                 *,
                 iam_id: str = None,
                 groups: List['DeleteFromAllGroupsResponseGroupsItem'] = None) -> None:
        """
        Initialize a DeleteFromAllGroupsResponse object.

        :param str iam_id: (optional) The `iam_id` of the member to removed from
               groups.
        :param List[DeleteFromAllGroupsResponseGroupsItem] groups: (optional) The
               groups the member was removed from.
        """
        self.iam_id = iam_id
        self.groups = groups

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFromAllGroupsResponse':
        """Initialize a DeleteFromAllGroupsResponse object from a json dictionary."""
        args = {}
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        if 'groups' in _dict:
            args['groups'] = [DeleteFromAllGroupsResponseGroupsItem.from_dict(x) for x in _dict.get('groups')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFromAllGroupsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'groups') and self.groups is not None:
            _dict['groups'] = [x.to_dict() for x in self.groups]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteFromAllGroupsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFromAllGroupsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFromAllGroupsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteFromAllGroupsResponseGroupsItem():
    """
    DeleteFromAllGroupsResponseGroupsItem.

    :attr str access_group_id: (optional) The access group that the member is to be
          deleted from.
    :attr int status_code: (optional) The outcome of the delete operation on this
          `access_group_id`.
    :attr str trace: (optional) A transaction-id that can be used for debugging
          purposes.
    :attr List[Error] errors: (optional) A list of errors that occurred when trying
          to remove a member from groups.
    """

    def __init__(self,
                 *,
                 access_group_id: str = None,
                 status_code: int = None,
                 trace: str = None,
                 errors: List['Error'] = None) -> None:
        """
        Initialize a DeleteFromAllGroupsResponseGroupsItem object.

        :param str access_group_id: (optional) The access group that the member is
               to be deleted from.
        :param int status_code: (optional) The outcome of the delete operation on
               this `access_group_id`.
        :param str trace: (optional) A transaction-id that can be used for
               debugging purposes.
        :param List[Error] errors: (optional) A list of errors that occurred when
               trying to remove a member from groups.
        """
        self.access_group_id = access_group_id
        self.status_code = status_code
        self.trace = trace
        self.errors = errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFromAllGroupsResponseGroupsItem':
        """Initialize a DeleteFromAllGroupsResponseGroupsItem object from a json dictionary."""
        args = {}
        if 'access_group_id' in _dict:
            args['access_group_id'] = _dict.get('access_group_id')
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        if 'trace' in _dict:
            args['trace'] = _dict.get('trace')
        if 'errors' in _dict:
            args['errors'] = [Error.from_dict(x) for x in _dict.get('errors')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFromAllGroupsResponseGroupsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'access_group_id') and self.access_group_id is not None:
            _dict['access_group_id'] = self.access_group_id
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteFromAllGroupsResponseGroupsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFromAllGroupsResponseGroupsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFromAllGroupsResponseGroupsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteGroupBulkMembersResponse():
    """
    The access group id and the members removed from it.

    :attr str access_group_id: (optional) The access group id.
    :attr List[DeleteGroupBulkMembersResponseMembersItem] members: (optional) The
          `iam_id`s removed from the access group.
    """

    def __init__(self,
                 *,
                 access_group_id: str = None,
                 members: List['DeleteGroupBulkMembersResponseMembersItem'] = None) -> None:
        """
        Initialize a DeleteGroupBulkMembersResponse object.

        :param str access_group_id: (optional) The access group id.
        :param List[DeleteGroupBulkMembersResponseMembersItem] members: (optional)
               The `iam_id`s removed from the access group.
        """
        self.access_group_id = access_group_id
        self.members = members

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteGroupBulkMembersResponse':
        """Initialize a DeleteGroupBulkMembersResponse object from a json dictionary."""
        args = {}
        if 'access_group_id' in _dict:
            args['access_group_id'] = _dict.get('access_group_id')
        if 'members' in _dict:
            args['members'] = [DeleteGroupBulkMembersResponseMembersItem.from_dict(x) for x in _dict.get('members')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteGroupBulkMembersResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'access_group_id') and self.access_group_id is not None:
            _dict['access_group_id'] = self.access_group_id
        if hasattr(self, 'members') and self.members is not None:
            _dict['members'] = [x.to_dict() for x in self.members]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteGroupBulkMembersResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteGroupBulkMembersResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteGroupBulkMembersResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteGroupBulkMembersResponseMembersItem():
    """
    DeleteGroupBulkMembersResponseMembersItem.

    :attr str iam_id: (optional) The `iam_id` to be deleted.
    :attr str trace: (optional) A transaction-id that can be used for debugging
          purposes.
    :attr int status_code: (optional) The outcome of the delete membership operation
          on this `access_group_id`.
    :attr List[Error] errors: (optional) A list of errors that occurred when trying
          to remove a member from groups.
    """

    def __init__(self,
                 *,
                 iam_id: str = None,
                 trace: str = None,
                 status_code: int = None,
                 errors: List['Error'] = None) -> None:
        """
        Initialize a DeleteGroupBulkMembersResponseMembersItem object.

        :param str iam_id: (optional) The `iam_id` to be deleted.
        :param str trace: (optional) A transaction-id that can be used for
               debugging purposes.
        :param int status_code: (optional) The outcome of the delete membership
               operation on this `access_group_id`.
        :param List[Error] errors: (optional) A list of errors that occurred when
               trying to remove a member from groups.
        """
        self.iam_id = iam_id
        self.trace = trace
        self.status_code = status_code
        self.errors = errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteGroupBulkMembersResponseMembersItem':
        """Initialize a DeleteGroupBulkMembersResponseMembersItem object from a json dictionary."""
        args = {}
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        if 'trace' in _dict:
            args['trace'] = _dict.get('trace')
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        if 'errors' in _dict:
            args['errors'] = [Error.from_dict(x) for x in _dict.get('errors')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteGroupBulkMembersResponseMembersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteGroupBulkMembersResponseMembersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteGroupBulkMembersResponseMembersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteGroupBulkMembersResponseMembersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Error():
    """
    Error contains the code and message for an error returned to the user code is a string
    identifying the problem, examples "missing_field", "reserved_value" message is a
    string explaining the solution to the problem that was encountered.

    :attr str code: (optional) A human-readable error code represented by a snake
          case string.
    :attr str message: (optional) A specific error message that details the issue or
          an action to take.
    """

    def __init__(self,
                 *,
                 code: str = None,
                 message: str = None) -> None:
        """
        Initialize a Error object.

        :param str code: (optional) A human-readable error code represented by a
               snake case string.
        :param str message: (optional) A specific error message that details the
               issue or an action to take.
        """
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Error':
        """Initialize a Error object from a json dictionary."""
        args = {}
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Error object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Error object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Error') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Error') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Group():
    """
    An IAM access group.

    :attr str id: (optional) The group's access group ID.
    :attr str name: (optional) The group's name.
    :attr str description: (optional) The group's description - if defined.
    :attr str account_id: (optional) The account id where the group was created.
    :attr datetime created_at: (optional) The timestamp the group was created at.
    :attr str created_by_id: (optional) The `iam_id` of the entity that created the
          group.
    :attr datetime last_modified_at: (optional) The timestamp the group was last
          edited at.
    :attr str last_modified_by_id: (optional) The `iam_id` of the entity that last
          modified the group name or description.
    :attr str href: (optional) A url to the given group resource.
    :attr bool is_federated: (optional) This is set to true if rules exist for the
          group.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 account_id: str = None,
                 created_at: datetime = None,
                 created_by_id: str = None,
                 last_modified_at: datetime = None,
                 last_modified_by_id: str = None,
                 href: str = None,
                 is_federated: bool = None) -> None:
        """
        Initialize a Group object.

        :param str id: (optional) The group's access group ID.
        :param str name: (optional) The group's name.
        :param str description: (optional) The group's description - if defined.
        :param str account_id: (optional) The account id where the group was
               created.
        :param str href: (optional) A url to the given group resource.
        :param bool is_federated: (optional) This is set to true if rules exist for
               the group.
        """
        self.id = id
        self.name = name
        self.description = description
        self.account_id = account_id
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id
        self.href = href
        self.is_federated = is_federated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Group':
        """Initialize a Group object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        if 'last_modified_at' in _dict:
            args['last_modified_at'] = string_to_datetime(_dict.get('last_modified_at'))
        if 'last_modified_by_id' in _dict:
            args['last_modified_by_id'] = _dict.get('last_modified_by_id')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'is_federated' in _dict:
            args['is_federated'] = _dict.get('is_federated')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Group object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = datetime_to_string(getattr(self, 'created_at'))
        if hasattr(self, 'created_by_id') and getattr(self, 'created_by_id') is not None:
            _dict['created_by_id'] = getattr(self, 'created_by_id')
        if hasattr(self, 'last_modified_at') and getattr(self, 'last_modified_at') is not None:
            _dict['last_modified_at'] = datetime_to_string(getattr(self, 'last_modified_at'))
        if hasattr(self, 'last_modified_by_id') and getattr(self, 'last_modified_by_id') is not None:
            _dict['last_modified_by_id'] = getattr(self, 'last_modified_by_id')
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'is_federated') and self.is_federated is not None:
            _dict['is_federated'] = self.is_federated
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Group object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Group') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Group') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GroupMembersList():
    """
    The members of a group.

    :attr int limit: (optional) Limit on how many items can be returned.
    :attr int offset: (optional) The offset of the first item returned in the result
          set.
    :attr int total_count: (optional) The total number of items that match the
          query.
    :attr HrefStruct first: (optional) A link object.
    :attr HrefStruct previous: (optional) A link object.
    :attr HrefStruct next: (optional) A link object.
    :attr HrefStruct last: (optional) A link object.
    :attr List[ListGroupMembersResponseMember] members: (optional) The members of an
          access group.
    """

    def __init__(self,
                 *,
                 limit: int = None,
                 offset: int = None,
                 total_count: int = None,
                 first: 'HrefStruct' = None,
                 previous: 'HrefStruct' = None,
                 next: 'HrefStruct' = None,
                 last: 'HrefStruct' = None,
                 members: List['ListGroupMembersResponseMember'] = None) -> None:
        """
        Initialize a GroupMembersList object.

        :param int limit: (optional) Limit on how many items can be returned.
        :param int offset: (optional) The offset of the first item returned in the
               result set.
        :param int total_count: (optional) The total number of items that match the
               query.
        :param HrefStruct first: (optional) A link object.
        :param HrefStruct previous: (optional) A link object.
        :param HrefStruct next: (optional) A link object.
        :param HrefStruct last: (optional) A link object.
        :param List[ListGroupMembersResponseMember] members: (optional) The members
               of an access group.
        """
        self.limit = limit
        self.offset = offset
        self.total_count = total_count
        self.first = first
        self.previous = previous
        self.next = next
        self.last = last
        self.members = members

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GroupMembersList':
        """Initialize a GroupMembersList object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'first' in _dict:
            args['first'] = HrefStruct.from_dict(_dict.get('first'))
        if 'previous' in _dict:
            args['previous'] = HrefStruct.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = HrefStruct.from_dict(_dict.get('next'))
        if 'last' in _dict:
            args['last'] = HrefStruct.from_dict(_dict.get('last'))
        if 'members' in _dict:
            args['members'] = [ListGroupMembersResponseMember.from_dict(x) for x in _dict.get('members')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GroupMembersList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'members') and self.members is not None:
            _dict['members'] = [x.to_dict() for x in self.members]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GroupMembersList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GroupMembersList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GroupMembersList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GroupsList():
    """
    The list of access groups returned as part of a response.

    :attr int limit: (optional) Limit on how many items can be returned.
    :attr int offset: (optional) The offset of the first item returned in the result
          set.
    :attr int total_count: (optional) The total number of items that match the
          query.
    :attr HrefStruct first: (optional) A link object.
    :attr HrefStruct previous: (optional) A link object.
    :attr HrefStruct next: (optional) A link object.
    :attr HrefStruct last: (optional) A link object.
    :attr List[Group] groups: (optional) An array of access groups.
    """

    def __init__(self,
                 *,
                 limit: int = None,
                 offset: int = None,
                 total_count: int = None,
                 first: 'HrefStruct' = None,
                 previous: 'HrefStruct' = None,
                 next: 'HrefStruct' = None,
                 last: 'HrefStruct' = None,
                 groups: List['Group'] = None) -> None:
        """
        Initialize a GroupsList object.

        :param int limit: (optional) Limit on how many items can be returned.
        :param int offset: (optional) The offset of the first item returned in the
               result set.
        :param int total_count: (optional) The total number of items that match the
               query.
        :param HrefStruct first: (optional) A link object.
        :param HrefStruct previous: (optional) A link object.
        :param HrefStruct next: (optional) A link object.
        :param HrefStruct last: (optional) A link object.
        :param List[Group] groups: (optional) An array of access groups.
        """
        self.limit = limit
        self.offset = offset
        self.total_count = total_count
        self.first = first
        self.previous = previous
        self.next = next
        self.last = last
        self.groups = groups

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GroupsList':
        """Initialize a GroupsList object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'first' in _dict:
            args['first'] = HrefStruct.from_dict(_dict.get('first'))
        if 'previous' in _dict:
            args['previous'] = HrefStruct.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = HrefStruct.from_dict(_dict.get('next'))
        if 'last' in _dict:
            args['last'] = HrefStruct.from_dict(_dict.get('last'))
        if 'groups' in _dict:
            args['groups'] = [Group.from_dict(x) for x in _dict.get('groups')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GroupsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'groups') and self.groups is not None:
            _dict['groups'] = [x.to_dict() for x in self.groups]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GroupsList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GroupsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GroupsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HrefStruct():
    """
    A link object.

    :attr str href: (optional) A string containing the link’s URL.
    """

    def __init__(self,
                 *,
                 href: str = None) -> None:
        """
        Initialize a HrefStruct object.

        :param str href: (optional) A string containing the link’s URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HrefStruct':
        """Initialize a HrefStruct object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HrefStruct object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HrefStruct object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HrefStruct') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HrefStruct') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListGroupMembersResponseMember():
    """
    A single member of an access group in a list.

    :attr str iam_id: (optional) The IBMid or Service Id of the member.
    :attr str type: (optional) The member type - either `user` or `service`.
    :attr str name: (optional) The user's or service id's name.
    :attr str email: (optional) If the member type is user, this is the user's
          email.
    :attr str description: (optional) If the member type is service, this is the
          service id's description.
    :attr str href: (optional) A url to the given member resource.
    :attr datetime created_at: (optional) The timestamp the membership was created
          at.
    :attr str created_by_id: (optional) The `iam_id` of the entity that created the
          membership.
    """

    def __init__(self,
                 *,
                 iam_id: str = None,
                 type: str = None,
                 name: str = None,
                 email: str = None,
                 description: str = None,
                 href: str = None,
                 created_at: datetime = None,
                 created_by_id: str = None) -> None:
        """
        Initialize a ListGroupMembersResponseMember object.

        :param str iam_id: (optional) The IBMid or Service Id of the member.
        :param str type: (optional) The member type - either `user` or `service`.
        :param str name: (optional) The user's or service id's name.
        :param str email: (optional) If the member type is user, this is the user's
               email.
        :param str description: (optional) If the member type is service, this is
               the service id's description.
        :param str href: (optional) A url to the given member resource.
        :param datetime created_at: (optional) The timestamp the membership was
               created at.
        :param str created_by_id: (optional) The `iam_id` of the entity that
               created the membership.
        """
        self.iam_id = iam_id
        self.type = type
        self.name = name
        self.email = email
        self.description = description
        self.href = href
        self.created_at = created_at
        self.created_by_id = created_by_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListGroupMembersResponseMember':
        """Initialize a ListGroupMembersResponseMember object from a json dictionary."""
        args = {}
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'email' in _dict:
            args['email'] = _dict.get('email')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListGroupMembersResponseMember object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = self.email
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'created_by_id') and self.created_by_id is not None:
            _dict['created_by_id'] = self.created_by_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListGroupMembersResponseMember object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListGroupMembersResponseMember') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListGroupMembersResponseMember') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Rule():
    """
    A rule of an access group.

    :attr str id: (optional) The rule id.
    :attr str name: (optional) The name of the rule.
    :attr int expiration: (optional) The number of hours that the rule lives for
          (Must be between 1 and 24).
    :attr str realm_name: (optional) The url of the identity provider.
    :attr str access_group_id: (optional) The group id that the rule is assigned to.
    :attr str account_id: (optional) The account id that the group is in.
    :attr List[RuleConditions] conditions: (optional) A list of conditions the rule
          must satisfy.
    :attr datetime created_at: (optional) The timestamp the rule was created at.
    :attr str created_by_id: (optional) The `iam_id` of the entity that created the
          rule.
    :attr datetime last_modified_at: (optional) The timestamp the rule was last
          edited at.
    :attr str last_modified_by_id: (optional) The IAM id that last modified the
          rule.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 expiration: int = None,
                 realm_name: str = None,
                 access_group_id: str = None,
                 account_id: str = None,
                 conditions: List['RuleConditions'] = None,
                 created_at: datetime = None,
                 created_by_id: str = None,
                 last_modified_at: datetime = None,
                 last_modified_by_id: str = None) -> None:
        """
        Initialize a Rule object.

        :param str id: (optional) The rule id.
        :param str name: (optional) The name of the rule.
        :param int expiration: (optional) The number of hours that the rule lives
               for (Must be between 1 and 24).
        :param str realm_name: (optional) The url of the identity provider.
        :param str access_group_id: (optional) The group id that the rule is
               assigned to.
        :param str account_id: (optional) The account id that the group is in.
        :param List[RuleConditions] conditions: (optional) A list of conditions the
               rule must satisfy.
        :param datetime created_at: (optional) The timestamp the rule was created
               at.
        :param str created_by_id: (optional) The `iam_id` of the entity that
               created the rule.
        :param datetime last_modified_at: (optional) The timestamp the rule was
               last edited at.
        :param str last_modified_by_id: (optional) The IAM id that last modified
               the rule.
        """
        self.id = id
        self.name = name
        self.expiration = expiration
        self.realm_name = realm_name
        self.access_group_id = access_group_id
        self.account_id = account_id
        self.conditions = conditions
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Rule':
        """Initialize a Rule object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'expiration' in _dict:
            args['expiration'] = _dict.get('expiration')
        if 'realm_name' in _dict:
            args['realm_name'] = _dict.get('realm_name')
        if 'access_group_id' in _dict:
            args['access_group_id'] = _dict.get('access_group_id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'conditions' in _dict:
            args['conditions'] = [RuleConditions.from_dict(x) for x in _dict.get('conditions')]
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        if 'last_modified_at' in _dict:
            args['last_modified_at'] = string_to_datetime(_dict.get('last_modified_at'))
        if 'last_modified_by_id' in _dict:
            args['last_modified_by_id'] = _dict.get('last_modified_by_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Rule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'expiration') and self.expiration is not None:
            _dict['expiration'] = self.expiration
        if hasattr(self, 'realm_name') and self.realm_name is not None:
            _dict['realm_name'] = self.realm_name
        if hasattr(self, 'access_group_id') and self.access_group_id is not None:
            _dict['access_group_id'] = self.access_group_id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'conditions') and self.conditions is not None:
            _dict['conditions'] = [x.to_dict() for x in self.conditions]
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'created_by_id') and self.created_by_id is not None:
            _dict['created_by_id'] = self.created_by_id
        if hasattr(self, 'last_modified_at') and self.last_modified_at is not None:
            _dict['last_modified_at'] = datetime_to_string(self.last_modified_at)
        if hasattr(self, 'last_modified_by_id') and self.last_modified_by_id is not None:
            _dict['last_modified_by_id'] = self.last_modified_by_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Rule object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Rule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Rule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RuleConditions():
    """
    The conditions of a rule.

    :attr str claim: The claim to evaluate against. This will be found in the `ext`
          claims of a user's login request.
    :attr str operator: The operation to perform on the claim.
    :attr str value: The stringified JSON value that the claim is compared to using
          the operator.
    """

    def __init__(self,
                 claim: str,
                 operator: str,
                 value: str) -> None:
        """
        Initialize a RuleConditions object.

        :param str claim: The claim to evaluate against. This will be found in the
               `ext` claims of a user's login request.
        :param str operator: The operation to perform on the claim.
        :param str value: The stringified JSON value that the claim is compared to
               using the operator.
        """
        self.claim = claim
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleConditions':
        """Initialize a RuleConditions object from a json dictionary."""
        args = {}
        if 'claim' in _dict:
            args['claim'] = _dict.get('claim')
        else:
            raise ValueError('Required property \'claim\' not present in RuleConditions JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in RuleConditions JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in RuleConditions JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleConditions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'claim') and self.claim is not None:
            _dict['claim'] = self.claim
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleConditions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleConditions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleConditions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operation to perform on the claim.
        """
        EQUALS = 'EQUALS'
        EQUALS_IGNORE_CASE = 'EQUALS_IGNORE_CASE'
        IN = 'IN'
        NOT_EQUALS_IGNORE_CASE = 'NOT_EQUALS_IGNORE_CASE'
        NOT_EQUALS = 'NOT_EQUALS'
        CONTAINS = 'CONTAINS'


class RulesList():
    """
    A list of rules attached to the access group.

    :attr List[Rule] rules: (optional) A list of rules.
    """

    def __init__(self,
                 *,
                 rules: List['Rule'] = None) -> None:
        """
        Initialize a RulesList object.

        :param List[Rule] rules: (optional) A list of rules.
        """
        self.rules = rules

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RulesList':
        """Initialize a RulesList object from a json dictionary."""
        args = {}
        if 'rules' in _dict:
            args['rules'] = [Rule.from_dict(x) for x in _dict.get('rules')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RulesList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rules') and self.rules is not None:
            _dict['rules'] = [x.to_dict() for x in self.rules]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RulesList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RulesList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RulesList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
