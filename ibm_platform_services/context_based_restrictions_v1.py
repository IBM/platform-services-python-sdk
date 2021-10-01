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

# IBM OpenAPI SDK Code Generator Version: 3.38.1-1037b405-20210908-184149

"""
With the Context Based Restrictions API, you can:
* Create, list, get, update, and delete network zones
* Create, list, get, update, and delete context-based restriction rules
* Get account settings

API Version: 1.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json
import sys

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers


##############################################################################
# Service
##############################################################################

class ContextBasedRestrictionsV1(BaseService):
    """The Context Based Restrictions V1 service."""

    DEFAULT_SERVICE_URL = 'https://cbr.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'context_based_restrictions'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                     ) -> 'ContextBasedRestrictionsV1':
        """
        Return a new client for the Context Based Restrictions service using the
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
        Construct a new client for the Context Based Restrictions service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)

    #########################
    # Zones
    #########################

    def create_zone(self,
                    *,
                    name: str = None,
                    account_id: str = None,
                    addresses: List['Address'] = None,
                    description: str = None,
                    excluded: List['Address'] = None,
                    transaction_id: str = None,
                    **kwargs
                    ) -> DetailedResponse:
        """
        Create a zone.

        This operation creates a network zone for the specified account.

        :param str name: (optional) The name of the zone.
        :param str account_id: (optional) The id of the account owning this zone.
        :param List[Address] addresses: (optional) The list of addresses in the
               zone.
        :param str description: (optional) The description of the zone.
        :param List[Address] excluded: (optional) The list of excluded addresses in
               the zone.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Zone` object
        """

        if addresses is not None:
            addresses = [convert_model(x) for x in addresses]
        if excluded is not None:
            excluded = [convert_model(x) for x in excluded]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_zone')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'account_id': account_id,
            'addresses': addresses,
            'description': description,
            'excluded': excluded
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/zones'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def list_zones(self,
                   account_id: str,
                   *,
                   transaction_id: str = None,
                   name: str = None,
                   sort: str = None,
                   **kwargs
                   ) -> DetailedResponse:
        """
        List network zones.

        This operation lists network zones in the specified account.

        :param str account_id: The ID of the managing account.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param str name: (optional) The name of the zone.
        :param str sort: (optional) Sorts results by using a valid sort field. To
               learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZoneList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_zones')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'name': name,
            'sort': sort
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/zones'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def get_zone(self,
                 zone_id: str,
                 *,
                 transaction_id: str = None,
                 **kwargs
                 ) -> DetailedResponse:
        """
        Get the specified network zone.

        This operation returns the network zone for the specified ID.

        :param str zone_id: The ID of a zone.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Zone` object
        """

        if zone_id is None:
            raise ValueError('zone_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_zone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['zone_id']
        path_param_values = self.encode_path_vars(zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/zones/{zone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    def replace_zone(self,
                     zone_id: str,
                     if_match: str,
                     *,
                     name: str = None,
                     account_id: str = None,
                     addresses: List['Address'] = None,
                     description: str = None,
                     excluded: List['Address'] = None,
                     transaction_id: str = None,
                     **kwargs
                     ) -> DetailedResponse:
        """
        Update the specified network zone.

        This operation updates the network zone with the specified ID.

        :param str zone_id: The ID of a zone.
        :param str if_match: The current revision of the resource being updated.
               This can be found in the Create/Get/Update resource response ETag header.
        :param str name: (optional) The name of the zone.
        :param str account_id: (optional) The id of the account owning this zone.
        :param List[Address] addresses: (optional) The list of addresses in the
               zone.
        :param str description: (optional) The description of the zone.
        :param List[Address] excluded: (optional) The list of excluded addresses in
               the zone.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Zone` object
        """

        if zone_id is None:
            raise ValueError('zone_id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        if addresses is not None:
            addresses = [convert_model(x) for x in addresses]
        if excluded is not None:
            excluded = [convert_model(x) for x in excluded]
        headers = {
            'If-Match': if_match,
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='replace_zone')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'account_id': account_id,
            'addresses': addresses,
            'description': description,
            'excluded': excluded
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['zone_id']
        path_param_values = self.encode_path_vars(zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/zones/{zone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_zone(self,
                    zone_id: str,
                    *,
                    transaction_id: str = None,
                    **kwargs
                    ) -> DetailedResponse:
        """
        Delete the specified network zone.

        This operation deletes the network zone with the specified home ID.

        :param str zone_id: The ID of a zone.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if zone_id is None:
            raise ValueError('zone_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_zone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['zone_id']
        path_param_values = self.encode_path_vars(zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/zones/{zone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    def list_available_serviceref_targets(self,
                                          *,
                                          type: str = None,
                                          **kwargs
                                          ) -> DetailedResponse:
        """
        List available service reference targets.

        This operation lists all available service reference targets.

        :param str type: (optional) Specifies the types of services to retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceRefTargetList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_available_serviceref_targets')
        headers.update(sdk_headers)

        params = {
            'type': type
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/zones/serviceref_targets'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Rules
    #########################

    def create_rule(self,
                    *,
                    contexts: List['RuleContext'] = None,
                    resources: List['Resource'] = None,
                    description: str = None,
                    transaction_id: str = None,
                    **kwargs
                    ) -> DetailedResponse:
        """
        Create a rule.

        This operation creates a rule for the specified account.

        :param List[RuleContext] contexts: (optional) The contexts this rule
               applies to.
        :param List[Resource] resources: (optional) The resources this rule apply
               to.
        :param str description: (optional) The description of the rule.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if contexts is not None:
            contexts = [convert_model(x) for x in contexts]
        if resources is not None:
            resources = [convert_model(x) for x in resources]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_rule')
        headers.update(sdk_headers)

        data = {
            'contexts': contexts,
            'resources': resources,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/rules'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def list_rules(self,
                   account_id: str,
                   *,
                   transaction_id: str = None,
                   region: str = None,
                   resource: str = None,
                   resource_type: str = None,
                   service_instance: str = None,
                   service_name: str = None,
                   service_type: str = None,
                   zone_id: str = None,
                   sort: str = None,
                   **kwargs
                   ) -> DetailedResponse:
        """
        List rules.

        This operation lists rules for the specified account.

        :param str account_id: The ID of the managing account.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param str region: (optional) The `region` resource attribute.
        :param str resource: (optional) The `resource` resource attribute.
        :param str resource_type: (optional) The `resourceType` resource attribute.
        :param str service_instance: (optional) The `serviceInstance` resource
               attribute.
        :param str service_name: (optional) The `serviceName` resource attribute.
        :param str service_type: (optional) The rule's `serviceType` resource
               attribute.
        :param str zone_id: (optional) The globally unique ID of the zone.
        :param str sort: (optional) Sorts results by using a valid sort field. To
               learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RuleList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_rules')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'region': region,
            'resource': resource,
            'resource_type': resource_type,
            'service_instance': service_instance,
            'service_name': service_name,
            'service_type': service_type,
            'zone_id': zone_id,
            'sort': sort
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v1/rules'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def get_rule(self,
                 rule_id: str,
                 *,
                 transaction_id: str = None,
                 **kwargs
                 ) -> DetailedResponse:
        """
        Get the specified rule.

        This operation gets the rule for the specified ID.

        :param str rule_id: The ID of a rule.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    def replace_rule(self,
                     rule_id: str,
                     if_match: str,
                     *,
                     contexts: List['RuleContext'] = None,
                     resources: List['Resource'] = None,
                     description: str = None,
                     transaction_id: str = None,
                     **kwargs
                     ) -> DetailedResponse:
        """
        Update the specified rule.

        This operation updates the rule for the specified ID.

        :param str rule_id: The ID of a rule.
        :param str if_match: The current revision of the resource being updated.
               This can be found in the Create/Get/Update resource response ETag header.
        :param List[RuleContext] contexts: (optional) The contexts this rule
               applies to.
        :param List[Resource] resources: (optional) The resources this rule apply
               to.
        :param str description: (optional) The description of the rule.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        if contexts is not None:
            contexts = [convert_model(x) for x in contexts]
        if resources is not None:
            resources = [convert_model(x) for x in resources]
        headers = {
            'If-Match': if_match,
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='replace_rule')
        headers.update(sdk_headers)

        data = {
            'contexts': contexts,
            'resources': resources,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_rule(self,
                    rule_id: str,
                    *,
                    transaction_id: str = None,
                    **kwargs
                    ) -> DetailedResponse:
        """
        Delete the specified rule.

        This operation deletes the rule for the specified home ID.

        :param str rule_id: The ID of a rule.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
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
        Get the specified account settings.

        This operation gets the settings for the specified account ID.

        :param str account_id: The ID of the account the settings are for.
        :param str transaction_id: (optional) The UUID that is used to correlate
               and track transactions. If you omit this field, the service generates and
               sends a transaction ID in the response.
               **Note:** To help with debugging, we strongly recommend that you generate
               and supply a `Transaction-Id` with each request.
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
                                      service_version='V1',
                                      operation_id='get_account_settings')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/account_settings/{account_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


class ListAvailableServicerefTargetsEnums:
    """
    Enums for list_available_serviceref_targets parameters.
    """

    class Type(str, Enum):
        """
        Specifies the types of services to retrieve.
        """
        ALL = 'all'
        PLATFORM_SERVICE = 'platform_service'


##############################################################################
# Models
##############################################################################


class AccountSettings():
    """
    An output account settings.

    :attr str id: The globally unique ID of the account settings.
    :attr str crn: The account settings CRN.
    :attr int rule_count_limit: the max number of rules allowed for the account.
    :attr int zone_count_limit: the max number of zones allowed for the account.
    :attr int current_rule_count: the current number of rules used by the account.
    :attr int current_zone_count: the current number of zones used by the account.
    :attr str href: The href link to the resource.
    :attr datetime created_at: The time the resource was created.
    :attr str created_by_id: IAM ID of the user or service which created the
          resource.
    :attr datetime last_modified_at: The last time the resource was modified.
    :attr str last_modified_by_id: IAM ID of the user or service which modified the
          resource.
    """

    def __init__(self,
                 id: str,
                 crn: str,
                 rule_count_limit: int,
                 zone_count_limit: int,
                 current_rule_count: int,
                 current_zone_count: int,
                 href: str,
                 created_at: datetime,
                 created_by_id: str,
                 last_modified_at: datetime,
                 last_modified_by_id: str) -> None:
        """
        Initialize a AccountSettings object.

        :param str id: The globally unique ID of the account settings.
        :param str crn: The account settings CRN.
        :param int rule_count_limit: the max number of rules allowed for the
               account.
        :param int zone_count_limit: the max number of zones allowed for the
               account.
        :param int current_rule_count: the current number of rules used by the
               account.
        :param int current_zone_count: the current number of zones used by the
               account.
        :param str href: The href link to the resource.
        :param datetime created_at: The time the resource was created.
        :param str created_by_id: IAM ID of the user or service which created the
               resource.
        :param datetime last_modified_at: The last time the resource was modified.
        :param str last_modified_by_id: IAM ID of the user or service which
               modified the resource.
        """
        self.id = id
        self.crn = crn
        self.rule_count_limit = rule_count_limit
        self.zone_count_limit = zone_count_limit
        self.current_rule_count = current_rule_count
        self.current_zone_count = current_zone_count
        self.href = href
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountSettings':
        """Initialize a AccountSettings object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AccountSettings JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in AccountSettings JSON')
        if 'rule_count_limit' in _dict:
            args['rule_count_limit'] = _dict.get('rule_count_limit')
        else:
            raise ValueError('Required property \'rule_count_limit\' not present in AccountSettings JSON')
        if 'zone_count_limit' in _dict:
            args['zone_count_limit'] = _dict.get('zone_count_limit')
        else:
            raise ValueError('Required property \'zone_count_limit\' not present in AccountSettings JSON')
        if 'current_rule_count' in _dict:
            args['current_rule_count'] = _dict.get('current_rule_count')
        else:
            raise ValueError('Required property \'current_rule_count\' not present in AccountSettings JSON')
        if 'current_zone_count' in _dict:
            args['current_zone_count'] = _dict.get('current_zone_count')
        else:
            raise ValueError('Required property \'current_zone_count\' not present in AccountSettings JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in AccountSettings JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in AccountSettings JSON')
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        else:
            raise ValueError('Required property \'created_by_id\' not present in AccountSettings JSON')
        if 'last_modified_at' in _dict:
            args['last_modified_at'] = string_to_datetime(_dict.get('last_modified_at'))
        else:
            raise ValueError('Required property \'last_modified_at\' not present in AccountSettings JSON')
        if 'last_modified_by_id' in _dict:
            args['last_modified_by_id'] = _dict.get('last_modified_by_id')
        else:
            raise ValueError('Required property \'last_modified_by_id\' not present in AccountSettings JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'rule_count_limit') and self.rule_count_limit is not None:
            _dict['rule_count_limit'] = self.rule_count_limit
        if hasattr(self, 'zone_count_limit') and self.zone_count_limit is not None:
            _dict['zone_count_limit'] = self.zone_count_limit
        if hasattr(self, 'current_rule_count') and self.current_rule_count is not None:
            _dict['current_rule_count'] = self.current_rule_count
        if hasattr(self, 'current_zone_count') and self.current_zone_count is not None:
            _dict['current_zone_count'] = self.current_zone_count
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


class Address():
    """
    A zone address.

    :attr str type: (optional) The type of address.
    """

    def __init__(self,
                 *,
                 type: str = None) -> None:
        """
        Initialize a Address object.

        :param str type: (optional) The type of address.
        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(
                ['AddressIPAddress', 'AddressIPAddressRange', 'AddressSubnet', 'AddressVPC', 'AddressServiceRef']))
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Address':
        """Initialize a Address object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = ("Cannot convert dictionary into an instance of base class 'Address'. " +
               "The discriminator value should map to a valid subclass: {1}").format(
            ", ".join(
                ['AddressIPAddress', 'AddressIPAddressRange', 'AddressSubnet', 'AddressVPC', 'AddressServiceRef']))
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a Address object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['ipAddress'] = 'AddressIPAddress'
        mapping['ipRange'] = 'AddressIPAddressRange'
        mapping['subnet'] = 'AddressSubnet'
        mapping['vpc'] = 'AddressVPC'
        mapping['serviceRef'] = 'AddressServiceRef'
        disc_value = _dict.get('type')
        if disc_value is None:
            raise ValueError('Discriminator property \'type\' not found in Address JSON')
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)

    class TypeEnum(str, Enum):
        """
        The type of address.
        """
        IPADDRESS = 'ipAddress'
        IPRANGE = 'ipRange'
        SUBNET = 'subnet'
        VPC = 'vpc'
        SERVICEREF = 'serviceRef'


class Resource():
    """
    An rule resource.

    :attr List[ResourceAttribute] attributes: The resource attributes.
    :attr List[ResourceTagAttribute] tags: (optional) The optional resource tags.
    """

    def __init__(self,
                 attributes: List['ResourceAttribute'],
                 *,
                 tags: List['ResourceTagAttribute'] = None) -> None:
        """
        Initialize a Resource object.

        :param List[ResourceAttribute] attributes: The resource attributes.
        :param List[ResourceTagAttribute] tags: (optional) The optional resource
               tags.
        """
        self.attributes = attributes
        self.tags = tags

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Resource':
        """Initialize a Resource object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [ResourceAttribute.from_dict(x) for x in _dict.get('attributes')]
        else:
            raise ValueError('Required property \'attributes\' not present in Resource JSON')
        if 'tags' in _dict:
            args['tags'] = [ResourceTagAttribute.from_dict(x) for x in _dict.get('tags')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Resource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x.to_dict() for x in self.attributes]
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = [x.to_dict() for x in self.tags]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Resource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Resource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Resource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceAttribute():
    """
    A rule resource attribute.

    :attr str name: The attribute name.
    :attr str value: The attribute value.
    :attr str operator: (optional) The attribute operator.
    """

    def __init__(self,
                 name: str,
                 value: str,
                 *,
                 operator: str = None) -> None:
        """
        Initialize a ResourceAttribute object.

        :param str name: The attribute name.
        :param str value: The attribute value.
        :param str operator: (optional) The attribute operator.
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


class ResourceTagAttribute():
    """
    A rule resource tag attribute.

    :attr str name: The tag attribute name.
    :attr str value: The tag attribute value.
    :attr str operator: (optional) The attribute operator.
    """

    def __init__(self,
                 name: str,
                 value: str,
                 *,
                 operator: str = None) -> None:
        """
        Initialize a ResourceTagAttribute object.

        :param str name: The tag attribute name.
        :param str value: The tag attribute value.
        :param str operator: (optional) The attribute operator.
        """
        self.name = name
        self.value = value
        self.operator = operator

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceTagAttribute':
        """Initialize a ResourceTagAttribute object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ResourceTagAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ResourceTagAttribute JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceTagAttribute object from a json dictionary."""
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
        """Return a `str` version of this ResourceTagAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceTagAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceTagAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Rule():
    """
    An output rule.

    :attr str id: The globally unique ID of the rule.
    :attr str crn: The rule CRN.
    :attr str description: The description of the rule.
    :attr List[RuleContext] contexts: The contexts this rule applies to.
    :attr List[Resource] resources: The resources this rule apply to.
    :attr str href: The href link to the resource.
    :attr datetime created_at: The time the resource was created.
    :attr str created_by_id: IAM ID of the user or service which created the
          resource.
    :attr datetime last_modified_at: The last time the resource was modified.
    :attr str last_modified_by_id: IAM ID of the user or service which modified the
          resource.
    """

    def __init__(self,
                 id: str,
                 crn: str,
                 description: str,
                 contexts: List['RuleContext'],
                 resources: List['Resource'],
                 href: str,
                 created_at: datetime,
                 created_by_id: str,
                 last_modified_at: datetime,
                 last_modified_by_id: str) -> None:
        """
        Initialize a Rule object.

        :param str id: The globally unique ID of the rule.
        :param str crn: The rule CRN.
        :param str description: The description of the rule.
        :param List[RuleContext] contexts: The contexts this rule applies to.
        :param List[Resource] resources: The resources this rule apply to.
        :param str href: The href link to the resource.
        :param datetime created_at: The time the resource was created.
        :param str created_by_id: IAM ID of the user or service which created the
               resource.
        :param datetime last_modified_at: The last time the resource was modified.
        :param str last_modified_by_id: IAM ID of the user or service which
               modified the resource.
        """
        self.id = id
        self.crn = crn
        self.description = description
        self.contexts = contexts
        self.resources = resources
        self.href = href
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
        else:
            raise ValueError('Required property \'id\' not present in Rule JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in Rule JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in Rule JSON')
        if 'contexts' in _dict:
            args['contexts'] = [RuleContext.from_dict(x) for x in _dict.get('contexts')]
        else:
            raise ValueError('Required property \'contexts\' not present in Rule JSON')
        if 'resources' in _dict:
            args['resources'] = [Resource.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in Rule JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in Rule JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in Rule JSON')
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        else:
            raise ValueError('Required property \'created_by_id\' not present in Rule JSON')
        if 'last_modified_at' in _dict:
            args['last_modified_at'] = string_to_datetime(_dict.get('last_modified_at'))
        else:
            raise ValueError('Required property \'last_modified_at\' not present in Rule JSON')
        if 'last_modified_by_id' in _dict:
            args['last_modified_by_id'] = _dict.get('last_modified_by_id')
        else:
            raise ValueError('Required property \'last_modified_by_id\' not present in Rule JSON')
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
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'contexts') and self.contexts is not None:
            _dict['contexts'] = [x.to_dict() for x in self.contexts]
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


class RuleContext():
    """
    A rule context.

    :attr List[RuleContextAttribute] attributes: The attributes.
    """

    def __init__(self,
                 attributes: List['RuleContextAttribute']) -> None:
        """
        Initialize a RuleContext object.

        :param List[RuleContextAttribute] attributes: The attributes.
        """
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleContext':
        """Initialize a RuleContext object from a json dictionary."""
        args = {}
        if 'attributes' in _dict:
            args['attributes'] = [RuleContextAttribute.from_dict(x) for x in _dict.get('attributes')]
        else:
            raise ValueError('Required property \'attributes\' not present in RuleContext JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleContext object from a json dictionary."""
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
        """Return a `str` version of this RuleContext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleContext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleContext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuleContextAttribute():
    """
    An rule context attribute.

    :attr str name: The attribute name.
    :attr str value: The attribute value.
    """

    def __init__(self,
                 name: str,
                 value: str) -> None:
        """
        Initialize a RuleContextAttribute object.

        :param str name: The attribute name.
        :param str value: The attribute value.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleContextAttribute':
        """Initialize a RuleContextAttribute object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in RuleContextAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in RuleContextAttribute JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleContextAttribute object from a json dictionary."""
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
        """Return a `str` version of this RuleContextAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleContextAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleContextAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuleList():
    """
    The response object of the ListRules operation.

    :attr int count: The number of returned results.
    :attr List[Rule] rules: The returned rules.
    """

    def __init__(self,
                 count: int,
                 rules: List['Rule']) -> None:
        """
        Initialize a RuleList object.

        :param int count: The number of returned results.
        :param List[Rule] rules: The returned rules.
        """
        self.count = count
        self.rules = rules

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleList':
        """Initialize a RuleList object from a json dictionary."""
        args = {}
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in RuleList JSON')
        if 'rules' in _dict:
            args['rules'] = [Rule.from_dict(x) for x in _dict.get('rules')]
        else:
            raise ValueError('Required property \'rules\' not present in RuleList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'rules') and self.rules is not None:
            _dict['rules'] = [x.to_dict() for x in self.rules]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceRefTarget():
    """
    Summary information about a service reference target.

    :attr str service_name: The name of the service.
    :attr str service_type: (optional) The type of the service.
    """

    def __init__(self,
                 service_name: str,
                 *,
                 service_type: str = None) -> None:
        """
        Initialize a ServiceRefTarget object.

        :param str service_name: The name of the service.
        :param str service_type: (optional) The type of the service.
        """
        self.service_name = service_name
        self.service_type = service_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceRefTarget':
        """Initialize a ServiceRefTarget object from a json dictionary."""
        args = {}
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        else:
            raise ValueError('Required property \'service_name\' not present in ServiceRefTarget JSON')
        if 'service_type' in _dict:
            args['service_type'] = _dict.get('service_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceRefTarget object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'service_type') and self.service_type is not None:
            _dict['service_type'] = self.service_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceRefTarget object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceRefTarget') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceRefTarget') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceRefTargetList():
    """
    A list of service reference targets.

    :attr int count: The number of returned results.
    :attr List[ServiceRefTarget] targets: The list of service reference targets.
    """

    def __init__(self,
                 count: int,
                 targets: List['ServiceRefTarget']) -> None:
        """
        Initialize a ServiceRefTargetList object.

        :param int count: The number of returned results.
        :param List[ServiceRefTarget] targets: The list of service reference
               targets.
        """
        self.count = count
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceRefTargetList':
        """Initialize a ServiceRefTargetList object from a json dictionary."""
        args = {}
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ServiceRefTargetList JSON')
        if 'targets' in _dict:
            args['targets'] = [ServiceRefTarget.from_dict(x) for x in _dict.get('targets')]
        else:
            raise ValueError('Required property \'targets\' not present in ServiceRefTargetList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceRefTargetList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = [x.to_dict() for x in self.targets]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceRefTargetList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceRefTargetList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceRefTargetList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceRefValue():
    """
    A service reference value.

    :attr str account_id: The id of the account owning the service.
    :attr str service_type: (optional) The service type.
    :attr str service_name: (optional) The service name.
    :attr str service_instance: (optional) The service instance.
    """

    def __init__(self,
                 account_id: str,
                 *,
                 service_type: str = None,
                 service_name: str = None,
                 service_instance: str = None) -> None:
        """
        Initialize a ServiceRefValue object.

        :param str account_id: The id of the account owning the service.
        :param str service_type: (optional) The service type.
        :param str service_name: (optional) The service name.
        :param str service_instance: (optional) The service instance.
        """
        self.account_id = account_id
        self.service_type = service_type
        self.service_name = service_name
        self.service_instance = service_instance

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceRefValue':
        """Initialize a ServiceRefValue object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in ServiceRefValue JSON')
        if 'service_type' in _dict:
            args['service_type'] = _dict.get('service_type')
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        if 'service_instance' in _dict:
            args['service_instance'] = _dict.get('service_instance')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceRefValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'service_type') and self.service_type is not None:
            _dict['service_type'] = self.service_type
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'service_instance') and self.service_instance is not None:
            _dict['service_instance'] = self.service_instance
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceRefValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceRefValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceRefValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Zone():
    """
    An output zone.

    :attr str id: The globally unique ID of the zone.
    :attr str crn: The zone CRN.
    :attr str name: The name of the zone.
    :attr str account_id: The id of the account owning this zone.
    :attr str description: The description of the zone.
    :attr List[Address] addresses: The list of addresses in the zone.
    :attr List[Address] excluded: The list of excluded addresses in the zone.
    :attr str href: The href link to the resource.
    :attr datetime created_at: The time the resource was created.
    :attr str created_by_id: IAM ID of the user or service which created the
          resource.
    :attr datetime last_modified_at: The last time the resource was modified.
    :attr str last_modified_by_id: IAM ID of the user or service which modified the
          resource.
    """

    def __init__(self,
                 id: str,
                 crn: str,
                 name: str,
                 account_id: str,
                 description: str,
                 addresses: List['Address'],
                 excluded: List['Address'],
                 href: str,
                 created_at: datetime,
                 created_by_id: str,
                 last_modified_at: datetime,
                 last_modified_by_id: str) -> None:
        """
        Initialize a Zone object.

        :param str id: The globally unique ID of the zone.
        :param str crn: The zone CRN.
        :param str name: The name of the zone.
        :param str account_id: The id of the account owning this zone.
        :param str description: The description of the zone.
        :param List[Address] addresses: The list of addresses in the zone.
        :param List[Address] excluded: The list of excluded addresses in the zone.
        :param str href: The href link to the resource.
        :param datetime created_at: The time the resource was created.
        :param str created_by_id: IAM ID of the user or service which created the
               resource.
        :param datetime last_modified_at: The last time the resource was modified.
        :param str last_modified_by_id: IAM ID of the user or service which
               modified the resource.
        """
        self.id = id
        self.crn = crn
        self.name = name
        self.account_id = account_id
        self.description = description
        self.addresses = addresses
        self.excluded = excluded
        self.href = href
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Zone':
        """Initialize a Zone object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Zone JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in Zone JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Zone JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in Zone JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in Zone JSON')
        if 'addresses' in _dict:
            args['addresses'] = [Address.from_dict(x) for x in _dict.get('addresses')]
        else:
            raise ValueError('Required property \'addresses\' not present in Zone JSON')
        if 'excluded' in _dict:
            args['excluded'] = [Address.from_dict(x) for x in _dict.get('excluded')]
        else:
            raise ValueError('Required property \'excluded\' not present in Zone JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in Zone JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in Zone JSON')
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        else:
            raise ValueError('Required property \'created_by_id\' not present in Zone JSON')
        if 'last_modified_at' in _dict:
            args['last_modified_at'] = string_to_datetime(_dict.get('last_modified_at'))
        else:
            raise ValueError('Required property \'last_modified_at\' not present in Zone JSON')
        if 'last_modified_by_id' in _dict:
            args['last_modified_by_id'] = _dict.get('last_modified_by_id')
        else:
            raise ValueError('Required property \'last_modified_by_id\' not present in Zone JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Zone object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'addresses') and self.addresses is not None:
            _dict['addresses'] = [x.to_dict() for x in self.addresses]
        if hasattr(self, 'excluded') and self.excluded is not None:
            _dict['excluded'] = [x.to_dict() for x in self.excluded]
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
        """Return a `str` version of this Zone object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Zone') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Zone') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ZoneList():
    """
    The response object of the ListZones operation.

    :attr int count: The number of returned results.
    :attr List[ZoneSummary] zones: The returned zones.
    """

    def __init__(self,
                 count: int,
                 zones: List['ZoneSummary']) -> None:
        """
        Initialize a ZoneList object.

        :param int count: The number of returned results.
        :param List[ZoneSummary] zones: The returned zones.
        """
        self.count = count
        self.zones = zones

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZoneList':
        """Initialize a ZoneList object from a json dictionary."""
        args = {}
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ZoneList JSON')
        if 'zones' in _dict:
            args['zones'] = [ZoneSummary.from_dict(x) for x in _dict.get('zones')]
        else:
            raise ValueError('Required property \'zones\' not present in ZoneList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZoneList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'zones') and self.zones is not None:
            _dict['zones'] = [x.to_dict() for x in self.zones]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ZoneList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZoneList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZoneList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ZoneSummary():
    """
    An output zone summary.

    :attr str id: The globally unique ID of the zone.
    :attr str crn: The zone CRN.
    :attr str name: The name of the zone.
    :attr str description: (optional) The description of the zone.
    :attr List[Address] addresses_preview: A preview of addresses in the zone (3
          addresses maximum).
    :attr int address_count: The number of addresses in the zone.
    :attr int excluded_count: The number of excluded addresses in the zone.
    :attr str href: The href link to the resource.
    :attr datetime created_at: The time the resource was created.
    :attr str created_by_id: IAM ID of the user or service which created the
          resource.
    :attr datetime last_modified_at: The last time the resource was modified.
    :attr str last_modified_by_id: IAM ID of the user or service which modified the
          resource.
    """

    def __init__(self,
                 id: str,
                 crn: str,
                 name: str,
                 addresses_preview: List['Address'],
                 address_count: int,
                 excluded_count: int,
                 href: str,
                 created_at: datetime,
                 created_by_id: str,
                 last_modified_at: datetime,
                 last_modified_by_id: str,
                 *,
                 description: str = None) -> None:
        """
        Initialize a ZoneSummary object.

        :param str id: The globally unique ID of the zone.
        :param str crn: The zone CRN.
        :param str name: The name of the zone.
        :param List[Address] addresses_preview: A preview of addresses in the zone
               (3 addresses maximum).
        :param int address_count: The number of addresses in the zone.
        :param int excluded_count: The number of excluded addresses in the zone.
        :param str href: The href link to the resource.
        :param datetime created_at: The time the resource was created.
        :param str created_by_id: IAM ID of the user or service which created the
               resource.
        :param datetime last_modified_at: The last time the resource was modified.
        :param str last_modified_by_id: IAM ID of the user or service which
               modified the resource.
        :param str description: (optional) The description of the zone.
        """
        self.id = id
        self.crn = crn
        self.name = name
        self.description = description
        self.addresses_preview = addresses_preview
        self.address_count = address_count
        self.excluded_count = excluded_count
        self.href = href
        self.created_at = created_at
        self.created_by_id = created_by_id
        self.last_modified_at = last_modified_at
        self.last_modified_by_id = last_modified_by_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZoneSummary':
        """Initialize a ZoneSummary object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ZoneSummary JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ZoneSummary JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ZoneSummary JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'addresses_preview' in _dict:
            args['addresses_preview'] = [Address.from_dict(x) for x in _dict.get('addresses_preview')]
        else:
            raise ValueError('Required property \'addresses_preview\' not present in ZoneSummary JSON')
        if 'address_count' in _dict:
            args['address_count'] = _dict.get('address_count')
        else:
            raise ValueError('Required property \'address_count\' not present in ZoneSummary JSON')
        if 'excluded_count' in _dict:
            args['excluded_count'] = _dict.get('excluded_count')
        else:
            raise ValueError('Required property \'excluded_count\' not present in ZoneSummary JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ZoneSummary JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ZoneSummary JSON')
        if 'created_by_id' in _dict:
            args['created_by_id'] = _dict.get('created_by_id')
        else:
            raise ValueError('Required property \'created_by_id\' not present in ZoneSummary JSON')
        if 'last_modified_at' in _dict:
            args['last_modified_at'] = string_to_datetime(_dict.get('last_modified_at'))
        else:
            raise ValueError('Required property \'last_modified_at\' not present in ZoneSummary JSON')
        if 'last_modified_by_id' in _dict:
            args['last_modified_by_id'] = _dict.get('last_modified_by_id')
        else:
            raise ValueError('Required property \'last_modified_by_id\' not present in ZoneSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZoneSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'addresses_preview') and self.addresses_preview is not None:
            _dict['addresses_preview'] = [x.to_dict() for x in self.addresses_preview]
        if hasattr(self, 'address_count') and self.address_count is not None:
            _dict['address_count'] = self.address_count
        if hasattr(self, 'excluded_count') and self.excluded_count is not None:
            _dict['excluded_count'] = self.excluded_count
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
        """Return a `str` version of this ZoneSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZoneSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZoneSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AddressIPAddress(Address):
    """
    A single IP address.

    :attr str type: The type of address.
    :attr str value: The IP address.
    """

    def __init__(self,
                 type: str,
                 value: str) -> None:
        """
        Initialize a AddressIPAddress object.

        :param str type: The type of address.
        :param str value: The IP address.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddressIPAddress':
        """Initialize a AddressIPAddress object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in AddressIPAddress JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in AddressIPAddress JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddressIPAddress object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddressIPAddress object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddressIPAddress') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddressIPAddress') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of address.
        """
        IPADDRESS = 'ipAddress'


class AddressIPAddressRange(Address):
    """
    An IP address range.

    :attr str type: The type of address.
    :attr str value: The ip range in <first-ip>-<last-ip> format.
    """

    def __init__(self,
                 type: str,
                 value: str) -> None:
        """
        Initialize a AddressIPAddressRange object.

        :param str type: The type of address.
        :param str value: The ip range in <first-ip>-<last-ip> format.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddressIPAddressRange':
        """Initialize a AddressIPAddressRange object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in AddressIPAddressRange JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in AddressIPAddressRange JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddressIPAddressRange object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddressIPAddressRange object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddressIPAddressRange') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddressIPAddressRange') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of address.
        """
        IPRANGE = 'ipRange'


