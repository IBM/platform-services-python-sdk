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
IAM Policy Management API
"""

from datetime import datetime
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

    DEFAULT_SERVICE_URL = 'https://iam.test.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'iam_policy_management'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'IamPolicyManagementV1':
        """
        Return a new client for the iam_policy_management service using the
               specified parameters and external configuration.
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
        Construct a new client for the iam_policy_management service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Policies
    #########################


    def list_policies(self,
        account_id: str,
        *,
        accept_language: str = None,
        iam_id: str = None,
        access_group_id: str = None,
        type: str = None,
        service_type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get policies by attributes.

        Get policies and filter by attributes. While managing policies, you may want to
        retrieve policies in the account and filter by attribute values. This can be done
        through query parameters. Currently, we only support the following attributes:
        account_id, iam_id, access_group_id, type, and service_type. account_id is a
        required query parameter. Only policies that have the specified attributes and
        that the caller has read access to are returned. If the caller does not have read
        access to any policies an empty array is returned.

        :param str account_id: The account GUID in which the policies belong to.
        :param str accept_language: (optional) Translation language code.
        :param str iam_id: (optional) The IAM ID used to identify the subject.
        :param str access_group_id: (optional) The access group id.
        :param str type: (optional) The type of policy (access or authorization).
        :param str service_type: (optional) The type of service.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PolicyList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_policies')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'iam_id': iam_id,
            'access_group_id': access_group_id,
            'type': type,
            'service_type': service_type
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/policies'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_policy(self,
        type: str,
        subjects: List['PolicyRequestSubjectsItem'],
        roles: List['PolicyRequestRolesItem'],
        resources: List['PolicyRequestResourcesItem'],
        *,
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
        ### Access To create an access policy, use **`"type": "access"`** in the body. The
        possible subject attributes are **`iam_id`** and **`access_group_id`**. Use the
        **`iam_id`** subject attribute for assigning access for a user or service-id. Use
        the **`access_group_id`** subject attribute for assigning access for an access
        group. The roles must be a subset of a service's or the platform's supported
        roles. The resource attributes must be a subset of a service's or the platform's
        supported attributes. The policy resource must include either the
        **`serviceType`**, **`serviceName`**,  or **`resourceGroupId`** attribute and the
        **`accountId`** attribute.` If the subject is a locked service-id, the request
        will fail.
        ### Authorization Authorization policies are supported by services on a case by
        case basis. Refer to service documentation to verify their support of
        authorization policies. To create an authorization policy, use **`"type":
        "authorization"`** in the body. The subject attributes must match the supported
        authorization subjects of the resource. Multiple subject attributes might be
        provided. The following attributes are supported:
          serviceName, serviceInstance, region, resourceType, resource, accountId The
        policy roles must be a subset of the supported authorization roles supported by
        the target service. The user must also have the same level of access or greater to
        the target resource in order to grant the role. The resource attributes must be a
        subset of a service's or the platform's supported attributes. Both the policy
        subject and the policy resource must include the **`serviceName`** and
        **`accountId`** attributes.

        :param str type: The policy type; either 'access' or 'authorization'.
        :param List[PolicyRequestSubjectsItem] subjects: The subject attribute
               values that must match in order for this policy to apply in a permission
               decision.
        :param List[PolicyRequestRolesItem] roles: A set of role cloud resource
               names (CRNs) granted by the policy.
        :param List[PolicyRequestResourcesItem] resources: The attributes of the
               resource. Note that only one resource is allowed in a policy.
        :param str accept_language: (optional) Translation language code.
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
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_policy')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'subjects': subjects,
            'roles': roles,
            'resources': resources
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/policies'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def update_policy(self,
        policy_id: str,
        if_match: str,
        type: str,
        subjects: List['PolicyRequestSubjectsItem'],
        roles: List['PolicyRequestRolesItem'],
        resources: List['PolicyRequestResourcesItem'],
        **kwargs
    ) -> DetailedResponse:
        """
        Update a policy.

        Update a policy to grant access between a subject and a resource. A policy
        administrator might want to update an existing policy. The policy type cannot be
        changed (You cannot change an access policy to an authorization policy).
        ### Access To update an access policy, use **`"type": "access"`** in the body. The
        possible subject attributes are **`iam_id`** and **`access_group_id`**. Use the
        **`iam_id`** subject attribute for assigning access for a user or service-id. Use
        the **`access_group_id`** subject attribute for assigning access for an access
        group. The roles must be a subset of a service's or the platform's supported
        roles. The resource attributes must be a subset of a service's or the platform's
        supported attributes. The policy resource must include either the
        **`serviceType`**, **`serviceName`**,  or **`resourceGroupId`** attribute and the
        **`accountId`** attribute.` If the subject is a locked service-id, the request
        will fail.
        ### Authorization To update an authorization policy, use **`"type":
        "authorization"`** in the body. The subject attributes must match the supported
        authorization subjects of the resource. Multiple subject attributes might be
        provided. The following attributes are supported:
          serviceName, serviceInstance, region, resourceType, resource, accountId The
        policy roles must be a subset of the supported authorization roles supported by
        the target service. The user must also have the same level of access or greater to
        the target resource in order to grant the role. The resource attributes must be a
        subset of a service's or the platform's supported attributes. Both the policy
        subject and the policy resource must include the **`serviceName`** and
        **`accountId`** attributes.

        :param str policy_id: The policy ID.
        :param str if_match: The revision number for updating a policy and must
               match the ETag value of the existing policy. The Etag can be retrieved
               using the GET /v1/policies/{policy_id} API and looking at the ETag response
               header.
        :param str type: The policy type; either 'access' or 'authorization'.
        :param List[PolicyRequestSubjectsItem] subjects: The subject attribute
               values that must match in order for this policy to apply in a permission
               decision.
        :param List[PolicyRequestRolesItem] roles: A set of role cloud resource
               names (CRNs) granted by the policy.
        :param List[PolicyRequestResourcesItem] resources: The attributes of the
               resource. Note that only one resource is allowed in a policy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Policy` object
        """

        if policy_id is None:
            raise ValueError('policy_id must be provided')
        if if_match is None:
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
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_policy')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'subjects': subjects,
            'roles': roles,
            'resources': resources
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/policies/{0}'.format(
            *self.encode_path_vars(policy_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_policy(self,
        policy_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a policy by ID.

        Retrieve a policy by providing a policy ID.

        :param str policy_id: The policy ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Policy` object
        """

        if policy_id is None:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_policy')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/policies/{0}'.format(
            *self.encode_path_vars(policy_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_policy(self,
        policy_id: str,
        **kwargs
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

        if policy_id is None:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_policy')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/policies/{0}'.format(
            *self.encode_path_vars(policy_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Roles
    #########################


    def list_roles(self,
        *,
        accept_language: str = None,
        account_id: str = None,
        service_name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get roles by filters.

        Get roles based on the filters. While managing roles, you may want to retrieve
        roles and filter by usages. This can be done through query parameters. Currently,
        we only support the following attributes: account_id, and service_name. Only roles
        that match the filter and that the caller has read access to are returned. If the
        caller does not have read access to any roles an empty array is returned.

        :param str accept_language: (optional) Translation language code.
        :param str account_id: (optional) The account GUID in which the roles
               belong to.
        :param str service_name: (optional) The name of service.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RoleList` object
        """

        headers = {
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_roles')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'service_name': service_name
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/roles'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_role(self,
        name: str,
        account_id: str,
        service_name: str,
        display_name: str,
        actions: List[str],
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

        :param str name: The name of the role that is used in the CRN. Can only be
               alphanumeric and has to be capitalized.
        :param str account_id: The account GUID.
        :param str service_name: The service name.
        :param str display_name: The display name of the role that is shown in the
               console.
        :param List[str] actions: The actions of the role.
        :param str description: (optional) The description of the role.
        :param str accept_language: (optional) Translation language code.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomRole` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if account_id is None:
            raise ValueError('account_id must be provided')
        if service_name is None:
            raise ValueError('service_name must be provided')
        if display_name is None:
            raise ValueError('display_name must be provided')
        if actions is None:
            raise ValueError('actions must be provided')
        headers = {
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_role')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'account_id': account_id,
            'service_name': service_name,
            'display_name': display_name,
            'actions': actions,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/roles'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def update_role(self,
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
        :param List[str] actions: (optional) The actions of the role.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomRole` object
        """

        if role_id is None:
            raise ValueError('role_id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_role')
        headers.update(sdk_headers)

        data = {
            'display_name': display_name,
            'description': description,
            'actions': actions
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/roles/{0}'.format(
            *self.encode_path_vars(role_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_role(self,
        role_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a role by ID.

        Retrieve a role by providing a role ID.

        :param str role_id: The role ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomRole` object
        """

        if role_id is None:
            raise ValueError('role_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_role')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/roles/{0}'.format(
            *self.encode_path_vars(role_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_role(self,
        role_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a role by ID.

        Delete a role by providing a role ID.

        :param str role_id: The role ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if role_id is None:
            raise ValueError('role_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_role')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/roles/{0}'.format(
            *self.encode_path_vars(role_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class PolicyBaseResourcesItem():
    """
    PolicyBaseResourcesItem.

    :attr List[PolicyBaseResourcesItemAttributesItem] attributes: (optional) List of
          resource attributes.
    """

    def __init__(self,
                 *,
                 attributes: List['PolicyBaseResourcesItemAttributesItem'] = None) -> None:
        """
        Initialize a PolicyBaseResourcesItem object.

        :param List[PolicyBaseResourcesItemAttributesItem] attributes: (optional)
               List of resource attributes.
        """
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyBaseResourcesItem':
        """Initialize a PolicyBaseResourcesItem object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [PolicyBaseResourcesItemAttributesItem.from_dict(x) for x in _dict.get('attributes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyBaseResourcesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x.to_dict() for x in self.attributes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyBaseResourcesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyBaseResourcesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyBaseResourcesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PolicyBaseResourcesItemAttributesItem():
    """
    PolicyBaseResourcesItemAttributesItem.

    :attr str name: (optional) The name of an attribute.
    :attr str value: (optional) The value of an attribute.
    :attr str operator: (optional) The operator of an attribute.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 value: str = None,
                 operator: str = None) -> None:
        """
        Initialize a PolicyBaseResourcesItemAttributesItem object.

        :param str name: (optional) The name of an attribute.
        :param str value: (optional) The value of an attribute.
        :param str operator: (optional) The operator of an attribute.
        """
        self.name = name
        self.value = value
        self.operator = operator

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyBaseResourcesItemAttributesItem':
        """Initialize a PolicyBaseResourcesItemAttributesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyBaseResourcesItemAttributesItem object from a json dictionary."""
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
        """Return a `str` version of this PolicyBaseResourcesItemAttributesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyBaseResourcesItemAttributesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyBaseResourcesItemAttributesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PolicyBaseSubjectsItem():
    """
    PolicyBaseSubjectsItem.

    :attr List[PolicyBaseSubjectsItemAttributesItem] attributes: (optional) List of
          subject attributes.
    """

    def __init__(self,
                 *,
                 attributes: List['PolicyBaseSubjectsItemAttributesItem'] = None) -> None:
        """
        Initialize a PolicyBaseSubjectsItem object.

        :param List[PolicyBaseSubjectsItemAttributesItem] attributes: (optional)
               List of subject attributes.
        """
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyBaseSubjectsItem':
        """Initialize a PolicyBaseSubjectsItem object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [PolicyBaseSubjectsItemAttributesItem.from_dict(x) for x in _dict.get('attributes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyBaseSubjectsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x.to_dict() for x in self.attributes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyBaseSubjectsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyBaseSubjectsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyBaseSubjectsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PolicyBaseSubjectsItemAttributesItem():
    """
    PolicyBaseSubjectsItemAttributesItem.

    :attr str name: (optional) The name of an attribute.
    :attr str value: (optional) The value of an attribute.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 value: str = None) -> None:
        """
        Initialize a PolicyBaseSubjectsItemAttributesItem object.

        :param str name: (optional) The name of an attribute.
        :param str value: (optional) The value of an attribute.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyBaseSubjectsItemAttributesItem':
        """Initialize a PolicyBaseSubjectsItemAttributesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyBaseSubjectsItemAttributesItem object from a json dictionary."""
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
        """Return a `str` version of this PolicyBaseSubjectsItemAttributesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyBaseSubjectsItemAttributesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyBaseSubjectsItemAttributesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PolicyRequestResourcesItem():
    """
    PolicyRequestResourcesItem.

    :attr List[PolicyRequestResourcesItemAttributesItem] attributes: List of
          resource attributes.
    """

    def __init__(self,
                 attributes: List['PolicyRequestResourcesItemAttributesItem']) -> None:
        """
        Initialize a PolicyRequestResourcesItem object.

        :param List[PolicyRequestResourcesItemAttributesItem] attributes: List of
               resource attributes.
        """
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyRequestResourcesItem':
        """Initialize a PolicyRequestResourcesItem object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [PolicyRequestResourcesItemAttributesItem.from_dict(x) for x in _dict.get('attributes')]
        else:
            raise ValueError('Required property \'attributes\' not present in PolicyRequestResourcesItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyRequestResourcesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x.to_dict() for x in self.attributes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyRequestResourcesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyRequestResourcesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyRequestResourcesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PolicyRequestResourcesItemAttributesItem():
    """
    PolicyRequestResourcesItemAttributesItem.

    :attr str name: The name of an attribute.
    :attr str value: The value of an attribute.
    :attr str operator: (optional) The operator of an attribute.
    """

    def __init__(self,
                 name: str,
                 value: str,
                 *,
                 operator: str = None) -> None:
        """
        Initialize a PolicyRequestResourcesItemAttributesItem object.

        :param str name: The name of an attribute.
        :param str value: The value of an attribute.
        :param str operator: (optional) The operator of an attribute.
        """
        self.name = name
        self.value = value
        self.operator = operator

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyRequestResourcesItemAttributesItem':
        """Initialize a PolicyRequestResourcesItemAttributesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in PolicyRequestResourcesItemAttributesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in PolicyRequestResourcesItemAttributesItem JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyRequestResourcesItemAttributesItem object from a json dictionary."""
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
        """Return a `str` version of this PolicyRequestResourcesItemAttributesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyRequestResourcesItemAttributesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyRequestResourcesItemAttributesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PolicyRequestRolesItem():
    """
    PolicyRequestRolesItem.

    :attr str role_id: A role cloud resource name (CRN).
    """

    def __init__(self,
                 role_id: str) -> None:
        """
        Initialize a PolicyRequestRolesItem object.

        :param str role_id: A role cloud resource name (CRN).
        """
        self.role_id = role_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyRequestRolesItem':
        """Initialize a PolicyRequestRolesItem object from a json dictionary."""
        args = {}
        if 'role_id' in _dict:
            args['role_id'] = _dict.get('role_id')
        else:
            raise ValueError('Required property \'role_id\' not present in PolicyRequestRolesItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyRequestRolesItem object from a json dictionary."""
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
        """Return a `str` version of this PolicyRequestRolesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyRequestRolesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyRequestRolesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PolicyRequestSubjectsItem():
    """
    PolicyRequestSubjectsItem.

    :attr List[PolicyRequestSubjectsItemAttributesItem] attributes: List of subject
          attributes.
    """

    def __init__(self,
                 attributes: List['PolicyRequestSubjectsItemAttributesItem']) -> None:
        """
        Initialize a PolicyRequestSubjectsItem object.

        :param List[PolicyRequestSubjectsItemAttributesItem] attributes: List of
               subject attributes.
        """
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyRequestSubjectsItem':
        """Initialize a PolicyRequestSubjectsItem object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [PolicyRequestSubjectsItemAttributesItem.from_dict(x) for x in _dict.get('attributes')]
        else:
            raise ValueError('Required property \'attributes\' not present in PolicyRequestSubjectsItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyRequestSubjectsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x.to_dict() for x in self.attributes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyRequestSubjectsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyRequestSubjectsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyRequestSubjectsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PolicyRequestSubjectsItemAttributesItem():
    """
    PolicyRequestSubjectsItemAttributesItem.

    :attr str name: The name of an attribute.
    :attr str value: The value of an attribute.
    """

    def __init__(self,
                 name: str,
                 value: str) -> None:
        """
        Initialize a PolicyRequestSubjectsItemAttributesItem object.

        :param str name: The name of an attribute.
        :param str value: The value of an attribute.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyRequestSubjectsItemAttributesItem':
        """Initialize a PolicyRequestSubjectsItemAttributesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in PolicyRequestSubjectsItemAttributesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in PolicyRequestSubjectsItemAttributesItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyRequestSubjectsItemAttributesItem object from a json dictionary."""
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
        """Return a `str` version of this PolicyRequestSubjectsItemAttributesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyRequestSubjectsItemAttributesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyRequestSubjectsItemAttributesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PolicyRolesItem():
    """
    PolicyRolesItem.

    :attr str role_id: (optional) The role cloud resource name granted by the
          policy.
    :attr str display_name: (optional) The display name of the role.
    :attr str description: (optional) The description of the role.
    """

    def __init__(self,
                 *,
                 role_id: str = None,
                 display_name: str = None,
                 description: str = None) -> None:
        """
        Initialize a PolicyRolesItem object.

        :param str role_id: (optional) The role cloud resource name granted by the
               policy.
        :param str display_name: (optional) The display name of the role.
        :param str description: (optional) The description of the role.
        """
        self.role_id = role_id
        self.display_name = display_name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyRolesItem':
        """Initialize a PolicyRolesItem object from a json dictionary."""
        args = {}
        if 'role_id' in _dict:
            args['role_id'] = _dict.get('role_id')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyRolesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'role_id') and self.role_id is not None:
            _dict['role_id'] = self.role_id
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyRolesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyRolesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyRolesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RoleListCustomRolesItem():
    """
    RoleListCustomRolesItem.

    :attr str id: (optional) The role ID.
    :attr str name: (optional) The name of the role that is used in the CRN. Can
          only be alphanumeric and has to be capitalized.
    :attr str account_id: (optional) The account GUID.
    :attr str service_name: (optional) The service name.
    :attr str display_name: (optional) The display name of the role that is shown in
          the console.
    :attr str description: (optional) The description of the role.
    :attr str crn: (optional) The role CRN.
    :attr List[str] actions: (optional) The actions of the role.
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

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 account_id: str = None,
                 service_name: str = None,
                 display_name: str = None,
                 description: str = None,
                 crn: str = None,
                 actions: List[str] = None,
                 created_at: datetime = None,
                 created_by_id: str = None,
                 last_modified_at: datetime = None,
                 last_modified_by_id: str = None,
                 href: str = None) -> None:
        """
        Initialize a RoleListCustomRolesItem object.

        :param str id: (optional) The role ID.
        :param str name: (optional) The name of the role that is used in the CRN.
               Can only be alphanumeric and has to be capitalized.
        :param str account_id: (optional) The account GUID.
        :param str service_name: (optional) The service name.
        :param str display_name: (optional) The display name of the role that is
               shown in the console.
        :param str description: (optional) The description of the role.
        :param List[str] actions: (optional) The actions of the role.
        :param datetime created_at: (optional) The UTC timestamp when the role was
               created.
        :param str created_by_id: (optional) The iam ID of the entity that created
               the role.
        :param datetime last_modified_at: (optional) The UTC timestamp when the
               role was last modified.
        :param str last_modified_by_id: (optional) The iam ID of the entity that
               last modified the policy.
        :param str href: (optional) The href link back to the role.
        """
        self.id = id
        self.name = name
        self.account_id = account_id
        self.service_name = service_name
        self.display_name = display_name
        self.description = description
        self.crn = crn
        self.actions = actions
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoleListCustomRolesItem':
        """Initialize a RoleListCustomRolesItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'actions' in _dict:
            args['actions'] = _dict.get('actions')
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
        """Initialize a RoleListCustomRolesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'crn') and getattr(self, 'crn') is not None:
            _dict['crn'] = getattr(self, 'crn')
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = self.actions
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'created_by_id') and self.created_by_id is not None:
            _dict['created_by_id'] = self.created_by_id
        if hasattr(self, 'last_modified_at') and self.last_modified_at is not None:
            _dict['last_modified_at'] = datetime_to_string(self.last_modified_at)
        if hasattr(self, 'last_modified_by_id') and self.last_modified_by_id is not None:
            _dict['last_modified_by_id'] = self.last_modified_by_id
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoleListCustomRolesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoleListCustomRolesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoleListCustomRolesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RoleListServiceRolesItem():
    """
    RoleListServiceRolesItem.

    :attr str display_name: (optional) The display name of the role that is shown in
          the console.
    :attr str description: (optional) The description of the role.
    :attr str crn: (optional) The role CRN.
    :attr List[str] actions: (optional) The actions of the role.
    """

    def __init__(self,
                 *,
                 display_name: str = None,
                 description: str = None,
                 crn: str = None,
                 actions: List[str] = None) -> None:
        """
        Initialize a RoleListServiceRolesItem object.

        :param str display_name: (optional) The display name of the role that is
               shown in the console.
        :param str description: (optional) The description of the role.
        :param List[str] actions: (optional) The actions of the role.
        """
        self.display_name = display_name
        self.description = description
        self.crn = crn
        self.actions = actions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoleListServiceRolesItem':
        """Initialize a RoleListServiceRolesItem object from a json dictionary."""
        args = {}
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'actions' in _dict:
            args['actions'] = _dict.get('actions')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoleListServiceRolesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'crn') and getattr(self, 'crn') is not None:
            _dict['crn'] = getattr(self, 'crn')
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = self.actions
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoleListServiceRolesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoleListServiceRolesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoleListServiceRolesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RoleListSystemRolesItem():
    """
    RoleListSystemRolesItem.

    :attr str display_name: (optional) The display name of the role that is shown in
          the console.
    :attr str description: (optional) The description of the role.
    :attr str crn: (optional) The role CRN.
    :attr List[str] actions: (optional) The actions of the role.
    """

    def __init__(self,
                 *,
                 display_name: str = None,
                 description: str = None,
                 crn: str = None,
                 actions: List[str] = None) -> None:
        """
        Initialize a RoleListSystemRolesItem object.

        :param str display_name: (optional) The display name of the role that is
               shown in the console.
        :param str description: (optional) The description of the role.
        :param List[str] actions: (optional) The actions of the role.
        """
        self.display_name = display_name
        self.description = description
        self.crn = crn
        self.actions = actions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoleListSystemRolesItem':
        """Initialize a RoleListSystemRolesItem object from a json dictionary."""
        args = {}
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'actions' in _dict:
            args['actions'] = _dict.get('actions')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoleListSystemRolesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'crn') and getattr(self, 'crn') is not None:
            _dict['crn'] = getattr(self, 'crn')
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = self.actions
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoleListSystemRolesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoleListSystemRolesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoleListSystemRolesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CustomRole():
    """
    CustomRole.

    :attr str id: (optional) The role ID.
    :attr str name: (optional) The name of the role that is used in the CRN. Can
          only be alphanumeric and has to be capitalized.
    :attr str account_id: (optional) The account GUID.
    :attr str service_name: (optional) The service name.
    :attr str display_name: (optional) The display name of the role that is shown in
          the console.
    :attr str description: (optional) The description of the role.
    :attr str crn: (optional) The role CRN.
    :attr List[str] actions: (optional) The actions of the role.
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

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 account_id: str = None,
                 service_name: str = None,
                 display_name: str = None,
                 description: str = None,
                 crn: str = None,
                 actions: List[str] = None,
                 created_at: datetime = None,
                 created_by_id: str = None,
                 last_modified_at: datetime = None,
                 last_modified_by_id: str = None,
                 href: str = None) -> None:
        """
        Initialize a CustomRole object.

        :param str id: (optional) The role ID.
        :param str name: (optional) The name of the role that is used in the CRN.
               Can only be alphanumeric and has to be capitalized.
        :param str account_id: (optional) The account GUID.
        :param str service_name: (optional) The service name.
        :param str display_name: (optional) The display name of the role that is
               shown in the console.
        :param str description: (optional) The description of the role.
        :param List[str] actions: (optional) The actions of the role.
        :param datetime created_at: (optional) The UTC timestamp when the role was
               created.
        :param str created_by_id: (optional) The iam ID of the entity that created
               the role.
        :param datetime last_modified_at: (optional) The UTC timestamp when the
               role was last modified.
        :param str last_modified_by_id: (optional) The iam ID of the entity that
               last modified the policy.
        :param str href: (optional) The href link back to the role.
        """
        self.id = id
        self.name = name
        self.account_id = account_id
        self.service_name = service_name
        self.display_name = display_name
        self.description = description
        self.crn = crn
        self.actions = actions
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
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'actions' in _dict:
            args['actions'] = _dict.get('actions')
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
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'crn') and getattr(self, 'crn') is not None:
            _dict['crn'] = getattr(self, 'crn')
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = self.actions
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'created_by_id') and self.created_by_id is not None:
            _dict['created_by_id'] = self.created_by_id
        if hasattr(self, 'last_modified_at') and self.last_modified_at is not None:
            _dict['last_modified_at'] = datetime_to_string(self.last_modified_at)
        if hasattr(self, 'last_modified_by_id') and self.last_modified_by_id is not None:
            _dict['last_modified_by_id'] = self.last_modified_by_id
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
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

class Policy():
    """
    Policy.

    :attr str id: (optional) The policy ID.
    :attr str type: (optional) The policy type; either 'access' or 'authorization'.
    :attr List[PolicyBaseSubjectsItem] subjects: (optional) The subject attribute
          values that must match in order for this policy to apply in a permission
          decision.
    :attr List[PolicyRolesItem] roles: (optional) A set of role cloud resource names
          (CRNs) granted by the policy.
    :attr List[PolicyBaseResourcesItem] resources: (optional) The attributes of the
          resource. Note that only one resource is allowed in a policy.
    :attr str href: (optional) The href link back to the policy.
    :attr datetime created_at: (optional) The UTC timestamp when the policy was
          created.
    :attr str created_by_id: (optional) The iam ID of the entity that created the
          policy.
    :attr datetime last_modified_at: (optional) The UTC timestamp when the policy
          was last modified.
    :attr str last_modified_by_id: (optional) The iam ID of the entity that last
          modified the policy.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 type: str = None,
                 subjects: List['PolicyBaseSubjectsItem'] = None,
                 roles: List['PolicyRolesItem'] = None,
                 resources: List['PolicyBaseResourcesItem'] = None,
                 href: str = None,
                 created_at: datetime = None,
                 created_by_id: str = None,
                 last_modified_at: datetime = None,
                 last_modified_by_id: str = None) -> None:
        """
        Initialize a Policy object.

        :param str id: (optional) The policy ID.
        :param str type: (optional) The policy type; either 'access' or
               'authorization'.
        :param List[PolicyBaseSubjectsItem] subjects: (optional) The subject
               attribute values that must match in order for this policy to apply in a
               permission decision.
        :param List[PolicyRolesItem] roles: (optional) A set of role cloud resource
               names (CRNs) granted by the policy.
        :param List[PolicyBaseResourcesItem] resources: (optional) The attributes
               of the resource. Note that only one resource is allowed in a policy.
        :param str href: (optional) The href link back to the policy.
        :param datetime created_at: (optional) The UTC timestamp when the policy
               was created.
        :param str created_by_id: (optional) The iam ID of the entity that created
               the policy.
        :param datetime last_modified_at: (optional) The UTC timestamp when the
               policy was last modified.
        :param str last_modified_by_id: (optional) The iam ID of the entity that
               last modified the policy.
        """
        self.id = id
        self.type = type
        self.subjects = subjects
        self.roles = roles
        self.resources = resources
        self.href = href
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Policy':
        """Initialize a Policy object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'subjects' in _dict:
            args['subjects'] = [PolicyBaseSubjectsItem.from_dict(x) for x in _dict.get('subjects')]
        if 'roles' in _dict:
            args['roles'] = [PolicyRolesItem.from_dict(x) for x in _dict.get('roles')]
        if 'resources' in _dict:
            args['resources'] = [PolicyBaseResourcesItem.from_dict(x) for x in _dict.get('resources')]
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
        """Initialize a Policy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'subjects') and self.subjects is not None:
            _dict['subjects'] = [x.to_dict() for x in self.subjects]
        if hasattr(self, 'roles') and self.roles is not None:
            _dict['roles'] = [x.to_dict() for x in self.roles]
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
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

class PolicyList():
    """
    PolicyList.

    :attr List[Policy] policies: (optional) List of policies.
    """

    def __init__(self,
                 *,
                 policies: List['Policy'] = None) -> None:
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
            args['policies'] = [Policy.from_dict(x) for x in _dict.get('policies')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'policies') and self.policies is not None:
            _dict['policies'] = [x.to_dict() for x in self.policies]
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

class RoleList():
    """
    RoleList.

    :attr List[RoleListCustomRolesItem] custom_roles: (optional) List of custom
          roles.
    :attr List[RoleListServiceRolesItem] service_roles: (optional) List of service
          roles.
    :attr List[RoleListSystemRolesItem] system_roles: (optional) List of system
          roles.
    """

    def __init__(self,
                 *,
                 custom_roles: List['RoleListCustomRolesItem'] = None,
                 service_roles: List['RoleListServiceRolesItem'] = None,
                 system_roles: List['RoleListSystemRolesItem'] = None) -> None:
        """
        Initialize a RoleList object.

        :param List[RoleListCustomRolesItem] custom_roles: (optional) List of
               custom roles.
        :param List[RoleListServiceRolesItem] service_roles: (optional) List of
               service roles.
        :param List[RoleListSystemRolesItem] system_roles: (optional) List of
               system roles.
        """
        self.custom_roles = custom_roles
        self.service_roles = service_roles
        self.system_roles = system_roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoleList':
        """Initialize a RoleList object from a json dictionary."""
        args = {}
        if 'custom_roles' in _dict:
            args['custom_roles'] = [RoleListCustomRolesItem.from_dict(x) for x in _dict.get('custom_roles')]
        if 'service_roles' in _dict:
            args['service_roles'] = [RoleListServiceRolesItem.from_dict(x) for x in _dict.get('service_roles')]
        if 'system_roles' in _dict:
            args['system_roles'] = [RoleListSystemRolesItem.from_dict(x) for x in _dict.get('system_roles')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoleList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'custom_roles') and self.custom_roles is not None:
            _dict['custom_roles'] = [x.to_dict() for x in self.custom_roles]
        if hasattr(self, 'service_roles') and self.service_roles is not None:
            _dict['service_roles'] = [x.to_dict() for x in self.service_roles]
        if hasattr(self, 'system_roles') and self.system_roles is not None:
            _dict['system_roles'] = [x.to_dict() for x in self.system_roles]
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
