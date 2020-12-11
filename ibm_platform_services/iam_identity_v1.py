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

# IBM OpenAPI SDK Code Generator Version: 99-SNAPSHOT-d753183b-20201209-163011
 
"""
The IAM Identity Service API allows for the management of Identities (Service IDs,
ApiKeys).
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

class IamIdentityV1(BaseService):
    """The iam_identity V1 service."""

    DEFAULT_SERVICE_URL = 'https://iam.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'iam_identity'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'IamIdentityV1':
        """
        Return a new client for the iam_identity service using the specified
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
        Construct a new client for the iam_identity service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Identity Operations
    #########################


    def list_api_keys(self,
        *,
        account_id: str = None,
        iam_id: str = None,
        pagesize: int = None,
        pagetoken: str = None,
        scope: str = None,
        type: str = None,
        sort: str = None,
        order: str = None,
        include_history: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get API keys for a given service or user IAM ID and account ID.

        Returns the list of API key details for a given service or user IAM ID and account
        ID. Users can manage user API keys for themself, or service ID API keys for
        service IDs that are bound to an entity they have access to. In case of  service
        IDs and their API keys, a user must be either an account owner,  a IBM Cloud org
        manager or IBM Cloud space developer in order to manage  service IDs of the
        entity.

        :param str account_id: (optional) Account ID of the API keys(s) to query.
               If a service IAM ID is specified in iam_id then account_id must match the
               account of the IAM ID. If a user IAM ID is specified in iam_id then then
               account_id must match the account of the Authorization token.
        :param str iam_id: (optional) IAM ID of the API key(s) to be queried. The
               IAM ID may be that of a user or a service. For a user IAM ID iam_id must
               match the Authorization token.
        :param int pagesize: (optional) Optional size of a single page. Default is
               20 items per page. Valid range is 1 to 100.
        :param str pagetoken: (optional) Optional Prev or Next page token returned
               from a previous query execution. Default is start with first page.
        :param str scope: (optional) Optional parameter to define the scope of the
               queried API Keys. Can be 'entity' (default) or 'account'.
        :param str type: (optional) Optional parameter to filter the type of the
               queried API Keys. Can be 'user' or 'serviceid'.
        :param str sort: (optional) Optional sort property, valid values are name,
               description, created_at and created_by. If specified, the items are sorted
               by the value of this property.
        :param str order: (optional) Optional sort order, valid values are asc and
               desc. Default: asc.
        :param bool include_history: (optional) Defines if the entity history is
               included in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiKeyList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_api_keys')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'iam_id': iam_id,
            'pagesize': pagesize,
            'pagetoken': pagetoken,
            'scope': scope,
            'type': type,
            'sort': sort,
            'order': order,
            'include_history': include_history
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/apikeys'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_api_key(self,
        name: str,
        iam_id: str,
        *,
        description: str = None,
        account_id: str = None,
        apikey: str = None,
        store_value: bool = None,
        entity_lock: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create an API key.

        Creates an API key for a UserID or service ID. Users can manage user API keys for
        themself, or service ID API keys for  service IDs that are bound to an entity they
        have access to.

        :param str name: Name of the API key. The name is not checked for
               uniqueness. Therefore multiple names with the same value can exist. Access
               is done via the UUID of the API key.
        :param str iam_id: The iam_id that this API key authenticates.
        :param str description: (optional) The optional description of the API key.
               The 'description' property is only available if a description was provided
               during a create of an API key.
        :param str account_id: (optional) The account ID of the API key.
        :param str apikey: (optional) You can optionally passthrough the API key
               value for this API key. If passed, NO validation of that apiKey value is
               done, i.e. the value can be non-URL safe. If omitted, the API key
               management will create an URL safe opaque API key value. The value of the
               API key is checked for uniqueness. Please ensure enough variations when
               passing in this value.
        :param bool store_value: (optional) Send true or false to set whether the
               API key value is retrievable in the future by using the Get details of an
               API key request. If you create an API key for a user, you must specify
               `false` or omit the value. We don't allow storing of API keys for users.
        :param str entity_lock: (optional) Indicates if the API key is locked for
               further write operations. False by default.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiKey` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {
            'Entity-Lock': entity_lock
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_api_key')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'iam_id': iam_id,
            'description': description,
            'account_id': account_id,
            'apikey': apikey,
            'store_value': store_value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/apikeys'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_api_keys_details(self,
        *,
        iam_api_key: str = None,
        include_history: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get details of an API key by its value.

        Returns the details of an API key by its value. Users can manage user API keys for
        themself, or service ID API keys  for service IDs that are bound to an entity they
        have access to.

        :param str iam_api_key: (optional) API key value.
        :param bool include_history: (optional) Defines if the entity history is
               included in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiKey` object
        """

        headers = {
            'IAM-ApiKey': iam_api_key
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_api_keys_details')
        headers.update(sdk_headers)

        params = {
            'include_history': include_history
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/apikeys/details'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_api_key(self,
        id: str,
        *,
        include_history: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get details of an API key.

        Returns the details of an API key. Users can manage user API keys for themself, or
        service ID API keys for  service IDs that are bound to an entity they have access
        to. In case of  service IDs and their API keys, a user must be either an account
        owner,  a IBM Cloud org manager or IBM Cloud space developer in order to manage
        service IDs of the entity.

        :param str id: Unique ID of the API key.
        :param bool include_history: (optional) Defines if the entity history is
               included in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiKey` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_api_key')
        headers.update(sdk_headers)

        params = {
            'include_history': include_history
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/apikeys/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def update_api_key(self,
        id: str,
        if_match: str,
        *,
        name: str = None,
        description: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Updates an API key.

        Updates properties of an API key. This does NOT affect existing access tokens.
        Their token content will stay unchanged until the access token is refreshed. To
        update an API key, pass the property to be modified. To delete one property's
        value, pass the property with an empty value "".Users can manage user API keys for
        themself, or service ID API keys for service IDs that are bound to an entity they
        have access to.

        :param str id: Unique ID of the API key to be updated.
        :param str if_match: Version of the API key to be updated. Specify the
               version that you retrieved when reading the API key. This value  helps
               identifying parallel usage of this API. Pass * to indicate to update any
               version available. This might result in stale updates.
        :param str name: (optional) The name of the API key to update. If specified
               in the request the parameter must not be empty. The name is not checked for
               uniqueness. Failure to this will result in an Error condition.
        :param str description: (optional) The description of the API key to
               update. If specified an empty description will clear the description of the
               API key. If a non empty value is provided the API key will be updated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiKey` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_api_key')
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

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/apikeys/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_api_key(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes an API key.

        Deletes an API key. Existing tokens will remain valid until expired. Refresh
        tokens  will not work any more for this API key. Users can manage user API keys
        for themself, or service ID API  keys for service IDs that are bound to an entity
        they have access  to.

        :param str id: Unique ID of the API key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_api_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/apikeys/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def lock_api_key(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Lock the API key.

        Locks an API key by ID. Users can manage user API keys for themself, or service ID
        API keys for service IDs that are bound to an entity they have access to. In case
        of service IDs and their API keys, a user must be either an account owner, a IBM
        Cloud org manager or IBM Cloud space developer in order to manage service IDs of
        the entity.

        :param str id: Unique ID of the API key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='lock_api_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/apikeys/{id}/lock'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def unlock_api_key(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Unlock the API key.

        Unlocks an API key by ID. Users can manage user API keys for themself, or service
        ID API keys for service IDs that are bound to an entity they have access to. In
        case of service IDs and their API keys, a user must be either an account owner, a
        IBM Cloud org manager or IBM Cloud space developer in order to manage service IDs
        of the entity.

        :param str id: Unique ID of the API key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='unlock_api_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/apikeys/{id}/lock'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_service_ids(self,
        *,
        account_id: str = None,
        name: str = None,
        pagesize: int = None,
        pagetoken: str = None,
        sort: str = None,
        order: str = None,
        include_history: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List service IDs.

        Returns a list of service IDs. Users can manage user API keys for themself, or
        service ID API keys for service IDs that are bound to an entity they have access
        to.

        :param str account_id: (optional) Account ID of the service ID(s) to query.
               This parameter is required (unless using a pagetoken).
        :param str name: (optional) Name of the service ID(s) to query. Optional.20
               items per page. Valid range is 1 to 100.
        :param int pagesize: (optional) Optional size of a single page. Default is
               20 items per page. Valid range is 1 to 100.
        :param str pagetoken: (optional) Optional Prev or Next page token returned
               from a previous query execution. Default is start with first page.
        :param str sort: (optional) Optional sort property, valid values are name,
               description, created_at and modified_at. If specified, the items are sorted
               by the value of this property.
        :param str order: (optional) Optional sort order, valid values are asc and
               desc. Default: asc.
        :param bool include_history: (optional) Defines if the entity history is
               included in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceIdList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_service_ids')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'name': name,
            'pagesize': pagesize,
            'pagetoken': pagetoken,
            'sort': sort,
            'order': order,
            'include_history': include_history
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/serviceids/'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_service_id(self,
        account_id: str,
        name: str,
        *,
        description: str = None,
        unique_instance_crns: List[str] = None,
        apikey: 'ApiKeyInsideCreateServiceIdRequest' = None,
        entity_lock: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a service ID.

        Creates a service ID for an IBM Cloud account. Users can manage user API keys for
        themself, or service ID API keys for service IDs that are bound to an entity they
        have access to.

        :param str account_id: ID of the account the service ID belongs to.
        :param str name: Name of the Service Id. The name is not checked for
               uniqueness. Therefore multiple names with the same value can exist. Access
               is done via the UUID of the Service Id.
        :param str description: (optional) The optional description of the Service
               Id. The 'description' property is only available if a description was
               provided during a create of a Service Id.
        :param List[str] unique_instance_crns: (optional) Optional list of CRNs
               (string array) which point to the services connected to the service ID.
        :param ApiKeyInsideCreateServiceIdRequest apikey: (optional) Parameters for
               the API key in the Create service Id V1 REST request.
        :param str entity_lock: (optional) Indicates if the service ID is locked
               for further write operations. False by default.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceId` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if apikey is not None:
            apikey = convert_model(apikey)
        headers = {
            'Entity-Lock': entity_lock
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_service_id')
        headers.update(sdk_headers)

        data = {
            'account_id': account_id,
            'name': name,
            'description': description,
            'unique_instance_crns': unique_instance_crns,
            'apikey': apikey
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/serviceids/'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_service_id(self,
        id: str,
        *,
        include_history: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get details of a service ID.

        Returns the details of a service ID. Users can manage user API keys for themself,
        or service ID API keys for service IDs that are bound to an entity they have
        access to.

        :param str id: Unique ID of the service ID.
        :param bool include_history: (optional) Defines if the entity history is
               included in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceId` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_service_id')
        headers.update(sdk_headers)

        params = {
            'include_history': include_history
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/serviceids/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def update_service_id(self,
        id: str,
        if_match: str,
        *,
        name: str = None,
        description: str = None,
        unique_instance_crns: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update service ID.

        Updates properties of a service ID. This does NOT affect existing access tokens.
        Their token content will stay unchanged until the access token is refreshed. To
        update a service ID, pass the property to be modified. To delete one property's
        value, pass the property with an empty value "".Users can manage user API keys for
        themself, or service ID API keys for service IDs that are bound to an entity they
        have access to.

        :param str id: Unique ID of the service ID to be updated.
        :param str if_match: Version of the service ID to be updated. Specify the
               version that you retrieved as entity_tag (ETag header) when reading the
               service ID. This value helps identifying parallel usage of this API. Pass *
               to indicate to update any version available. This might result in stale
               updates.
        :param str name: (optional) The name of the service ID to update. If
               specified in the request the parameter must not be empty. The name is not
               checked for uniqueness. Failure to this will result in an Error condition.
        :param str description: (optional) The description of the service ID to
               update. If specified an empty description will clear the description of the
               service ID. If an non empty value is provided the service ID will be
               updated.
        :param List[str] unique_instance_crns: (optional) List of CRNs which point
               to the services connected to this service ID. If specified an empty list
               will clear all existing unique instance crns of the service ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceId` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_service_id')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'unique_instance_crns': unique_instance_crns
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/serviceids/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_service_id(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes a service ID and associated API keys.

        Deletes a service ID and all API keys associated to it. Before deleting the
        service ID, all associated API keys are deleted. In case a Delete Conflict (status
        code 409) a retry of the request may help as the service ID is only deleted if the
        associated API keys were successfully deleted before. Users can manage user API
        keys for themself, or service ID API keys for service IDs that are bound to an
        entity they have access to.

        :param str id: Unique ID of the service ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_service_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/serviceids/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def lock_service_id(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Lock the service ID.

        Locks a service ID by ID. Users can manage user API keys for themself, or service
        ID API keys for service IDs that are bound to an entity they have access to. In
        case of service IDs and their API keys, a user must be either an account owner, a
        IBM Cloud org manager or IBM Cloud space developer in order to manage service IDs
        of the entity.

        :param str id: Unique ID of the service ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='lock_service_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/serviceids/{id}/lock'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def unlock_service_id(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Unlock the service ID.

        Unlocks a service ID by ID. Users can manage user API keys for themself, or
        service ID API keys for service IDs that are bound to an entity they have access
        to. In case of service IDs and their API keys, a user must be either an account
        owner, a IBM Cloud org manager or IBM Cloud space developer in order to manage
        service IDs of the entity.

        :param str id: Unique ID of the service ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='unlock_service_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/serviceids/{id}/lock'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


class ListApiKeysEnums:
    """
    Enums for list_api_keys parameters.
    """

    class Scope(str, Enum):
        """
        Optional parameter to define the scope of the queried API Keys. Can be 'entity'
        (default) or 'account'.
        """
        ENTITY = 'entity'
        ACCOUNT = 'account'
    class Type(str, Enum):
        """
        Optional parameter to filter the type of the queried API Keys. Can be 'user' or
        'serviceid'.
        """
        USER = 'user'
        SERVICEID = 'serviceid'
    class Order(str, Enum):
        """
        Optional sort order, valid values are asc and desc. Default: asc.
        """
        ASC = 'asc'
        DESC = 'desc'


class ListServiceIdsEnums:
    """
    Enums for list_service_ids parameters.
    """

    class Order(str, Enum):
        """
        Optional sort order, valid values are asc and desc. Default: asc.
        """
        ASC = 'asc'
        DESC = 'desc'


##############################################################################
# Models
##############################################################################


class ApiKey():
    """
    Response body format for API key V1 REST requests.

    :attr ResponseContext context: (optional) Context with key properties for
          problem determination.
    :attr str id: Unique identifier of this API Key.
    :attr str entity_tag: (optional) Version of the API Key details object. You need
          to specify this value when updating the API key to avoid stale updates.
    :attr str crn: Cloud Resource Name of the item. Example Cloud Resource Name:
          'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::apikey:1234-9012-5678'.
    :attr bool locked: The API key cannot be changed if set to true.
    :attr datetime created_at: (optional) If set contains a date time string of the
          creation date in ISO format.
    :attr str created_by: IAM ID of the user or service which created the API key.
    :attr datetime modified_at: (optional) If set contains a date time string of the
          last modification date in ISO format.
    :attr str name: Name of the API key. The name is not checked for uniqueness.
          Therefore multiple names with the same value can exist. Access is done via the
          UUID of the API key.
    :attr str description: (optional) The optional description of the API key. The
          'description' property is only available if a description was provided during a
          create of an API key.
    :attr str iam_id: The iam_id that this API key authenticates.
    :attr str account_id: ID of the account that this API key authenticates for.
    :attr str apikey: The API key value. This property only contains the API key
          value for the following cases: create an API key, update a service ID API key
          that stores the API key value as retrievable, or get a service ID API key that
          stores the API key value as retrievable. All other operations don't return the
          API key value, for example all user API key related operations, except for
          create, don't contain the API key value.
    :attr List[EnityHistoryRecord] history: (optional) History of the API key.
    """

    def __init__(self,
                 id: str,
                 crn: str,
                 locked: bool,
                 created_by: str,
                 name: str,
                 iam_id: str,
                 account_id: str,
                 apikey: str,
                 *,
                 context: 'ResponseContext' = None,
                 entity_tag: str = None,
                 created_at: datetime = None,
                 modified_at: datetime = None,
                 description: str = None,
                 history: List['EnityHistoryRecord'] = None) -> None:
        """
        Initialize a ApiKey object.

        :param str id: Unique identifier of this API Key.
        :param str crn: Cloud Resource Name of the item. Example Cloud Resource
               Name:
               'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::apikey:1234-9012-5678'.
        :param bool locked: The API key cannot be changed if set to true.
        :param str created_by: IAM ID of the user or service which created the API
               key.
        :param str name: Name of the API key. The name is not checked for
               uniqueness. Therefore multiple names with the same value can exist. Access
               is done via the UUID of the API key.
        :param str iam_id: The iam_id that this API key authenticates.
        :param str account_id: ID of the account that this API key authenticates
               for.
        :param str apikey: The API key value. This property only contains the API
               key value for the following cases: create an API key, update a service ID
               API key that stores the API key value as retrievable, or get a service ID
               API key that stores the API key value as retrievable. All other operations
               don't return the API key value, for example all user API key related
               operations, except for create, don't contain the API key value.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param str entity_tag: (optional) Version of the API Key details object.
               You need to specify this value when updating the API key to avoid stale
               updates.
        :param datetime created_at: (optional) If set contains a date time string
               of the creation date in ISO format.
        :param datetime modified_at: (optional) If set contains a date time string
               of the last modification date in ISO format.
        :param str description: (optional) The optional description of the API key.
               The 'description' property is only available if a description was provided
               during a create of an API key.
        :param List[EnityHistoryRecord] history: (optional) History of the API key.
        """
        self.context = context
        self.id = id
        self.entity_tag = entity_tag
        self.crn = crn
        self.locked = locked
        self.created_at = created_at
        self.created_by = created_by
        self.modified_at = modified_at
        self.name = name
        self.description = description
        self.iam_id = iam_id
        self.account_id = account_id
        self.apikey = apikey
        self.history = history

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiKey':
        """Initialize a ApiKey object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ResponseContext.from_dict(_dict.get('context'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ApiKey JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ApiKey JSON')
        if 'locked' in _dict:
            args['locked'] = _dict.get('locked')
        else:
            raise ValueError('Required property \'locked\' not present in ApiKey JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        else:
            raise ValueError('Required property \'created_by\' not present in ApiKey JSON')
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ApiKey JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in ApiKey JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in ApiKey JSON')
        if 'apikey' in _dict:
            args['apikey'] = _dict.get('apikey')
        else:
            raise ValueError('Required property \'apikey\' not present in ApiKey JSON')
        if 'history' in _dict:
            args['history'] = [EnityHistoryRecord.from_dict(x) for x in _dict.get('history')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiKey object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'locked') and self.locked is not None:
            _dict['locked'] = self.locked
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'apikey') and self.apikey is not None:
            _dict['apikey'] = self.apikey
        if hasattr(self, 'history') and self.history is not None:
            _dict['history'] = [x.to_dict() for x in self.history]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiKey object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiKey') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiKey') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApiKeyInsideCreateServiceIdRequest():
    """
    Parameters for the API key in the Create service Id V1 REST request.

    :attr str name: Name of the API key. The name is not checked for uniqueness.
          Therefore multiple names with the same value can exist. Access is done via the
          UUID of the API key.
    :attr str description: (optional) The optional description of the API key. The
          'description' property is only available if a description was provided during a
          create of an API key.
    :attr str apikey: (optional) You can optionally passthrough the API key value
          for this API key. If passed, NO validation of that apiKey value is done, i.e.
          the value can be non-URL safe. If omitted, the API key management will create an
          URL safe opaque API key value. The value of the API key is checked for
          uniqueness. Please ensure enough variations when passing in this value.
    :attr bool store_value: (optional) Send true or false to set whether the API key
          value is retrievable in the future by using the Get details of an API key
          request. If you create an API key for a user, you must specify `false` or omit
          the value. We don't allow storing of API keys for users.
    """

    def __init__(self,
                 name: str,
                 *,
                 description: str = None,
                 apikey: str = None,
                 store_value: bool = None) -> None:
        """
        Initialize a ApiKeyInsideCreateServiceIdRequest object.

        :param str name: Name of the API key. The name is not checked for
               uniqueness. Therefore multiple names with the same value can exist. Access
               is done via the UUID of the API key.
        :param str description: (optional) The optional description of the API key.
               The 'description' property is only available if a description was provided
               during a create of an API key.
        :param str apikey: (optional) You can optionally passthrough the API key
               value for this API key. If passed, NO validation of that apiKey value is
               done, i.e. the value can be non-URL safe. If omitted, the API key
               management will create an URL safe opaque API key value. The value of the
               API key is checked for uniqueness. Please ensure enough variations when
               passing in this value.
        :param bool store_value: (optional) Send true or false to set whether the
               API key value is retrievable in the future by using the Get details of an
               API key request. If you create an API key for a user, you must specify
               `false` or omit the value. We don't allow storing of API keys for users.
        """
        self.name = name
        self.description = description
        self.apikey = apikey
        self.store_value = store_value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiKeyInsideCreateServiceIdRequest':
        """Initialize a ApiKeyInsideCreateServiceIdRequest object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ApiKeyInsideCreateServiceIdRequest JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'apikey' in _dict:
            args['apikey'] = _dict.get('apikey')
        if 'store_value' in _dict:
            args['store_value'] = _dict.get('store_value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiKeyInsideCreateServiceIdRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'apikey') and self.apikey is not None:
            _dict['apikey'] = self.apikey
        if hasattr(self, 'store_value') and self.store_value is not None:
            _dict['store_value'] = self.store_value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiKeyInsideCreateServiceIdRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiKeyInsideCreateServiceIdRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiKeyInsideCreateServiceIdRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApiKeyList():
    """
    Response body format for the List API keys V1 REST request.

    :attr ResponseContext context: (optional) Context with key properties for
          problem determination.
    :attr int offset: (optional) The offset of the current page.
    :attr int limit: (optional) Optional size of a single page. Default is 20 items
          per page. Valid range is 1 to 100.
    :attr str first: (optional) Link to the first page.
    :attr str previous: (optional) Link to the previous available page. If
          'previous' property is not part of the response no previous page is available.
    :attr str next: (optional) Link to the next available page. If 'next' property
          is not part of the response no next page is available.
    :attr List[ApiKey] apikeys: List of API keys based on the query paramters and
          the page size. The apikeys array is always part of the response but might be
          empty depending on the query parameters values provided.
    """

    def __init__(self,
                 apikeys: List['ApiKey'],
                 *,
                 context: 'ResponseContext' = None,
                 offset: int = None,
                 limit: int = None,
                 first: str = None,
                 previous: str = None,
                 next: str = None) -> None:
        """
        Initialize a ApiKeyList object.

        :param List[ApiKey] apikeys: List of API keys based on the query paramters
               and the page size. The apikeys array is always part of the response but
               might be empty depending on the query parameters values provided.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param int offset: (optional) The offset of the current page.
        :param int limit: (optional) Optional size of a single page. Default is 20
               items per page. Valid range is 1 to 100.
        :param str first: (optional) Link to the first page.
        :param str previous: (optional) Link to the previous available page. If
               'previous' property is not part of the response no previous page is
               available.
        :param str next: (optional) Link to the next available page. If 'next'
               property is not part of the response no next page is available.
        """
        self.context = context
        self.offset = offset
        self.limit = limit
        self.first = first
        self.previous = previous
        self.next = next
        self.apikeys = apikeys

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiKeyList':
        """Initialize a ApiKeyList object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ResponseContext.from_dict(_dict.get('context'))
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'previous' in _dict:
            args['previous'] = _dict.get('previous')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'apikeys' in _dict:
            args['apikeys'] = [ApiKey.from_dict(x) for x in _dict.get('apikeys')]
        else:
            raise ValueError('Required property \'apikeys\' not present in ApiKeyList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiKeyList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context.to_dict()
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'apikeys') and self.apikeys is not None:
            _dict['apikeys'] = [x.to_dict() for x in self.apikeys]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiKeyList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiKeyList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiKeyList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class EnityHistoryRecord():
    """
    Response body format for an entity history record.

    :attr str timestamp: Timestamp when the action was triggered.
    :attr str iam_id: IAM ID of the identity which triggered the action.
    :attr str iam_id_account: Account of the identity which triggered the action.
    :attr str action: Action of the history entry.
    :attr List[str] params: Params of the history entry.
    :attr str message: Message which summarizes the executed action.
    """

    def __init__(self,
                 timestamp: str,
                 iam_id: str,
                 iam_id_account: str,
                 action: str,
                 params: List[str],
                 message: str) -> None:
        """
        Initialize a EnityHistoryRecord object.

        :param str timestamp: Timestamp when the action was triggered.
        :param str iam_id: IAM ID of the identity which triggered the action.
        :param str iam_id_account: Account of the identity which triggered the
               action.
        :param str action: Action of the history entry.
        :param List[str] params: Params of the history entry.
        :param str message: Message which summarizes the executed action.
        """
        self.timestamp = timestamp
        self.iam_id = iam_id
        self.iam_id_account = iam_id_account
        self.action = action
        self.params = params
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnityHistoryRecord':
        """Initialize a EnityHistoryRecord object from a json dictionary."""
        args = {}
        if 'timestamp' in _dict:
            args['timestamp'] = _dict.get('timestamp')
        else:
            raise ValueError('Required property \'timestamp\' not present in EnityHistoryRecord JSON')
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in EnityHistoryRecord JSON')
        if 'iam_id_account' in _dict:
            args['iam_id_account'] = _dict.get('iam_id_account')
        else:
            raise ValueError('Required property \'iam_id_account\' not present in EnityHistoryRecord JSON')
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError('Required property \'action\' not present in EnityHistoryRecord JSON')
        if 'params' in _dict:
            args['params'] = _dict.get('params')
        else:
            raise ValueError('Required property \'params\' not present in EnityHistoryRecord JSON')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError('Required property \'message\' not present in EnityHistoryRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnityHistoryRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = self.timestamp
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'iam_id_account') and self.iam_id_account is not None:
            _dict['iam_id_account'] = self.iam_id_account
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'params') and self.params is not None:
            _dict['params'] = self.params
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnityHistoryRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnityHistoryRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnityHistoryRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResponseContext():
    """
    Context with key properties for problem determination.

    :attr str transaction_id: (optional) The transaction ID of the inbound REST
          request.
    :attr str operation: (optional) The operation of the inbound REST request.
    :attr str user_agent: (optional) The user agent of the inbound REST request.
    :attr str url: (optional) The URL of that cluster.
    :attr str instance_id: (optional) The instance ID of the server instance
          processing the request.
    :attr str thread_id: (optional) The thread ID of the server instance processing
          the request.
    :attr str host: (optional) The host of the server instance processing the
          request.
    :attr str start_time: (optional) The start time of the request.
    :attr str end_time: (optional) The finish time of the request.
    :attr str elapsed_time: (optional) The elapsed time in msec.
    :attr str cluster_name: (optional) The cluster name.
    """

    def __init__(self,
                 *,
                 transaction_id: str = None,
                 operation: str = None,
                 user_agent: str = None,
                 url: str = None,
                 instance_id: str = None,
                 thread_id: str = None,
                 host: str = None,
                 start_time: str = None,
                 end_time: str = None,
                 elapsed_time: str = None,
                 cluster_name: str = None) -> None:
        """
        Initialize a ResponseContext object.

        :param str transaction_id: (optional) The transaction ID of the inbound
               REST request.
        :param str operation: (optional) The operation of the inbound REST request.
        :param str user_agent: (optional) The user agent of the inbound REST
               request.
        :param str url: (optional) The URL of that cluster.
        :param str instance_id: (optional) The instance ID of the server instance
               processing the request.
        :param str thread_id: (optional) The thread ID of the server instance
               processing the request.
        :param str host: (optional) The host of the server instance processing the
               request.
        :param str start_time: (optional) The start time of the request.
        :param str end_time: (optional) The finish time of the request.
        :param str elapsed_time: (optional) The elapsed time in msec.
        :param str cluster_name: (optional) The cluster name.
        """
        self.transaction_id = transaction_id
        self.operation = operation
        self.user_agent = user_agent
        self.url = url
        self.instance_id = instance_id
        self.thread_id = thread_id
        self.host = host
        self.start_time = start_time
        self.end_time = end_time
        self.elapsed_time = elapsed_time
        self.cluster_name = cluster_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResponseContext':
        """Initialize a ResponseContext object from a json dictionary."""
        args = {}
        if 'transaction_id' in _dict:
            args['transaction_id'] = _dict.get('transaction_id')
        if 'operation' in _dict:
            args['operation'] = _dict.get('operation')
        if 'user_agent' in _dict:
            args['user_agent'] = _dict.get('user_agent')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'thread_id' in _dict:
            args['thread_id'] = _dict.get('thread_id')
        if 'host' in _dict:
            args['host'] = _dict.get('host')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        if 'end_time' in _dict:
            args['end_time'] = _dict.get('end_time')
        if 'elapsed_time' in _dict:
            args['elapsed_time'] = _dict.get('elapsed_time')
        if 'cluster_name' in _dict:
            args['cluster_name'] = _dict.get('cluster_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResponseContext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'transaction_id') and self.transaction_id is not None:
            _dict['transaction_id'] = self.transaction_id
        if hasattr(self, 'operation') and self.operation is not None:
            _dict['operation'] = self.operation
        if hasattr(self, 'user_agent') and self.user_agent is not None:
            _dict['user_agent'] = self.user_agent
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'thread_id') and self.thread_id is not None:
            _dict['thread_id'] = self.thread_id
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'elapsed_time') and self.elapsed_time is not None:
            _dict['elapsed_time'] = self.elapsed_time
        if hasattr(self, 'cluster_name') and self.cluster_name is not None:
            _dict['cluster_name'] = self.cluster_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResponseContext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResponseContext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResponseContext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ServiceId():
    """
    Response body format for service ID V1 REST requests.

    :attr ResponseContext context: (optional) Context with key properties for
          problem determination.
    :attr str id: Unique identifier of this Service Id.
    :attr str iam_id: Cloud wide identifier for identities of this service ID.
    :attr str entity_tag: (optional) Version of the service ID details object. You
          need to specify this value when updating the service ID to avoid stale updates.
    :attr str crn: Cloud Resource Name of the item. Example Cloud Resource Name:
          'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::serviceid:1234-5678-9012'.
    :attr bool locked: The service ID cannot be changed if set to true.
    :attr datetime created_at: (optional) If set contains a date time string of the
          creation date in ISO format.
    :attr datetime modified_at: (optional) If set contains a date time string of the
          last modification date in ISO format.
    :attr str account_id: ID of the account the service ID belongs to.
    :attr str name: Name of the Service Id. The name is not checked for uniqueness.
          Therefore multiple names with the same value can exist. Access is done via the
          UUID of the Service Id.
    :attr str description: (optional) The optional description of the Service Id.
          The 'description' property is only available if a description was provided
          during a create of a Service Id.
    :attr List[str] unique_instance_crns: (optional) Optional list of CRNs (string
          array) which point to the services connected to the service ID.
    :attr List[EnityHistoryRecord] history: (optional) History of the Service ID.
    :attr ApiKey apikey: Response body format for API key V1 REST requests.
    """

    def __init__(self,
                 id: str,
                 iam_id: str,
                 crn: str,
                 locked: bool,
                 account_id: str,
                 name: str,
                 apikey: 'ApiKey',
                 *,
                 context: 'ResponseContext' = None,
                 entity_tag: str = None,
                 created_at: datetime = None,
                 modified_at: datetime = None,
                 description: str = None,
                 unique_instance_crns: List[str] = None,
                 history: List['EnityHistoryRecord'] = None) -> None:
        """
        Initialize a ServiceId object.

        :param str id: Unique identifier of this Service Id.
        :param str iam_id: Cloud wide identifier for identities of this service ID.
        :param str crn: Cloud Resource Name of the item. Example Cloud Resource
               Name:
               'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::serviceid:1234-5678-9012'.
        :param bool locked: The service ID cannot be changed if set to true.
        :param str account_id: ID of the account the service ID belongs to.
        :param str name: Name of the Service Id. The name is not checked for
               uniqueness. Therefore multiple names with the same value can exist. Access
               is done via the UUID of the Service Id.
        :param ApiKey apikey: Response body format for API key V1 REST requests.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param str entity_tag: (optional) Version of the service ID details object.
               You need to specify this value when updating the service ID to avoid stale
               updates.
        :param datetime created_at: (optional) If set contains a date time string
               of the creation date in ISO format.
        :param datetime modified_at: (optional) If set contains a date time string
               of the last modification date in ISO format.
        :param str description: (optional) The optional description of the Service
               Id. The 'description' property is only available if a description was
               provided during a create of a Service Id.
        :param List[str] unique_instance_crns: (optional) Optional list of CRNs
               (string array) which point to the services connected to the service ID.
        :param List[EnityHistoryRecord] history: (optional) History of the Service
               ID.
        """
        self.context = context
        self.id = id
        self.iam_id = iam_id
        self.entity_tag = entity_tag
        self.crn = crn
        self.locked = locked
        self.created_at = created_at
        self.modified_at = modified_at
        self.account_id = account_id
        self.name = name
        self.description = description
        self.unique_instance_crns = unique_instance_crns
        self.history = history
        self.apikey = apikey

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceId':
        """Initialize a ServiceId object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ResponseContext.from_dict(_dict.get('context'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ServiceId JSON')
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in ServiceId JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ServiceId JSON')
        if 'locked' in _dict:
            args['locked'] = _dict.get('locked')
        else:
            raise ValueError('Required property \'locked\' not present in ServiceId JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in ServiceId JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ServiceId JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'unique_instance_crns' in _dict:
            args['unique_instance_crns'] = _dict.get('unique_instance_crns')
        if 'history' in _dict:
            args['history'] = [EnityHistoryRecord.from_dict(x) for x in _dict.get('history')]
        if 'apikey' in _dict:
            args['apikey'] = ApiKey.from_dict(_dict.get('apikey'))
        else:
            raise ValueError('Required property \'apikey\' not present in ServiceId JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceId object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'locked') and self.locked is not None:
            _dict['locked'] = self.locked
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'unique_instance_crns') and self.unique_instance_crns is not None:
            _dict['unique_instance_crns'] = self.unique_instance_crns
        if hasattr(self, 'history') and self.history is not None:
            _dict['history'] = [x.to_dict() for x in self.history]
        if hasattr(self, 'apikey') and self.apikey is not None:
            _dict['apikey'] = self.apikey.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceId object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceId') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceId') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ServiceIdList():
    """
    Response body format for the list service ID V1 REST request.

    :attr ResponseContext context: (optional) Context with key properties for
          problem determination.
    :attr int offset: (optional) The offset of the current page.
    :attr int limit: (optional) Optional size of a single page. Default is 20 items
          per page. Valid range is 1 to 100.
    :attr str first: (optional) Link to the first page.
    :attr str previous: (optional) Link to the previous available page. If
          'previous' property is not part of the response no previous page is available.
    :attr str next: (optional) Link to the next available page. If 'next' property
          is not part of the response no next page is available.
    :attr List[ServiceId] serviceids: List of service IDs based on the query
          paramters and the page size. The service IDs array is always part of the
          response but might be empty depending on the query parameter values provided.
    """

    def __init__(self,
                 serviceids: List['ServiceId'],
                 *,
                 context: 'ResponseContext' = None,
                 offset: int = None,
                 limit: int = None,
                 first: str = None,
                 previous: str = None,
                 next: str = None) -> None:
        """
        Initialize a ServiceIdList object.

        :param List[ServiceId] serviceids: List of service IDs based on the query
               paramters and the page size. The service IDs array is always part of the
               response but might be empty depending on the query parameter values
               provided.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param int offset: (optional) The offset of the current page.
        :param int limit: (optional) Optional size of a single page. Default is 20
               items per page. Valid range is 1 to 100.
        :param str first: (optional) Link to the first page.
        :param str previous: (optional) Link to the previous available page. If
               'previous' property is not part of the response no previous page is
               available.
        :param str next: (optional) Link to the next available page. If 'next'
               property is not part of the response no next page is available.
        """
        self.context = context
        self.offset = offset
        self.limit = limit
        self.first = first
        self.previous = previous
        self.next = next
        self.serviceids = serviceids

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceIdList':
        """Initialize a ServiceIdList object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ResponseContext.from_dict(_dict.get('context'))
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'previous' in _dict:
            args['previous'] = _dict.get('previous')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'serviceids' in _dict:
            args['serviceids'] = [ServiceId.from_dict(x) for x in _dict.get('serviceids')]
        else:
            raise ValueError('Required property \'serviceids\' not present in ServiceIdList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceIdList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context.to_dict()
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'serviceids') and self.serviceids is not None:
            _dict['serviceids'] = [x.to_dict() for x in self.serviceids]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceIdList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceIdList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceIdList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
