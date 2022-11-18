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

# IBM OpenAPI SDK Code Generator Version: 3.47.0-60650593-20220330-200002

"""
The IAM Identity Service API allows for the management of Account Settings and Identities
(Service IDs, ApiKeys).

API Version: 1.0.0
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
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # API key Operations
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

        :param str account_id: (optional) Account ID of the API keys to query. If a
               service IAM ID is specified in iam_id then account_id must match the
               account of the IAM ID. If a user IAM ID is specified in iam_id then then
               account_id must match the account of the Authorization token.
        :param str iam_id: (optional) IAM ID of the API keys to be queried. The IAM
               ID may be that of a user or a service. For a user IAM ID iam_id must match
               the Authorization token.
        :param int pagesize: (optional) Optional size of a single page. Default is
               20 items per page. Valid range is 1 to 100.
        :param str pagetoken: (optional) Optional Prev or Next page token returned
               from a previous query execution. Default is start with first page.
        :param str scope: (optional) Optional parameter to define the scope of the
               queried API keys. Can be 'entity' (default) or 'account'.
        :param str type: (optional) Optional parameter to filter the type of the
               queried API keys. Can be 'user' or 'serviceid'.
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

        response = self.send(request, **kwargs)
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

        response = self.send(request, **kwargs)
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

        response = self.send(request, **kwargs)
        return response


    def get_api_key(self,
        id: str,
        *,
        include_history: bool = None,
        include_activity: bool = None,
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
        :param bool include_activity: (optional) Defines if the entity's activity
               is included in the response. Retrieving activity data is an expensive
               operation, so please only request this when needed.
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
            'include_history': include_history,
            'include_activity': include_activity
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

        response = self.send(request, **kwargs)
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

        response = self.send(request, **kwargs)
        return response


    def delete_api_key(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes an API key.

        Deletes an API key. Existing tokens will remain valid until expired. Users can
        manage user API keys for themself, or service ID API  keys for service IDs that
        are bound to an entity they have access  to.

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

        response = self.send(request, **kwargs)
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

        response = self.send(request, **kwargs)
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

        response = self.send(request, **kwargs)
        return response

    #########################
    # Service ID Operations
    #########################


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
        to. Note: apikey details are only included in the response when  creating a
        Service ID with an apikey.

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

        response = self.send(request, **kwargs)
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

        response = self.send(request, **kwargs)
        return response


    def get_service_id(self,
        id: str,
        *,
        include_history: bool = None,
        include_activity: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get details of a service ID.

        Returns the details of a service ID. Users can manage user API keys for themself,
        or service ID API keys for service IDs that are bound to an entity they have
        access to. Note: apikey details are only included in the response when  creating a
        Service ID with an apikey.

        :param str id: Unique ID of the service ID.
        :param bool include_history: (optional) Defines if the entity history is
               included in the response.
        :param bool include_activity: (optional) Defines if the entity's activity
               is included in the response. Retrieving activity data is an expensive
               operation, so please only request this when needed.
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
            'include_history': include_history,
            'include_activity': include_activity
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

        response = self.send(request, **kwargs)
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
        have access to.   Note: apikey details are only included in the response when
        creating a  Service ID with an apikey.

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

        response = self.send(request, **kwargs)
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

        response = self.send(request, **kwargs)
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

        response = self.send(request, **kwargs)
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

        response = self.send(request, **kwargs)
        return response

    #########################
    # Trusted Profiles Operations
    #########################


    def create_profile(self,
        name: str,
        account_id: str,
        *,
        description: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a trusted profile.

        Create a trusted profile for a given account ID.

        :param str name: Name of the trusted profile. The name is checked for
               uniqueness. Therefore trusted profiles with the same names can not exist in
               the same account.
        :param str account_id: The account ID of the trusted profile.
        :param str description: (optional) The optional description of the trusted
               profile. The 'description' property is only available if a description was
               provided during creation of trusted profile.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrustedProfile` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_profile')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'account_id': account_id,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/profiles'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def list_profiles(self,
        account_id: str,
        *,
        name: str = None,
        pagesize: int = None,
        sort: str = None,
        order: str = None,
        include_history: bool = None,
        pagetoken: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List trusted profiles.

        List the trusted profiles in an account. The `account_id` query parameter
        determines the account from which to retrieve the list of trusted profiles.

        :param str account_id: Account ID to query for trusted profiles.
        :param str name: (optional) Name of the trusted profile to query.
        :param int pagesize: (optional) Optional size of a single page. Default is
               20 items per page. Valid range is 1 to 100.
        :param str sort: (optional) Optional sort property, valid values are name,
               description, created_at and modified_at. If specified, the items are sorted
               by the value of this property.
        :param str order: (optional) Optional sort order, valid values are asc and
               desc. Default: asc.
        :param bool include_history: (optional) Defines if the entity history is
               included in the response.
        :param str pagetoken: (optional) Optional Prev or Next page token returned
               from a previous query execution. Default is start with first page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrustedProfilesList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_profiles')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'name': name,
            'pagesize': pagesize,
            'sort': sort,
            'order': order,
            'include_history': include_history,
            'pagetoken': pagetoken
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/profiles'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_profile(self,
        profile_id: str,
        *,
        include_activity: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a trusted profile.

        Retrieve a trusted profile by its `profile-id`. Only the trusted profile's data is
        returned (`name`, `description`, `iam_id`, etc.), not the federated users or
        compute resources that qualify to apply the trusted profile.

        :param str profile_id: ID of the trusted profile to get.
        :param bool include_activity: (optional) Defines if the entity's activity
               is included in the response. Retrieving activity data is an expensive
               operation, so please only request this when needed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrustedProfile` object
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_profile')
        headers.update(sdk_headers)

        params = {
            'include_activity': include_activity
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile-id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def update_profile(self,
        profile_id: str,
        if_match: str,
        *,
        name: str = None,
        description: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a trusted profile.

        Update the name or description of an existing trusted profile.

        :param str profile_id: ID of the trusted profile to be updated.
        :param str if_match: Version of the trusted profile to be updated.  Specify
               the version that you retrived when reading list of trusted profiles. This
               value helps to identify any parallel usage of trusted profile. Pass * to
               indicate to update any version available. This might result in stale
               updates.
        :param str name: (optional) The name of the trusted profile to update. If
               specified in the request the parameter must not be empty. The name is
               checked for uniqueness. Failure to this will result in an Error condition.
        :param str description: (optional) The description of the trusted profile
               to update. If specified an empty description will clear the description of
               the trusted profile. If a non empty value is provided the trusted profile
               will be updated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrustedProfile` object
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_profile')
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

        path_param_keys = ['profile-id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_profile(self,
        profile_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a trusted profile.

        Delete a trusted profile. When you delete trusted profile, compute resources and
        federated users are unlinked from the profile and can no longer apply the trusted
        profile identity.

        :param str profile_id: ID of the trusted profile.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_profile')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['profile-id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_claim_rule(self,
        profile_id: str,
        type: str,
        conditions: List['ProfileClaimRuleConditions'],
        *,
        context: 'ResponseContext' = None,
        name: str = None,
        realm_name: str = None,
        cr_type: str = None,
        expiration: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create claim rule for a trusted profile.

        Create a claim rule for a trusted profile. There is a limit of 20 rules per
        trusted profile.

        :param str profile_id: ID of the trusted profile to create a claim rule.
        :param str type: Type of the calim rule, either 'Profile-SAML' or
               'Profile-CR'.
        :param List[ProfileClaimRuleConditions] conditions: Conditions of this
               claim rule.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param str name: (optional) Name of the claim rule to be created or
               updated.
        :param str realm_name: (optional) The realm name of the Idp this claim rule
               applies to. This field is required only if the type is specified as
               'Profile-SAML'.
        :param str cr_type: (optional) The compute resource type the rule applies
               to, required only if type is specified as 'Profile-CR'. Valid values are
               VSI, IKS_SA, ROKS_SA.
        :param int expiration: (optional) Session expiration in seconds, only
               required if type is 'Profile-SAML'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileClaimRule` object
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if conditions is None:
            raise ValueError('conditions must be provided')
        conditions = [convert_model(x) for x in conditions]
        if context is not None:
            context = convert_model(context)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_claim_rule')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'conditions': conditions,
            'context': context,
            'name': name,
            'realm_name': realm_name,
            'cr_type': cr_type,
            'expiration': expiration
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile-id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}/rules'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def list_claim_rules(self,
        profile_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List claim rules for a trusted profile.

        Get a list of all claim rules for a trusted profile. The `profile-id` query
        parameter determines the profile from which to retrieve the list of claim rules.

        :param str profile_id: ID of the trusted profile.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileClaimRuleList` object
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_claim_rules')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile-id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}/rules'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_claim_rule(self,
        profile_id: str,
        rule_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a claim rule for a trusted profile.

        A specific claim rule can be fetched for a given trusted profile ID and rule ID.

        :param str profile_id: ID of the trusted profile.
        :param str rule_id: ID of the claim rule to get.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileClaimRule` object
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_claim_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile-id', 'rule-id']
        path_param_values = self.encode_path_vars(profile_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}/rules/{rule-id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_claim_rule(self,
        profile_id: str,
        rule_id: str,
        if_match: str,
        type: str,
        conditions: List['ProfileClaimRuleConditions'],
        *,
        context: 'ResponseContext' = None,
        name: str = None,
        realm_name: str = None,
        cr_type: str = None,
        expiration: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update claim rule for a trusted profile.

        Update a specific claim rule for a given trusted profile ID and rule ID.

        :param str profile_id: ID of the trusted profile.
        :param str rule_id: ID of the claim rule to update.
        :param str if_match: Version of the claim rule to be updated.  Specify the
               version that you retrived when reading list of claim rules. This value
               helps to identify any parallel usage of claim rule. Pass * to indicate to
               update any version available. This might result in stale updates.
        :param str type: Type of the calim rule, either 'Profile-SAML' or
               'Profile-CR'.
        :param List[ProfileClaimRuleConditions] conditions: Conditions of this
               claim rule.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param str name: (optional) Name of the claim rule to be created or
               updated.
        :param str realm_name: (optional) The realm name of the Idp this claim rule
               applies to. This field is required only if the type is specified as
               'Profile-SAML'.
        :param str cr_type: (optional) The compute resource type the rule applies
               to, required only if type is specified as 'Profile-CR'. Valid values are
               VSI, IKS_SA, ROKS_SA.
        :param int expiration: (optional) Session expiration in seconds, only
               required if type is 'Profile-SAML'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileClaimRule` object
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if conditions is None:
            raise ValueError('conditions must be provided')
        conditions = [convert_model(x) for x in conditions]
        if context is not None:
            context = convert_model(context)
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_claim_rule')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'conditions': conditions,
            'context': context,
            'name': name,
            'realm_name': realm_name,
            'cr_type': cr_type,
            'expiration': expiration
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile-id', 'rule-id']
        path_param_values = self.encode_path_vars(profile_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}/rules/{rule-id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_claim_rule(self,
        profile_id: str,
        rule_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a claim rule.

        Delete a claim rule. When you delete a claim rule, federated user or compute
        resources are no longer required to meet the conditions of the claim rule in order
        to apply the trusted profile.

        :param str profile_id: ID of the trusted profile.
        :param str rule_id: ID of the claim rule to delete.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_claim_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['profile-id', 'rule-id']
        path_param_values = self.encode_path_vars(profile_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}/rules/{rule-id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_link(self,
        profile_id: str,
        cr_type: str,
        link: 'CreateProfileLinkRequestLink',
        *,
        name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create link to a trusted profile.

        Create a direct link between a specific compute resource and a trusted profile,
        rather than creating conditions that a compute resource must fulfill to apply a
        trusted profile.

        :param str profile_id: ID of the trusted profile.
        :param str cr_type: The compute resource type. Valid values are VSI,
               IKS_SA, ROKS_SA.
        :param CreateProfileLinkRequestLink link: Link details.
        :param str name: (optional) Optional name of the Link.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileLink` object
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        if cr_type is None:
            raise ValueError('cr_type must be provided')
        if link is None:
            raise ValueError('link must be provided')
        link = convert_model(link)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_link')
        headers.update(sdk_headers)

        data = {
            'cr_type': cr_type,
            'link': link,
            'name': name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile-id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}/links'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def list_links(self,
        profile_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List links to a trusted profile.

        Get a list of links to a trusted profile.

        :param str profile_id: ID of the trusted profile.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileLinkList` object
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_links')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile-id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}/links'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_link(self,
        profile_id: str,
        link_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get link to a trusted profile.

        Get a specific link to a trusted profile by `link_id`.

        :param str profile_id: ID of the trusted profile.
        :param str link_id: ID of the link.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileLink` object
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        if link_id is None:
            raise ValueError('link_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_link')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile-id', 'link-id']
        path_param_values = self.encode_path_vars(profile_id, link_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}/links/{link-id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_link(self,
        profile_id: str,
        link_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete link to a trusted profile.

        Delete a link between a compute resource and a trusted profile.

        :param str profile_id: ID of the trusted profile.
        :param str link_id: ID of the link.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if profile_id is None:
            raise ValueError('profile_id must be provided')
        if link_id is None:
            raise ValueError('link_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_link')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['profile-id', 'link-id']
        path_param_values = self.encode_path_vars(profile_id, link_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/profiles/{profile-id}/links/{link-id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Account Settings
    #########################


    def get_account_settings(self,
        account_id: str,
        *,
        include_history: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get account configurations.

        Returns the details of an account's configuration.

        :param str account_id: Unique ID of the account.
        :param bool include_history: (optional) Defines if the entity history is
               included in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountSettingsResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_account_settings')
        headers.update(sdk_headers)

        params = {
            'include_history': include_history
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/accounts/{account_id}/settings/identity'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def update_account_settings(self,
        if_match: str,
        account_id: str,
        *,
        restrict_create_service_id: str = None,
        restrict_create_platform_apikey: str = None,
        allowed_ip_addresses: str = None,
        mfa: str = None,
        session_expiration_in_seconds: str = None,
        session_invalidation_in_seconds: str = None,
        max_sessions_per_identity: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update account configurations.

        Allows a user to configure settings on their account with regards to MFA, session
        lifetimes,  access control for creating new identities, and enforcing IP
        restrictions on  token creation.

        :param str if_match: Version of the account settings to be updated. Specify
               the version that you  retrieved as entity_tag (ETag header) when reading
               the account. This value helps  identifying parallel usage of this API. Pass
               * to indicate to update any version  available. This might result in stale
               updates.
        :param str account_id: The id of the account to update the settings for.
        :param str restrict_create_service_id: (optional) Defines whether or not
               creating a Service Id is access controlled. Valid values:
                 * RESTRICTED - to apply access control
                 * NOT_RESTRICTED - to remove access control
                 * NOT_SET - to unset a previously set value.
        :param str restrict_create_platform_apikey: (optional) Defines whether or
               not creating platform API keys is access controlled. Valid values:
                 * RESTRICTED - to apply access control
                 * NOT_RESTRICTED - to remove access control
                 * NOT_SET - to 'unset' a previous set value.
        :param str allowed_ip_addresses: (optional) Defines the IP addresses and
               subnets from which IAM tokens can be created for the account.
        :param str mfa: (optional) Defines the MFA trait for the account. Valid
               values:
                 * NONE - No MFA trait set
                 * TOTP - For all non-federated IBMId users
                 * TOTP4ALL - For all users
                 * LEVEL1 - Email-based MFA for all users
                 * LEVEL2 - TOTP-based MFA for all users
                 * LEVEL3 - U2F MFA for all users.
        :param str session_expiration_in_seconds: (optional) Defines the session
               expiration in seconds for the account. Valid values:
                 * Any whole number between between '900' and '86400'
                 * NOT_SET - To unset account setting and use service default.
        :param str session_invalidation_in_seconds: (optional) Defines the period
               of time in seconds in which a session will be invalidated due  to
               inactivity. Valid values:
                 * Any whole number between '900' and '7200'
                 * NOT_SET - To unset account setting and use service default.
        :param str max_sessions_per_identity: (optional) Defines the max allowed
               sessions per identity required by the account. Value values:
                 * Any whole number greater than 0
                 * NOT_SET - To unset account setting and use service default.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountSettingsResponse` object
        """

        if if_match is None:
            raise ValueError('if_match must be provided')
        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_account_settings')
        headers.update(sdk_headers)

        data = {
            'restrict_create_service_id': restrict_create_service_id,
            'restrict_create_platform_apikey': restrict_create_platform_apikey,
            'allowed_ip_addresses': allowed_ip_addresses,
            'mfa': mfa,
            'session_expiration_in_seconds': session_expiration_in_seconds,
            'session_invalidation_in_seconds': session_invalidation_in_seconds,
            'max_sessions_per_identity': max_sessions_per_identity
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/accounts/{account_id}/settings/identity'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # activityOperations
    #########################


    def create_report(self,
        account_id: str,
        *,
        type: str = None,
        duration: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Trigger activity report across on account scope.

        Trigger activity report across on account scope for a given accountid.

        :param str account_id: ID of the account.
        :param str type: (optional) Optional report type, supported value is
               'inactive' - List all identities that have not authenticated within the
               time indicated by duration.
        :param str duration: (optional) Optional duration of the report, supported
               unit of duration is hours.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportReference` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_report')
        headers.update(sdk_headers)

        params = {
            'type': type,
            'duration': duration
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/activity/accounts/{account_id}/report'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_report(self,
        account_id: str,
        reference: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get activity report across on account scope.

        Get activity report across on account scope for a given accountid.

        :param str account_id: ID of the account.
        :param str reference: Reference for the report to be generated, You can use
               'latest' to get the latest report for the given account.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Report` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if reference is None:
            raise ValueError('reference must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_report')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'reference']
        path_param_values = self.encode_path_vars(account_id, reference)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/activity/accounts/{account_id}/report/{reference}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


class ListApiKeysEnums:
    """
    Enums for list_api_keys parameters.
    """

    class Scope(str, Enum):
        """
        Optional parameter to define the scope of the queried API keys. Can be 'entity'
        (default) or 'account'.
        """
        ENTITY = 'entity'
        ACCOUNT = 'account'
    class Type(str, Enum):
        """
        Optional parameter to filter the type of the queried API keys. Can be 'user' or
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


class ListProfilesEnums:
    """
    Enums for list_profiles parameters.
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


class AccountSettingsResponse():
    """
    Response body format for Account Settings REST requests.

    :attr ResponseContext context: (optional) Context with key properties for
          problem determination.
    :attr str account_id: Unique ID of the account.
    :attr str restrict_create_service_id: Defines whether or not creating a Service
          Id is access controlled. Valid values:
            * RESTRICTED - to apply access control
            * NOT_RESTRICTED - to remove access control
            * NOT_SET - to 'unset' a previous set value.
    :attr str restrict_create_platform_apikey: Defines whether or not creating
          platform API keys is access controlled. Valid values:
            * RESTRICTED - to apply access control
            * NOT_RESTRICTED - to remove access control
            * NOT_SET - to 'unset' a previous set value.
    :attr str allowed_ip_addresses: Defines the IP addresses and subnets from which
          IAM tokens can be created for the account.
    :attr str entity_tag: Version of the account settings.
    :attr str mfa: Defines the MFA trait for the account. Valid values:
            * NONE - No MFA trait set
            * TOTP - For all non-federated IBMId users
            * TOTP4ALL - For all users
            * LEVEL1 - Email-based MFA for all users
            * LEVEL2 - TOTP-based MFA for all users
            * LEVEL3 - U2F MFA for all users.
    :attr List[EnityHistoryRecord] history: (optional) History of the Account
          Settings.
    :attr str session_expiration_in_seconds: Defines the session expiration in
          seconds for the account. Valid values:
            * Any whole number between between '900' and '86400'
            * NOT_SET - To unset account setting and use service default.
    :attr str session_invalidation_in_seconds: Defines the period of time in seconds
          in which a session will be invalidated due  to inactivity. Valid values:
            * Any whole number between '900' and '7200'
            * NOT_SET - To unset account setting and use service default.
    :attr str max_sessions_per_identity: Defines the max allowed sessions per
          identity required by the account. Valid values:
            * Any whole number greater than 0
            * NOT_SET - To unset account setting and use service default.
    """

    def __init__(self,
                 account_id: str,
                 restrict_create_service_id: str,
                 restrict_create_platform_apikey: str,
                 allowed_ip_addresses: str,
                 entity_tag: str,
                 mfa: str,
                 session_expiration_in_seconds: str,
                 session_invalidation_in_seconds: str,
                 max_sessions_per_identity: str,
                 *,
                 context: 'ResponseContext' = None,
                 history: List['EnityHistoryRecord'] = None) -> None:
        """
        Initialize a AccountSettingsResponse object.

        :param str account_id: Unique ID of the account.
        :param str restrict_create_service_id: Defines whether or not creating a
               Service Id is access controlled. Valid values:
                 * RESTRICTED - to apply access control
                 * NOT_RESTRICTED - to remove access control
                 * NOT_SET - to 'unset' a previous set value.
        :param str restrict_create_platform_apikey: Defines whether or not creating
               platform API keys is access controlled. Valid values:
                 * RESTRICTED - to apply access control
                 * NOT_RESTRICTED - to remove access control
                 * NOT_SET - to 'unset' a previous set value.
        :param str allowed_ip_addresses: Defines the IP addresses and subnets from
               which IAM tokens can be created for the account.
        :param str entity_tag: Version of the account settings.
        :param str mfa: Defines the MFA trait for the account. Valid values:
                 * NONE - No MFA trait set
                 * TOTP - For all non-federated IBMId users
                 * TOTP4ALL - For all users
                 * LEVEL1 - Email-based MFA for all users
                 * LEVEL2 - TOTP-based MFA for all users
                 * LEVEL3 - U2F MFA for all users.
        :param str session_expiration_in_seconds: Defines the session expiration in
               seconds for the account. Valid values:
                 * Any whole number between between '900' and '86400'
                 * NOT_SET - To unset account setting and use service default.
        :param str session_invalidation_in_seconds: Defines the period of time in
               seconds in which a session will be invalidated due  to inactivity. Valid
               values:
                 * Any whole number between '900' and '7200'
                 * NOT_SET - To unset account setting and use service default.
        :param str max_sessions_per_identity: Defines the max allowed sessions per
               identity required by the account. Valid values:
                 * Any whole number greater than 0
                 * NOT_SET - To unset account setting and use service default.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param List[EnityHistoryRecord] history: (optional) History of the Account
               Settings.
        """
        self.context = context
        self.account_id = account_id
        self.restrict_create_service_id = restrict_create_service_id
        self.restrict_create_platform_apikey = restrict_create_platform_apikey
        self.allowed_ip_addresses = allowed_ip_addresses
        self.entity_tag = entity_tag
        self.mfa = mfa
        self.history = history
        self.session_expiration_in_seconds = session_expiration_in_seconds
        self.session_invalidation_in_seconds = session_invalidation_in_seconds
        self.max_sessions_per_identity = max_sessions_per_identity

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountSettingsResponse':
        """Initialize a AccountSettingsResponse object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ResponseContext.from_dict(_dict.get('context'))
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in AccountSettingsResponse JSON')
        if 'restrict_create_service_id' in _dict:
            args['restrict_create_service_id'] = _dict.get('restrict_create_service_id')
        else:
            raise ValueError('Required property \'restrict_create_service_id\' not present in AccountSettingsResponse JSON')
        if 'restrict_create_platform_apikey' in _dict:
            args['restrict_create_platform_apikey'] = _dict.get('restrict_create_platform_apikey')
        else:
            raise ValueError('Required property \'restrict_create_platform_apikey\' not present in AccountSettingsResponse JSON')
        if 'allowed_ip_addresses' in _dict:
            args['allowed_ip_addresses'] = _dict.get('allowed_ip_addresses')
        else:
            raise ValueError('Required property \'allowed_ip_addresses\' not present in AccountSettingsResponse JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        else:
            raise ValueError('Required property \'entity_tag\' not present in AccountSettingsResponse JSON')
        if 'mfa' in _dict:
            args['mfa'] = _dict.get('mfa')
        else:
            raise ValueError('Required property \'mfa\' not present in AccountSettingsResponse JSON')
        if 'history' in _dict:
            args['history'] = [EnityHistoryRecord.from_dict(x) for x in _dict.get('history')]
        if 'session_expiration_in_seconds' in _dict:
            args['session_expiration_in_seconds'] = _dict.get('session_expiration_in_seconds')
        else:
            raise ValueError('Required property \'session_expiration_in_seconds\' not present in AccountSettingsResponse JSON')
        if 'session_invalidation_in_seconds' in _dict:
            args['session_invalidation_in_seconds'] = _dict.get('session_invalidation_in_seconds')
        else:
            raise ValueError('Required property \'session_invalidation_in_seconds\' not present in AccountSettingsResponse JSON')
        if 'max_sessions_per_identity' in _dict:
            args['max_sessions_per_identity'] = _dict.get('max_sessions_per_identity')
        else:
            raise ValueError('Required property \'max_sessions_per_identity\' not present in AccountSettingsResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountSettingsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context.to_dict()
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'restrict_create_service_id') and self.restrict_create_service_id is not None:
            _dict['restrict_create_service_id'] = self.restrict_create_service_id
        if hasattr(self, 'restrict_create_platform_apikey') and self.restrict_create_platform_apikey is not None:
            _dict['restrict_create_platform_apikey'] = self.restrict_create_platform_apikey
        if hasattr(self, 'allowed_ip_addresses') and self.allowed_ip_addresses is not None:
            _dict['allowed_ip_addresses'] = self.allowed_ip_addresses
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'mfa') and self.mfa is not None:
            _dict['mfa'] = self.mfa
        if hasattr(self, 'history') and self.history is not None:
            _dict['history'] = [x.to_dict() for x in self.history]
        if hasattr(self, 'session_expiration_in_seconds') and self.session_expiration_in_seconds is not None:
            _dict['session_expiration_in_seconds'] = self.session_expiration_in_seconds
        if hasattr(self, 'session_invalidation_in_seconds') and self.session_invalidation_in_seconds is not None:
            _dict['session_invalidation_in_seconds'] = self.session_invalidation_in_seconds
        if hasattr(self, 'max_sessions_per_identity') and self.max_sessions_per_identity is not None:
            _dict['max_sessions_per_identity'] = self.max_sessions_per_identity
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountSettingsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountSettingsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountSettingsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class RestrictCreateServiceIdEnum(str, Enum):
        """
        Defines whether or not creating a Service Id is access controlled. Valid values:
          * RESTRICTED - to apply access control
          * NOT_RESTRICTED - to remove access control
          * NOT_SET - to 'unset' a previous set value.
        """
        RESTRICTED = 'RESTRICTED'
        NOT_RESTRICTED = 'NOT_RESTRICTED'
        NOT_SET = 'NOT_SET'


    class RestrictCreatePlatformApikeyEnum(str, Enum):
        """
        Defines whether or not creating platform API keys is access controlled. Valid
        values:
          * RESTRICTED - to apply access control
          * NOT_RESTRICTED - to remove access control
          * NOT_SET - to 'unset' a previous set value.
        """
        RESTRICTED = 'RESTRICTED'
        NOT_RESTRICTED = 'NOT_RESTRICTED'
        NOT_SET = 'NOT_SET'


    class MfaEnum(str, Enum):
        """
        Defines the MFA trait for the account. Valid values:
          * NONE - No MFA trait set
          * TOTP - For all non-federated IBMId users
          * TOTP4ALL - For all users
          * LEVEL1 - Email-based MFA for all users
          * LEVEL2 - TOTP-based MFA for all users
          * LEVEL3 - U2F MFA for all users.
        """
        NONE = 'NONE'
        TOTP = 'TOTP'
        TOTP4ALL = 'TOTP4ALL'
        LEVEL1 = 'LEVEL1'
        LEVEL2 = 'LEVEL2'
        LEVEL3 = 'LEVEL3'


class Activity():
    """
    Activity.

    :attr str last_authn: (optional) Time when the entity was last authenticated.
    :attr int authn_count: Authentication count, number of times the entity was
          authenticated.
    """

    def __init__(self,
                 authn_count: int,
                 *,
                 last_authn: str = None) -> None:
        """
        Initialize a Activity object.

        :param int authn_count: Authentication count, number of times the entity
               was authenticated.
        :param str last_authn: (optional) Time when the entity was last
               authenticated.
        """
        self.last_authn = last_authn
        self.authn_count = authn_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Activity':
        """Initialize a Activity object from a json dictionary."""
        args = {}
        if 'last_authn' in _dict:
            args['last_authn'] = _dict.get('last_authn')
        if 'authn_count' in _dict:
            args['authn_count'] = _dict.get('authn_count')
        else:
            raise ValueError('Required property \'authn_count\' not present in Activity JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Activity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'last_authn') and self.last_authn is not None:
            _dict['last_authn'] = self.last_authn
        if hasattr(self, 'authn_count') and self.authn_count is not None:
            _dict['authn_count'] = self.authn_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Activity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Activity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Activity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

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
    :attr Activity activity: (optional)
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
                 history: List['EnityHistoryRecord'] = None,
                 activity: 'Activity' = None) -> None:
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
        :param Activity activity: (optional)
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
        self.activity = activity

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
        if 'activity' in _dict:
            args['activity'] = Activity.from_dict(_dict.get('activity'))
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
        if hasattr(self, 'activity') and self.activity is not None:
            _dict['activity'] = self.activity.to_dict()
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

class ApikeyActivity():
    """
    Apikeys activity details.

    :attr str id: Unique id of the apikey.
    :attr str name: (optional) Name provided during creation of the apikey.
    :attr str type: Type of the apikey. Supported values are `serviceid` and `user`.
    :attr ApikeyActivityServiceid serviceid: (optional) serviceid details will be
          present if type is `serviceid`.
    :attr ApikeyActivityUser user: (optional) user details will be present if type
          is `user`.
    :attr str last_authn: (optional) Time when the apikey was last authenticated.
    """

    def __init__(self,
                 id: str,
                 type: str,
                 *,
                 name: str = None,
                 serviceid: 'ApikeyActivityServiceid' = None,
                 user: 'ApikeyActivityUser' = None,
                 last_authn: str = None) -> None:
        """
        Initialize a ApikeyActivity object.

        :param str id: Unique id of the apikey.
        :param str type: Type of the apikey. Supported values are `serviceid` and
               `user`.
        :param str name: (optional) Name provided during creation of the apikey.
        :param ApikeyActivityServiceid serviceid: (optional) serviceid details will
               be present if type is `serviceid`.
        :param ApikeyActivityUser user: (optional) user details will be present if
               type is `user`.
        :param str last_authn: (optional) Time when the apikey was last
               authenticated.
        """
        self.id = id
        self.name = name
        self.type = type
        self.serviceid = serviceid
        self.user = user
        self.last_authn = last_authn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApikeyActivity':
        """Initialize a ApikeyActivity object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ApikeyActivity JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in ApikeyActivity JSON')
        if 'serviceid' in _dict:
            args['serviceid'] = ApikeyActivityServiceid.from_dict(_dict.get('serviceid'))
        if 'user' in _dict:
            args['user'] = ApikeyActivityUser.from_dict(_dict.get('user'))
        if 'last_authn' in _dict:
            args['last_authn'] = _dict.get('last_authn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApikeyActivity object from a json dictionary."""
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
        if hasattr(self, 'serviceid') and self.serviceid is not None:
            _dict['serviceid'] = self.serviceid.to_dict()
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user.to_dict()
        if hasattr(self, 'last_authn') and self.last_authn is not None:
            _dict['last_authn'] = self.last_authn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApikeyActivity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApikeyActivity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApikeyActivity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApikeyActivityServiceid():
    """
    serviceid details will be present if type is `serviceid`.

    :attr str id: (optional) Unique identifier of this Service Id.
    :attr str name: (optional) Name provided during creation of the serviceid.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None) -> None:
        """
        Initialize a ApikeyActivityServiceid object.

        :param str id: (optional) Unique identifier of this Service Id.
        :param str name: (optional) Name provided during creation of the serviceid.
        """
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApikeyActivityServiceid':
        """Initialize a ApikeyActivityServiceid object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApikeyActivityServiceid object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApikeyActivityServiceid object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApikeyActivityServiceid') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApikeyActivityServiceid') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApikeyActivityUser():
    """
    user details will be present if type is `user`.

    :attr str iam_id: (optional) IAMid of the user.
    :attr str name: (optional) Name of the user.
    :attr str username: (optional) Username of the user.
    :attr str email: (optional) Email of the user.
    """

    def __init__(self,
                 *,
                 iam_id: str = None,
                 name: str = None,
                 username: str = None,
                 email: str = None) -> None:
        """
        Initialize a ApikeyActivityUser object.

        :param str iam_id: (optional) IAMid of the user.
        :param str name: (optional) Name of the user.
        :param str username: (optional) Username of the user.
        :param str email: (optional) Email of the user.
        """
        self.iam_id = iam_id
        self.name = name
        self.username = username
        self.email = email

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApikeyActivityUser':
        """Initialize a ApikeyActivityUser object from a json dictionary."""
        args = {}
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'email' in _dict:
            args['email'] = _dict.get('email')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApikeyActivityUser object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = self.email
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApikeyActivityUser object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApikeyActivityUser') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApikeyActivityUser') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreateProfileLinkRequestLink():
    """
    Link details.

    :attr str crn: The CRN of the compute resource.
    :attr str namespace: The compute resource namespace, only required if cr_type is
          IKS_SA or ROKS_SA.
    :attr str name: (optional) Name of the compute resource, only required if
          cr_type is IKS_SA or ROKS_SA.
    """

    def __init__(self,
                 crn: str,
                 namespace: str,
                 *,
                 name: str = None) -> None:
        """
        Initialize a CreateProfileLinkRequestLink object.

        :param str crn: The CRN of the compute resource.
        :param str namespace: The compute resource namespace, only required if
               cr_type is IKS_SA or ROKS_SA.
        :param str name: (optional) Name of the compute resource, only required if
               cr_type is IKS_SA or ROKS_SA.
        """
        self.crn = crn
        self.namespace = namespace
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateProfileLinkRequestLink':
        """Initialize a CreateProfileLinkRequestLink object from a json dictionary."""
        args = {}
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in CreateProfileLinkRequestLink JSON')
        if 'namespace' in _dict:
            args['namespace'] = _dict.get('namespace')
        else:
            raise ValueError('Required property \'namespace\' not present in CreateProfileLinkRequestLink JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateProfileLinkRequestLink object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'namespace') and self.namespace is not None:
            _dict['namespace'] = self.namespace
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateProfileLinkRequestLink object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateProfileLinkRequestLink') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateProfileLinkRequestLink') -> bool:
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

