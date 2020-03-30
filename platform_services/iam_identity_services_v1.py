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
The IAM Identity Service API allows for the management of Identities (Service IDs,
ApiKeys).
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

class IamIdentityServicesV1(BaseService):
    """The iam_identity_services V1 service."""

    DEFAULT_SERVICE_URL = 'https://iam.test.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'iam_identity_services'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'IamIdentityServicesV1':
        """
        Return a new client for the iam_identity_services service using the
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
        Construct a new client for the iam_identity_services service.

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


    def list_api_keys(self, *, account_id: str = None, iam_id: str = None, pagesize: str = None, pagetoken: str = None, **kwargs) -> DetailedResponse:
        """
        Get API keys for a given a service or user IAM ID and account ID.

        Returns the list of API key details for a given service or user IAM ID and account
        ID. Users can manage user API keys for themself, or service ID API keys for
        service IDs that are bound to an entity they have access to.

        :param str account_id: (optional) Account ID of the API keys(s) to query.
               If a service IAM ID is specified in iam_id then account_id must match the
               account of the IAM ID. If a user IAM ID is specified in iam_id then then
               account_id must match the account of the Authorization token.
        :param str iam_id: (optional) IAM ID of the API key(s) to be queried. The
               IAM ID may be that of a user or a service. For a user IAM ID iam_id must
               match the Authorization token.
        :param str pagesize: (optional) Optional size of a single page. Default is
               20 items per page. Valid range is 1 to 100.
        :param str pagetoken: (optional) Optional Prev or Next page token returned
               from a previous query execution. Default is start with first page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListApiKeysResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_api_keys')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'iam_id': iam_id,
            'pagesize': pagesize,
            'pagetoken': pagetoken
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/apikeys'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_api_key(self, name: str, iam_id: str, *, description: str = None, account_id: str = None, apikey: str = None, entity_lock: str = None, **kwargs) -> DetailedResponse:
        """
        Create an ApiKey.

        Creates an API key for a UserID or service ID. Users can manage user API keys for
        themself, or service ID API keys for service IDs that are bound to an entity they
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
        :param str entity_lock: (optional) Indicates if the API key is locked for
               further write operations. False by default.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiKeyDetails` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if iam_id is None:
            raise ValueError('iam_id must be provided')
        headers = {
            'Entity-Lock': entity_lock
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_api_key')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'iam_id': iam_id,
            'description': description,
            'account_id': account_id,
            'apikey': apikey
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/apikeys'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_api_key_details(self, *, iam_api_key: str = None, **kwargs) -> DetailedResponse:
        """
        Get details of an API key by its value.

        Returns the details of an API key by its value. Users can manage user API keys for
        themself, or service ID API keys for service IDs that are bound to an entity they
        have access to.

        :param str iam_api_key: (optional) API key value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiKeyDetails` object
        """

        headers = {
            'IAM-ApiKey': iam_api_key
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_api_key_details')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/apikeys/details'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_api_key(self, id: str, **kwargs) -> DetailedResponse:
        """
        Get details of an API key.

        Returns the details of an API key. Users can manage user API keys for themself, or
        service ID API keys for service IDs that are bound to an entity they have access
        to.

        :param str id: Unique ID of the API key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiKeyDetails` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_api_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/apikeys/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_api_key(self, id: str, if_match: str, *, name: str = None, description: str = None, **kwargs) -> DetailedResponse:
        """
        Updates an ApiKey.

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
        :rtype: DetailedResponse with `dict` result representing a `ApiKeyDetails` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_api_key')
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

        url = '/v1/apikeys/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_api_key(self, id: str, **kwargs) -> DetailedResponse:
        """
        Deletes an ApiKey.

        Deletes an API key. Existing tokens will remain valid until expired. Refresh
        tokens will not work any more for this API key. Users can manage user API keys for
        themself, or service ID API keys for service IDs that are bound to an entity they
        have access to.

        :param str id: Unique ID of the API key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_api_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/apikeys/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def lock_api_key(self, id: str, **kwargs) -> DetailedResponse:
        """
        Lock the API key.

        Locks an API key by ID. Users can manage user API keys for themself, or service ID
        API keys for service IDs that are bound to an entity they have access to.

        :param str id: Unique ID of the API key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='lock_api_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/apikeys/{0}/lock'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def unlock_api_key(self, id: str, **kwargs) -> DetailedResponse:
        """
        Unlock the API key.

        Unlocks an API key by ID. Users can manage user API keys for themself, or service
        ID API keys for service IDs that are bound to an entity they have access to.

        :param str id: Unique ID of the API key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='unlock_api_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/apikeys/{0}/lock'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_service_ids(self, *, account_id: str = None, name: str = None, pagesize: str = None, pagetoken: str = None, sort: str = None, order: str = None, **kwargs) -> DetailedResponse:
        """
        List service IDs.

        Returns a list of service IDs. Users can manage user API keys for themself, or
        service ID API keys for service IDs that are bound to an entity they have access
        to.

        :param str account_id: (optional) Account ID of the service ID(s) to query.
               This parameter is required (unless using a pagetoken).
        :param str name: (optional) Name of the service ID(s) to query. Optional.20
               items per page.
        :param str pagesize: (optional) Optional size of a single page. Default is
               20 items per page. Valid range is 1 to 100.
        :param str pagetoken: (optional) Optional Prev or Next page token returned
               from a previous query execution. Default is start with first page.
        :param str sort: (optional) Optional sort property, valid values are name,
               description, createdAt and modifiedAt. If specified, the items are sorted
               by the value of this property.
        :param str order: (optional) Optional sort order, valid values are asc and
               desc. Default: asc.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceIdsList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_service_ids')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'name': name,
            'pagesize': pagesize,
            'pagetoken': pagetoken,
            'sort': sort,
            'order': order
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/serviceids'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_service_id(self, account_id: str, name: str, *, description: str = None, unique_instance_crns: List[str] = None, apikey: 'CreateApiKeyRequest' = None, entity_lock: str = None, **kwargs) -> DetailedResponse:
        """
        Create a service ID.

        Creates a service ID for an IBM Cloud account. Users can manage user API keys for
        themself, or service ID API keys for service IDs that are bound to an entity they
        have access to.

        :param str account_id: ID of the account the service ID belongs to.
        :param str name: Name of the service ID. The name is not checked for
               uniqueness. Therefore multiple names with the same value can exist. Access
               is done via the UUID of the Service Id.
        :param str description: (optional) The optional description of the Service
               Id. The 'description' property is only available if a description was
               provided during a create of a ServiceId.
        :param List[str] unique_instance_crns: (optional) Optional list of CRNs
               (string array) which point to the services connected to the service ID.
        :param CreateApiKeyRequest apikey: (optional) Input body parameters for the
               Create API key V1 REST request.
        :param str entity_lock: (optional) Indicates if the service ID is locked
               for further write operations. False by default.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceIdDetails` object
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_service_id')
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

        url = '/v1/serviceids'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_service_id(self, id: str, **kwargs) -> DetailedResponse:
        """
        Get details of a service ID.

        Returns the details of a service ID. Users can manage user API keys for themself,
        or service ID API keys for service IDs that are bound to an entity they have
        access to.

        :param str id: Unique ID of the service ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceIdDetails` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_service_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/serviceids/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_service_id(self, id: str, if_match: str, *, name: str = None, description: str = None, unique_instance_crns: List[str] = None, **kwargs) -> DetailedResponse:
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
        :rtype: DetailedResponse with `dict` result representing a `ServiceIdDetails` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_service_id')
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

        url = '/v1/serviceids/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_service_id(self, id: str, **kwargs) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_service_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/serviceids/{0}'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def lock_service_id(self, id: str, **kwargs) -> DetailedResponse:
        """
        Lock the service ID.

        Locks a service ID by ID. Users can manage user API keys for themself, or service
        ID API keys for service IDs that are bound to an entity they have access to.

        :param str id: Unique ID of the service ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceIdDetails` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='lock_service_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/serviceids/{0}/lock'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def unlock_service_id(self, id: str, **kwargs) -> DetailedResponse:
        """
        Unlock the service ID.

        Unlocks a service ID by ID. Users can manage user API keys for themself, or
        service ID API keys for service IDs that are bound to an entity they have access
        to.

        :param str id: Unique ID of the service ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceIdDetails` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='unlock_service_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/serviceids/{0}/lock'.format(*self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class ApiKeyDetails():
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
    :attr str apikey: The API key value. For API keys representing a user, this is
          only returned in the response to the create API key request.
    """

    def __init__(self, id: str, crn: str, locked: bool, name: str, iam_id: str, account_id: str, apikey: str, *, context: 'ResponseContext' = None, entity_tag: str = None, created_at: datetime = None, modified_at: datetime = None, description: str = None) -> None:
        """
        Initialize a ApiKeyDetails object.

        :param str id: Unique identifier of this API Key.
        :param str crn: Cloud Resource Name of the item. Example Cloud Resource
               Name:
               'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::apikey:1234-9012-5678'.
        :param bool locked: The API key cannot be changed if set to true.
        :param str name: Name of the API key. The name is not checked for
               uniqueness. Therefore multiple names with the same value can exist. Access
               is done via the UUID of the API key.
        :param str iam_id: The iam_id that this API key authenticates.
        :param str account_id: ID of the account that this API key authenticates
               for.
        :param str apikey: The API key value. For API keys representing a user,
               this is only returned in the response to the create API key request.
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
        """
        self.context = context
        self.id = id
        self.entity_tag = entity_tag
        self.crn = crn
        self.locked = locked
        self.created_at = created_at
        self.modified_at = modified_at
        self.name = name
        self.description = description
        self.iam_id = iam_id
        self.account_id = account_id
        self.apikey = apikey

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiKeyDetails':
        """Initialize a ApiKeyDetails object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ResponseContext.from_dict(_dict.get('context'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ApiKeyDetails JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ApiKeyDetails JSON')
        if 'locked' in _dict:
            args['locked'] = _dict.get('locked')
        else:
            raise ValueError('Required property \'locked\' not present in ApiKeyDetails JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ApiKeyDetails JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in ApiKeyDetails JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in ApiKeyDetails JSON')
        if 'apikey' in _dict:
            args['apikey'] = _dict.get('apikey')
        else:
            raise ValueError('Required property \'apikey\' not present in ApiKeyDetails JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiKeyDetails object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiKeyDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiKeyDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiKeyDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateApiKeyRequest():
    """
    Input body parameters for the Create API key V1 REST request.

    :attr str name: Name of the API key. The name is not checked for uniqueness.
          Therefore multiple names with the same value can exist. Access is done via the
          UUID of the API key.
    :attr str description: (optional) The optional description of the API key. The
          'description' property is only available if a description was provided during a
          create of an API key.
    :attr str iam_id: The iam_id that this API key authenticates.
    :attr str account_id: (optional) The account ID of the API key.
    :attr str apikey: (optional) You can optionally passthrough the API key value
          for this API key. If passed, NO validation of that apiKey value is done, i.e.
          the value can be non-URL safe. If omitted, the API key management will create an
          URL safe opaque API key value. The value of the API key is checked for
          uniqueness. Please ensure enough variations when passing in this value.
    """

    def __init__(self, name: str, iam_id: str, *, description: str = None, account_id: str = None, apikey: str = None) -> None:
        """
        Initialize a CreateApiKeyRequest object.

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
        """
        self.name = name
        self.description = description
        self.iam_id = iam_id
        self.account_id = account_id
        self.apikey = apikey

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateApiKeyRequest':
        """Initialize a CreateApiKeyRequest object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in CreateApiKeyRequest JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in CreateApiKeyRequest JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'apikey' in _dict:
            args['apikey'] = _dict.get('apikey')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateApiKeyRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateApiKeyRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateApiKeyRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateApiKeyRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExceptionResponseContext():
    """
    Context fill with key properties for problem determination.

    :attr str request_id: (optional) The request ID of the inbound REST request.
    :attr str request_type: (optional) The request type of the inbound REST request.
    :attr str user_agent: (optional) The user agent of the inbound REST request.
    :attr str client_ip: (optional) The client ip address of the inbound REST
          request.
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
    :attr str locale: (optional) The language used to present the error message.
    :attr str cluster_name: (optional) The cluster name.
    """

    def __init__(self, *, request_id: str = None, request_type: str = None, user_agent: str = None, client_ip: str = None, url: str = None, instance_id: str = None, thread_id: str = None, host: str = None, start_time: str = None, end_time: str = None, elapsed_time: str = None, locale: str = None, cluster_name: str = None) -> None:
        """
        Initialize a ExceptionResponseContext object.

        :param str request_id: (optional) The request ID of the inbound REST
               request.
        :param str request_type: (optional) The request type of the inbound REST
               request.
        :param str user_agent: (optional) The user agent of the inbound REST
               request.
        :param str client_ip: (optional) The client ip address of the inbound REST
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
        :param str locale: (optional) The language used to present the error
               message.
        :param str cluster_name: (optional) The cluster name.
        """
        self.request_id = request_id
        self.request_type = request_type
        self.user_agent = user_agent
        self.client_ip = client_ip
        self.url = url
        self.instance_id = instance_id
        self.thread_id = thread_id
        self.host = host
        self.start_time = start_time
        self.end_time = end_time
        self.elapsed_time = elapsed_time
        self.locale = locale
        self.cluster_name = cluster_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ExceptionResponseContext':
        """Initialize a ExceptionResponseContext object from a json dictionary."""
        args = {}
        if 'requestId' in _dict:
            args['request_id'] = _dict.get('requestId')
        if 'requestType' in _dict:
            args['request_type'] = _dict.get('requestType')
        if 'userAgent' in _dict:
            args['user_agent'] = _dict.get('userAgent')
        if 'clientIp' in _dict:
            args['client_ip'] = _dict.get('clientIp')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'instanceId' in _dict:
            args['instance_id'] = _dict.get('instanceId')
        if 'threadId' in _dict:
            args['thread_id'] = _dict.get('threadId')
        if 'host' in _dict:
            args['host'] = _dict.get('host')
        if 'startTime' in _dict:
            args['start_time'] = _dict.get('startTime')
        if 'endTime' in _dict:
            args['end_time'] = _dict.get('endTime')
        if 'elapsedTime' in _dict:
            args['elapsed_time'] = _dict.get('elapsedTime')
        if 'locale' in _dict:
            args['locale'] = _dict.get('locale')
        if 'clusterName' in _dict:
            args['cluster_name'] = _dict.get('clusterName')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExceptionResponseContext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request_id') and self.request_id is not None:
            _dict['requestId'] = self.request_id
        if hasattr(self, 'request_type') and self.request_type is not None:
            _dict['requestType'] = self.request_type
        if hasattr(self, 'user_agent') and self.user_agent is not None:
            _dict['userAgent'] = self.user_agent
        if hasattr(self, 'client_ip') and self.client_ip is not None:
            _dict['clientIp'] = self.client_ip
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instanceId'] = self.instance_id
        if hasattr(self, 'thread_id') and self.thread_id is not None:
            _dict['threadId'] = self.thread_id
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['startTime'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['endTime'] = self.end_time
        if hasattr(self, 'elapsed_time') and self.elapsed_time is not None:
            _dict['elapsedTime'] = self.elapsed_time
        if hasattr(self, 'locale') and self.locale is not None:
            _dict['locale'] = self.locale
        if hasattr(self, 'cluster_name') and self.cluster_name is not None:
            _dict['clusterName'] = self.cluster_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ExceptionResponseContext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ExceptionResponseContext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ExceptionResponseContext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListApiKeysResponse():
    """
    Response body format for the List API keys V1 REST request.

    :attr ExceptionResponseContext context: (optional) Context fill with key
          properties for problem determination.
    :attr int offset: (optional) The offset of the current page.
    :attr int limit: (optional) Optional size of a single page. Default is 20 items
          per page. Valid range is 1 to 100.
    :attr str first: (optional) Link to the first page.
    :attr str previous: (optional) Link to the previous available page. If
          'previous' property is not part of the response no previous page is available.
    :attr str next: (optional) Link to the next available page. If 'next' property
          is not part of the response no next page is available.
    :attr List[ApiKeyDetails] apikeys: List of API keys based on the query paramters
          and the page size. The apikeys array is always part of the response but might be
          empty depending on the query parameters values provided.
    """

    def __init__(self, apikeys: List['ApiKeyDetails'], *, context: 'ExceptionResponseContext' = None, offset: int = None, limit: int = None, first: str = None, previous: str = None, next: str = None) -> None:
        """
        Initialize a ListApiKeysResponse object.

        :param List[ApiKeyDetails] apikeys: List of API keys based on the query
               paramters and the page size. The apikeys array is always part of the
               response but might be empty depending on the query parameters values
               provided.
        :param ExceptionResponseContext context: (optional) Context fill with key
               properties for problem determination.
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
    def from_dict(cls, _dict: Dict) -> 'ListApiKeysResponse':
        """Initialize a ListApiKeysResponse object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ExceptionResponseContext.from_dict(_dict.get('context'))
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
            args['apikeys'] = [ApiKeyDetails.from_dict(x) for x in _dict.get('apikeys')]
        else:
            raise ValueError('Required property \'apikeys\' not present in ListApiKeysResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListApiKeysResponse object from a json dictionary."""
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
        """Return a `str` version of this ListApiKeysResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListApiKeysResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListApiKeysResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResponseContext():
    """
    Context with key properties for problem determination.

    :attr str transaction_id: (optional) The transaction ID of the inbound REST
          request.
    :attr str operation: (optional) The operation of the inbound REST request.
    :attr str user_agent: (optional) The user agent of the inbound REST request.
    :attr str client_ip: (optional) The client ip address of the inbound REST
          request.
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

    def __init__(self, *, transaction_id: str = None, operation: str = None, user_agent: str = None, client_ip: str = None, url: str = None, instance_id: str = None, thread_id: str = None, host: str = None, start_time: str = None, end_time: str = None, elapsed_time: str = None, cluster_name: str = None) -> None:
        """
        Initialize a ResponseContext object.

        :param str transaction_id: (optional) The transaction ID of the inbound
               REST request.
        :param str operation: (optional) The operation of the inbound REST request.
        :param str user_agent: (optional) The user agent of the inbound REST
               request.
        :param str client_ip: (optional) The client ip address of the inbound REST
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
        self.client_ip = client_ip
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
        if 'client_ip' in _dict:
            args['client_ip'] = _dict.get('client_ip')
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
        if hasattr(self, 'client_ip') and self.client_ip is not None:
            _dict['client_ip'] = self.client_ip
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


class ServiceIdDetails():
    """
    Response body format for service ID V1 REST requests.

    :attr ResponseContext context: (optional) Context with key properties for
          problem determination.
    :attr str id: Unique identifier of this Service ID.
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
    :attr str name: Name of the service ID. The name is not checked for uniqueness.
          Therefore multiple names with the same value can exist. Access is done via the
          UUID of the service ID.
    :attr str description: (optional) The optional description of the service ID.
          The 'description' property is only available if a description was provided
          during a create of a service ID.
    :attr List[str] unique_instance_crns: (optional) Optional list of CRNs (string
          array) which point to the services connected to the service ID.
    :attr ApiKeyDetails apikey: Response body format for API key V1 REST requests.
    """

    def __init__(self, id: str, iam_id: str, crn: str, locked: bool, account_id: str, name: str, apikey: 'ApiKeyDetails', *, context: 'ResponseContext' = None, entity_tag: str = None, created_at: datetime = None, modified_at: datetime = None, description: str = None, unique_instance_crns: List[str] = None) -> None:
        """
        Initialize a ServiceIdDetails object.

        :param str id: Unique identifier of this Service ID.
        :param str iam_id: Cloud wide identifier for identities of this service ID.
        :param str crn: Cloud Resource Name of the item. Example Cloud Resource
               Name:
               'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::serviceid:1234-5678-9012'.
        :param bool locked: The service ID cannot be changed if set to true.
        :param str account_id: ID of the account the service ID belongs to.
        :param str name: Name of the service ID. The name is not checked for
               uniqueness. Therefore multiple names with the same value can exist. Access
               is done via the UUID of the service ID.
        :param ApiKeyDetails apikey: Response body format for API key V1 REST
               requests.
        :param ResponseContext context: (optional) Context with key properties for
               problem determination.
        :param str entity_tag: (optional) Version of the service ID details object.
               You need to specify this value when updating the service ID to avoid stale
               updates.
        :param datetime created_at: (optional) If set contains a date time string
               of the creation date in ISO format.
        :param datetime modified_at: (optional) If set contains a date time string
               of the last modification date in ISO format.
        :param str description: (optional) The optional description of the service
               ID. The 'description' property is only available if a description was
               provided during a create of a service ID.
        :param List[str] unique_instance_crns: (optional) Optional list of CRNs
               (string array) which point to the services connected to the service ID.
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
        self.apikey = apikey

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceIdDetails':
        """Initialize a ServiceIdDetails object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ResponseContext.from_dict(_dict.get('context'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ServiceIdDetails JSON')
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in ServiceIdDetails JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ServiceIdDetails JSON')
        if 'locked' in _dict:
            args['locked'] = _dict.get('locked')
        else:
            raise ValueError('Required property \'locked\' not present in ServiceIdDetails JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in ServiceIdDetails JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ServiceIdDetails JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'unique_instance_crns' in _dict:
            args['unique_instance_crns'] = _dict.get('unique_instance_crns')
        if 'apikey' in _dict:
            args['apikey'] = ApiKeyDetails.from_dict(_dict.get('apikey'))
        else:
            raise ValueError('Required property \'apikey\' not present in ServiceIdDetails JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceIdDetails object from a json dictionary."""
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
        if hasattr(self, 'apikey') and self.apikey is not None:
            _dict['apikey'] = self.apikey.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceIdDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceIdDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceIdDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceIdsList():
    """
    Response body format for the list service ID V1 REST request.

    :attr ExceptionResponseContext context: (optional) Context fill with key
          properties for problem determination.
    :attr int offset: (optional) The offset of the current page.
    :attr int limit: (optional) Optional size of a single page. Default is 20 items
          per page. Valid range is 1 to 100.
    :attr str first: (optional) Link to the first page.
    :attr str previous: (optional) Link to the previous available page. If
          'previous' property is not part of the response no previous page is available.
    :attr str next: (optional) Link to the next available page. If 'next' property
          is not part of the response no next page is available.
    :attr List[ServiceIdDetails] serviceids: List of service IDs based on the query
          paramters and the page size. The service IDs array is always part of the
          response but might be empty depending on the query parameter values provided.
    """

    def __init__(self, serviceids: List['ServiceIdDetails'], *, context: 'ExceptionResponseContext' = None, offset: int = None, limit: int = None, first: str = None, previous: str = None, next: str = None) -> None:
        """
        Initialize a ServiceIdsList object.

        :param List[ServiceIdDetails] serviceids: List of service IDs based on the
               query paramters and the page size. The service IDs array is always part of
               the response but might be empty depending on the query parameter values
               provided.
        :param ExceptionResponseContext context: (optional) Context fill with key
               properties for problem determination.
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
    def from_dict(cls, _dict: Dict) -> 'ServiceIdsList':
        """Initialize a ServiceIdsList object from a json dictionary."""
        args = {}
        if 'context' in _dict:
            args['context'] = ExceptionResponseContext.from_dict(_dict.get('context'))
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
            args['serviceids'] = [ServiceIdDetails.from_dict(x) for x in _dict.get('serviceids')]
        else:
            raise ValueError('Required property \'serviceids\' not present in ServiceIdsList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceIdsList object from a json dictionary."""
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
        """Return a `str` version of this ServiceIdsList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceIdsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceIdsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