class AddressServiceRef(Address):
    """
    A service reference.

    :attr str type: The type of address.
    :attr ServiceRefValue ref: A service reference value.
    """

    def __init__(self,
                 type: str,
                 ref: 'ServiceRefValue') -> None:
        """
        Initialize a AddressServiceRef object.

        :param str type: The type of address.
        :param ServiceRefValue ref: A service reference value.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.ref = ref

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddressServiceRef':
        """Initialize a AddressServiceRef object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in AddressServiceRef JSON')
        if 'ref' in _dict:
            args['ref'] = ServiceRefValue.from_dict(_dict.get('ref'))
        else:
            raise ValueError('Required property \'ref\' not present in AddressServiceRef JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddressServiceRef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'ref') and self.ref is not None:
            _dict['ref'] = self.ref.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddressServiceRef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddressServiceRef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddressServiceRef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of address.
        """
        SERVICEREF = 'serviceRef'


class AddressSubnet(Address):
    """
    A subnet in CIDR format.

    :attr str type: The type of address.
    :attr str value: The subnet in CIDR format.
    """

    def __init__(self,
                 type: str,
                 value: str) -> None:
        """
        Initialize a AddressSubnet object.

        :param str type: The type of address.
        :param str value: The subnet in CIDR format.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddressSubnet':
        """Initialize a AddressSubnet object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in AddressSubnet JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in AddressSubnet JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddressSubnet object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddressSubnet object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddressSubnet') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddressSubnet') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of address.
        """
        SUBNET = 'subnet'


class AddressVPC(Address):
    """
    A single VPC address.

    :attr str type: The type of address.
    :attr str value: The VPC CRN.
    """

    def __init__(self,
                 type: str,
                 value: str) -> None:
        """
        Initialize a AddressVPC object.

        :param str type: The type of address.
        :param str value: The VPC CRN.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddressVPC':
        """Initialize a AddressVPC object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in AddressVPC JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in AddressVPC JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddressVPC object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddressVPC object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddressVPC') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddressVPC') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of address.
        """
        VPC = 'vpc'
