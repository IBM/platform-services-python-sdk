# coding: utf-8

# (C) Copyright IBM Corp. 2023.
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

# IBM OpenAPI SDK Code Generator Version: 3.79.0-2eb6af3d-20230905-174838

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
        **kwargs,
    ) -> DetailedResponse:
        """
        Get policies by attributes.

        Get policies and filter by attributes. While managing policies, you might want to
        retrieve policies in the account and filter by attribute values. This can be done
        through query parameters. The following attributes are supported: account_id,
        iam_id, access_group_id, type, service_type, sort, format and state. account_id is
        a required query parameter. Only policies that have the specified attributes and
        that the caller has read access to are returned. If the caller does not have read
        access to any policies an empty array is returned.

        :param str account_id: The account GUID that the policies belong to.
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
        :param str tag_name: (optional) Optional name of the access tag in the
               policy.
        :param str tag_value: (optional) Optional value of the access tag in the
               policy.
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
        :rtype: DetailedResponse with `dict` result representing a `PolicyCollection` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        headers = {
            'Accept-Language': accept_language,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_policies',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

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
        **kwargs,
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
        group. Assign roles that are supported by the service or platform roles. For more
        information, see [IAM roles and
        actions](/docs/account?topic=account-iam-service-roles-actions). Use only the
        resource attributes supported by the service. To view a service's or the
        platform's supported attributes, check the [documentation](/docs?tab=all-docs).
        The policy resource must include either the **`serviceType`**, **`serviceName`**,
        **`resourceGroupId`** or **`service_group_id`** attribute and the **`accountId`**
        attribute. The IAM Services group (`IAM`) is a subset of account management
        services that includes the IAM platform services IAM Identity, IAM Access
        Management, IAM Users Management, IAM Groups, and future IAM services. If the
        subject is a locked service-id, the request will fail.
        ### Authorization
        Authorization policies are supported by services on a case by case basis. Refer to
        service documentation to verify their support of authorization policies. To create
        an authorization policy, use **`"type": "authorization"`** in the body. The
        subject attributes must match the supported authorization subjects of the
        resource. Multiple subject attributes might be provided. The following attributes
        are supported:
          serviceName, serviceInstance, region, resourceType, resource, accountId Assign
        roles that are supported by the service or platform roles. For more information,
        see [IAM roles and
        actions](/docs/account?topic=account-iam-service-roles-actions). The user must
        also have the same level of access or greater to the target resource in order to
        grant the role. Use only the resource attributes supported by the service. To view
        a service's or the platform's supported attributes, check the
        [documentation](/docs?tab=all-docs). Both the policy subject and the policy
        resource must include the **`serviceName`** and **`accountId`** attributes.
        ### Attribute Operators
        Currently, only the `stringEquals` and the `stringMatch` operators are available.
        Resource attributes may support one or both operators. For more information, see
        [Assigning access by using wildcard
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
        headers = {
            'Accept-Language': accept_language,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_policy',
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'subjects': subjects,
            'roles': roles,
            'resources': resources,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/policies'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_policy(
        self,
        policy_id: str,
        if_match: str,
        type: str,
        subjects: List['PolicySubject'],
        roles: List['PolicyRole'],
        resources: List['PolicyResource'],
        *,
        description: str = None,
        **kwargs,
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
        group. Assign roles that are supported by the service or platform roles. For more
        information, see [IAM roles and
        actions](/docs/account?topic=account-iam-service-roles-actions). Use only the
        resource attributes supported by the service. To view a service's or the
        platform's supported attributes, check the [documentation](/docs?tab=all-docs).
        The policy resource must include either the **`serviceType`**, **`serviceName`**,
        or **`resourceGroupId`** attribute and the **`accountId`** attribute.` If the
        subject is a locked service-id, the request will fail.
        ### Authorization
        To update an authorization policy, use **`"type": "authorization"`** in the body.
        The subject attributes must match the supported authorization subjects of the
        resource. Multiple subject attributes might be provided. The following attributes
        are supported:
          serviceName, serviceInstance, region, resourceType, resource, accountId Assign
        roles that are supported by the service or platform roles. For more information,
        see [IAM roles and
        actions](/docs/account?topic=account-iam-service-roles-actions). The user must
        also have the same level of access or greater to the target resource in order to
        grant the role. Use only the resource attributes supported by the service. To view
        a service's or the platform's supported attributes, check the
        [documentation](/docs?tab=all-docs). Both the policy subject and the policy
        resource must include the **`serviceName`** and **`accountId`** attributes.
        ### Attribute Operators
        Currently, only the `stringEquals` and the `stringMatch` operators are available.
        Resource attributes might support one or both operators. For more information, see
        [Assigning access by using wildcard
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
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='replace_policy',
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'subjects': subjects,
            'roles': roles,
            'resources': resources,
            'description': description,
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
        url = '/v1/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_policy(
        self,
        policy_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a policy by ID.

        Retrieve a policy by providing a policy ID.

        :param str policy_id: The policy ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyTemplateMetaData` object
        """

        if not policy_id:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_policy',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_policy(
        self,
        policy_id: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_policy',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['policy_id']
        path_param_values = self.encode_path_vars(policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_policy_state(
        self,
        policy_id: str,
        if_match: str,
        *,
        state: str = None,
        **kwargs,
    ) -> DetailedResponse:
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
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_policy_state',
        )
        headers.update(sdk_headers)

        data = {
            'state': state,
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
        url = '/v1/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

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
        service_group_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get roles by filters.

        Get roles based on the filters. While managing roles, you may want to retrieve
        roles and filter by usages. This can be done through query parameters. Currently,
        we only support the following attributes: account_id, service_name,
        service_group_id, source_service_name and policy_type. Both service_name and
        service_group_id attributes are mutually exclusive. Only roles that match the
        filter and that the caller has read access to are returned. If the caller does not
        have read access to any roles an empty array is returned.

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
        :param str service_group_id: (optional) Optional id of service group.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RoleCollection` object
        """

        headers = {
            'Accept-Language': accept_language,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_roles',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'service_name': service_name,
            'source_service_name': source_service_name,
            'policy_type': policy_type,
            'service_group_id': service_group_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/roles'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

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
        **kwargs,
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
        :param List[str] actions: The actions of the role. For more information,
               see [IAM roles and
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
        headers = {
            'Accept-Language': accept_language,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_role',
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_role(
        self,
        role_id: str,
        if_match: str,
        display_name: str,
        actions: List[str],
        *,
        description: str = None,
        **kwargs,
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
        :param str display_name: The display name of the role that is shown in the
               console.
        :param List[str] actions: The actions of the role. For more information,
               see [IAM roles and
               actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
        :param str description: (optional) The description of the role.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomRole` object
        """

        if not role_id:
            raise ValueError('role_id must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if display_name is None:
            raise ValueError('display_name must be provided')
        if actions is None:
            raise ValueError('actions must be provided')
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='replace_role',
        )
        headers.update(sdk_headers)

        data = {
            'display_name': display_name,
            'actions': actions,
            'description': description,
        }
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
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_role(
        self,
        role_id: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_role',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_role(
        self,
        role_id: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_role',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['role_id']
        path_param_values = self.encode_path_vars(role_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/roles/{role_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # v2/Policies
    #########################

    def list_v2_policies(
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
        sort: str = None,
        format: str = None,
        state: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get policies by attributes.

        Get policies and filter by attributes. While managing policies, you might want to
        retrieve policies in the account and filter by attribute values. This can be done
        through query parameters. The following attributes are supported: account_id,
        iam_id, access_group_id, type, service_type, sort, format and state. account_id is
        a required query parameter. Only policies that have the specified attributes and
        that the caller has read access to are returned. If the caller does not have read
        access to any policies an empty array is returned.

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
        :param str sort: (optional) Optional top level policy field to sort
               results. Ascending sort is default. Descending sort available by prepending
               '-' to field, for example, '-last_modified_at'. Note that last permit
               information is only included when 'format=include_last_permit', for
               example, "format=include_last_permit&sort=last_permit_at" Example fields
               that can be sorted on:
                 - 'id'
                 - 'type'
                 - 'href'
                 - 'created_at'
                 - 'created_by_id'
                 - 'last_modified_at'
                 - 'last_modified_by_id'
                 - 'state'
                 - 'last_permit_at'
                 - 'last_permit_frequency'.
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
        :rtype: DetailedResponse with `dict` result representing a `V2PolicyCollection` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        headers = {
            'Accept-Language': accept_language,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_v2_policies',
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
            'sort': sort,
            'format': format,
            'state': state,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/policies'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_v2_policy(
        self,
        control: 'Control',
        type: str,
        *,
        description: str = None,
        subject: 'V2PolicySubject' = None,
        resource: 'V2PolicyResource' = None,
        pattern: str = None,
        rule: 'V2PolicyRule' = None,
        accept_language: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a policy.

        Creates a policy to grant access between a subject and a resource. Currently,
        there is one type of a v2/policy: **access**. A policy administrator might want to
        create an access policy that grants access to a user, service-id, or an access
        group.
        ### Access
        To create an access policy, use **`"type": "access"`** in the body. The supported
        subject attributes are **`iam_id`** and **`access_group_id`**. Use the
        **`iam_id`** subject attribute to assign access to a user or service-id. Use the
        **`access_group_id`** subject attribute to assign access to an access group.
        Assign roles that are supported by the service or platform roles. For more
        information, see [IAM roles and
        actions](/docs/account?topic=account-iam-service-roles-actions). Use only the
        resource attributes supported by the service. To view a service's or the
        platform's supported attributes, check the [documentation](/docs?tab=all-docs).
        The policy resource must include either the **`serviceType`**, **`serviceName`**,
        **`resourceGroupId`** or **`service_group_id`** attribute and the **`accountId`**
        attribute. In the rule field, you can specify a single condition by using
        **`key`**, **`value`**, and condition **`operator`**, or a set of **`conditions`**
        with a combination **`operator`**. The possible combination operators are
        **`and`** and **`or`**. Combine conditions to specify a time-based restriction
        (e.g., access only during business hours, during the Monday-Friday work week). For
        example, a policy can grant access Monday-Friday, 9:00am-5:00pm using the
        following rule:
        ```json
          "rule": {
            "operator": "and",
            "conditions": [{
              "key": "{{environment.attributes.day_of_week}}",
              "operator": "dayOfWeekAnyOf",
              "value": ["1+00:00", "2+00:00", "3+00:00", "4+00:00", "5+00:00"]
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
        ``` You can use the following operators in the **`key`** and **`value`** pair:
        ```
          'timeLessThan', 'timeLessThanOrEquals', 'timeGreaterThan',
        'timeGreaterThanOrEquals',
          'dateTimeLessThan', 'dateTimeLessThanOrEquals', 'dateTimeGreaterThan',
        'dateTimeGreaterThanOrEquals',
          'dayOfWeekEquals', 'dayOfWeekAnyOf',
        ```
        The pattern field that matches the rule is required when rule is provided. For the
        business hour rule example above, the **`pattern`** is
        **`"time-based-conditions:weekly"`**. For more information, see [Time-based
        conditions
        operators](https://cloud.ibm.com/docs/account?topic=account-iam-condition-properties&interface=ui#policy-condition-properties)
        and
        [Limiting access with time-based
        conditions](https://cloud.ibm.com/docs/account?topic=account-iam-time-based&interface=ui).
        If the subject is a locked service-id, the request will fail.
        ### Attribute Operators
        Currently, only the `stringEquals`, `stringMatch`, and `stringEquals` operators
        are available. For more information, see [Assigning access by using wildcard
        policies](https://cloud.ibm.com/docs/account?topic=account-wildcard).
        ### Attribute Validations
        Policy attribute values must be between 1 and 1,000 characters in length. If
        location related attributes like geography, country, metro, region, satellite, and
        locationvalues are supported by the service, they are validated against Global
        Catalog locations.

        :param Control control: Specifies the type of access granted by the policy.
        :param str type: The policy type; either 'access' or 'authorization'.
        :param str description: (optional) Description of the policy.
        :param V2PolicySubject subject: (optional) The subject attributes for whom
               the policy grants access.
        :param V2PolicyResource resource: (optional) The resource attributes to
               which the policy grants access.
        :param str pattern: (optional) Indicates pattern of rule, either
               'time-based-conditions:once', 'time-based-conditions:weekly:all-day', or
               'time-based-conditions:weekly:custom-hours'.
        :param V2PolicyRule rule: (optional) Additional access conditions
               associated with the policy.
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

        if control is None:
            raise ValueError('control must be provided')
        if type is None:
            raise ValueError('type must be provided')
        control = convert_model(control)
        if subject is not None:
            subject = convert_model(subject)
        if resource is not None:
            resource = convert_model(resource)
        if rule is not None:
            rule = convert_model(rule)
        headers = {
            'Accept-Language': accept_language,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_v2_policy',
        )
        headers.update(sdk_headers)

        data = {
            'control': control,
            'type': type,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_v2_policy(
        self,
        id: str,
        if_match: str,
        control: 'Control',
        type: str,
        *,
        description: str = None,
        subject: 'V2PolicySubject' = None,
        resource: 'V2PolicyResource' = None,
        pattern: str = None,
        rule: 'V2PolicyRule' = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a policy.

        Update a policy to grant access between a subject and a resource. A policy
        administrator might want to update an existing policy.
        ### Access
        To create an access policy, use **`"type": "access"`** in the body. The supported
        subject attributes are **`iam_id`** and **`access_group_id`**. Use the
        **`iam_id`** subject attribute to assign access to a user or service-id. Use the
        **`access_group_id`** subject attribute to assign access to an access group.
        Assign roles that are supported by the service or platform roles. For more
        information, see [IAM roles and
        actions](/docs/account?topic=account-iam-service-roles-actions). Use only the
        resource attributes supported by the service. To view a service's or the
        platform's supported attributes, check the [documentation](/docs?tab=all-docs).
        The policy resource must include either the **`serviceType`**, **`serviceName`**,
        **`resourceGroupId`** or **`service_group_id`** attribute and the **`accountId`**
        attribute. In the rule field, you can specify a single condition by using
        **`key`**, **`value`**, and condition **`operator`**, or a set of **`conditions`**
        with a combination **`operator`**. The possible combination operators are
        **`and`** and **`or`**. Combine conditions to specify a time-based restriction
        (e.g., access only during business hours, during the Monday-Friday work week). For
        example, a policy can grant access Monday-Friday, 9:00am-5:00pm using the
        following rule:
        ```json
          "rule": {
            "operator": "and",
            "conditions": [{
              "key": "{{environment.attributes.day_of_week}}",
              "operator": "dayOfWeekAnyOf",
              "value": ["1+00:00", "2+00:00", "3+00:00", "4+00:00", "5+00:00"]
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
        ``` You can use the following operators in the **`key`**, **`value`** pair:
        ```
          'timeLessThan', 'timeLessThanOrEquals', 'timeGreaterThan',
        'timeGreaterThanOrEquals',
          'dateTimeLessThan', 'dateTimeLessThanOrEquals', 'dateTimeGreaterThan',
        'dateTimeGreaterThanOrEquals',
          'dayOfWeekEquals', 'dayOfWeekAnyOf',
        ``` The pattern field that matches the rule is required when rule is provided. For
        the business hour rule example above, the **`pattern`** is
        **`"time-based-conditions:weekly"`**. For more information, see [Time-based
        conditions
        operators](https://cloud.ibm.com/docs/account?topic=account-iam-condition-properties&interface=ui#policy-condition-properties)
        and
        [Limiting access with time-based
        conditions](https://cloud.ibm.com/docs/account?topic=account-iam-time-based&interface=ui).
        ### Attribute Operators
        Currently, only the `stringEquals`, `stringMatch`, and `stringEquals` operators
        are available. For more information, see [Assigning access by using wildcard
        policies](https://cloud.ibm.com/docs/account?topic=account-wildcard).
        ### Attribute Validations
        Policy attribute values must be between 1 and 1,000 characters in length. If
        location related attributes like geography, country, metro, region, satellite, and
        locationvalues are supported by the service, they are validated against Global
        Catalog locations.

        :param str id: The policy ID.
        :param str if_match: The revision number for updating a policy and must
               match the ETag value of the existing policy. The Etag can be retrieved
               using the GET /v2/policies/{id} API and looking at the ETag response
               header.
        :param Control control: Specifies the type of access granted by the policy.
        :param str type: The policy type; either 'access' or 'authorization'.
        :param str description: (optional) Description of the policy.
        :param V2PolicySubject subject: (optional) The subject attributes for whom
               the policy grants access.
        :param V2PolicyResource resource: (optional) The resource attributes to
               which the policy grants access.
        :param str pattern: (optional) Indicates pattern of rule, either
               'time-based-conditions:once', 'time-based-conditions:weekly:all-day', or
               'time-based-conditions:weekly:custom-hours'.
        :param V2PolicyRule rule: (optional) Additional access conditions
               associated with the policy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `V2Policy` object
        """

        if not id:
            raise ValueError('id must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if control is None:
            raise ValueError('control must be provided')
        if type is None:
            raise ValueError('type must be provided')
        control = convert_model(control)
        if subject is not None:
            subject = convert_model(subject)
        if resource is not None:
            resource = convert_model(resource)
        if rule is not None:
            rule = convert_model(rule)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='replace_v2_policy',
        )
        headers.update(sdk_headers)

        data = {
            'control': control,
            'type': type,
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

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/policies/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_v2_policy(
        self,
        id: str,
        *,
        format: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a policy by ID.

        Retrieve a policy by providing a policy ID.

        :param str id: The policy ID.
        :param str format: (optional) Include additional data for policy returned
               * `include_last_permit` - returns details of when the policy last granted a
               permit decision and the number of times it has done so
               * `display` - returns the list of all actions included in each of the
               policy roles and translations for all relevant fields.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `V2PolicyTemplateMetaData` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_v2_policy',
        )
        headers.update(sdk_headers)

        params = {
            'format': format,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/policies/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_v2_policy(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a policy by ID.

        Delete a policy by providing a policy ID. A policy cannot be deleted if the
        subject ID contains a locked service ID. If the subject of the policy is a locked
        service-id, the request will fail.

        :param str id: The policy ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_v2_policy',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/policies/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Policy templates
    #########################

    def list_policy_templates(
        self,
        account_id: str,
        *,
        accept_language: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List policy templates by attributes.

        List policy templates and filter by attributes by using query parameters. The
        following attributes are supported: `account_id`.
        `account_id` is a required query parameter. Only policy templates that have the
        specified attributes and that the caller has read access to are returned. If the
        caller does not have read access to any policy templates an empty array is
        returned.

        :param str account_id: The account GUID that the policy templates belong
               to.
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
        :rtype: DetailedResponse with `dict` result representing a `PolicyTemplateCollection` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        headers = {
            'Accept-Language': accept_language,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_policy_templates',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/policy_templates'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_policy_template(
        self,
        name: str,
        account_id: str,
        policy: 'TemplatePolicy',
        *,
        description: str = None,
        committed: bool = None,
        accept_language: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a policy template.

        Create a policy template. Policy templates define a policy without requiring a
        subject, and you can use them to grant access to multiple subjects.

        :param str name: Required field when creating a new template. Otherwise
               this field is optional. If the field is included it will change the name
               value for all existing versions of the template.
        :param str account_id: Enterprise account ID where this template will be
               created.
        :param TemplatePolicy policy: The core set of properties associated with
               the template's policy objet.
        :param str description: (optional) Description of the policy template. This
               is shown to users in the enterprise account. Use this to describe the
               purpose or context of the policy for enterprise users managing IAM
               templates.
        :param bool committed: (optional) Committed status of the template.
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
        :rtype: DetailedResponse with `dict` result representing a `PolicyTemplate` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if account_id is None:
            raise ValueError('account_id must be provided')
        if policy is None:
            raise ValueError('policy must be provided')
        policy = convert_model(policy)
        headers = {
            'Accept-Language': accept_language,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_policy_template',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'account_id': account_id,
            'policy': policy,
            'description': description,
            'committed': committed,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/policy_templates'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_policy_template(
        self,
        policy_template_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve latest version of a policy template.

        Retrieve the latest version of a policy template by providing a policy template
        ID.

        :param str policy_template_id: The policy template ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyTemplate` object
        """

        if not policy_template_id:
            raise ValueError('policy_template_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_policy_template',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_template_id']
        path_param_values = self.encode_path_vars(policy_template_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policy_templates/{policy_template_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_policy_template(
        self,
        policy_template_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a policy template.

        Delete a policy template by providing the policy template ID. This deletes all
        versions of this template. A policy template can't be deleted if any version of
        the template is assigned to one or more child accounts. You must remove the policy
        assignments first.

        :param str policy_template_id: The policy template ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not policy_template_id:
            raise ValueError('policy_template_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_policy_template',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['policy_template_id']
        path_param_values = self.encode_path_vars(policy_template_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policy_templates/{policy_template_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_policy_template_version(
        self,
        policy_template_id: str,
        policy: 'TemplatePolicy',
        *,
        name: str = None,
        description: str = None,
        committed: bool = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new policy template version.

        Create a new version of a policy template. Use this if you need to make updates to
        a policy template that is committed.

        :param str policy_template_id: The policy template ID.
        :param TemplatePolicy policy: The core set of properties associated with
               the template's policy objet.
        :param str name: (optional) Required field when creating a new template.
               Otherwise this field is optional. If the field is included it will change
               the name value for all existing versions of the template.
        :param str description: (optional) Description of the policy template. This
               is shown to users in the enterprise account. Use this to describe the
               purpose or context of the policy for enterprise users managing IAM
               templates.
        :param bool committed: (optional) Committed status of the template version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyTemplate` object
        """

        if not policy_template_id:
            raise ValueError('policy_template_id must be provided')
        if policy is None:
            raise ValueError('policy must be provided')
        policy = convert_model(policy)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_policy_template_version',
        )
        headers.update(sdk_headers)

        data = {
            'policy': policy,
            'name': name,
            'description': description,
            'committed': committed,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_template_id']
        path_param_values = self.encode_path_vars(policy_template_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policy_templates/{policy_template_id}/versions'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_policy_template_versions(
        self,
        policy_template_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve policy template versions.

        Retrieve the versions of a policy template by providing a policy template ID.

        :param str policy_template_id: The policy template ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyTemplateVersionsCollection` object
        """

        if not policy_template_id:
            raise ValueError('policy_template_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_policy_template_versions',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_template_id']
        path_param_values = self.encode_path_vars(policy_template_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policy_templates/{policy_template_id}/versions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_policy_template(
        self,
        policy_template_id: str,
        version: str,
        if_match: str,
        policy: 'TemplatePolicy',
        *,
        name: str = None,
        description: str = None,
        committed: bool = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a policy template version.

        Update a specific version of a policy template. You can use this only if the
        version isn't committed.

        :param str policy_template_id: The policy template ID.
        :param str version: The policy template version.
        :param str if_match: The revision number for updating a policy template
               version and must match the ETag value of the existing policy template
               version. The Etag can be retrieved using the GET
               /v1/policy_templates/{policy_template_id}/versions/{version} API and
               looking at the ETag response header.
        :param TemplatePolicy policy: The core set of properties associated with
               the template's policy objet.
        :param str name: (optional) Required field when creating a new template.
               Otherwise this field is optional. If the field is included it will change
               the name value for all existing versions of the template.
        :param str description: (optional) Description of the policy template. This
               is shown to users in the enterprise account. Use this to describe the
               purpose or context of the policy for enterprise users managing IAM
               templates.
        :param bool committed: (optional) Committed status of the template version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyTemplate` object
        """

        if not policy_template_id:
            raise ValueError('policy_template_id must be provided')
        if not version:
            raise ValueError('version must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if policy is None:
            raise ValueError('policy must be provided')
        policy = convert_model(policy)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='replace_policy_template',
        )
        headers.update(sdk_headers)

        data = {
            'policy': policy,
            'name': name,
            'description': description,
            'committed': committed,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_template_id', 'version']
        path_param_values = self.encode_path_vars(policy_template_id, version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policy_templates/{policy_template_id}/versions/{version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_policy_template_version(
        self,
        policy_template_id: str,
        version: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a policy template version.

        Delete a specific version of a policy template by providing a policy template ID
        and version number. You can't delete a policy template version that is assigned to
        one or more child accounts. You must remove the policy assignments first.

        :param str policy_template_id: The policy template ID.
        :param str version: The policy template version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not policy_template_id:
            raise ValueError('policy_template_id must be provided')
        if not version:
            raise ValueError('version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_policy_template_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['policy_template_id', 'version']
        path_param_values = self.encode_path_vars(policy_template_id, version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policy_templates/{policy_template_id}/versions/{version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_policy_template_version(
        self,
        policy_template_id: str,
        version: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a policy template version.

        Retrieve a policy template by providing a policy template ID and version number.

        :param str policy_template_id: The policy template ID.
        :param str version: The policy template version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyTemplate` object
        """

        if not policy_template_id:
            raise ValueError('policy_template_id must be provided')
        if not version:
            raise ValueError('version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_policy_template_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['policy_template_id', 'version']
        path_param_values = self.encode_path_vars(policy_template_id, version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policy_templates/{policy_template_id}/versions/{version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def commit_policy_template(
        self,
        policy_template_id: str,
        version: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Commit a policy template version.

        Commit a policy template version. You can make no further changes to the policy
        template once it's committed. If you need to make updates after committing a
        version, create a new version.

        :param str policy_template_id: The policy template ID.
        :param str version: The policy template version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not policy_template_id:
            raise ValueError('policy_template_id must be provided')
        if not version:
            raise ValueError('version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='commit_policy_template',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['policy_template_id', 'version']
        path_param_values = self.encode_path_vars(policy_template_id, version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policy_templates/{policy_template_id}/versions/{version}/commit'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Policy assignments
    #########################

    def list_policy_assignments(
        self,
        account_id: str,
        *,
        accept_language: str = None,
        template_id: str = None,
        template_version: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get policy template assignments.

        Get policy template assignments by attributes. The following attributes are
        supported:
        `account_id`, `template_id`, `template_version`, `sort`.
        `account_id` is a required query parameter. Only policy template assignments that
        have the specified attributes and that the caller has read access to are returned.
        If the caller does not have read access to any policy template assignments an
        empty array is returned.

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
        :param str template_id: (optional) Optional template id.
        :param str template_version: (optional) Optional policy template version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyTemplateAssignmentCollection` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        headers = {
            'Accept-Language': accept_language,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_policy_assignments',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'template_id': template_id,
            'template_version': template_version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/policy_assignments'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_policy_assignment(
        self,
        assignment_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a policy assignment.

        Retrieve a policy template assignment by providing a policy assignment ID.

        :param str assignment_id: The policy template assignment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyAssignment` object
        """

        if not assignment_id:
            raise ValueError('assignment_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_policy_assignment',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assignment_id']
        path_param_values = self.encode_path_vars(assignment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/policy_assignments/{assignment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

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


class ListV2PoliciesEnums:
    """
    Enums for list_v2_policies parameters.
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


class GetV2PolicyEnums:
    """
    Enums for get_v2_policy parameters.
    """

    class Format(str, Enum):
        """
        Include additional data for policy returned
        * `include_last_permit` - returns details of when the policy last granted a permit
        decision and the number of times it has done so
        * `display` - returns the list of all actions included in each of the policy roles
        and translations for all relevant fields.
        """

        INCLUDE_LAST_PERMIT = 'include_last_permit'
        DISPLAY = 'display'


##############################################################################
# Models
##############################################################################


class AssignmentResourceCreated:
    """
    On success, includes the  policy assigned.

    :attr str id: (optional) policy id.
    """

    def __init__(
        self,
        *,
        id: str = None,
    ) -> None:
        """
        Initialize a AssignmentResourceCreated object.

        :param str id: (optional) policy id.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssignmentResourceCreated':
        """Initialize a AssignmentResourceCreated object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssignmentResourceCreated object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssignmentResourceCreated object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssignmentResourceCreated') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssignmentResourceCreated') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConflictsWith:
    """
    Details of conflicting resource.

    :attr str etag: (optional) The revision number of the resource.
    :attr str role: (optional) The conflicting role id.
    :attr str policy: (optional) The conflicting policy id.
    """

    def __init__(
        self,
        *,
        etag: str = None,
        role: str = None,
        policy: str = None,
    ) -> None:
        """
        Initialize a ConflictsWith object.

        :param str etag: (optional) The revision number of the resource.
        :param str role: (optional) The conflicting role id.
        :param str policy: (optional) The conflicting policy id.
        """
        self.etag = etag
        self.role = role
        self.policy = policy

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConflictsWith':
        """Initialize a ConflictsWith object from a json dictionary."""
        args = {}
        if 'etag' in _dict:
            args['etag'] = _dict.get('etag')
        if 'role' in _dict:
            args['role'] = _dict.get('role')
        if 'policy' in _dict:
            args['policy'] = _dict.get('policy')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConflictsWith object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'etag') and self.etag is not None:
            _dict['etag'] = self.etag
        if hasattr(self, 'role') and self.role is not None:
            _dict['role'] = self.role
        if hasattr(self, 'policy') and self.policy is not None:
            _dict['policy'] = self.policy
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConflictsWith object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConflictsWith') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConflictsWith') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Control:
    """
    Specifies the type of access granted by the policy.

    :attr Grant grant: Permission granted by the policy.
    """

    def __init__(
        self,
        grant: 'Grant',
    ) -> None:
        """
        Initialize a Control object.

        :param Grant grant: Permission granted by the policy.
        """
        self.grant = grant

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Control':
        """Initialize a Control object from a json dictionary."""
        args = {}
        if 'grant' in _dict:
            args['grant'] = Grant.from_dict(_dict.get('grant'))
        else:
            raise ValueError('Required property \'grant\' not present in Control JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Control object from a json dictionary."""
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
        """Return a `str` version of this Control object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Control') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Control') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlResponse:
    """
    ControlResponse.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a ControlResponse object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['ControlResponseControl', 'ControlResponseControlWithEnrichedRoles'])
        )
        raise Exception(msg)


class CustomRole:
    """
    An additional set of properties associated with a role.

    :attr str id: (optional) The role ID. Composed of hexadecimal characters.
    :attr str display_name: The display name of the role that is shown in the
          console.
    :attr str description: (optional) The description of the role.
    :attr List[str] actions: The actions of the role. For more information, see [IAM
          roles and
          actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
    :attr str crn: (optional) The role Cloud Resource Name (CRN). Example CRN:
          'crn:v1:ibmcloud:public:iam-access-management::a/exampleAccountId::customRole:ExampleRoleName'.
    :attr str name: The name of the role that is used in the CRN. Can only be
          alphanumeric and has to be capitalized.
    :attr str account_id: The account GUID.
    :attr str service_name: The service name.
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
        display_name: str,
        actions: List[str],
        name: str,
        account_id: str,
        service_name: str,
        *,
        id: str = None,
        description: str = None,
        crn: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
        href: str = None,
    ) -> None:
        """
        Initialize a CustomRole object.

        :param str display_name: The display name of the role that is shown in the
               console.
        :param List[str] actions: The actions of the role. For more information,
               see [IAM roles and
               actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
        :param str name: The name of the role that is used in the CRN. Can only be
               alphanumeric and has to be capitalized.
        :param str account_id: The account GUID.
        :param str service_name: The service name.
        :param str description: (optional) The description of the role.
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
        else:
            raise ValueError('Required property \'display_name\' not present in CustomRole JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'actions' in _dict:
            args['actions'] = _dict.get('actions')
        else:
            raise ValueError('Required property \'actions\' not present in CustomRole JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in CustomRole JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in CustomRole JSON')
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        else:
            raise ValueError('Required property \'service_name\' not present in CustomRole JSON')
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


class EnrichedRoles:
    """
    A role associated with a policy with additional information (display_name,
    description, actions) when `format=display`.

    :attr str role_id: The role Cloud Resource Name (CRN) granted by the policy.
          Example CRN: 'crn:v1:bluemix:public:iam::::role:Editor'.
    :attr str display_name: (optional) The service defined (or user defined if a
          custom role) display name of the role.
    :attr str description: (optional) The service defined (or user defined if a
          custom role) description of the role.
    :attr List[RoleAction] actions: The actions of the role. For more information,
          see [IAM roles and
          actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
    """

    def __init__(
        self,
        role_id: str,
        actions: List['RoleAction'],
        *,
        display_name: str = None,
        description: str = None,
    ) -> None:
        """
        Initialize a EnrichedRoles object.

        :param str role_id: The role Cloud Resource Name (CRN) granted by the
               policy. Example CRN: 'crn:v1:bluemix:public:iam::::role:Editor'.
        :param List[RoleAction] actions: The actions of the role. For more
               information, see [IAM roles and
               actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
        """
        self.role_id = role_id
        self.display_name = display_name
        self.description = description
        self.actions = actions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnrichedRoles':
        """Initialize a EnrichedRoles object from a json dictionary."""
        args = {}
        if 'role_id' in _dict:
            args['role_id'] = _dict.get('role_id')
        else:
            raise ValueError('Required property \'role_id\' not present in EnrichedRoles JSON')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'actions' in _dict:
            args['actions'] = [RoleAction.from_dict(v) for v in _dict.get('actions')]
        else:
            raise ValueError('Required property \'actions\' not present in EnrichedRoles JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnrichedRoles object from a json dictionary."""
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
        if hasattr(self, 'actions') and self.actions is not None:
            actions_list = []
            for v in self.actions:
                if isinstance(v, dict):
                    actions_list.append(v)
                else:
                    actions_list.append(v.to_dict())
            _dict['actions'] = actions_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnrichedRoles object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnrichedRoles') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnrichedRoles') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ErrorDetails:
    """
    Additional error details.

    :attr ConflictsWith conflicts_with: (optional) Details of conflicting resource.
    """

    def __init__(
        self,
        *,
        conflicts_with: 'ConflictsWith' = None,
    ) -> None:
        """
        Initialize a ErrorDetails object.

        :param ConflictsWith conflicts_with: (optional) Details of conflicting
               resource.
        """
        self.conflicts_with = conflicts_with

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorDetails':
        """Initialize a ErrorDetails object from a json dictionary."""
        args = {}
        if 'conflicts_with' in _dict:
            args['conflicts_with'] = ConflictsWith.from_dict(_dict.get('conflicts_with'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'conflicts_with') and self.conflicts_with is not None:
            if isinstance(self.conflicts_with, dict):
                _dict['conflicts_with'] = self.conflicts_with
            else:
                _dict['conflicts_with'] = self.conflicts_with.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ErrorDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ErrorObject:
    """
    ErrorObject.

    :attr str code: The API error code for the error.
    :attr str message: The error message returned by the API.
    :attr ErrorDetails details: (optional) Additional error details.
    :attr str more_info: (optional) Additional info for error.
    """

    def __init__(
        self,
        code: str,
        message: str,
        *,
        details: 'ErrorDetails' = None,
        more_info: str = None,
    ) -> None:
        """
        Initialize a ErrorObject object.

        :param str code: The API error code for the error.
        :param str message: The error message returned by the API.
        :param ErrorDetails details: (optional) Additional error details.
        :param str more_info: (optional) Additional info for error.
        """
        self.code = code
        self.message = message
        self.details = details
        self.more_info = more_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorObject':
        """Initialize a ErrorObject object from a json dictionary."""
        args = {}
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        else:
            raise ValueError('Required property \'code\' not present in ErrorObject JSON')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError('Required property \'message\' not present in ErrorObject JSON')
        if 'details' in _dict:
            args['details'] = ErrorDetails.from_dict(_dict.get('details'))
        if 'more_info' in _dict:
            args['more_info'] = _dict.get('more_info')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'details') and self.details is not None:
            if isinstance(self.details, dict):
                _dict['details'] = self.details
            else:
                _dict['details'] = self.details.to_dict()
        if hasattr(self, 'more_info') and self.more_info is not None:
            _dict['more_info'] = self.more_info
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ErrorObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CodeEnum(str, Enum):
        """
        The API error code for the error.
        """

        INSUFFICENT_PERMISSIONS = 'insufficent_permissions'
        INVALID_BODY = 'invalid_body'
        INVALID_TOKEN = 'invalid_token'
        MISSING_REQUIRED_QUERY_PARAMETER = 'missing_required_query_parameter'
        NOT_FOUND = 'not_found'
        POLICY_CONFLICT_ERROR = 'policy_conflict_error'
        POLICY_NOT_FOUND = 'policy_not_found'
        REQUEST_NOT_PROCESSED = 'request_not_processed'
        ROLE_CONFLICT_ERROR = 'role_conflict_error'
        ROLE_NOT_FOUND = 'role_not_found'
        TOO_MANY_REQUESTS = 'too_many_requests'
        UNABLE_TO_PROCESS = 'unable_to_process'
        UNSUPPORTED_CONTENT_TYPE = 'unsupported_content_type'
        POLICY_TEMPLATE_CONFLICT_ERROR = 'policy_template_conflict_error'
        POLICY_TEMPLATE_NOT_FOUND = 'policy_template_not_found'
        POLICY_ASSIGNMENT_NOT_FOUND = 'policy_assignment_not_found'
        POLICY_ASSIGNMENT_CONFLICT_ERROR = 'policy_assignment_conflict_error'


class ErrorResponse:
    """
    The error response from API.

    :attr str trace: (optional) The unique transaction id for the request.
    :attr List[ErrorObject] errors: (optional) The errors encountered during the
          response.
    :attr int status_code: (optional) The http error code of the response.
    """

    def __init__(
        self,
        *,
        trace: str = None,
        errors: List['ErrorObject'] = None,
        status_code: int = None,
    ) -> None:
        """
        Initialize a ErrorResponse object.

        :param str trace: (optional) The unique transaction id for the request.
        :param List[ErrorObject] errors: (optional) The errors encountered during
               the response.
        :param int status_code: (optional) The http error code of the response.
        """
        self.trace = trace
        self.errors = errors
        self.status_code = status_code

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorResponse':
        """Initialize a ErrorResponse object from a json dictionary."""
        args = {}
        if 'trace' in _dict:
            args['trace'] = _dict.get('trace')
        if 'errors' in _dict:
            args['errors'] = [ErrorObject.from_dict(v) for v in _dict.get('errors')]
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        if hasattr(self, 'errors') and self.errors is not None:
            errors_list = []
            for v in self.errors:
                if isinstance(v, dict):
                    errors_list.append(v)
                else:
                    errors_list.append(v.to_dict())
            _dict['errors'] = errors_list
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ErrorResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Grant:
    """
    Permission granted by the policy.

    :attr List[Roles] roles: A set of role cloud resource names (CRNs) granted by
          the policy.
    """

    def __init__(
        self,
        roles: List['Roles'],
    ) -> None:
        """
        Initialize a Grant object.

        :param List[Roles] roles: A set of role cloud resource names (CRNs) granted
               by the policy.
        """
        self.roles = roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Grant':
        """Initialize a Grant object from a json dictionary."""
        args = {}
        if 'roles' in _dict:
            args['roles'] = [Roles.from_dict(v) for v in _dict.get('roles')]
        else:
            raise ValueError('Required property \'roles\' not present in Grant JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Grant object from a json dictionary."""
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
        """Return a `str` version of this Grant object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Grant') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Grant') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GrantWithEnrichedRoles:
    """
    Permission granted by the policy with translated roles and additional role
    information.

    :attr List[EnrichedRoles] roles: A set of roles granted by the policy.
    """

    def __init__(
        self,
        roles: List['EnrichedRoles'],
    ) -> None:
        """
        Initialize a GrantWithEnrichedRoles object.

        :param List[EnrichedRoles] roles: A set of roles granted by the policy.
        """
        self.roles = roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GrantWithEnrichedRoles':
        """Initialize a GrantWithEnrichedRoles object from a json dictionary."""
        args = {}
        if 'roles' in _dict:
            args['roles'] = [EnrichedRoles.from_dict(v) for v in _dict.get('roles')]
        else:
            raise ValueError('Required property \'roles\' not present in GrantWithEnrichedRoles JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GrantWithEnrichedRoles object from a json dictionary."""
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
        """Return a `str` version of this GrantWithEnrichedRoles object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GrantWithEnrichedRoles') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GrantWithEnrichedRoles') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Policy:
    """
    The core set of properties associated with a policy.

    :attr str id: (optional) The policy ID.
    :attr str type: The policy type; either 'access' or 'authorization'.
    :attr str description: (optional) Customer-defined description.
    :attr List[PolicySubject] subjects: The subjects associated with a policy.
    :attr List[PolicyRole] roles: A set of role cloud resource names (CRNs) granted
          by the policy.
    :attr List[PolicyResource] resources: The resources associated with a policy.
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
        subjects: List['PolicySubject'],
        roles: List['PolicyRole'],
        resources: List['PolicyResource'],
        *,
        id: str = None,
        description: str = None,
        href: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
        state: str = None,
    ) -> None:
        """
        Initialize a Policy object.

        :param str type: The policy type; either 'access' or 'authorization'.
        :param List[PolicySubject] subjects: The subjects associated with a policy.
        :param List[PolicyRole] roles: A set of role cloud resource names (CRNs)
               granted by the policy.
        :param List[PolicyResource] resources: The resources associated with a
               policy.
        :param str description: (optional) Customer-defined description.
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
        else:
            raise ValueError('Required property \'type\' not present in Policy JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'subjects' in _dict:
            args['subjects'] = [PolicySubject.from_dict(v) for v in _dict.get('subjects')]
        else:
            raise ValueError('Required property \'subjects\' not present in Policy JSON')
        if 'roles' in _dict:
            args['roles'] = [PolicyRole.from_dict(v) for v in _dict.get('roles')]
        else:
            raise ValueError('Required property \'roles\' not present in Policy JSON')
        if 'resources' in _dict:
            args['resources'] = [PolicyResource.from_dict(v) for v in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in Policy JSON')
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


class PolicyAssignment:
    """
    The set of properties associated with the policy template assignment.

    :attr str template_id: policy template id.
    :attr str template_version: policy template version.
    :attr str assignment_id: Passed in value to correlate with other assignments.
    :attr str target_type: Assignment target type.
    :attr str target: ID of the target account.
    :attr List[PolicyAssignmentOptions] options: List of objects with required
          properties for a policy assignment.
    :attr str id: (optional) Policy assignment ID.
    :attr str account_id: (optional) The account GUID that the policies assignments
          belong to..
    :attr str href: (optional) The href URL that links to the policies assignments
          API by policy assignment ID.
    :attr datetime created_at: (optional) The UTC timestamp when the policy
          assignment was created.
    :attr str created_by_id: (optional) The iam ID of the entity that created the
          policy assignment.
    :attr datetime last_modified_at: (optional) The UTC timestamp when the policy
          assignment was last modified.
    :attr str last_modified_by_id: (optional) The iam ID of the entity that last
          modified the policy assignment.
    :attr List[PolicyAssignmentResources] resources: (optional) Object for each
          account assigned.
    :attr str status: The policy assignment status.
    """

    def __init__(
        self,
        template_id: str,
        template_version: str,
        assignment_id: str,
        target_type: str,
        target: str,
        options: List['PolicyAssignmentOptions'],
        status: str,
        *,
        id: str = None,
        account_id: str = None,
        href: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
        resources: List['PolicyAssignmentResources'] = None,
    ) -> None:
        """
        Initialize a PolicyAssignment object.

        :param str template_id: policy template id.
        :param str template_version: policy template version.
        :param str assignment_id: Passed in value to correlate with other
               assignments.
        :param str target_type: Assignment target type.
        :param str target: ID of the target account.
        :param List[PolicyAssignmentOptions] options: List of objects with required
               properties for a policy assignment.
        :param str status: The policy assignment status.
        :param List[PolicyAssignmentResources] resources: (optional) Object for
               each account assigned.
        """
        self.template_id = template_id
        self.template_version = template_version
        self.assignment_id = assignment_id
        self.target_type = target_type
        self.target = target
        self.options = options
        self.id = id
        self.account_id = account_id
        self.href = href
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id
        self.resources = resources
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyAssignment':
        """Initialize a PolicyAssignment object from a json dictionary."""
        args = {}
        if 'template_id' in _dict:
            args['template_id'] = _dict.get('template_id')
        else:
            raise ValueError('Required property \'template_id\' not present in PolicyAssignment JSON')
        if 'template_version' in _dict:
            args['template_version'] = _dict.get('template_version')
        else:
            raise ValueError('Required property \'template_version\' not present in PolicyAssignment JSON')
        if 'assignment_id' in _dict:
            args['assignment_id'] = _dict.get('assignment_id')
        else:
            raise ValueError('Required property \'assignment_id\' not present in PolicyAssignment JSON')
        if 'target_type' in _dict:
            args['target_type'] = _dict.get('target_type')
        else:
            raise ValueError('Required property \'target_type\' not present in PolicyAssignment JSON')
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in PolicyAssignment JSON')
        if 'options' in _dict:
            args['options'] = [PolicyAssignmentOptions.from_dict(v) for v in _dict.get('options')]
        else:
            raise ValueError('Required property \'options\' not present in PolicyAssignment JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
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
        if 'resources' in _dict:
            args['resources'] = [PolicyAssignmentResources.from_dict(v) for v in _dict.get('resources')]
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in PolicyAssignment JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyAssignment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'template_id') and self.template_id is not None:
            _dict['template_id'] = self.template_id
        if hasattr(self, 'template_version') and self.template_version is not None:
            _dict['template_version'] = self.template_version
        if hasattr(self, 'assignment_id') and self.assignment_id is not None:
            _dict['assignment_id'] = self.assignment_id
        if hasattr(self, 'target_type') and self.target_type is not None:
            _dict['target_type'] = self.target_type
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'options') and self.options is not None:
            options_list = []
            for v in self.options:
                if isinstance(v, dict):
                    options_list.append(v)
                else:
                    options_list.append(v.to_dict())
            _dict['options'] = options_list
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'account_id') and getattr(self, 'account_id') is not None:
            _dict['account_id'] = getattr(self, 'account_id')
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
        if hasattr(self, 'resources') and self.resources is not None:
            resources_list = []
            for v in self.resources:
                if isinstance(v, dict):
                    resources_list.append(v)
                else:
                    resources_list.append(v.to_dict())
            _dict['resources'] = resources_list
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyAssignment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyAssignment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyAssignment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TargetTypeEnum(str, Enum):
        """
        Assignment target type.
        """

        ACCOUNT = 'Account'

    class StatusEnum(str, Enum):
        """
        The policy assignment status.
        """

        IN_PROGRESS = 'in_progress'
        SUCCEEDED = 'succeeded'
        SUCCEED_WITH_ERRORS = 'succeed_with_errors'
        FAILED = 'failed'


class PolicyAssignmentOptions:
    """
    The set of properties required for a policy assignment.

    :attr str subject_type: The policy subject type; either 'iam_id' or
          'access_group_id'.
    :attr str subject_id: The policy subject id.
    :attr str root_requester_id: The policy assignment requester id.
    :attr str root_template_id: (optional) The template id where this policy is
          being assigned from.
    :attr str root_template_version: (optional) The template version where this
          policy is being assigned from.
    """

    def __init__(
        self,
        subject_type: str,
        subject_id: str,
        root_requester_id: str,
        *,
        root_template_id: str = None,
        root_template_version: str = None,
    ) -> None:
        """
        Initialize a PolicyAssignmentOptions object.

        :param str subject_type: The policy subject type; either 'iam_id' or
               'access_group_id'.
        :param str subject_id: The policy subject id.
        :param str root_requester_id: The policy assignment requester id.
        :param str root_template_id: (optional) The template id where this policy
               is being assigned from.
        :param str root_template_version: (optional) The template version where
               this policy is being assigned from.
        """
        self.subject_type = subject_type
        self.subject_id = subject_id
        self.root_requester_id = root_requester_id
        self.root_template_id = root_template_id
        self.root_template_version = root_template_version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyAssignmentOptions':
        """Initialize a PolicyAssignmentOptions object from a json dictionary."""
        args = {}
        if 'subject_type' in _dict:
            args['subject_type'] = _dict.get('subject_type')
        else:
            raise ValueError('Required property \'subject_type\' not present in PolicyAssignmentOptions JSON')
        if 'subject_id' in _dict:
            args['subject_id'] = _dict.get('subject_id')
        else:
            raise ValueError('Required property \'subject_id\' not present in PolicyAssignmentOptions JSON')
        if 'root_requester_id' in _dict:
            args['root_requester_id'] = _dict.get('root_requester_id')
        else:
            raise ValueError('Required property \'root_requester_id\' not present in PolicyAssignmentOptions JSON')
        if 'root_template_id' in _dict:
            args['root_template_id'] = _dict.get('root_template_id')
        if 'root_template_version' in _dict:
            args['root_template_version'] = _dict.get('root_template_version')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyAssignmentOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'subject_type') and self.subject_type is not None:
            _dict['subject_type'] = self.subject_type
        if hasattr(self, 'subject_id') and self.subject_id is not None:
            _dict['subject_id'] = self.subject_id
        if hasattr(self, 'root_requester_id') and self.root_requester_id is not None:
            _dict['root_requester_id'] = self.root_requester_id
        if hasattr(self, 'root_template_id') and self.root_template_id is not None:
            _dict['root_template_id'] = self.root_template_id
        if hasattr(self, 'root_template_version') and self.root_template_version is not None:
            _dict['root_template_version'] = self.root_template_version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyAssignmentOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyAssignmentOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyAssignmentOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SubjectTypeEnum(str, Enum):
        """
        The policy subject type; either 'iam_id' or 'access_group_id'.
        """

        IAM_ID = 'iam_id'
        ACCESS_GROUP_ID = 'access_group_id'


class PolicyAssignmentResourcePolicy:
    """
    Set of properties for the assigned resource.

    :attr AssignmentResourceCreated resource_created: (optional) On success,
          includes the  policy assigned.
    :attr str status: (optional) policy status.
    :attr ErrorResponse error_message: (optional) The error response from API.
    """

    def __init__(
        self,
        *,
        resource_created: 'AssignmentResourceCreated' = None,
        status: str = None,
        error_message: 'ErrorResponse' = None,
    ) -> None:
        """
        Initialize a PolicyAssignmentResourcePolicy object.

        :param AssignmentResourceCreated resource_created: (optional) On success,
               includes the  policy assigned.
        :param str status: (optional) policy status.
        :param ErrorResponse error_message: (optional) The error response from API.
        """
        self.resource_created = resource_created
        self.status = status
        self.error_message = error_message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyAssignmentResourcePolicy':
        """Initialize a PolicyAssignmentResourcePolicy object from a json dictionary."""
        args = {}
        if 'resource_created' in _dict:
            args['resource_created'] = AssignmentResourceCreated.from_dict(_dict.get('resource_created'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'error_message' in _dict:
            args['error_message'] = ErrorResponse.from_dict(_dict.get('error_message'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyAssignmentResourcePolicy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_created') and self.resource_created is not None:
            if isinstance(self.resource_created, dict):
                _dict['resource_created'] = self.resource_created
            else:
                _dict['resource_created'] = self.resource_created.to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'error_message') and self.error_message is not None:
            if isinstance(self.error_message, dict):
                _dict['error_message'] = self.error_message
            else:
                _dict['error_message'] = self.error_message.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyAssignmentResourcePolicy object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyAssignmentResourcePolicy') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyAssignmentResourcePolicy') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyAssignmentResources:
    """
    The policy assignment resources.

    :attr str target: (optional) Account ID where resources are assigned.
    :attr PolicyAssignmentResourcePolicy policy: (optional) Set of properties for
          the assigned resource.
    """

    def __init__(
        self,
        *,
        target: str = None,
        policy: 'PolicyAssignmentResourcePolicy' = None,
    ) -> None:
        """
        Initialize a PolicyAssignmentResources object.

        :param str target: (optional) Account ID where resources are assigned.
        :param PolicyAssignmentResourcePolicy policy: (optional) Set of properties
               for the assigned resource.
        """
        self.target = target
        self.policy = policy

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyAssignmentResources':
        """Initialize a PolicyAssignmentResources object from a json dictionary."""
        args = {}
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        if 'policy' in _dict:
            args['policy'] = PolicyAssignmentResourcePolicy.from_dict(_dict.get('policy'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyAssignmentResources object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'policy') and self.policy is not None:
            if isinstance(self.policy, dict):
                _dict['policy'] = self.policy
            else:
                _dict['policy'] = self.policy.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyAssignmentResources object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyAssignmentResources') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyAssignmentResources') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyCollection:
    """
    A collection of policies.

    :attr List[PolicyTemplateMetaData] policies: (optional) List of policies.
    """

    def __init__(
        self,
        *,
        policies: List['PolicyTemplateMetaData'] = None,
    ) -> None:
        """
        Initialize a PolicyCollection object.

        :param List[PolicyTemplateMetaData] policies: (optional) List of policies.
        """
        self.policies = policies

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyCollection':
        """Initialize a PolicyCollection object from a json dictionary."""
        args = {}
        if 'policies' in _dict:
            args['policies'] = [PolicyTemplateMetaData.from_dict(v) for v in _dict.get('policies')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyCollection object from a json dictionary."""
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
        """Return a `str` version of this PolicyCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyResource:
    """
    The attributes of the resource. Note that only one resource is allowed in a policy.

    :attr List[ResourceAttribute] attributes: (optional) List of resource
          attributes.
    :attr List[ResourceTag] tags: (optional) List of access management tags.
    """

    def __init__(
        self,
        *,
        attributes: List['ResourceAttribute'] = None,
        tags: List['ResourceTag'] = None,
    ) -> None:
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

    def __init__(
        self,
        role_id: str,
        *,
        display_name: str = None,
        description: str = None,
    ) -> None:
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

    def __init__(
        self,
        *,
        attributes: List['SubjectAttribute'] = None,
    ) -> None:
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


class PolicyTemplate:
    """
    The core set of properties associated with the policy template.

    :attr str name: Required field when creating a new template. Otherwise this
          field is optional. If the field is included it will change the name value for
          all existing versions of the template.
    :attr str description: (optional) Description of the policy template. This is
          shown to users in the enterprise account. Use this to describe the purpose or
          context of the policy for enterprise users managing IAM templates.
    :attr str account_id: Enterprise account ID where this template will be created.
    :attr str version: Template version.
    :attr bool committed: (optional) Committed status of the template version.
    :attr TemplatePolicy policy: The core set of properties associated with the
          template's policy objet.
    :attr str id: (optional) The policy template ID.
    :attr str href: (optional) The href URL that links to the policy templates API
          by policy template ID.
    :attr datetime created_at: (optional) The UTC timestamp when the policy template
          was created.
    :attr str created_by_id: (optional) The iam ID of the entity that created the
          policy template.
    :attr datetime last_modified_at: (optional) The UTC timestamp when the policy
          template was last modified.
    :attr str last_modified_by_id: (optional) The iam ID of the entity that last
          modified the policy template.
    """

    def __init__(
        self,
        name: str,
        account_id: str,
        version: str,
        policy: 'TemplatePolicy',
        *,
        description: str = None,
        committed: bool = None,
        id: str = None,
        href: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
    ) -> None:
        """
        Initialize a PolicyTemplate object.

        :param str name: Required field when creating a new template. Otherwise
               this field is optional. If the field is included it will change the name
               value for all existing versions of the template.
        :param str account_id: Enterprise account ID where this template will be
               created.
        :param str version: Template version.
        :param TemplatePolicy policy: The core set of properties associated with
               the template's policy objet.
        :param str description: (optional) Description of the policy template. This
               is shown to users in the enterprise account. Use this to describe the
               purpose or context of the policy for enterprise users managing IAM
               templates.
        :param bool committed: (optional) Committed status of the template version.
        """
        self.name = name
        self.description = description
        self.account_id = account_id
        self.version = version
        self.committed = committed
        self.policy = policy
        self.id = id
        self.href = href
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyTemplate':
        """Initialize a PolicyTemplate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in PolicyTemplate JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in PolicyTemplate JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in PolicyTemplate JSON')
        if 'committed' in _dict:
            args['committed'] = _dict.get('committed')
        if 'policy' in _dict:
            args['policy'] = TemplatePolicy.from_dict(_dict.get('policy'))
        else:
            raise ValueError('Required property \'policy\' not present in PolicyTemplate JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
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
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyTemplate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'committed') and self.committed is not None:
            _dict['committed'] = self.committed
        if hasattr(self, 'policy') and self.policy is not None:
            if isinstance(self.policy, dict):
                _dict['policy'] = self.policy
            else:
                _dict['policy'] = self.policy.to_dict()
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyTemplate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyTemplate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyTemplate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyTemplateAssignmentCollection:
    """
    A collection of policies assignments.

    :attr List[PolicyAssignment] assignments: (optional) List of policy assignments.
    """

    def __init__(
        self,
        *,
        assignments: List['PolicyAssignment'] = None,
    ) -> None:
        """
        Initialize a PolicyTemplateAssignmentCollection object.

        :param List[PolicyAssignment] assignments: (optional) List of policy
               assignments.
        """
        self.assignments = assignments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyTemplateAssignmentCollection':
        """Initialize a PolicyTemplateAssignmentCollection object from a json dictionary."""
        args = {}
        if 'assignments' in _dict:
            args['assignments'] = [PolicyAssignment.from_dict(v) for v in _dict.get('assignments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyTemplateAssignmentCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'assignments') and self.assignments is not None:
            assignments_list = []
            for v in self.assignments:
                if isinstance(v, dict):
                    assignments_list.append(v)
                else:
                    assignments_list.append(v.to_dict())
            _dict['assignments'] = assignments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyTemplateAssignmentCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyTemplateAssignmentCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyTemplateAssignmentCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyTemplateCollection:
    """
    A collection of policy Templates.

    :attr List[PolicyTemplate] policy_templates: (optional) List of policy
          templates.
    """

    def __init__(
        self,
        *,
        policy_templates: List['PolicyTemplate'] = None,
    ) -> None:
        """
        Initialize a PolicyTemplateCollection object.

        :param List[PolicyTemplate] policy_templates: (optional) List of policy
               templates.
        """
        self.policy_templates = policy_templates

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyTemplateCollection':
        """Initialize a PolicyTemplateCollection object from a json dictionary."""
        args = {}
        if 'policy_templates' in _dict:
            args['policy_templates'] = [PolicyTemplate.from_dict(v) for v in _dict.get('policy_templates')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyTemplateCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'policy_templates') and self.policy_templates is not None:
            policy_templates_list = []
            for v in self.policy_templates:
                if isinstance(v, dict):
                    policy_templates_list.append(v)
                else:
                    policy_templates_list.append(v.to_dict())
            _dict['policy_templates'] = policy_templates_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyTemplateCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyTemplateCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyTemplateCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyTemplateMetaData:
    """
    The core set of properties associated with a policy.

    :attr str id: (optional) The policy ID.
    :attr str type: The policy type; either 'access' or 'authorization'.
    :attr str description: (optional) Customer-defined description.
    :attr List[PolicySubject] subjects: The subjects associated with a policy.
    :attr List[PolicyRole] roles: A set of role cloud resource names (CRNs) granted
          by the policy.
    :attr List[PolicyResource] resources: The resources associated with a policy.
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
    :attr TemplateMetadata template: (optional) The details of the IAM template that
          was used to create an enterprise-managed policy in your account. When returned,
          this indicates that the policy is created from and managed by a template in the
          root enterprise account.
    """

    def __init__(
        self,
        type: str,
        subjects: List['PolicySubject'],
        roles: List['PolicyRole'],
        resources: List['PolicyResource'],
        *,
        id: str = None,
        description: str = None,
        href: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
        state: str = None,
        template: 'TemplateMetadata' = None,
    ) -> None:
        """
        Initialize a PolicyTemplateMetaData object.

        :param str type: The policy type; either 'access' or 'authorization'.
        :param List[PolicySubject] subjects: The subjects associated with a policy.
        :param List[PolicyRole] roles: A set of role cloud resource names (CRNs)
               granted by the policy.
        :param List[PolicyResource] resources: The resources associated with a
               policy.
        :param str description: (optional) Customer-defined description.
        :param str state: (optional) The policy state.
        :param TemplateMetadata template: (optional) The details of the IAM
               template that was used to create an enterprise-managed policy in your
               account. When returned, this indicates that the policy is created from and
               managed by a template in the root enterprise account.
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
        self.template = template

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyTemplateMetaData':
        """Initialize a PolicyTemplateMetaData object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in PolicyTemplateMetaData JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'subjects' in _dict:
            args['subjects'] = [PolicySubject.from_dict(v) for v in _dict.get('subjects')]
        else:
            raise ValueError('Required property \'subjects\' not present in PolicyTemplateMetaData JSON')
        if 'roles' in _dict:
            args['roles'] = [PolicyRole.from_dict(v) for v in _dict.get('roles')]
        else:
            raise ValueError('Required property \'roles\' not present in PolicyTemplateMetaData JSON')
        if 'resources' in _dict:
            args['resources'] = [PolicyResource.from_dict(v) for v in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in PolicyTemplateMetaData JSON')
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
        if 'template' in _dict:
            args['template'] = TemplateMetadata.from_dict(_dict.get('template'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyTemplateMetaData object from a json dictionary."""
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
        if hasattr(self, 'template') and self.template is not None:
            if isinstance(self.template, dict):
                _dict['template'] = self.template
            else:
                _dict['template'] = self.template.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyTemplateMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyTemplateMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyTemplateMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The policy state.
        """

        ACTIVE = 'active'
        DELETED = 'deleted'


class PolicyTemplateVersionsCollection:
    """
    A collection of versions for a specific policy template.

    :attr List[PolicyTemplate] versions: (optional) List of policy templates
          versions.
    """

    def __init__(
        self,
        *,
        versions: List['PolicyTemplate'] = None,
    ) -> None:
        """
        Initialize a PolicyTemplateVersionsCollection object.

        :param List[PolicyTemplate] versions: (optional) List of policy templates
               versions.
        """
        self.versions = versions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyTemplateVersionsCollection':
        """Initialize a PolicyTemplateVersionsCollection object from a json dictionary."""
        args = {}
        if 'versions' in _dict:
            args['versions'] = [PolicyTemplate.from_dict(v) for v in _dict.get('versions')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyTemplateVersionsCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'versions') and self.versions is not None:
            versions_list = []
            for v in self.versions:
                if isinstance(v, dict):
                    versions_list.append(v)
                else:
                    versions_list.append(v.to_dict())
            _dict['versions'] = versions_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyTemplateVersionsCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyTemplateVersionsCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyTemplateVersionsCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceAttribute:
    """
    An attribute associated with a resource.

    :attr str name: The name of an attribute.
    :attr str value: The value of an attribute.
    :attr str operator: (optional) The operator of an attribute.
    """

    def __init__(
        self,
        name: str,
        value: str,
        *,
        operator: str = None,
    ) -> None:
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

    def __init__(
        self,
        name: str,
        value: str,
        *,
        operator: str = None,
    ) -> None:
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

    :attr str display_name: The display name of the role that is shown in the
          console.
    :attr str description: (optional) The description of the role.
    :attr List[str] actions: The actions of the role. For more information, see [IAM
          roles and
          actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
    :attr str crn: (optional) The role Cloud Resource Name (CRN). Example CRN:
          'crn:v1:ibmcloud:public:iam-access-management::a/exampleAccountId::customRole:ExampleRoleName'.
    """

    def __init__(
        self,
        display_name: str,
        actions: List[str],
        *,
        description: str = None,
        crn: str = None,
    ) -> None:
        """
        Initialize a Role object.

        :param str display_name: The display name of the role that is shown in the
               console.
        :param List[str] actions: The actions of the role. For more information,
               see [IAM roles and
               actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions).
        :param str description: (optional) The description of the role.
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
        else:
            raise ValueError('Required property \'display_name\' not present in Role JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'actions' in _dict:
            args['actions'] = _dict.get('actions')
        else:
            raise ValueError('Required property \'actions\' not present in Role JSON')
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


class RoleAction:
    """
    An action that can be performed by the policy subject when assigned role.

    :attr str id: Unique identifier for action with structure
          service.resource.action e.g., cbr.rule.read.
    :attr str display_name: Service defined display name for action.
    :attr str description: Service defined description for action.
    """

    def __init__(
        self,
        id: str,
        display_name: str,
        description: str,
    ) -> None:
        """
        Initialize a RoleAction object.

        :param str id: Unique identifier for action with structure
               service.resource.action e.g., cbr.rule.read.
        :param str display_name: Service defined display name for action.
        :param str description: Service defined description for action.
        """
        self.id = id
        self.display_name = display_name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoleAction':
        """Initialize a RoleAction object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in RoleAction JSON')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        else:
            raise ValueError('Required property \'display_name\' not present in RoleAction JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in RoleAction JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoleAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoleAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoleAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoleAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoleCollection:
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
        system_roles: List['Role'] = None,
    ) -> None:
        """
        Initialize a RoleCollection object.

        :param List[CustomRole] custom_roles: (optional) List of custom roles.
        :param List[Role] service_roles: (optional) List of service roles.
        :param List[Role] system_roles: (optional) List of system roles.
        """
        self.custom_roles = custom_roles
        self.service_roles = service_roles
        self.system_roles = system_roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoleCollection':
        """Initialize a RoleCollection object from a json dictionary."""
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
        """Initialize a RoleCollection object from a json dictionary."""
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
        """Return a `str` version of this RoleCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoleCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoleCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Roles:
    """
    A role associated with a policy.

    :attr str role_id: The role Cloud Resource Name (CRN) granted by the policy.
          Example CRN: 'crn:v1:bluemix:public:iam::::role:Editor'.
    """

    def __init__(
        self,
        role_id: str,
    ) -> None:
        """
        Initialize a Roles object.

        :param str role_id: The role Cloud Resource Name (CRN) granted by the
               policy. Example CRN: 'crn:v1:bluemix:public:iam::::role:Editor'.
        """
        self.role_id = role_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Roles':
        """Initialize a Roles object from a json dictionary."""
        args = {}
        if 'role_id' in _dict:
            args['role_id'] = _dict.get('role_id')
        else:
            raise ValueError('Required property \'role_id\' not present in Roles JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Roles object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'role_id') and self.role_id is not None:
            _dict['role_id'] = self.role_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Roles object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Roles') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Roles') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuleAttribute:
    """
    Rule that specifies additional access granted (e.g., time-based condition).

    :attr str key: The name of an attribute.
    :attr str operator: The operator of an attribute.
    :attr object value: The value of a rule or resource attribute; can be boolean or
          string for resource attribute. Can be string or an array of strings (e.g., array
          of days to permit access) for rule attribute.
    """

    def __init__(
        self,
        key: str,
        operator: str,
        value: object,
    ) -> None:
        """
        Initialize a RuleAttribute object.

        :param str key: The name of an attribute.
        :param str operator: The operator of an attribute.
        :param object value: The value of a rule or resource attribute; can be
               boolean or string for resource attribute. Can be string or an array of
               strings (e.g., array of days to permit access) for rule attribute.
        """
        self.key = key
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleAttribute':
        """Initialize a RuleAttribute object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError('Required property \'key\' not present in RuleAttribute JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in RuleAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in RuleAttribute JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleAttribute object from a json dictionary."""
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
        """Return a `str` version of this RuleAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operator of an attribute.
        """

        TIMELESSTHAN = 'timeLessThan'
        TIMELESSTHANOREQUALS = 'timeLessThanOrEquals'
        TIMEGREATERTHAN = 'timeGreaterThan'
        TIMEGREATERTHANOREQUALS = 'timeGreaterThanOrEquals'
        DATETIMELESSTHAN = 'dateTimeLessThan'
        DATETIMELESSTHANOREQUALS = 'dateTimeLessThanOrEquals'
        DATETIMEGREATERTHAN = 'dateTimeGreaterThan'
        DATETIMEGREATERTHANOREQUALS = 'dateTimeGreaterThanOrEquals'
        DAYOFWEEKEQUALS = 'dayOfWeekEquals'
        DAYOFWEEKANYOF = 'dayOfWeekAnyOf'


class SubjectAttribute:
    """
    An attribute associated with a subject.

    :attr str name: The name of an attribute.
    :attr str value: The value of an attribute.
    """

    def __init__(
        self,
        name: str,
        value: str,
    ) -> None:
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


class TemplateMetadata:
    """
    The details of the IAM template that was used to create an enterprise-managed policy
    in your account. When returned, this indicates that the policy is created from and
    managed by a template in the root enterprise account.

    :attr str id: (optional) The policy template ID.
    :attr str version: (optional) Template version.
    :attr str assignment_id: (optional) policy assignment id.
    :attr str root_id: (optional) orchestrator template id.
    :attr str root_version: (optional) orchestrator template version.
    """

    def __init__(
        self,
        *,
        id: str = None,
        version: str = None,
        assignment_id: str = None,
        root_id: str = None,
        root_version: str = None,
    ) -> None:
        """
        Initialize a TemplateMetadata object.

        :param str id: (optional) The policy template ID.
        :param str version: (optional) Template version.
        :param str assignment_id: (optional) policy assignment id.
        :param str root_id: (optional) orchestrator template id.
        :param str root_version: (optional) orchestrator template version.
        """
        self.id = id
        self.version = version
        self.assignment_id = assignment_id
        self.root_id = root_id
        self.root_version = root_version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TemplateMetadata':
        """Initialize a TemplateMetadata object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'assignment_id' in _dict:
            args['assignment_id'] = _dict.get('assignment_id')
        if 'root_id' in _dict:
            args['root_id'] = _dict.get('root_id')
        if 'root_version' in _dict:
            args['root_version'] = _dict.get('root_version')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TemplateMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'assignment_id') and self.assignment_id is not None:
            _dict['assignment_id'] = self.assignment_id
        if hasattr(self, 'root_id') and self.root_id is not None:
            _dict['root_id'] = self.root_id
        if hasattr(self, 'root_version') and self.root_version is not None:
            _dict['root_version'] = self.root_version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TemplateMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TemplateMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TemplateMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TemplatePolicy:
    """
    The core set of properties associated with the template's policy objet.

    :attr str type: The policy type; either 'access' or 'authorization'.
    :attr str description: (optional) Description of the policy. This is shown in
          child accounts when an access group or trusted profile template uses the policy
          template to assign access.
    :attr V2PolicyResource resource: (optional) The resource attributes to which the
          policy grants access.
    :attr str pattern: (optional) Indicates pattern of rule, either
          'time-based-conditions:once', 'time-based-conditions:weekly:all-day', or
          'time-based-conditions:weekly:custom-hours'.
    :attr V2PolicyRule rule: (optional) Additional access conditions associated with
          the policy.
    :attr Control control: Specifies the type of access granted by the policy.
    """

    def __init__(
        self,
        type: str,
        control: 'Control',
        *,
        description: str = None,
        resource: 'V2PolicyResource' = None,
        pattern: str = None,
        rule: 'V2PolicyRule' = None,
    ) -> None:
        """
        Initialize a TemplatePolicy object.

        :param str type: The policy type; either 'access' or 'authorization'.
        :param Control control: Specifies the type of access granted by the policy.
        :param str description: (optional) Description of the policy. This is shown
               in child accounts when an access group or trusted profile template uses the
               policy template to assign access.
        :param V2PolicyResource resource: (optional) The resource attributes to
               which the policy grants access.
        :param str pattern: (optional) Indicates pattern of rule, either
               'time-based-conditions:once', 'time-based-conditions:weekly:all-day', or
               'time-based-conditions:weekly:custom-hours'.
        :param V2PolicyRule rule: (optional) Additional access conditions
               associated with the policy.
        """
        self.type = type
        self.description = description
        self.resource = resource
        self.pattern = pattern
        self.rule = rule
        self.control = control

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TemplatePolicy':
        """Initialize a TemplatePolicy object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TemplatePolicy JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'resource' in _dict:
            args['resource'] = V2PolicyResource.from_dict(_dict.get('resource'))
        if 'pattern' in _dict:
            args['pattern'] = _dict.get('pattern')
        if 'rule' in _dict:
            args['rule'] = _dict.get('rule')
        if 'control' in _dict:
            args['control'] = Control.from_dict(_dict.get('control'))
        else:
            raise ValueError('Required property \'control\' not present in TemplatePolicy JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TemplatePolicy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
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
        if hasattr(self, 'control') and self.control is not None:
            if isinstance(self.control, dict):
                _dict['control'] = self.control
            else:
                _dict['control'] = self.control.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TemplatePolicy object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TemplatePolicy') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TemplatePolicy') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The policy type; either 'access' or 'authorization'.
        """

        ACCESS = 'access'
        AUTHORIZATION = 'authorization'


class V2Policy:
    """
    The core set of properties associated with the policy.

    :attr str type: The policy type; either 'access' or 'authorization'.
    :attr str description: (optional) Description of the policy.
    :attr V2PolicySubject subject: (optional) The subject attributes for whom the
          policy grants access.
    :attr V2PolicyResource resource: (optional) The resource attributes to which the
          policy grants access.
    :attr str pattern: (optional) Indicates pattern of rule, either
          'time-based-conditions:once', 'time-based-conditions:weekly:all-day', or
          'time-based-conditions:weekly:custom-hours'.
    :attr V2PolicyRule rule: (optional) Additional access conditions associated with
          the policy.
    :attr str id: (optional) The policy ID.
    :attr str href: (optional) The href URL that links to the policies API by policy
          ID.
    :attr ControlResponse control:
    :attr datetime created_at: (optional) The UTC timestamp when the policy was
          created.
    :attr str created_by_id: (optional) The iam ID of the entity that created the
          policy.
    :attr datetime last_modified_at: (optional) The UTC timestamp when the policy
          was last modified.
    :attr str last_modified_by_id: (optional) The iam ID of the entity that last
          modified the policy.
    :attr str state: The policy state, either 'deleted' or 'active'.
    :attr str last_permit_at: (optional) The optional last permit time of policy,
          when passing query parameter format=include_last_permit.
    :attr int last_permit_frequency: (optional) The optional count of times that
          policy has provided a permit, when passing query parameter
          format=include_last_permit.
    """

    def __init__(
        self,
        type: str,
        control: 'ControlResponse',
        state: str,
        *,
        description: str = None,
        subject: 'V2PolicySubject' = None,
        resource: 'V2PolicyResource' = None,
        pattern: str = None,
        rule: 'V2PolicyRule' = None,
        id: str = None,
        href: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
        last_permit_at: str = None,
        last_permit_frequency: int = None,
    ) -> None:
        """
        Initialize a V2Policy object.

        :param str type: The policy type; either 'access' or 'authorization'.
        :param ControlResponse control:
        :param str state: The policy state, either 'deleted' or 'active'.
        :param str description: (optional) Description of the policy.
        :param V2PolicySubject subject: (optional) The subject attributes for whom
               the policy grants access.
        :param V2PolicyResource resource: (optional) The resource attributes to
               which the policy grants access.
        :param str pattern: (optional) Indicates pattern of rule, either
               'time-based-conditions:once', 'time-based-conditions:weekly:all-day', or
               'time-based-conditions:weekly:custom-hours'.
        :param V2PolicyRule rule: (optional) Additional access conditions
               associated with the policy.
        :param str last_permit_at: (optional) The optional last permit time of
               policy, when passing query parameter format=include_last_permit.
        :param int last_permit_frequency: (optional) The optional count of times
               that policy has provided a permit, when passing query parameter
               format=include_last_permit.
        """
        self.type = type
        self.description = description
        self.subject = subject
        self.resource = resource
        self.pattern = pattern
        self.rule = rule
        self.id = id
        self.href = href
        self.control = control
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id
        self.state = state
        self.last_permit_at = last_permit_at
        self.last_permit_frequency = last_permit_frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2Policy':
        """Initialize a V2Policy object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in V2Policy JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'subject' in _dict:
            args['subject'] = V2PolicySubject.from_dict(_dict.get('subject'))
        if 'resource' in _dict:
            args['resource'] = V2PolicyResource.from_dict(_dict.get('resource'))
        if 'pattern' in _dict:
            args['pattern'] = _dict.get('pattern')
        if 'rule' in _dict:
            args['rule'] = _dict.get('rule')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'control' in _dict:
            args['control'] = _dict.get('control')
        else:
            raise ValueError('Required property \'control\' not present in V2Policy JSON')
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
        else:
            raise ValueError('Required property \'state\' not present in V2Policy JSON')
        if 'last_permit_at' in _dict:
            args['last_permit_at'] = _dict.get('last_permit_at')
        if 'last_permit_frequency' in _dict:
            args['last_permit_frequency'] = _dict.get('last_permit_frequency')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2Policy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'subject') and self.subject is not None:
            if isinstance(self.subject, dict):
                _dict['subject'] = self.subject
            else:
                _dict['subject'] = self.subject.to_dict()
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
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'control') and self.control is not None:
            if isinstance(self.control, dict):
                _dict['control'] = self.control
            else:
                _dict['control'] = self.control.to_dict()
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
        if hasattr(self, 'last_permit_at') and self.last_permit_at is not None:
            _dict['last_permit_at'] = self.last_permit_at
        if hasattr(self, 'last_permit_frequency') and self.last_permit_frequency is not None:
            _dict['last_permit_frequency'] = self.last_permit_frequency
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

    class TypeEnum(str, Enum):
        """
        The policy type; either 'access' or 'authorization'.
        """

        ACCESS = 'access'
        AUTHORIZATION = 'authorization'

    class StateEnum(str, Enum):
        """
        The policy state, either 'deleted' or 'active'.
        """

        ACTIVE = 'active'
        DELETED = 'deleted'


class V2PolicyCollection:
    """
    A collection of policies.

    :attr List[V2PolicyTemplateMetaData] policies: (optional) List of policies.
    """

    def __init__(
        self,
        *,
        policies: List['V2PolicyTemplateMetaData'] = None,
    ) -> None:
        """
        Initialize a V2PolicyCollection object.

        :param List[V2PolicyTemplateMetaData] policies: (optional) List of
               policies.
        """
        self.policies = policies

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyCollection':
        """Initialize a V2PolicyCollection object from a json dictionary."""
        args = {}
        if 'policies' in _dict:
            args['policies'] = [V2PolicyTemplateMetaData.from_dict(v) for v in _dict.get('policies')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyCollection object from a json dictionary."""
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
        """Return a `str` version of this V2PolicyCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicyResource:
    """
    The resource attributes to which the policy grants access.

    :attr List[V2PolicyResourceAttribute] attributes: List of resource attributes to
          which the policy grants access.
    :attr List[V2PolicyResourceTag] tags: (optional) Optional list of resource tags
          to which the policy grants access.
    """

    def __init__(
        self,
        attributes: List['V2PolicyResourceAttribute'],
        *,
        tags: List['V2PolicyResourceTag'] = None,
    ) -> None:
        """
        Initialize a V2PolicyResource object.

        :param List[V2PolicyResourceAttribute] attributes: List of resource
               attributes to which the policy grants access.
        :param List[V2PolicyResourceTag] tags: (optional) Optional list of resource
               tags to which the policy grants access.
        """
        self.attributes = attributes
        self.tags = tags

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyResource':
        """Initialize a V2PolicyResource object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [V2PolicyResourceAttribute.from_dict(v) for v in _dict.get('attributes')]
        else:
            raise ValueError('Required property \'attributes\' not present in V2PolicyResource JSON')
        if 'tags' in _dict:
            args['tags'] = [V2PolicyResourceTag.from_dict(v) for v in _dict.get('tags')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyResource object from a json dictionary."""
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
        """Return a `str` version of this V2PolicyResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicyResourceAttribute:
    """
    Resource attribute to which the policy grants access.

    :attr str key: The name of a resource attribute.
    :attr str operator: The operator of an attribute.
    :attr object value: The value of a rule or resource attribute; can be boolean or
          string for resource attribute. Can be string or an array of strings (e.g., array
          of days to permit access) for rule attribute.
    """

    def __init__(
        self,
        key: str,
        operator: str,
        value: object,
    ) -> None:
        """
        Initialize a V2PolicyResourceAttribute object.

        :param str key: The name of a resource attribute.
        :param str operator: The operator of an attribute.
        :param object value: The value of a rule or resource attribute; can be
               boolean or string for resource attribute. Can be string or an array of
               strings (e.g., array of days to permit access) for rule attribute.
        """
        self.key = key
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyResourceAttribute':
        """Initialize a V2PolicyResourceAttribute object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError('Required property \'key\' not present in V2PolicyResourceAttribute JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in V2PolicyResourceAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in V2PolicyResourceAttribute JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyResourceAttribute object from a json dictionary."""
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
        """Return a `str` version of this V2PolicyResourceAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyResourceAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyResourceAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operator of an attribute.
        """

        STRINGEQUALS = 'stringEquals'
        STRINGEXISTS = 'stringExists'
        STRINGMATCH = 'stringMatch'


class V2PolicyResourceTag:
    """
    A tag associated with a resource.

    :attr str key: The name of an access management tag.
    :attr str value: The value of an access management tag.
    :attr str operator: The operator of an access management tag.
    """

    def __init__(
        self,
        key: str,
        value: str,
        operator: str,
    ) -> None:
        """
        Initialize a V2PolicyResourceTag object.

        :param str key: The name of an access management tag.
        :param str value: The value of an access management tag.
        :param str operator: The operator of an access management tag.
        """
        self.key = key
        self.value = value
        self.operator = operator

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyResourceTag':
        """Initialize a V2PolicyResourceTag object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError('Required property \'key\' not present in V2PolicyResourceTag JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in V2PolicyResourceTag JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in V2PolicyResourceTag JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyResourceTag object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyResourceTag object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyResourceTag') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyResourceTag') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operator of an access management tag.
        """

        STRINGEQUALS = 'stringEquals'
        STRINGMATCH = 'stringMatch'


class V2PolicyRule:
    """
    Additional access conditions associated with the policy.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a V2PolicyRule object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['V2PolicyRuleRuleAttribute', 'V2PolicyRuleRuleWithConditions'])
        )
        raise Exception(msg)


class V2PolicySubject:
    """
    The subject attributes for whom the policy grants access.

    :attr List[V2PolicySubjectAttribute] attributes: List of subject attributes
          associated with policy/.
    """

    def __init__(
        self,
        attributes: List['V2PolicySubjectAttribute'],
    ) -> None:
        """
        Initialize a V2PolicySubject object.

        :param List[V2PolicySubjectAttribute] attributes: List of subject
               attributes associated with policy/.
        """
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicySubject':
        """Initialize a V2PolicySubject object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [V2PolicySubjectAttribute.from_dict(v) for v in _dict.get('attributes')]
        else:
            raise ValueError('Required property \'attributes\' not present in V2PolicySubject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicySubject object from a json dictionary."""
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
        """Return a `str` version of this V2PolicySubject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicySubject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicySubject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicySubjectAttribute:
    """
    Subject attribute for whom the policy grants access.

    :attr str key: The name of a subject attribute, e.g., iam_id, access_group_id.
    :attr str operator: The operator of an attribute.
    :attr str value: The value of the ID of the subject, e.g., service ID, access
          group ID, IAM ID.
    """

    def __init__(
        self,
        key: str,
        operator: str,
        value: str,
    ) -> None:
        """
        Initialize a V2PolicySubjectAttribute object.

        :param str key: The name of a subject attribute, e.g., iam_id,
               access_group_id.
        :param str operator: The operator of an attribute.
        :param str value: The value of the ID of the subject, e.g., service ID,
               access group ID, IAM ID.
        """
        self.key = key
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicySubjectAttribute':
        """Initialize a V2PolicySubjectAttribute object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError('Required property \'key\' not present in V2PolicySubjectAttribute JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in V2PolicySubjectAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in V2PolicySubjectAttribute JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicySubjectAttribute object from a json dictionary."""
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
        """Return a `str` version of this V2PolicySubjectAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicySubjectAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicySubjectAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operator of an attribute.
        """

        STRINGEQUALS = 'stringEquals'


class V2PolicyTemplateMetaData:
    """
    The core set of properties associated with the policy.

    :attr str type: The policy type; either 'access' or 'authorization'.
    :attr str description: (optional) Description of the policy.
    :attr V2PolicySubject subject: (optional) The subject attributes for whom the
          policy grants access.
    :attr V2PolicyResource resource: (optional) The resource attributes to which the
          policy grants access.
    :attr str pattern: (optional) Indicates pattern of rule, either
          'time-based-conditions:once', 'time-based-conditions:weekly:all-day', or
          'time-based-conditions:weekly:custom-hours'.
    :attr V2PolicyRule rule: (optional) Additional access conditions associated with
          the policy.
    :attr str id: (optional) The policy ID.
    :attr str href: (optional) The href URL that links to the policies API by policy
          ID.
    :attr ControlResponse control:
    :attr datetime created_at: (optional) The UTC timestamp when the policy was
          created.
    :attr str created_by_id: (optional) The iam ID of the entity that created the
          policy.
    :attr datetime last_modified_at: (optional) The UTC timestamp when the policy
          was last modified.
    :attr str last_modified_by_id: (optional) The iam ID of the entity that last
          modified the policy.
    :attr str state: The policy state, either 'deleted' or 'active'.
    :attr str last_permit_at: (optional) The optional last permit time of policy,
          when passing query parameter format=include_last_permit.
    :attr int last_permit_frequency: (optional) The optional count of times that
          policy has provided a permit, when passing query parameter
          format=include_last_permit.
    :attr TemplateMetadata template: (optional) The details of the IAM template that
          was used to create an enterprise-managed policy in your account. When returned,
          this indicates that the policy is created from and managed by a template in the
          root enterprise account.
    """

    def __init__(
        self,
        type: str,
        control: 'ControlResponse',
        state: str,
        *,
        description: str = None,
        subject: 'V2PolicySubject' = None,
        resource: 'V2PolicyResource' = None,
        pattern: str = None,
        rule: 'V2PolicyRule' = None,
        id: str = None,
        href: str = None,
        created_at: datetime = None,
        created_by_id: str = None,
        last_modified_at: datetime = None,
        last_modified_by_id: str = None,
        last_permit_at: str = None,
        last_permit_frequency: int = None,
        template: 'TemplateMetadata' = None,
    ) -> None:
        """
        Initialize a V2PolicyTemplateMetaData object.

        :param str type: The policy type; either 'access' or 'authorization'.
        :param ControlResponse control:
        :param str state: The policy state, either 'deleted' or 'active'.
        :param str description: (optional) Description of the policy.
        :param V2PolicySubject subject: (optional) The subject attributes for whom
               the policy grants access.
        :param V2PolicyResource resource: (optional) The resource attributes to
               which the policy grants access.
        :param str pattern: (optional) Indicates pattern of rule, either
               'time-based-conditions:once', 'time-based-conditions:weekly:all-day', or
               'time-based-conditions:weekly:custom-hours'.
        :param V2PolicyRule rule: (optional) Additional access conditions
               associated with the policy.
        :param str last_permit_at: (optional) The optional last permit time of
               policy, when passing query parameter format=include_last_permit.
        :param int last_permit_frequency: (optional) The optional count of times
               that policy has provided a permit, when passing query parameter
               format=include_last_permit.
        :param TemplateMetadata template: (optional) The details of the IAM
               template that was used to create an enterprise-managed policy in your
               account. When returned, this indicates that the policy is created from and
               managed by a template in the root enterprise account.
        """
        self.type = type
        self.description = description
        self.subject = subject
        self.resource = resource
        self.pattern = pattern
        self.rule = rule
        self.id = id
        self.href = href
        self.control = control
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id
        self.state = state
        self.last_permit_at = last_permit_at
        self.last_permit_frequency = last_permit_frequency
        self.template = template

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyTemplateMetaData':
        """Initialize a V2PolicyTemplateMetaData object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in V2PolicyTemplateMetaData JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'subject' in _dict:
            args['subject'] = V2PolicySubject.from_dict(_dict.get('subject'))
        if 'resource' in _dict:
            args['resource'] = V2PolicyResource.from_dict(_dict.get('resource'))
        if 'pattern' in _dict:
            args['pattern'] = _dict.get('pattern')
        if 'rule' in _dict:
            args['rule'] = _dict.get('rule')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'control' in _dict:
            args['control'] = _dict.get('control')
        else:
            raise ValueError('Required property \'control\' not present in V2PolicyTemplateMetaData JSON')
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
        else:
            raise ValueError('Required property \'state\' not present in V2PolicyTemplateMetaData JSON')
        if 'last_permit_at' in _dict:
            args['last_permit_at'] = _dict.get('last_permit_at')
        if 'last_permit_frequency' in _dict:
            args['last_permit_frequency'] = _dict.get('last_permit_frequency')
        if 'template' in _dict:
            args['template'] = TemplateMetadata.from_dict(_dict.get('template'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyTemplateMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'subject') and self.subject is not None:
            if isinstance(self.subject, dict):
                _dict['subject'] = self.subject
            else:
                _dict['subject'] = self.subject.to_dict()
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
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'control') and self.control is not None:
            if isinstance(self.control, dict):
                _dict['control'] = self.control
            else:
                _dict['control'] = self.control.to_dict()
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
        if hasattr(self, 'last_permit_at') and self.last_permit_at is not None:
            _dict['last_permit_at'] = self.last_permit_at
        if hasattr(self, 'last_permit_frequency') and self.last_permit_frequency is not None:
            _dict['last_permit_frequency'] = self.last_permit_frequency
        if hasattr(self, 'template') and self.template is not None:
            if isinstance(self.template, dict):
                _dict['template'] = self.template
            else:
                _dict['template'] = self.template.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this V2PolicyTemplateMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyTemplateMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyTemplateMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The policy type; either 'access' or 'authorization'.
        """

        ACCESS = 'access'
        AUTHORIZATION = 'authorization'

    class StateEnum(str, Enum):
        """
        The policy state, either 'deleted' or 'active'.
        """

        ACTIVE = 'active'
        DELETED = 'deleted'


class ControlResponseControl(ControlResponse):
    """
    Specifies the type of access granted by the policy.

    :attr Grant grant: Permission granted by the policy.
    """

    def __init__(
        self,
        grant: 'Grant',
    ) -> None:
        """
        Initialize a ControlResponseControl object.

        :param Grant grant: Permission granted by the policy.
        """
        # pylint: disable=super-init-not-called
        self.grant = grant

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlResponseControl':
        """Initialize a ControlResponseControl object from a json dictionary."""
        args = {}
        if 'grant' in _dict:
            args['grant'] = Grant.from_dict(_dict.get('grant'))
        else:
            raise ValueError('Required property \'grant\' not present in ControlResponseControl JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlResponseControl object from a json dictionary."""
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
        """Return a `str` version of this ControlResponseControl object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlResponseControl') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlResponseControl') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlResponseControlWithEnrichedRoles(ControlResponse):
    """
    Specifies the type of access granted by the policy with additional role information.

    :attr GrantWithEnrichedRoles grant: Permission granted by the policy with
          translated roles and additional role information.
    """

    def __init__(
        self,
        grant: 'GrantWithEnrichedRoles',
    ) -> None:
        """
        Initialize a ControlResponseControlWithEnrichedRoles object.

        :param GrantWithEnrichedRoles grant: Permission granted by the policy with
               translated roles and additional role information.
        """
        # pylint: disable=super-init-not-called
        self.grant = grant

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlResponseControlWithEnrichedRoles':
        """Initialize a ControlResponseControlWithEnrichedRoles object from a json dictionary."""
        args = {}
        if 'grant' in _dict:
            args['grant'] = GrantWithEnrichedRoles.from_dict(_dict.get('grant'))
        else:
            raise ValueError('Required property \'grant\' not present in ControlResponseControlWithEnrichedRoles JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlResponseControlWithEnrichedRoles object from a json dictionary."""
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
        """Return a `str` version of this ControlResponseControlWithEnrichedRoles object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlResponseControlWithEnrichedRoles') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlResponseControlWithEnrichedRoles') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class V2PolicyRuleRuleAttribute(V2PolicyRule):
    """
    Rule that specifies additional access granted (e.g., time-based condition).

    :attr str key: The name of an attribute.
    :attr str operator: The operator of an attribute.
    :attr object value: The value of a rule or resource attribute; can be boolean or
          string for resource attribute. Can be string or an array of strings (e.g., array
          of days to permit access) for rule attribute.
    """

    def __init__(
        self,
        key: str,
        operator: str,
        value: object,
    ) -> None:
        """
        Initialize a V2PolicyRuleRuleAttribute object.

        :param str key: The name of an attribute.
        :param str operator: The operator of an attribute.
        :param object value: The value of a rule or resource attribute; can be
               boolean or string for resource attribute. Can be string or an array of
               strings (e.g., array of days to permit access) for rule attribute.
        """
        # pylint: disable=super-init-not-called
        self.key = key
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyRuleRuleAttribute':
        """Initialize a V2PolicyRuleRuleAttribute object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError('Required property \'key\' not present in V2PolicyRuleRuleAttribute JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in V2PolicyRuleRuleAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in V2PolicyRuleRuleAttribute JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyRuleRuleAttribute object from a json dictionary."""
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
        """Return a `str` version of this V2PolicyRuleRuleAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyRuleRuleAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyRuleRuleAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operator of an attribute.
        """

        TIMELESSTHAN = 'timeLessThan'
        TIMELESSTHANOREQUALS = 'timeLessThanOrEquals'
        TIMEGREATERTHAN = 'timeGreaterThan'
        TIMEGREATERTHANOREQUALS = 'timeGreaterThanOrEquals'
        DATETIMELESSTHAN = 'dateTimeLessThan'
        DATETIMELESSTHANOREQUALS = 'dateTimeLessThanOrEquals'
        DATETIMEGREATERTHAN = 'dateTimeGreaterThan'
        DATETIMEGREATERTHANOREQUALS = 'dateTimeGreaterThanOrEquals'
        DAYOFWEEKEQUALS = 'dayOfWeekEquals'
        DAYOFWEEKANYOF = 'dayOfWeekAnyOf'


class V2PolicyRuleRuleWithConditions(V2PolicyRule):
    """
    Rule that specifies additional access granted (e.g., time-based condition) accross
    multiple conditions.

    :attr str operator: Operator to evaluate conditions.
    :attr List[RuleAttribute] conditions: List of conditions associated with a
          policy, e.g., time-based conditions that grant access over a certain time
          period.
    """

    def __init__(
        self,
        operator: str,
        conditions: List['RuleAttribute'],
    ) -> None:
        """
        Initialize a V2PolicyRuleRuleWithConditions object.

        :param str operator: Operator to evaluate conditions.
        :param List[RuleAttribute] conditions: List of conditions associated with a
               policy, e.g., time-based conditions that grant access over a certain time
               period.
        """
        # pylint: disable=super-init-not-called
        self.operator = operator
        self.conditions = conditions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'V2PolicyRuleRuleWithConditions':
        """Initialize a V2PolicyRuleRuleWithConditions object from a json dictionary."""
        args = {}
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in V2PolicyRuleRuleWithConditions JSON')
        if 'conditions' in _dict:
            args['conditions'] = [RuleAttribute.from_dict(v) for v in _dict.get('conditions')]
        else:
            raise ValueError('Required property \'conditions\' not present in V2PolicyRuleRuleWithConditions JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a V2PolicyRuleRuleWithConditions object from a json dictionary."""
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
        """Return a `str` version of this V2PolicyRuleRuleWithConditions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'V2PolicyRuleRuleWithConditions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V2PolicyRuleRuleWithConditions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        Operator to evaluate conditions.
        """

        AND = 'and'
        OR = 'or'
