# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.62.0-a2a22f95-20221115-162524

"""
IAM Policy Management API

API Version: 1.0.1
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


class IamPolicyManagementV1(BaseService):
    """The iam_policy_management V1 service."""

    DEFAULT_SERVICE_URL = 'https://iam.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'iam_policy_management'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'IamPolicyManagementV1':
        """
        Return a new client for the iam_policy_management service using the
               specified parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(authenticator)
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the iam_policy_management service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Policies
    #########################

    def list_policies(
        self,
        account_id: str,
        *,
        accept_language: str = None,
        iam_id: str = None,
        access_group_id: str = None,
        type: str = None,
        service_type: str = None,
        tag_name: str = None,
        tag_value: str = None,
        sort: str = None,
        format: str = None,
        state: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get policies by attributes.

        Get policies and filter by attributes. While managing policies, you may want to
        retrieve policies in the account and filter by attribute values. This can be done
        through query parameters. Currently, only the following attributes are supported:
        account_id, iam_id, access_group_id, type, service_type, sort, format and state.
        account_id is a required query parameter. Only policies that have the specified
        attributes and that the caller has read access to are returned. If the caller does
        not have read access to any policies an empty array is returned.

        :param str account_id: The account GUID in which the policies belong to.
        :param str accept_language: (optional) Language code for translations
               * `default` - English
               * `de` -  German (Standard)
               * `en` - English
               * `es` - Spanish (Spain)
               * `fr` - French (Standard)
               * `it` - Italian (Standard)
               * `ja` - Japanese
               * `ko` - Korean
               * `pt-br` - Portuguese (Brazil)
               * `zh-cn` - Chinese (Simplified, PRC)
               * `zh-tw` - (Chinese, Taiwan).
        :param str iam_id: (optional) Optional IAM ID used to identify the subject.
        :param str access_group_id: (optional) Optional access group id.
        :param str type: (optional) Optional type of policy.
        :param str service_type: (optional) Optional type of service.
        :param str tag_name: (optional) Optional name of the access management tag
               in the policy.
        :param str tag_value: (optional) Optional value of the access management
               tag in the policy.
        :param str sort: (optional) Optional top level policy field to sort
               results. Ascending sort is default. Descending sort available by prepending
               '-' to field. Example '-last_modified_at'.
        :param str format: (optional) Include additional data per policy returned
               * `include_last_permit` - returns details of when the policy last granted a
               permit decision and the number of times it has done so
               * `display` - returns the list of all actions included in each of the
               policy roles.
        :param str state: (optional) The state of the policy.
               * `active` - returns active policies
               * `deleted` - returns non-active policies.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyList` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        headers = {'Accept-Language': accept_language}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_policies'
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'iam_id': iam_id,
            'access_group_id': access_group_id,
            'type': type,
            'service_type': service_type,
            'tag_name': tag_name,
            'tag_value': tag_value,
            'sort': sort,
            'format': format,
            'state': state,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/policies'
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_policy(
        self,
        type: str,
        subjects: List['PolicySubject'],
        roles: List['PolicyRole'],
        resources: List['PolicyResource'],
        *,
        description: str = None,
        accept_language: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a policy.

        Creates a policy to grant access between a subject and a resource. There are two
        types of policies: **access** and **authorization**. A policy administrator might
        want to create an access policy which grants access to a user, service-id, or an
        access group. They might also want to create an authorization policy and setup
        access between services.
        ### Access
        To create an access policy, use **`"type": "access"`** in the body. The possible
        subject attributes are **`iam_id`** and **`access_group_id`**. Use the
        **`iam_id`** subject attribute for assigning access for a user or service-id. Use
        the **`access_group_id`** subject attribute for assigning access for an access
        group. The roles must be a subset of a service's or the platform's supported
        roles. The resource attributes must be a subset of a service's or the platform's
        supported attributes. The policy resource must include either the
        **`serviceType`**, **`serviceName`**, **`resourceGroupId`** or
        **`service_group_id`** attribute and the **`accountId`** attribute.` The IAM
        Services group (`IAM`) is a subset of account management services that includes
        the IAM platform services IAM Identity, IAM Access Management, IAM Users
        Management, IAM Groups, and future IAM services. If the subject is a locked
        service-id, the request will fail.
        ### Authorization
        Authorization policies are supported by services on a case by case basis. Refer to
        service documentation to verify their support of authorization policies. To create
        an authorization policy, use **`"type": "authorization"`** in the body. The
        subject attributes must match the supported authorization subjects of the
        resource. Multiple subject attributes might be provided. The following attributes
        are supported:
          serviceName, serviceInstance, region, resourceType, resource, accountId The
        policy roles must be a subset of the supported authorization roles supported by
        the target service. The user must also have the same level of access or greater to
        the target resource in order to grant the role. The resource attributes must be a
        subset of a service's or the platform's supported attributes. Both the policy
        subject and the policy resource must include the **`serviceName`** and
        **`accountId`** attributes.
        ### Attribute Operators
        Currently, only the `stringEquals` and the `stringMatch` operators are available.
        Resource attributes may support one or both operators. For more information, see
        [how to assign access by using wildcards
        policies](https://cloud.ibm.com/docs/account?topic=account-wildcard).
        ### Attribute Validations
        Policy attribute values must be between 1 and 1,000 characters in length. If
        location related attributes like geography, country, metro, region, satellite, and
        locationvalues are supported by the service, they are validated against Global
        Catalog locations.

        :param str type: The policy type; either 'access' or 'authorization'.
        :param List[PolicySubject] subjects: The subjects associated with a policy.
        :param List[PolicyRole] roles: A set of role cloud resource names (CRNs)
               granted by the policy.
        :param List[PolicyResource] resources: The resources associated with a
               policy.
        :param str description: (optional) Customer-defined description.
        :param str accept_language: (optional) Language code for translations
               * `default` - English
               * `de` -  German (Standard)
               * `en` - English
               * `es` - Spanish (Spain)
               * `fr` - French (Standard)
               * `it` - Italian (Standard)
               * `ja` - Japanese
               * `ko` - Korean
               * `pt-br` - Portuguese (Brazil)
               * `zh-cn` - Chinese (Simplified, PRC)
               * `zh-tw` - (Chinese, Taiwan).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Policy` object
        """

        if type is None:
            raise ValueError('type must be provided')
        if subjects is None:
            raise ValueError('subjects must be provided')
        if roles is None:
            raise ValueError('roles must be provided')
        if resources is None:
            raise ValueError('resources must be provided')
        subjects = [convert_model(x) for x in subjects]
        roles = [convert_model(x) for x in roles]
        resources = [convert_model(x) for x in resources]
        headers = {'Accept-Language': accept_language}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_policy'
        )
        headers.update(sdk_headers)

        data = {'type': type, 'subjects': subjects, 'roles': roles, 'resources': resources, 'description': description}
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/policies'
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def update_policy(
        self,
        policy_id: str,
        if_match: str,
        type: str,
        subjects: List['PolicySubject'],
        roles: List['PolicyRole'],
        resources: List['PolicyResource'],
        *,
        description: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a policy.

        Update a policy to grant access between a subject and a resource. A policy
        administrator might want to update an existing policy. The policy type cannot be
        changed (You cannot change an access policy to an authorization policy).
        ### Access
        To update an access policy, use **`"type": "access"`** in the body. The possible
        subject attributes are **`iam_id`** and **`access_group_id`**. Use the
        **`iam_id`** subject attribute for assigning access for a user or service-id. Use
        the **`access_group_id`** subject attribute for assigning access for an access
        group. The roles must be a subset of a service's or the platform's supported
        roles. The resource attributes must be a subset of a service's or the platform's
        supported attributes. The policy resource must include either the
        **`serviceType`**, **`serviceName`**,  or **`resourceGroupId`** attribute and the
        **`accountId`** attribute.` If the subject is a locked service-id, the request
        will fail.
        ### Authorization
        To update an authorization policy, use **`"type": "authorization"`** in the body.
        The subject attributes must match the supported authorization subjects of the
        resource. Multiple subject attributes might be provided. The following attributes
        are supported:
          serviceName, serviceInstance, region, resourceType, resource, accountId The
        policy roles must be a subset of the supported authorization roles supported by
        the target service. The user must also have the same level of access or greater to
        the target resource in order to grant the role. The resource attributes must be a
        subset of a service's or the platform's supported attributes. Both the policy
        subject and the policy resource must include the **`serviceName`** and
        **`accountId`** attributes.
        ### Attribute Operators
        Currently, only the `stringEquals` and the `stringMatch` operators are available.
        Resource attributes might support one or both operators. For more information, see
        [how to assign access by using wildcards
        policies](https://cloud.ibm.com/docs/account?topic=account-wildcard).
        ### Attribute Validations
        Policy attribute values must be between 1 and 1,000 characters in length. If
        location related attributes like geography, country, metro, region, satellite, and
        locationvalues are supported by the service, they are validated against Global
        Catalog locations.

        :param str policy_id: The policy ID.
        :param str if_match: The revision number for updating a policy and must
               match the ETag value of the existing policy. The Etag can be retrieved
               using the GET /v1/policies/{policy_id} API and looking at the ETag response
               header.
        :param str type: The policy type; either 'access' or 'authorization'.
        :param List[PolicySubject] subjects: The subjects associated with a policy.
        :param List[PolicyRole] roles: A set of role cloud resource names (CRNs)
               granted by the policy.
        :param List[PolicyResource] resources: The resources associated with a
               policy.
        :param str description: (optional) Customer-defined description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Policy` object
        """

        if not policy_id:
            raise ValueError('policy_id must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if subjects is None:
            raise ValueError('subjects must be provided')
        if roles is None:
            raise ValueError('roles must be provided')
        if resources is None:
            raise ValueError('resources must be provided')
        subjects = [convert_model(x) for x in subjects]
        roles = [convert_model(x) for x in roles]
        resources = [convert_model(x) for x in resources]
        headers = {'If-Match': if_match}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_policy'
        )
        headers.update(sdk_headers)

        data = {'type': type, 'subjects': subjects, 'roles': roles, 'resources': resources, 'description': description}
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_id']
        path_param_values = self.encode_path_vars(policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_policy(self, policy_id: str, **kwargs) -> DetailedResponse:
        """
        Retrieve a policy by ID.

        Retrieve a policy by providing a policy ID.

        :param str policy_id: The policy ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Policy` object
        """

        if not policy_id:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_policy'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_id']
        path_param_values = self.encode_path_vars(policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_policy(self, policy_id: str, **kwargs) -> DetailedResponse:
        """
        Delete a policy by ID.

        Delete a policy by providing a policy ID. A policy cannot be deleted if the
        subject ID contains a locked service ID. If the subject of the policy is a locked
        service-id, the request will fail.

        :param str policy_id: The policy ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not policy_id:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_policy'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['policy_id']
        path_param_values = self.encode_path_vars(policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def patch_policy(self, policy_id: str, if_match: str, *, state: str = None, **kwargs) -> DetailedResponse:
        """
        Restore a deleted policy by ID.

        Restore a policy that has recently been deleted. A policy administrator might want
        to restore a deleted policy. To restore a policy, use **`"state": "active"`** in
        the body.

        :param str policy_id: The policy ID.
        :param str if_match: The revision number for updating a policy and must
               match the ETag value of the existing policy. The Etag can be retrieved
               using the GET /v1/policies/{policy_id} API and looking at the ETag response
               header.
        :param str state: (optional) The policy state.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Policy` object
        """

        if not policy_id:
            raise ValueError('policy_id must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        headers = {'If-Match': if_match}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='patch_policy'
        )
        headers.update(sdk_headers)

        data = {'state': state}
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_id']
        path_param_values = self.encode_path_vars(policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Roles
    #########################

    def list_roles(
        self,
        *,
        accept_language: str = None,
        account_id: str = None,
        service_name: str = None,
        source_service_name: str = None,
        policy_type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get roles by filters.

        Get roles based on the filters. While managing roles, you may want to retrieve
        roles and filter by usages. This can be done through query parameters. Currently,
        we only support the following attributes: account_id, service_name,
        source_service_name and policy_type. Only roles that match the filter and that the
        caller has read access to are returned. If the caller does not have read access to
        any roles an empty array is returned.

        :param str accept_language: (optional) Language code for translations
               * `default` - English
               * `de` -  German (Standard)
               * `en` - English
               * `es` - Spanish (Spain)
               * `fr` - French (Standard)
               * `it` - Italian (Standard)
               * `ja` - Japanese
               * `ko` - Korean
               * `pt-br` - Portuguese (Brazil)
               * `zh-cn` - Chinese (Simplified, PRC)
               * `zh-tw` - (Chinese, Taiwan).
        :param str account_id: (optional) Optional account GUID in which the roles
               belong to.
        :param str service_name: (optional) Optional name of IAM enabled service.
        :param str source_service_name: (optional) Optional name of source IAM
               enabled service.
        :param str policy_type: (optional) Optional Policy Type.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RoleList` object
        """

        headers = {'Accept-Language': accept_language}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_roles'
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'service_name': service_name,
            'source_service_name': source_service_name,
            'policy_type': policy_type,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/roles'
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_role(
        self,
        display_name: str,
        actions: List[str],
        name: str,
        account_id: str,
        service_name: str,
        *,
        description: str = None,
        accept_language: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a role.

        Creates a custom role for a specific service within the account. An account owner
        or a user assigned the Administrator role on the Role management service can
        create a custom role. Any number of actions for a single service can be mapped to
        the new role, but there must be at least one service-defined action to
        successfully create the new role.

        :param str display_name: The display name of the role that is shown in the
               console.
        :param List[str] actions: The actions of the role. Please refer to [IAM
               roles and
               actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
        :param str name: The name of the role that is used in the CRN. Can only be
               alphanumeric and has to be capitalized.
        :param str account_id: The account GUID.
        :param str service_name: The service name.
        :param str description: (optional) The description of the role.
        :param str accept_language: (optional) Language code for translations
               * `default` - English
               * `de` -  German (Standard)
               * `en` - English
               * `es` - Spanish (Spain)
               * `fr` - French (Standard)
               * `it` - Italian (Standard)
               * `ja` - Japanese
               * `ko` - Korean
               * `pt-br` - Portuguese (Brazil)
               * `zh-cn` - Chinese (Simplified, PRC)
               * `zh-tw` - (Chinese, Taiwan).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomRole` object
        """

        if display_name is None:
            raise ValueError('display_name must be provided')
        if actions is None:
            raise ValueError('actions must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if account_id is None:
            raise ValueError('account_id must be provided')
        if service_name is None:
            raise ValueError('service_name must be provided')
        headers = {'Accept-Language': accept_language}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_role'
        )
        headers.update(sdk_headers)

        data = {
            'display_name': display_name,
            'actions': actions,
            'name': name,
            'account_id': account_id,
            'service_name': service_name,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/roles'
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def update_role(
        self,
        role_id: str,
        if_match: str,
        *,
        display_name: str = None,
        description: str = None,
        actions: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a role.

        Update a custom role. A role administrator might want to update an existing role
        by updating the display name, description, or the actions that are mapped to the
        role. The name, account_id, and service_name can't be changed.

        :param str role_id: The role ID.
        :param str if_match: The revision number for updating a role and must match
               the ETag value of the existing role. The Etag can be retrieved using the
               GET /v2/roles/{role_id} API and looking at the ETag response header.
        :param str display_name: (optional) The display name of the role that is
               shown in the console.
        :param str description: (optional) The description of the role.
        :param List[str] actions: (optional) The actions of the role. Please refer
               to [IAM roles and
               actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomRole` object
        """

        if not role_id:
            raise ValueError('role_id must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        headers = {'If-Match': if_match}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_role'
        )
        headers.update(sdk_headers)

        data = {'display_name': display_name, 'description': description, 'actions': actions}
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['role_id']
        path_param_values = self.encode_path_vars(role_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/roles/{role_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_role(self, role_id: str, **kwargs) -> DetailedResponse:
        """
        Retrieve a role by ID.

        Retrieve a role by providing a role ID.

        :param str role_id: The role ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomRole` object
        """

        if not role_id:
            raise ValueError('role_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_role'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['role_id']
        path_param_values = self.encode_path_vars(role_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/roles/{role_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_role(self, role_id: str, **kwargs) -> DetailedResponse:
        """
        Delete a role by ID.

        Delete a role by providing a role ID.

        :param str role_id: The role ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not role_id:
            raise ValueError('role_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_role'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['role_id']
        path_param_values = self.encode_path_vars(role_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/roles/{role_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # v2Policies
    #########################

    def v2_list_policies(
        self,
        account_id: str,
        *,
        accept_language: str = None,
        iam_id: str = None,
        access_group_id: str = None,
        type: str = None,
        service_type: str = None,
        service_name: str = None,
        service_group_id: str = None,
        format: str = None,
        state: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get policies by attributes.

        Get policies and filter by attributes. While managing policies, you may want to
        retrieve policies in the account and filter by attribute values. This can be done
        through query parameters. Currently, only the following attributes are supported:
        account_id, iam_id, access_group_id, type, service_type, sort, format and state.
        account_id is a required query parameter. Only policies that have the specified
        attributes and that the caller has read access to are returned. If the caller does
        not have read access to any policies an empty array is returned.

        :param str account_id: The account GUID in which the policies belong to.
        :param str accept_language: (optional) Language code for translations
               * `default` - English
               * `de` -  German (Standard)
               * `en` - English
               * `es` - Spanish (Spain)
               * `fr` - French (Standard)
               * `it` - Italian (Standard)
               * `ja` - Japanese
               * `ko` - Korean
               * `pt-br` - Portuguese (Brazil)
               * `zh-cn` - Chinese (Simplified, PRC)
               * `zh-tw` - (Chinese, Taiwan).
        :param str iam_id: (optional) Optional IAM ID used to identify the subject.
        :param str access_group_id: (optional) Optional access group id.
        :param str type: (optional) Optional type of policy.
        :param str service_type: (optional) Optional type of service.
        :param str service_name: (optional) Optional name of service.
        :param str service_group_id: (optional) Optional ID of service group.
        :param str format: (optional) Include additional data per policy returned
               * `include_last_permit` - returns details of when the policy last granted a
               permit decision and the number of times it has done so
               * `display` - returns the list of all actions included in each of the
               policy roles and translations for all relevant fields.
        :param str state: (optional) The state of the policy.
               * `active` - returns active policies
               * `deleted` - returns non-active policies.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `V2PolicyList` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        headers = {'Accept-Language': accept_language}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='v2_list_policies'
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'iam_id': iam_id,
            'access_group_id': access_group_id,
            'type': type,
            'service_type': service_type,
            'service_name': service_name,
            'service_group_id': service_group_id,
            'format': format,
            'state': state,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/policies'
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def v2_create_policy(
        self,
        type: str,
        control: 'V2PolicyBaseControl',
        *,
        description: str = None,
        subject: 'V2PolicyBaseSubject' = None,
        resource: 'V2PolicyBaseResource' = None,
        pattern: str = None,
        rule: 'V2PolicyBaseRule' = None,
        accept_language: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a policy.

        Creates a policy to grant access between a subject and a resource. Currently,
        there is one type of a v2/policy: **access**. A policy administrator might want to
        create an access policy which grants access to a user, service-id, or an access
        group.
        ### Access
        To create an access policy, use **`"type": "access"`** in the body. The possible
        subject attributes are **`iam_id`** and **`access_group_id`**. Use the
        **`iam_id`** subject attribute for assigning access for a user or service-id. Use
        the **`access_group_id`** subject attribute for assigning access for an access
        group. The roles must be a subset of a service's or the platform's supported
        roles. The resource attributes must be a subset of a service's or the platform's
        supported attributes. The policy resource must include either the
        **`serviceType`**, **`serviceName`**, **`resourceGroupId`** or
        **`service_group_id`** attribute and the **`accountId`** attribute.` The rule
        field can either specify single **`key`**, **`value`**, and **`operator`** or be
        set of **`conditions`** with a combination **`operator`**.  The possible
        combination operator are **`and`** and **`or`**. The rule field has a maximum of 2
        levels of nested **`conditions`**. The operator for a rule can be used to specify
        a time based restriction (e.g., access only during business hours, during the
        Monday-Friday work week). For example, a policy can grant access Monday-Friday,
        9:00am-5:00pm using the following rule:
        ```json
          "rule": {
            "operator": "and",
            "conditions": [{
              "key": "{{environment.attributes.day_of_week}}",
              "operator": "dayOfWeekAnyOf",
              "value": [1, 2, 3, 4, 5]
            },
              "key": "{{environment.attributes.current_time}}",
              "operator": "timeGreaterThanOrEquals",
              "value": "09:00:00+00:00"
            },
              "key": "{{environment.attributes.current_time}}",
              "operator": "timeLessThanOrEquals",
              "value": "17:00:00+00:00"
            }]
          }
        ``` Rules and conditions allow the following operators with **`key`**, **`value`**
        :
        ```
          'timeLessThan', 'timeLessThanOrEquals', 'timeGreaterThan',
        'timeGreaterThanOrEquals',
          'dateLessThan', 'dateLessThanOrEquals', 'dateGreaterThan',
        'dateGreaterThanOrEquals',
          'dateTimeLessThan', 'dateTimeLessThanOrEquals', 'dateTimeGreaterThan',
        'dateTimeGreaterThanOrEquals',
          'dayOfWeekEquals', 'dayOfWeekAnyOf',
          'monthEquals', 'monthAnyOf',
          'dayOfMonthEquals', 'dayOfMonthAnyOf'
        ``` The pattern field can be coupled with a rule that matches the pattern. For the
        business hour rule example above, the **`pattern`** is
        **`"time-based-restrictions:weekly"`**. The IAM Services group (`IAM`) is a subset
        of account management services that includes the IAM platform services IAM
        Identity, IAM Access Management, IAM Users Management, IAM Groups, and future IAM
        services. If the subject is a locked service-id, the request will fail.
        ### Attribute Operators
        Currently, only the `stringEquals`, `stringMatch`, and `stringEquals` operators
        are available. For more information, see [how to assign access by using wildcards
        policies](https://cloud.ibm.com/docs/account?topic=account-wildcard).
        ### Attribute Validations
        Policy attribute values must be between 1 and 1,000 characters in length. If
        location related attributes like geography, country, metro, region, satellite, and
        locationvalues are supported by the service, they are validated against Global
        Catalog locations.

        :param str type: The policy type; either 'access' or 'authorization'.
        :param V2PolicyBaseControl control: Specifies the type of access granted by
               the policy.
        :param str description: (optional) Customer-defined description.
        :param V2PolicyBaseSubject subject: (optional) The subject attributes
               associated with a policy.
        :param V2PolicyBaseResource resource: (optional) The resource attributes
               associated with a policy.
        :param str pattern: (optional) Indicates pattern of rule.
        :param V2PolicyBaseRule rule: (optional) Additional access conditions
               associated with a policy.
        :param str accept_language: (optional) Language code for translations
               * `default` - English
               * `de` -  German (Standard)
               * `en` - English
               * `es` - Spanish (Spain)
               * `fr` - French (Standard)
               * `it` - Italian (Standard)
               * `ja` - Japanese
               * `ko` - Korean
               * `pt-br` - Portuguese (Brazil)
               * `zh-cn` - Chinese (Simplified, PRC)
               * `zh-tw` - (Chinese, Taiwan).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `V2Policy` object
        """

        if type is None:
            raise ValueError('type must be provided')
        if control is None:
            raise ValueError('control must be provided')
        control = convert_model(control)
        if subject is not None:
            subject = convert_model(subject)
        if resource is not None:
            resource = convert_model(resource)
        if rule is not None:
            rule = convert_model(rule)
        headers = {'Accept-Language': accept_language}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='v2_create_policy'
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'control': control,
            'description': description,
            'subject': subject,
            'resource': resource,
            'pattern': pattern,
            'rule': rule,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/policies'
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def v2_update_policy(
        self,
        policy_id: str,
        if_match: str,
        type: str,
        control: 'V2PolicyBaseControl',
        *,
        description: str = None,
        subject: 'V2PolicyBaseSubject' = None,
        resource: 'V2PolicyBaseResource' = None,
        pattern: str = None,
        rule: 'V2PolicyBaseRule' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a policy.

        Update a policy to grant access between a subject and a resource. A policy
        administrator might want to update an existing policy.
        ### Access
        To update an access policy, use **`"type": "access"`** in the body. The possible
        subject attributes are **`iam_id`** and **`access_group_id`**. Use the
        **`iam_id`** subject attribute for assigning access for a user or service-id. Use
        the **`access_group_id`** subject attribute for assigning access for an access
        group. The roles must be a subset of a service's or the platform's supported
        roles. The resource attributes must be a subset of a service's or the platform's
        supported attributes. The policy resource must include either the
        **`serviceType`**, **`serviceName`**,  or **`resourceGroupId`** attribute and the
        **`accountId`** attribute.` The rule field can either specify single **`key`**,
        **`value`**, and **`operator`** or be set of **`conditions`** with a combination
        **`operator`**.  The possible combination operator are **`and`** and **`or`**. The
        rule field has a maximum of 2 levels of nested **`conditions`**. The operator for
        a rule can be used to specify a time based restriction (e.g., access only during
        business hours, during the Monday-Friday work week). For example, a policy can
        grant access Monday-Friday, 9:00am-5:00pm using the following rule:
        ```json
          "rule": {
            "operator": "and",
            "conditions": [{
              "key": "{{environment.attributes.day_of_week}}",
              "operator": "dayOfWeekAnyOf",
              "value": [1, 2, 3, 4, 5]
            },
              "key": "{{environment.attributes.current_time}}",
              "operator": "timeGreaterThanOrEquals",
              "value": "09:00:00+00:00"
            },
              "key": "{{environment.attributes.current_time}}",
              "operator": "timeLessThanOrEquals",
              "value": "17:00:00+00:00"
            }]
          }
        ``` Rules and conditions allow the following operators with **`key`**, **`value`**
        :
        ```
          'timeLessThan', 'timeLessThanOrEquals', 'timeGreaterThan',
        'timeGreaterThanOrEquals',
          'dateLessThan', 'dateLessThanOrEquals', 'dateGreaterThan',
        'dateGreaterThanOrEquals',
          'dateTimeLessThan', 'dateTimeLessThanOrEquals', 'dateTimeGreaterThan',
        'dateTimeGreaterThanOrEquals',
          'dayOfWeekEquals', 'dayOfWeekAnyOf',
          'monthEquals', 'monthAnyOf',
          'dayOfMonthEquals', 'dayOfMonthAnyOf'
        ``` The pattern field can be coupled with a rule that matches the pattern. For the
        business hour rule example above, the **`pattern`** is
        **`"time-based-restrictions:weekly"`**. If the subject is a locked service-id, the
        request will fail.
        ### Attribute Operators
        Currently, only the `stringEquals`, `stringMatch`, and `stringEquals` operators
        are available. For more information, see [how to assign access by using wildcards
        policies](https://cloud.ibm.com/docs/account?topic=account-wildcard).
        ### Attribute Validations
        Policy attribute values must be between 1 and 1,000 characters in length. If
        location related attributes like geography, country, metro, region, satellite, and
        locationvalues are supported by the service, they are validated against Global
        Catalog locations.

        :param str policy_id: The policy ID.
        :param str if_match: The revision number for updating a policy and must
               match the ETag value of the existing policy. The Etag can be retrieved
               using the GET /v1/policies/{policy_id} API and looking at the ETag response
               header.
        :param str type: The policy type; either 'access' or 'authorization'.
        :param V2PolicyBaseControl control: Specifies the type of access granted by
               the policy.
        :param str description: (optional) Customer-defined description.
        :param V2PolicyBaseSubject subject: (optional) The subject attributes
               associated with a policy.
        :param V2PolicyBaseResource resource: (optional) The resource attributes
               associated with a policy.
        :param str pattern: (optional) Indicates pattern of rule.
        :param V2PolicyBaseRule rule: (optional) Additional access conditions
               associated with a policy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `V2Policy` object
        """

        if not policy_id:
            raise ValueError('policy_id must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if control is None:
            raise ValueError('control must be provided')
        control = convert_model(control)
        if subject is not None:
            subject = convert_model(subject)
        if resource is not None:
            resource = convert_model(resource)
        if rule is not None:
            rule = convert_model(rule)
        headers = {'If-Match': if_match}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='v2_update_policy'
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'control': control,
            'description': description,
            'subject': subject,
            'resource': resource,
            'pattern': pattern,
            'rule': rule,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_id']
        path_param_values = self.encode_path_vars(policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def v2_get_policy(self, policy_id: str, **kwargs) -> DetailedResponse:
        """
        Retrieve a policy by ID.

        Retrieve a policy by providing a policy ID.

        :param str policy_id: The policy ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `V2Policy` object
        """

        if not policy_id:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='v2_get_policy'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_id']
        path_param_values = self.encode_path_vars(policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def v2_delete_policy(self, policy_id: str, **kwargs) -> DetailedResponse:
        """
        Delete a policy by ID.

        Delete a policy by providing a policy ID. A policy cannot be deleted if the
        subject ID contains a locked service ID. If the subject of the policy is a locked
        service-id, the request will fail.

        :param str policy_id: The policy ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not policy_id:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='v2_delete_policy'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['policy_id']
        path_param_values = self.encode_path_vars(policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response


class ListPoliciesEnums:
    """
    Enums for list_policies parameters.
    """

    class Type(str, Enum):
        """
        Optional type of policy.
        """

        ACCESS = 'access'
        AUTHORIZATION = 'authorization'

    class ServiceType(str, Enum):
        """
        Optional type of service.
        """

        SERVICE = 'service'
        PLATFORM_SERVICE = 'platform_service'

    class Sort(str, Enum):
        """
        Optional top level policy field to sort results. Ascending sort is default.
        Descending sort available by prepending '-' to field. Example '-last_modified_at'.
        """

        ID = 'id'
        TYPE = 'type'
        HREF = 'href'
        CREATED_AT = 'created_at'
        CREATED_BY_ID = 'created_by_id'
        LAST_MODIFIED_AT = 'last_modified_at'
        LAST_MODIFIED_BY_ID = 'last_modified_by_id'
        STATE = 'state'

    class Format(str, Enum):
        """
        Include additional data per policy returned
        * `include_last_permit` - returns details of when the policy last granted a permit
        decision and the number of times it has done so
        * `display` - returns the list of all actions included in each of the policy
        roles.
        """

        INCLUDE_LAST_PERMIT = 'include_last_permit'
        DISPLAY = 'display'

    class State(str, Enum):
        """
        The state of the policy.
        * `active` - returns active policies
        * `deleted` - returns non-active policies.
        """

        ACTIVE = 'active'
        DELETED = 'deleted'


class V2ListPoliciesEnums:
    """
    Enums for v2_list_policies parameters.
    """

    class Type(str, Enum):
        """
        Optional type of policy.
        """

        ACCESS = 'access'
        AUTHORIZATION = 'authorization'

    class ServiceType(str, Enum):
        """
        Optional type of service.
        """

        SERVICE = 'service'
        PLATFORM_SERVICE = 'platform_service'

    class Format(str, Enum):
        """
        Include additional data per policy returned
        * `include_last_permit` - returns details of when the policy last granted a permit
        decision and the number of times it has done so
        * `display` - returns the list of all actions included in each of the policy roles
        and translations for all relevant fields.
        """

        INCLUDE_LAST_PERMIT = 'include_last_permit'
        DISPLAY = 'display'

    class State(str, Enum):
        """
        The state of the policy.
        * `active` - returns active policies
        * `deleted` - returns non-active policies.
        """

        ACTIVE = 'active'
        DELETED = 'deleted'


##############################################################################
# Models
##############################################################################


class V2PolicyBaseControl:
    """
    Specifies the type of access granted by the policy.

    :attr V2PolicyBaseControlGrant grant: Permission granted by the policy.
    """

    def __init__(self, grant: 'V2PolicyBaseControlGrant') -> None:
        """
        Initialize a V2PolicyBaseControl object.

        :param V2PolicyBaseControlGrant grant: Permission granted by the policy.
        """
        self.grant = grant

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyBaseControl':
        """Initialize a V2PolicyBaseControl object from a json dictionary."""
        args = {}
        if 'grant' in _dict:
            args['grant'] = V2PolicyBaseControlGrant.from_dict(_dict.get('grant'))
        else:
            raise ValueError('Required property \'grant\' not present in V2PolicyBaseControl JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyBaseControl object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'grant') and self.grant is not None:
            if isinstance(self.grant, dict):
                _dict['grant'] = self.grant
            else:
                _dict['grant'] = self.grant.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyBaseControl object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyBaseControl') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyBaseControl') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicyBaseControlGrant:
    """
    Permission granted by the policy.

    :attr List[PolicyRole] roles: A set of role cloud resource names (CRNs) granted
          by the policy.
    """

    def __init__(self, roles: List['PolicyRole']) -> None:
        """
        Initialize a V2PolicyBaseControlGrant object.

        :param List[PolicyRole] roles: A set of role cloud resource names (CRNs)
               granted by the policy.
        """
        self.roles = roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyBaseControlGrant':
        """Initialize a V2PolicyBaseControlGrant object from a json dictionary."""
        args = {}
        if 'roles' in _dict:
            args['roles'] = [PolicyRole.from_dict(v) for v in _dict.get('roles')]
        else:
            raise ValueError('Required property \'roles\' not present in V2PolicyBaseControlGrant JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyBaseControlGrant object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'roles') and self.roles is not None:
            roles_list = []
            for v in self.roles:
                if isinstance(v, dict):
                    roles_list.append(v)
                else:
                    roles_list.append(v.to_dict())
            _dict['roles'] = roles_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyBaseControlGrant object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyBaseControlGrant') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyBaseControlGrant') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicyBaseResource:
    """
    The resource attributes associated with a policy.

    :attr List[V2PolicyAttribute] attributes: (optional) List of resource attributes
          associated with policy/.
    """

    def __init__(self, *, attributes: List['V2PolicyAttribute'] = None) -> None:
        """
        Initialize a V2PolicyBaseResource object.

        :param List[V2PolicyAttribute] attributes: (optional) List of resource
               attributes associated with policy/.
        """
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyBaseResource':
        """Initialize a V2PolicyBaseResource object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [V2PolicyAttribute.from_dict(v) for v in _dict.get('attributes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyBaseResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attributes') and self.attributes is not None:
            attributes_list = []
            for v in self.attributes:
                if isinstance(v, dict):
                    attributes_list.append(v)
                else:
                    attributes_list.append(v.to_dict())
            _dict['attributes'] = attributes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyBaseResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyBaseResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyBaseResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicyBaseRule:
    """
    Additional access conditions associated with a policy.

    """

    def __init__(self) -> None:
        """
        Initialize a V2PolicyBaseRule object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['V2PolicyBaseRuleV2PolicyAttribute', 'V2PolicyBaseRuleV2RuleWithConditions'])
        )
        raise Exception(msg)


class V2PolicyBaseSubject:
    """
    The subject attributes associated with a policy.

    :attr List[V2PolicyAttribute] attributes: (optional) List of subject attributes
          associated with policy/.
    """

    def __init__(self, *, attributes: List['V2PolicyAttribute'] = None) -> None:
        """
        Initialize a V2PolicyBaseSubject object.

        :param List[V2PolicyAttribute] attributes: (optional) List of subject
               attributes associated with policy/.
        """
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyBaseSubject':
        """Initialize a V2PolicyBaseSubject object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [V2PolicyAttribute.from_dict(v) for v in _dict.get('attributes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyBaseSubject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attributes') and self.attributes is not None:
            attributes_list = []
            for v in self.attributes:
                if isinstance(v, dict):
                    attributes_list.append(v)
                else:
                    attributes_list.append(v.to_dict())
            _dict['attributes'] = attributes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyBaseSubject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyBaseSubject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyBaseSubject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CustomRole:
    """
    An additional set of properties associated with a role.

    :attr str id: (optional) The role ID. Composed of hexadecimal characters.
    :attr str display_name: (optional) The display name of the role that is shown in
          the console.
    :attr str description: (optional) The description of the role.
    :attr List[str] actions: (optional) The actions of the role. Please refer to
          [IAM roles and
          actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
    :attr str crn: (optional) The role Cloud Resource Name (CRN). Example CRN:
          'crn:v1:ibmcloud:public:iam-access-management::a/exampleAccountId::customRole:ExampleRoleName'.
    :attr str name: (optional) The name of the role that is used in the CRN. Can
          only be alphanumeric and has to be capitalized.
    :attr str account_id: (optional) The account GUID.
    :attr str service_name: (optional) The service name.
    :attr datetime created_at: (optional) The UTC timestamp when the role was
          created.
    :attr str created_by_id: (optional) The iam ID of the entity that created the
          role.
    :attr datetime last_modified_at: (optional) The UTC timestamp when the role was
          last modified.
    :attr str last_modified_by_id: (optional) The iam ID of the entity that last
          modified the policy.
    :attr str href: (optional) The href link back to the role.
    """

    def __init__(
        self,
        *,
        id: str = None,
        display_name: str = None,
        description: str = None,
        actions: List[str] = None,
        crn: str = None,
        name: str = None,
        account_id: str = None,
        service_name: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
        href: str = None
    ) -> None:
        """
        Initialize a CustomRole object.

        :param str display_name: (optional) The display name of the role that is
               shown in the console.
        :param str description: (optional) The description of the role.
        :param List[str] actions: (optional) The actions of the role. Please refer
               to [IAM roles and
               actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
        :param str name: (optional) The name of the role that is used in the CRN.
               Can only be alphanumeric and has to be capitalized.
        :param str account_id: (optional) The account GUID.
        :param str service_name: (optional) The service name.
        """
        self.id = id
        self.display_name = display_name
        self.description = description
        self.actions = actions
        self.crn = crn
        self.name = name
        self.account_id = account_id
        self.service_name = service_name
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomRole':
        """Initialize a CustomRole object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'actions' in _dict:
            args['actions'] = _dict.get('actions')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
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
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomRole object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = self.actions
        if hasattr(self, 'crn') and getattr(self, 'crn') is not None:
            _dict['crn'] = getattr(self, 'crn')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = datetime_to_string(getattr(self, 'created_at'))
        if hasattr(self, 'created_by_id') and getattr(self, 'created_by_id') is not None:
            _dict['created_by_id'] = getattr(self, 'created_by_id')
        if hasattr(self, 'last_modified_at') and getattr(self, 'last_modified_at') is not None:
            _dict['last_modified_at'] = datetime_to_string(getattr(self, 'last_modified_at'))
        if hasattr(self, 'last_modified_by_id') and getattr(self, 'last_modified_by_id') is not None:
            _dict['last_modified_by_id'] = getattr(self, 'last_modified_by_id')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomRole object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomRole') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomRole') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Policy:
    """
    The core set of properties associated with a policy.

    :attr str id: (optional) The policy ID.
    :attr str type: (optional) The policy type; either 'access' or 'authorization'.
    :attr str description: (optional) Customer-defined description.
    :attr List[PolicySubject] subjects: (optional) The subjects associated with a
          policy.
    :attr List[PolicyRole] roles: (optional) A set of role cloud resource names
          (CRNs) granted by the policy.
    :attr List[PolicyResource] resources: (optional) The resources associated with a
          policy.
    :attr str href: (optional) The href link back to the policy.
    :attr datetime created_at: (optional) The UTC timestamp when the policy was
          created.
    :attr str created_by_id: (optional) The iam ID of the entity that created the
          policy.
    :attr datetime last_modified_at: (optional) The UTC timestamp when the policy
          was last modified.
    :attr str last_modified_by_id: (optional) The iam ID of the entity that last
          modified the policy.
    :attr str state: (optional) The policy state.
    """

    def __init__(
        self,
        *,
        id: str = None,
        type: str = None,
        description: str = None,
        subjects: List['PolicySubject'] = None,
        roles: List['PolicyRole'] = None,
        resources: List['PolicyResource'] = None,
        href: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
        state: str = None
    ) -> None:
        """
        Initialize a Policy object.

        :param str type: (optional) The policy type; either 'access' or
               'authorization'.
        :param str description: (optional) Customer-defined description.
        :param List[PolicySubject] subjects: (optional) The subjects associated
               with a policy.
        :param List[PolicyRole] roles: (optional) A set of role cloud resource
               names (CRNs) granted by the policy.
        :param List[PolicyResource] resources: (optional) The resources associated
               with a policy.
        :param str state: (optional) The policy state.
        """
        self.id = id
        self.type = type
        self.description = description
        self.subjects = subjects
        self.roles = roles
        self.resources = resources
        self.href = href
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Policy':
        """Initialize a Policy object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'subjects' in _dict:
            args['subjects'] = [PolicySubject.from_dict(v) for v in _dict.get('subjects')]
        if 'roles' in _dict:
            args['roles'] = [PolicyRole.from_dict(v) for v in _dict.get('roles')]
        if 'resources' in _dict:
            args['resources'] = [PolicyResource.from_dict(v) for v in _dict.get('resources')]
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        if 'last_modified_at' in _dict:
            args['last_modified_at'] = string_to_datetime(_dict.get('last_modified_at'))
        if 'last_modified_by_id' in _dict:
            args['last_modified_by_id'] = _dict.get('last_modified_by_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Policy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'subjects') and self.subjects is not None:
            subjects_list = []
            for v in self.subjects:
                if isinstance(v, dict):
                    subjects_list.append(v)
                else:
                    subjects_list.append(v.to_dict())
            _dict['subjects'] = subjects_list
        if hasattr(self, 'roles') and self.roles is not None:
            roles_list = []
            for v in self.roles:
                if isinstance(v, dict):
                    roles_list.append(v)
                else:
                    roles_list.append(v.to_dict())
            _dict['roles'] = roles_list
        if hasattr(self, 'resources') and self.resources is not None:
            resources_list = []
            for v in self.resources:
                if isinstance(v, dict):
                    resources_list.append(v)
                else:
                    resources_list.append(v.to_dict())
            _dict['resources'] = resources_list
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = datetime_to_string(getattr(self, 'created_at'))
        if hasattr(self, 'created_by_id') and getattr(self, 'created_by_id') is not None:
            _dict['created_by_id'] = getattr(self, 'created_by_id')
        if hasattr(self, 'last_modified_at') and getattr(self, 'last_modified_at') is not None:
            _dict['last_modified_at'] = datetime_to_string(getattr(self, 'last_modified_at'))
        if hasattr(self, 'last_modified_by_id') and getattr(self, 'last_modified_by_id') is not None:
            _dict['last_modified_by_id'] = getattr(self, 'last_modified_by_id')
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Policy object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Policy') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Policy') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The policy state.
        """

        ACTIVE = 'active'
        DELETED = 'deleted'


class PolicyList:
    """
    A collection of policies.

    :attr List[Policy] policies: (optional) List of policies.
    """

    def __init__(self, *, policies: List['Policy'] = None) -> None:
        """
        Initialize a PolicyList object.

        :param List[Policy] policies: (optional) List of policies.
        """
        self.policies = policies

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyList':
        """Initialize a PolicyList object from a json dictionary."""
        args = {}
        if 'policies' in _dict:
            args['policies'] = [Policy.from_dict(v) for v in _dict.get('policies')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'policies') and self.policies is not None:
            policies_list = []
            for v in self.policies:
                if isinstance(v, dict):
                    policies_list.append(v)
                else:
                    policies_list.append(v.to_dict())
            _dict['policies'] = policies_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyResource:
    """
    The attributes of the resource. Note that only one resource is allowed in a policy.

    :attr List[ResourceAttribute] attributes: (optional) List of resource
          attributes.
    :attr List[ResourceTag] tags: (optional) List of access management tags.
    """

    def __init__(self, *, attributes: List['ResourceAttribute'] = None, tags: List['ResourceTag'] = None) -> None:
        """
        Initialize a PolicyResource object.

        :param List[ResourceAttribute] attributes: (optional) List of resource
               attributes.
        :param List[ResourceTag] tags: (optional) List of access management tags.
        """
        self.attributes = attributes
        self.tags = tags

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyResource':
        """Initialize a PolicyResource object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [ResourceAttribute.from_dict(v) for v in _dict.get('attributes')]
        if 'tags' in _dict:
            args['tags'] = [ResourceTag.from_dict(v) for v in _dict.get('tags')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attributes') and self.attributes is not None:
            attributes_list = []
            for v in self.attributes:
                if isinstance(v, dict):
                    attributes_list.append(v)
                else:
                    attributes_list.append(v.to_dict())
            _dict['attributes'] = attributes_list
        if hasattr(self, 'tags') and self.tags is not None:
            tags_list = []
            for v in self.tags:
                if isinstance(v, dict):
                    tags_list.append(v)
                else:
                    tags_list.append(v.to_dict())
            _dict['tags'] = tags_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyRole:
    """
    A role associated with a policy.

    :attr str role_id: The role Cloud Resource Name (CRN) granted by the policy.
          Example CRN: 'crn:v1:bluemix:public:iam::::role:Editor'.
    :attr str display_name: (optional) The display name of the role.
    :attr str description: (optional) The description of the role.
    """

    def __init__(self, role_id: str, *, display_name: str = None, description: str = None) -> None:
        """
        Initialize a PolicyRole object.

        :param str role_id: The role Cloud Resource Name (CRN) granted by the
               policy. Example CRN: 'crn:v1:bluemix:public:iam::::role:Editor'.
        """
        self.role_id = role_id
        self.display_name = display_name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyRole':
        """Initialize a PolicyRole object from a json dictionary."""
        args = {}
        if 'role_id' in _dict:
            args['role_id'] = _dict.get('role_id')
        else:
            raise ValueError('Required property \'role_id\' not present in PolicyRole JSON')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyRole object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'role_id') and self.role_id is not None:
            _dict['role_id'] = self.role_id
        if hasattr(self, 'display_name') and getattr(self, 'display_name') is not None:
            _dict['display_name'] = getattr(self, 'display_name')
        if hasattr(self, 'description') and getattr(self, 'description') is not None:
            _dict['description'] = getattr(self, 'description')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyRole object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyRole') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyRole') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicySubject:
    """
    The subject attribute values that must match in order for this policy to apply in a
    permission decision.

    :attr List[SubjectAttribute] attributes: (optional) List of subject attributes.
    """

    def __init__(self, *, attributes: List['SubjectAttribute'] = None) -> None:
        """
        Initialize a PolicySubject object.

        :param List[SubjectAttribute] attributes: (optional) List of subject
               attributes.
        """
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicySubject':
        """Initialize a PolicySubject object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [SubjectAttribute.from_dict(v) for v in _dict.get('attributes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicySubject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attributes') and self.attributes is not None:
            attributes_list = []
            for v in self.attributes:
                if isinstance(v, dict):
                    attributes_list.append(v)
                else:
                    attributes_list.append(v.to_dict())
            _dict['attributes'] = attributes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicySubject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicySubject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicySubject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceAttribute:
    """
    An attribute associated with a resource.

    :attr str name: The name of an attribute.
    :attr str value: The value of an attribute.
    :attr str operator: (optional) The operator of an attribute.
    """

    def __init__(self, name: str, value: str, *, operator: str = None) -> None:
        """
        Initialize a ResourceAttribute object.

        :param str name: The name of an attribute.
        :param str value: The value of an attribute.
        :param str operator: (optional) The operator of an attribute.
        """
        self.name = name
        self.value = value
        self.operator = operator

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceAttribute':
        """Initialize a ResourceAttribute object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ResourceAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ResourceAttribute JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceAttribute object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceTag:
    """
    A tag associated with a resource.

    :attr str name: The name of an access management tag.
    :attr str value: The value of an access management tag.
    :attr str operator: (optional) The operator of an access management tag.
    """

    def __init__(self, name: str, value: str, *, operator: str = None) -> None:
        """
        Initialize a ResourceTag object.

        :param str name: The name of an access management tag.
        :param str value: The value of an access management tag.
        :param str operator: (optional) The operator of an access management tag.
        """
        self.name = name
        self.value = value
        self.operator = operator

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceTag':
        """Initialize a ResourceTag object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ResourceTag JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ResourceTag JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceTag object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceTag object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceTag') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceTag') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Role:
    """
    A role resource.

    :attr str display_name: (optional) The display name of the role that is shown in
          the console.
    :attr str description: (optional) The description of the role.
    :attr List[str] actions: (optional) The actions of the role. Please refer to
          [IAM roles and
          actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
    :attr str crn: (optional) The role Cloud Resource Name (CRN). Example CRN:
          'crn:v1:ibmcloud:public:iam-access-management::a/exampleAccountId::customRole:ExampleRoleName'.
    """

    def __init__(
        self, *, display_name: str = None, description: str = None, actions: List[str] = None, crn: str = None
    ) -> None:
        """
        Initialize a Role object.

        :param str display_name: (optional) The display name of the role that is
               shown in the console.
        :param str description: (optional) The description of the role.
        :param List[str] actions: (optional) The actions of the role. Please refer
               to [IAM roles and
               actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
        """
        self.display_name = display_name
        self.description = description
        self.actions = actions
        self.crn = crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Role':
        """Initialize a Role object from a json dictionary."""
        args = {}
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'actions' in _dict:
            args['actions'] = _dict.get('actions')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Role object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = self.actions
        if hasattr(self, 'crn') and getattr(self, 'crn') is not None:
            _dict['crn'] = getattr(self, 'crn')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Role object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Role') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Role') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoleList:
    """
    A collection of roles returned by the 'list roles' operation.

    :attr List[CustomRole] custom_roles: (optional) List of custom roles.
    :attr List[Role] service_roles: (optional) List of service roles.
    :attr List[Role] system_roles: (optional) List of system roles.
    """

    def __init__(
        self,
        *,
        custom_roles: List['CustomRole'] = None,
        service_roles: List['Role'] = None,
        system_roles: List['Role'] = None
    ) -> None:
        """
        Initialize a RoleList object.

        :param List[CustomRole] custom_roles: (optional) List of custom roles.
        :param List[Role] service_roles: (optional) List of service roles.
        :param List[Role] system_roles: (optional) List of system roles.
        """
        self.custom_roles = custom_roles
        self.service_roles = service_roles
        self.system_roles = system_roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoleList':
        """Initialize a RoleList object from a json dictionary."""
        args = {}
        if 'custom_roles' in _dict:
            args['custom_roles'] = [CustomRole.from_dict(v) for v in _dict.get('custom_roles')]
        if 'service_roles' in _dict:
            args['service_roles'] = [Role.from_dict(v) for v in _dict.get('service_roles')]
        if 'system_roles' in _dict:
            args['system_roles'] = [Role.from_dict(v) for v in _dict.get('system_roles')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoleList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'custom_roles') and self.custom_roles is not None:
            custom_roles_list = []
            for v in self.custom_roles:
                if isinstance(v, dict):
                    custom_roles_list.append(v)
                else:
                    custom_roles_list.append(v.to_dict())
            _dict['custom_roles'] = custom_roles_list
        if hasattr(self, 'service_roles') and self.service_roles is not None:
            service_roles_list = []
            for v in self.service_roles:
                if isinstance(v, dict):
                    service_roles_list.append(v)
                else:
                    service_roles_list.append(v.to_dict())
            _dict['service_roles'] = service_roles_list
        if hasattr(self, 'system_roles') and self.system_roles is not None:
            system_roles_list = []
            for v in self.system_roles:
                if isinstance(v, dict):
                    system_roles_list.append(v)
                else:
                    system_roles_list.append(v.to_dict())
            _dict['system_roles'] = system_roles_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoleList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoleList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoleList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SubjectAttribute:
    """
    An attribute associated with a subject.

    :attr str name: The name of an attribute.
    :attr str value: The value of an attribute.
    """

    def __init__(self, name: str, value: str) -> None:
        """
        Initialize a SubjectAttribute object.

        :param str name: The name of an attribute.
        :param str value: The value of an attribute.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SubjectAttribute':
        """Initialize a SubjectAttribute object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in SubjectAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in SubjectAttribute JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SubjectAttribute object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SubjectAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SubjectAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SubjectAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2Policy:
    """
    The core set of properties associated with a policy.

    :attr str id: (optional) The policy ID.
    :attr str type: The policy type; either 'access' or 'authorization'.
    :attr str description: (optional) Customer-defined description.
    :attr V2PolicyBaseSubject subject: (optional) The subject attributes associated
          with a policy.
    :attr V2PolicyBaseControl control: Specifies the type of access granted by the
          policy.
    :attr V2PolicyBaseResource resource: (optional) The resource attributes
          associated with a policy.
    :attr str pattern: (optional) Indicates pattern of rule.
    :attr V2PolicyBaseRule rule: (optional) Additional access conditions associated
          with a policy.
    :attr str href: (optional) The href link back to the policy.
    :attr datetime created_at: (optional) The UTC timestamp when the policy was
          created.
    :attr str created_by_id: (optional) The iam ID of the entity that created the
          policy.
    :attr datetime last_modified_at: (optional) The UTC timestamp when the policy
          was last modified.
    :attr str last_modified_by_id: (optional) The iam ID of the entity that last
          modified the policy.
    :attr str state: (optional) The policy state.
    """

    def __init__(
        self,
        type: str,
        control: 'V2PolicyBaseControl',
        *,
        id: str = None,
        description: str = None,
        subject: 'V2PolicyBaseSubject' = None,
        resource: 'V2PolicyBaseResource' = None,
        pattern: str = None,
        rule: 'V2PolicyBaseRule' = None,
        href: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
        state: str = None
    ) -> None:
        """
        Initialize a V2Policy object.

        :param str type: The policy type; either 'access' or 'authorization'.
        :param V2PolicyBaseControl control: Specifies the type of access granted by
               the policy.
        :param str description: (optional) Customer-defined description.
        :param V2PolicyBaseSubject subject: (optional) The subject attributes
               associated with a policy.
        :param V2PolicyBaseResource resource: (optional) The resource attributes
               associated with a policy.
        :param str pattern: (optional) Indicates pattern of rule.
        :param V2PolicyBaseRule rule: (optional) Additional access conditions
               associated with a policy.
        :param str state: (optional) The policy state.
        """
        self.id = id
        self.type = type
        self.description = description
        self.subject = subject
        self.control = control
        self.resource = resource
        self.pattern = pattern
        self.rule = rule
        self.href = href
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2Policy':
        """Initialize a V2Policy object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in V2Policy JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'subject' in _dict:
            args['subject'] = V2PolicyBaseSubject.from_dict(_dict.get('subject'))
        if 'control' in _dict:
            args['control'] = V2PolicyBaseControl.from_dict(_dict.get('control'))
        else:
            raise ValueError('Required property \'control\' not present in V2Policy JSON')
        if 'resource' in _dict:
            args['resource'] = V2PolicyBaseResource.from_dict(_dict.get('resource'))
        if 'pattern' in _dict:
            args['pattern'] = _dict.get('pattern')
        if 'rule' in _dict:
            args['rule'] = _dict.get('rule')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        if 'last_modified_at' in _dict:
            args['last_modified_at'] = string_to_datetime(_dict.get('last_modified_at'))
        if 'last_modified_by_id' in _dict:
            args['last_modified_by_id'] = _dict.get('last_modified_by_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2Policy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'subject') and self.subject is not None:
            if isinstance(self.subject, dict):
                _dict['subject'] = self.subject
            else:
                _dict['subject'] = self.subject.to_dict()
        if hasattr(self, 'control') and self.control is not None:
            if isinstance(self.control, dict):
                _dict['control'] = self.control
            else:
                _dict['control'] = self.control.to_dict()
        if hasattr(self, 'resource') and self.resource is not None:
            if isinstance(self.resource, dict):
                _dict['resource'] = self.resource
            else:
                _dict['resource'] = self.resource.to_dict()
        if hasattr(self, 'pattern') and self.pattern is not None:
            _dict['pattern'] = self.pattern
        if hasattr(self, 'rule') and self.rule is not None:
            if isinstance(self.rule, dict):
                _dict['rule'] = self.rule
            else:
                _dict['rule'] = self.rule.to_dict()
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = datetime_to_string(getattr(self, 'created_at'))
        if hasattr(self, 'created_by_id') and getattr(self, 'created_by_id') is not None:
            _dict['created_by_id'] = getattr(self, 'created_by_id')
        if hasattr(self, 'last_modified_at') and getattr(self, 'last_modified_at') is not None:
            _dict['last_modified_at'] = datetime_to_string(getattr(self, 'last_modified_at'))
        if hasattr(self, 'last_modified_by_id') and getattr(self, 'last_modified_by_id') is not None:
            _dict['last_modified_by_id'] = getattr(self, 'last_modified_by_id')
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2Policy object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2Policy') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2Policy') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The policy state.
        """

        ACTIVE = 'active'
        DELETED = 'deleted'


class V2PolicyAttribute:
    """
    Resource/subject attribute associated with policy attributes.

    :attr str key: The name of an attribute.
    :attr str operator: The operator of an attribute.
    :attr object value: The value of an attribute; can be array, boolean, string, or
          integer.
    """

    def __init__(self, key: str, operator: str, value: object) -> None:
        """
        Initialize a V2PolicyAttribute object.

        :param str key: The name of an attribute.
        :param str operator: The operator of an attribute.
        :param object value: The value of an attribute; can be array, boolean,
               string, or integer.
        """
        self.key = key
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyAttribute':
        """Initialize a V2PolicyAttribute object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError('Required property \'key\' not present in V2PolicyAttribute JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in V2PolicyAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in V2PolicyAttribute JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyAttribute object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicyList:
    """
    A collection of policies.

    :attr List[V2Policy] policies: (optional) List of policies.
    """

    def __init__(self, *, policies: List['V2Policy'] = None) -> None:
        """
        Initialize a V2PolicyList object.

        :param List[V2Policy] policies: (optional) List of policies.
        """
        self.policies = policies

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyList':
        """Initialize a V2PolicyList object from a json dictionary."""
        args = {}
        if 'policies' in _dict:
            args['policies'] = [V2Policy.from_dict(v) for v in _dict.get('policies')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'policies') and self.policies is not None:
            policies_list = []
            for v in self.policies:
                if isinstance(v, dict):
                    policies_list.append(v)
                else:
                    policies_list.append(v.to_dict())
            _dict['policies'] = policies_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicyBaseRuleV2PolicyAttribute(V2PolicyBaseRule):
    """
    Resource/subject attribute associated with policy attributes.

    :attr str key: The name of an attribute.
    :attr str operator: The operator of an attribute.
    :attr object value: The value of an attribute; can be array, boolean, string, or
          integer.
    """

    def __init__(self, key: str, operator: str, value: object) -> None:
        """
        Initialize a V2PolicyBaseRuleV2PolicyAttribute object.

        :param str key: The name of an attribute.
        :param str operator: The operator of an attribute.
        :param object value: The value of an attribute; can be array, boolean,
               string, or integer.
        """
        # pylint: disable=super-init-not-called
        self.key = key
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyBaseRuleV2PolicyAttribute':
        """Initialize a V2PolicyBaseRuleV2PolicyAttribute object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError('Required property \'key\' not present in V2PolicyBaseRuleV2PolicyAttribute JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in V2PolicyBaseRuleV2PolicyAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in V2PolicyBaseRuleV2PolicyAttribute JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyBaseRuleV2PolicyAttribute object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyBaseRuleV2PolicyAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyBaseRuleV2PolicyAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyBaseRuleV2PolicyAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicyBaseRuleV2RuleWithConditions(V2PolicyBaseRule):
    """
    Policy rule that has 2 to 10 conditions.

    :attr str operator: Operator to evalute conditions.
    :attr List[V2PolicyAttribute] conditions: List of conditions to associated with
          a policy. Note that conditions can be nested up to 2 levels.
    """

    def __init__(self, operator: str, conditions: List['V2PolicyAttribute']) -> None:
        """
        Initialize a V2PolicyBaseRuleV2RuleWithConditions object.

        :param str operator: Operator to evalute conditions.
        :param List[V2PolicyAttribute] conditions: List of conditions to associated
               with a policy. Note that conditions can be nested up to 2 levels.
        """
        # pylint: disable=super-init-not-called
        self.operator = operator
        self.conditions = conditions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyBaseRuleV2RuleWithConditions':
        """Initialize a V2PolicyBaseRuleV2RuleWithConditions object from a json dictionary."""
        args = {}
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in V2PolicyBaseRuleV2RuleWithConditions JSON')
        if 'conditions' in _dict:
            args['conditions'] = [V2PolicyAttribute.from_dict(v) for v in _dict.get('conditions')]
        else:
            raise ValueError(
                'Required property \'conditions\' not present in V2PolicyBaseRuleV2RuleWithConditions JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyBaseRuleV2RuleWithConditions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'conditions') and self.conditions is not None:
            conditions_list = []
            for v in self.conditions:
                if isinstance(v, dict):
                    conditions_list.append(v)
                else:
                    conditions_list.append(v.to_dict())
            _dict['conditions'] = conditions_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyBaseRuleV2RuleWithConditions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyBaseRuleV2RuleWithConditions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyBaseRuleV2RuleWithConditions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        Operator to evalute conditions.
        """

        AND = 'and'
        OR = 'or'