class EntityActivity():
    """
    EntityActivity.

    :attr str id: Unique id of the entity.
    :attr str name: (optional) Name provided during creation of the entity.
    :attr str last_authn: (optional) Time when the entity was last authenticated.
    """

    def __init__(self,
                 id: str,
                 *,
                 name: str = None,
                 last_authn: str = None) -> None:
        """
        Initialize a EntityActivity object.

        :param str id: Unique id of the entity.
        :param str name: (optional) Name provided during creation of the entity.
        :param str last_authn: (optional) Time when the entity was last
               authenticated.
        """
        self.id = id
        self.name = name
        self.last_authn = last_authn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntityActivity':
        """Initialize a EntityActivity object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in EntityActivity JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'last_authn' in _dict:
            args['last_authn'] = _dict.get('last_authn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityActivity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'last_authn') and self.last_authn is not None:
            _dict['last_authn'] = self.last_authn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EntityActivity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EntityActivity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntityActivity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ProfileClaimRule():
    """
    ProfileClaimRule.

    :attr str id: the unique identifier of the claim rule.
    :attr str entity_tag: version of the claim rule.
    :attr datetime created_at: If set contains a date time string of the creation
          date in ISO format.
    :attr datetime modified_at: (optional) If set contains a date time string of the
          last modification date in ISO format.
    :attr str name: (optional) The optional claim rule name.
    :attr str type: Type of the Calim rule, either 'Profile-SAML' or 'Profile-CR'.
    :attr str realm_name: (optional) The realm name of the Idp this claim rule
          applies to.
    :attr int expiration: Session expiration in seconds.
    :attr str cr_type: (optional) The compute resource type. Not required if type is
          Profile-SAML. Valid values are VSI, IKS_SA, ROKS_SA.
    :attr List[ProfileClaimRuleConditions] conditions: Conditions of this claim
          rule.
    """

    def __init__(self,
                 id: str,
                 entity_tag: str,
                 created_at: datetime,
                 type: str,
                 expiration: int,
                 conditions: List['ProfileClaimRuleConditions'],
                 *,
                 modified_at: datetime = None,
                 name: str = None,
                 realm_name: str = None,
                 cr_type: str = None) -> None:
        """
        Initialize a ProfileClaimRule object.

        :param str id: the unique identifier of the claim rule.
        :param str entity_tag: version of the claim rule.
        :param datetime created_at: If set contains a date time string of the
               creation date in ISO format.
        :param str type: Type of the Calim rule, either 'Profile-SAML' or
               'Profile-CR'.
        :param int expiration: Session expiration in seconds.
        :param List[ProfileClaimRuleConditions] conditions: Conditions of this
               claim rule.
        :param datetime modified_at: (optional) If set contains a date time string
               of the last modification date in ISO format.
        :param str name: (optional) The optional claim rule name.
        :param str realm_name: (optional) The realm name of the Idp this claim rule
               applies to.
        :param str cr_type: (optional) The compute resource type. Not required if
               type is Profile-SAML. Valid values are VSI, IKS_SA, ROKS_SA.
        """
        self.id = id
        self.entity_tag = entity_tag
        self.created_at = created_at
        self.modified_at = modified_at
        self.name = name
        self.type = type
        self.realm_name = realm_name
        self.expiration = expiration
        self.cr_type = cr_type
        self.conditions = conditions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileClaimRule':
        """Initialize a ProfileClaimRule object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProfileClaimRule JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        else:
            raise ValueError('Required property \'entity_tag\' not present in ProfileClaimRule JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProfileClaimRule JSON')
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in ProfileClaimRule JSON')
        if 'realm_name' in _dict:
            args['realm_name'] = _dict.get('realm_name')
        if 'expiration' in _dict:
            args['expiration'] = _dict.get('expiration')
        else:
            raise ValueError('Required property \'expiration\' not present in ProfileClaimRule JSON')
        if 'cr_type' in _dict:
            args['cr_type'] = _dict.get('cr_type')
        if 'conditions' in _dict:
            args['conditions'] = [ProfileClaimRuleConditions.from_dict(x) for x in _dict.get('conditions')]
        else:
            raise ValueError('Required property \'conditions\' not present in ProfileClaimRule JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileClaimRule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'realm_name') and self.realm_name is not None:
            _dict['realm_name'] = self.realm_name
        if hasattr(self, 'expiration') and self.expiration is not None:
            _dict['expiration'] = self.expiration
        if hasattr(self, 'cr_type') and self.cr_type is not None:
            _dict['cr_type'] = self.cr_type
        if hasattr(self, 'conditions') and self.conditions is not None:
            _dict['conditions'] = [x.to_dict() for x in self.conditions]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileClaimRule object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileClaimRule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileClaimRule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ProfileClaimRuleConditions():
    """
    ProfileClaimRuleConditions.

    :attr str claim: The claim to evaluate against.
    :attr str operator: The operation to perform on the claim. valid values are
          EQUALS, NOT_EQUALS, EQUALS_IGNORE_CASE, NOT_EQUALS_IGNORE_CASE, CONTAINS, IN.
    :attr str value: The stringified JSON value that the claim is compared to using
          the operator.
    """

    def __init__(self,
                 claim: str,
                 operator: str,
                 value: str) -> None:
        """
        Initialize a ProfileClaimRuleConditions object.

        :param str claim: The claim to evaluate against.
        :param str operator: The operation to perform on the claim. valid values
               are EQUALS, NOT_EQUALS, EQUALS_IGNORE_CASE, NOT_EQUALS_IGNORE_CASE,
               CONTAINS, IN.
        :param str value: The stringified JSON value that the claim is compared to
               using the operator.
        """
        self.claim = claim
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileClaimRuleConditions':
        """Initialize a ProfileClaimRuleConditions object from a json dictionary."""
        args = {}
        if 'claim' in _dict:
            args['claim'] = _dict.get('claim')
        else:
            raise ValueError('Required property \'claim\' not present in ProfileClaimRuleConditions JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in ProfileClaimRuleConditions JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ProfileClaimRuleConditions JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileClaimRuleConditions object from a json dictionary."""
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
        """Return a `str` version of this ProfileClaimRuleConditions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileClaimRuleConditions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileClaimRuleConditions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ProfileClaimRuleList():
    """
    ProfileClaimRuleList.

    :attr ResponseContext context: (optional) Context with key properties for
          problem determination.
    :attr List[ProfileClaimRule] rules: List of claim rules.
    """

    def __init__(self,
                 rules: List['ProfileClaimRule'],
                 *,
                 context: 'ResponseContext' = None) -> None:
        """
        Initialize a ProfileClaimRuleList object.

        :param List[ProfileClaimRule] rules: List of claim rules.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        """
        self.context = context
        self.rules = rules

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileClaimRuleList':
        """Initialize a ProfileClaimRuleList object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ResponseContext.from_dict(_dict.get('context'))
        if 'rules' in _dict:
            args['rules'] = [ProfileClaimRule.from_dict(x) for x in _dict.get('rules')]
        else:
            raise ValueError('Required property \'rules\' not present in ProfileClaimRuleList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileClaimRuleList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context.to_dict()
        if hasattr(self, 'rules') and self.rules is not None:
            _dict['rules'] = [x.to_dict() for x in self.rules]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileClaimRuleList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileClaimRuleList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileClaimRuleList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ProfileLink():
    """
    Link details.

    :attr str id: the unique identifier of the claim rule.
    :attr str entity_tag: version of the claim rule.
    :attr datetime created_at: If set contains a date time string of the creation
          date in ISO format.
    :attr datetime modified_at: If set contains a date time string of the last
          modification date in ISO format.
    :attr str name: (optional) Optional name of the Link.
    :attr str cr_type: The compute resource type. Valid values are VSI, IKS_SA,
          ROKS_SA.
    :attr ProfileLinkLink link:
    """

    def __init__(self,
                 id: str,
                 entity_tag: str,
                 created_at: datetime,
                 modified_at: datetime,
                 cr_type: str,
                 link: 'ProfileLinkLink',
                 *,
                 name: str = None) -> None:
        """
        Initialize a ProfileLink object.

        :param str id: the unique identifier of the claim rule.
        :param str entity_tag: version of the claim rule.
        :param datetime created_at: If set contains a date time string of the
               creation date in ISO format.
        :param datetime modified_at: If set contains a date time string of the last
               modification date in ISO format.
        :param str cr_type: The compute resource type. Valid values are VSI,
               IKS_SA, ROKS_SA.
        :param ProfileLinkLink link:
        :param str name: (optional) Optional name of the Link.
        """
        self.id = id
        self.entity_tag = entity_tag
        self.created_at = created_at
        self.modified_at = modified_at
        self.name = name
        self.cr_type = cr_type
        self.link = link

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileLink':
        """Initialize a ProfileLink object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProfileLink JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        else:
            raise ValueError('Required property \'entity_tag\' not present in ProfileLink JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProfileLink JSON')
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        else:
            raise ValueError('Required property \'modified_at\' not present in ProfileLink JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'cr_type' in _dict:
            args['cr_type'] = _dict.get('cr_type')
        else:
            raise ValueError('Required property \'cr_type\' not present in ProfileLink JSON')
        if 'link' in _dict:
            args['link'] = ProfileLinkLink.from_dict(_dict.get('link'))
        else:
            raise ValueError('Required property \'link\' not present in ProfileLink JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileLink object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'cr_type') and self.cr_type is not None:
            _dict['cr_type'] = self.cr_type
        if hasattr(self, 'link') and self.link is not None:
            _dict['link'] = self.link.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileLink object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileLink') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileLink') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ProfileLinkLink():
    """
    ProfileLinkLink.

    :attr str crn: (optional) The CRN of the compute resource.
    :attr str namespace: (optional) The compute resource namespace, only required if
          cr_type is IKS_SA or ROKS_SA.
    :attr str name: (optional) Name of the compute resource, only required if
          cr_type is IKS_SA or ROKS_SA.
    """

    def __init__(self,
                 *,
                 crn: str = None,
                 namespace: str = None,
                 name: str = None) -> None:
        """
        Initialize a ProfileLinkLink object.

        :param str crn: (optional) The CRN of the compute resource.
        :param str namespace: (optional) The compute resource namespace, only
               required if cr_type is IKS_SA or ROKS_SA.
        :param str name: (optional) Name of the compute resource, only required if
               cr_type is IKS_SA or ROKS_SA.
        """
        self.crn = crn
        self.namespace = namespace
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileLinkLink':
        """Initialize a ProfileLinkLink object from a json dictionary."""
        args = {}
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'namespace' in _dict:
            args['namespace'] = _dict.get('namespace')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileLinkLink object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'namespace') and self.namespace is not None:
            _dict['namespace'] = self.namespace
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileLinkLink object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileLinkLink') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileLinkLink') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ProfileLinkList():
    """
    ProfileLinkList.

    :attr List[ProfileLink] links: List of links to a trusted profile.
    """

    def __init__(self,
                 links: List['ProfileLink']) -> None:
        """
        Initialize a ProfileLinkList object.

        :param List[ProfileLink] links: List of links to a trusted profile.
        """
        self.links = links

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileLinkList':
        """Initialize a ProfileLinkList object from a json dictionary."""
        args = {}
        if 'links' in _dict:
            args['links'] = [ProfileLink.from_dict(x) for x in _dict.get('links')]
        else:
            raise ValueError('Required property \'links\' not present in ProfileLinkList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileLinkList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'links') and self.links is not None:
            _dict['links'] = [x.to_dict() for x in self.links]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileLinkList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileLinkList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileLinkList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Report():
    """
    Report.

    :attr str created_by: IAMid of the user who triggered the report.
    :attr str reference: Unique reference used to generate the report.
    :attr str report_duration: Duration in hours for which the report is generated.
    :attr str report_start_time: Start time of the report.
    :attr str report_end_time: End time of the report.
    :attr List[UserActivity] users: (optional) List of users.
    :attr List[ApikeyActivity] apikeys: (optional) List of apikeys.
    :attr List[EntityActivity] serviceids: (optional) List of serviceids.
    :attr List[EntityActivity] profiles: (optional) List of profiles.
    """

    def __init__(self,
                 created_by: str,
                 reference: str,
                 report_duration: str,
                 report_start_time: str,
                 report_end_time: str,
                 *,
                 users: List['UserActivity'] = None,
                 apikeys: List['ApikeyActivity'] = None,
                 serviceids: List['EntityActivity'] = None,
                 profiles: List['EntityActivity'] = None) -> None:
        """
        Initialize a Report object.

        :param str created_by: IAMid of the user who triggered the report.
        :param str reference: Unique reference used to generate the report.
        :param str report_duration: Duration in hours for which the report is
               generated.
        :param str report_start_time: Start time of the report.
        :param str report_end_time: End time of the report.
        :param List[UserActivity] users: (optional) List of users.
        :param List[ApikeyActivity] apikeys: (optional) List of apikeys.
        :param List[EntityActivity] serviceids: (optional) List of serviceids.
        :param List[EntityActivity] profiles: (optional) List of profiles.
        """
        self.created_by = created_by
        self.reference = reference
        self.report_duration = report_duration
        self.report_start_time = report_start_time
        self.report_end_time = report_end_time
        self.users = users
        self.apikeys = apikeys
        self.serviceids = serviceids
        self.profiles = profiles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Report':
        """Initialize a Report object from a json dictionary."""
        args = {}
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        else:
            raise ValueError('Required property \'created_by\' not present in Report JSON')
        if 'reference' in _dict:
            args['reference'] = _dict.get('reference')
        else:
            raise ValueError('Required property \'reference\' not present in Report JSON')
        if 'report_duration' in _dict:
            args['report_duration'] = _dict.get('report_duration')
        else:
            raise ValueError('Required property \'report_duration\' not present in Report JSON')
        if 'report_start_time' in _dict:
            args['report_start_time'] = _dict.get('report_start_time')
        else:
            raise ValueError('Required property \'report_start_time\' not present in Report JSON')
        if 'report_end_time' in _dict:
            args['report_end_time'] = _dict.get('report_end_time')
        else:
            raise ValueError('Required property \'report_end_time\' not present in Report JSON')
        if 'users' in _dict:
            args['users'] = [UserActivity.from_dict(x) for x in _dict.get('users')]
        if 'apikeys' in _dict:
            args['apikeys'] = [ApikeyActivity.from_dict(x) for x in _dict.get('apikeys')]
        if 'serviceids' in _dict:
            args['serviceids'] = [EntityActivity.from_dict(x) for x in _dict.get('serviceids')]
        if 'profiles' in _dict:
            args['profiles'] = [EntityActivity.from_dict(x) for x in _dict.get('profiles')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Report object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'reference') and self.reference is not None:
            _dict['reference'] = self.reference
        if hasattr(self, 'report_duration') and self.report_duration is not None:
            _dict['report_duration'] = self.report_duration
        if hasattr(self, 'report_start_time') and self.report_start_time is not None:
            _dict['report_start_time'] = self.report_start_time
        if hasattr(self, 'report_end_time') and self.report_end_time is not None:
            _dict['report_end_time'] = self.report_end_time
        if hasattr(self, 'users') and self.users is not None:
            _dict['users'] = [x.to_dict() for x in self.users]
        if hasattr(self, 'apikeys') and self.apikeys is not None:
            _dict['apikeys'] = [x.to_dict() for x in self.apikeys]
        if hasattr(self, 'serviceids') and self.serviceids is not None:
            _dict['serviceids'] = [x.to_dict() for x in self.serviceids]
        if hasattr(self, 'profiles') and self.profiles is not None:
            _dict['profiles'] = [x.to_dict() for x in self.profiles]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Report object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Report') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Report') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ReportReference():
    """
    ReportReference.

    :attr str reference: Reference for the report to be generated.
    """

    def __init__(self,
                 reference: str) -> None:
        """
        Initialize a ReportReference object.

        :param str reference: Reference for the report to be generated.
        """
        self.reference = reference

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportReference':
        """Initialize a ReportReference object from a json dictionary."""
        args = {}
        if 'reference' in _dict:
            args['reference'] = _dict.get('reference')
        else:
            raise ValueError('Required property \'reference\' not present in ReportReference JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'reference') and self.reference is not None:
            _dict['reference'] = self.reference
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReportReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportReference') -> bool:
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
    :attr str entity_tag: Version of the service ID details object. You need to
          specify this value when updating the service ID to avoid stale updates.
    :attr str crn: Cloud Resource Name of the item. Example Cloud Resource Name:
          'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::serviceid:1234-5678-9012'.
    :attr bool locked: The service ID cannot be changed if set to true.
    :attr datetime created_at: If set contains a date time string of the creation
          date in ISO format.
    :attr datetime modified_at: If set contains a date time string of the last
          modification date in ISO format.
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
    :attr ApiKey apikey: (optional) Response body format for API key V1 REST
          requests.
    :attr Activity activity: (optional)
    """

    def __init__(self,
                 id: str,
                 iam_id: str,
                 entity_tag: str,
                 crn: str,
                 locked: bool,
                 created_at: datetime,
                 modified_at: datetime,
                 account_id: str,
                 name: str,
                 *,
                 context: 'ResponseContext' = None,
                 description: str = None,
                 unique_instance_crns: List[str] = None,
                 history: List['EnityHistoryRecord'] = None,
                 apikey: 'ApiKey' = None,
                 activity: 'Activity' = None) -> None:
        """
        Initialize a ServiceId object.

        :param str id: Unique identifier of this Service Id.
        :param str iam_id: Cloud wide identifier for identities of this service ID.
        :param str entity_tag: Version of the service ID details object. You need
               to specify this value when updating the service ID to avoid stale updates.
        :param str crn: Cloud Resource Name of the item. Example Cloud Resource
               Name:
               'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::serviceid:1234-5678-9012'.
        :param bool locked: The service ID cannot be changed if set to true.
        :param datetime created_at: If set contains a date time string of the
               creation date in ISO format.
        :param datetime modified_at: If set contains a date time string of the last
               modification date in ISO format.
        :param str account_id: ID of the account the service ID belongs to.
        :param str name: Name of the Service Id. The name is not checked for
               uniqueness. Therefore multiple names with the same value can exist. Access
               is done via the UUID of the Service Id.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param str description: (optional) The optional description of the Service
               Id. The 'description' property is only available if a description was
               provided during a create of a Service Id.
        :param List[str] unique_instance_crns: (optional) Optional list of CRNs
               (string array) which point to the services connected to the service ID.
        :param List[EnityHistoryRecord] history: (optional) History of the Service
               ID.
        :param ApiKey apikey: (optional) Response body format for API key V1 REST
               requests.
        :param Activity activity: (optional)
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
        self.activity = activity

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
        else:
            raise ValueError('Required property \'entity_tag\' not present in ServiceId JSON')
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
        else:
            raise ValueError('Required property \'created_at\' not present in ServiceId JSON')
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        else:
            raise ValueError('Required property \'modified_at\' not present in ServiceId JSON')
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
        if 'activity' in _dict:
            args['activity'] = Activity.from_dict(_dict.get('activity'))
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
        if hasattr(self, 'activity') and self.activity is not None:
            _dict['activity'] = self.activity.to_dict()
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

class TrustedProfile():
    """
    Response body format for trusted profile V1 REST requests.

    :attr ResponseContext context: (optional) Context with key properties for
          problem determination.
    :attr str id: the unique identifier of the trusted profile.
          Example:'Profile-94497d0d-2ac3-41bf-a993-a49d1b14627c'.
    :attr str entity_tag: Version of the trusted profile details object. You need to
          specify this value when updating the trusted profile to avoid stale updates.
    :attr str crn: Cloud Resource Name of the item. Example Cloud Resource Name:
          'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::profile:Profile-94497d0d-2ac3-41bf-a993-a49d1b14627c'.
    :attr str name: Name of the trusted profile. The name is checked for uniqueness.
          Therefore trusted profiles with the same names can not exist in the same
          account.
    :attr str description: (optional) The optional description of the trusted
          profile. The 'description' property is only available if a description was
          provided during a create of a trusted profile.
    :attr datetime created_at: (optional) If set contains a date time string of the
          creation date in ISO format.
    :attr datetime modified_at: (optional) If set contains a date time string of the
          last modification date in ISO format.
    :attr str iam_id: The iam_id of this trusted profile.
    :attr str account_id: ID of the account that this trusted profile belong to.
    :attr int ims_account_id: (optional) IMS acount ID of the trusted profile.
    :attr int ims_user_id: (optional) IMS user ID of the trusted profile.
    :attr List[EnityHistoryRecord] history: (optional) History of the trusted
          profile.
    :attr Activity activity: (optional)
    """

    def __init__(self,
                 id: str,
                 entity_tag: str,
                 crn: str,
                 name: str,
                 iam_id: str,
                 account_id: str,
                 *,
                 context: 'ResponseContext' = None,
                 description: str = None,
                 created_at: datetime = None,
                 modified_at: datetime = None,
                 ims_account_id: int = None,
                 ims_user_id: int = None,
                 history: List['EnityHistoryRecord'] = None,
                 activity: 'Activity' = None) -> None:
        """
        Initialize a TrustedProfile object.

        :param str id: the unique identifier of the trusted profile.
               Example:'Profile-94497d0d-2ac3-41bf-a993-a49d1b14627c'.
        :param str entity_tag: Version of the trusted profile details object. You
               need to specify this value when updating the trusted profile to avoid stale
               updates.
        :param str crn: Cloud Resource Name of the item. Example Cloud Resource
               Name:
               'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::profile:Profile-94497d0d-2ac3-41bf-a993-a49d1b14627c'.
        :param str name: Name of the trusted profile. The name is checked for
               uniqueness. Therefore trusted profiles with the same names can not exist in
               the same account.
        :param str iam_id: The iam_id of this trusted profile.
        :param str account_id: ID of the account that this trusted profile belong
               to.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param str description: (optional) The optional description of the trusted
               profile. The 'description' property is only available if a description was
               provided during a create of a trusted profile.
        :param datetime created_at: (optional) If set contains a date time string
               of the creation date in ISO format.
        :param datetime modified_at: (optional) If set contains a date time string
               of the last modification date in ISO format.
        :param int ims_account_id: (optional) IMS acount ID of the trusted profile.
        :param int ims_user_id: (optional) IMS user ID of the trusted profile.
        :param List[EnityHistoryRecord] history: (optional) History of the trusted
               profile.
        :param Activity activity: (optional)
        """
        self.context = context
        self.id = id
        self.entity_tag = entity_tag
        self.crn = crn
        self.name = name
        self.description = description
        self.created_at = created_at
        self.modified_at = modified_at
        self.iam_id = iam_id
        self.account_id = account_id
        self.ims_account_id = ims_account_id
        self.ims_user_id = ims_user_id
        self.history = history
        self.activity = activity

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrustedProfile':
        """Initialize a TrustedProfile object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ResponseContext.from_dict(_dict.get('context'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in TrustedProfile JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        else:
            raise ValueError('Required property \'entity_tag\' not present in TrustedProfile JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in TrustedProfile JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TrustedProfile JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in TrustedProfile JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in TrustedProfile JSON')
        if 'ims_account_id' in _dict:
            args['ims_account_id'] = _dict.get('ims_account_id')
        if 'ims_user_id' in _dict:
            args['ims_user_id'] = _dict.get('ims_user_id')
        if 'history' in _dict:
            args['history'] = [EnityHistoryRecord.from_dict(x) for x in _dict.get('history')]
        if 'activity' in _dict:
            args['activity'] = Activity.from_dict(_dict.get('activity'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrustedProfile object from a json dictionary."""
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
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'ims_account_id') and self.ims_account_id is not None:
            _dict['ims_account_id'] = self.ims_account_id
        if hasattr(self, 'ims_user_id') and self.ims_user_id is not None:
            _dict['ims_user_id'] = self.ims_user_id
        if hasattr(self, 'history') and self.history is not None:
            _dict['history'] = [x.to_dict() for x in self.history]
        if hasattr(self, 'activity') and self.activity is not None:
            _dict['activity'] = self.activity.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrustedProfile object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrustedProfile') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrustedProfile') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TrustedProfilesList():
    """
    Response body format for the List trusted profiles V1 REST request.

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
    :attr List[TrustedProfile] profiles: List of trusted profiles.
    """

    def __init__(self,
                 profiles: List['TrustedProfile'],
                 *,
                 context: 'ResponseContext' = None,
                 offset: int = None,
                 limit: int = None,
                 first: str = None,
                 previous: str = None,
                 next: str = None) -> None:
        """
        Initialize a TrustedProfilesList object.

        :param List[TrustedProfile] profiles: List of trusted profiles.
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
        self.profiles = profiles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrustedProfilesList':
        """Initialize a TrustedProfilesList object from a json dictionary."""
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
        if 'profiles' in _dict:
            args['profiles'] = [TrustedProfile.from_dict(x) for x in _dict.get('profiles')]
        else:
            raise ValueError('Required property \'profiles\' not present in TrustedProfilesList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrustedProfilesList object from a json dictionary."""
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
        if hasattr(self, 'profiles') and self.profiles is not None:
            _dict['profiles'] = [x.to_dict() for x in self.profiles]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrustedProfilesList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrustedProfilesList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrustedProfilesList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UserActivity():
    """
    UserActivity.

    :attr str iam_id: IAMid of the user.
    :attr str name: (optional) Name of the user.
    :attr str username: Username of the user.
    :attr str email: (optional) Email of the user.
    :attr str last_authn: (optional) Time when the user was last authenticated.
    """

    def __init__(self,
                 iam_id: str,
                 username: str,
                 *,
                 name: str = None,
                 email: str = None,
                 last_authn: str = None) -> None:
        """
        Initialize a UserActivity object.

        :param str iam_id: IAMid of the user.
        :param str username: Username of the user.
        :param str name: (optional) Name of the user.
        :param str email: (optional) Email of the user.
        :param str last_authn: (optional) Time when the user was last
               authenticated.
        """
        self.iam_id = iam_id
        self.name = name
        self.username = username
        self.email = email
        self.last_authn = last_authn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UserActivity':
        """Initialize a UserActivity object from a json dictionary."""
        args = {}
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in UserActivity JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        else:
            raise ValueError('Required property \'username\' not present in UserActivity JSON')
        if 'email' in _dict:
            args['email'] = _dict.get('email')
        if 'last_authn' in _dict:
            args['last_authn'] = _dict.get('last_authn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UserActivity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = self.email
        if hasattr(self, 'last_authn') and self.last_authn is not None:
            _dict['last_authn'] = self.last_authn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UserActivity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UserActivity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UserActivity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
