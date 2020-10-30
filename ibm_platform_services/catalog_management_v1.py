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

# IBM OpenAPI SDK Code Generator Version: 99-SNAPSHOT-8d569e8f-20201030-111043
 
"""
This is the API to use for managing private catalogs for IBM Cloud. Private catalogs
provide a way to centrally manage access to products in the IBM Cloud catalog and your own
catalogs.
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

class CatalogManagementV1(BaseService):
    """The Catalog Management V1 service."""

    DEFAULT_SERVICE_URL = 'https://cm.globalcatalog.cloud.ibm.com/api/v1-beta'
    DEFAULT_SERVICE_NAME = 'catalog_management'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'CatalogManagementV1':
        """
        Return a new client for the Catalog Management service using the specified
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
        Construct a new client for the Catalog Management service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Account
    #########################


    def get_catalog_account(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the account settings.

        Get the account level settings for the account for private catalog.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Account` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_catalog_account')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/catalogaccount'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_catalog_account(self,
        *,
        id: str = None,
        account_filters: 'Filters' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set the account settings.

        :param str id: (optional) Account identification.
        :param Filters account_filters: (optional) Filters for account and catalog
               filters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_filters is not None:
            account_filters = convert_model(account_filters)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_catalog_account')
        headers.update(sdk_headers)

        data = {
            'id': id,
            'account_filters': account_filters
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/catalogaccount'
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_catalog_account_audit(self,
        *,
        id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the audit log(s) for catalog account.

        Get the audit log(s) for catalog account.

        :param str id: (optional) Log identification.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_catalog_account_audit')
        headers.update(sdk_headers)

        params = {
            'id': id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/catalogaccount/audit'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_catalog_account_filters(self,
        *,
        catalog: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the accumulated filters of the account and of the catalogs you have access to.

        Get the accumulated filters of the account and of the catalogs you have access to.

        :param str catalog: (optional) catalog id. Narrow down filters to the
               account and just the one catalog.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccumulatedFilters` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_catalog_account_filters')
        headers.update(sdk_headers)

        params = {
            'catalog': catalog
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/catalogaccount/filters'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Catalogs
    #########################


    def list_catalogs(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get list of catalogs.

        List the available catalogs for a given account.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CatalogSearchResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_catalogs')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/catalogs'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_catalog(self,
        *,
        id: str = None,
        rev: str = None,
        label: str = None,
        short_description: str = None,
        catalog_icon_url: str = None,
        tags: List[str] = None,
        url: str = None,
        crn: str = None,
        offerings_url: str = None,
        features: List['Feature'] = None,
        disabled: bool = None,
        created: datetime = None,
        updated: datetime = None,
        resource_group_id: str = None,
        owning_account: str = None,
        catalog_filters: 'Filters' = None,
        syndication_settings: 'SyndicationResource' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a catalog.

        Create a catalog for a given account.

        :param str id: (optional) Unique ID.
        :param str rev: (optional) Cloudant revision.
        :param str label: (optional) Display Name in the requested language.
        :param str short_description: (optional) Description in the requested
               language.
        :param str catalog_icon_url: (optional) URL for an icon associated with
               this catalog.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param str url: (optional) The url for this specific catalog.
        :param str crn: (optional) CRN associated with the catalog.
        :param str offerings_url: (optional) URL path to offerings.
        :param List[Feature] features: (optional) List of features associated with
               this catalog.
        :param bool disabled: (optional) Denotes whether a catalog is disabled.
        :param datetime created: (optional) The date'time this catalog was created.
        :param datetime updated: (optional) The date'time this catalog was last
               updated.
        :param str resource_group_id: (optional) Resource group id the catalog is
               owned by.
        :param str owning_account: (optional) Account that owns catalog.
        :param Filters catalog_filters: (optional) Filters for account and catalog
               filters.
        :param SyndicationResource syndication_settings: (optional) Feature
               information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Catalog` object
        """

        if features is not None:
            features = [convert_model(x) for x in features]
        if created is not None:
            created = datetime_to_string(created)
        if updated is not None:
            updated = datetime_to_string(updated)
        if catalog_filters is not None:
            catalog_filters = convert_model(catalog_filters)
        if syndication_settings is not None:
            syndication_settings = convert_model(syndication_settings)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_catalog')
        headers.update(sdk_headers)

        data = {
            'id': id,
            '_rev': rev,
            'label': label,
            'short_description': short_description,
            'catalog_icon_url': catalog_icon_url,
            'tags': tags,
            'url': url,
            'crn': crn,
            'offerings_url': offerings_url,
            'features': features,
            'disabled': disabled,
            'created': created,
            'updated': updated,
            'resource_group_id': resource_group_id,
            'owning_account': owning_account,
            'catalog_filters': catalog_filters,
            'syndication_settings': syndication_settings
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/catalogs'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_catalog(self,
        catalog_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a catalog.

        Get a catalog.

        :param str catalog_identifier: Catalog identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Catalog` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_catalog')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def replace_catalog(self,
        catalog_identifier: str,
        *,
        id: str = None,
        rev: str = None,
        label: str = None,
        short_description: str = None,
        catalog_icon_url: str = None,
        tags: List[str] = None,
        url: str = None,
        crn: str = None,
        offerings_url: str = None,
        features: List['Feature'] = None,
        disabled: bool = None,
        created: datetime = None,
        updated: datetime = None,
        resource_group_id: str = None,
        owning_account: str = None,
        catalog_filters: 'Filters' = None,
        syndication_settings: 'SyndicationResource' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a catalog.

        Update a catalog.

        :param str catalog_identifier: Catalog identifier.
        :param str id: (optional) Unique ID.
        :param str rev: (optional) Cloudant revision.
        :param str label: (optional) Display Name in the requested language.
        :param str short_description: (optional) Description in the requested
               language.
        :param str catalog_icon_url: (optional) URL for an icon associated with
               this catalog.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param str url: (optional) The url for this specific catalog.
        :param str crn: (optional) CRN associated with the catalog.
        :param str offerings_url: (optional) URL path to offerings.
        :param List[Feature] features: (optional) List of features associated with
               this catalog.
        :param bool disabled: (optional) Denotes whether a catalog is disabled.
        :param datetime created: (optional) The date'time this catalog was created.
        :param datetime updated: (optional) The date'time this catalog was last
               updated.
        :param str resource_group_id: (optional) Resource group id the catalog is
               owned by.
        :param str owning_account: (optional) Account that owns catalog.
        :param Filters catalog_filters: (optional) Filters for account and catalog
               filters.
        :param SyndicationResource syndication_settings: (optional) Feature
               information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Catalog` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if features is not None:
            features = [convert_model(x) for x in features]
        if created is not None:
            created = datetime_to_string(created)
        if updated is not None:
            updated = datetime_to_string(updated)
        if catalog_filters is not None:
            catalog_filters = convert_model(catalog_filters)
        if syndication_settings is not None:
            syndication_settings = convert_model(syndication_settings)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='replace_catalog')
        headers.update(sdk_headers)

        data = {
            'id': id,
            '_rev': rev,
            'label': label,
            'short_description': short_description,
            'catalog_icon_url': catalog_icon_url,
            'tags': tags,
            'url': url,
            'crn': crn,
            'offerings_url': offerings_url,
            'features': features,
            'disabled': disabled,
            'created': created,
            'updated': updated,
            'resource_group_id': resource_group_id,
            'owning_account': owning_account,
            'catalog_filters': catalog_filters,
            'syndication_settings': syndication_settings
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_catalog(self,
        catalog_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a catalog.

        Delete a catalog.

        :param str catalog_identifier: Catalog identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_catalog')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['catalog_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_catalog_audit(self,
        catalog_identifier: str,
        *,
        id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the audit log(s) for catalog.

        Get the audit log(s) for catalog.

        :param str catalog_identifier: Catalog identifier.
        :param str id: (optional) Log identification.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_catalog_audit')
        headers.update(sdk_headers)

        params = {
            'id': id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['catalog_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/audit'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Enterprise
    #########################


    def get_enterprise(self,
        enterprise_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the enterprise settings for the specified enterprise ID.

        Get the enterprise settings for the specified enterprise ID.

        :param str enterprise_id: Enterprise identification.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Enterprise` object
        """

        if enterprise_id is None:
            raise ValueError('enterprise_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_enterprise')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['enterprise_id']
        path_param_values = self.encode_path_vars(enterprise_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/enterprises/{enterprise_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def replace_enterprise(self,
        enterprise_id: str,
        *,
        id: str = None,
        rev: str = None,
        account_filters: 'Filters' = None,
        account_groups: 'EnterpriseAccountGroups' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set the enterprise settings.

        :param str enterprise_id: Enterprise identification.
        :param str id: (optional) Enterprise identification.
        :param str rev: (optional) Cloudant revision.
        :param Filters account_filters: (optional) Filters for account and catalog
               filters.
        :param EnterpriseAccountGroups account_groups: (optional) Map of account
               group ids to AccountGroup objects.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if enterprise_id is None:
            raise ValueError('enterprise_id must be provided')
        if account_filters is not None:
            account_filters = convert_model(account_filters)
        if account_groups is not None:
            account_groups = convert_model(account_groups)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='replace_enterprise')
        headers.update(sdk_headers)

        data = {
            'id': id,
            '_rev': rev,
            'account_filters': account_filters,
            'account_groups': account_groups
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['enterprise_id']
        path_param_values = self.encode_path_vars(enterprise_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/enterprises/{enterprise_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_enterprises_audit(self,
        enterprise_id: str,
        *,
        id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the audit log(s) for enterprises.

        Get the audit log(s) for enterprises.

        :param str enterprise_id: Enterprise identification.
        :param str id: (optional) Log identification.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if enterprise_id is None:
            raise ValueError('enterprise_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_enterprises_audit')
        headers.update(sdk_headers)

        params = {
            'id': id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['enterprise_id']
        path_param_values = self.encode_path_vars(enterprise_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/enterprises/{enterprise_id}/audit'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Offerings
    #########################


    def get_consumption_offerings(self,
        *,
        digest: bool = None,
        catalog: str = None,
        select: str = None,
        include_hidden: bool = None,
        limit: int = None,
        offset: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get list of offerings for consumption.

        List the available offerings from both public and from the account that currently
        scoped for consumption. These copies cannot be used updating. They are not
        complete and only return what is visible to the caller.

        :param bool digest: (optional) true - Strip down the content of what is
               returned. For example don't return the readme. Makes the result much
               smaller. Defaults to false.
        :param str catalog: (optional) catalog id. Narrow search down to just a
               particular catalog. It will apply the catalog's public filters to the
               public catalog offerings on the result.
        :param str select: (optional) What should be selected. Default is 'all'
               which will return both public and private offerings. 'public' returns only
               the public offerings and 'private' returns only the private offerings.
        :param bool include_hidden: (optional) true - include offerings which have
               been marked as hidden. The default is false and hidden offerings are not
               returned.
        :param int limit: (optional) number or results to return.
        :param int offset: (optional) number of results to skip before returning
               values.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OfferingSearchResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_consumption_offerings')
        headers.update(sdk_headers)

        params = {
            'digest': digest,
            'catalog': catalog,
            'select': select,
            'includeHidden': include_hidden,
            'limit': limit,
            'offset': offset
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/offerings'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def list_offerings(self,
        catalog_identifier: str,
        *,
        digest: bool = None,
        limit: int = None,
        offset: int = None,
        name: str = None,
        sort: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get list of offerings.

        List the available offerings in the specified catalog.

        :param str catalog_identifier: Catalog identifier.
        :param bool digest: (optional) true - Strip down the content of what is
               returned. For example don't return the readme. Makes the result much
               smaller. Defaults to false.
        :param int limit: (optional) number or results to return.
        :param int offset: (optional) number of results to skip before returning
               values.
        :param str name: (optional) only return results that contain the specified
               string.
        :param str sort: (optional) The field on which the output is sorted. Sorts
               by default by **label** property. Available fields are **name**, **label**,
               **created**, and **updated**. By adding **-** (i.e. **-label**) in front of
               the query string, you can specify descending order. Default is ascending
               order.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OfferingSearchResult` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_offerings')
        headers.update(sdk_headers)

        params = {
            'digest': digest,
            'limit': limit,
            'offset': offset,
            'name': name,
            'sort': sort
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_offering(self,
        catalog_identifier: str,
        *,
        id: str = None,
        rev: str = None,
        url: str = None,
        crn: str = None,
        label: str = None,
        name: str = None,
        offering_icon_url: str = None,
        offering_docs_url: str = None,
        offering_support_url: str = None,
        tags: List[str] = None,
        rating: 'Rating' = None,
        created: datetime = None,
        updated: datetime = None,
        short_description: str = None,
        long_description: str = None,
        features: List['Feature'] = None,
        kinds: List['Kind'] = None,
        permit_request_ibm_public_publish: bool = None,
        ibm_publish_approved: bool = None,
        public_publish_approved: bool = None,
        public_original_crn: str = None,
        publish_public_crn: str = None,
        portal_approval_record: str = None,
        portal_ui_url: str = None,
        catalog_id: str = None,
        catalog_name: str = None,
        metadata: object = None,
        disclaimer: str = None,
        hidden: bool = None,
        provider: str = None,
        repo_info: 'RepoInfo' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create an offering.

        Create an offering.

        :param str catalog_identifier: Catalog identifier.
        :param str id: (optional) unique id.
        :param str rev: (optional) Cloudant revision.
        :param str url: (optional) The url for this specific offering.
        :param str crn: (optional) The crn for this specific offering.
        :param str label: (optional) Display Name in the requested language.
        :param str name: (optional) The programmatic name of this offering.
        :param str offering_icon_url: (optional) URL for an icon associated with
               this offering.
        :param str offering_docs_url: (optional) URL for an additional docs with
               this offering.
        :param str offering_support_url: (optional) URL to be displayed in the
               Consumption UI for getting support on this offering.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param Rating rating: (optional) Repository info for offerings.
        :param datetime created: (optional) The date and time this catalog was
               created.
        :param datetime updated: (optional) The date and time this catalog was last
               updated.
        :param str short_description: (optional) Short description in the requested
               language.
        :param str long_description: (optional) Long description in the requested
               language.
        :param List[Feature] features: (optional) list of features associated with
               this offering.
        :param List[Kind] kinds: (optional) Array of kind.
        :param bool permit_request_ibm_public_publish: (optional) Is it permitted
               to request publishing to IBM or Public.
        :param bool ibm_publish_approved: (optional) Indicates if this offering has
               been approved for use by all IBMers.
        :param bool public_publish_approved: (optional) Indicates if this offering
               has been approved for use by all IBM Cloud users.
        :param str public_original_crn: (optional) The original offering CRN that
               this publish entry came from.
        :param str publish_public_crn: (optional) The crn of the public catalog
               entry of this offering.
        :param str portal_approval_record: (optional) The portal's approval record
               ID.
        :param str portal_ui_url: (optional) The portal UI URL.
        :param str catalog_id: (optional) The id of the catalog containing this
               offering.
        :param str catalog_name: (optional) The name of the catalog.
        :param object metadata: (optional) Map of metadata values for this
               offering.
        :param str disclaimer: (optional) A disclaimer for this offering.
        :param bool hidden: (optional) Determine if this offering should be
               displayed in the Consumption UI.
        :param str provider: (optional) Provider of this offering.
        :param RepoInfo repo_info: (optional) Repository info for offerings.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Offering` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if rating is not None:
            rating = convert_model(rating)
        if created is not None:
            created = datetime_to_string(created)
        if updated is not None:
            updated = datetime_to_string(updated)
        if features is not None:
            features = [convert_model(x) for x in features]
        if kinds is not None:
            kinds = [convert_model(x) for x in kinds]
        if repo_info is not None:
            repo_info = convert_model(repo_info)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_offering')
        headers.update(sdk_headers)

        data = {
            'id': id,
            '_rev': rev,
            'url': url,
            'crn': crn,
            'label': label,
            'name': name,
            'offering_icon_url': offering_icon_url,
            'offering_docs_url': offering_docs_url,
            'offering_support_url': offering_support_url,
            'tags': tags,
            'rating': rating,
            'created': created,
            'updated': updated,
            'short_description': short_description,
            'long_description': long_description,
            'features': features,
            'kinds': kinds,
            'permit_request_ibm_public_publish': permit_request_ibm_public_publish,
            'ibm_publish_approved': ibm_publish_approved,
            'public_publish_approved': public_publish_approved,
            'public_original_crn': public_original_crn,
            'publish_public_crn': publish_public_crn,
            'portal_approval_record': portal_approval_record,
            'portal_ui_url': portal_ui_url,
            'catalog_id': catalog_id,
            'catalog_name': catalog_name,
            'metadata': metadata,
            'disclaimer': disclaimer,
            'hidden': hidden,
            'provider': provider,
            'repo_info': repo_info
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def import_offering_version(self,
        catalog_identifier: str,
        offering_id: str,
        *,
        tags: List[str] = None,
        target_kinds: List[str] = None,
        content: List[int] = None,
        zipurl: str = None,
        target_version: str = None,
        include_config: bool = None,
        repo_type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Import new version to offering from a tgz.

        Import new version to offering from a tgz.

        :param str catalog_identifier: Catalog identifier.
        :param str offering_id: Offering identification.
        :param List[str] tags: (optional) Tags array.
        :param List[str] target_kinds: (optional) Target kinds.  Current valid
               values are 'iks', 'roks', 'vcenter', and 'terraform'.
        :param List[int] content: (optional) byte array representing the content to
               be imported.  Only supported for OVA images at this time.
        :param str zipurl: (optional) URL path to zip location.  If not specified,
               must provide content in the body of this call.
        :param str target_version: (optional) The semver value for this new
               version, if not found in the zip url package content.
        :param bool include_config: (optional) Add all possible configuration
               values to this version when importing.
        :param str repo_type: (optional) The type of repository containing this
               version.  Valid values are 'public_git' or 'enterprise_git'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Offering` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if offering_id is None:
            raise ValueError('offering_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='import_offering_version')
        headers.update(sdk_headers)

        params = {
            'zipurl': zipurl,
            'targetVersion': target_version,
            'includeConfig': include_config,
            'repoType': repo_type
        }

        data = {
            'tags': tags,
            'target_kinds': target_kinds,
            'content': content
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier', 'offering_id']
        path_param_values = self.encode_path_vars(catalog_identifier, offering_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings/{offering_id}/version'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def import_offering(self,
        catalog_identifier: str,
        *,
        tags: List[str] = None,
        target_kinds: List[str] = None,
        content: List[int] = None,
        zipurl: str = None,
        offering_id: str = None,
        target_version: str = None,
        include_config: bool = None,
        repo_type: str = None,
        x_auth_token: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Import a new offering from a tgz.

        Import a new offering from a tgz.

        :param str catalog_identifier: Catalog identifier.
        :param List[str] tags: (optional) Tags array.
        :param List[str] target_kinds: (optional) Target kinds.  Current valid
               values are 'iks', 'roks', 'vcenter', and 'terraform'.
        :param List[int] content: (optional) byte array representing the content to
               be imported.  Only supported for OVA images at this time.
        :param str zipurl: (optional) URL path to zip location.  If not specified,
               must provide content in this post body.
        :param str offering_id: (optional) Re-use the specified offeringID during
               import.
        :param str target_version: (optional) The semver value for this new
               version.
        :param bool include_config: (optional) Add all possible configuration items
               when creating this version.
        :param str repo_type: (optional) The type of repository containing this
               version.  Valid values are 'public_git' or 'enterprise_git'.
        :param str x_auth_token: (optional) Authentication token used to access the
               specified zip file.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Offering` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        headers = {
            'X-Auth-Token': x_auth_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='import_offering')
        headers.update(sdk_headers)

        params = {
            'zipurl': zipurl,
            'offeringID': offering_id,
            'targetVersion': target_version,
            'includeConfig': include_config,
            'repoType': repo_type
        }

        data = {
            'tags': tags,
            'target_kinds': target_kinds,
            'content': content
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/import/offerings'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def reload_offering(self,
        catalog_identifier: str,
        offering_id: str,
        target_version: str,
        *,
        tags: List[str] = None,
        target_kinds: List[str] = None,
        content: List[int] = None,
        zipurl: str = None,
        repo_type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Reload existing version in offering from a tgz.

        Reload existing version in offering from a tgz.

        :param str catalog_identifier: Catalog identifier.
        :param str offering_id: Offering identification.
        :param str target_version: The semver value for this new version.
        :param List[str] tags: (optional) Tags array.
        :param List[str] target_kinds: (optional) Target kinds.  Current valid
               values are 'iks', 'roks', 'vcenter', and 'terraform'.
        :param List[int] content: (optional) byte array representing the content to
               be imported.  Only supported for OVA images at this time.
        :param str zipurl: (optional) URL path to zip location.  If not specified,
               must provide content in this post body.
        :param str repo_type: (optional) The type of repository containing this
               version.  Valid values are 'public_git' or 'enterprise_git'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Offering` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if offering_id is None:
            raise ValueError('offering_id must be provided')
        if target_version is None:
            raise ValueError('target_version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='reload_offering')
        headers.update(sdk_headers)

        params = {
            'targetVersion': target_version,
            'zipurl': zipurl,
            'repoType': repo_type
        }

        data = {
            'tags': tags,
            'target_kinds': target_kinds,
            'content': content
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier', 'offering_id']
        path_param_values = self.encode_path_vars(catalog_identifier, offering_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings/{offering_id}/reload'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def get_offering(self,
        catalog_identifier: str,
        offering_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get an offering.

        Get an offering.

        :param str catalog_identifier: Catalog identifier.
        :param str offering_id: Offering identification.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Offering` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if offering_id is None:
            raise ValueError('offering_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_offering')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier', 'offering_id']
        path_param_values = self.encode_path_vars(catalog_identifier, offering_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings/{offering_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def replace_offering(self,
        catalog_identifier: str,
        offering_id: str,
        *,
        id: str = None,
        rev: str = None,
        url: str = None,
        crn: str = None,
        label: str = None,
        name: str = None,
        offering_icon_url: str = None,
        offering_docs_url: str = None,
        offering_support_url: str = None,
        tags: List[str] = None,
        rating: 'Rating' = None,
        created: datetime = None,
        updated: datetime = None,
        short_description: str = None,
        long_description: str = None,
        features: List['Feature'] = None,
        kinds: List['Kind'] = None,
        permit_request_ibm_public_publish: bool = None,
        ibm_publish_approved: bool = None,
        public_publish_approved: bool = None,
        public_original_crn: str = None,
        publish_public_crn: str = None,
        portal_approval_record: str = None,
        portal_ui_url: str = None,
        catalog_id: str = None,
        catalog_name: str = None,
        metadata: object = None,
        disclaimer: str = None,
        hidden: bool = None,
        provider: str = None,
        repo_info: 'RepoInfo' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update an offering.

        Update an offering.

        :param str catalog_identifier: Catalog identifier.
        :param str offering_id: Offering identification.
        :param str id: (optional) unique id.
        :param str rev: (optional) Cloudant revision.
        :param str url: (optional) The url for this specific offering.
        :param str crn: (optional) The crn for this specific offering.
        :param str label: (optional) Display Name in the requested language.
        :param str name: (optional) The programmatic name of this offering.
        :param str offering_icon_url: (optional) URL for an icon associated with
               this offering.
        :param str offering_docs_url: (optional) URL for an additional docs with
               this offering.
        :param str offering_support_url: (optional) URL to be displayed in the
               Consumption UI for getting support on this offering.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param Rating rating: (optional) Repository info for offerings.
        :param datetime created: (optional) The date and time this catalog was
               created.
        :param datetime updated: (optional) The date and time this catalog was last
               updated.
        :param str short_description: (optional) Short description in the requested
               language.
        :param str long_description: (optional) Long description in the requested
               language.
        :param List[Feature] features: (optional) list of features associated with
               this offering.
        :param List[Kind] kinds: (optional) Array of kind.
        :param bool permit_request_ibm_public_publish: (optional) Is it permitted
               to request publishing to IBM or Public.
        :param bool ibm_publish_approved: (optional) Indicates if this offering has
               been approved for use by all IBMers.
        :param bool public_publish_approved: (optional) Indicates if this offering
               has been approved for use by all IBM Cloud users.
        :param str public_original_crn: (optional) The original offering CRN that
               this publish entry came from.
        :param str publish_public_crn: (optional) The crn of the public catalog
               entry of this offering.
        :param str portal_approval_record: (optional) The portal's approval record
               ID.
        :param str portal_ui_url: (optional) The portal UI URL.
        :param str catalog_id: (optional) The id of the catalog containing this
               offering.
        :param str catalog_name: (optional) The name of the catalog.
        :param object metadata: (optional) Map of metadata values for this
               offering.
        :param str disclaimer: (optional) A disclaimer for this offering.
        :param bool hidden: (optional) Determine if this offering should be
               displayed in the Consumption UI.
        :param str provider: (optional) Provider of this offering.
        :param RepoInfo repo_info: (optional) Repository info for offerings.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Catalog` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if offering_id is None:
            raise ValueError('offering_id must be provided')
        if rating is not None:
            rating = convert_model(rating)
        if created is not None:
            created = datetime_to_string(created)
        if updated is not None:
            updated = datetime_to_string(updated)
        if features is not None:
            features = [convert_model(x) for x in features]
        if kinds is not None:
            kinds = [convert_model(x) for x in kinds]
        if repo_info is not None:
            repo_info = convert_model(repo_info)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='replace_offering')
        headers.update(sdk_headers)

        data = {
            'id': id,
            '_rev': rev,
            'url': url,
            'crn': crn,
            'label': label,
            'name': name,
            'offering_icon_url': offering_icon_url,
            'offering_docs_url': offering_docs_url,
            'offering_support_url': offering_support_url,
            'tags': tags,
            'rating': rating,
            'created': created,
            'updated': updated,
            'short_description': short_description,
            'long_description': long_description,
            'features': features,
            'kinds': kinds,
            'permit_request_ibm_public_publish': permit_request_ibm_public_publish,
            'ibm_publish_approved': ibm_publish_approved,
            'public_publish_approved': public_publish_approved,
            'public_original_crn': public_original_crn,
            'publish_public_crn': publish_public_crn,
            'portal_approval_record': portal_approval_record,
            'portal_ui_url': portal_ui_url,
            'catalog_id': catalog_id,
            'catalog_name': catalog_name,
            'metadata': metadata,
            'disclaimer': disclaimer,
            'hidden': hidden,
            'provider': provider,
            'repo_info': repo_info
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier', 'offering_id']
        path_param_values = self.encode_path_vars(catalog_identifier, offering_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings/{offering_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_offering(self,
        catalog_identifier: str,
        offering_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an offering.

        Delete an offering.

        :param str catalog_identifier: Catalog identifier.
        :param str offering_id: Offering identification.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if offering_id is None:
            raise ValueError('offering_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_offering')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['catalog_identifier', 'offering_id']
        path_param_values = self.encode_path_vars(catalog_identifier, offering_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings/{offering_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_offering_audit(self,
        catalog_identifier: str,
        offering_id: str,
        *,
        id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the audit log(s) for offering.

        Get the audit log(s) for offering.

        :param str catalog_identifier: Catalog identifier.
        :param str offering_id: Offering identifier.
        :param str id: (optional) Log identification.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if offering_id is None:
            raise ValueError('offering_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_offering_audit')
        headers.update(sdk_headers)

        params = {
            'id': id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['catalog_identifier', 'offering_id']
        path_param_values = self.encode_path_vars(catalog_identifier, offering_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings/{offering_id}/audit'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def replace_offering_icon(self,
        catalog_identifier: str,
        offering_id: str,
        file_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        upload an icon for the offering.

        upload an icon file to be stored in GC. File is uploaded as a binary payload - not
        as a form.

        :param str catalog_identifier: Catalog identifier.
        :param str offering_id: Offering identification.
        :param str file_name: Name of the file name that is being uploaded.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Offering` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if offering_id is None:
            raise ValueError('offering_id must be provided')
        if file_name is None:
            raise ValueError('file_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='replace_offering_icon')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier', 'offering_id', 'file_name']
        path_param_values = self.encode_path_vars(catalog_identifier, offering_id, file_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings/{offering_id}/icon/{file_name}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_offering_ibm(self,
        catalog_identifier: str,
        offering_id: str,
        approval_type: str,
        approved: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Approve offering to be permitted to publish or to request to be published to IBM Public Catalog (IBMers only or Everyone).

        Approve or disapprove the offering to be allowed to publish to the IBM Public
        Catalog. Options:
        * `allow_request` - (Allow requesting to publish to IBM)
        * `ibm` - (Allow publishing to be visible to IBM only)
        * `public` - (Allow publishing to be visible to everyone, including IBM)
        If disapprove `public`, then `ibm` approval will not  be changed. If disapprove
        `ibm` then `public` will automatically be disapproved. if disapprove
        `allow_request` then all rights to publish will be removed. This is because the
        process steps always go first through `allow` to `ibm` and then to `public`. `ibm`
        cannot be skipped. Only users with Approval IAM authority can use this. Approvers
        should use the catalog and offering id from the public catalog since they wouldn't
        have access to the private offering.'.

        :param str catalog_identifier: Catalog identifier.
        :param str offering_id: Offering identification.
        :param str approval_type: Type of approval, ibm or public.
        :param str approved: Approve (true) or disapprove (false).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApprovalResult` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if offering_id is None:
            raise ValueError('offering_id must be provided')
        if approval_type is None:
            raise ValueError('approval_type must be provided')
        if approved is None:
            raise ValueError('approved must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_offering_ibm')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier', 'offering_id', 'approval_type', 'approved']
        path_param_values = self.encode_path_vars(catalog_identifier, offering_id, approval_type, approved)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings/{offering_id}/publish/{approval_type}/{approved}'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Versions
    #########################


    def get_version_about(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the about information, in markdown, for the current version.

        Get the about information, in markdown, for the current version.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_version_about')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'text/markdown'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/about'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_version_license(self,
        version_loc_id: str,
        license_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the license content for the specified license ID in the specified version.

        Get the license content for the specified license ID in the specified version.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param str license_id: The ID of the license, which maps to the file name
               in the 'licenses' directory of this verions tgz file.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        if license_id is None:
            raise ValueError('license_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_version_license')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id', 'license_id']
        path_param_values = self.encode_path_vars(version_loc_id, license_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/licenses/{license_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_version_container_images(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get get the list of container images associated with this version.

        The "image_manifest_url" property of the version should be pointing the a URL for
        the image manifest, this api reflects that content.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageManifest` object
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_version_container_images')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/containerImages'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def deprecate_version(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deprecate the specified version.

        Deprecate the specified version.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='deprecate_version')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/deprecate'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def account_publish_version(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Publish the specified version so it is viewable by account members.

        Publish the specified version so it is viewable by account members.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='account_publish_version')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/account-publish'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def ibm_publish_version(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Publish the specified version so that it is visible to IBMers in the public catalog.

        Publish the specified version so that it is visible to IBMers in the public
        catalog.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='ibm_publish_version')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/ibm-publish'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def public_publish_version(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Publish the specified version so it is visible to all users in the public catalog.

        Publish the specified version so it is visible to all users in the public catalog.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='public_publish_version')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/public-publish'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def commit_version(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Commit a working copy of the specified version.

        Commit a working copy of the specified version.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='commit_version')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/commit'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def copy_version(self,
        version_loc_id: str,
        *,
        tags: List[str] = None,
        target_kinds: List[str] = None,
        content: List[int] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Copy the specified version to a new target kind within the same offering.

        Copy the specified version to a new target kind within the same offering.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param List[str] tags: (optional) Tags array.
        :param List[str] target_kinds: (optional) Target kinds.  Current valid
               values are 'iks', 'roks', 'vcenter', and 'terraform'.
        :param List[int] content: (optional) byte array representing the content to
               be imported.  Only supported for OVA images at this time.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='copy_version')
        headers.update(sdk_headers)

        data = {
            'tags': tags,
            'target_kinds': target_kinds,
            'content': content
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/copy'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_version_working_copy(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a working copy of the specified version.

        Create a working copy of the specified version.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Version` object
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_version_working_copy')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/workingcopy'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_version_updates(self,
        version_loc_id: str,
        *,
        cluster_id: str = None,
        region: str = None,
        resource_group_id: str = None,
        namespace: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get available updates for the specified version.

        Get available updates for the specified version.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param str cluster_id: (optional) The id of the cluster where this version
               was installed.
        :param str region: (optional) The region of the cluster where this version
               was installed.
        :param str resource_group_id: (optional) The resource group id of the
               cluster where this version was installed.
        :param str namespace: (optional) The namespace of the cluster where this
               version was installed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[VersionUpdateDescriptor]` result
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_version_updates')
        headers.update(sdk_headers)

        params = {
            'cluster_id': cluster_id,
            'region': region,
            'resource_group_id': resource_group_id,
            'namespace': namespace
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/updates'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_version(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the Offering/Kind/Version 'branch' for the specified locator ID.

        Get the Offering/Kind/Version 'branch' for the specified locator ID.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Offering` object
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_version')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_version(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a version.

        Delete a the specified version.  If the version is an active version with a
        working copy, the working copy will be deleted as well.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_version')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_versions(self,
        q: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Search for versions.

        [deprecated] use /search/license/versions api instead.   Search across all
        accounts for versions, requires global admin permission.

        :param str q: query, for now only \"q=entitlement_key:<some-key>\" is
               supported.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if q is None:
            raise ValueError('q must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_versions')
        headers.update(sdk_headers)

        params = {
            'q': q
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/versions'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Repo
    #########################


    def get_repos(self,
        type: str,
        repourl: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List a repo's entries.

        List the available entries from a given repo.

        :param str type: The type of repo (valid repo types: helm).
        :param str repourl: The URL for the repo's root (e.g
               https://kubernetes-charts-incubator.storage.googleapis.com).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HelmRepoList` object
        """

        if type is None:
            raise ValueError('type must be provided')
        if repourl is None:
            raise ValueError('repourl must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_repos')
        headers.update(sdk_headers)

        params = {
            'repourl': repourl
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['type']
        path_param_values = self.encode_path_vars(type)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/repo/{type}/entries'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_repo(self,
        type: str,
        charturl: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get contents of a repo.

        Get the contents of a given repo.

        :param str type: The type of repo (valid repo types: helm).
        :param str charturl: The URL for the repo's chart zip file (e.g
               https://registry.bluemix.net/helm/ibm-charts/charts/ibm-redis-ha-dev-1.0.0.tgz).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HelmPackage` object
        """

        if type is None:
            raise ValueError('type must be provided')
        if charturl is None:
            raise ValueError('charturl must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_repo')
        headers.update(sdk_headers)

        params = {
            'charturl': charturl
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['type']
        path_param_values = self.encode_path_vars(type)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/repo/{type}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Deploy
    #########################


    def list_clusters(self,
        *,
        limit: int = None,
        offset: int = None,
        type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List Kube clusters.

        List Kube clusters.

        :param int limit: (optional) number or results to return.
        :param int offset: (optional) number of results to skip before returning
               values.
        :param str type: (optional) Kubernetes or OpenShift.  Default is
               kubernetes.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClusterSearchResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_clusters')
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'offset': offset,
            'type': type
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/deploy/kubernetes/clusters'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_cluster(self,
        cluster_id: str,
        region: str,
        x_auth_refresh_token: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get Kube cluster.

        Get Kube cluster.

        :param str cluster_id: ID of the cluster.
        :param str region: Region of the cluster.
        :param str x_auth_refresh_token: IAM Refresh token.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClusterInfo` object
        """

        if cluster_id is None:
            raise ValueError('cluster_id must be provided')
        if region is None:
            raise ValueError('region must be provided')
        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_cluster')
        headers.update(sdk_headers)

        params = {
            'region': region
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['cluster_id']
        path_param_values = self.encode_path_vars(cluster_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deploy/kubernetes/clusters/{cluster_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_namespaces(self,
        cluster_id: str,
        region: str,
        x_auth_refresh_token: str,
        *,
        limit: int = None,
        offset: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get cluster namespaces.

        Get cluster namespaces.

        :param str cluster_id: ID of the cluster.
        :param str region: Cluster region.
        :param str x_auth_refresh_token: IAM Refresh token.
        :param int limit: (optional) number or results to return.
        :param int offset: (optional) number of results to skip before returning
               values.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `NamespaceSearchResult` object
        """

        if cluster_id is None:
            raise ValueError('cluster_id must be provided')
        if region is None:
            raise ValueError('region must be provided')
        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_namespaces')
        headers.update(sdk_headers)

        params = {
            'region': region,
            'limit': limit,
            'offset': offset
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['cluster_id']
        path_param_values = self.encode_path_vars(cluster_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deploy/kubernetes/clusters/{cluster_id}/namespaces'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_operator(self,
        x_auth_refresh_token: str,
        *,
        cluster_id: str = None,
        region: str = None,
        namespaces: List[str] = None,
        all_namespaces: bool = None,
        version_locator_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Deploy Operator(s) on a Kube cluster.

        Deploy Operator(s) on a Kube cluster.

        :param str x_auth_refresh_token: IAM Refresh token.
        :param str cluster_id: (optional) Cluster ID.
        :param str region: (optional) Cluster region.
        :param List[str] namespaces: (optional) Kube namespaces to deploy
               Operator(s) to.
        :param bool all_namespaces: (optional) Denotes whether to install
               Operator(s) globally.
        :param str version_locator_id: (optional) A dotted value of
               `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[OperatorDeployResult]` result
        """

        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_operator')
        headers.update(sdk_headers)

        data = {
            'cluster_id': cluster_id,
            'region': region,
            'namespaces': namespaces,
            'all_namespaces': all_namespaces,
            'version_locator_id': version_locator_id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/deploy/kubernetes/olm/operator'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_operators(self,
        x_auth_refresh_token: str,
        cluster_id: str,
        region: str,
        version_locator_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get Operator(s) from a Kube cluster.

        Get Operator(s) from a Kube cluster.

        :param str x_auth_refresh_token: IAM Refresh token.
        :param str cluster_id: Cluster identification.
        :param str region: Cluster region.
        :param str version_locator_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[OperatorDeployResult]` result
        """

        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        if cluster_id is None:
            raise ValueError('cluster_id must be provided')
        if region is None:
            raise ValueError('region must be provided')
        if version_locator_id is None:
            raise ValueError('version_locator_id must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_operators')
        headers.update(sdk_headers)

        params = {
            'cluster_id': cluster_id,
            'region': region,
            'version_locator_id': version_locator_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/deploy/kubernetes/olm/operator'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def replace_operator(self,
        x_auth_refresh_token: str,
        *,
        cluster_id: str = None,
        region: str = None,
        namespaces: List[str] = None,
        all_namespaces: bool = None,
        version_locator_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update Operator(s) on a Kube cluster.

        Update Operator(s) on a Kube cluster.

        :param str x_auth_refresh_token: IAM Refresh token.
        :param str cluster_id: (optional) Cluster ID.
        :param str region: (optional) Cluster region.
        :param List[str] namespaces: (optional) Kube namespaces to deploy
               Operator(s) to.
        :param bool all_namespaces: (optional) Denotes whether to install
               Operator(s) globally.
        :param str version_locator_id: (optional) A dotted value of
               `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[OperatorDeployResult]` result
        """

        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='replace_operator')
        headers.update(sdk_headers)

        data = {
            'cluster_id': cluster_id,
            'region': region,
            'namespaces': namespaces,
            'all_namespaces': all_namespaces,
            'version_locator_id': version_locator_id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/deploy/kubernetes/olm/operator'
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_operator(self,
        x_auth_refresh_token: str,
        cluster_id: str,
        region: str,
        version_locator_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete Operator(s) from a Kube cluster.

        Delete Operator(s) from a Kube cluster.

        :param str x_auth_refresh_token: IAM Refresh token.
        :param str cluster_id: Cluster identification.
        :param str region: Cluster region.
        :param str version_locator_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        if cluster_id is None:
            raise ValueError('cluster_id must be provided')
        if region is None:
            raise ValueError('region must be provided')
        if version_locator_id is None:
            raise ValueError('version_locator_id must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_operator')
        headers.update(sdk_headers)

        params = {
            'cluster_id': cluster_id,
            'region': region,
            'version_locator_id': version_locator_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/deploy/kubernetes/olm/operator'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def install_version(self,
        version_loc_id: str,
        x_auth_refresh_token: str,
        *,
        cluster_id: str = None,
        region: str = None,
        namespace: str = None,
        override_values: object = None,
        entitlement_apikey: str = None,
        schematics: 'DeployRequestBodySchematics' = None,
        script: str = None,
        script_id: str = None,
        version_locator_id: str = None,
        vcenter_id: str = None,
        vcenter_user: str = None,
        vcenter_password: str = None,
        vcenter_location: str = None,
        vcenter_datastore: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create an install.

        Create an install.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param str x_auth_refresh_token: IAM Refresh token.
        :param str cluster_id: (optional) Cluster ID.
        :param str region: (optional) Cluster region.
        :param str namespace: (optional) Kube namespace.
        :param object override_values: (optional) Object containing Helm chart
               override values.
        :param str entitlement_apikey: (optional) Entitlement API Key for this
               offering.
        :param DeployRequestBodySchematics schematics: (optional) Schematics
               workspace configuration.
        :param str script: (optional) Script.
        :param str script_id: (optional) Script ID.
        :param str version_locator_id: (optional) A dotted value of
               `catalogID`.`versionID`.
        :param str vcenter_id: (optional) VCenter ID.
        :param str vcenter_user: (optional) VCenter User.
        :param str vcenter_password: (optional) VCenter Password.
        :param str vcenter_location: (optional) VCenter Location.
        :param str vcenter_datastore: (optional) VCenter Datastore.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        if schematics is not None:
            schematics = convert_model(schematics)
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='install_version')
        headers.update(sdk_headers)

        data = {
            'cluster_id': cluster_id,
            'region': region,
            'namespace': namespace,
            'override_values': override_values,
            'entitlement_apikey': entitlement_apikey,
            'schematics': schematics,
            'script': script,
            'script_id': script_id,
            'version_locator_id': version_locator_id,
            'vcenter_id': vcenter_id,
            'vcenter_user': vcenter_user,
            'vcenter_password': vcenter_password,
            'vcenter_location': vcenter_location,
            'vcenter_datastore': vcenter_datastore
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/install'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def preinstall_version(self,
        version_loc_id: str,
        x_auth_refresh_token: str,
        *,
        cluster_id: str = None,
        region: str = None,
        namespace: str = None,
        override_values: object = None,
        entitlement_apikey: str = None,
        schematics: 'DeployRequestBodySchematics' = None,
        script: str = None,
        script_id: str = None,
        version_locator_id: str = None,
        vcenter_id: str = None,
        vcenter_user: str = None,
        vcenter_password: str = None,
        vcenter_location: str = None,
        vcenter_datastore: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a preinstall.

        Create a preinstall.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param str x_auth_refresh_token: IAM Refresh token.
        :param str cluster_id: (optional) Cluster ID.
        :param str region: (optional) Cluster region.
        :param str namespace: (optional) Kube namespace.
        :param object override_values: (optional) Object containing Helm chart
               override values.
        :param str entitlement_apikey: (optional) Entitlement API Key for this
               offering.
        :param DeployRequestBodySchematics schematics: (optional) Schematics
               workspace configuration.
        :param str script: (optional) Script.
        :param str script_id: (optional) Script ID.
        :param str version_locator_id: (optional) A dotted value of
               `catalogID`.`versionID`.
        :param str vcenter_id: (optional) VCenter ID.
        :param str vcenter_user: (optional) VCenter User.
        :param str vcenter_password: (optional) VCenter Password.
        :param str vcenter_location: (optional) VCenter Location.
        :param str vcenter_datastore: (optional) VCenter Datastore.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        if schematics is not None:
            schematics = convert_model(schematics)
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='preinstall_version')
        headers.update(sdk_headers)

        data = {
            'cluster_id': cluster_id,
            'region': region,
            'namespace': namespace,
            'override_values': override_values,
            'entitlement_apikey': entitlement_apikey,
            'schematics': schematics,
            'script': script,
            'script_id': script_id,
            'version_locator_id': version_locator_id,
            'vcenter_id': vcenter_id,
            'vcenter_user': vcenter_user,
            'vcenter_password': vcenter_password,
            'vcenter_location': vcenter_location,
            'vcenter_datastore': vcenter_datastore
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/preinstall'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_preinstall(self,
        version_loc_id: str,
        x_auth_refresh_token: str,
        *,
        cluster_id: str = None,
        region: str = None,
        namespace: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a preinstall.

        Get a preinstall.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param str x_auth_refresh_token: IAM Refresh token.
        :param str cluster_id: (optional) ID of the cluster.
        :param str region: (optional) Cluster region.
        :param str namespace: (optional) Required if the version's pre-install
               scope is `namespace`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InstallStatus` object
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_preinstall')
        headers.update(sdk_headers)

        params = {
            'cluster_id': cluster_id,
            'region': region,
            'namespace': namespace
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/preinstall'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def validation_install(self,
        version_loc_id: str,
        x_auth_refresh_token: str,
        *,
        cluster_id: str = None,
        region: str = None,
        namespace: str = None,
        override_values: object = None,
        entitlement_apikey: str = None,
        schematics: 'DeployRequestBodySchematics' = None,
        script: str = None,
        script_id: str = None,
        version_locator_id: str = None,
        vcenter_id: str = None,
        vcenter_user: str = None,
        vcenter_password: str = None,
        vcenter_location: str = None,
        vcenter_datastore: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Validate a offering.

        Validate a offering.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param str x_auth_refresh_token: IAM Refresh token.
        :param str cluster_id: (optional) Cluster ID.
        :param str region: (optional) Cluster region.
        :param str namespace: (optional) Kube namespace.
        :param object override_values: (optional) Object containing Helm chart
               override values.
        :param str entitlement_apikey: (optional) Entitlement API Key for this
               offering.
        :param DeployRequestBodySchematics schematics: (optional) Schematics
               workspace configuration.
        :param str script: (optional) Script.
        :param str script_id: (optional) Script ID.
        :param str version_locator_id: (optional) A dotted value of
               `catalogID`.`versionID`.
        :param str vcenter_id: (optional) VCenter ID.
        :param str vcenter_user: (optional) VCenter User.
        :param str vcenter_password: (optional) VCenter Password.
        :param str vcenter_location: (optional) VCenter Location.
        :param str vcenter_datastore: (optional) VCenter Datastore.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        if schematics is not None:
            schematics = convert_model(schematics)
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='validation_install')
        headers.update(sdk_headers)

        data = {
            'cluster_id': cluster_id,
            'region': region,
            'namespace': namespace,
            'override_values': override_values,
            'entitlement_apikey': entitlement_apikey,
            'schematics': schematics,
            'script': script,
            'script_id': script_id,
            'version_locator_id': version_locator_id,
            'vcenter_id': vcenter_id,
            'vcenter_user': vcenter_user,
            'vcenter_password': vcenter_password,
            'vcenter_location': vcenter_location,
            'vcenter_datastore': vcenter_datastore
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/validation/install'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_validation_status(self,
        version_loc_id: str,
        x_auth_refresh_token: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Returns the install status for the specified offering version.

        Returns the install status for the specified offering version.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param str x_auth_refresh_token: IAM Refresh token.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Validation` object
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_validation_status')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/validation/install'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_override_values(self,
        version_loc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Returns the override values that were used to validate the specified offering version.

        Returns the override values that were used to validate the specified offering
        version.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_override_values')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/validation/overridevalues'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_schematics_workspaces(self,
        version_loc_id: str,
        x_auth_refresh_token: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Returns the schematics workspaces for the specified offering version.

        Returns the schematics workspaces for the specified offering version.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param str x_auth_refresh_token: IAM Refresh token.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchematicsWorkspaceSearchResult` object
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        if x_auth_refresh_token is None:
            raise ValueError('x_auth_refresh_token must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_schematics_workspaces')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/workspaces'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def can_deploy_schematics(self,
        version_loc_id: str,
        cluster_id: str,
        region: str,
        *,
        namespace: str = None,
        resource_group_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Returns the schematics permissions for the specified user.

        Returns the schematics permissions for the specified user.

        :param str version_loc_id: A dotted value of `catalogID`.`versionID`.
        :param str cluster_id: ID of the cluster.
        :param str region: Cluster region.
        :param str namespace: (optional) Required if the version's pre-install
               scope is `namespace`.
        :param str resource_group_id: (optional) Resource group identification.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeployRequirementsCheck` object
        """

        if version_loc_id is None:
            raise ValueError('version_loc_id must be provided')
        if cluster_id is None:
            raise ValueError('cluster_id must be provided')
        if region is None:
            raise ValueError('region must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='can_deploy_schematics')
        headers.update(sdk_headers)

        params = {
            'cluster_id': cluster_id,
            'region': region,
            'namespace': namespace,
            'resource_group_id': resource_group_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['version_loc_id']
        path_param_values = self.encode_path_vars(version_loc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/versions/{version_loc_id}/candeploy'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_resource_groups(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Returns all active resource groups in the current account, where the current user has permission to create schematics workspaces.

        Returns all active resource groups in the current account, where the current user
        has permission to create schematics workspaces.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceGroups` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_resource_groups')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/deploy/schematics/resourcegroups'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Licensing
    #########################


    def get_license_providers(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get license providers.

        Get license providers.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LicenseProviders` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_license_providers')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/license/license_providers'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_license_entitlements(self,
        *,
        account_id: str = None,
        license_product_id: str = None,
        version_id: str = None,
        state: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get license entitlements.

        Get license entitlements bound to an account.

        :param str account_id: (optional) The account ID to query for the
               entitlement. Default is the account from the user's token.
        :param str license_product_id: (optional) The license product ID. If from
               PPA (Passport Advantage) this is the product Part number(s) which can be
               one or more IDs, eg. D1YGZLL,5737L09.
        :param str version_id: (optional) The GC ID of the specific offering
               version.
        :param str state: (optional) The state of the license entitlement. eg.
               usually 'active', or if it's been deleted will show as 'removed'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LicenseEntitlements` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_license_entitlements')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'license_product_id': license_product_id,
            'version_id': version_id,
            'state': state
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/license/entitlements'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_license_entitlement(self,
        *,
        name: str = None,
        effective_from: str = None,
        effective_until: str = None,
        version_id: str = None,
        license_id: str = None,
        license_owner_id: str = None,
        license_provider_id: str = None,
        license_product_id: str = None,
        account_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a license entitlement.

        Create an entitlement for a Cloud account.  This is used to give an account an
        entitlement to a license.

        :param str name: (optional) Entitlement name.
        :param str effective_from: (optional) Entitlement is good from this
               starting date. eg. '2019-07-17T21:21:47.6794935Z'.
        :param str effective_until: (optional) Entitlement is good until this
               ending date. eg. '2019-07-17T21:21:47.6794935Z'.
        :param str version_id: (optional) Global Catalog ID of the version.
        :param str license_id: (optional) Specific license entitlement ID from the
               license provider, eg. D1W3R4.
        :param str license_owner_id: (optional) IBM ID of the owner of this license
               entitlement.
        :param str license_provider_id: (optional) License provider ID.
        :param str license_product_id: (optional) License product ID.
        :param str account_id: (optional) if not specified the token's account will
               be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LicenseEntitlement` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_license_entitlement')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id
        }

        data = {
            'name': name,
            'effective_from': effective_from,
            'effective_until': effective_until,
            'version_id': version_id,
            'license_id': license_id,
            'license_owner_id': license_owner_id,
            'license_provider_id': license_provider_id,
            'license_product_id': license_product_id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/license/entitlements'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def get_license_entitlements(self,
        license_product_id: str,
        *,
        account_id: str = None,
        version_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get entitlements for a specific license product ID.

        Get an entitlements for a specific license product ID bound to an account.

        :param str license_product_id: The license product ID. If from PPA
               (Passport Advantage) this is a specific product Part number, eg. D1YGZLL.
        :param str account_id: (optional) The account ID to query for the
               entitlement. Default is the account from the user's token.
        :param str version_id: (optional) The GC ID of the specific offering
               version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LicenseEntitlements` object
        """

        if license_product_id is None:
            raise ValueError('license_product_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_license_entitlements')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'version_id': version_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['license_product_id']
        path_param_values = self.encode_path_vars(license_product_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/license/entitlements/productID/{license_product_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def delete_license_entitlement(self,
        entitlement_id: str,
        *,
        account_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete license entitlement.

        Delete a license entitlement that is bound to an account. Note that BSS will mark
        the entitlement field "state": "removed".

        :param str entitlement_id: The specific entitlement ID (can be obtained
               from one of the license entitlement queries).
        :param str account_id: (optional) The account ID to query for the
               entitlement. Default is the account from the user's token.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if entitlement_id is None:
            raise ValueError('entitlement_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_license_entitlement')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['entitlement_id']
        path_param_values = self.encode_path_vars(entitlement_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/license/entitlements/{entitlement_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_licenses(self,
        license_provider_id: str,
        *,
        account_id: str = None,
        name: str = None,
        license_type: str = None,
        license_product_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get licenses.

        Retrieve available licenses from supported license subsystems.  This is used to
        get the list of available licenses that the user has.

        :param str license_provider_id: ID of the license provider, ie. retrieved
               from GET license_providers.
        :param str account_id: (optional) If not specified the token's account will
               be used.
        :param str name: (optional) License name.
        :param str license_type: (optional) Type of license, if not specified,
               default is ibm-ppa.
        :param str license_product_id: (optional) The license product ID. If from
               PPA (Passport Advantage) this is the product Part number, eg. D1YGZLL.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Licenses` object
        """

        if license_provider_id is None:
            raise ValueError('license_provider_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_licenses')
        headers.update(sdk_headers)

        params = {
            'license_provider_id': license_provider_id,
            'account_id': account_id,
            'name': name,
            'license_type': license_type,
            'license_product_id': license_product_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/license/licenses'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Cross Account Search
    #########################


    def search_license_versions(self,
        q: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Search for versions.

        Search across accounts for all versions usig a particular license, requires global
        admin permission.

        :param str q: query, for now only \"q=entitlement_key:<some-key>\" is
               supported.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if q is None:
            raise ValueError('q must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='search_license_versions')
        headers.update(sdk_headers)

        params = {
            'q': q
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/search/license/versions'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def search_license_offerings(self,
        q: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Search for Offerings.

        Search across accounts for all offerings using a particular license, requires
        global admin permission.

        :param str q: query, for now only \"q=entitlement_key:<some-key>\" is
               supported.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if q is None:
            raise ValueError('q must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='search_license_offerings')
        headers.update(sdk_headers)

        params = {
            'q': q
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/search/license/offerings'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # objects
    #########################


    def search_objects(self,
        query: str,
        *,
        limit: int = None,
        offset: int = None,
        collapse: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Search for objects across catalogs.

        List the available objects from both public and private. These copies cannot be
        used for updating. They are not complete and only return what is visible to the
        caller.

        :param str query: Lucene query string.
        :param int limit: (optional) number or results to return.
        :param int offset: (optional) number of results to skip before returning
               values.
        :param bool collapse: (optional) when true, hide private objects that
               correspond to public or IBM published objects.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ObjectSearchResult` object
        """

        if query is None:
            raise ValueError('query must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='search_objects')
        headers.update(sdk_headers)

        params = {
            'query': query,
            'limit': limit,
            'offset': offset,
            'collapse': collapse
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/objects'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def list_objects(self,
        catalog_identifier: str,
        *,
        limit: int = None,
        offset: int = None,
        name: str = None,
        sort: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get list of objects.

        List the available objects in the specified catalog.

        :param str catalog_identifier: Catalog identifier.
        :param int limit: (optional) number or results to return.
        :param int offset: (optional) number of results to skip before returning
               values.
        :param str name: (optional) only return results that contain the specified
               string.
        :param str sort: (optional) The field on which the output is sorted. Sorts
               by default by **label** property. Available fields are **name**, **label**,
               **created**, and **updated**. By adding **-** (i.e. **-label**) in front of
               the query string, you can specify descending order. Default is ascending
               order.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ObjectListResult` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_objects')
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'offset': offset,
            'name': name,
            'sort': sort
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/objects'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_object(self,
        catalog_identifier: str,
        *,
        id: str = None,
        name: str = None,
        rev: str = None,
        crn: str = None,
        url: str = None,
        parent_id: str = None,
        allow_list: List[str] = None,
        label_i18n: str = None,
        label: str = None,
        tags: List[str] = None,
        created: datetime = None,
        updated: datetime = None,
        short_description: str = None,
        short_description_i18n: str = None,
        kind: str = None,
        publish: 'PublishObject' = None,
        state: 'State' = None,
        catalog_id: str = None,
        catalog_name: str = None,
        data: object = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create an object.

        Create an object.

        :param str catalog_identifier: Catalog identifier.
        :param str id: (optional) unique id.
        :param str name: (optional) The programmatic name of this offering.
        :param str rev: (optional) Cloudant revision.
        :param str crn: (optional) The crn for this specific object.
        :param str url: (optional) The url for this specific object.
        :param str parent_id: (optional) The parent for this specific object.
        :param List[str] allow_list: (optional) List of allowed accounts for this
               specific object.
        :param str label_i18n: (optional) Translated display name in the requested
               language.
        :param str label: (optional) Display name in the requested language.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param datetime created: (optional) The date and time this catalog was
               created.
        :param datetime updated: (optional) The date and time this catalog was last
               updated.
        :param str short_description: (optional) Short description in the requested
               language.
        :param str short_description_i18n: (optional) Short description
               translation.
        :param str kind: (optional) Kind of object.
        :param PublishObject publish: (optional) Publish information.
        :param State state: (optional) Offering state.
        :param str catalog_id: (optional) The id of the catalog containing this
               offering.
        :param str catalog_name: (optional) The name of the catalog.
        :param object data: (optional) Map of data values for this object.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Object` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if created is not None:
            created = datetime_to_string(created)
        if updated is not None:
            updated = datetime_to_string(updated)
        if publish is not None:
            publish = convert_model(publish)
        if state is not None:
            state = convert_model(state)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_object')
        headers.update(sdk_headers)

        data = {
            'id': id,
            'name': name,
            '_rev': rev,
            'crn': crn,
            'url': url,
            'parent_id': parent_id,
            'allow_list': allow_list,
            'label_i18n': label_i18n,
            'label': label,
            'tags': tags,
            'created': created,
            'updated': updated,
            'short_description': short_description,
            'short_description_i18n': short_description_i18n,
            'kind': kind,
            'publish': publish,
            'state': state,
            'catalog_id': catalog_id,
            'catalog_name': catalog_name,
            'data': data
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/objects'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_object(self,
        catalog_identifier: str,
        object_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get an object.

        Get an object.

        :param str catalog_identifier: Catalog identifier.
        :param str object_identifier: Object identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Object` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if object_identifier is None:
            raise ValueError('object_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_object')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier', 'object_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier, object_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/objects/{object_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def replace_object(self,
        catalog_identifier: str,
        object_identifier: str,
        *,
        id: str = None,
        name: str = None,
        rev: str = None,
        crn: str = None,
        url: str = None,
        parent_id: str = None,
        allow_list: List[str] = None,
        label_i18n: str = None,
        label: str = None,
        tags: List[str] = None,
        created: datetime = None,
        updated: datetime = None,
        short_description: str = None,
        short_description_i18n: str = None,
        kind: str = None,
        publish: 'PublishObject' = None,
        state: 'State' = None,
        catalog_id: str = None,
        catalog_name: str = None,
        data: object = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update an object.

        Update an object.

        :param str catalog_identifier: Catalog identifier.
        :param str object_identifier: Object identifier.
        :param str id: (optional) unique id.
        :param str name: (optional) The programmatic name of this offering.
        :param str rev: (optional) Cloudant revision.
        :param str crn: (optional) The crn for this specific object.
        :param str url: (optional) The url for this specific object.
        :param str parent_id: (optional) The parent for this specific object.
        :param List[str] allow_list: (optional) List of allowed accounts for this
               specific object.
        :param str label_i18n: (optional) Translated display name in the requested
               language.
        :param str label: (optional) Display name in the requested language.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param datetime created: (optional) The date and time this catalog was
               created.
        :param datetime updated: (optional) The date and time this catalog was last
               updated.
        :param str short_description: (optional) Short description in the requested
               language.
        :param str short_description_i18n: (optional) Short description
               translation.
        :param str kind: (optional) Kind of object.
        :param PublishObject publish: (optional) Publish information.
        :param State state: (optional) Offering state.
        :param str catalog_id: (optional) The id of the catalog containing this
               offering.
        :param str catalog_name: (optional) The name of the catalog.
        :param object data: (optional) Map of data values for this object.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Object` object
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if object_identifier is None:
            raise ValueError('object_identifier must be provided')
        if created is not None:
            created = datetime_to_string(created)
        if updated is not None:
            updated = datetime_to_string(updated)
        if publish is not None:
            publish = convert_model(publish)
        if state is not None:
            state = convert_model(state)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='replace_object')
        headers.update(sdk_headers)

        data = {
            'id': id,
            'name': name,
            '_rev': rev,
            'crn': crn,
            'url': url,
            'parent_id': parent_id,
            'allow_list': allow_list,
            'label_i18n': label_i18n,
            'label': label,
            'tags': tags,
            'created': created,
            'updated': updated,
            'short_description': short_description,
            'short_description_i18n': short_description_i18n,
            'kind': kind,
            'publish': publish,
            'state': state,
            'catalog_id': catalog_id,
            'catalog_name': catalog_name,
            'data': data
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['catalog_identifier', 'object_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier, object_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/objects/{object_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_object(self,
        catalog_identifier: str,
        object_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an object.

        Delete an object.

        :param str catalog_identifier: Catalog identifier.
        :param str object_identifier: Object identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if object_identifier is None:
            raise ValueError('object_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_object')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['catalog_identifier', 'object_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier, object_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/objects/{object_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_object_audit(self,
        catalog_identifier: str,
        object_identifier: str,
        *,
        id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the audit log(s) for object.

        Get the audit log(s) for object.

        :param str catalog_identifier: Catalog identifier.
        :param str object_identifier: Object identifier.
        :param str id: (optional) Log identification.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if catalog_identifier is None:
            raise ValueError('catalog_identifier must be provided')
        if object_identifier is None:
            raise ValueError('object_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_object_audit')
        headers.update(sdk_headers)

        params = {
            'id': id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['catalog_identifier', 'object_identifier']
        path_param_values = self.encode_path_vars(catalog_identifier, object_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/catalogs/{catalog_identifier}/offerings/{object_identifier}/audit'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


class GetConsumptionOfferingsEnums:
    """
    Enums for get_consumption_offerings parameters.
    """

    class Select(str, Enum):
        """
        What should be selected. Default is 'all' which will return both public and
        private offerings. 'public' returns only the public offerings and 'private'
        returns only the private offerings.
        """
        ALL = 'all'
        PUBLIC = 'public'
        PRIVATE = 'private'


class UpdateOfferingIbmEnums:
    """
    Enums for update_offering_ibm parameters.
    """

    class ApprovalType(str, Enum):
        """
        Type of approval, ibm or public.
        """
        ALLOW_REQUEST = 'allow_request'
        IBM = 'ibm'
        PUBLIC = 'public'
    class Approved(str, Enum):
        """
        Approve (true) or disapprove (false).
        """
        TRUE = 'true'
        FALSE = 'false'


##############################################################################
# Models
##############################################################################


class Account():
    """
    Account information.

    :attr str id: (optional) Account identification.
    :attr Filters account_filters: (optional) Filters for account and catalog
          filters.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 account_filters: 'Filters' = None) -> None:
        """
        Initialize a Account object.

        :param str id: (optional) Account identification.
        :param Filters account_filters: (optional) Filters for account and catalog
               filters.
        """
        self.id = id
        self.account_filters = account_filters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Account':
        """Initialize a Account object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'account_filters' in _dict:
            args['account_filters'] = Filters.from_dict(_dict.get('account_filters'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Account object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_filters') and self.account_filters is not None:
            _dict['account_filters'] = self.account_filters.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Account object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Account') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Account') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AccountGroup():
    """
    Filters for an Account Group.

    :attr str id: (optional) Account group identification.
    :attr Filters account_filters: (optional) Filters for account and catalog
          filters.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 account_filters: 'Filters' = None) -> None:
        """
        Initialize a AccountGroup object.

        :param str id: (optional) Account group identification.
        :param Filters account_filters: (optional) Filters for account and catalog
               filters.
        """
        self.id = id
        self.account_filters = account_filters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountGroup':
        """Initialize a AccountGroup object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'account_filters' in _dict:
            args['account_filters'] = Filters.from_dict(_dict.get('account_filters'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_filters') and self.account_filters is not None:
            _dict['account_filters'] = self.account_filters.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AccumulatedFilters():
    """
    The accumulated filters for an account. This will return the account filters plus a
    filter for each catalog the user has access to.

    :attr List[Filters] account_filters: (optional) Filters for accounts (at this
          time this will always be just one item array).
    :attr List[AccumulatedFiltersCatalogFiltersItem] catalog_filters: (optional) The
          filters for all of the accessible catalogs.
    """

    def __init__(self,
                 *,
                 account_filters: List['Filters'] = None,
                 catalog_filters: List['AccumulatedFiltersCatalogFiltersItem'] = None) -> None:
        """
        Initialize a AccumulatedFilters object.

        :param List[Filters] account_filters: (optional) Filters for accounts (at
               this time this will always be just one item array).
        :param List[AccumulatedFiltersCatalogFiltersItem] catalog_filters:
               (optional) The filters for all of the accessible catalogs.
        """
        self.account_filters = account_filters
        self.catalog_filters = catalog_filters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccumulatedFilters':
        """Initialize a AccumulatedFilters object from a json dictionary."""
        args = {}
        if 'account_filters' in _dict:
            args['account_filters'] = [Filters.from_dict(x) for x in _dict.get('account_filters')]
        if 'catalog_filters' in _dict:
            args['catalog_filters'] = [AccumulatedFiltersCatalogFiltersItem.from_dict(x) for x in _dict.get('catalog_filters')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccumulatedFilters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_filters') and self.account_filters is not None:
            _dict['account_filters'] = [x.to_dict() for x in self.account_filters]
        if hasattr(self, 'catalog_filters') and self.catalog_filters is not None:
            _dict['catalog_filters'] = [x.to_dict() for x in self.catalog_filters]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccumulatedFilters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccumulatedFilters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccumulatedFilters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AccumulatedFiltersCatalogFiltersItem():
    """
    AccumulatedFiltersCatalogFiltersItem.

    :attr AccumulatedFiltersCatalogFiltersItemCatalog catalog: (optional) Filters
          for catalog.
    :attr Filters filters: (optional) Filters for account and catalog filters.
    """

    def __init__(self,
                 *,
                 catalog: 'AccumulatedFiltersCatalogFiltersItemCatalog' = None,
                 filters: 'Filters' = None) -> None:
        """
        Initialize a AccumulatedFiltersCatalogFiltersItem object.

        :param AccumulatedFiltersCatalogFiltersItemCatalog catalog: (optional)
               Filters for catalog.
        :param Filters filters: (optional) Filters for account and catalog filters.
        """
        self.catalog = catalog
        self.filters = filters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccumulatedFiltersCatalogFiltersItem':
        """Initialize a AccumulatedFiltersCatalogFiltersItem object from a json dictionary."""
        args = {}
        if 'catalog' in _dict:
            args['catalog'] = AccumulatedFiltersCatalogFiltersItemCatalog.from_dict(_dict.get('catalog'))
        if 'filters' in _dict:
            args['filters'] = Filters.from_dict(_dict.get('filters'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccumulatedFiltersCatalogFiltersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'catalog') and self.catalog is not None:
            _dict['catalog'] = self.catalog.to_dict()
        if hasattr(self, 'filters') and self.filters is not None:
            _dict['filters'] = self.filters.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccumulatedFiltersCatalogFiltersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccumulatedFiltersCatalogFiltersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccumulatedFiltersCatalogFiltersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AccumulatedFiltersCatalogFiltersItemCatalog():
    """
    Filters for catalog.

    :attr str id: (optional) The ID of the catalog.
    :attr str name: (optional) The name of the catalog.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None) -> None:
        """
        Initialize a AccumulatedFiltersCatalogFiltersItemCatalog object.

        :param str id: (optional) The ID of the catalog.
        :param str name: (optional) The name of the catalog.
        """
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccumulatedFiltersCatalogFiltersItemCatalog':
        """Initialize a AccumulatedFiltersCatalogFiltersItemCatalog object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccumulatedFiltersCatalogFiltersItemCatalog object from a json dictionary."""
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
        """Return a `str` version of this AccumulatedFiltersCatalogFiltersItemCatalog object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccumulatedFiltersCatalogFiltersItemCatalog') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccumulatedFiltersCatalogFiltersItemCatalog') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApprovalResult():
    """
    Result of approval.

    :attr bool allow_request: (optional) Allowed to request to publish.
    :attr bool ibm: (optional) Visible to IBM.
    :attr bool public: (optional) Visible to everyone.
    :attr bool changed: (optional) Denotes whether approval has changed.
    """

    def __init__(self,
                 *,
                 allow_request: bool = None,
                 ibm: bool = None,
                 public: bool = None,
                 changed: bool = None) -> None:
        """
        Initialize a ApprovalResult object.

        :param bool allow_request: (optional) Allowed to request to publish.
        :param bool ibm: (optional) Visible to IBM.
        :param bool public: (optional) Visible to everyone.
        :param bool changed: (optional) Denotes whether approval has changed.
        """
        self.allow_request = allow_request
        self.ibm = ibm
        self.public = public
        self.changed = changed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApprovalResult':
        """Initialize a ApprovalResult object from a json dictionary."""
        args = {}
        if 'allow_request' in _dict:
            args['allow_request'] = _dict.get('allow_request')
        if 'ibm' in _dict:
            args['ibm'] = _dict.get('ibm')
        if 'public' in _dict:
            args['public'] = _dict.get('public')
        if 'changed' in _dict:
            args['changed'] = _dict.get('changed')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApprovalResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allow_request') and self.allow_request is not None:
            _dict['allow_request'] = self.allow_request
        if hasattr(self, 'ibm') and self.ibm is not None:
            _dict['ibm'] = self.ibm
        if hasattr(self, 'public') and self.public is not None:
            _dict['public'] = self.public
        if hasattr(self, 'changed') and self.changed is not None:
            _dict['changed'] = self.changed
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApprovalResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApprovalResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApprovalResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Catalog():
    """
    Catalog information.

    :attr str id: (optional) Unique ID.
    :attr str rev: (optional) Cloudant revision.
    :attr str label: (optional) Display Name in the requested language.
    :attr str short_description: (optional) Description in the requested language.
    :attr str catalog_icon_url: (optional) URL for an icon associated with this
          catalog.
    :attr List[str] tags: (optional) List of tags associated with this catalog.
    :attr str url: (optional) The url for this specific catalog.
    :attr str crn: (optional) CRN associated with the catalog.
    :attr str offerings_url: (optional) URL path to offerings.
    :attr List[Feature] features: (optional) List of features associated with this
          catalog.
    :attr bool disabled: (optional) Denotes whether a catalog is disabled.
    :attr datetime created: (optional) The date'time this catalog was created.
    :attr datetime updated: (optional) The date'time this catalog was last updated.
    :attr str resource_group_id: (optional) Resource group id the catalog is owned
          by.
    :attr str owning_account: (optional) Account that owns catalog.
    :attr Filters catalog_filters: (optional) Filters for account and catalog
          filters.
    :attr SyndicationResource syndication_settings: (optional) Feature information.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 rev: str = None,
                 label: str = None,
                 short_description: str = None,
                 catalog_icon_url: str = None,
                 tags: List[str] = None,
                 url: str = None,
                 crn: str = None,
                 offerings_url: str = None,
                 features: List['Feature'] = None,
                 disabled: bool = None,
                 created: datetime = None,
                 updated: datetime = None,
                 resource_group_id: str = None,
                 owning_account: str = None,
                 catalog_filters: 'Filters' = None,
                 syndication_settings: 'SyndicationResource' = None) -> None:
        """
        Initialize a Catalog object.

        :param str id: (optional) Unique ID.
        :param str rev: (optional) Cloudant revision.
        :param str label: (optional) Display Name in the requested language.
        :param str short_description: (optional) Description in the requested
               language.
        :param str catalog_icon_url: (optional) URL for an icon associated with
               this catalog.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param str url: (optional) The url for this specific catalog.
        :param str crn: (optional) CRN associated with the catalog.
        :param str offerings_url: (optional) URL path to offerings.
        :param List[Feature] features: (optional) List of features associated with
               this catalog.
        :param bool disabled: (optional) Denotes whether a catalog is disabled.
        :param datetime created: (optional) The date'time this catalog was created.
        :param datetime updated: (optional) The date'time this catalog was last
               updated.
        :param str resource_group_id: (optional) Resource group id the catalog is
               owned by.
        :param str owning_account: (optional) Account that owns catalog.
        :param Filters catalog_filters: (optional) Filters for account and catalog
               filters.
        :param SyndicationResource syndication_settings: (optional) Feature
               information.
        """
        self.id = id
        self.rev = rev
        self.label = label
        self.short_description = short_description
        self.catalog_icon_url = catalog_icon_url
        self.tags = tags
        self.url = url
        self.crn = crn
        self.offerings_url = offerings_url
        self.features = features
        self.disabled = disabled
        self.created = created
        self.updated = updated
        self.resource_group_id = resource_group_id
        self.owning_account = owning_account
        self.catalog_filters = catalog_filters
        self.syndication_settings = syndication_settings

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Catalog':
        """Initialize a Catalog object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if '_rev' in _dict:
            args['rev'] = _dict.get('_rev')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'short_description' in _dict:
            args['short_description'] = _dict.get('short_description')
        if 'catalog_icon_url' in _dict:
            args['catalog_icon_url'] = _dict.get('catalog_icon_url')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'offerings_url' in _dict:
            args['offerings_url'] = _dict.get('offerings_url')
        if 'features' in _dict:
            args['features'] = [Feature.from_dict(x) for x in _dict.get('features')]
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        if 'owning_account' in _dict:
            args['owning_account'] = _dict.get('owning_account')
        if 'catalog_filters' in _dict:
            args['catalog_filters'] = Filters.from_dict(_dict.get('catalog_filters'))
        if 'syndication_settings' in _dict:
            args['syndication_settings'] = SyndicationResource.from_dict(_dict.get('syndication_settings'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Catalog object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['_rev'] = self.rev
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'short_description') and self.short_description is not None:
            _dict['short_description'] = self.short_description
        if hasattr(self, 'catalog_icon_url') and self.catalog_icon_url is not None:
            _dict['catalog_icon_url'] = self.catalog_icon_url
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'offerings_url') and self.offerings_url is not None:
            _dict['offerings_url'] = self.offerings_url
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = [x.to_dict() for x in self.features]
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'owning_account') and self.owning_account is not None:
            _dict['owning_account'] = self.owning_account
        if hasattr(self, 'catalog_filters') and self.catalog_filters is not None:
            _dict['catalog_filters'] = self.catalog_filters.to_dict()
        if hasattr(self, 'syndication_settings') and self.syndication_settings is not None:
            _dict['syndication_settings'] = self.syndication_settings.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Catalog object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Catalog') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Catalog') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CatalogSearchResult():
    """
    Paginated catalog search result.

    :attr int offset: (optional) The offset (origin 0) of the first resource in this
          page of search results.
    :attr int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :attr int total_count: (optional) The overall total number of resources in the
          search result set.
    :attr int resource_count: (optional) The number of resources returned in this
          page of search results.
    :attr str first: (optional) A URL for retrieving the first page of search
          results.
    :attr str last: (optional) A URL for retrieving the last page of search results.
    :attr str prev: (optional) A URL for retrieving the previous page of search
          results.
    :attr str next: (optional) A URL for retrieving the next page of search results.
    :attr List[Catalog] resources: (optional) Resulting objects.
    """

    def __init__(self,
                 *,
                 offset: int = None,
                 limit: int = None,
                 total_count: int = None,
                 resource_count: int = None,
                 first: str = None,
                 last: str = None,
                 prev: str = None,
                 next: str = None,
                 resources: List['Catalog'] = None) -> None:
        """
        Initialize a CatalogSearchResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int total_count: (optional) The overall total number of resources in
               the search result set.
        :param int resource_count: (optional) The number of resources returned in
               this page of search results.
        :param str first: (optional) A URL for retrieving the first page of search
               results.
        :param str last: (optional) A URL for retrieving the last page of search
               results.
        :param str prev: (optional) A URL for retrieving the previous page of
               search results.
        :param str next: (optional) A URL for retrieving the next page of search
               results.
        :param List[Catalog] resources: (optional) Resulting objects.
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CatalogSearchResult':
        """Initialize a CatalogSearchResult object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'resource_count' in _dict:
            args['resource_count'] = _dict.get('resource_count')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'last' in _dict:
            args['last'] = _dict.get('last')
        if 'prev' in _dict:
            args['prev'] = _dict.get('prev')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'resources' in _dict:
            args['resources'] = [Catalog.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CatalogSearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'resource_count') and self.resource_count is not None:
            _dict['resource_count'] = self.resource_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last
        if hasattr(self, 'prev') and self.prev is not None:
            _dict['prev'] = self.prev
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CatalogSearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CatalogSearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CatalogSearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CategoryFilter():
    """
    Filter on a category. The filter will match against the values of the given category
    with include or exclude.

    :attr bool include: (optional) -> true - This is an include filter, false - this
          is an exclude filter.
    :attr FilterTerms filter: (optional) Offering filter terms.
    """

    def __init__(self,
                 *,
                 include: bool = None,
                 filter: 'FilterTerms' = None) -> None:
        """
        Initialize a CategoryFilter object.

        :param bool include: (optional) -> true - This is an include filter, false
               - this is an exclude filter.
        :param FilterTerms filter: (optional) Offering filter terms.
        """
        self.include = include
        self.filter = filter

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoryFilter':
        """Initialize a CategoryFilter object from a json dictionary."""
        args = {}
        if 'include' in _dict:
            args['include'] = _dict.get('include')
        if 'filter' in _dict:
            args['filter'] = FilterTerms.from_dict(_dict.get('filter'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoryFilter object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'include') and self.include is not None:
            _dict['include'] = self.include
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoryFilter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CategoryFilter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoryFilter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ClusterInfo():
    """
    Cluster information.

    :attr str resource_group_id: (optional) Resource Group ID.
    :attr str resource_group_name: (optional) Resource Group name.
    :attr str id: (optional) Cluster ID.
    :attr str name: (optional) Cluster name.
    :attr str region: (optional) Cluster region.
    """

    def __init__(self,
                 *,
                 resource_group_id: str = None,
                 resource_group_name: str = None,
                 id: str = None,
                 name: str = None,
                 region: str = None) -> None:
        """
        Initialize a ClusterInfo object.

        :param str resource_group_id: (optional) Resource Group ID.
        :param str resource_group_name: (optional) Resource Group name.
        :param str id: (optional) Cluster ID.
        :param str name: (optional) Cluster name.
        :param str region: (optional) Cluster region.
        """
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.id = id
        self.name = name
        self.region = region

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClusterInfo':
        """Initialize a ClusterInfo object from a json dictionary."""
        args = {}
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        if 'resource_group_name' in _dict:
            args['resource_group_name'] = _dict.get('resource_group_name')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'region' in _dict:
            args['region'] = _dict.get('region')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClusterInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'resource_group_name') and self.resource_group_name is not None:
            _dict['resource_group_name'] = self.resource_group_name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClusterInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClusterInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClusterInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ClusterSearchResult():
    """
    Paginated cluster search result.

    :attr int offset: (optional) The offset (origin 0) of the first resource in this
          page of search results.
    :attr int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :attr int total_count: (optional) The overall total number of resources in the
          search result set.
    :attr int resource_count: (optional) The number of resources returned in this
          page of search results.
    :attr str first: (optional) A URL for retrieving the first page of search
          results.
    :attr str last: (optional) A URL for retrieving the last page of search results.
    :attr str prev: (optional) A URL for retrieving the previous page of search
          results.
    :attr str next: (optional) A URL for retrieving the next page of search results.
    :attr List[ClusterInfo] resources: (optional) Resulting objects.
    """

    def __init__(self,
                 *,
                 offset: int = None,
                 limit: int = None,
                 total_count: int = None,
                 resource_count: int = None,
                 first: str = None,
                 last: str = None,
                 prev: str = None,
                 next: str = None,
                 resources: List['ClusterInfo'] = None) -> None:
        """
        Initialize a ClusterSearchResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int total_count: (optional) The overall total number of resources in
               the search result set.
        :param int resource_count: (optional) The number of resources returned in
               this page of search results.
        :param str first: (optional) A URL for retrieving the first page of search
               results.
        :param str last: (optional) A URL for retrieving the last page of search
               results.
        :param str prev: (optional) A URL for retrieving the previous page of
               search results.
        :param str next: (optional) A URL for retrieving the next page of search
               results.
        :param List[ClusterInfo] resources: (optional) Resulting objects.
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClusterSearchResult':
        """Initialize a ClusterSearchResult object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'resource_count' in _dict:
            args['resource_count'] = _dict.get('resource_count')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'last' in _dict:
            args['last'] = _dict.get('last')
        if 'prev' in _dict:
            args['prev'] = _dict.get('prev')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'resources' in _dict:
            args['resources'] = [ClusterInfo.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClusterSearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'resource_count') and self.resource_count is not None:
            _dict['resource_count'] = self.resource_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last
        if hasattr(self, 'prev') and self.prev is not None:
            _dict['prev'] = self.prev
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClusterSearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClusterSearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClusterSearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Configuration():
    """
    Configuration description.

    :attr str key: (optional) Configuration key.
    :attr str type: (optional) Value type (string, boolean, int).
    :attr object default_value: (optional) The default value.
    :attr str value_constraint: (optional) Constraint associated with value, e.g.,
          for string type - regx:[a-z].
    :attr str description: (optional) Key description.
    :attr bool required: (optional) Is key required to install.
    :attr List[object] options: (optional) List of options of type.
    :attr bool hidden: (optional) Hide values.
    """

    def __init__(self,
                 *,
                 key: str = None,
                 type: str = None,
                 default_value: object = None,
                 value_constraint: str = None,
                 description: str = None,
                 required: bool = None,
                 options: List[object] = None,
                 hidden: bool = None) -> None:
        """
        Initialize a Configuration object.

        :param str key: (optional) Configuration key.
        :param str type: (optional) Value type (string, boolean, int).
        :param object default_value: (optional) The default value.
        :param str value_constraint: (optional) Constraint associated with value,
               e.g., for string type - regx:[a-z].
        :param str description: (optional) Key description.
        :param bool required: (optional) Is key required to install.
        :param List[object] options: (optional) List of options of type.
        :param bool hidden: (optional) Hide values.
        """
        self.key = key
        self.type = type
        self.default_value = default_value
        self.value_constraint = value_constraint
        self.description = description
        self.required = required
        self.options = options
        self.hidden = hidden

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Configuration':
        """Initialize a Configuration object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'default_value' in _dict:
            args['default_value'] = _dict.get('default_value')
        if 'value_constraint' in _dict:
            args['value_constraint'] = _dict.get('value_constraint')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'required' in _dict:
            args['required'] = _dict.get('required')
        if 'options' in _dict:
            args['options'] = _dict.get('options')
        if 'hidden' in _dict:
            args['hidden'] = _dict.get('hidden')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Configuration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'default_value') and self.default_value is not None:
            _dict['default_value'] = self.default_value
        if hasattr(self, 'value_constraint') and self.value_constraint is not None:
            _dict['value_constraint'] = self.value_constraint
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'required') and self.required is not None:
            _dict['required'] = self.required
        if hasattr(self, 'options') and self.options is not None:
            _dict['options'] = self.options
        if hasattr(self, 'hidden') and self.hidden is not None:
            _dict['hidden'] = self.hidden
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Configuration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Configuration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Configuration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeployRequestBodySchematics():
    """
    Schematics workspace configuration.

    :attr str name: (optional) Schematics workspace name.
    :attr str description: (optional) Schematics workspace description.
    :attr List[str] tags: (optional) Schematics workspace tags.
    :attr str resource_group_id: (optional) Resource group to use when creating the
          schematics workspace.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 description: str = None,
                 tags: List[str] = None,
                 resource_group_id: str = None) -> None:
        """
        Initialize a DeployRequestBodySchematics object.

        :param str name: (optional) Schematics workspace name.
        :param str description: (optional) Schematics workspace description.
        :param List[str] tags: (optional) Schematics workspace tags.
        :param str resource_group_id: (optional) Resource group to use when
               creating the schematics workspace.
        """
        self.name = name
        self.description = description
        self.tags = tags
        self.resource_group_id = resource_group_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeployRequestBodySchematics':
        """Initialize a DeployRequestBodySchematics object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeployRequestBodySchematics object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeployRequestBodySchematics object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeployRequestBodySchematics') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeployRequestBodySchematics') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeployRequirementsCheck():
    """
    Failed deployment requirements.

    :attr object pre_install: (optional) Failed during pre-install.
    :attr object install: (optional) Failed during install.
    """

    def __init__(self,
                 *,
                 pre_install: object = None,
                 install: object = None) -> None:
        """
        Initialize a DeployRequirementsCheck object.

        :param object pre_install: (optional) Failed during pre-install.
        :param object install: (optional) Failed during install.
        """
        self.pre_install = pre_install
        self.install = install

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeployRequirementsCheck':
        """Initialize a DeployRequirementsCheck object from a json dictionary."""
        args = {}
        if 'pre_install' in _dict:
            args['pre_install'] = _dict.get('pre_install')
        if 'install' in _dict:
            args['install'] = _dict.get('install')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeployRequirementsCheck object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pre_install') and self.pre_install is not None:
            _dict['pre_install'] = self.pre_install
        if hasattr(self, 'install') and self.install is not None:
            _dict['install'] = self.install
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeployRequirementsCheck object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeployRequirementsCheck') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeployRequirementsCheck') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Deployment():
    """
    Deployment for offering.

    :attr str id: (optional) unique id.
    :attr str label: (optional) Display Name in the requested language.
    :attr str name: (optional) The programmatic name of this offering.
    :attr str short_description: (optional) Short description in the requested
          language.
    :attr str long_description: (optional) Long description in the requested
          language.
    :attr object metadata: (optional) open ended metadata information.
    :attr List[str] tags: (optional) list of tags associated with this catalog.
    :attr datetime created: (optional) the date'time this catalog was created.
    :attr datetime updated: (optional) the date'time this catalog was last updated.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 label: str = None,
                 name: str = None,
                 short_description: str = None,
                 long_description: str = None,
                 metadata: object = None,
                 tags: List[str] = None,
                 created: datetime = None,
                 updated: datetime = None) -> None:
        """
        Initialize a Deployment object.

        :param str id: (optional) unique id.
        :param str label: (optional) Display Name in the requested language.
        :param str name: (optional) The programmatic name of this offering.
        :param str short_description: (optional) Short description in the requested
               language.
        :param str long_description: (optional) Long description in the requested
               language.
        :param object metadata: (optional) open ended metadata information.
        :param List[str] tags: (optional) list of tags associated with this
               catalog.
        :param datetime created: (optional) the date'time this catalog was created.
        :param datetime updated: (optional) the date'time this catalog was last
               updated.
        """
        self.id = id
        self.label = label
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.metadata = metadata
        self.tags = tags
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Deployment':
        """Initialize a Deployment object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'short_description' in _dict:
            args['short_description'] = _dict.get('short_description')
        if 'long_description' in _dict:
            args['long_description'] = _dict.get('long_description')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Deployment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'short_description') and self.short_description is not None:
            _dict['short_description'] = self.short_description
        if hasattr(self, 'long_description') and self.long_description is not None:
            _dict['long_description'] = self.long_description
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Deployment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Deployment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Deployment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Enterprise():
    """
    Enterprise account information.

    :attr str id: (optional) Enterprise identification.
    :attr str rev: (optional) Cloudant revision.
    :attr Filters account_filters: (optional) Filters for account and catalog
          filters.
    :attr EnterpriseAccountGroups account_groups: (optional) Map of account group
          ids to AccountGroup objects.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 rev: str = None,
                 account_filters: 'Filters' = None,
                 account_groups: 'EnterpriseAccountGroups' = None) -> None:
        """
        Initialize a Enterprise object.

        :param str id: (optional) Enterprise identification.
        :param str rev: (optional) Cloudant revision.
        :param Filters account_filters: (optional) Filters for account and catalog
               filters.
        :param EnterpriseAccountGroups account_groups: (optional) Map of account
               group ids to AccountGroup objects.
        """
        self.id = id
        self.rev = rev
        self.account_filters = account_filters
        self.account_groups = account_groups

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Enterprise':
        """Initialize a Enterprise object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if '_rev' in _dict:
            args['rev'] = _dict.get('_rev')
        if 'account_filters' in _dict:
            args['account_filters'] = Filters.from_dict(_dict.get('account_filters'))
        if 'account_groups' in _dict:
            args['account_groups'] = EnterpriseAccountGroups.from_dict(_dict.get('account_groups'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Enterprise object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['_rev'] = self.rev
        if hasattr(self, 'account_filters') and self.account_filters is not None:
            _dict['account_filters'] = self.account_filters.to_dict()
        if hasattr(self, 'account_groups') and self.account_groups is not None:
            _dict['account_groups'] = self.account_groups.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Enterprise object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Enterprise') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Enterprise') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class EnterpriseAccountGroups():
    """
    Map of account group ids to AccountGroup objects.

    :attr AccountGroup keys: (optional) Filters for an Account Group.
    """

    def __init__(self,
                 *,
                 keys: 'AccountGroup' = None) -> None:
        """
        Initialize a EnterpriseAccountGroups object.

        :param AccountGroup keys: (optional) Filters for an Account Group.
        """
        self.keys = keys

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnterpriseAccountGroups':
        """Initialize a EnterpriseAccountGroups object from a json dictionary."""
        args = {}
        if 'keys' in _dict:
            args['keys'] = AccountGroup.from_dict(_dict.get('keys'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnterpriseAccountGroups object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'keys') and self.keys is not None:
            _dict['keys'] = self.keys.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnterpriseAccountGroups object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnterpriseAccountGroups') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnterpriseAccountGroups') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Feature():
    """
    Feature information.

    :attr str title: (optional) Heading.
    :attr str description: (optional) Feature description.
    """

    def __init__(self,
                 *,
                 title: str = None,
                 description: str = None) -> None:
        """
        Initialize a Feature object.

        :param str title: (optional) Heading.
        :param str description: (optional) Feature description.
        """
        self.title = title
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Feature':
        """Initialize a Feature object from a json dictionary."""
        args = {}
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Feature object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Feature object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Feature') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Feature') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FilterTerms():
    """
    Offering filter terms.

    :attr List[str] filter_terms: (optional) List of values to match against. If
          include is true, then if the offering has one of the values then the offering is
          included. If include is false, then if the offering has one of the values then
          the offering is excluded.
    """

    def __init__(self,
                 *,
                 filter_terms: List[str] = None) -> None:
        """
        Initialize a FilterTerms object.

        :param List[str] filter_terms: (optional) List of values to match against.
               If include is true, then if the offering has one of the values then the
               offering is included. If include is false, then if the offering has one of
               the values then the offering is excluded.
        """
        self.filter_terms = filter_terms

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FilterTerms':
        """Initialize a FilterTerms object from a json dictionary."""
        args = {}
        if 'filter_terms' in _dict:
            args['filter_terms'] = _dict.get('filter_terms')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FilterTerms object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'filter_terms') and self.filter_terms is not None:
            _dict['filter_terms'] = self.filter_terms
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FilterTerms object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FilterTerms') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FilterTerms') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Filters():
    """
    Filters for account and catalog filters.

    :attr bool include_all: (optional) -> true - Include all of the public catalog
          when filtering. Further settings will specifically exclude some offerings. false
          - Exclude all of the public catalog when filtering. Further settings will
          specifically include some offerings.
    :attr dict category_filters: (optional) Filter against offering properties.
    :attr IDFilter id_filters: (optional) Filter on offering ID's. There is an
          include filter and an exclule filter. Both can be set.
    """

    def __init__(self,
                 *,
                 include_all: bool = None,
                 category_filters: dict = None,
                 id_filters: 'IDFilter' = None) -> None:
        """
        Initialize a Filters object.

        :param bool include_all: (optional) -> true - Include all of the public
               catalog when filtering. Further settings will specifically exclude some
               offerings. false - Exclude all of the public catalog when filtering.
               Further settings will specifically include some offerings.
        :param dict category_filters: (optional) Filter against offering
               properties.
        :param IDFilter id_filters: (optional) Filter on offering ID's. There is an
               include filter and an exclule filter. Both can be set.
        """
        self.include_all = include_all
        self.category_filters = category_filters
        self.id_filters = id_filters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Filters':
        """Initialize a Filters object from a json dictionary."""
        args = {}
        if 'include_all' in _dict:
            args['include_all'] = _dict.get('include_all')
        if 'category_filters' in _dict:
            args['category_filters'] = {k : CategoryFilter.from_dict(v) for k, v in _dict.get('category_filters').items()}
        if 'id_filters' in _dict:
            args['id_filters'] = IDFilter.from_dict(_dict.get('id_filters'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Filters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'include_all') and self.include_all is not None:
            _dict['include_all'] = self.include_all
        if hasattr(self, 'category_filters') and self.category_filters is not None:
            _dict['category_filters'] = {k : v.to_dict() for k, v in self.category_filters.items()}
        if hasattr(self, 'id_filters') and self.id_filters is not None:
            _dict['id_filters'] = self.id_filters.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Filters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Filters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Filters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HelmChart():
    """
    Helm chart.

    :attr str name: (optional) Chart name.
    :attr str description: (optional) Chart description.
    :attr str icon: (optional) Chart icon.
    :attr str version: (optional) Chart version.
    :attr str app_version: (optional) Chart app version.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 description: str = None,
                 icon: str = None,
                 version: str = None,
                 app_version: str = None) -> None:
        """
        Initialize a HelmChart object.

        :param str name: (optional) Chart name.
        :param str description: (optional) Chart description.
        :param str icon: (optional) Chart icon.
        :param str version: (optional) Chart version.
        :param str app_version: (optional) Chart app version.
        """
        self.name = name
        self.description = description
        self.icon = icon
        self.version = version
        self.app_version = app_version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HelmChart':
        """Initialize a HelmChart object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'icon' in _dict:
            args['icon'] = _dict.get('icon')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'appVersion' in _dict:
            args['app_version'] = _dict.get('appVersion')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HelmChart object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'icon') and self.icon is not None:
            _dict['icon'] = self.icon
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'app_version') and self.app_version is not None:
            _dict['appVersion'] = self.app_version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HelmChart object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HelmChart') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HelmChart') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HelmPackage():
    """
    Helm package.

    :attr HelmPackageChart chart: (optional) The name of the requested chart, or the
          name of a nested chart within the requested chart.
    """

    def __init__(self,
                 *,
                 chart: 'HelmPackageChart' = None) -> None:
        """
        Initialize a HelmPackage object.

        :param HelmPackageChart chart: (optional) The name of the requested chart,
               or the name of a nested chart within the requested chart.
        """
        self.chart = chart

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HelmPackage':
        """Initialize a HelmPackage object from a json dictionary."""
        args = {}
        if 'chart' in _dict:
            args['chart'] = HelmPackageChart.from_dict(_dict.get('chart'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HelmPackage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'chart') and self.chart is not None:
            _dict['chart'] = self.chart.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HelmPackage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HelmPackage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HelmPackage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HelmPackageChart():
    """
    The name of the requested chart, or the name of a nested chart within the requested
    chart.

    :attr HelmChart chart_yaml: (optional) Helm chart.
    :attr object sha: (optional) Project SHA.
    :attr str readme_md: (optional) Helm chart description.
    :attr object values_metadata: (optional) Values metadata.
    :attr object license_metadata: (optional) License metadata.
    """

    def __init__(self,
                 *,
                 chart_yaml: 'HelmChart' = None,
                 sha: object = None,
                 readme_md: str = None,
                 values_metadata: object = None,
                 license_metadata: object = None) -> None:
        """
        Initialize a HelmPackageChart object.

        :param HelmChart chart_yaml: (optional) Helm chart.
        :param object sha: (optional) Project SHA.
        :param str readme_md: (optional) Helm chart description.
        :param object values_metadata: (optional) Values metadata.
        :param object license_metadata: (optional) License metadata.
        """
        self.chart_yaml = chart_yaml
        self.sha = sha
        self.readme_md = readme_md
        self.values_metadata = values_metadata
        self.license_metadata = license_metadata

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HelmPackageChart':
        """Initialize a HelmPackageChart object from a json dictionary."""
        args = {}
        if 'Chart.yaml' in _dict:
            args['chart_yaml'] = HelmChart.from_dict(_dict.get('Chart.yaml'))
        if 'sha' in _dict:
            args['sha'] = _dict.get('sha')
        if 'README.md' in _dict:
            args['readme_md'] = _dict.get('README.md')
        if 'values-metadata' in _dict:
            args['values_metadata'] = _dict.get('values-metadata')
        if 'license-metadata' in _dict:
            args['license_metadata'] = _dict.get('license-metadata')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HelmPackageChart object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'chart_yaml') and self.chart_yaml is not None:
            _dict['Chart.yaml'] = self.chart_yaml.to_dict()
        if hasattr(self, 'sha') and self.sha is not None:
            _dict['sha'] = self.sha
        if hasattr(self, 'readme_md') and self.readme_md is not None:
            _dict['README.md'] = self.readme_md
        if hasattr(self, 'values_metadata') and self.values_metadata is not None:
            _dict['values-metadata'] = self.values_metadata
        if hasattr(self, 'license_metadata') and self.license_metadata is not None:
            _dict['license-metadata'] = self.license_metadata
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HelmPackageChart object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HelmPackageChart') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HelmPackageChart') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HelmRepoList():
    """
    Helm repository metadata.

    :attr HelmRepoListChart chart: (optional) A chart entry in the repo. This
          response will contain many chart names.
    """

    def __init__(self,
                 *,
                 chart: 'HelmRepoListChart' = None) -> None:
        """
        Initialize a HelmRepoList object.

        :param HelmRepoListChart chart: (optional) A chart entry in the repo. This
               response will contain many chart names.
        """
        self.chart = chart

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HelmRepoList':
        """Initialize a HelmRepoList object from a json dictionary."""
        args = {}
        if 'chart' in _dict:
            args['chart'] = HelmRepoListChart.from_dict(_dict.get('chart'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HelmRepoList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'chart') and self.chart is not None:
            _dict['chart'] = self.chart.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HelmRepoList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HelmRepoList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HelmRepoList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HelmRepoListChart():
    """
    A chart entry in the repo. This response will contain many chart names.

    :attr str api_version: (optional) API version.
    :attr datetime created: (optional) Date and time created.
    :attr str description: (optional) Description of Helm repo entry.
    :attr bool deprecated: (optional) Denotes whether repo entry is deprecated.
    :attr str digest: (optional) Digest of entry.
    :attr str home: (optional) Location of repo entry.
    :attr str icon: (optional) Entry icon.
    :attr List[str] keywords: (optional) List of keywords.
    :attr List[Maintainers] maintainers: (optional) Emails and names of repo
          maintainers.
    :attr str name: (optional) Entry name.
    :attr str tiller_version: (optional) Helm server version.
    :attr List[str] urls: (optional) Array of URLs.
    :attr List[str] sources: (optional) Array of sources.
    :attr str version: (optional) Entry version.
    :attr str app_version: (optional) Application version.
    """

    def __init__(self,
                 *,
                 api_version: str = None,
                 created: datetime = None,
                 description: str = None,
                 deprecated: bool = None,
                 digest: str = None,
                 home: str = None,
                 icon: str = None,
                 keywords: List[str] = None,
                 maintainers: List['Maintainers'] = None,
                 name: str = None,
                 tiller_version: str = None,
                 urls: List[str] = None,
                 sources: List[str] = None,
                 version: str = None,
                 app_version: str = None) -> None:
        """
        Initialize a HelmRepoListChart object.

        :param str api_version: (optional) API version.
        :param datetime created: (optional) Date and time created.
        :param str description: (optional) Description of Helm repo entry.
        :param bool deprecated: (optional) Denotes whether repo entry is
               deprecated.
        :param str digest: (optional) Digest of entry.
        :param str home: (optional) Location of repo entry.
        :param str icon: (optional) Entry icon.
        :param List[str] keywords: (optional) List of keywords.
        :param List[Maintainers] maintainers: (optional) Emails and names of repo
               maintainers.
        :param str name: (optional) Entry name.
        :param str tiller_version: (optional) Helm server version.
        :param List[str] urls: (optional) Array of URLs.
        :param List[str] sources: (optional) Array of sources.
        :param str version: (optional) Entry version.
        :param str app_version: (optional) Application version.
        """
        self.api_version = api_version
        self.created = created
        self.description = description
        self.deprecated = deprecated
        self.digest = digest
        self.home = home
        self.icon = icon
        self.keywords = keywords
        self.maintainers = maintainers
        self.name = name
        self.tiller_version = tiller_version
        self.urls = urls
        self.sources = sources
        self.version = version
        self.app_version = app_version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HelmRepoListChart':
        """Initialize a HelmRepoListChart object from a json dictionary."""
        args = {}
        if 'api_version' in _dict:
            args['api_version'] = _dict.get('api_version')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'deprecated' in _dict:
            args['deprecated'] = _dict.get('deprecated')
        if 'digest' in _dict:
            args['digest'] = _dict.get('digest')
        if 'home' in _dict:
            args['home'] = _dict.get('home')
        if 'icon' in _dict:
            args['icon'] = _dict.get('icon')
        if 'keywords' in _dict:
            args['keywords'] = _dict.get('keywords')
        if 'maintainers' in _dict:
            args['maintainers'] = [Maintainers.from_dict(x) for x in _dict.get('maintainers')]
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'tiller_version' in _dict:
            args['tiller_version'] = _dict.get('tiller_version')
        if 'urls' in _dict:
            args['urls'] = _dict.get('urls')
        if 'sources' in _dict:
            args['sources'] = _dict.get('sources')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'appVersion' in _dict:
            args['app_version'] = _dict.get('appVersion')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HelmRepoListChart object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'api_version') and self.api_version is not None:
            _dict['api_version'] = self.api_version
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'deprecated') and self.deprecated is not None:
            _dict['deprecated'] = self.deprecated
        if hasattr(self, 'digest') and self.digest is not None:
            _dict['digest'] = self.digest
        if hasattr(self, 'home') and self.home is not None:
            _dict['home'] = self.home
        if hasattr(self, 'icon') and self.icon is not None:
            _dict['icon'] = self.icon
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = self.keywords
        if hasattr(self, 'maintainers') and self.maintainers is not None:
            _dict['maintainers'] = [x.to_dict() for x in self.maintainers]
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'tiller_version') and self.tiller_version is not None:
            _dict['tiller_version'] = self.tiller_version
        if hasattr(self, 'urls') and self.urls is not None:
            _dict['urls'] = self.urls
        if hasattr(self, 'sources') and self.sources is not None:
            _dict['sources'] = self.sources
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'app_version') and self.app_version is not None:
            _dict['appVersion'] = self.app_version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HelmRepoListChart object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HelmRepoListChart') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HelmRepoListChart') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IDFilter():
    """
    Filter on offering ID's. There is an include filter and an exclule filter. Both can be
    set.

    :attr FilterTerms include: (optional) Offering filter terms.
    :attr FilterTerms exclude: (optional) Offering filter terms.
    """

    def __init__(self,
                 *,
                 include: 'FilterTerms' = None,
                 exclude: 'FilterTerms' = None) -> None:
        """
        Initialize a IDFilter object.

        :param FilterTerms include: (optional) Offering filter terms.
        :param FilterTerms exclude: (optional) Offering filter terms.
        """
        self.include = include
        self.exclude = exclude

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IDFilter':
        """Initialize a IDFilter object from a json dictionary."""
        args = {}
        if 'include' in _dict:
            args['include'] = FilterTerms.from_dict(_dict.get('include'))
        if 'exclude' in _dict:
            args['exclude'] = FilterTerms.from_dict(_dict.get('exclude'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IDFilter object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'include') and self.include is not None:
            _dict['include'] = self.include.to_dict()
        if hasattr(self, 'exclude') and self.exclude is not None:
            _dict['exclude'] = self.exclude.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IDFilter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IDFilter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IDFilter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Image():
    """
    Image.

    :attr str image: (optional) Image.
    """

    def __init__(self,
                 *,
                 image: str = None) -> None:
        """
        Initialize a Image object.

        :param str image: (optional) Image.
        """
        self.image = image

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Image':
        """Initialize a Image object from a json dictionary."""
        args = {}
        if 'image' in _dict:
            args['image'] = _dict.get('image')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Image object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'image') and self.image is not None:
            _dict['image'] = self.image
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Image object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Image') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Image') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageManifest():
    """
    Image Manifest.

    :attr str description: (optional) Image manifest description.
    :attr List[Image] images: (optional) List of images.
    """

    def __init__(self,
                 *,
                 description: str = None,
                 images: List['Image'] = None) -> None:
        """
        Initialize a ImageManifest object.

        :param str description: (optional) Image manifest description.
        :param List[Image] images: (optional) List of images.
        """
        self.description = description
        self.images = images

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageManifest':
        """Initialize a ImageManifest object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'images' in _dict:
            args['images'] = [Image.from_dict(x) for x in _dict.get('images')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageManifest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'images') and self.images is not None:
            _dict['images'] = [x.to_dict() for x in self.images]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageManifest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageManifest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageManifest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstallStatus():
    """
    Installation status.

    :attr InstallStatusMetadata metadata: (optional) Installation status metadata.
    :attr InstallStatusRelease release: (optional) Release information.
    :attr InstallStatusContentMgmt content_mgmt: (optional) Content management
          information.
    """

    def __init__(self,
                 *,
                 metadata: 'InstallStatusMetadata' = None,
                 release: 'InstallStatusRelease' = None,
                 content_mgmt: 'InstallStatusContentMgmt' = None) -> None:
        """
        Initialize a InstallStatus object.

        :param InstallStatusMetadata metadata: (optional) Installation status
               metadata.
        :param InstallStatusRelease release: (optional) Release information.
        :param InstallStatusContentMgmt content_mgmt: (optional) Content management
               information.
        """
        self.metadata = metadata
        self.release = release
        self.content_mgmt = content_mgmt

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstallStatus':
        """Initialize a InstallStatus object from a json dictionary."""
        args = {}
        if 'metadata' in _dict:
            args['metadata'] = InstallStatusMetadata.from_dict(_dict.get('metadata'))
        if 'release' in _dict:
            args['release'] = InstallStatusRelease.from_dict(_dict.get('release'))
        if 'content_mgmt' in _dict:
            args['content_mgmt'] = InstallStatusContentMgmt.from_dict(_dict.get('content_mgmt'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstallStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata.to_dict()
        if hasattr(self, 'release') and self.release is not None:
            _dict['release'] = self.release.to_dict()
        if hasattr(self, 'content_mgmt') and self.content_mgmt is not None:
            _dict['content_mgmt'] = self.content_mgmt.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstallStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstallStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstallStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstallStatusContentMgmt():
    """
    Content management information.

    :attr List[object] pods: (optional) Pods.
    :attr List[object] errors: (optional) Errors.
    """

    def __init__(self,
                 *,
                 pods: List[object] = None,
                 errors: List[object] = None) -> None:
        """
        Initialize a InstallStatusContentMgmt object.

        :param List[object] pods: (optional) Pods.
        :param List[object] errors: (optional) Errors.
        """
        self.pods = pods
        self.errors = errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstallStatusContentMgmt':
        """Initialize a InstallStatusContentMgmt object from a json dictionary."""
        args = {}
        if 'pods' in _dict:
            args['pods'] = _dict.get('pods')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstallStatusContentMgmt object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pods') and self.pods is not None:
            _dict['pods'] = self.pods
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstallStatusContentMgmt object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstallStatusContentMgmt') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstallStatusContentMgmt') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstallStatusMetadata():
    """
    Installation status metadata.

    :attr str cluster_id: (optional) Cluster ID.
    :attr str region: (optional) Cluster region.
    :attr str namespace: (optional) Cluster namespace.
    :attr str workspace_id: (optional) Workspace ID.
    :attr str workspace_name: (optional) Workspace name.
    """

    def __init__(self,
                 *,
                 cluster_id: str = None,
                 region: str = None,
                 namespace: str = None,
                 workspace_id: str = None,
                 workspace_name: str = None) -> None:
        """
        Initialize a InstallStatusMetadata object.

        :param str cluster_id: (optional) Cluster ID.
        :param str region: (optional) Cluster region.
        :param str namespace: (optional) Cluster namespace.
        :param str workspace_id: (optional) Workspace ID.
        :param str workspace_name: (optional) Workspace name.
        """
        self.cluster_id = cluster_id
        self.region = region
        self.namespace = namespace
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstallStatusMetadata':
        """Initialize a InstallStatusMetadata object from a json dictionary."""
        args = {}
        if 'cluster_id' in _dict:
            args['cluster_id'] = _dict.get('cluster_id')
        if 'region' in _dict:
            args['region'] = _dict.get('region')
        if 'namespace' in _dict:
            args['namespace'] = _dict.get('namespace')
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        if 'workspace_name' in _dict:
            args['workspace_name'] = _dict.get('workspace_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstallStatusMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cluster_id') and self.cluster_id is not None:
            _dict['cluster_id'] = self.cluster_id
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'namespace') and self.namespace is not None:
            _dict['namespace'] = self.namespace
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
        if hasattr(self, 'workspace_name') and self.workspace_name is not None:
            _dict['workspace_name'] = self.workspace_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstallStatusMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstallStatusMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstallStatusMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstallStatusRelease():
    """
    Release information.

    :attr List[object] deployments: (optional) Kube deployments.
    :attr List[object] replicasets: (optional) Kube replica sets.
    :attr List[object] statefulsets: (optional) Kube stateful sets.
    :attr List[object] pods: (optional) Kube pods.
    :attr List[object] errors: (optional) Kube errors.
    """

    def __init__(self,
                 *,
                 deployments: List[object] = None,
                 replicasets: List[object] = None,
                 statefulsets: List[object] = None,
                 pods: List[object] = None,
                 errors: List[object] = None) -> None:
        """
        Initialize a InstallStatusRelease object.

        :param List[object] deployments: (optional) Kube deployments.
        :param List[object] replicasets: (optional) Kube replica sets.
        :param List[object] statefulsets: (optional) Kube stateful sets.
        :param List[object] pods: (optional) Kube pods.
        :param List[object] errors: (optional) Kube errors.
        """
        self.deployments = deployments
        self.replicasets = replicasets
        self.statefulsets = statefulsets
        self.pods = pods
        self.errors = errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstallStatusRelease':
        """Initialize a InstallStatusRelease object from a json dictionary."""
        args = {}
        if 'deployments' in _dict:
            args['deployments'] = _dict.get('deployments')
        if 'replicasets' in _dict:
            args['replicasets'] = _dict.get('replicasets')
        if 'statefulsets' in _dict:
            args['statefulsets'] = _dict.get('statefulsets')
        if 'pods' in _dict:
            args['pods'] = _dict.get('pods')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstallStatusRelease object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deployments') and self.deployments is not None:
            _dict['deployments'] = self.deployments
        if hasattr(self, 'replicasets') and self.replicasets is not None:
            _dict['replicasets'] = self.replicasets
        if hasattr(self, 'statefulsets') and self.statefulsets is not None:
            _dict['statefulsets'] = self.statefulsets
        if hasattr(self, 'pods') and self.pods is not None:
            _dict['pods'] = self.pods
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstallStatusRelease object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstallStatusRelease') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstallStatusRelease') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Kind():
    """
    Offering kind.

    :attr str id: (optional) Unique ID.
    :attr str format_kind: (optional) content kind, e.g., helm, vm image.
    :attr str target_kind: (optional) target cloud to install, e.g., iks,
          open_shift_iks.
    :attr object metadata: (optional) Open ended metadata information.
    :attr str install_description: (optional) Installation instruction.
    :attr List[str] tags: (optional) List of tags associated with this catalog.
    :attr List[Feature] additional_features: (optional) List of features associated
          with this offering.
    :attr datetime created: (optional) The date and time this catalog was created.
    :attr datetime updated: (optional) The date and time this catalog was last
          updated.
    :attr List[Version] versions: (optional) list of versions.
    :attr List[Plan] plans: (optional) list of plans.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 format_kind: str = None,
                 target_kind: str = None,
                 metadata: object = None,
                 install_description: str = None,
                 tags: List[str] = None,
                 additional_features: List['Feature'] = None,
                 created: datetime = None,
                 updated: datetime = None,
                 versions: List['Version'] = None,
                 plans: List['Plan'] = None) -> None:
        """
        Initialize a Kind object.

        :param str id: (optional) Unique ID.
        :param str format_kind: (optional) content kind, e.g., helm, vm image.
        :param str target_kind: (optional) target cloud to install, e.g., iks,
               open_shift_iks.
        :param object metadata: (optional) Open ended metadata information.
        :param str install_description: (optional) Installation instruction.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param List[Feature] additional_features: (optional) List of features
               associated with this offering.
        :param datetime created: (optional) The date and time this catalog was
               created.
        :param datetime updated: (optional) The date and time this catalog was last
               updated.
        :param List[Version] versions: (optional) list of versions.
        :param List[Plan] plans: (optional) list of plans.
        """
        self.id = id
        self.format_kind = format_kind
        self.target_kind = target_kind
        self.metadata = metadata
        self.install_description = install_description
        self.tags = tags
        self.additional_features = additional_features
        self.created = created
        self.updated = updated
        self.versions = versions
        self.plans = plans

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Kind':
        """Initialize a Kind object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'format_kind' in _dict:
            args['format_kind'] = _dict.get('format_kind')
        if 'target_kind' in _dict:
            args['target_kind'] = _dict.get('target_kind')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'install_description' in _dict:
            args['install_description'] = _dict.get('install_description')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'additional_features' in _dict:
            args['additional_features'] = [Feature.from_dict(x) for x in _dict.get('additional_features')]
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'versions' in _dict:
            args['versions'] = [Version.from_dict(x) for x in _dict.get('versions')]
        if 'plans' in _dict:
            args['plans'] = [Plan.from_dict(x) for x in _dict.get('plans')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Kind object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'format_kind') and self.format_kind is not None:
            _dict['format_kind'] = self.format_kind
        if hasattr(self, 'target_kind') and self.target_kind is not None:
            _dict['target_kind'] = self.target_kind
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'install_description') and self.install_description is not None:
            _dict['install_description'] = self.install_description
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'additional_features') and self.additional_features is not None:
            _dict['additional_features'] = [x.to_dict() for x in self.additional_features]
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'versions') and self.versions is not None:
            _dict['versions'] = [x.to_dict() for x in self.versions]
        if hasattr(self, 'plans') and self.plans is not None:
            _dict['plans'] = [x.to_dict() for x in self.plans]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Kind object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Kind') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Kind') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class License():
    """
    BSS license.

    :attr str id: (optional) License ID.
    :attr str name: (optional) license name.
    :attr str type: (optional) type of license e.g., Apache xxx.
    :attr str url: (optional) URL for the license text.
    :attr str description: (optional) License description.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 url: str = None,
                 description: str = None) -> None:
        """
        Initialize a License object.

        :param str id: (optional) License ID.
        :param str name: (optional) license name.
        :param str type: (optional) type of license e.g., Apache xxx.
        :param str url: (optional) URL for the license text.
        :param str description: (optional) License description.
        """
        self.id = id
        self.name = name
        self.type = type
        self.url = url
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'License':
        """Initialize a License object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a License object from a json dictionary."""
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
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this License object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'License') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'License') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LicenseEntitlement():
    """
    License entitlement.

    :attr str name: (optional) Entitlement name.
    :attr str id: (optional) Entitlement ID.
    :attr str crn: (optional) Entitlement CRN.
    :attr str url: (optional) URL for the BSS entitlement, e.g.
          /v1/licensing/entitlements/:id.
    :attr str offering_type: (optional) Entitlement offering type.
    :attr str state: (optional) State of the BSS entitlement, e.g. 'active' or if
          it's been deleted, 'removed'.
    :attr str effective_from: (optional) Entitlement is good from this starting
          date. eg. '2019-07-17T21:21:47.6794935Z'.
    :attr str effective_until: (optional) Entitlement is good until this ending
          date. eg. '2019-07-17T21:21:47.6794935Z'.
    :attr str account_id: (optional) Account ID where this entitlement is bound to.
    :attr str owner_id: (optional) Account ID of owner.
    :attr str version_id: (optional) GC ID of the specific offering version.
    :attr str license_offering_id: (optional) Marketplace offering ID for this
          license entitlement.
    :attr str license_id: (optional) Specific license entitlement ID from the
          license provider, eg. D1W3R4.
    :attr str license_owner_id: (optional) IBM ID of the owner of this license
          entitlement.
    :attr str license_type: (optional) Type of license entitlement, e.g. ibm-ppa.
    :attr str license_provider_id: (optional) ID of the license provider.
    :attr str license_provider_url: (optional) URL for the BSS license provider,
          e.g. /v1/licensing/license_providers/:license_provider_id.
    :attr str license_product_id: (optional) Specific license entitlement ID from
          the license provider, eg. D1W3R4.
    :attr str namespace_repository: (optional) Location of the registry images, eg.
          cp/cp4d.
    :attr str apikey: (optional) API key for access to the license entitlement.
    :attr str create_by: (optional) IBM ID.
    :attr str update_by: (optional) IBM ID.
    :attr str create_at: (optional) Creation date, eg.
          '2019-07-17T21:21:47.6794935Z'.
    :attr str updated_at: (optional) Date last updated, eg.
          '2019-07-17T21:21:47.6794935Z'.
    :attr List[LicenseEntitlementHistoryItem] history: (optional) Entitlement
          history.
    :attr List[LicenseOfferingReference] offering_list: (optional) Array of license
          offering references.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 id: str = None,
                 crn: str = None,
                 url: str = None,
                 offering_type: str = None,
                 state: str = None,
                 effective_from: str = None,
                 effective_until: str = None,
                 account_id: str = None,
                 owner_id: str = None,
                 version_id: str = None,
                 license_offering_id: str = None,
                 license_id: str = None,
                 license_owner_id: str = None,
                 license_type: str = None,
                 license_provider_id: str = None,
                 license_provider_url: str = None,
                 license_product_id: str = None,
                 namespace_repository: str = None,
                 apikey: str = None,
                 create_by: str = None,
                 update_by: str = None,
                 create_at: str = None,
                 updated_at: str = None,
                 history: List['LicenseEntitlementHistoryItem'] = None,
                 offering_list: List['LicenseOfferingReference'] = None) -> None:
        """
        Initialize a LicenseEntitlement object.

        :param str name: (optional) Entitlement name.
        :param str id: (optional) Entitlement ID.
        :param str crn: (optional) Entitlement CRN.
        :param str url: (optional) URL for the BSS entitlement, e.g.
               /v1/licensing/entitlements/:id.
        :param str offering_type: (optional) Entitlement offering type.
        :param str state: (optional) State of the BSS entitlement, e.g. 'active' or
               if it's been deleted, 'removed'.
        :param str effective_from: (optional) Entitlement is good from this
               starting date. eg. '2019-07-17T21:21:47.6794935Z'.
        :param str effective_until: (optional) Entitlement is good until this
               ending date. eg. '2019-07-17T21:21:47.6794935Z'.
        :param str account_id: (optional) Account ID where this entitlement is
               bound to.
        :param str owner_id: (optional) Account ID of owner.
        :param str version_id: (optional) GC ID of the specific offering version.
        :param str license_offering_id: (optional) Marketplace offering ID for this
               license entitlement.
        :param str license_id: (optional) Specific license entitlement ID from the
               license provider, eg. D1W3R4.
        :param str license_owner_id: (optional) IBM ID of the owner of this license
               entitlement.
        :param str license_type: (optional) Type of license entitlement, e.g.
               ibm-ppa.
        :param str license_provider_id: (optional) ID of the license provider.
        :param str license_provider_url: (optional) URL for the BSS license
               provider, e.g. /v1/licensing/license_providers/:license_provider_id.
        :param str license_product_id: (optional) Specific license entitlement ID
               from the license provider, eg. D1W3R4.
        :param str namespace_repository: (optional) Location of the registry
               images, eg. cp/cp4d.
        :param str apikey: (optional) API key for access to the license
               entitlement.
        :param str create_by: (optional) IBM ID.
        :param str update_by: (optional) IBM ID.
        :param str create_at: (optional) Creation date, eg.
               '2019-07-17T21:21:47.6794935Z'.
        :param str updated_at: (optional) Date last updated, eg.
               '2019-07-17T21:21:47.6794935Z'.
        :param List[LicenseEntitlementHistoryItem] history: (optional) Entitlement
               history.
        :param List[LicenseOfferingReference] offering_list: (optional) Array of
               license offering references.
        """
        self.name = name
        self.id = id
        self.crn = crn
        self.url = url
        self.offering_type = offering_type
        self.state = state
        self.effective_from = effective_from
        self.effective_until = effective_until
        self.account_id = account_id
        self.owner_id = owner_id
        self.version_id = version_id
        self.license_offering_id = license_offering_id
        self.license_id = license_id
        self.license_owner_id = license_owner_id
        self.license_type = license_type
        self.license_provider_id = license_provider_id
        self.license_provider_url = license_provider_url
        self.license_product_id = license_product_id
        self.namespace_repository = namespace_repository
        self.apikey = apikey
        self.create_by = create_by
        self.update_by = update_by
        self.create_at = create_at
        self.updated_at = updated_at
        self.history = history
        self.offering_list = offering_list

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LicenseEntitlement':
        """Initialize a LicenseEntitlement object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'offering_type' in _dict:
            args['offering_type'] = _dict.get('offering_type')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'effective_from' in _dict:
            args['effective_from'] = _dict.get('effective_from')
        if 'effective_until' in _dict:
            args['effective_until'] = _dict.get('effective_until')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'owner_id' in _dict:
            args['owner_id'] = _dict.get('owner_id')
        if 'version_id' in _dict:
            args['version_id'] = _dict.get('version_id')
        if 'license_offering_id' in _dict:
            args['license_offering_id'] = _dict.get('license_offering_id')
        if 'license_id' in _dict:
            args['license_id'] = _dict.get('license_id')
        if 'license_owner_id' in _dict:
            args['license_owner_id'] = _dict.get('license_owner_id')
        if 'license_type' in _dict:
            args['license_type'] = _dict.get('license_type')
        if 'license_provider_id' in _dict:
            args['license_provider_id'] = _dict.get('license_provider_id')
        if 'license_provider_url' in _dict:
            args['license_provider_url'] = _dict.get('license_provider_url')
        if 'license_product_id' in _dict:
            args['license_product_id'] = _dict.get('license_product_id')
        if 'namespace_repository' in _dict:
            args['namespace_repository'] = _dict.get('namespace_repository')
        if 'apikey' in _dict:
            args['apikey'] = _dict.get('apikey')
        if 'create_by' in _dict:
            args['create_by'] = _dict.get('create_by')
        if 'update_by' in _dict:
            args['update_by'] = _dict.get('update_by')
        if 'create_at' in _dict:
            args['create_at'] = _dict.get('create_at')
        if 'updated_at' in _dict:
            args['updated_at'] = _dict.get('updated_at')
        if 'history' in _dict:
            args['history'] = [LicenseEntitlementHistoryItem.from_dict(x) for x in _dict.get('history')]
        if 'offering_list' in _dict:
            args['offering_list'] = [LicenseOfferingReference.from_dict(x) for x in _dict.get('offering_list')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LicenseEntitlement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'offering_type') and self.offering_type is not None:
            _dict['offering_type'] = self.offering_type
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'effective_from') and self.effective_from is not None:
            _dict['effective_from'] = self.effective_from
        if hasattr(self, 'effective_until') and self.effective_until is not None:
            _dict['effective_until'] = self.effective_until
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'owner_id') and self.owner_id is not None:
            _dict['owner_id'] = self.owner_id
        if hasattr(self, 'version_id') and self.version_id is not None:
            _dict['version_id'] = self.version_id
        if hasattr(self, 'license_offering_id') and self.license_offering_id is not None:
            _dict['license_offering_id'] = self.license_offering_id
        if hasattr(self, 'license_id') and self.license_id is not None:
            _dict['license_id'] = self.license_id
        if hasattr(self, 'license_owner_id') and self.license_owner_id is not None:
            _dict['license_owner_id'] = self.license_owner_id
        if hasattr(self, 'license_type') and self.license_type is not None:
            _dict['license_type'] = self.license_type
        if hasattr(self, 'license_provider_id') and self.license_provider_id is not None:
            _dict['license_provider_id'] = self.license_provider_id
        if hasattr(self, 'license_provider_url') and self.license_provider_url is not None:
            _dict['license_provider_url'] = self.license_provider_url
        if hasattr(self, 'license_product_id') and self.license_product_id is not None:
            _dict['license_product_id'] = self.license_product_id
        if hasattr(self, 'namespace_repository') and self.namespace_repository is not None:
            _dict['namespace_repository'] = self.namespace_repository
        if hasattr(self, 'apikey') and self.apikey is not None:
            _dict['apikey'] = self.apikey
        if hasattr(self, 'create_by') and self.create_by is not None:
            _dict['create_by'] = self.create_by
        if hasattr(self, 'update_by') and self.update_by is not None:
            _dict['update_by'] = self.update_by
        if hasattr(self, 'create_at') and self.create_at is not None:
            _dict['create_at'] = self.create_at
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = self.updated_at
        if hasattr(self, 'history') and self.history is not None:
            _dict['history'] = [x.to_dict() for x in self.history]
        if hasattr(self, 'offering_list') and self.offering_list is not None:
            _dict['offering_list'] = [x.to_dict() for x in self.offering_list]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LicenseEntitlement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LicenseEntitlement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LicenseEntitlement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LicenseEntitlementHistoryItem():
    """
    LicenseEntitlementHistoryItem.

    :attr str action: (optional) Eg. create.
    :attr str user: (optional) Eg. IBM ID of user.
    :attr str date: (optional) Date of action, eg. '2019-07-17T21:21:47.6794935Z'.
    """

    def __init__(self,
                 *,
                 action: str = None,
                 user: str = None,
                 date: str = None) -> None:
        """
        Initialize a LicenseEntitlementHistoryItem object.

        :param str action: (optional) Eg. create.
        :param str user: (optional) Eg. IBM ID of user.
        :param str date: (optional) Date of action, eg.
               '2019-07-17T21:21:47.6794935Z'.
        """
        self.action = action
        self.user = user
        self.date = date

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LicenseEntitlementHistoryItem':
        """Initialize a LicenseEntitlementHistoryItem object from a json dictionary."""
        args = {}
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        if 'date' in _dict:
            args['date'] = _dict.get('date')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LicenseEntitlementHistoryItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        if hasattr(self, 'date') and self.date is not None:
            _dict['date'] = self.date
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LicenseEntitlementHistoryItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LicenseEntitlementHistoryItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LicenseEntitlementHistoryItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LicenseEntitlements():
    """
    Paginated list of license entitlements.

    :attr int total_results: (optional) Total number of results.
    :attr int total_pages: (optional) Total number of pages.
    :attr str prev_url: (optional) Previous URL.
    :attr str next_url: (optional) Next URL.
    :attr List[LicenseEntitlement] resources: (optional) Resulting Entitlement
          objects.
    """

    def __init__(self,
                 *,
                 total_results: int = None,
                 total_pages: int = None,
                 prev_url: str = None,
                 next_url: str = None,
                 resources: List['LicenseEntitlement'] = None) -> None:
        """
        Initialize a LicenseEntitlements object.

        :param int total_results: (optional) Total number of results.
        :param int total_pages: (optional) Total number of pages.
        :param str prev_url: (optional) Previous URL.
        :param str next_url: (optional) Next URL.
        :param List[LicenseEntitlement] resources: (optional) Resulting Entitlement
               objects.
        """
        self.total_results = total_results
        self.total_pages = total_pages
        self.prev_url = prev_url
        self.next_url = next_url
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LicenseEntitlements':
        """Initialize a LicenseEntitlements object from a json dictionary."""
        args = {}
        if 'total_results' in _dict:
            args['total_results'] = _dict.get('total_results')
        if 'total_pages' in _dict:
            args['total_pages'] = _dict.get('total_pages')
        if 'prev_url' in _dict:
            args['prev_url'] = _dict.get('prev_url')
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        if 'resources' in _dict:
            args['resources'] = [LicenseEntitlement.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LicenseEntitlements object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_results') and self.total_results is not None:
            _dict['total_results'] = self.total_results
        if hasattr(self, 'total_pages') and self.total_pages is not None:
            _dict['total_pages'] = self.total_pages
        if hasattr(self, 'prev_url') and self.prev_url is not None:
            _dict['prev_url'] = self.prev_url
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LicenseEntitlements object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LicenseEntitlements') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LicenseEntitlements') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LicenseObject():
    """
    License information.

    :attr str name: (optional) License name.
    :attr str offering_type: (optional) Type of offering.
    :attr str seats_allowed: (optional) Number of seats allowed for license.
    :attr str seats_used: (optional) Number of seats used for license.
    :attr str owner_id: (optional) ID of license owner.
    :attr str license_offering_id: (optional) Marketplace offering ID for this
          license.
    :attr str license_id: (optional) specific license entitlement ID from the
          license provider, eg. D1W3R4.
    :attr str license_owner_id: (optional) IBM ID of the owner of this license
          entitlement.
    :attr str license_type: (optional) type of license entitlement, e.g. ibm-ppa.
    :attr str license_provider_id: (optional) ID of the license provider.
    :attr str license_product_id: (optional) specific license entitlement ID from
          the license provider, eg. D1W3R4.
    :attr str license_provider_url: (optional) URL for the BSS license provider,
          e.g. /v1/licensing/license_providers/:license_provider_id.
    :attr str effective_from: (optional) license is good from this starting date.
          eg. '2019-07-17T21:21:47.6794935Z'.
    :attr str effective_until: (optional) license is good until this ending date.
          eg. '2019-07-17T21:21:47.6794935Z'.
    :attr bool internal: (optional) If true, this will allow use of this license by
          all IBMers.
    :attr List[LicenseOfferingReference] offering_list: (optional) Array of license
          offering references.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 offering_type: str = None,
                 seats_allowed: str = None,
                 seats_used: str = None,
                 owner_id: str = None,
                 license_offering_id: str = None,
                 license_id: str = None,
                 license_owner_id: str = None,
                 license_type: str = None,
                 license_provider_id: str = None,
                 license_product_id: str = None,
                 license_provider_url: str = None,
                 effective_from: str = None,
                 effective_until: str = None,
                 internal: bool = None,
                 offering_list: List['LicenseOfferingReference'] = None) -> None:
        """
        Initialize a LicenseObject object.

        :param str name: (optional) License name.
        :param str offering_type: (optional) Type of offering.
        :param str seats_allowed: (optional) Number of seats allowed for license.
        :param str seats_used: (optional) Number of seats used for license.
        :param str owner_id: (optional) ID of license owner.
        :param str license_offering_id: (optional) Marketplace offering ID for this
               license.
        :param str license_id: (optional) specific license entitlement ID from the
               license provider, eg. D1W3R4.
        :param str license_owner_id: (optional) IBM ID of the owner of this license
               entitlement.
        :param str license_type: (optional) type of license entitlement, e.g.
               ibm-ppa.
        :param str license_provider_id: (optional) ID of the license provider.
        :param str license_product_id: (optional) specific license entitlement ID
               from the license provider, eg. D1W3R4.
        :param str license_provider_url: (optional) URL for the BSS license
               provider, e.g. /v1/licensing/license_providers/:license_provider_id.
        :param str effective_from: (optional) license is good from this starting
               date. eg. '2019-07-17T21:21:47.6794935Z'.
        :param str effective_until: (optional) license is good until this ending
               date. eg. '2019-07-17T21:21:47.6794935Z'.
        :param bool internal: (optional) If true, this will allow use of this
               license by all IBMers.
        :param List[LicenseOfferingReference] offering_list: (optional) Array of
               license offering references.
        """
        self.name = name
        self.offering_type = offering_type
        self.seats_allowed = seats_allowed
        self.seats_used = seats_used
        self.owner_id = owner_id
        self.license_offering_id = license_offering_id
        self.license_id = license_id
        self.license_owner_id = license_owner_id
        self.license_type = license_type
        self.license_provider_id = license_provider_id
        self.license_product_id = license_product_id
        self.license_provider_url = license_provider_url
        self.effective_from = effective_from
        self.effective_until = effective_until
        self.internal = internal
        self.offering_list = offering_list

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LicenseObject':
        """Initialize a LicenseObject object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'offering_type' in _dict:
            args['offering_type'] = _dict.get('offering_type')
        if 'seats_allowed' in _dict:
            args['seats_allowed'] = _dict.get('seats_allowed')
        if 'seats_used' in _dict:
            args['seats_used'] = _dict.get('seats_used')
        if 'owner_id' in _dict:
            args['owner_id'] = _dict.get('owner_id')
        if 'license_offering_id' in _dict:
            args['license_offering_id'] = _dict.get('license_offering_id')
        if 'license_id' in _dict:
            args['license_id'] = _dict.get('license_id')
        if 'license_owner_id' in _dict:
            args['license_owner_id'] = _dict.get('license_owner_id')
        if 'license_type' in _dict:
            args['license_type'] = _dict.get('license_type')
        if 'license_provider_id' in _dict:
            args['license_provider_id'] = _dict.get('license_provider_id')
        if 'license_product_id' in _dict:
            args['license_product_id'] = _dict.get('license_product_id')
        if 'license_provider_url' in _dict:
            args['license_provider_url'] = _dict.get('license_provider_url')
        if 'effective_from' in _dict:
            args['effective_from'] = _dict.get('effective_from')
        if 'effective_until' in _dict:
            args['effective_until'] = _dict.get('effective_until')
        if 'internal' in _dict:
            args['internal'] = _dict.get('internal')
        if 'offering_list' in _dict:
            args['offering_list'] = [LicenseOfferingReference.from_dict(x) for x in _dict.get('offering_list')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LicenseObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'offering_type') and self.offering_type is not None:
            _dict['offering_type'] = self.offering_type
        if hasattr(self, 'seats_allowed') and self.seats_allowed is not None:
            _dict['seats_allowed'] = self.seats_allowed
        if hasattr(self, 'seats_used') and self.seats_used is not None:
            _dict['seats_used'] = self.seats_used
        if hasattr(self, 'owner_id') and self.owner_id is not None:
            _dict['owner_id'] = self.owner_id
        if hasattr(self, 'license_offering_id') and self.license_offering_id is not None:
            _dict['license_offering_id'] = self.license_offering_id
        if hasattr(self, 'license_id') and self.license_id is not None:
            _dict['license_id'] = self.license_id
        if hasattr(self, 'license_owner_id') and self.license_owner_id is not None:
            _dict['license_owner_id'] = self.license_owner_id
        if hasattr(self, 'license_type') and self.license_type is not None:
            _dict['license_type'] = self.license_type
        if hasattr(self, 'license_provider_id') and self.license_provider_id is not None:
            _dict['license_provider_id'] = self.license_provider_id
        if hasattr(self, 'license_product_id') and self.license_product_id is not None:
            _dict['license_product_id'] = self.license_product_id
        if hasattr(self, 'license_provider_url') and self.license_provider_url is not None:
            _dict['license_provider_url'] = self.license_provider_url
        if hasattr(self, 'effective_from') and self.effective_from is not None:
            _dict['effective_from'] = self.effective_from
        if hasattr(self, 'effective_until') and self.effective_until is not None:
            _dict['effective_until'] = self.effective_until
        if hasattr(self, 'internal') and self.internal is not None:
            _dict['internal'] = self.internal
        if hasattr(self, 'offering_list') and self.offering_list is not None:
            _dict['offering_list'] = [x.to_dict() for x in self.offering_list]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LicenseObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LicenseObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LicenseObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LicenseOfferingReference():
    """
    License offering reference.

    :attr str id: (optional) Offering ID.
    :attr str name: (optional) Offering name.
    :attr str label: (optional) Offering label'.
    :attr str offering_icon_url: (optional) URL to offering icon.
    :attr str account_id: (optional) Account ID associated with offering.
    :attr str catalog_id: (optional) Catalog ID associated with offering.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 label: str = None,
                 offering_icon_url: str = None,
                 account_id: str = None,
                 catalog_id: str = None) -> None:
        """
        Initialize a LicenseOfferingReference object.

        :param str id: (optional) Offering ID.
        :param str name: (optional) Offering name.
        :param str label: (optional) Offering label'.
        :param str offering_icon_url: (optional) URL to offering icon.
        :param str account_id: (optional) Account ID associated with offering.
        :param str catalog_id: (optional) Catalog ID associated with offering.
        """
        self.id = id
        self.name = name
        self.label = label
        self.offering_icon_url = offering_icon_url
        self.account_id = account_id
        self.catalog_id = catalog_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LicenseOfferingReference':
        """Initialize a LicenseOfferingReference object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'offering_icon_url' in _dict:
            args['offering_icon_url'] = _dict.get('offering_icon_url')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'catalog_id' in _dict:
            args['catalog_id'] = _dict.get('catalog_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LicenseOfferingReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'offering_icon_url') and self.offering_icon_url is not None:
            _dict['offering_icon_url'] = self.offering_icon_url
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'catalog_id') and self.catalog_id is not None:
            _dict['catalog_id'] = self.catalog_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LicenseOfferingReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LicenseOfferingReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LicenseOfferingReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LicenseProvider():
    """
    BSS License provider.

    :attr str name: (optional) Provider name, eg. IBM Passport Advantage.
    :attr str short_description: (optional) Short description of license provider.
    :attr str id: (optional) Provider ID.
    :attr str licence_type: (optional) Type of license entitlement, e.g. ibm-ppa.
    :attr str offering_type: (optional) Type of offering.
    :attr str create_url: (optional) URL of the license provider for where to
          create/get a license, e.g.
          https://www.ibm.com/software/passportadvantage/aboutpassport.html.
    :attr str info_url: (optional) URL of the license provider for additional info,
          e.g. https://www.ibm.com/software/passportadvantage.
    :attr str url: (optional) URL for the BSS license provider, e.g.
          /v1/licensing/license_providers/:id.
    :attr str crn: (optional) Provider CRN.
    :attr str state: (optional) State of license provider.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 short_description: str = None,
                 id: str = None,
                 licence_type: str = None,
                 offering_type: str = None,
                 create_url: str = None,
                 info_url: str = None,
                 url: str = None,
                 crn: str = None,
                 state: str = None) -> None:
        """
        Initialize a LicenseProvider object.

        :param str name: (optional) Provider name, eg. IBM Passport Advantage.
        :param str short_description: (optional) Short description of license
               provider.
        :param str id: (optional) Provider ID.
        :param str licence_type: (optional) Type of license entitlement, e.g.
               ibm-ppa.
        :param str offering_type: (optional) Type of offering.
        :param str create_url: (optional) URL of the license provider for where to
               create/get a license, e.g.
               https://www.ibm.com/software/passportadvantage/aboutpassport.html.
        :param str info_url: (optional) URL of the license provider for additional
               info, e.g. https://www.ibm.com/software/passportadvantage.
        :param str url: (optional) URL for the BSS license provider, e.g.
               /v1/licensing/license_providers/:id.
        :param str crn: (optional) Provider CRN.
        :param str state: (optional) State of license provider.
        """
        self.name = name
        self.short_description = short_description
        self.id = id
        self.licence_type = licence_type
        self.offering_type = offering_type
        self.create_url = create_url
        self.info_url = info_url
        self.url = url
        self.crn = crn
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LicenseProvider':
        """Initialize a LicenseProvider object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'short_description' in _dict:
            args['short_description'] = _dict.get('short_description')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'licence_type' in _dict:
            args['licence_type'] = _dict.get('licence_type')
        if 'offering_type' in _dict:
            args['offering_type'] = _dict.get('offering_type')
        if 'create_url' in _dict:
            args['create_url'] = _dict.get('create_url')
        if 'info_url' in _dict:
            args['info_url'] = _dict.get('info_url')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LicenseProvider object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'short_description') and self.short_description is not None:
            _dict['short_description'] = self.short_description
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'licence_type') and self.licence_type is not None:
            _dict['licence_type'] = self.licence_type
        if hasattr(self, 'offering_type') and self.offering_type is not None:
            _dict['offering_type'] = self.offering_type
        if hasattr(self, 'create_url') and self.create_url is not None:
            _dict['create_url'] = self.create_url
        if hasattr(self, 'info_url') and self.info_url is not None:
            _dict['info_url'] = self.info_url
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LicenseProvider object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LicenseProvider') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LicenseProvider') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LicenseProviders():
    """
    Paginated list of license providers.

    :attr int total_results: (optional) Total number of results.
    :attr int total_pages: (optional) Total number of pages.
    :attr str prev_url: (optional) Previous URL.
    :attr str next_url: (optional) Next URL.
    :attr List[LicenseProvider] resources: (optional) Resulting License Provider
          objects.
    """

    def __init__(self,
                 *,
                 total_results: int = None,
                 total_pages: int = None,
                 prev_url: str = None,
                 next_url: str = None,
                 resources: List['LicenseProvider'] = None) -> None:
        """
        Initialize a LicenseProviders object.

        :param int total_results: (optional) Total number of results.
        :param int total_pages: (optional) Total number of pages.
        :param str prev_url: (optional) Previous URL.
        :param str next_url: (optional) Next URL.
        :param List[LicenseProvider] resources: (optional) Resulting License
               Provider objects.
        """
        self.total_results = total_results
        self.total_pages = total_pages
        self.prev_url = prev_url
        self.next_url = next_url
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LicenseProviders':
        """Initialize a LicenseProviders object from a json dictionary."""
        args = {}
        if 'total_results' in _dict:
            args['total_results'] = _dict.get('total_results')
        if 'total_pages' in _dict:
            args['total_pages'] = _dict.get('total_pages')
        if 'prev_url' in _dict:
            args['prev_url'] = _dict.get('prev_url')
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        if 'resources' in _dict:
            args['resources'] = [LicenseProvider.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LicenseProviders object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_results') and self.total_results is not None:
            _dict['total_results'] = self.total_results
        if hasattr(self, 'total_pages') and self.total_pages is not None:
            _dict['total_pages'] = self.total_pages
        if hasattr(self, 'prev_url') and self.prev_url is not None:
            _dict['prev_url'] = self.prev_url
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LicenseProviders object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LicenseProviders') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LicenseProviders') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Licenses():
    """
    Paginated list of licenses.

    :attr int total_results: (optional) Total number of results.
    :attr int total_pages: (optional) Total number of pages.
    :attr str prev_url: (optional) Previous URL.
    :attr str next_url: (optional) Next URL.
    :attr List[LicenseObject] resources: (optional) Resulting License objects.
    """

    def __init__(self,
                 *,
                 total_results: int = None,
                 total_pages: int = None,
                 prev_url: str = None,
                 next_url: str = None,
                 resources: List['LicenseObject'] = None) -> None:
        """
        Initialize a Licenses object.

        :param int total_results: (optional) Total number of results.
        :param int total_pages: (optional) Total number of pages.
        :param str prev_url: (optional) Previous URL.
        :param str next_url: (optional) Next URL.
        :param List[LicenseObject] resources: (optional) Resulting License objects.
        """
        self.total_results = total_results
        self.total_pages = total_pages
        self.prev_url = prev_url
        self.next_url = next_url
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Licenses':
        """Initialize a Licenses object from a json dictionary."""
        args = {}
        if 'total_results' in _dict:
            args['total_results'] = _dict.get('total_results')
        if 'total_pages' in _dict:
            args['total_pages'] = _dict.get('total_pages')
        if 'prev_url' in _dict:
            args['prev_url'] = _dict.get('prev_url')
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        if 'resources' in _dict:
            args['resources'] = [LicenseObject.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Licenses object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_results') and self.total_results is not None:
            _dict['total_results'] = self.total_results
        if hasattr(self, 'total_pages') and self.total_pages is not None:
            _dict['total_pages'] = self.total_pages
        if hasattr(self, 'prev_url') and self.prev_url is not None:
            _dict['prev_url'] = self.prev_url
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Licenses object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Licenses') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Licenses') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Maintainers():
    """
    Repo maintainers.

    :attr str email: (optional) Maintainer email address.
    :attr str name: (optional) Name of maintainer.
    """

    def __init__(self,
                 *,
                 email: str = None,
                 name: str = None) -> None:
        """
        Initialize a Maintainers object.

        :param str email: (optional) Maintainer email address.
        :param str name: (optional) Name of maintainer.
        """
        self.email = email
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Maintainers':
        """Initialize a Maintainers object from a json dictionary."""
        args = {}
        if 'email' in _dict:
            args['email'] = _dict.get('email')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Maintainers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = self.email
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Maintainers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Maintainers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Maintainers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NamespaceSearchResult():
    """
    Paginated list of namespace search results.

    :attr int offset: (optional) The offset (origin 0) of the first resource in this
          page of search results.
    :attr int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :attr int total_count: (optional) The overall total number of resources in the
          search result set.
    :attr int resource_count: (optional) The number of resources returned in this
          page of search results.
    :attr str first: (optional) A URL for retrieving the first page of search
          results.
    :attr str last: (optional) A URL for retrieving the last page of search results.
    :attr str prev: (optional) A URL for retrieving the previous page of search
          results.
    :attr str next: (optional) A URL for retrieving the next page of search results.
    :attr List[str] resources: (optional) Resulting objects.
    """

    def __init__(self,
                 *,
                 offset: int = None,
                 limit: int = None,
                 total_count: int = None,
                 resource_count: int = None,
                 first: str = None,
                 last: str = None,
                 prev: str = None,
                 next: str = None,
                 resources: List[str] = None) -> None:
        """
        Initialize a NamespaceSearchResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int total_count: (optional) The overall total number of resources in
               the search result set.
        :param int resource_count: (optional) The number of resources returned in
               this page of search results.
        :param str first: (optional) A URL for retrieving the first page of search
               results.
        :param str last: (optional) A URL for retrieving the last page of search
               results.
        :param str prev: (optional) A URL for retrieving the previous page of
               search results.
        :param str next: (optional) A URL for retrieving the next page of search
               results.
        :param List[str] resources: (optional) Resulting objects.
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NamespaceSearchResult':
        """Initialize a NamespaceSearchResult object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'resource_count' in _dict:
            args['resource_count'] = _dict.get('resource_count')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'last' in _dict:
            args['last'] = _dict.get('last')
        if 'prev' in _dict:
            args['prev'] = _dict.get('prev')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'resources' in _dict:
            args['resources'] = _dict.get('resources')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NamespaceSearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'resource_count') and self.resource_count is not None:
            _dict['resource_count'] = self.resource_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last
        if hasattr(self, 'prev') and self.prev is not None:
            _dict['prev'] = self.prev
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = self.resources
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NamespaceSearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NamespaceSearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NamespaceSearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Object():
    """
    object information.

    :attr str id: (optional) unique id.
    :attr str name: (optional) The programmatic name of this offering.
    :attr str rev: (optional) Cloudant revision.
    :attr str crn: (optional) The crn for this specific object.
    :attr str url: (optional) The url for this specific object.
    :attr str parent_id: (optional) The parent for this specific object.
    :attr List[str] allow_list: (optional) List of allowed accounts for this
          specific object.
    :attr str label_i18n: (optional) Translated display name in the requested
          language.
    :attr str label: (optional) Display name in the requested language.
    :attr List[str] tags: (optional) List of tags associated with this catalog.
    :attr datetime created: (optional) The date and time this catalog was created.
    :attr datetime updated: (optional) The date and time this catalog was last
          updated.
    :attr str short_description: (optional) Short description in the requested
          language.
    :attr str short_description_i18n: (optional) Short description translation.
    :attr str kind: (optional) Kind of object.
    :attr PublishObject publish: (optional) Publish information.
    :attr State state: (optional) Offering state.
    :attr str catalog_id: (optional) The id of the catalog containing this offering.
    :attr str catalog_name: (optional) The name of the catalog.
    :attr object data: (optional) Map of data values for this object.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 rev: str = None,
                 crn: str = None,
                 url: str = None,
                 parent_id: str = None,
                 allow_list: List[str] = None,
                 label_i18n: str = None,
                 label: str = None,
                 tags: List[str] = None,
                 created: datetime = None,
                 updated: datetime = None,
                 short_description: str = None,
                 short_description_i18n: str = None,
                 kind: str = None,
                 publish: 'PublishObject' = None,
                 state: 'State' = None,
                 catalog_id: str = None,
                 catalog_name: str = None,
                 data: object = None) -> None:
        """
        Initialize a Object object.

        :param str id: (optional) unique id.
        :param str name: (optional) The programmatic name of this offering.
        :param str rev: (optional) Cloudant revision.
        :param str crn: (optional) The crn for this specific object.
        :param str url: (optional) The url for this specific object.
        :param str parent_id: (optional) The parent for this specific object.
        :param List[str] allow_list: (optional) List of allowed accounts for this
               specific object.
        :param str label_i18n: (optional) Translated display name in the requested
               language.
        :param str label: (optional) Display name in the requested language.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param datetime created: (optional) The date and time this catalog was
               created.
        :param datetime updated: (optional) The date and time this catalog was last
               updated.
        :param str short_description: (optional) Short description in the requested
               language.
        :param str short_description_i18n: (optional) Short description
               translation.
        :param str kind: (optional) Kind of object.
        :param PublishObject publish: (optional) Publish information.
        :param State state: (optional) Offering state.
        :param str catalog_id: (optional) The id of the catalog containing this
               offering.
        :param str catalog_name: (optional) The name of the catalog.
        :param object data: (optional) Map of data values for this object.
        """
        self.id = id
        self.name = name
        self.rev = rev
        self.crn = crn
        self.url = url
        self.parent_id = parent_id
        self.allow_list = allow_list
        self.label_i18n = label_i18n
        self.label = label
        self.tags = tags
        self.created = created
        self.updated = updated
        self.short_description = short_description
        self.short_description_i18n = short_description_i18n
        self.kind = kind
        self.publish = publish
        self.state = state
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Object':
        """Initialize a Object object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if '_rev' in _dict:
            args['rev'] = _dict.get('_rev')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'parent_id' in _dict:
            args['parent_id'] = _dict.get('parent_id')
        if 'allow_list' in _dict:
            args['allow_list'] = _dict.get('allow_list')
        if 'label_i18n' in _dict:
            args['label_i18n'] = _dict.get('label_i18n')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'short_description' in _dict:
            args['short_description'] = _dict.get('short_description')
        if 'short_description_i18n' in _dict:
            args['short_description_i18n'] = _dict.get('short_description_i18n')
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        if 'publish' in _dict:
            args['publish'] = PublishObject.from_dict(_dict.get('publish'))
        if 'state' in _dict:
            args['state'] = State.from_dict(_dict.get('state'))
        if 'catalog_id' in _dict:
            args['catalog_id'] = _dict.get('catalog_id')
        if 'catalog_name' in _dict:
            args['catalog_name'] = _dict.get('catalog_name')
        if 'data' in _dict:
            args['data'] = _dict.get('data')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Object object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['_rev'] = self.rev
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'parent_id') and self.parent_id is not None:
            _dict['parent_id'] = self.parent_id
        if hasattr(self, 'allow_list') and self.allow_list is not None:
            _dict['allow_list'] = self.allow_list
        if hasattr(self, 'label_i18n') and self.label_i18n is not None:
            _dict['label_i18n'] = self.label_i18n
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'short_description') and self.short_description is not None:
            _dict['short_description'] = self.short_description
        if hasattr(self, 'short_description_i18n') and self.short_description_i18n is not None:
            _dict['short_description_i18n'] = self.short_description_i18n
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'publish') and self.publish is not None:
            _dict['publish'] = self.publish.to_dict()
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state.to_dict()
        if hasattr(self, 'catalog_id') and self.catalog_id is not None:
            _dict['catalog_id'] = self.catalog_id
        if hasattr(self, 'catalog_name') and self.catalog_name is not None:
            _dict['catalog_name'] = self.catalog_name
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Object object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Object') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Object') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ObjectDigest():
    """
    object information.

    :attr str id: (optional) unique id.
    :attr List[float] order: (optional) Lucene match order.
    :attr ObjectDigestFields fields: (optional) Object digest.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 order: List[float] = None,
                 fields: 'ObjectDigestFields' = None) -> None:
        """
        Initialize a ObjectDigest object.

        :param str id: (optional) unique id.
        :param List[float] order: (optional) Lucene match order.
        :param ObjectDigestFields fields: (optional) Object digest.
        """
        self.id = id
        self.order = order
        self.fields = fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectDigest':
        """Initialize a ObjectDigest object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'order' in _dict:
            args['order'] = _dict.get('order')
        if 'fields' in _dict:
            args['fields'] = ObjectDigestFields.from_dict(_dict.get('fields'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectDigest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'order') and self.order is not None:
            _dict['order'] = self.order
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectDigest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ObjectDigest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectDigest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ObjectDigestFields():
    """
    Object digest.

    :attr str catalog_id: (optional) The id of the catalog containing this offering.
    :attr str name: (optional) The programmatic name of this offering.
    :attr str parent_id: (optional) The parent for this specific object.
    :attr str label: (optional) Display name in the requested language.
    :attr datetime updated: (optional) The date and time this catalog was last
          updated.
    :attr str kind: (optional) Kind of object.
    :attr str parent_name: (optional) The name of the object's parent.
    """

    def __init__(self,
                 *,
                 catalog_id: str = None,
                 name: str = None,
                 parent_id: str = None,
                 label: str = None,
                 updated: datetime = None,
                 kind: str = None,
                 parent_name: str = None) -> None:
        """
        Initialize a ObjectDigestFields object.

        :param str catalog_id: (optional) The id of the catalog containing this
               offering.
        :param str name: (optional) The programmatic name of this offering.
        :param str parent_id: (optional) The parent for this specific object.
        :param str label: (optional) Display name in the requested language.
        :param datetime updated: (optional) The date and time this catalog was last
               updated.
        :param str kind: (optional) Kind of object.
        :param str parent_name: (optional) The name of the object's parent.
        """
        self.catalog_id = catalog_id
        self.name = name
        self.parent_id = parent_id
        self.label = label
        self.updated = updated
        self.kind = kind
        self.parent_name = parent_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectDigestFields':
        """Initialize a ObjectDigestFields object from a json dictionary."""
        args = {}
        if 'catalog_id' in _dict:
            args['catalog_id'] = _dict.get('catalog_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'parent_id' in _dict:
            args['parent_id'] = _dict.get('parent_id')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        if 'parent_name' in _dict:
            args['parent_name'] = _dict.get('parent_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectDigestFields object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'catalog_id') and self.catalog_id is not None:
            _dict['catalog_id'] = self.catalog_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'parent_id') and self.parent_id is not None:
            _dict['parent_id'] = self.parent_id
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'parent_name') and self.parent_name is not None:
            _dict['parent_name'] = self.parent_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectDigestFields object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ObjectDigestFields') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectDigestFields') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ObjectListResult():
    """
    Paginated object search result.

    :attr int offset: (optional) The offset (origin 0) of the first resource in this
          page of search results.
    :attr int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :attr int total_count: (optional) The overall total number of resources in the
          search result set.
    :attr int resource_count: (optional) The number of resources returned in this
          page of search results.
    :attr str first: (optional) A URL for retrieving the first page of search
          results.
    :attr str last: (optional) A URL for retrieving the last page of search results.
    :attr str prev: (optional) A URL for retrieving the previous page of search
          results.
    :attr str next: (optional) A URL for retrieving the next page of search results.
    :attr List[Object] resources: (optional) Resulting objects.
    """

    def __init__(self,
                 *,
                 offset: int = None,
                 limit: int = None,
                 total_count: int = None,
                 resource_count: int = None,
                 first: str = None,
                 last: str = None,
                 prev: str = None,
                 next: str = None,
                 resources: List['Object'] = None) -> None:
        """
        Initialize a ObjectListResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int total_count: (optional) The overall total number of resources in
               the search result set.
        :param int resource_count: (optional) The number of resources returned in
               this page of search results.
        :param str first: (optional) A URL for retrieving the first page of search
               results.
        :param str last: (optional) A URL for retrieving the last page of search
               results.
        :param str prev: (optional) A URL for retrieving the previous page of
               search results.
        :param str next: (optional) A URL for retrieving the next page of search
               results.
        :param List[Object] resources: (optional) Resulting objects.
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectListResult':
        """Initialize a ObjectListResult object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'resource_count' in _dict:
            args['resource_count'] = _dict.get('resource_count')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'last' in _dict:
            args['last'] = _dict.get('last')
        if 'prev' in _dict:
            args['prev'] = _dict.get('prev')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'resources' in _dict:
            args['resources'] = [Object.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectListResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'resource_count') and self.resource_count is not None:
            _dict['resource_count'] = self.resource_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last
        if hasattr(self, 'prev') and self.prev is not None:
            _dict['prev'] = self.prev
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectListResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ObjectListResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectListResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ObjectSearchResult():
    """
    Paginated object search result.

    :attr int offset: (optional) The offset (origin 0) of the first resource in this
          page of search results.
    :attr int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :attr int total_count: (optional) The overall total number of resources in the
          search result set.
    :attr int resource_count: (optional) The number of resources returned in this
          page of search results.
    :attr str first: (optional) A URL for retrieving the first page of search
          results.
    :attr str last: (optional) A URL for retrieving the last page of search results.
    :attr str prev: (optional) A URL for retrieving the previous page of search
          results.
    :attr str next: (optional) A URL for retrieving the next page of search results.
    :attr List[ObjectDigest] resources: (optional) Resulting objects.
    """

    def __init__(self,
                 *,
                 offset: int = None,
                 limit: int = None,
                 total_count: int = None,
                 resource_count: int = None,
                 first: str = None,
                 last: str = None,
                 prev: str = None,
                 next: str = None,
                 resources: List['ObjectDigest'] = None) -> None:
        """
        Initialize a ObjectSearchResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int total_count: (optional) The overall total number of resources in
               the search result set.
        :param int resource_count: (optional) The number of resources returned in
               this page of search results.
        :param str first: (optional) A URL for retrieving the first page of search
               results.
        :param str last: (optional) A URL for retrieving the last page of search
               results.
        :param str prev: (optional) A URL for retrieving the previous page of
               search results.
        :param str next: (optional) A URL for retrieving the next page of search
               results.
        :param List[ObjectDigest] resources: (optional) Resulting objects.
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectSearchResult':
        """Initialize a ObjectSearchResult object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'resource_count' in _dict:
            args['resource_count'] = _dict.get('resource_count')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'last' in _dict:
            args['last'] = _dict.get('last')
        if 'prev' in _dict:
            args['prev'] = _dict.get('prev')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'resources' in _dict:
            args['resources'] = [ObjectDigest.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectSearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'resource_count') and self.resource_count is not None:
            _dict['resource_count'] = self.resource_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last
        if hasattr(self, 'prev') and self.prev is not None:
            _dict['prev'] = self.prev
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectSearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ObjectSearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectSearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Offering():
    """
    Offering information.

    :attr str id: (optional) unique id.
    :attr str rev: (optional) Cloudant revision.
    :attr str url: (optional) The url for this specific offering.
    :attr str crn: (optional) The crn for this specific offering.
    :attr str label: (optional) Display Name in the requested language.
    :attr str name: (optional) The programmatic name of this offering.
    :attr str offering_icon_url: (optional) URL for an icon associated with this
          offering.
    :attr str offering_docs_url: (optional) URL for an additional docs with this
          offering.
    :attr str offering_support_url: (optional) URL to be displayed in the
          Consumption UI for getting support on this offering.
    :attr List[str] tags: (optional) List of tags associated with this catalog.
    :attr Rating rating: (optional) Repository info for offerings.
    :attr datetime created: (optional) The date and time this catalog was created.
    :attr datetime updated: (optional) The date and time this catalog was last
          updated.
    :attr str short_description: (optional) Short description in the requested
          language.
    :attr str long_description: (optional) Long description in the requested
          language.
    :attr List[Feature] features: (optional) list of features associated with this
          offering.
    :attr List[Kind] kinds: (optional) Array of kind.
    :attr bool permit_request_ibm_public_publish: (optional) Is it permitted to
          request publishing to IBM or Public.
    :attr bool ibm_publish_approved: (optional) Indicates if this offering has been
          approved for use by all IBMers.
    :attr bool public_publish_approved: (optional) Indicates if this offering has
          been approved for use by all IBM Cloud users.
    :attr str public_original_crn: (optional) The original offering CRN that this
          publish entry came from.
    :attr str publish_public_crn: (optional) The crn of the public catalog entry of
          this offering.
    :attr str portal_approval_record: (optional) The portal's approval record ID.
    :attr str portal_ui_url: (optional) The portal UI URL.
    :attr str catalog_id: (optional) The id of the catalog containing this offering.
    :attr str catalog_name: (optional) The name of the catalog.
    :attr object metadata: (optional) Map of metadata values for this offering.
    :attr str disclaimer: (optional) A disclaimer for this offering.
    :attr bool hidden: (optional) Determine if this offering should be displayed in
          the Consumption UI.
    :attr str provider: (optional) Provider of this offering.
    :attr RepoInfo repo_info: (optional) Repository info for offerings.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 rev: str = None,
                 url: str = None,
                 crn: str = None,
                 label: str = None,
                 name: str = None,
                 offering_icon_url: str = None,
                 offering_docs_url: str = None,
                 offering_support_url: str = None,
                 tags: List[str] = None,
                 rating: 'Rating' = None,
                 created: datetime = None,
                 updated: datetime = None,
                 short_description: str = None,
                 long_description: str = None,
                 features: List['Feature'] = None,
                 kinds: List['Kind'] = None,
                 permit_request_ibm_public_publish: bool = None,
                 ibm_publish_approved: bool = None,
                 public_publish_approved: bool = None,
                 public_original_crn: str = None,
                 publish_public_crn: str = None,
                 portal_approval_record: str = None,
                 portal_ui_url: str = None,
                 catalog_id: str = None,
                 catalog_name: str = None,
                 metadata: object = None,
                 disclaimer: str = None,
                 hidden: bool = None,
                 provider: str = None,
                 repo_info: 'RepoInfo' = None) -> None:
        """
        Initialize a Offering object.

        :param str id: (optional) unique id.
        :param str rev: (optional) Cloudant revision.
        :param str url: (optional) The url for this specific offering.
        :param str crn: (optional) The crn for this specific offering.
        :param str label: (optional) Display Name in the requested language.
        :param str name: (optional) The programmatic name of this offering.
        :param str offering_icon_url: (optional) URL for an icon associated with
               this offering.
        :param str offering_docs_url: (optional) URL for an additional docs with
               this offering.
        :param str offering_support_url: (optional) URL to be displayed in the
               Consumption UI for getting support on this offering.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param Rating rating: (optional) Repository info for offerings.
        :param datetime created: (optional) The date and time this catalog was
               created.
        :param datetime updated: (optional) The date and time this catalog was last
               updated.
        :param str short_description: (optional) Short description in the requested
               language.
        :param str long_description: (optional) Long description in the requested
               language.
        :param List[Feature] features: (optional) list of features associated with
               this offering.
        :param List[Kind] kinds: (optional) Array of kind.
        :param bool permit_request_ibm_public_publish: (optional) Is it permitted
               to request publishing to IBM or Public.
        :param bool ibm_publish_approved: (optional) Indicates if this offering has
               been approved for use by all IBMers.
        :param bool public_publish_approved: (optional) Indicates if this offering
               has been approved for use by all IBM Cloud users.
        :param str public_original_crn: (optional) The original offering CRN that
               this publish entry came from.
        :param str publish_public_crn: (optional) The crn of the public catalog
               entry of this offering.
        :param str portal_approval_record: (optional) The portal's approval record
               ID.
        :param str portal_ui_url: (optional) The portal UI URL.
        :param str catalog_id: (optional) The id of the catalog containing this
               offering.
        :param str catalog_name: (optional) The name of the catalog.
        :param object metadata: (optional) Map of metadata values for this
               offering.
        :param str disclaimer: (optional) A disclaimer for this offering.
        :param bool hidden: (optional) Determine if this offering should be
               displayed in the Consumption UI.
        :param str provider: (optional) Provider of this offering.
        :param RepoInfo repo_info: (optional) Repository info for offerings.
        """
        self.id = id
        self.rev = rev
        self.url = url
        self.crn = crn
        self.label = label
        self.name = name
        self.offering_icon_url = offering_icon_url
        self.offering_docs_url = offering_docs_url
        self.offering_support_url = offering_support_url
        self.tags = tags
        self.rating = rating
        self.created = created
        self.updated = updated
        self.short_description = short_description
        self.long_description = long_description
        self.features = features
        self.kinds = kinds
        self.permit_request_ibm_public_publish = permit_request_ibm_public_publish
        self.ibm_publish_approved = ibm_publish_approved
        self.public_publish_approved = public_publish_approved
        self.public_original_crn = public_original_crn
        self.publish_public_crn = publish_public_crn
        self.portal_approval_record = portal_approval_record
        self.portal_ui_url = portal_ui_url
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.metadata = metadata
        self.disclaimer = disclaimer
        self.hidden = hidden
        self.provider = provider
        self.repo_info = repo_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Offering':
        """Initialize a Offering object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if '_rev' in _dict:
            args['rev'] = _dict.get('_rev')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'offering_icon_url' in _dict:
            args['offering_icon_url'] = _dict.get('offering_icon_url')
        if 'offering_docs_url' in _dict:
            args['offering_docs_url'] = _dict.get('offering_docs_url')
        if 'offering_support_url' in _dict:
            args['offering_support_url'] = _dict.get('offering_support_url')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'rating' in _dict:
            args['rating'] = Rating.from_dict(_dict.get('rating'))
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'short_description' in _dict:
            args['short_description'] = _dict.get('short_description')
        if 'long_description' in _dict:
            args['long_description'] = _dict.get('long_description')
        if 'features' in _dict:
            args['features'] = [Feature.from_dict(x) for x in _dict.get('features')]
        if 'kinds' in _dict:
            args['kinds'] = [Kind.from_dict(x) for x in _dict.get('kinds')]
        if 'permit_request_ibm_public_publish' in _dict:
            args['permit_request_ibm_public_publish'] = _dict.get('permit_request_ibm_public_publish')
        if 'ibm_publish_approved' in _dict:
            args['ibm_publish_approved'] = _dict.get('ibm_publish_approved')
        if 'public_publish_approved' in _dict:
            args['public_publish_approved'] = _dict.get('public_publish_approved')
        if 'public_original_crn' in _dict:
            args['public_original_crn'] = _dict.get('public_original_crn')
        if 'publish_public_crn' in _dict:
            args['publish_public_crn'] = _dict.get('publish_public_crn')
        if 'portal_approval_record' in _dict:
            args['portal_approval_record'] = _dict.get('portal_approval_record')
        if 'portal_ui_url' in _dict:
            args['portal_ui_url'] = _dict.get('portal_ui_url')
        if 'catalog_id' in _dict:
            args['catalog_id'] = _dict.get('catalog_id')
        if 'catalog_name' in _dict:
            args['catalog_name'] = _dict.get('catalog_name')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'disclaimer' in _dict:
            args['disclaimer'] = _dict.get('disclaimer')
        if 'hidden' in _dict:
            args['hidden'] = _dict.get('hidden')
        if 'provider' in _dict:
            args['provider'] = _dict.get('provider')
        if 'repo_info' in _dict:
            args['repo_info'] = RepoInfo.from_dict(_dict.get('repo_info'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Offering object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['_rev'] = self.rev
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'offering_icon_url') and self.offering_icon_url is not None:
            _dict['offering_icon_url'] = self.offering_icon_url
        if hasattr(self, 'offering_docs_url') and self.offering_docs_url is not None:
            _dict['offering_docs_url'] = self.offering_docs_url
        if hasattr(self, 'offering_support_url') and self.offering_support_url is not None:
            _dict['offering_support_url'] = self.offering_support_url
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'rating') and self.rating is not None:
            _dict['rating'] = self.rating.to_dict()
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'short_description') and self.short_description is not None:
            _dict['short_description'] = self.short_description
        if hasattr(self, 'long_description') and self.long_description is not None:
            _dict['long_description'] = self.long_description
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = [x.to_dict() for x in self.features]
        if hasattr(self, 'kinds') and self.kinds is not None:
            _dict['kinds'] = [x.to_dict() for x in self.kinds]
        if hasattr(self, 'permit_request_ibm_public_publish') and self.permit_request_ibm_public_publish is not None:
            _dict['permit_request_ibm_public_publish'] = self.permit_request_ibm_public_publish
        if hasattr(self, 'ibm_publish_approved') and self.ibm_publish_approved is not None:
            _dict['ibm_publish_approved'] = self.ibm_publish_approved
        if hasattr(self, 'public_publish_approved') and self.public_publish_approved is not None:
            _dict['public_publish_approved'] = self.public_publish_approved
        if hasattr(self, 'public_original_crn') and self.public_original_crn is not None:
            _dict['public_original_crn'] = self.public_original_crn
        if hasattr(self, 'publish_public_crn') and self.publish_public_crn is not None:
            _dict['publish_public_crn'] = self.publish_public_crn
        if hasattr(self, 'portal_approval_record') and self.portal_approval_record is not None:
            _dict['portal_approval_record'] = self.portal_approval_record
        if hasattr(self, 'portal_ui_url') and self.portal_ui_url is not None:
            _dict['portal_ui_url'] = self.portal_ui_url
        if hasattr(self, 'catalog_id') and self.catalog_id is not None:
            _dict['catalog_id'] = self.catalog_id
        if hasattr(self, 'catalog_name') and self.catalog_name is not None:
            _dict['catalog_name'] = self.catalog_name
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'disclaimer') and self.disclaimer is not None:
            _dict['disclaimer'] = self.disclaimer
        if hasattr(self, 'hidden') and self.hidden is not None:
            _dict['hidden'] = self.hidden
        if hasattr(self, 'provider') and self.provider is not None:
            _dict['provider'] = self.provider
        if hasattr(self, 'repo_info') and self.repo_info is not None:
            _dict['repo_info'] = self.repo_info.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Offering object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Offering') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Offering') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OfferingSearchResult():
    """
    Paginated offering search result.

    :attr int offset: (optional) The offset (origin 0) of the first resource in this
          page of search results.
    :attr int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :attr int total_count: (optional) The overall total number of resources in the
          search result set.
    :attr int resource_count: (optional) The number of resources returned in this
          page of search results.
    :attr str first: (optional) A URL for retrieving the first page of search
          results.
    :attr str last: (optional) A URL for retrieving the last page of search results.
    :attr str prev: (optional) A URL for retrieving the previous page of search
          results.
    :attr str next: (optional) A URL for retrieving the next page of search results.
    :attr List[Offering] resources: (optional) Resulting objects.
    """

    def __init__(self,
                 *,
                 offset: int = None,
                 limit: int = None,
                 total_count: int = None,
                 resource_count: int = None,
                 first: str = None,
                 last: str = None,
                 prev: str = None,
                 next: str = None,
                 resources: List['Offering'] = None) -> None:
        """
        Initialize a OfferingSearchResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int total_count: (optional) The overall total number of resources in
               the search result set.
        :param int resource_count: (optional) The number of resources returned in
               this page of search results.
        :param str first: (optional) A URL for retrieving the first page of search
               results.
        :param str last: (optional) A URL for retrieving the last page of search
               results.
        :param str prev: (optional) A URL for retrieving the previous page of
               search results.
        :param str next: (optional) A URL for retrieving the next page of search
               results.
        :param List[Offering] resources: (optional) Resulting objects.
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OfferingSearchResult':
        """Initialize a OfferingSearchResult object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'resource_count' in _dict:
            args['resource_count'] = _dict.get('resource_count')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'last' in _dict:
            args['last'] = _dict.get('last')
        if 'prev' in _dict:
            args['prev'] = _dict.get('prev')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'resources' in _dict:
            args['resources'] = [Offering.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OfferingSearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'resource_count') and self.resource_count is not None:
            _dict['resource_count'] = self.resource_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last
        if hasattr(self, 'prev') and self.prev is not None:
            _dict['prev'] = self.prev
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OfferingSearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OfferingSearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OfferingSearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OperatorDeployResult():
    """
    Operator deploy result.

    :attr str phase: (optional) Status phase.
    :attr str message: (optional) Status message.
    :attr str link: (optional) Operator API path.
    :attr str name: (optional) Name of Operator.
    :attr str version: (optional) Operator version.
    :attr str namespace: (optional) Kube namespace.
    :attr str package_name: (optional) Package Operator exists in.
    :attr str catalog_id: (optional) Catalog identification.
    """

    def __init__(self,
                 *,
                 phase: str = None,
                 message: str = None,
                 link: str = None,
                 name: str = None,
                 version: str = None,
                 namespace: str = None,
                 package_name: str = None,
                 catalog_id: str = None) -> None:
        """
        Initialize a OperatorDeployResult object.

        :param str phase: (optional) Status phase.
        :param str message: (optional) Status message.
        :param str link: (optional) Operator API path.
        :param str name: (optional) Name of Operator.
        :param str version: (optional) Operator version.
        :param str namespace: (optional) Kube namespace.
        :param str package_name: (optional) Package Operator exists in.
        :param str catalog_id: (optional) Catalog identification.
        """
        self.phase = phase
        self.message = message
        self.link = link
        self.name = name
        self.version = version
        self.namespace = namespace
        self.package_name = package_name
        self.catalog_id = catalog_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OperatorDeployResult':
        """Initialize a OperatorDeployResult object from a json dictionary."""
        args = {}
        if 'phase' in _dict:
            args['phase'] = _dict.get('phase')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        if 'link' in _dict:
            args['link'] = _dict.get('link')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'namespace' in _dict:
            args['namespace'] = _dict.get('namespace')
        if 'package_name' in _dict:
            args['package_name'] = _dict.get('package_name')
        if 'catalog_id' in _dict:
            args['catalog_id'] = _dict.get('catalog_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OperatorDeployResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'phase') and self.phase is not None:
            _dict['phase'] = self.phase
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'link') and self.link is not None:
            _dict['link'] = self.link
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'namespace') and self.namespace is not None:
            _dict['namespace'] = self.namespace
        if hasattr(self, 'package_name') and self.package_name is not None:
            _dict['package_name'] = self.package_name
        if hasattr(self, 'catalog_id') and self.catalog_id is not None:
            _dict['catalog_id'] = self.catalog_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OperatorDeployResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OperatorDeployResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OperatorDeployResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Plan():
    """
    Offering plan.

    :attr str id: (optional) unique id.
    :attr str label: (optional) Display Name in the requested language.
    :attr str name: (optional) The programmatic name of this offering.
    :attr str short_description: (optional) Short description in the requested
          language.
    :attr str long_description: (optional) Long description in the requested
          language.
    :attr object metadata: (optional) open ended metadata information.
    :attr List[str] tags: (optional) list of tags associated with this catalog.
    :attr List[Feature] additional_features: (optional) list of features associated
          with this offering.
    :attr datetime created: (optional) the date'time this catalog was created.
    :attr datetime updated: (optional) the date'time this catalog was last updated.
    :attr List[Deployment] deployments: (optional) list of deployments.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 label: str = None,
                 name: str = None,
                 short_description: str = None,
                 long_description: str = None,
                 metadata: object = None,
                 tags: List[str] = None,
                 additional_features: List['Feature'] = None,
                 created: datetime = None,
                 updated: datetime = None,
                 deployments: List['Deployment'] = None) -> None:
        """
        Initialize a Plan object.

        :param str id: (optional) unique id.
        :param str label: (optional) Display Name in the requested language.
        :param str name: (optional) The programmatic name of this offering.
        :param str short_description: (optional) Short description in the requested
               language.
        :param str long_description: (optional) Long description in the requested
               language.
        :param object metadata: (optional) open ended metadata information.
        :param List[str] tags: (optional) list of tags associated with this
               catalog.
        :param List[Feature] additional_features: (optional) list of features
               associated with this offering.
        :param datetime created: (optional) the date'time this catalog was created.
        :param datetime updated: (optional) the date'time this catalog was last
               updated.
        :param List[Deployment] deployments: (optional) list of deployments.
        """
        self.id = id
        self.label = label
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.metadata = metadata
        self.tags = tags
        self.additional_features = additional_features
        self.created = created
        self.updated = updated
        self.deployments = deployments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Plan':
        """Initialize a Plan object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'short_description' in _dict:
            args['short_description'] = _dict.get('short_description')
        if 'long_description' in _dict:
            args['long_description'] = _dict.get('long_description')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'additional_features' in _dict:
            args['additional_features'] = [Feature.from_dict(x) for x in _dict.get('additional_features')]
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'deployments' in _dict:
            args['deployments'] = [Deployment.from_dict(x) for x in _dict.get('deployments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Plan object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'short_description') and self.short_description is not None:
            _dict['short_description'] = self.short_description
        if hasattr(self, 'long_description') and self.long_description is not None:
            _dict['long_description'] = self.long_description
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'additional_features') and self.additional_features is not None:
            _dict['additional_features'] = [x.to_dict() for x in self.additional_features]
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'deployments') and self.deployments is not None:
            _dict['deployments'] = [x.to_dict() for x in self.deployments]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Plan object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Plan') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Plan') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PublishObject():
    """
    Publish information.

    :attr bool permit_ibm_public_publish: (optional) Is it permitted to request
          publishing to IBM or Public.
    :attr bool ibm_approved: (optional) Indicates if this offering has been approved
          for use by all IBMers.
    :attr bool public_approved: (optional) Indicates if this offering has been
          approved for use by all IBM Cloud users.
    :attr str portal_approval_record: (optional) The portal's approval record ID.
    :attr str portal_url: (optional) The portal UI URL.
    """

    def __init__(self,
                 *,
                 permit_ibm_public_publish: bool = None,
                 ibm_approved: bool = None,
                 public_approved: bool = None,
                 portal_approval_record: str = None,
                 portal_url: str = None) -> None:
        """
        Initialize a PublishObject object.

        :param bool permit_ibm_public_publish: (optional) Is it permitted to
               request publishing to IBM or Public.
        :param bool ibm_approved: (optional) Indicates if this offering has been
               approved for use by all IBMers.
        :param bool public_approved: (optional) Indicates if this offering has been
               approved for use by all IBM Cloud users.
        :param str portal_approval_record: (optional) The portal's approval record
               ID.
        :param str portal_url: (optional) The portal UI URL.
        """
        self.permit_ibm_public_publish = permit_ibm_public_publish
        self.ibm_approved = ibm_approved
        self.public_approved = public_approved
        self.portal_approval_record = portal_approval_record
        self.portal_url = portal_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PublishObject':
        """Initialize a PublishObject object from a json dictionary."""
        args = {}
        if 'permit_ibm_public_publish' in _dict:
            args['permit_ibm_public_publish'] = _dict.get('permit_ibm_public_publish')
        if 'ibm_approved' in _dict:
            args['ibm_approved'] = _dict.get('ibm_approved')
        if 'public_approved' in _dict:
            args['public_approved'] = _dict.get('public_approved')
        if 'portal_approval_record' in _dict:
            args['portal_approval_record'] = _dict.get('portal_approval_record')
        if 'portal_url' in _dict:
            args['portal_url'] = _dict.get('portal_url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PublishObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'permit_ibm_public_publish') and self.permit_ibm_public_publish is not None:
            _dict['permit_ibm_public_publish'] = self.permit_ibm_public_publish
        if hasattr(self, 'ibm_approved') and self.ibm_approved is not None:
            _dict['ibm_approved'] = self.ibm_approved
        if hasattr(self, 'public_approved') and self.public_approved is not None:
            _dict['public_approved'] = self.public_approved
        if hasattr(self, 'portal_approval_record') and self.portal_approval_record is not None:
            _dict['portal_approval_record'] = self.portal_approval_record
        if hasattr(self, 'portal_url') and self.portal_url is not None:
            _dict['portal_url'] = self.portal_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PublishObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PublishObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PublishObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Rating():
    """
    Repository info for offerings.

    :attr int one_star_count: (optional) One start rating.
    :attr int two_star_count: (optional) Two start rating.
    :attr int three_star_count: (optional) Three start rating.
    :attr int four_star_count: (optional) Four start rating.
    """

    def __init__(self,
                 *,
                 one_star_count: int = None,
                 two_star_count: int = None,
                 three_star_count: int = None,
                 four_star_count: int = None) -> None:
        """
        Initialize a Rating object.

        :param int one_star_count: (optional) One start rating.
        :param int two_star_count: (optional) Two start rating.
        :param int three_star_count: (optional) Three start rating.
        :param int four_star_count: (optional) Four start rating.
        """
        self.one_star_count = one_star_count
        self.two_star_count = two_star_count
        self.three_star_count = three_star_count
        self.four_star_count = four_star_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Rating':
        """Initialize a Rating object from a json dictionary."""
        args = {}
        if 'one_star_count' in _dict:
            args['one_star_count'] = _dict.get('one_star_count')
        if 'two_star_count' in _dict:
            args['two_star_count'] = _dict.get('two_star_count')
        if 'three_star_count' in _dict:
            args['three_star_count'] = _dict.get('three_star_count')
        if 'four_star_count' in _dict:
            args['four_star_count'] = _dict.get('four_star_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Rating object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'one_star_count') and self.one_star_count is not None:
            _dict['one_star_count'] = self.one_star_count
        if hasattr(self, 'two_star_count') and self.two_star_count is not None:
            _dict['two_star_count'] = self.two_star_count
        if hasattr(self, 'three_star_count') and self.three_star_count is not None:
            _dict['three_star_count'] = self.three_star_count
        if hasattr(self, 'four_star_count') and self.four_star_count is not None:
            _dict['four_star_count'] = self.four_star_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Rating object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Rating') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Rating') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RepoInfo():
    """
    Repository info for offerings.

    :attr str token: (optional) Token for private repos.
    :attr str type: (optional) Public or enterprise GitHub.
    """

    def __init__(self,
                 *,
                 token: str = None,
                 type: str = None) -> None:
        """
        Initialize a RepoInfo object.

        :param str token: (optional) Token for private repos.
        :param str type: (optional) Public or enterprise GitHub.
        """
        self.token = token
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RepoInfo':
        """Initialize a RepoInfo object from a json dictionary."""
        args = {}
        if 'token' in _dict:
            args['token'] = _dict.get('token')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RepoInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'token') and self.token is not None:
            _dict['token'] = self.token
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RepoInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RepoInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RepoInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Resource():
    """
    Resource requirements.

    :attr str type: (optional) Type of requirement.
    :attr object value: (optional) mem, disk, cores, and nodes can be parsed as an
          int.  targetVersion will be a semver range value.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 value: object = None) -> None:
        """
        Initialize a Resource object.

        :param str type: (optional) Type of requirement.
        :param object value: (optional) mem, disk, cores, and nodes can be parsed
               as an int.  targetVersion will be a semver range value.
        """
        self.type = type
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Resource':
        """Initialize a Resource object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Resource object from a json dictionary."""
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

    class TypeEnum(str, Enum):
        """
        Type of requirement.
        """
        MEM = 'mem'
        DISK = 'disk'
        CORES = 'cores'
        TARGETVERSION = 'targetVersion'
        NODES = 'nodes'


class ResourceGroup():
    """
    Resource group details.

    :attr str id: (optional) Resource Group ID.
    :attr str name: (optional) Provider name, eg. IBM Passport Advantage.
    :attr str crn: (optional) Provider CRN.
    :attr str account_id: (optional) Account ID for this Resource Group.
    :attr str state: (optional) State of this Resource Group.
    :attr bool default: (optional) Indicates if this Resource Group is active or
          not.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 crn: str = None,
                 account_id: str = None,
                 state: str = None,
                 default: bool = None) -> None:
        """
        Initialize a ResourceGroup object.

        :param str id: (optional) Resource Group ID.
        :param str name: (optional) Provider name, eg. IBM Passport Advantage.
        :param str crn: (optional) Provider CRN.
        :param str account_id: (optional) Account ID for this Resource Group.
        :param str state: (optional) State of this Resource Group.
        :param bool default: (optional) Indicates if this Resource Group is active
               or not.
        """
        self.id = id
        self.name = name
        self.crn = crn
        self.account_id = account_id
        self.state = state
        self.default = default

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceGroup':
        """Initialize a ResourceGroup object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'default' in _dict:
            args['default'] = _dict.get('default')
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
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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

class ResourceGroups():
    """
    Resource groups details.

    :attr int offset: (optional) The offset (origin 0) of the first resource in this
          page of search results.
    :attr int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :attr int total_count: (optional) The overall total number of resources in the
          search result set.
    :attr int resource_count: (optional) The number of resources returned in this
          page of search results.
    :attr str first: (optional) A URL for retrieving the first page of search
          results.
    :attr str last: (optional) A URL for retrieving the last page of search results.
    :attr str prev: (optional) A URL for retrieving the previous page of search
          results.
    :attr str next: (optional) A URL for retrieving the next page of search results.
    :attr List[ResourceGroup] resources: (optional) Resulting Resource Group
          objects.
    """

    def __init__(self,
                 *,
                 offset: int = None,
                 limit: int = None,
                 total_count: int = None,
                 resource_count: int = None,
                 first: str = None,
                 last: str = None,
                 prev: str = None,
                 next: str = None,
                 resources: List['ResourceGroup'] = None) -> None:
        """
        Initialize a ResourceGroups object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int total_count: (optional) The overall total number of resources in
               the search result set.
        :param int resource_count: (optional) The number of resources returned in
               this page of search results.
        :param str first: (optional) A URL for retrieving the first page of search
               results.
        :param str last: (optional) A URL for retrieving the last page of search
               results.
        :param str prev: (optional) A URL for retrieving the previous page of
               search results.
        :param str next: (optional) A URL for retrieving the next page of search
               results.
        :param List[ResourceGroup] resources: (optional) Resulting Resource Group
               objects.
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceGroups':
        """Initialize a ResourceGroups object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'resource_count' in _dict:
            args['resource_count'] = _dict.get('resource_count')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'last' in _dict:
            args['last'] = _dict.get('last')
        if 'prev' in _dict:
            args['prev'] = _dict.get('prev')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'resources' in _dict:
            args['resources'] = [ResourceGroup.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceGroups object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'resource_count') and self.resource_count is not None:
            _dict['resource_count'] = self.resource_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last
        if hasattr(self, 'prev') and self.prev is not None:
            _dict['prev'] = self.prev
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceGroups object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceGroups') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceGroups') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchematicsWorkspace():
    """
    Schematics workspace information.

    :attr str id: (optional) Workspace ID.
    :attr str name: (optional) Workspace name.
    :attr List[str] type: (optional) Workspace types.
    :attr str description: (optional) Workspace description.
    :attr List[str] tags: (optional) Workspace tags.
    :attr datetime created_at: (optional) Workspace creation date and time.
    :attr str created_by: (optional) Email address of user that created the ID.
    :attr str status: (optional) Workspace apply status.
    :attr SchematicsWorkspaceWorkspaceStatus workspace_status: (optional) Workspace
          frozen/locked status.
    :attr str template_ref: (optional) Template reference.
    :attr SchematicsWorkspaceTemplateRepo template_repo: (optional) Template
          repository.
    :attr List[object] template_data: (optional) Map of template data.
    :attr SchematicsWorkspaceRuntimeData runtime_data: (optional) Data describing
          runtime.
    :attr object shared_data: (optional) Map of shared data.
    :attr SchematicsWorkspaceCatalogRef catalog_ref: (optional) Catalog reference.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 type: List[str] = None,
                 description: str = None,
                 tags: List[str] = None,
                 created_at: datetime = None,
                 created_by: str = None,
                 status: str = None,
                 workspace_status: 'SchematicsWorkspaceWorkspaceStatus' = None,
                 template_ref: str = None,
                 template_repo: 'SchematicsWorkspaceTemplateRepo' = None,
                 template_data: List[object] = None,
                 runtime_data: 'SchematicsWorkspaceRuntimeData' = None,
                 shared_data: object = None,
                 catalog_ref: 'SchematicsWorkspaceCatalogRef' = None) -> None:
        """
        Initialize a SchematicsWorkspace object.

        :param str id: (optional) Workspace ID.
        :param str name: (optional) Workspace name.
        :param List[str] type: (optional) Workspace types.
        :param str description: (optional) Workspace description.
        :param List[str] tags: (optional) Workspace tags.
        :param datetime created_at: (optional) Workspace creation date and time.
        :param str created_by: (optional) Email address of user that created the
               ID.
        :param str status: (optional) Workspace apply status.
        :param SchematicsWorkspaceWorkspaceStatus workspace_status: (optional)
               Workspace frozen/locked status.
        :param str template_ref: (optional) Template reference.
        :param SchematicsWorkspaceTemplateRepo template_repo: (optional) Template
               repository.
        :param List[object] template_data: (optional) Map of template data.
        :param SchematicsWorkspaceRuntimeData runtime_data: (optional) Data
               describing runtime.
        :param object shared_data: (optional) Map of shared data.
        :param SchematicsWorkspaceCatalogRef catalog_ref: (optional) Catalog
               reference.
        """
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.tags = tags
        self.created_at = created_at
        self.created_by = created_by
        self.status = status
        self.workspace_status = workspace_status
        self.template_ref = template_ref
        self.template_repo = template_repo
        self.template_data = template_data
        self.runtime_data = runtime_data
        self.shared_data = shared_data
        self.catalog_ref = catalog_ref

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchematicsWorkspace':
        """Initialize a SchematicsWorkspace object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'workspace_status' in _dict:
            args['workspace_status'] = SchematicsWorkspaceWorkspaceStatus.from_dict(_dict.get('workspace_status'))
        if 'template_ref' in _dict:
            args['template_ref'] = _dict.get('template_ref')
        if 'template_repo' in _dict:
            args['template_repo'] = SchematicsWorkspaceTemplateRepo.from_dict(_dict.get('template_repo'))
        if 'template_data' in _dict:
            args['template_data'] = _dict.get('template_data')
        if 'runtime_data' in _dict:
            args['runtime_data'] = SchematicsWorkspaceRuntimeData.from_dict(_dict.get('runtime_data'))
        if 'shared_data' in _dict:
            args['shared_data'] = _dict.get('shared_data')
        if 'catalog_ref' in _dict:
            args['catalog_ref'] = SchematicsWorkspaceCatalogRef.from_dict(_dict.get('catalog_ref'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchematicsWorkspace object from a json dictionary."""
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
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'workspace_status') and self.workspace_status is not None:
            _dict['workspace_status'] = self.workspace_status.to_dict()
        if hasattr(self, 'template_ref') and self.template_ref is not None:
            _dict['template_ref'] = self.template_ref
        if hasattr(self, 'template_repo') and self.template_repo is not None:
            _dict['template_repo'] = self.template_repo.to_dict()
        if hasattr(self, 'template_data') and self.template_data is not None:
            _dict['template_data'] = self.template_data
        if hasattr(self, 'runtime_data') and self.runtime_data is not None:
            _dict['runtime_data'] = self.runtime_data.to_dict()
        if hasattr(self, 'shared_data') and self.shared_data is not None:
            _dict['shared_data'] = self.shared_data
        if hasattr(self, 'catalog_ref') and self.catalog_ref is not None:
            _dict['catalog_ref'] = self.catalog_ref.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchematicsWorkspace object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchematicsWorkspace') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchematicsWorkspace') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchematicsWorkspaceCatalogRef():
    """
    Catalog reference.

    :attr str item_id: (optional) Version locator ID.
    :attr str item_name: (optional) The name of the offering that generated this
          Blueprint.
    :attr str item_url: (optional) Relative Dashboard URL for content that generated
          this Blueprint.
    """

    def __init__(self,
                 *,
                 item_id: str = None,
                 item_name: str = None,
                 item_url: str = None) -> None:
        """
        Initialize a SchematicsWorkspaceCatalogRef object.

        :param str item_id: (optional) Version locator ID.
        :param str item_name: (optional) The name of the offering that generated
               this Blueprint.
        :param str item_url: (optional) Relative Dashboard URL for content that
               generated this Blueprint.
        """
        self.item_id = item_id
        self.item_name = item_name
        self.item_url = item_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchematicsWorkspaceCatalogRef':
        """Initialize a SchematicsWorkspaceCatalogRef object from a json dictionary."""
        args = {}
        if 'item_id' in _dict:
            args['item_id'] = _dict.get('item_id')
        if 'item_name' in _dict:
            args['item_name'] = _dict.get('item_name')
        if 'item_url' in _dict:
            args['item_url'] = _dict.get('item_url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchematicsWorkspaceCatalogRef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'item_id') and self.item_id is not None:
            _dict['item_id'] = self.item_id
        if hasattr(self, 'item_name') and self.item_name is not None:
            _dict['item_name'] = self.item_name
        if hasattr(self, 'item_url') and self.item_url is not None:
            _dict['item_url'] = self.item_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchematicsWorkspaceCatalogRef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchematicsWorkspaceCatalogRef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchematicsWorkspaceCatalogRef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchematicsWorkspaceRuntimeData():
    """
    Data describing runtime.

    :attr str id: (optional) Runtime ID.
    :attr str engine_name: (optional) Engine name.
    :attr str engine_version: (optional) Engine version.
    :attr str state_store_url: (optional) URL path to state store.
    :attr str log_store_url: (optional) URL path to log store.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 engine_name: str = None,
                 engine_version: str = None,
                 state_store_url: str = None,
                 log_store_url: str = None) -> None:
        """
        Initialize a SchematicsWorkspaceRuntimeData object.

        :param str id: (optional) Runtime ID.
        :param str engine_name: (optional) Engine name.
        :param str engine_version: (optional) Engine version.
        :param str state_store_url: (optional) URL path to state store.
        :param str log_store_url: (optional) URL path to log store.
        """
        self.id = id
        self.engine_name = engine_name
        self.engine_version = engine_version
        self.state_store_url = state_store_url
        self.log_store_url = log_store_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchematicsWorkspaceRuntimeData':
        """Initialize a SchematicsWorkspaceRuntimeData object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'engine_name' in _dict:
            args['engine_name'] = _dict.get('engine_name')
        if 'engine_version' in _dict:
            args['engine_version'] = _dict.get('engine_version')
        if 'state_store_url' in _dict:
            args['state_store_url'] = _dict.get('state_store_url')
        if 'log_store_url' in _dict:
            args['log_store_url'] = _dict.get('log_store_url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchematicsWorkspaceRuntimeData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'engine_name') and self.engine_name is not None:
            _dict['engine_name'] = self.engine_name
        if hasattr(self, 'engine_version') and self.engine_version is not None:
            _dict['engine_version'] = self.engine_version
        if hasattr(self, 'state_store_url') and self.state_store_url is not None:
            _dict['state_store_url'] = self.state_store_url
        if hasattr(self, 'log_store_url') and self.log_store_url is not None:
            _dict['log_store_url'] = self.log_store_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchematicsWorkspaceRuntimeData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchematicsWorkspaceRuntimeData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchematicsWorkspaceRuntimeData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchematicsWorkspaceSearchResult():
    """
    Result of schematics workspace search.

    :attr int offset: (optional) The offset (origin 0) of the first resource in this
          page of search results.
    :attr int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :attr int total_count: (optional) The overall total number of resources in the
          search result set.
    :attr int resource_count: (optional) The number of resources returned in this
          page of search results.
    :attr str first: (optional) A URL for retrieving the first page of search
          results.
    :attr str last: (optional) A URL for retrieving the last page of search results.
    :attr str prev: (optional) A URL for retrieving the previous page of search
          results.
    :attr str next: (optional) A URL for retrieving the next page of search results.
    :attr List[SchematicsWorkspace] resources: (optional) Resulting objects.
    """

    def __init__(self,
                 *,
                 offset: int = None,
                 limit: int = None,
                 total_count: int = None,
                 resource_count: int = None,
                 first: str = None,
                 last: str = None,
                 prev: str = None,
                 next: str = None,
                 resources: List['SchematicsWorkspace'] = None) -> None:
        """
        Initialize a SchematicsWorkspaceSearchResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int total_count: (optional) The overall total number of resources in
               the search result set.
        :param int resource_count: (optional) The number of resources returned in
               this page of search results.
        :param str first: (optional) A URL for retrieving the first page of search
               results.
        :param str last: (optional) A URL for retrieving the last page of search
               results.
        :param str prev: (optional) A URL for retrieving the previous page of
               search results.
        :param str next: (optional) A URL for retrieving the next page of search
               results.
        :param List[SchematicsWorkspace] resources: (optional) Resulting objects.
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchematicsWorkspaceSearchResult':
        """Initialize a SchematicsWorkspaceSearchResult object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'resource_count' in _dict:
            args['resource_count'] = _dict.get('resource_count')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'last' in _dict:
            args['last'] = _dict.get('last')
        if 'prev' in _dict:
            args['prev'] = _dict.get('prev')
        if 'next' in _dict:
            args['next'] = _dict.get('next')
        if 'resources' in _dict:
            args['resources'] = [SchematicsWorkspace.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchematicsWorkspaceSearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'resource_count') and self.resource_count is not None:
            _dict['resource_count'] = self.resource_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last
        if hasattr(self, 'prev') and self.prev is not None:
            _dict['prev'] = self.prev
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchematicsWorkspaceSearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchematicsWorkspaceSearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchematicsWorkspaceSearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchematicsWorkspaceTemplateRepo():
    """
    Template repository.

    :attr str repo_url: (optional) The fully qualified path of the tgz used in the
          deploy.
    :attr str chart_name: (optional) Name of chart.
    :attr str script_name: (optional) Name of script.
    :attr str uninstall_script_name: (optional) Name of uninstall script.
    :attr str folder_name: (optional) Name of folder.
    :attr str repo_sha_value: (optional) Digest of project.
    """

    def __init__(self,
                 *,
                 repo_url: str = None,
                 chart_name: str = None,
                 script_name: str = None,
                 uninstall_script_name: str = None,
                 folder_name: str = None,
                 repo_sha_value: str = None) -> None:
        """
        Initialize a SchematicsWorkspaceTemplateRepo object.

        :param str repo_url: (optional) The fully qualified path of the tgz used in
               the deploy.
        :param str chart_name: (optional) Name of chart.
        :param str script_name: (optional) Name of script.
        :param str uninstall_script_name: (optional) Name of uninstall script.
        :param str folder_name: (optional) Name of folder.
        :param str repo_sha_value: (optional) Digest of project.
        """
        self.repo_url = repo_url
        self.chart_name = chart_name
        self.script_name = script_name
        self.uninstall_script_name = uninstall_script_name
        self.folder_name = folder_name
        self.repo_sha_value = repo_sha_value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchematicsWorkspaceTemplateRepo':
        """Initialize a SchematicsWorkspaceTemplateRepo object from a json dictionary."""
        args = {}
        if 'repo_url' in _dict:
            args['repo_url'] = _dict.get('repo_url')
        if 'chart_name' in _dict:
            args['chart_name'] = _dict.get('chart_name')
        if 'script_name' in _dict:
            args['script_name'] = _dict.get('script_name')
        if 'uninstall_script_name' in _dict:
            args['uninstall_script_name'] = _dict.get('uninstall_script_name')
        if 'folder_name' in _dict:
            args['folder_name'] = _dict.get('folder_name')
        if 'repo_sha_value' in _dict:
            args['repo_sha_value'] = _dict.get('repo_sha_value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchematicsWorkspaceTemplateRepo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'repo_url') and self.repo_url is not None:
            _dict['repo_url'] = self.repo_url
        if hasattr(self, 'chart_name') and self.chart_name is not None:
            _dict['chart_name'] = self.chart_name
        if hasattr(self, 'script_name') and self.script_name is not None:
            _dict['script_name'] = self.script_name
        if hasattr(self, 'uninstall_script_name') and self.uninstall_script_name is not None:
            _dict['uninstall_script_name'] = self.uninstall_script_name
        if hasattr(self, 'folder_name') and self.folder_name is not None:
            _dict['folder_name'] = self.folder_name
        if hasattr(self, 'repo_sha_value') and self.repo_sha_value is not None:
            _dict['repo_sha_value'] = self.repo_sha_value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchematicsWorkspaceTemplateRepo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchematicsWorkspaceTemplateRepo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchematicsWorkspaceTemplateRepo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchematicsWorkspaceWorkspaceStatus():
    """
    Workspace frozen/locked status.

    :attr bool frozen: (optional) Workspace frozen state.
    :attr bool locked: (optional) Workspace locked state.
    """

    def __init__(self,
                 *,
                 frozen: bool = None,
                 locked: bool = None) -> None:
        """
        Initialize a SchematicsWorkspaceWorkspaceStatus object.

        :param bool frozen: (optional) Workspace frozen state.
        :param bool locked: (optional) Workspace locked state.
        """
        self.frozen = frozen
        self.locked = locked

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchematicsWorkspaceWorkspaceStatus':
        """Initialize a SchematicsWorkspaceWorkspaceStatus object from a json dictionary."""
        args = {}
        if 'frozen' in _dict:
            args['frozen'] = _dict.get('frozen')
        if 'locked' in _dict:
            args['locked'] = _dict.get('locked')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchematicsWorkspaceWorkspaceStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'frozen') and self.frozen is not None:
            _dict['frozen'] = self.frozen
        if hasattr(self, 'locked') and self.locked is not None:
            _dict['locked'] = self.locked
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchematicsWorkspaceWorkspaceStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchematicsWorkspaceWorkspaceStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchematicsWorkspaceWorkspaceStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Script():
    """
    Script information.

    :attr str instructions: (optional) Instruction on step and by whom (role) that
          are needed to take place to prepare the target for installing this version.
    :attr str script: (optional) Optional script that needs to be run post any
          pre-condition script.
    :attr str script_permission: (optional) Optional iam permissions that are
          required on the target cluster to run this script.
    :attr str delete_script: (optional) Optional script that if run will remove the
          installed version.
    :attr str scope: (optional) Optional value indicating if this script is scoped
          to a namespace or the entire cluster.
    """

    def __init__(self,
                 *,
                 instructions: str = None,
                 script: str = None,
                 script_permission: str = None,
                 delete_script: str = None,
                 scope: str = None) -> None:
        """
        Initialize a Script object.

        :param str instructions: (optional) Instruction on step and by whom (role)
               that are needed to take place to prepare the target for installing this
               version.
        :param str script: (optional) Optional script that needs to be run post any
               pre-condition script.
        :param str script_permission: (optional) Optional iam permissions that are
               required on the target cluster to run this script.
        :param str delete_script: (optional) Optional script that if run will
               remove the installed version.
        :param str scope: (optional) Optional value indicating if this script is
               scoped to a namespace or the entire cluster.
        """
        self.instructions = instructions
        self.script = script
        self.script_permission = script_permission
        self.delete_script = delete_script
        self.scope = scope

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Script':
        """Initialize a Script object from a json dictionary."""
        args = {}
        if 'instructions' in _dict:
            args['instructions'] = _dict.get('instructions')
        if 'script' in _dict:
            args['script'] = _dict.get('script')
        if 'script_permission' in _dict:
            args['script_permission'] = _dict.get('script_permission')
        if 'delete_script' in _dict:
            args['delete_script'] = _dict.get('delete_script')
        if 'scope' in _dict:
            args['scope'] = _dict.get('scope')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Script object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instructions') and self.instructions is not None:
            _dict['instructions'] = self.instructions
        if hasattr(self, 'script') and self.script is not None:
            _dict['script'] = self.script
        if hasattr(self, 'script_permission') and self.script_permission is not None:
            _dict['script_permission'] = self.script_permission
        if hasattr(self, 'delete_script') and self.delete_script is not None:
            _dict['delete_script'] = self.delete_script
        if hasattr(self, 'scope') and self.scope is not None:
            _dict['scope'] = self.scope
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Script object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Script') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Script') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class State():
    """
    Offering state.

    :attr str current: (optional) one of: new, validated, account-published,
          ibm-published, public-published.
    :attr datetime current_entered: (optional) Date and time of current request.
    :attr str pending: (optional) one of: new, validated, account-published,
          ibm-published, public-published.
    :attr datetime pending_requested: (optional) Date and time of pending request.
    :attr str previous: (optional) one of: new, validated, account-published,
          ibm-published, public-published.
    """

    def __init__(self,
                 *,
                 current: str = None,
                 current_entered: datetime = None,
                 pending: str = None,
                 pending_requested: datetime = None,
                 previous: str = None) -> None:
        """
        Initialize a State object.

        :param str current: (optional) one of: new, validated, account-published,
               ibm-published, public-published.
        :param datetime current_entered: (optional) Date and time of current
               request.
        :param str pending: (optional) one of: new, validated, account-published,
               ibm-published, public-published.
        :param datetime pending_requested: (optional) Date and time of pending
               request.
        :param str previous: (optional) one of: new, validated, account-published,
               ibm-published, public-published.
        """
        self.current = current
        self.current_entered = current_entered
        self.pending = pending
        self.pending_requested = pending_requested
        self.previous = previous

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'State':
        """Initialize a State object from a json dictionary."""
        args = {}
        if 'current' in _dict:
            args['current'] = _dict.get('current')
        if 'current_entered' in _dict:
            args['current_entered'] = string_to_datetime(_dict.get('current_entered'))
        if 'pending' in _dict:
            args['pending'] = _dict.get('pending')
        if 'pending_requested' in _dict:
            args['pending_requested'] = string_to_datetime(_dict.get('pending_requested'))
        if 'previous' in _dict:
            args['previous'] = _dict.get('previous')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a State object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'current') and self.current is not None:
            _dict['current'] = self.current
        if hasattr(self, 'current_entered') and self.current_entered is not None:
            _dict['current_entered'] = datetime_to_string(self.current_entered)
        if hasattr(self, 'pending') and self.pending is not None:
            _dict['pending'] = self.pending
        if hasattr(self, 'pending_requested') and self.pending_requested is not None:
            _dict['pending_requested'] = datetime_to_string(self.pending_requested)
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this State object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'State') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'State') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SyndicationAuthorization():
    """
    Feature information.

    :attr str token: (optional) Array of syndicated namespaces.
    :attr datetime last_run: (optional) Date and time last updated.
    """

    def __init__(self,
                 *,
                 token: str = None,
                 last_run: datetime = None) -> None:
        """
        Initialize a SyndicationAuthorization object.

        :param str token: (optional) Array of syndicated namespaces.
        :param datetime last_run: (optional) Date and time last updated.
        """
        self.token = token
        self.last_run = last_run

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyndicationAuthorization':
        """Initialize a SyndicationAuthorization object from a json dictionary."""
        args = {}
        if 'token' in _dict:
            args['token'] = _dict.get('token')
        if 'last_run' in _dict:
            args['last_run'] = string_to_datetime(_dict.get('last_run'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyndicationAuthorization object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'token') and self.token is not None:
            _dict['token'] = self.token
        if hasattr(self, 'last_run') and self.last_run is not None:
            _dict['last_run'] = datetime_to_string(self.last_run)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyndicationAuthorization object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SyndicationAuthorization') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyndicationAuthorization') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SyndicationCluster():
    """
    Feature information.

    :attr str region: (optional) Cluster region.
    :attr str id: (optional) Cluster ID.
    :attr str name: (optional) Cluster name.
    :attr str resource_group_name: (optional) Resource group ID.
    :attr str type: (optional) Syndication type.
    :attr List[str] namespaces: (optional) Syndicated namespaces.
    :attr bool all_namespaces: (optional) Syndicated to all namespaces on cluster.
    """

    def __init__(self,
                 *,
                 region: str = None,
                 id: str = None,
                 name: str = None,
                 resource_group_name: str = None,
                 type: str = None,
                 namespaces: List[str] = None,
                 all_namespaces: bool = None) -> None:
        """
        Initialize a SyndicationCluster object.

        :param str region: (optional) Cluster region.
        :param str id: (optional) Cluster ID.
        :param str name: (optional) Cluster name.
        :param str resource_group_name: (optional) Resource group ID.
        :param str type: (optional) Syndication type.
        :param List[str] namespaces: (optional) Syndicated namespaces.
        :param bool all_namespaces: (optional) Syndicated to all namespaces on
               cluster.
        """
        self.region = region
        self.id = id
        self.name = name
        self.resource_group_name = resource_group_name
        self.type = type
        self.namespaces = namespaces
        self.all_namespaces = all_namespaces

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyndicationCluster':
        """Initialize a SyndicationCluster object from a json dictionary."""
        args = {}
        if 'region' in _dict:
            args['region'] = _dict.get('region')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'resource_group_name' in _dict:
            args['resource_group_name'] = _dict.get('resource_group_name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'namespaces' in _dict:
            args['namespaces'] = _dict.get('namespaces')
        if 'all_namespaces' in _dict:
            args['all_namespaces'] = _dict.get('all_namespaces')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyndicationCluster object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'resource_group_name') and self.resource_group_name is not None:
            _dict['resource_group_name'] = self.resource_group_name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'namespaces') and self.namespaces is not None:
            _dict['namespaces'] = self.namespaces
        if hasattr(self, 'all_namespaces') and self.all_namespaces is not None:
            _dict['all_namespaces'] = self.all_namespaces
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyndicationCluster object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SyndicationCluster') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyndicationCluster') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SyndicationHistory():
    """
    Feature information.

    :attr List[str] namespaces: (optional) Array of syndicated namespaces.
    :attr List[SyndicationCluster] clusters: (optional) Array of syndicated
          namespaces.
    :attr datetime last_run: (optional) Date and time last syndicated.
    """

    def __init__(self,
                 *,
                 namespaces: List[str] = None,
                 clusters: List['SyndicationCluster'] = None,
                 last_run: datetime = None) -> None:
        """
        Initialize a SyndicationHistory object.

        :param List[str] namespaces: (optional) Array of syndicated namespaces.
        :param List[SyndicationCluster] clusters: (optional) Array of syndicated
               namespaces.
        :param datetime last_run: (optional) Date and time last syndicated.
        """
        self.namespaces = namespaces
        self.clusters = clusters
        self.last_run = last_run

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyndicationHistory':
        """Initialize a SyndicationHistory object from a json dictionary."""
        args = {}
        if 'namespaces' in _dict:
            args['namespaces'] = _dict.get('namespaces')
        if 'clusters' in _dict:
            args['clusters'] = [SyndicationCluster.from_dict(x) for x in _dict.get('clusters')]
        if 'last_run' in _dict:
            args['last_run'] = string_to_datetime(_dict.get('last_run'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyndicationHistory object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'namespaces') and self.namespaces is not None:
            _dict['namespaces'] = self.namespaces
        if hasattr(self, 'clusters') and self.clusters is not None:
            _dict['clusters'] = [x.to_dict() for x in self.clusters]
        if hasattr(self, 'last_run') and self.last_run is not None:
            _dict['last_run'] = datetime_to_string(self.last_run)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyndicationHistory object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SyndicationHistory') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyndicationHistory') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SyndicationResource():
    """
    Feature information.

    :attr bool remove_related_components: (optional) Remove related components.
    :attr List[SyndicationCluster] clusters: (optional) Syndication clusters.
    :attr SyndicationHistory history: (optional) Feature information.
    :attr SyndicationAuthorization authorization: (optional) Feature information.
    """

    def __init__(self,
                 *,
                 remove_related_components: bool = None,
                 clusters: List['SyndicationCluster'] = None,
                 history: 'SyndicationHistory' = None,
                 authorization: 'SyndicationAuthorization' = None) -> None:
        """
        Initialize a SyndicationResource object.

        :param bool remove_related_components: (optional) Remove related
               components.
        :param List[SyndicationCluster] clusters: (optional) Syndication clusters.
        :param SyndicationHistory history: (optional) Feature information.
        :param SyndicationAuthorization authorization: (optional) Feature
               information.
        """
        self.remove_related_components = remove_related_components
        self.clusters = clusters
        self.history = history
        self.authorization = authorization

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyndicationResource':
        """Initialize a SyndicationResource object from a json dictionary."""
        args = {}
        if 'remove_related_components' in _dict:
            args['remove_related_components'] = _dict.get('remove_related_components')
        if 'clusters' in _dict:
            args['clusters'] = [SyndicationCluster.from_dict(x) for x in _dict.get('clusters')]
        if 'history' in _dict:
            args['history'] = SyndicationHistory.from_dict(_dict.get('history'))
        if 'authorization' in _dict:
            args['authorization'] = SyndicationAuthorization.from_dict(_dict.get('authorization'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyndicationResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'remove_related_components') and self.remove_related_components is not None:
            _dict['remove_related_components'] = self.remove_related_components
        if hasattr(self, 'clusters') and self.clusters is not None:
            _dict['clusters'] = [x.to_dict() for x in self.clusters]
        if hasattr(self, 'history') and self.history is not None:
            _dict['history'] = self.history.to_dict()
        if hasattr(self, 'authorization') and self.authorization is not None:
            _dict['authorization'] = self.authorization.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyndicationResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SyndicationResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyndicationResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Validation():
    """
    Validation response.

    :attr datetime validated: (optional) Date and time of last successful
          validation.
    :attr datetime requested: (optional) Date and time of last validation was
          requested.
    :attr str state: (optional) Current validation state - <empty>, in_progress,
          valid, invalid, expired.
    :attr str last_operation: (optional) Last operation (e.g. submit_deployment,
          generate_installer, install_offering.
    :attr object target: (optional) Validation target information (e.g. cluster_id,
          region, namespace, etc).  Values will vary by Content type.
    """

    def __init__(self,
                 *,
                 validated: datetime = None,
                 requested: datetime = None,
                 state: str = None,
                 last_operation: str = None,
                 target: object = None) -> None:
        """
        Initialize a Validation object.

        :param datetime validated: (optional) Date and time of last successful
               validation.
        :param datetime requested: (optional) Date and time of last validation was
               requested.
        :param str state: (optional) Current validation state - <empty>,
               in_progress, valid, invalid, expired.
        :param str last_operation: (optional) Last operation (e.g.
               submit_deployment, generate_installer, install_offering.
        :param object target: (optional) Validation target information (e.g.
               cluster_id, region, namespace, etc).  Values will vary by Content type.
        """
        self.validated = validated
        self.requested = requested
        self.state = state
        self.last_operation = last_operation
        self.target = target

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Validation':
        """Initialize a Validation object from a json dictionary."""
        args = {}
        if 'validated' in _dict:
            args['validated'] = string_to_datetime(_dict.get('validated'))
        if 'requested' in _dict:
            args['requested'] = string_to_datetime(_dict.get('requested'))
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'last_operation' in _dict:
            args['last_operation'] = _dict.get('last_operation')
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Validation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'validated') and self.validated is not None:
            _dict['validated'] = datetime_to_string(self.validated)
        if hasattr(self, 'requested') and self.requested is not None:
            _dict['requested'] = datetime_to_string(self.requested)
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'last_operation') and self.last_operation is not None:
            _dict['last_operation'] = self.last_operation
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Validation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Validation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Validation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Version():
    """
    Offering version information.

    :attr str id: (optional) Unique ID.
    :attr str rev: (optional) Cloudant revision.
    :attr str crn: (optional) Version's CRN.
    :attr str version: (optional) Version of content type.
    :attr str sha: (optional) hash of the content.
    :attr datetime created: (optional) The date and time this version was created.
    :attr datetime updated: (optional) The date and time this version was last
          updated.
    :attr str offering_id: (optional) Offering ID.
    :attr str catalog_id: (optional) Catalog ID.
    :attr str kind_id: (optional) Kind ID.
    :attr List[str] tags: (optional) List of tags associated with this catalog.
    :attr str repo_url: (optional) Content's repo URL.
    :attr str source_url: (optional) Content's source URL (e.g git repo).
    :attr str tgz_url: (optional) File used to on-board this version.
    :attr List[Configuration] configuration: (optional) List of user solicited
          overrides.
    :attr object metadata: (optional) Open ended metadata information.
    :attr Validation validation: (optional) Validation response.
    :attr List[Resource] required_resources: (optional) Resource requirments for
          installation.
    :attr bool single_instance: (optional) Denotes if single instance can be
          deployed to a given cluster.
    :attr Script install: (optional) Script information.
    :attr List[Script] pre_install: (optional) Optional pre-install instructions.
    :attr VersionEntitlement entitlement: (optional) Entitlement license info.
    :attr List[License] licenses: (optional) List of licenses the product was built
          with.
    :attr str image_manifest_url: (optional) If set, denotes a url to a YAML file
          with list of container images used by this version.
    :attr bool deprecated: (optional) read only field, indicating if this version is
          deprecated.
    :attr str package_version: (optional) Version of the package used to create this
          version.
    :attr State state: (optional) Offering state.
    :attr str version_locator: (optional) A dotted value of `catalogID`.`versionID`.
    :attr str console_url: (optional) Console URL.
    :attr str long_description: (optional) Long description for version.
    :attr List[str] whitelisted_accounts: (optional) Whitelisted accounts for
          version.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 rev: str = None,
                 crn: str = None,
                 version: str = None,
                 sha: str = None,
                 created: datetime = None,
                 updated: datetime = None,
                 offering_id: str = None,
                 catalog_id: str = None,
                 kind_id: str = None,
                 tags: List[str] = None,
                 repo_url: str = None,
                 source_url: str = None,
                 tgz_url: str = None,
                 configuration: List['Configuration'] = None,
                 metadata: object = None,
                 validation: 'Validation' = None,
                 required_resources: List['Resource'] = None,
                 single_instance: bool = None,
                 install: 'Script' = None,
                 pre_install: List['Script'] = None,
                 entitlement: 'VersionEntitlement' = None,
                 licenses: List['License'] = None,
                 image_manifest_url: str = None,
                 deprecated: bool = None,
                 package_version: str = None,
                 state: 'State' = None,
                 version_locator: str = None,
                 console_url: str = None,
                 long_description: str = None,
                 whitelisted_accounts: List[str] = None) -> None:
        """
        Initialize a Version object.

        :param str id: (optional) Unique ID.
        :param str rev: (optional) Cloudant revision.
        :param str crn: (optional) Version's CRN.
        :param str version: (optional) Version of content type.
        :param str sha: (optional) hash of the content.
        :param datetime created: (optional) The date and time this version was
               created.
        :param datetime updated: (optional) The date and time this version was last
               updated.
        :param str offering_id: (optional) Offering ID.
        :param str catalog_id: (optional) Catalog ID.
        :param str kind_id: (optional) Kind ID.
        :param List[str] tags: (optional) List of tags associated with this
               catalog.
        :param str repo_url: (optional) Content's repo URL.
        :param str source_url: (optional) Content's source URL (e.g git repo).
        :param str tgz_url: (optional) File used to on-board this version.
        :param List[Configuration] configuration: (optional) List of user solicited
               overrides.
        :param object metadata: (optional) Open ended metadata information.
        :param Validation validation: (optional) Validation response.
        :param List[Resource] required_resources: (optional) Resource requirments
               for installation.
        :param bool single_instance: (optional) Denotes if single instance can be
               deployed to a given cluster.
        :param Script install: (optional) Script information.
        :param List[Script] pre_install: (optional) Optional pre-install
               instructions.
        :param VersionEntitlement entitlement: (optional) Entitlement license info.
        :param List[License] licenses: (optional) List of licenses the product was
               built with.
        :param str image_manifest_url: (optional) If set, denotes a url to a YAML
               file with list of container images used by this version.
        :param bool deprecated: (optional) read only field, indicating if this
               version is deprecated.
        :param str package_version: (optional) Version of the package used to
               create this version.
        :param State state: (optional) Offering state.
        :param str version_locator: (optional) A dotted value of
               `catalogID`.`versionID`.
        :param str console_url: (optional) Console URL.
        :param str long_description: (optional) Long description for version.
        :param List[str] whitelisted_accounts: (optional) Whitelisted accounts for
               version.
        """
        self.id = id
        self.rev = rev
        self.crn = crn
        self.version = version
        self.sha = sha
        self.created = created
        self.updated = updated
        self.offering_id = offering_id
        self.catalog_id = catalog_id
        self.kind_id = kind_id
        self.tags = tags
        self.repo_url = repo_url
        self.source_url = source_url
        self.tgz_url = tgz_url
        self.configuration = configuration
        self.metadata = metadata
        self.validation = validation
        self.required_resources = required_resources
        self.single_instance = single_instance
        self.install = install
        self.pre_install = pre_install
        self.entitlement = entitlement
        self.licenses = licenses
        self.image_manifest_url = image_manifest_url
        self.deprecated = deprecated
        self.package_version = package_version
        self.state = state
        self.version_locator = version_locator
        self.console_url = console_url
        self.long_description = long_description
        self.whitelisted_accounts = whitelisted_accounts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Version':
        """Initialize a Version object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if '_rev' in _dict:
            args['rev'] = _dict.get('_rev')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'sha' in _dict:
            args['sha'] = _dict.get('sha')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'offering_id' in _dict:
            args['offering_id'] = _dict.get('offering_id')
        if 'catalog_id' in _dict:
            args['catalog_id'] = _dict.get('catalog_id')
        if 'kind_id' in _dict:
            args['kind_id'] = _dict.get('kind_id')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'repo_url' in _dict:
            args['repo_url'] = _dict.get('repo_url')
        if 'source_url' in _dict:
            args['source_url'] = _dict.get('source_url')
        if 'tgz_url' in _dict:
            args['tgz_url'] = _dict.get('tgz_url')
        if 'configuration' in _dict:
            args['configuration'] = [Configuration.from_dict(x) for x in _dict.get('configuration')]
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'validation' in _dict:
            args['validation'] = Validation.from_dict(_dict.get('validation'))
        if 'required_resources' in _dict:
            args['required_resources'] = [Resource.from_dict(x) for x in _dict.get('required_resources')]
        if 'single_instance' in _dict:
            args['single_instance'] = _dict.get('single_instance')
        if 'install' in _dict:
            args['install'] = Script.from_dict(_dict.get('install'))
        if 'pre_install' in _dict:
            args['pre_install'] = [Script.from_dict(x) for x in _dict.get('pre_install')]
        if 'entitlement' in _dict:
            args['entitlement'] = VersionEntitlement.from_dict(_dict.get('entitlement'))
        if 'licenses' in _dict:
            args['licenses'] = [License.from_dict(x) for x in _dict.get('licenses')]
        if 'image_manifest_url' in _dict:
            args['image_manifest_url'] = _dict.get('image_manifest_url')
        if 'deprecated' in _dict:
            args['deprecated'] = _dict.get('deprecated')
        if 'package_version' in _dict:
            args['package_version'] = _dict.get('package_version')
        if 'state' in _dict:
            args['state'] = State.from_dict(_dict.get('state'))
        if 'version_locator' in _dict:
            args['version_locator'] = _dict.get('version_locator')
        if 'console_url' in _dict:
            args['console_url'] = _dict.get('console_url')
        if 'long_description' in _dict:
            args['long_description'] = _dict.get('long_description')
        if 'whitelisted_accounts' in _dict:
            args['whitelisted_accounts'] = _dict.get('whitelisted_accounts')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Version object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['_rev'] = self.rev
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'sha') and self.sha is not None:
            _dict['sha'] = self.sha
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'offering_id') and self.offering_id is not None:
            _dict['offering_id'] = self.offering_id
        if hasattr(self, 'catalog_id') and self.catalog_id is not None:
            _dict['catalog_id'] = self.catalog_id
        if hasattr(self, 'kind_id') and self.kind_id is not None:
            _dict['kind_id'] = self.kind_id
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'repo_url') and self.repo_url is not None:
            _dict['repo_url'] = self.repo_url
        if hasattr(self, 'source_url') and self.source_url is not None:
            _dict['source_url'] = self.source_url
        if hasattr(self, 'tgz_url') and self.tgz_url is not None:
            _dict['tgz_url'] = self.tgz_url
        if hasattr(self, 'configuration') and self.configuration is not None:
            _dict['configuration'] = [x.to_dict() for x in self.configuration]
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'validation') and self.validation is not None:
            _dict['validation'] = self.validation.to_dict()
        if hasattr(self, 'required_resources') and self.required_resources is not None:
            _dict['required_resources'] = [x.to_dict() for x in self.required_resources]
        if hasattr(self, 'single_instance') and self.single_instance is not None:
            _dict['single_instance'] = self.single_instance
        if hasattr(self, 'install') and self.install is not None:
            _dict['install'] = self.install.to_dict()
        if hasattr(self, 'pre_install') and self.pre_install is not None:
            _dict['pre_install'] = [x.to_dict() for x in self.pre_install]
        if hasattr(self, 'entitlement') and self.entitlement is not None:
            _dict['entitlement'] = self.entitlement.to_dict()
        if hasattr(self, 'licenses') and self.licenses is not None:
            _dict['licenses'] = [x.to_dict() for x in self.licenses]
        if hasattr(self, 'image_manifest_url') and self.image_manifest_url is not None:
            _dict['image_manifest_url'] = self.image_manifest_url
        if hasattr(self, 'deprecated') and self.deprecated is not None:
            _dict['deprecated'] = self.deprecated
        if hasattr(self, 'package_version') and self.package_version is not None:
            _dict['package_version'] = self.package_version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state.to_dict()
        if hasattr(self, 'version_locator') and self.version_locator is not None:
            _dict['version_locator'] = self.version_locator
        if hasattr(self, 'console_url') and self.console_url is not None:
            _dict['console_url'] = self.console_url
        if hasattr(self, 'long_description') and self.long_description is not None:
            _dict['long_description'] = self.long_description
        if hasattr(self, 'whitelisted_accounts') and self.whitelisted_accounts is not None:
            _dict['whitelisted_accounts'] = self.whitelisted_accounts
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Version object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Version') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Version') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class VersionEntitlement():
    """
    Entitlement license info.

    :attr str provider_name: (optional) Provider name.
    :attr str provider_id: (optional) Provider ID.
    :attr str product_id: (optional) Product ID.
    :attr List[str] part_numbers: (optional) list of license entitlement part
          numbers, eg. D1YGZLL,D1ZXILL.
    :attr str image_repo_name: (optional) Image repository name.
    """

    def __init__(self,
                 *,
                 provider_name: str = None,
                 provider_id: str = None,
                 product_id: str = None,
                 part_numbers: List[str] = None,
                 image_repo_name: str = None) -> None:
        """
        Initialize a VersionEntitlement object.

        :param str provider_name: (optional) Provider name.
        :param str provider_id: (optional) Provider ID.
        :param str product_id: (optional) Product ID.
        :param List[str] part_numbers: (optional) list of license entitlement part
               numbers, eg. D1YGZLL,D1ZXILL.
        :param str image_repo_name: (optional) Image repository name.
        """
        self.provider_name = provider_name
        self.provider_id = provider_id
        self.product_id = product_id
        self.part_numbers = part_numbers
        self.image_repo_name = image_repo_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VersionEntitlement':
        """Initialize a VersionEntitlement object from a json dictionary."""
        args = {}
        if 'provider_name' in _dict:
            args['provider_name'] = _dict.get('provider_name')
        if 'provider_id' in _dict:
            args['provider_id'] = _dict.get('provider_id')
        if 'product_id' in _dict:
            args['product_id'] = _dict.get('product_id')
        if 'part_numbers' in _dict:
            args['part_numbers'] = _dict.get('part_numbers')
        if 'image_repo_name' in _dict:
            args['image_repo_name'] = _dict.get('image_repo_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VersionEntitlement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider_name') and self.provider_name is not None:
            _dict['provider_name'] = self.provider_name
        if hasattr(self, 'provider_id') and self.provider_id is not None:
            _dict['provider_id'] = self.provider_id
        if hasattr(self, 'product_id') and self.product_id is not None:
            _dict['product_id'] = self.product_id
        if hasattr(self, 'part_numbers') and self.part_numbers is not None:
            _dict['part_numbers'] = self.part_numbers
        if hasattr(self, 'image_repo_name') and self.image_repo_name is not None:
            _dict['image_repo_name'] = self.image_repo_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VersionEntitlement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VersionEntitlement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VersionEntitlement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class VersionUpdateDescriptor():
    """
    Indicates if the current version can be upgraded to the version identified by the
    descriptor.

    :attr str version_locator: (optional) A dotted value of `catalogID`.`versionID`.
    :attr str version: (optional) the version number of this version.
    :attr State state: (optional) Offering state.
    :attr List[Resource] required_resources: (optional) Resource requirments for
          installation.
    :attr str package_version: (optional) Version of package.
    :attr bool can_update: (optional) true if the current version can be upgraded to
          this version, false otherwise.
    :attr object messages: (optional) If can_update is false, this map will contain
          messages for each failed check, otherwise it will be omitted.  Possible keys
          include nodes, cores, mem, disk, targetVersion, and install-permission-check.
    """

    def __init__(self,
                 *,
                 version_locator: str = None,
                 version: str = None,
                 state: 'State' = None,
                 required_resources: List['Resource'] = None,
                 package_version: str = None,
                 can_update: bool = None,
                 messages: object = None) -> None:
        """
        Initialize a VersionUpdateDescriptor object.

        :param str version_locator: (optional) A dotted value of
               `catalogID`.`versionID`.
        :param str version: (optional) the version number of this version.
        :param State state: (optional) Offering state.
        :param List[Resource] required_resources: (optional) Resource requirments
               for installation.
        :param str package_version: (optional) Version of package.
        :param bool can_update: (optional) true if the current version can be
               upgraded to this version, false otherwise.
        :param object messages: (optional) If can_update is false, this map will
               contain messages for each failed check, otherwise it will be omitted.
               Possible keys include nodes, cores, mem, disk, targetVersion, and
               install-permission-check.
        """
        self.version_locator = version_locator
        self.version = version
        self.state = state
        self.required_resources = required_resources
        self.package_version = package_version
        self.can_update = can_update
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VersionUpdateDescriptor':
        """Initialize a VersionUpdateDescriptor object from a json dictionary."""
        args = {}
        if 'version_locator' in _dict:
            args['version_locator'] = _dict.get('version_locator')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'state' in _dict:
            args['state'] = State.from_dict(_dict.get('state'))
        if 'required_resources' in _dict:
            args['required_resources'] = [Resource.from_dict(x) for x in _dict.get('required_resources')]
        if 'package_version' in _dict:
            args['package_version'] = _dict.get('package_version')
        if 'can_update' in _dict:
            args['can_update'] = _dict.get('can_update')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VersionUpdateDescriptor object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version_locator') and self.version_locator is not None:
            _dict['version_locator'] = self.version_locator
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state.to_dict()
        if hasattr(self, 'required_resources') and self.required_resources is not None:
            _dict['required_resources'] = [x.to_dict() for x in self.required_resources]
        if hasattr(self, 'package_version') and self.package_version is not None:
            _dict['package_version'] = self.package_version
        if hasattr(self, 'can_update') and self.can_update is not None:
            _dict['can_update'] = self.can_update
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VersionUpdateDescriptor object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VersionUpdateDescriptor') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VersionUpdateDescriptor') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
