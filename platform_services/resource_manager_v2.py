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
Manage lifecycle of your Cloud resource groups using Resource Manager APIs.
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class ResourceManagerV2(BaseService):
    """The Resource Manager V2 service."""

    DEFAULT_SERVICE_URL = 'https://resource-controller.test.cloud.ibm.com/v2'
    DEFAULT_SERVICE_NAME = 'resource_manager'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ResourceManagerV2':
        """
        Return a new client for the Resource Manager service using the specified
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
        Construct a new client for the Resource Manager service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # accountQuotas
    #########################


    def get_account_quota_list(self, account_id: str, **kwargs) -> DetailedResponse:
        """
        Retrieve a list of quotas in an account.

        Retrieve a list of all "merged" quota definition for the specified account.You can
        use the IAM service token or a user token for authorization. To use this method,
        the requesting user or service ID must have at least the viewer, editor, operator,
        or administrator role on the Resource Controller service. The merge operation
        takes the default quota definition for each resource type, and if there is a delta
        override quota definition defined for the specified account, the override values
        will replace any corresponding values in the default quota specification.

        :param str account_id: The account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `QuotaDefinitions` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_account_quota_list')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/quota_definitions/accounts/{0}'.format(*self.encode_path_vars(account_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_resource_quota(self, account_id: str, resource_type: str, **kwargs) -> DetailedResponse:
        """
        Retrieve a quota of a resource in an account.

        Retrieve a "merged" quota definition for the specified account and type of
        resource. You can use the IAM service token or a user token for authorization. To
        use this method, the requesting user or service ID must have at least the viewer,
        editor, operator, or administrator role on the Resource Controller service. The
        merge operation takes the default quota definition for the specified resource
        type, and if there is a delta override quota definition defined for the specified
        account, the override values will replace any corresponding values in the default
        quota specification.

        :param str account_id: The account ID.
        :param str resource_type: The type of resource.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceQuota` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if resource_type is None:
            raise ValueError('resource_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_resource_quota')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/quota_definitions/accounts/{0}/resource_types/{1}'.format(*self.encode_path_vars(account_id, resource_type))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_resource_quota(self, account_id: str, resource_type: str, **kwargs) -> DetailedResponse:
        """
        Update a quota for a resource in an account.

        Override a quota definition for a specified account and type of resource,
        replacing any previous quota definition defined for the account and resource type.
        You can use the IAM service token or a user token for authorization. To use this
        method, the requesting user or service ID must have at least editor or
        administrator role on the Resource Controller service.

        :param str account_id: The account ID.
        :param str resource_type: The type of resource.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ErrorCollection` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if resource_type is None:
            raise ValueError('resource_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='update_resource_quota')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/quota_definitions/accounts/{0}/resource_types/{1}'.format(*self.encode_path_vars(account_id, resource_type))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_resource_quota(self, account_id: str, resource_type: str, **kwargs) -> DetailedResponse:
        """
        Delete a quota for a resource in an account.

        Deletes a quota definition if one has been defined for a specified account and
        type of resource, the default quota values for the resource type will still be
        effective. You can use the IAM service token or a user token for authorization. To
        use this method, the requesting user or service ID must have administrator role on
        the Resource Controller service.

        :param str account_id: The account ID.
        :param str resource_type: The type of resource.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ErrorCollection` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if resource_type is None:
            raise ValueError('resource_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_resource_quota')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/quota_definitions/accounts/{0}/resource_types/{1}'.format(*self.encode_path_vars(account_id, resource_type))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_default_resource_quota(self, resource_type: str, **kwargs) -> DetailedResponse:
        """
        Create a default resource quota for a resource type.

        Create a default resource quota for a resource type. You can use the IAM service
        token or a user token for authorization. To use this method, the requesting user
        or service ID must have at least editor or administrator role on the Resource
        Controller service.

        :param str resource_type: The resource type.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ErrorCollection` object
        """

        if resource_type is None:
            raise ValueError('resource_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_default_resource_quota')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/quota_definitions/resource_types/{0}'.format(*self.encode_path_vars(resource_type))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_schema(self, resource_type: str, **kwargs) -> DetailedResponse:
        """
        Create a schema for a resource type.

        Create a schema for a resource type. You can use the IAM service token or a user
        token for authorization. To use this method, the requesting user or service ID
        must have at least editor or administrator role on the Resource Controller
        service.

        :param str resource_type: The resource type.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ErrorCollection` object
        """

        if resource_type is None:
            raise ValueError('resource_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_schema')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/quota_definitions/resource_types/{0}/schemas'.format(*self.encode_path_vars(resource_type))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_schema(self, resource_type: str, **kwargs) -> DetailedResponse:
        """
        Retrieve a schema for a resource type.

        Retrieve a schema for a resource type. You can use the IAM service token or a user
        token for authorization. To use this method, the requesting user or service ID
        must have at least editor or administrator role on the Resource Controller
        service.

        :param str resource_type: The resource type.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceQuota` object
        """

        if resource_type is None:
            raise ValueError('resource_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_schema')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/quota_definitions/resource_types/{0}/schemas'.format(*self.encode_path_vars(resource_type))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # quotaDefinition
    #########################


    def list_quota_definitions(self, **kwargs) -> DetailedResponse:
        """
        Get a list of all quota definitions.

        Get a list of all quota definitions.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `QuotaDefinitionsList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_quota_definitions')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/quota_definitions'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_quota_definition(self, id: str, **kwargs) -> DetailedResponse:
        """
        Get a quota definition.

        Get a a quota definition.

        :param str id: The id of the quota.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `QuotaDefinitions` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_quota_definition')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/quota_definitions/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # resourceGroup
    #########################


    def list_resource_groups(self, *, account_id: str = None, date: str = None, **kwargs) -> DetailedResponse:
        """
        Get a list of all resource groups.

        Get a list of all resource groups in an account.

        :param str account_id: (optional) The ID of the account that contains the
               resource groups that you want to get.
        :param str date: (optional) The date would be in a format of YYYY-MM which
               returns resource groups exclude the deleted ones before this month.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceGroupsList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_resource_groups')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'date': date
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/resource_groups'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_resource_group(self, *, name: str = None, account_id: str = None, **kwargs) -> DetailedResponse:
        """
        Create a new resource group.

        Create a new resource group in an account.

        :param str name: (optional) The new name of the resource group.
        :param str account_id: (optional) The account id of the resource group.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResCreateResourceGroup` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_resource_group')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'account_id': account_id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/resource_groups'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_resource_group(self, id: str, **kwargs) -> DetailedResponse:
        """
        Get a resource group.

        Retrieve a resource group by ID.

        :param str id: The short or long ID of the alias.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceGroup` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_resource_group')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/resource_groups/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_resource_group(self, id: str, *, name: str = None, state: str = None, **kwargs) -> DetailedResponse:
        """
        Update a resource group.

        Update a resource group by ID.

        :param str id: The short or long ID of the alias.
        :param str name: (optional) The new name of the resource group.
        :param str state: (optional) The state of the resource group.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceGroup` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='update_resource_group')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'state': state
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/resource_groups/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_resource_group(self, id: str, **kwargs) -> DetailedResponse:
        """
        Delete a resource group.

        Delete a resource group by ID.

        :param str id: The short or long ID of the alias.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_resource_group')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/resource_groups/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class ErrorCollection():
    """
    Collection of errors.

    :attr str error_code: (optional) The error code encountered.
    :attr str message: (optional) The error message.
    :attr str status_code: (optional) The status code.
    :attr str transaction_id: (optional) The transaction-id of the request.
    """

    def __init__(self, *, error_code: str = None, message: str = None, status_code: str = None, transaction_id: str = None) -> None:
        """
        Initialize a ErrorCollection object.

        :param str error_code: (optional) The error code encountered.
        :param str message: (optional) The error message.
        :param str status_code: (optional) The status code.
        :param str transaction_id: (optional) The transaction-id of the request.
        """
        self.error_code = error_code
        self.message = message
        self.status_code = status_code
        self.transaction_id = transaction_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorCollection':
        """Initialize a ErrorCollection object from a json dictionary."""
        args = {}
        if 'error_code' in _dict:
            args['error_code'] = _dict.get('error_code')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        if 'transaction_id' in _dict:
            args['transaction_id'] = _dict.get('transaction_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'error_code') and self.error_code is not None:
            _dict['error_code'] = self.error_code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        if hasattr(self, 'transaction_id') and self.transaction_id is not None:
            _dict['transaction_id'] = self.transaction_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ErrorCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QuotaDefinitions():
    """
    Returned quota definitions.

    :attr str id: (optional) An alpha-numeric value identifying the quota.
    :attr str name: (optional) The human-readable name of the quota.
    :attr str type: (optional) The type of the quota.
    :attr float number_of_apps: (optional) The total app limit.
    :attr float number_of_service_instances: (optional) The total service instances
          limit per app.
    :attr float default_number_of_instances_per_lite_plan: (optional) Default number
          of instances per lite plan.
    :attr float instances_per_app: (optional) The total instances limit per app.
    :attr str instance_memory: (optional) The total memory of app instance.
    :attr str total_app_memory: (optional) The total app memory capacity.
    :attr float vsi_limit: (optional) The VSI limit.
    :attr ResourceQuota resource_quotas: (optional) Resource quota.
    :attr str created_at: (optional) The date when the quota was initially created.
    :attr str updated_at: (optional) The date when the quota was last updated.
    """

    def __init__(self, *, id: str = None, name: str = None, type: str = None, number_of_apps: float = None, number_of_service_instances: float = None, default_number_of_instances_per_lite_plan: float = None, instances_per_app: float = None, instance_memory: str = None, total_app_memory: str = None, vsi_limit: float = None, resource_quotas: 'ResourceQuota' = None, created_at: str = None, updated_at: str = None) -> None:
        """
        Initialize a QuotaDefinitions object.

        :param str id: (optional) An alpha-numeric value identifying the quota.
        :param str name: (optional) The human-readable name of the quota.
        :param str type: (optional) The type of the quota.
        :param float number_of_apps: (optional) The total app limit.
        :param float number_of_service_instances: (optional) The total service
               instances limit per app.
        :param float default_number_of_instances_per_lite_plan: (optional) Default
               number of instances per lite plan.
        :param float instances_per_app: (optional) The total instances limit per
               app.
        :param str instance_memory: (optional) The total memory of app instance.
        :param str total_app_memory: (optional) The total app memory capacity.
        :param float vsi_limit: (optional) The VSI limit.
        :param ResourceQuota resource_quotas: (optional) Resource quota.
        :param str created_at: (optional) The date when the quota was initially
               created.
        :param str updated_at: (optional) The date when the quota was last updated.
        """
        self.id = id
        self.name = name
        self.type = type
        self.number_of_apps = number_of_apps
        self.number_of_service_instances = number_of_service_instances
        self.default_number_of_instances_per_lite_plan = default_number_of_instances_per_lite_plan
        self.instances_per_app = instances_per_app
        self.instance_memory = instance_memory
        self.total_app_memory = total_app_memory
        self.vsi_limit = vsi_limit
        self.resource_quotas = resource_quotas
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QuotaDefinitions':
        """Initialize a QuotaDefinitions object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'number_of_apps' in _dict:
            args['number_of_apps'] = _dict.get('number_of_apps')
        if 'number_of_service_instances' in _dict:
            args['number_of_service_instances'] = _dict.get('number_of_service_instances')
        if 'default_number_of_instances_per_lite_plan' in _dict:
            args['default_number_of_instances_per_lite_plan'] = _dict.get('default_number_of_instances_per_lite_plan')
        if 'instances_per_app' in _dict:
            args['instances_per_app'] = _dict.get('instances_per_app')
        if 'instance_memory' in _dict:
            args['instance_memory'] = _dict.get('instance_memory')
        if 'total_app_memory' in _dict:
            args['total_app_memory'] = _dict.get('total_app_memory')
        if 'vsi_limit' in _dict:
            args['vsi_limit'] = _dict.get('vsi_limit')
        if 'resource_quotas' in _dict:
            args['resource_quotas'] = ResourceQuota.from_dict(_dict.get('resource_quotas'))
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        if 'updated_at' in _dict:
            args['updated_at'] = _dict.get('updated_at')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QuotaDefinitions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'number_of_apps') and self.number_of_apps is not None:
            _dict['number_of_apps'] = self.number_of_apps
        if hasattr(self, 'number_of_service_instances') and self.number_of_service_instances is not None:
            _dict['number_of_service_instances'] = self.number_of_service_instances
        if hasattr(self, 'default_number_of_instances_per_lite_plan') and self.default_number_of_instances_per_lite_plan is not None:
            _dict['default_number_of_instances_per_lite_plan'] = self.default_number_of_instances_per_lite_plan
        if hasattr(self, 'instances_per_app') and self.instances_per_app is not None:
            _dict['instances_per_app'] = self.instances_per_app
        if hasattr(self, 'instance_memory') and self.instance_memory is not None:
            _dict['instance_memory'] = self.instance_memory
        if hasattr(self, 'total_app_memory') and self.total_app_memory is not None:
            _dict['total_app_memory'] = self.total_app_memory
        if hasattr(self, 'vsi_limit') and self.vsi_limit is not None:
            _dict['vsi_limit'] = self.vsi_limit
        if hasattr(self, 'resource_quotas') and self.resource_quotas is not None:
            _dict['resource_quotas'] = self.resource_quotas.to_dict()
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = self.updated_at
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QuotaDefinitions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QuotaDefinitions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QuotaDefinitions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QuotaDefinitionsList():
    """
    A list of quota definitions.

    :attr List[QuotaDefinitions] resources: List of resources.
    """

    def __init__(self, resources: List['QuotaDefinitions']) -> None:
        """
        Initialize a QuotaDefinitionsList object.

        :param List[QuotaDefinitions] resources: List of resources.
        """
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QuotaDefinitionsList':
        """Initialize a QuotaDefinitionsList object from a json dictionary."""
        args = {}
        if 'resources' in _dict:
            args['resources'] = [QuotaDefinitions.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in QuotaDefinitionsList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QuotaDefinitionsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QuotaDefinitionsList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QuotaDefinitionsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QuotaDefinitionsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResCreateResourceGroup():
    """
    Create a resource group.

    :attr str id: (optional) An alpha-numeric value identifying the resource group.
    :attr str crn: (optional) The full CRN (cloud resource name) associated with the
          resource group. For more on this format, see [Cloud Resource
          Names](https://cloud.ibm.com/docs/resources?topic=resources-crn).
    """

    def __init__(self, *, id: str = None, crn: str = None) -> None:
        """
        Initialize a ResCreateResourceGroup object.

        :param str id: (optional) An alpha-numeric value identifying the resource
               group.
        :param str crn: (optional) The full CRN (cloud resource name) associated
               with the resource group. For more on this format, see [Cloud Resource
               Names](https://cloud.ibm.com/docs/resources?topic=resources-crn).
        """
        self.id = id
        self.crn = crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResCreateResourceGroup':
        """Initialize a ResCreateResourceGroup object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResCreateResourceGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResCreateResourceGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResCreateResourceGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResCreateResourceGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceGroup():
    """
    A resource group.

    :attr str id: (optional) An alpha-numeric value identifying the resource group.
    :attr str crn: (optional) The full CRN (cloud resource name) associated with the
          resource group. For more on this format, see [Cloud Resource
          Names](https://cloud.ibm.com/docs/resources?topic=resources-crn).
    :attr str account_id: (optional) An alpha-numeric value identifying the account
          ID.
    :attr str name: (optional) The human-readable name of the resource group.
    :attr str state: (optional) The state of the resource group.
    :attr bool default: (optional) Identify if this resource group is default of the
          account or not.
    :attr str quota_id: (optional) An alpha-numeric value identifying the quota ID
          associated with the resource group.
    :attr str quota_url: (optional) The URL to access the quota details that
          associated with the resource group.
    :attr str payment_methods_url: (optional) The URL to access the payment methods
          details that associated with the resource group.
    :attr List[object] resource_linkages: (optional) An array of the resources that
          linked to the resource group.
    :attr str teams_url: (optional) The URL to access the team details that
          associated with the resource group.
    :attr str created_at: (optional) The date when the resource group was initially
          created.
    :attr str updated_at: (optional) The date when the resource group was last
          updated.
    """

    def __init__(self, *, id: str = None, crn: str = None, account_id: str = None, name: str = None, state: str = None, default: bool = None, quota_id: str = None, quota_url: str = None, payment_methods_url: str = None, resource_linkages: List[object] = None, teams_url: str = None, created_at: str = None, updated_at: str = None) -> None:
        """
        Initialize a ResourceGroup object.

        :param str id: (optional) An alpha-numeric value identifying the resource
               group.
        :param str crn: (optional) The full CRN (cloud resource name) associated
               with the resource group. For more on this format, see [Cloud Resource
               Names](https://cloud.ibm.com/docs/resources?topic=resources-crn).
        :param str account_id: (optional) An alpha-numeric value identifying the
               account ID.
        :param str name: (optional) The human-readable name of the resource group.
        :param str state: (optional) The state of the resource group.
        :param bool default: (optional) Identify if this resource group is default
               of the account or not.
        :param str quota_id: (optional) An alpha-numeric value identifying the
               quota ID associated with the resource group.
        :param str quota_url: (optional) The URL to access the quota details that
               associated with the resource group.
        :param str payment_methods_url: (optional) The URL to access the payment
               methods details that associated with the resource group.
        :param List[object] resource_linkages: (optional) An array of the resources
               that linked to the resource group.
        :param str teams_url: (optional) The URL to access the team details that
               associated with the resource group.
        :param str created_at: (optional) The date when the resource group was
               initially created.
        :param str updated_at: (optional) The date when the resource group was last
               updated.
        """
        self.id = id
        self.crn = crn
        self.account_id = account_id
        self.name = name
        self.state = state
        self.default = default
        self.quota_id = quota_id
        self.quota_url = quota_url
        self.payment_methods_url = payment_methods_url
        self.resource_linkages = resource_linkages
        self.teams_url = teams_url
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceGroup':
        """Initialize a ResourceGroup object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'default' in _dict:
            args['default'] = _dict.get('default')
        if 'quota_id' in _dict:
            args['quota_id'] = _dict.get('quota_id')
        if 'quota_url' in _dict:
            args['quota_url'] = _dict.get('quota_url')
        if 'payment_methods_url' in _dict:
            args['payment_methods_url'] = _dict.get('payment_methods_url')
        if 'resource_linkages' in _dict:
            args['resource_linkages'] = [object.from_dict(x) for x in _dict.get('resource_linkages')]
        if 'teams_url' in _dict:
            args['teams_url'] = _dict.get('teams_url')
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        if 'updated_at' in _dict:
            args['updated_at'] = _dict.get('updated_at')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
        if hasattr(self, 'quota_id') and self.quota_id is not None:
            _dict['quota_id'] = self.quota_id
        if hasattr(self, 'quota_url') and self.quota_url is not None:
            _dict['quota_url'] = self.quota_url
        if hasattr(self, 'payment_methods_url') and self.payment_methods_url is not None:
            _dict['payment_methods_url'] = self.payment_methods_url
        if hasattr(self, 'resource_linkages') and self.resource_linkages is not None:
            _dict['resource_linkages'] = [x.to_dict() for x in self.resource_linkages]
        if hasattr(self, 'teams_url') and self.teams_url is not None:
            _dict['teams_url'] = self.teams_url
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = self.updated_at
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceGroupsList():
    """
    A list of resource groups.

    :attr List[ResourceGroup] resources: List of resources.
    """

    def __init__(self, resources: List['ResourceGroup']) -> None:
        """
        Initialize a ResourceGroupsList object.

        :param List[ResourceGroup] resources: List of resources.
        """
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceGroupsList':
        """Initialize a ResourceGroupsList object from a json dictionary."""
        args = {}
        if 'resources' in _dict:
            args['resources'] = [ResourceGroup.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in ResourceGroupsList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceGroupsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceGroupsList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceGroupsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceGroupsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceQuota():
    """
    Resource quota.

    :attr str id: (optional) An alpha-numeric value identifying the quota.
    :attr str resource_id: (optional) The human-readable name of the quota.
    :attr str crn: (optional) The full CRN (cloud resource name) associated with the
          quota. For more on this format, see
          https://console.bluemix.net/docs/overview/crn.html#crn.
    :attr float limit: (optional) The limit number of this resource.
    """

    def __init__(self, *, id: str = None, resource_id: str = None, crn: str = None, limit: float = None) -> None:
        """
        Initialize a ResourceQuota object.

        :param str id: (optional) An alpha-numeric value identifying the quota.
        :param str resource_id: (optional) The human-readable name of the quota.
        :param str crn: (optional) The full CRN (cloud resource name) associated
               with the quota. For more on this format, see
               https://console.bluemix.net/docs/overview/crn.html#crn.
        :param float limit: (optional) The limit number of this resource.
        """
        self.id = id
        self.resource_id = resource_id
        self.crn = crn
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceQuota':
        """Initialize a ResourceQuota object from a json dictionary."""
        args = {}
        if '_id' in _dict:
            args['id'] = _dict.get('_id')
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceQuota object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['_id'] = self.id
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceQuota object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceQuota') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceQuota') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


