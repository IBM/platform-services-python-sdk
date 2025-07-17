# coding: utf-8

# (C) Copyright IBM Corp. 2025.
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

# IBM OpenAPI SDK Code Generator Version: 3.106.0-09823488-20250707-071701

"""
The catalog service manages offerings across geographies as the system of record. The
catalog supports a RESTful API where users can retrieve information about existing
offerings and create, manage, and delete their offerings. Start with the base URL and use
the endpoints to retrieve metadata about services in the catalog and manage service
visbility. Depending on the kind of object, the metadata can include information about
pricing, provisioning, regions, and more. For more information, see the [catalog
documentation](https://cloud.ibm.com/docs/overview/catalog.html#global-catalog-overview).

API Version: 1.0.3
"""

from datetime import datetime
from enum import Enum
from typing import BinaryIO, Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class GlobalCatalogV1(BaseService):
    """The Global Catalog V1 service."""

    DEFAULT_SERVICE_URL = 'https://globalcatalog.cloud.ibm.com/api/v1'
    DEFAULT_SERVICE_NAME = 'global_catalog'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'GlobalCatalogV1':
        """
        Return a new client for the Global Catalog service using the specified
               parameters and external configuration.
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
        Construct a new client for the Global Catalog service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Object
    #########################

    def list_catalog_entries(
        self,
        *,
        account: Optional[str] = None,
        include: Optional[str] = None,
        q: Optional[str] = None,
        sort_by: Optional[str] = None,
        descending: Optional[str] = None,
        languages: Optional[str] = None,
        catalog: Optional[bool] = None,
        complete: Optional[bool] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Returns parent catalog entries.

        Includes key information, such as ID, name, kind, CRN, tags, and provider. This
        endpoint is ETag enabled.

        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param str include: (optional) A GET call by default returns a basic set of
               properties. To include other properties, you must add this parameter. A
               wildcard (`*`) includes all properties for an object, for example `GET
               /?include=*`. To include specific metadata fields, separate each field with
               a colon (:), for example `GET /?include=metadata.ui:metadata.pricing`.
        :param str q: (optional) Searches the catalog entries for keywords. Add
               filters to refine your search. A query filter, for example, `q=kind:iaas
               service_name rc:true`, filters entries of kind iaas with
               metadata.service.rc_compatible set to true and  have a service name is in
               their name, display name, or description.  Valid tags are
               **kind**:<string>, **tag**:<strging>, **rc**:[true|false],
               **iam**:[true|false], **active**:[true|false], **geo**:<string>, and
               **price**:<string>.
        :param str sort_by: (optional) The field on which the output is sorted.
               Sorts by default by **name** property. Available fields are **name**,
               **displayname** (overview_ui.display_name), **kind**, **provider**
               (provider.name), **sbsindex** (metadata.ui.side_by_side_index), and the
               time **created**, and **updated**.
        :param str descending: (optional) Sets the sort order. The default is
               false, which is ascending.
        :param str languages: (optional) Return the data strings in a specified
               language. By default, the strings returned are of the language preferred by
               your browser through the Accept-Language header, which allows an override
               of the header. Languages are specified in standard form, such as `en-us`.
               To include all languages use a wildcard (*).
        :param bool catalog: (optional) Checks to see if a catalog's object is
               visible, or if it's filtered by service, plan, deployment, or region. Use
               the value `?catalog=true`. If a `200` code is returned, the object is
               visible. If a `403` code is returned, the object is not visible for the
               user.
        :param bool complete: (optional) Returns all available fields for all
               languages. Use the value `?complete=true` as shortcut for
               ?include=*&languages=*.
        :param int offset: (optional) Useful for pagination, specifies index
               (origin 0) of first item to return in response.
        :param int limit: (optional) Useful for pagination, specifies the maximum
               number of items to return in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EntrySearchResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_catalog_entries',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
            'include': include,
            'q': q,
            'sort-by': sort_by,
            'descending': descending,
            'languages': languages,
            'catalog': catalog,
            'complete': complete,
            '_offset': offset,
            '_limit': limit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_catalog_entry(
        self,
        name: str,
        kind: str,
        overview_ui: dict,
        images: 'Image',
        disabled: bool,
        tags: List[str],
        provider: 'Provider',
        id: str,
        *,
        parent_id: Optional[str] = None,
        group: Optional[bool] = None,
        active: Optional[bool] = None,
        url: Optional[str] = None,
        metadata: Optional['ObjectMetadataSet'] = None,
        account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a catalog entry.

        The created catalog entry is restricted by default. You must have an administrator
        or editor role in the scope of the provided token. This API will return an ETag
        that can be used for standard ETag processing, except when depth query is used.

        :param str name: Programmatic name for this catalog entry, which must be
               formatted like a CRN segment. See the display name in OverviewUI for a
               user-readable name.
        :param str kind: The type of catalog entry which determines the type and
               shape of the object. Valid GC types are buildpack, cname, dataset,
               geography, iaas, platform_service, runtime, service, template,
               ui-dashboard.
        :param dict overview_ui: Overview is nested in the top level. The key value
               pair is `[_language_]overview_ui`.
        :param Image images: Image annotation for this catalog entry. The image is
               a URL.
        :param bool disabled: Boolean value that determines the global visibility
               for the catalog entry, and its children. If it is not enabled, all plans
               are disabled.
        :param List[str] tags: A searchable list of tags. For example, IBM, 3rd
               Party, Beta, GA, and Single Tenant. Valid values found at
               https://globalcatalog.test.cloud.ibm.com/search.
        :param Provider provider: Information related to the provider associated
               with a catalog entry.
        :param str id: Catalog entry's unique ID. It's the same across all catalog
               instances.
        :param str parent_id: (optional) The ID of the parent catalog entry if it
               exists.
        :param bool group: (optional) Boolean value that determines whether the
               catalog entry is a group.
        :param bool active: (optional) Boolean value that describes whether the
               service is active.
        :param str url: (optional) Url of the object.
        :param ObjectMetadataSet metadata: (optional) Model used to describe
               metadata object that can be set.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CatalogEntry` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if overview_ui is None:
            raise ValueError('overview_ui must be provided')
        if images is None:
            raise ValueError('images must be provided')
        if disabled is None:
            raise ValueError('disabled must be provided')
        if tags is None:
            raise ValueError('tags must be provided')
        if provider is None:
            raise ValueError('provider must be provided')
        if id is None:
            raise ValueError('id must be provided')
        images = convert_model(images)
        provider = convert_model(provider)
        if metadata is not None:
            metadata = convert_model(metadata)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_catalog_entry',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
        }

        data = {
            'name': name,
            'kind': kind,
            'overview_ui': overview_ui,
            'images': images,
            'disabled': disabled,
            'tags': tags,
            'provider': provider,
            'id': id,
            'parent_id': parent_id,
            'group': group,
            'active': active,
            'url': url,
            'metadata': metadata,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_catalog_entry(
        self,
        id: str,
        *,
        account: Optional[str] = None,
        include: Optional[str] = None,
        languages: Optional[str] = None,
        complete: Optional[bool] = None,
        depth: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a specific catalog object.

        This endpoint returns a specific catalog entry using the object's unique
        identifier, for example `/*service_name*?complete=true`. This endpoint is ETag
        enabled. This can be used by an unauthenticated user for publicly available
        services.

        :param str id: The catalog entry's unique ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param str include: (optional) A GET call by default returns a basic set of
               properties. To include other properties, you must add this parameter. A
               wildcard (`*`) includes all properties for an object, for example `GET
               /id?include=*`. To include specific metadata fields, separate each field
               with a colon (:), for example `GET
               /id?include=metadata.ui:metadata.pricing`.
        :param str languages: (optional) Return the data strings in the specified
               language. By default the strings returned are of the language preferred by
               your browser through the Accept-Language header, which allows an override
               of the header. Languages are specified in standard form, such as `en-us`.
               To include all languages use a wildcard (*).
        :param bool complete: (optional) Returns all available fields for all
               languages. Use the value `?complete=true` as shortcut for
               ?include=*&languages=*.
        :param int depth: (optional) Return the children down to the requested
               depth. Use * to include the entire children tree. If there are more
               children than the maximum permitted an error will be returned. Be judicious
               with this as it can cause a large number of database accesses and can
               result in a large amount of data returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CatalogEntry` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_catalog_entry',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
            'include': include,
            'languages': languages,
            'complete': complete,
            'depth': depth,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_catalog_entry(
        self,
        id: str,
        name: str,
        kind: str,
        overview_ui: dict,
        images: 'Image',
        disabled: bool,
        tags: List[str],
        provider: 'Provider',
        *,
        parent_id: Optional[str] = None,
        group: Optional[bool] = None,
        active: Optional[bool] = None,
        url: Optional[str] = None,
        metadata: Optional['ObjectMetadataSet'] = None,
        account: Optional[str] = None,
        move: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a catalog entry.

        Update a catalog entry. The visibility of the catalog entry cannot be modified
        with this endpoint. You must be an administrator or editor in the scope of the
        provided token. This endpoint is ETag enabled.

        :param str id: The object's unique ID.
        :param str name: Programmatic name for this catalog entry, which must be
               formatted like a CRN segment. See the display name in OverviewUI for a
               user-readable name.
        :param str kind: The type of catalog entry which determines the type and
               shape of the object. Valid GC types are buildpack, cname, dataset,
               geography, iaas, platform_service, runtime, service, template,
               ui-dashboard.
        :param dict overview_ui: Overview is nested in the top level. The key value
               pair is `[_language_]overview_ui`.
        :param Image images: Image annotation for this catalog entry. The image is
               a URL.
        :param bool disabled: Boolean value that determines the global visibility
               for the catalog entry, and its children. If it is not enabled, all plans
               are disabled.
        :param List[str] tags: A searchable list of tags. For example, IBM, 3rd
               Party, Beta, GA, and Single Tenant. Valid values found at
               https://globalcatalog.test.cloud.ibm.com/search.
        :param Provider provider: Information related to the provider associated
               with a catalog entry.
        :param str parent_id: (optional) The ID of the parent catalog entry if it
               exists.
        :param bool group: (optional) Boolean value that determines whether the
               catalog entry is a group.
        :param bool active: (optional) Boolean value that describes whether the
               service is active.
        :param str url: (optional) Url of the object.
        :param ObjectMetadataSet metadata: (optional) Model used to describe
               metadata object that can be set.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param str move: (optional) Reparenting object. In the body set the
               parent_id to a different parent. Or remove the parent_id field to reparent
               to the root of the catalog. If this is not set to 'true' then changing the
               parent_id in the body of the request will not be permitted. If this is
               'true' and no change to parent_id then this is also error. This is to
               prevent accidental changing of parent.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CatalogEntry` object
        """

        if not id:
            raise ValueError('id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if overview_ui is None:
            raise ValueError('overview_ui must be provided')
        if images is None:
            raise ValueError('images must be provided')
        if disabled is None:
            raise ValueError('disabled must be provided')
        if tags is None:
            raise ValueError('tags must be provided')
        if provider is None:
            raise ValueError('provider must be provided')
        images = convert_model(images)
        provider = convert_model(provider)
        if metadata is not None:
            metadata = convert_model(metadata)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_catalog_entry',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
            'move': move,
        }

        data = {
            'name': name,
            'kind': kind,
            'overview_ui': overview_ui,
            'images': images,
            'disabled': disabled,
            'tags': tags,
            'provider': provider,
            'parent_id': parent_id,
            'group': group,
            'active': active,
            'url': url,
            'metadata': metadata,
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
        url = '/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_catalog_entry(
        self,
        id: str,
        *,
        account: Optional[str] = None,
        force: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a catalog entry.

        Delete a catalog entry. This will archive the catalog entry for a minimum of two
        weeks. While archived, it can be restored using the PUT restore API. After two
        weeks, it will be deleted and cannot be restored. You must have administrator role
        in the scope of the provided token to modify it. This endpoint is ETag enabled.

        :param str id: The object's unique ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param bool force: (optional) This will cause entry to be deleted fully. By
               default it is archived for two weeks, so that it can be restored if
               necessary.
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
            operation_id='delete_catalog_entry',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
            'force': force,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_child_objects(
        self,
        id: str,
        kind: str,
        *,
        account: Optional[str] = None,
        include: Optional[str] = None,
        q: Optional[str] = None,
        sort_by: Optional[str] = None,
        descending: Optional[str] = None,
        languages: Optional[str] = None,
        complete: Optional[bool] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get child catalog entries of a specific kind.

        Fetch child catalog entries for a catalog entry with a specific id. This endpoint
        is ETag enabled. This can be used by an unauthenticated user for publicly
        available services.

        :param str id: The parent catalog entry's ID.
        :param str kind: The **kind** of child catalog entries to search for. A
               wildcard (*) includes all child catalog entries for all kinds, for example
               `GET /service_name/*`.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param str include: (optional) A colon (:) separated list of properties to
               include. A GET call by defaults return a limited set of properties. To
               include other properties, you must add the include parameter.  A wildcard
               (*) includes all properties.
        :param str q: (optional) A query filter, for example, `q=kind:iaas IBM`
               will filter on entries of **kind** iaas that has `IBM` in their name,
               display name, or description.
        :param str sort_by: (optional) The field on which to sort the output. By
               default by name. Available fields are **name**, **kind**, and **provider**.
        :param str descending: (optional) The sort order. The default is false,
               which is ascending.
        :param str languages: (optional) Return the data strings in the specified
               language. By default the strings returned are of the language preferred by
               your browser through the Accept-Language header. This allows an override of
               the header. Languages are specified in standard form, such as `en-us`. To
               include all languages use the wildcard (*).
        :param bool complete: (optional) Use the value `?complete=true` as shortcut
               for ?include=*&languages=*.
        :param int offset: (optional) Useful for pagination, specifies index
               (origin 0) of first item to return in response.
        :param int limit: (optional) Useful for pagination, specifies the maximum
               number of items to return in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EntrySearchResult` object
        """

        if not id:
            raise ValueError('id must be provided')
        if not kind:
            raise ValueError('kind must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_child_objects',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
            'include': include,
            'q': q,
            'sort-by': sort_by,
            'descending': descending,
            'languages': languages,
            'complete': complete,
            '_offset': offset,
            '_limit': limit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'kind']
        path_param_values = self.encode_path_vars(id, kind)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{id}/{kind}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def restore_catalog_entry(
        self,
        id: str,
        *,
        account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Restore archived catalog entry.

        Restore an archived catalog entry. You must have an administrator role in the
        scope of the provided token.

        :param str id: The catalog entry's unique ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
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
            operation_id='restore_catalog_entry',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{id}/restore'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Visibility
    #########################

    def get_visibility(
        self,
        id: str,
        *,
        account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get the visibility constraints for an object.

        This endpoint returns the visibility rules for this object. Overall visibility is
        determined by the parent objects and any further restrictions on this object. You
        must have an administrator role in the scope of the provided token. This endpoint
        is ETag enabled.

        :param str id: The object's unique ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Visibility` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_visibility',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{id}/visibility'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_visibility(
        self,
        id: str,
        *,
        restrictions: Optional[str] = None,
        extendable: Optional[bool] = None,
        include: Optional['VisibilityDetail'] = None,
        exclude: Optional['VisibilityDetail'] = None,
        account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update visibility.

        Update an Object's Visibility. You must have an administrator role in the scope of
        the provided token. This endpoint is ETag enabled.

        :param str id: The object's unique ID.
        :param str restrictions: (optional) This controls the overall visibility.
               It is an enum of *public*, *nonibm_only*, *ibm_only*, and *private*. public
               means it is visible to all. nonibm_only means it is visible to all except
               IBM unless their account is explicitly included, ibm_only means it is
               visible to all IBM unless their account is explicitly excluded. private
               means it is visible only to the included accounts.
        :param bool extendable: (optional) Allows the visibility to be extendable.
        :param VisibilityDetail include: (optional) Visibility details related to a
               catalog entry.
        :param VisibilityDetail exclude: (optional) Visibility details related to a
               catalog entry.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        if include is not None:
            include = convert_model(include)
        if exclude is not None:
            exclude = convert_model(exclude)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_visibility',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
        }

        data = {
            'restrictions': restrictions,
            'extendable': extendable,
            'include': include,
            'exclude': exclude,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{id}/visibility'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Pricing
    #########################

    def get_pricing(
        self,
        id: str,
        *,
        account: Optional[str] = None,
        deployment_region: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get the pricing for an object.

        This endpoint returns the pricing for an object. Static pricing is defined in the
        catalog. Dynamic pricing is stored in IBM Cloud Pricing Catalog. This can be used
        by an unauthenticated user for publicly available services.

        :param str id: The object's unique ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param str deployment_region: (optional) Specify a region to retrieve plan
               pricing for a global deployment. The value must match an entry in the
               `deployment_regions` list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PricingGet` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_pricing',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
            'deployment_region': deployment_region,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{id}/pricing'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_pricing_deployments(
        self,
        id: str,
        *,
        account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get the pricing deployments for a plan.

        This endpoint returns the deployment pricing for a plan. For a plan it returns a
        pricing for each visible child deployment object. Static pricing is defined in the
        catalog. Dynamic pricing is stored in IBM Cloud Pricing Catalog. This can be used
        by an unauthenticated user for publicly available services.

        :param str id: The object's unique ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PricingSearchResult` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_pricing_deployments',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{id}/pricing/deployment'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Audit
    #########################

    def get_audit_logs(
        self,
        id: str,
        *,
        account: Optional[str] = None,
        ascending: Optional[str] = None,
        startat: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get the audit logs for an object.

        This endpoint returns the audit logs for an object. Only administrators and
        editors can get logs.

        :param str id: The object's unique ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param str ascending: (optional) Sets the sort order. False is descending.
        :param str startat: (optional) Starting time for the logs. If it's
               descending then the entries will be equal or earlier. The default is
               latest. For ascending it will entries equal or later. The default is
               earliest. It can be either a number or a string. If a number then it is in
               the format of Unix timestamps. If it is a string then it is a date in the
               format YYYY-MM-DDTHH:MM:SSZ  and the time is UTC. The T and the Z are
               required. For example: 2017-12-24T12:00:00Z for Noon UTC on Dec 24, 2017.
        :param int offset: (optional) Count of number of log entries to skip before
               returning logs. The default is zero.
        :param int limit: (optional) Count of number of entries to return. The
               default is fifty. The maximum value is two hundred.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AuditSearchResult` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_audit_logs',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
            'ascending': ascending,
            'startat': startat,
            '_offset': offset,
            '_limit': limit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{id}/logs'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Artifact
    #########################

    def list_artifacts(
        self,
        object_id: str,
        *,
        account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get artifacts.

        This endpoint returns a list of artifacts for an object.

        :param str object_id: The object's unique ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Artifacts` object
        """

        if not object_id:
            raise ValueError('object_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_artifacts',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['object_id']
        path_param_values = self.encode_path_vars(object_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{object_id}/artifacts'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_artifact(
        self,
        object_id: str,
        artifact_id: str,
        *,
        account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get artifact.

        This endpoint returns the binary of an artifact.

        :param str object_id: The object's unique ID.
        :param str artifact_id: The artifact's ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not object_id:
            raise ValueError('object_id must be provided')
        if not artifact_id:
            raise ValueError('artifact_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_artifact',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = '*/*'

        path_param_keys = ['object_id', 'artifact_id']
        path_param_values = self.encode_path_vars(object_id, artifact_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{object_id}/artifacts/{artifact_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def upload_artifact(
        self,
        object_id: str,
        artifact_id: str,
        *,
        artifact: Optional[BinaryIO] = None,
        content_type: Optional[str] = None,
        account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Upload artifact.

        This endpoint uploads the binary for an artifact. Only administrators and editors
        can upload artifacts.

        :param str object_id: The object's unique ID.
        :param str artifact_id: The artifact's ID.
        :param BinaryIO artifact: (optional)
        :param str content_type: (optional) The type of the input.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not object_id:
            raise ValueError('object_id must be provided')
        if not artifact_id:
            raise ValueError('artifact_id must be provided')
        headers = {
            'Content-Type': content_type,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='upload_artifact',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
        }

        data = artifact

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['object_id', 'artifact_id']
        path_param_values = self.encode_path_vars(object_id, artifact_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{object_id}/artifacts/{artifact_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_artifact(
        self,
        object_id: str,
        artifact_id: str,
        *,
        account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete artifact.

        This endpoint deletes an artifact. Only administrators and editors can delete
        artifacts.

        :param str object_id: The object's unique ID.
        :param str artifact_id: The artifact's ID.
        :param str account: (optional) This changes the scope of the request
               regardless of the authorization header. Example scopes are `account` and
               `global`. `account=global` is reqired if operating with a service ID that
               has a global admin policy, for example `GET /?account=global`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not object_id:
            raise ValueError('object_id must be provided')
        if not artifact_id:
            raise ValueError('artifact_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_artifact',
        )
        headers.update(sdk_headers)

        params = {
            'account': account,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['object_id', 'artifact_id']
        path_param_values = self.encode_path_vars(object_id, artifact_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{object_id}/artifacts/{artifact_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AliasMetaData:
    """
    Alias-related metadata.

    :param str type: (optional) Type of alias.
    :param str plan_id: (optional) Points to the plan that this object is an alias
          for.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        plan_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a AliasMetaData object.

        :param str type: (optional) Type of alias.
        :param str plan_id: (optional) Points to the plan that this object is an
               alias for.
        """
        self.type = type
        self.plan_id = plan_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AliasMetaData':
        """Initialize a AliasMetaData object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (plan_id := _dict.get('plan_id')) is not None:
            args['plan_id'] = plan_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AliasMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'plan_id') and self.plan_id is not None:
            _dict['plan_id'] = self.plan_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AliasMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AliasMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AliasMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Amount:
    """
    Country-specific pricing information.

    :param str country: (optional) Country.
    :param str currency: (optional) Currency.
    :param List[Price] prices: (optional) See Price for nested fields.
    """

    def __init__(
        self,
        *,
        country: Optional[str] = None,
        currency: Optional[str] = None,
        prices: Optional[List['Price']] = None,
    ) -> None:
        """
        Initialize a Amount object.

        :param str country: (optional) Country.
        :param str currency: (optional) Currency.
        :param List[Price] prices: (optional) See Price for nested fields.
        """
        self.country = country
        self.currency = currency
        self.prices = prices

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Amount':
        """Initialize a Amount object from a json dictionary."""
        args = {}
        if (country := _dict.get('country')) is not None:
            args['country'] = country
        if (currency := _dict.get('currency')) is not None:
            args['currency'] = currency
        if (prices := _dict.get('prices')) is not None:
            args['prices'] = [Price.from_dict(v) for v in prices]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Amount object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'country') and self.country is not None:
            _dict['country'] = self.country
        if hasattr(self, 'currency') and self.currency is not None:
            _dict['currency'] = self.currency
        if hasattr(self, 'prices') and self.prices is not None:
            prices_list = []
            for v in self.prices:
                if isinstance(v, dict):
                    prices_list.append(v)
                else:
                    prices_list.append(v.to_dict())
            _dict['prices'] = prices_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Amount object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Amount') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Amount') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Artifact:
    """
    Artifact Details.

    :param str name: (optional) The name of the artifact.
    :param datetime updated: (optional) The timestamp of the last update to the
          artifact.
    :param str url: (optional) The url for the artifact.
    :param str etag: (optional) The etag of the artifact.
    :param int size: (optional) The content length of the artifact.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        updated: Optional[datetime] = None,
        url: Optional[str] = None,
        etag: Optional[str] = None,
        size: Optional[int] = None,
    ) -> None:
        """
        Initialize a Artifact object.

        :param str name: (optional) The name of the artifact.
        :param datetime updated: (optional) The timestamp of the last update to the
               artifact.
        :param str url: (optional) The url for the artifact.
        :param str etag: (optional) The etag of the artifact.
        :param int size: (optional) The content length of the artifact.
        """
        self.name = name
        self.updated = updated
        self.url = url
        self.etag = etag
        self.size = size

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Artifact':
        """Initialize a Artifact object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        if (etag := _dict.get('etag')) is not None:
            args['etag'] = etag
        if (size := _dict.get('size')) is not None:
            args['size'] = size
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Artifact object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'etag') and self.etag is not None:
            _dict['etag'] = self.etag
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Artifact object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Artifact') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Artifact') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Artifacts:
    """
    Artifacts List.

    :param int count: (optional) The total number of artifacts.
    :param List[Artifact] resources: (optional) The list of artifacts.
    """

    def __init__(
        self,
        *,
        count: Optional[int] = None,
        resources: Optional[List['Artifact']] = None,
    ) -> None:
        """
        Initialize a Artifacts object.

        :param int count: (optional) The total number of artifacts.
        :param List[Artifact] resources: (optional) The list of artifacts.
        """
        self.count = count
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Artifacts':
        """Initialize a Artifacts object from a json dictionary."""
        args = {}
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [Artifact.from_dict(v) for v in resources]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Artifacts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'resources') and self.resources is not None:
            resources_list = []
            for v in self.resources:
                if isinstance(v, dict):
                    resources_list.append(v)
                else:
                    resources_list.append(v.to_dict())
            _dict['resources'] = resources_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Artifacts object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Artifacts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Artifacts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AuditSearchResult:
    """
    A paginated search result containing audit logs.

    :param int offset: (optional) The offset (origin 0) of the first resource in
          this page of search results.
    :param int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :param int count: (optional) The overall total number of resources in the search
          result set.
    :param int resource_count: (optional) The number of resources returned in this
          page of search results.
    :param str first: (optional) A URL for retrieving the first page of search
          results.
    :param str last: (optional) A URL for retrieving the last page of search
          results.
    :param str prev: (optional) A URL for retrieving the previous page of search
          results.
    :param str next: (optional) A URL for retrieving the next page of search
          results.
    :param List[Message] resources: (optional) The resources (audit messages)
          contained in this page of search results.
    """

    def __init__(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        count: Optional[int] = None,
        resource_count: Optional[int] = None,
        first: Optional[str] = None,
        last: Optional[str] = None,
        prev: Optional[str] = None,
        next: Optional[str] = None,
        resources: Optional[List['Message']] = None,
    ) -> None:
        """
        Initialize a AuditSearchResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int count: (optional) The overall total number of resources in the
               search result set.
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
        :param List[Message] resources: (optional) The resources (audit messages)
               contained in this page of search results.
        """
        self.offset = offset
        self.limit = limit
        self.count = count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AuditSearchResult':
        """Initialize a AuditSearchResult object from a json dictionary."""
        args = {}
        if (offset := _dict.get('offset')) is not None:
            args['offset'] = offset
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (resource_count := _dict.get('resource_count')) is not None:
            args['resource_count'] = resource_count
        if (first := _dict.get('first')) is not None:
            args['first'] = first
        if (last := _dict.get('last')) is not None:
            args['last'] = last
        if (prev := _dict.get('prev')) is not None:
            args['prev'] = prev
        if (next := _dict.get('next')) is not None:
            args['next'] = next
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [Message.from_dict(v) for v in resources]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AuditSearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
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
            resources_list = []
            for v in self.resources:
                if isinstance(v, dict):
                    resources_list.append(v)
                else:
                    resources_list.append(v.to_dict())
            _dict['resources'] = resources_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AuditSearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AuditSearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AuditSearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Broker:
    """
    The broker associated with a catalog entry.

    :param str name: (optional) Broker name.
    :param str guid: (optional) Broker guid.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        guid: Optional[str] = None,
    ) -> None:
        """
        Initialize a Broker object.

        :param str name: (optional) Broker name.
        :param str guid: (optional) Broker guid.
        """
        self.name = name
        self.guid = guid

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Broker':
        """Initialize a Broker object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (guid := _dict.get('guid')) is not None:
            args['guid'] = guid
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Broker object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'guid') and self.guid is not None:
            _dict['guid'] = self.guid
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Broker object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Broker') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Broker') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Bullets:
    """
    Information related to list delimiters.

    :param str title: (optional) The bullet title.
    :param str description: (optional) The bullet description.
    :param str icon: (optional) The icon to use for rendering the bullet.
    :param int quantity: (optional) The bullet quantity.
    """

    def __init__(
        self,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        icon: Optional[str] = None,
        quantity: Optional[int] = None,
    ) -> None:
        """
        Initialize a Bullets object.

        :param str title: (optional) The bullet title.
        :param str description: (optional) The bullet description.
        :param str icon: (optional) The icon to use for rendering the bullet.
        :param int quantity: (optional) The bullet quantity.
        """
        self.title = title
        self.description = description
        self.icon = icon
        self.quantity = quantity

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Bullets':
        """Initialize a Bullets object from a json dictionary."""
        args = {}
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (icon := _dict.get('icon')) is not None:
            args['icon'] = icon
        if (quantity := _dict.get('quantity')) is not None:
            args['quantity'] = quantity
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Bullets object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'icon') and self.icon is not None:
            _dict['icon'] = self.icon
        if hasattr(self, 'quantity') and self.quantity is not None:
            _dict['quantity'] = self.quantity
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Bullets object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Bullets') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Bullets') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CFMetaData:
    """
    Service-related metadata.

    :param str type: (optional) Deprecated: The type of service (public, cfaas,
          personal_catalog, kms, toolchain, etc.).
    :param bool iam_compatible: (optional) Boolean value that describes whether the
          service is compatible with Identity and Access Management for authentication and
          authorization.
    :param bool unique_api_key: (optional) Deprecated: Boolean value that describes
          whether the service has a unique API key. Only settable on services, should be
          set via partnercenter.
    :param bool provisionable: (optional) Boolean value that, if true, the service
          is provisionable via resource controller (RC) or, if false, via a service
          control point API. If false, you may need sales or support to create this
          service.
    :param bool bindable: (optional) Boolean value that describes whether the
          service can be bound to an application. If true then this will create and use
          resource keys.
    :param bool async_provisioning_supported: (optional) Deprecated: Boolean value
          that describes whether the service supports asynchronous provisioning. Now
          handled by a 202 response indicating support from the broker on provisioning.
    :param bool async_unprovisioning_supported: (optional) Deprecated: Boolean value
          that describes whether the service supports asynchronous unprovisioning. Now
          handled by a 202 response indicating support from the broker on unprovisioning.
    :param List[str] requires: (optional) Deprecated: Dependencies needed to use
          this service.
    :param bool plan_updateable: (optional) Boolean value that describes whether the
          service supports changing plans within the service. Only settable on services,
          read only on plans and deployments.
    :param str state: (optional) Deprecated: String that describes whether the
          service is active or inactive.
    :param bool service_check_enabled: (optional) Deprecated: Boolean value that
          describes whether the Estado testing service will perform uptime tests for this
          service.
    :param int test_check_interval: (optional) Deprecated: A unit of time that
          determines the time in between uptime checks performed by Estado.
    :param bool service_key_supported: (optional) Boolean value that describes
          whether the service supports the creation of service credentials. Without
          service key support, a service cannot be bound to a cluster.
    :param dict cf_guid: (optional) Deprecated: If the field is imported from Cloud
          Foundry, the Cloud Foundry region's GUID. This is a required field. For example,
          `us-south=123`.
    :param str crn_mask: (optional) Cloud resource name identifying the environment
          containing this service.
    :param bool paid_only: (optional) Deprecated: Boolean flag indicating if this
          service only offers paid pricing plans rather than the default paygo.
    :param bool custom_create_page_hybrid_enabled: (optional) Boolean flag that
          determines if the hybrid page is accessible from the main catalog provisioning
          page.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        iam_compatible: Optional[bool] = None,
        unique_api_key: Optional[bool] = None,
        provisionable: Optional[bool] = None,
        bindable: Optional[bool] = None,
        async_provisioning_supported: Optional[bool] = None,
        async_unprovisioning_supported: Optional[bool] = None,
        requires: Optional[List[str]] = None,
        plan_updateable: Optional[bool] = None,
        state: Optional[str] = None,
        service_check_enabled: Optional[bool] = None,
        test_check_interval: Optional[int] = None,
        service_key_supported: Optional[bool] = None,
        cf_guid: Optional[dict] = None,
        crn_mask: Optional[str] = None,
        paid_only: Optional[bool] = None,
        custom_create_page_hybrid_enabled: Optional[bool] = None,
    ) -> None:
        """
        Initialize a CFMetaData object.

        :param str type: (optional) Deprecated: The type of service (public, cfaas,
               personal_catalog, kms, toolchain, etc.).
        :param bool iam_compatible: (optional) Boolean value that describes whether
               the service is compatible with Identity and Access Management for
               authentication and authorization.
        :param bool unique_api_key: (optional) Deprecated: Boolean value that
               describes whether the service has a unique API key. Only settable on
               services, should be set via partnercenter.
        :param bool provisionable: (optional) Boolean value that, if true, the
               service is provisionable via resource controller (RC) or, if false, via a
               service control point API. If false, you may need sales or support to
               create this service.
        :param bool bindable: (optional) Boolean value that describes whether the
               service can be bound to an application. If true then this will create and
               use resource keys.
        :param bool async_provisioning_supported: (optional) Deprecated: Boolean
               value that describes whether the service supports asynchronous
               provisioning. Now handled by a 202 response indicating support from the
               broker on provisioning.
        :param bool async_unprovisioning_supported: (optional) Deprecated: Boolean
               value that describes whether the service supports asynchronous
               unprovisioning. Now handled by a 202 response indicating support from the
               broker on unprovisioning.
        :param List[str] requires: (optional) Deprecated: Dependencies needed to
               use this service.
        :param bool plan_updateable: (optional) Boolean value that describes
               whether the service supports changing plans within the service. Only
               settable on services, read only on plans and deployments.
        :param str state: (optional) Deprecated: String that describes whether the
               service is active or inactive.
        :param bool service_check_enabled: (optional) Deprecated: Boolean value
               that describes whether the Estado testing service will perform uptime tests
               for this service.
        :param int test_check_interval: (optional) Deprecated: A unit of time that
               determines the time in between uptime checks performed by Estado.
        :param bool service_key_supported: (optional) Boolean value that describes
               whether the service supports the creation of service credentials. Without
               service key support, a service cannot be bound to a cluster.
        :param dict cf_guid: (optional) Deprecated: If the field is imported from
               Cloud Foundry, the Cloud Foundry region's GUID. This is a required field.
               For example, `us-south=123`.
        :param str crn_mask: (optional) Cloud resource name identifying the
               environment containing this service.
        :param bool paid_only: (optional) Deprecated: Boolean flag indicating if
               this service only offers paid pricing plans rather than the default paygo.
        :param bool custom_create_page_hybrid_enabled: (optional) Boolean flag that
               determines if the hybrid page is accessible from the main catalog
               provisioning page.
        """
        self.type = type
        self.iam_compatible = iam_compatible
        self.unique_api_key = unique_api_key
        self.provisionable = provisionable
        self.bindable = bindable
        self.async_provisioning_supported = async_provisioning_supported
        self.async_unprovisioning_supported = async_unprovisioning_supported
        self.requires = requires
        self.plan_updateable = plan_updateable
        self.state = state
        self.service_check_enabled = service_check_enabled
        self.test_check_interval = test_check_interval
        self.service_key_supported = service_key_supported
        self.cf_guid = cf_guid
        self.crn_mask = crn_mask
        self.paid_only = paid_only
        self.custom_create_page_hybrid_enabled = custom_create_page_hybrid_enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CFMetaData':
        """Initialize a CFMetaData object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (iam_compatible := _dict.get('iam_compatible')) is not None:
            args['iam_compatible'] = iam_compatible
        if (unique_api_key := _dict.get('unique_api_key')) is not None:
            args['unique_api_key'] = unique_api_key
        if (provisionable := _dict.get('provisionable')) is not None:
            args['provisionable'] = provisionable
        if (bindable := _dict.get('bindable')) is not None:
            args['bindable'] = bindable
        if (async_provisioning_supported := _dict.get('async_provisioning_supported')) is not None:
            args['async_provisioning_supported'] = async_provisioning_supported
        if (async_unprovisioning_supported := _dict.get('async_unprovisioning_supported')) is not None:
            args['async_unprovisioning_supported'] = async_unprovisioning_supported
        if (requires := _dict.get('requires')) is not None:
            args['requires'] = requires
        if (plan_updateable := _dict.get('plan_updateable')) is not None:
            args['plan_updateable'] = plan_updateable
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        if (service_check_enabled := _dict.get('service_check_enabled')) is not None:
            args['service_check_enabled'] = service_check_enabled
        if (test_check_interval := _dict.get('test_check_interval')) is not None:
            args['test_check_interval'] = test_check_interval
        if (service_key_supported := _dict.get('service_key_supported')) is not None:
            args['service_key_supported'] = service_key_supported
        if (cf_guid := _dict.get('cf_guid')) is not None:
            args['cf_guid'] = cf_guid
        if (crn_mask := _dict.get('crn_mask')) is not None:
            args['crn_mask'] = crn_mask
        if (paid_only := _dict.get('paid_only')) is not None:
            args['paid_only'] = paid_only
        if (custom_create_page_hybrid_enabled := _dict.get('custom_create_page_hybrid_enabled')) is not None:
            args['custom_create_page_hybrid_enabled'] = custom_create_page_hybrid_enabled
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CFMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'iam_compatible') and self.iam_compatible is not None:
            _dict['iam_compatible'] = self.iam_compatible
        if hasattr(self, 'unique_api_key') and self.unique_api_key is not None:
            _dict['unique_api_key'] = self.unique_api_key
        if hasattr(self, 'provisionable') and self.provisionable is not None:
            _dict['provisionable'] = self.provisionable
        if hasattr(self, 'bindable') and self.bindable is not None:
            _dict['bindable'] = self.bindable
        if hasattr(self, 'async_provisioning_supported') and self.async_provisioning_supported is not None:
            _dict['async_provisioning_supported'] = self.async_provisioning_supported
        if hasattr(self, 'async_unprovisioning_supported') and self.async_unprovisioning_supported is not None:
            _dict['async_unprovisioning_supported'] = self.async_unprovisioning_supported
        if hasattr(self, 'requires') and self.requires is not None:
            _dict['requires'] = self.requires
        if hasattr(self, 'plan_updateable') and self.plan_updateable is not None:
            _dict['plan_updateable'] = self.plan_updateable
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'service_check_enabled') and self.service_check_enabled is not None:
            _dict['service_check_enabled'] = self.service_check_enabled
        if hasattr(self, 'test_check_interval') and self.test_check_interval is not None:
            _dict['test_check_interval'] = self.test_check_interval
        if hasattr(self, 'service_key_supported') and self.service_key_supported is not None:
            _dict['service_key_supported'] = self.service_key_supported
        if hasattr(self, 'cf_guid') and self.cf_guid is not None:
            _dict['cf_guid'] = self.cf_guid
        if hasattr(self, 'crn_mask') and self.crn_mask is not None:
            _dict['crn_mask'] = self.crn_mask
        if hasattr(self, 'paid_only') and self.paid_only is not None:
            _dict['paid_only'] = self.paid_only
        if hasattr(self, 'custom_create_page_hybrid_enabled') and self.custom_create_page_hybrid_enabled is not None:
            _dict['custom_create_page_hybrid_enabled'] = self.custom_create_page_hybrid_enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CFMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CFMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CFMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Callbacks:
    """
    Callback-related information associated with a catalog entry.

    :param str controller_url: (optional) The URL of the deployment controller.
    :param str broker_url: (optional) The URL of the deployment broker.
    :param str broker_proxy_url: (optional) Deprecated: The URL of the deployment
          broker SC proxy.
    :param str dashboard_url: (optional) The URL of dashboard callback.
    :param str dashboard_data_url: (optional) The URL of dashboard data.
    :param str dashboard_detail_tab_url: (optional) The URL of the dashboard detail
          tab.
    :param str dashboard_detail_tab_ext_url: (optional) The URL of the dashboard
          detail tab extension.
    :param str service_monitor_api: (optional) Service monitor API URL.
    :param str service_monitor_app: (optional) Service monitor app URL.
    :param dict api_endpoint: (optional) API endpoint.
    """

    def __init__(
        self,
        *,
        controller_url: Optional[str] = None,
        broker_url: Optional[str] = None,
        broker_proxy_url: Optional[str] = None,
        dashboard_url: Optional[str] = None,
        dashboard_data_url: Optional[str] = None,
        dashboard_detail_tab_url: Optional[str] = None,
        dashboard_detail_tab_ext_url: Optional[str] = None,
        service_monitor_api: Optional[str] = None,
        service_monitor_app: Optional[str] = None,
        api_endpoint: Optional[dict] = None,
    ) -> None:
        """
        Initialize a Callbacks object.

        :param str controller_url: (optional) The URL of the deployment controller.
        :param str broker_url: (optional) The URL of the deployment broker.
        :param str broker_proxy_url: (optional) Deprecated: The URL of the
               deployment broker SC proxy.
        :param str dashboard_url: (optional) The URL of dashboard callback.
        :param str dashboard_data_url: (optional) The URL of dashboard data.
        :param str dashboard_detail_tab_url: (optional) The URL of the dashboard
               detail tab.
        :param str dashboard_detail_tab_ext_url: (optional) The URL of the
               dashboard detail tab extension.
        :param str service_monitor_api: (optional) Service monitor API URL.
        :param str service_monitor_app: (optional) Service monitor app URL.
        :param dict api_endpoint: (optional) API endpoint.
        """
        self.controller_url = controller_url
        self.broker_url = broker_url
        self.broker_proxy_url = broker_proxy_url
        self.dashboard_url = dashboard_url
        self.dashboard_data_url = dashboard_data_url
        self.dashboard_detail_tab_url = dashboard_detail_tab_url
        self.dashboard_detail_tab_ext_url = dashboard_detail_tab_ext_url
        self.service_monitor_api = service_monitor_api
        self.service_monitor_app = service_monitor_app
        self.api_endpoint = api_endpoint

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Callbacks':
        """Initialize a Callbacks object from a json dictionary."""
        args = {}
        if (controller_url := _dict.get('controller_url')) is not None:
            args['controller_url'] = controller_url
        if (broker_url := _dict.get('broker_url')) is not None:
            args['broker_url'] = broker_url
        if (broker_proxy_url := _dict.get('broker_proxy_url')) is not None:
            args['broker_proxy_url'] = broker_proxy_url
        if (dashboard_url := _dict.get('dashboard_url')) is not None:
            args['dashboard_url'] = dashboard_url
        if (dashboard_data_url := _dict.get('dashboard_data_url')) is not None:
            args['dashboard_data_url'] = dashboard_data_url
        if (dashboard_detail_tab_url := _dict.get('dashboard_detail_tab_url')) is not None:
            args['dashboard_detail_tab_url'] = dashboard_detail_tab_url
        if (dashboard_detail_tab_ext_url := _dict.get('dashboard_detail_tab_ext_url')) is not None:
            args['dashboard_detail_tab_ext_url'] = dashboard_detail_tab_ext_url
        if (service_monitor_api := _dict.get('service_monitor_api')) is not None:
            args['service_monitor_api'] = service_monitor_api
        if (service_monitor_app := _dict.get('service_monitor_app')) is not None:
            args['service_monitor_app'] = service_monitor_app
        if (api_endpoint := _dict.get('api_endpoint')) is not None:
            args['api_endpoint'] = api_endpoint
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Callbacks object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'controller_url') and self.controller_url is not None:
            _dict['controller_url'] = self.controller_url
        if hasattr(self, 'broker_url') and self.broker_url is not None:
            _dict['broker_url'] = self.broker_url
        if hasattr(self, 'broker_proxy_url') and self.broker_proxy_url is not None:
            _dict['broker_proxy_url'] = self.broker_proxy_url
        if hasattr(self, 'dashboard_url') and self.dashboard_url is not None:
            _dict['dashboard_url'] = self.dashboard_url
        if hasattr(self, 'dashboard_data_url') and self.dashboard_data_url is not None:
            _dict['dashboard_data_url'] = self.dashboard_data_url
        if hasattr(self, 'dashboard_detail_tab_url') and self.dashboard_detail_tab_url is not None:
            _dict['dashboard_detail_tab_url'] = self.dashboard_detail_tab_url
        if hasattr(self, 'dashboard_detail_tab_ext_url') and self.dashboard_detail_tab_ext_url is not None:
            _dict['dashboard_detail_tab_ext_url'] = self.dashboard_detail_tab_ext_url
        if hasattr(self, 'service_monitor_api') and self.service_monitor_api is not None:
            _dict['service_monitor_api'] = self.service_monitor_api
        if hasattr(self, 'service_monitor_app') and self.service_monitor_app is not None:
            _dict['service_monitor_app'] = self.service_monitor_app
        if hasattr(self, 'api_endpoint') and self.api_endpoint is not None:
            _dict['api_endpoint'] = self.api_endpoint
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Callbacks object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Callbacks') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Callbacks') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CatalogEntry:
    """
    An entry in the global catalog.

    :param str name: Programmatic name for this catalog entry, which must be
          formatted like a CRN segment. See the display name in OverviewUI for a
          user-readable name.
    :param str kind: The type of catalog entry which determines the type and shape
          of the object. Valid GC types are buildpack, cname, dataset, geography, iaas,
          platform_service, runtime, service, template, ui-dashboard.
    :param dict overview_ui: Overview is nested in the top level. The key value pair
          is `[_language_]overview_ui`.
    :param Image images: Image annotation for this catalog entry. The image is a
          URL.
    :param str parent_id: (optional) The ID of the parent catalog entry if it
          exists.
    :param bool disabled: Boolean value that determines the global visibility for
          the catalog entry, and its children. If it is not enabled, all plans are
          disabled.
    :param List[str] tags: A searchable list of tags. For example, IBM, 3rd Party,
          Beta, GA, and Single Tenant. Valid values found at
          https://globalcatalog.test.cloud.ibm.com/search.
    :param bool group: (optional) Boolean value that determines whether the catalog
          entry is a group.
    :param Provider provider: Information related to the provider associated with a
          catalog entry.
    :param bool active: (optional) Boolean value that describes whether the service
          is active.
    :param str url: (optional) URL to get details about this object.
    :param CatalogEntryMetadata metadata: (optional) Model used to describe metadata
          object returned.
    :param str id: (optional) Catalog entry's unique ID. It's the same across all
          catalog instances.
    :param str catalog_crn: (optional) The CRN associated with the catalog entry.
    :param str children_url: (optional) URL to get details about children of this
          object.
    :param List[str] geo_tags: (optional) tags to indicate the locations this
          service is deployable to.
    :param List[str] pricing_tags: (optional) tags to indicate the type of pricing
          plans this service supports. Plans tagged with paid_only will not be shown for
          trial accounts.
    :param datetime created: (optional) Date created.
    :param datetime updated: (optional) Date last updated.
    """

    def __init__(
        self,
        name: str,
        kind: str,
        overview_ui: dict,
        images: 'Image',
        disabled: bool,
        tags: List[str],
        provider: 'Provider',
        *,
        parent_id: Optional[str] = None,
        group: Optional[bool] = None,
        active: Optional[bool] = None,
        url: Optional[str] = None,
        metadata: Optional['CatalogEntryMetadata'] = None,
        id: Optional[str] = None,
        catalog_crn: Optional[str] = None,
        children_url: Optional[str] = None,
        geo_tags: Optional[List[str]] = None,
        pricing_tags: Optional[List[str]] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a CatalogEntry object.

        :param str name: Programmatic name for this catalog entry, which must be
               formatted like a CRN segment. See the display name in OverviewUI for a
               user-readable name.
        :param str kind: The type of catalog entry which determines the type and
               shape of the object. Valid GC types are buildpack, cname, dataset,
               geography, iaas, platform_service, runtime, service, template,
               ui-dashboard.
        :param dict overview_ui: Overview is nested in the top level. The key value
               pair is `[_language_]overview_ui`.
        :param Image images: Image annotation for this catalog entry. The image is
               a URL.
        :param bool disabled: Boolean value that determines the global visibility
               for the catalog entry, and its children. If it is not enabled, all plans
               are disabled.
        :param List[str] tags: A searchable list of tags. For example, IBM, 3rd
               Party, Beta, GA, and Single Tenant. Valid values found at
               https://globalcatalog.test.cloud.ibm.com/search.
        :param Provider provider: Information related to the provider associated
               with a catalog entry.
        :param str parent_id: (optional) The ID of the parent catalog entry if it
               exists.
        :param bool group: (optional) Boolean value that determines whether the
               catalog entry is a group.
        :param bool active: (optional) Boolean value that describes whether the
               service is active.
        :param CatalogEntryMetadata metadata: (optional) Model used to describe
               metadata object returned.
        """
        self.name = name
        self.kind = kind
        self.overview_ui = overview_ui
        self.images = images
        self.parent_id = parent_id
        self.disabled = disabled
        self.tags = tags
        self.group = group
        self.provider = provider
        self.active = active
        self.url = url
        self.metadata = metadata
        self.id = id
        self.catalog_crn = catalog_crn
        self.children_url = children_url
        self.geo_tags = geo_tags
        self.pricing_tags = pricing_tags
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CatalogEntry':
        """Initialize a CatalogEntry object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in CatalogEntry JSON')
        if (kind := _dict.get('kind')) is not None:
            args['kind'] = kind
        else:
            raise ValueError('Required property \'kind\' not present in CatalogEntry JSON')
        if (overview_ui := _dict.get('overview_ui')) is not None:
            args['overview_ui'] = {k: Overview.from_dict(v) for k, v in overview_ui.items()}
        else:
            raise ValueError('Required property \'overview_ui\' not present in CatalogEntry JSON')
        if (images := _dict.get('images')) is not None:
            args['images'] = Image.from_dict(images)
        else:
            raise ValueError('Required property \'images\' not present in CatalogEntry JSON')
        if (parent_id := _dict.get('parent_id')) is not None:
            args['parent_id'] = parent_id
        if (disabled := _dict.get('disabled')) is not None:
            args['disabled'] = disabled
        else:
            raise ValueError('Required property \'disabled\' not present in CatalogEntry JSON')
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        else:
            raise ValueError('Required property \'tags\' not present in CatalogEntry JSON')
        if (group := _dict.get('group')) is not None:
            args['group'] = group
        if (provider := _dict.get('provider')) is not None:
            args['provider'] = Provider.from_dict(provider)
        else:
            raise ValueError('Required property \'provider\' not present in CatalogEntry JSON')
        if (active := _dict.get('active')) is not None:
            args['active'] = active
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = CatalogEntryMetadata.from_dict(metadata)
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (catalog_crn := _dict.get('catalog_crn')) is not None:
            args['catalog_crn'] = catalog_crn
        if (children_url := _dict.get('children_url')) is not None:
            args['children_url'] = children_url
        if (geo_tags := _dict.get('geo_tags')) is not None:
            args['geo_tags'] = geo_tags
        if (pricing_tags := _dict.get('pricing_tags')) is not None:
            args['pricing_tags'] = pricing_tags
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CatalogEntry object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'overview_ui') and self.overview_ui is not None:
            overview_ui_map = {}
            for k, v in self.overview_ui.items():
                if isinstance(v, dict):
                    overview_ui_map[k] = v
                else:
                    overview_ui_map[k] = v.to_dict()
            _dict['overview_ui'] = overview_ui_map
        if hasattr(self, 'images') and self.images is not None:
            if isinstance(self.images, dict):
                _dict['images'] = self.images
            else:
                _dict['images'] = self.images.to_dict()
        if hasattr(self, 'parent_id') and self.parent_id is not None:
            _dict['parent_id'] = self.parent_id
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'group') and self.group is not None:
            _dict['group'] = self.group
        if hasattr(self, 'provider') and self.provider is not None:
            if isinstance(self.provider, dict):
                _dict['provider'] = self.provider
            else:
                _dict['provider'] = self.provider.to_dict()
        if hasattr(self, 'active') and self.active is not None:
            _dict['active'] = self.active
        if hasattr(self, 'url') and getattr(self, 'url') is not None:
            _dict['url'] = getattr(self, 'url')
        if hasattr(self, 'metadata') and self.metadata is not None:
            if isinstance(self.metadata, dict):
                _dict['metadata'] = self.metadata
            else:
                _dict['metadata'] = self.metadata.to_dict()
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'catalog_crn') and getattr(self, 'catalog_crn') is not None:
            _dict['catalog_crn'] = getattr(self, 'catalog_crn')
        if hasattr(self, 'children_url') and getattr(self, 'children_url') is not None:
            _dict['children_url'] = getattr(self, 'children_url')
        if hasattr(self, 'geo_tags') and getattr(self, 'geo_tags') is not None:
            _dict['geo_tags'] = getattr(self, 'geo_tags')
        if hasattr(self, 'pricing_tags') and getattr(self, 'pricing_tags') is not None:
            _dict['pricing_tags'] = getattr(self, 'pricing_tags')
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CatalogEntry object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CatalogEntry') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CatalogEntry') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        The type of catalog entry which determines the type and shape of the object. Valid
        GC types are buildpack, cname, dataset, geography, iaas, platform_service,
        runtime, service, template, ui-dashboard.
        """

        SERVICE = 'service'
        TEMPLATE = 'template'
        DASHBOARD = 'dashboard'


class CatalogEntryMetadata:
    """
    Model used to describe metadata object returned.

    :param bool rc_compatible: (optional) Boolean value that describes whether the
          service is compatible with the Resource Controller. Only settable for
          deployments, propogated upward.
    :param CFMetaData service: (optional) Service-related metadata.
    :param PlanMetaData plan: (optional) Plan-related metadata.
    :param AliasMetaData alias: (optional) Alias-related metadata.
    :param TemplateMetaData template: (optional) Template-related metadata.
    :param UIMetaData ui: (optional) Information related to the UI presentation
          associated with a catalog entry.
    :param List[str] compliance: (optional) Compliance information for HIPAA and
          PCI.
    :param SLAMetaData sla: (optional) Service Level Agreement related metadata.
    :param Callbacks callbacks: (optional) Callback-related information associated
          with a catalog entry.
    :param str original_name: (optional) The original name of the object.
    :param str version: (optional) Deprecated: Optional version of the object. Only
          valid for templates.
    :param dict other: (optional) Additional information.
    :param CatalogEntryMetadataPricing pricing: (optional) Pricing-related
          information.
    :param CatalogEntryMetadataDeployment deployment: (optional) Deployment-related
          metadata.
    """

    def __init__(
        self,
        *,
        rc_compatible: Optional[bool] = None,
        service: Optional['CFMetaData'] = None,
        plan: Optional['PlanMetaData'] = None,
        alias: Optional['AliasMetaData'] = None,
        template: Optional['TemplateMetaData'] = None,
        ui: Optional['UIMetaData'] = None,
        compliance: Optional[List[str]] = None,
        sla: Optional['SLAMetaData'] = None,
        callbacks: Optional['Callbacks'] = None,
        original_name: Optional[str] = None,
        version: Optional[str] = None,
        other: Optional[dict] = None,
        pricing: Optional['CatalogEntryMetadataPricing'] = None,
        deployment: Optional['CatalogEntryMetadataDeployment'] = None,
    ) -> None:
        """
        Initialize a CatalogEntryMetadata object.

        :param bool rc_compatible: (optional) Boolean value that describes whether
               the service is compatible with the Resource Controller. Only settable for
               deployments, propogated upward.
        :param CFMetaData service: (optional) Service-related metadata.
        :param PlanMetaData plan: (optional) Plan-related metadata.
        :param AliasMetaData alias: (optional) Alias-related metadata.
        :param TemplateMetaData template: (optional) Template-related metadata.
        :param UIMetaData ui: (optional) Information related to the UI presentation
               associated with a catalog entry.
        :param List[str] compliance: (optional) Compliance information for HIPAA
               and PCI.
        :param SLAMetaData sla: (optional) Service Level Agreement related
               metadata.
        :param Callbacks callbacks: (optional) Callback-related information
               associated with a catalog entry.
        :param str original_name: (optional) The original name of the object.
        :param str version: (optional) Deprecated: Optional version of the object.
               Only valid for templates.
        :param dict other: (optional) Additional information.
        :param CatalogEntryMetadataPricing pricing: (optional) Pricing-related
               information.
        :param CatalogEntryMetadataDeployment deployment: (optional)
               Deployment-related metadata.
        """
        self.rc_compatible = rc_compatible
        self.service = service
        self.plan = plan
        self.alias = alias
        self.template = template
        self.ui = ui
        self.compliance = compliance
        self.sla = sla
        self.callbacks = callbacks
        self.original_name = original_name
        self.version = version
        self.other = other
        self.pricing = pricing
        self.deployment = deployment

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CatalogEntryMetadata':
        """Initialize a CatalogEntryMetadata object from a json dictionary."""
        args = {}
        if (rc_compatible := _dict.get('rc_compatible')) is not None:
            args['rc_compatible'] = rc_compatible
        if (service := _dict.get('service')) is not None:
            args['service'] = CFMetaData.from_dict(service)
        if (plan := _dict.get('plan')) is not None:
            args['plan'] = PlanMetaData.from_dict(plan)
        if (alias := _dict.get('alias')) is not None:
            args['alias'] = AliasMetaData.from_dict(alias)
        if (template := _dict.get('template')) is not None:
            args['template'] = TemplateMetaData.from_dict(template)
        if (ui := _dict.get('ui')) is not None:
            args['ui'] = UIMetaData.from_dict(ui)
        if (compliance := _dict.get('compliance')) is not None:
            args['compliance'] = compliance
        if (sla := _dict.get('sla')) is not None:
            args['sla'] = SLAMetaData.from_dict(sla)
        if (callbacks := _dict.get('callbacks')) is not None:
            args['callbacks'] = Callbacks.from_dict(callbacks)
        if (original_name := _dict.get('original_name')) is not None:
            args['original_name'] = original_name
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        if (other := _dict.get('other')) is not None:
            args['other'] = other
        if (pricing := _dict.get('pricing')) is not None:
            args['pricing'] = CatalogEntryMetadataPricing.from_dict(pricing)
        if (deployment := _dict.get('deployment')) is not None:
            args['deployment'] = CatalogEntryMetadataDeployment.from_dict(deployment)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CatalogEntryMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rc_compatible') and self.rc_compatible is not None:
            _dict['rc_compatible'] = self.rc_compatible
        if hasattr(self, 'service') and self.service is not None:
            if isinstance(self.service, dict):
                _dict['service'] = self.service
            else:
                _dict['service'] = self.service.to_dict()
        if hasattr(self, 'plan') and self.plan is not None:
            if isinstance(self.plan, dict):
                _dict['plan'] = self.plan
            else:
                _dict['plan'] = self.plan.to_dict()
        if hasattr(self, 'alias') and self.alias is not None:
            if isinstance(self.alias, dict):
                _dict['alias'] = self.alias
            else:
                _dict['alias'] = self.alias.to_dict()
        if hasattr(self, 'template') and self.template is not None:
            if isinstance(self.template, dict):
                _dict['template'] = self.template
            else:
                _dict['template'] = self.template.to_dict()
        if hasattr(self, 'ui') and self.ui is not None:
            if isinstance(self.ui, dict):
                _dict['ui'] = self.ui
            else:
                _dict['ui'] = self.ui.to_dict()
        if hasattr(self, 'compliance') and self.compliance is not None:
            _dict['compliance'] = self.compliance
        if hasattr(self, 'sla') and self.sla is not None:
            if isinstance(self.sla, dict):
                _dict['sla'] = self.sla
            else:
                _dict['sla'] = self.sla.to_dict()
        if hasattr(self, 'callbacks') and self.callbacks is not None:
            if isinstance(self.callbacks, dict):
                _dict['callbacks'] = self.callbacks
            else:
                _dict['callbacks'] = self.callbacks.to_dict()
        if hasattr(self, 'original_name') and self.original_name is not None:
            _dict['original_name'] = self.original_name
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'other') and self.other is not None:
            _dict['other'] = self.other
        if hasattr(self, 'pricing') and self.pricing is not None:
            if isinstance(self.pricing, dict):
                _dict['pricing'] = self.pricing
            else:
                _dict['pricing'] = self.pricing.to_dict()
        if hasattr(self, 'deployment') and self.deployment is not None:
            if isinstance(self.deployment, dict):
                _dict['deployment'] = self.deployment
            else:
                _dict['deployment'] = self.deployment.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CatalogEntryMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CatalogEntryMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CatalogEntryMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CatalogEntryMetadataDeployment:
    """
    Deployment-related metadata.

    :param str location: (optional) Describes the region where the service is
          located.
    :param str location_url: (optional) Pointer to the location resource in the
          catalog.
    :param str original_location: (optional) The original region in which this
          deployment existed.
    :param str target_crn: (optional) A CRN that describes the deployment.
          crn:v1:[cname]:[ctype]:[location]:[scope]::[resource-type]:[resource].
    :param str service_crn: (optional) Cloud resource name for this deployment.
    :param str mccp_id: (optional) Deprecated: ID of the multi cloud connectivity
          platform.
    :param Broker broker: (optional) The broker associated with a catalog entry.
    :param bool supports_rc_migration: (optional) Deprecated: This deployment not
          only supports RC but is ready to migrate and support the RC broker for a
          location.
    :param str target_network: (optional) When using the service_endpoint_supported
          tag for a deployment, this optional field can be set on a deployment to denote
          the supported service endpoint type (cse_private, public, or
          cse_private+public).
    """

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        location_url: Optional[str] = None,
        original_location: Optional[str] = None,
        target_crn: Optional[str] = None,
        service_crn: Optional[str] = None,
        mccp_id: Optional[str] = None,
        broker: Optional['Broker'] = None,
        supports_rc_migration: Optional[bool] = None,
        target_network: Optional[str] = None,
    ) -> None:
        """
        Initialize a CatalogEntryMetadataDeployment object.

        :param str location: (optional) Describes the region where the service is
               located.
        :param str original_location: (optional) The original region in which this
               deployment existed.
        :param str target_crn: (optional) A CRN that describes the deployment.
               crn:v1:[cname]:[ctype]:[location]:[scope]::[resource-type]:[resource].
        :param str service_crn: (optional) Cloud resource name for this deployment.
        :param str mccp_id: (optional) Deprecated: ID of the multi cloud
               connectivity platform.
        :param Broker broker: (optional) The broker associated with a catalog
               entry.
        :param bool supports_rc_migration: (optional) Deprecated: This deployment
               not only supports RC but is ready to migrate and support the RC broker for
               a location.
        :param str target_network: (optional) When using the
               service_endpoint_supported tag for a deployment, this optional field can be
               set on a deployment to denote the supported service endpoint type
               (cse_private, public, or cse_private+public).
        """
        self.location = location
        self.location_url = location_url
        self.original_location = original_location
        self.target_crn = target_crn
        self.service_crn = service_crn
        self.mccp_id = mccp_id
        self.broker = broker
        self.supports_rc_migration = supports_rc_migration
        self.target_network = target_network

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CatalogEntryMetadataDeployment':
        """Initialize a CatalogEntryMetadataDeployment object from a json dictionary."""
        args = {}
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        if (location_url := _dict.get('location_url')) is not None:
            args['location_url'] = location_url
        if (original_location := _dict.get('original_location')) is not None:
            args['original_location'] = original_location
        if (target_crn := _dict.get('target_crn')) is not None:
            args['target_crn'] = target_crn
        if (service_crn := _dict.get('service_crn')) is not None:
            args['service_crn'] = service_crn
        if (mccp_id := _dict.get('mccp_id')) is not None:
            args['mccp_id'] = mccp_id
        if (broker := _dict.get('broker')) is not None:
            args['broker'] = Broker.from_dict(broker)
        if (supports_rc_migration := _dict.get('supports_rc_migration')) is not None:
            args['supports_rc_migration'] = supports_rc_migration
        if (target_network := _dict.get('target_network')) is not None:
            args['target_network'] = target_network
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CatalogEntryMetadataDeployment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'location_url') and getattr(self, 'location_url') is not None:
            _dict['location_url'] = getattr(self, 'location_url')
        if hasattr(self, 'original_location') and self.original_location is not None:
            _dict['original_location'] = self.original_location
        if hasattr(self, 'target_crn') and self.target_crn is not None:
            _dict['target_crn'] = self.target_crn
        if hasattr(self, 'service_crn') and self.service_crn is not None:
            _dict['service_crn'] = self.service_crn
        if hasattr(self, 'mccp_id') and self.mccp_id is not None:
            _dict['mccp_id'] = self.mccp_id
        if hasattr(self, 'broker') and self.broker is not None:
            if isinstance(self.broker, dict):
                _dict['broker'] = self.broker
            else:
                _dict['broker'] = self.broker.to_dict()
        if hasattr(self, 'supports_rc_migration') and self.supports_rc_migration is not None:
            _dict['supports_rc_migration'] = self.supports_rc_migration
        if hasattr(self, 'target_network') and self.target_network is not None:
            _dict['target_network'] = self.target_network
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CatalogEntryMetadataDeployment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CatalogEntryMetadataDeployment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CatalogEntryMetadataDeployment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CatalogEntryMetadataPricing:
    """
    Pricing-related information.

    :param str type: (optional) Type of plan. Valid values are `free`, `trial`,
          `paygo`, `paid`, `subscription`.
    :param str origin: (optional) Defines where the pricing originates.
    :param StartingPrice starting_price: (optional) Plan-specific starting price
          information.
    :param str deployment_id: (optional) The deployment object id this pricing is
          from. Only set if object kind is deployment.
    :param str deployment_location: (optional) The deployment location this pricing
          is from. Only set if object kind is deployment.
    :param str deployment_region: (optional) If price is for a deployment object
          then the region in the pricing catalog of the deployment object will be here. To
          be valid, this value must be contained within deployment_regions.
    :param bool deployment_location_no_price_available: (optional) Is the location
          price not available. Only set in api /pricing/deployment and only set if true.
          This means for the given deployment object there was no pricing set in pricing
          catalog.
    :param List[Metrics] metrics: (optional) Plan-specific cost metric structure.
    :param List[str] deployment_regions: (optional) List of regions where region
          pricing is available. Only set on global deployments if enabled by owner.
    :param datetime effective_from: (optional) The start date-time indicating when
          this pricing plan takes effect.
    :param datetime effective_until: (optional) The end date-time indicating when
          this pricing plan is no longer in effect.
    :param bool require_login: (optional) Boolean value indicating whether or not
          this pricing plan requires login to get pricing data.
    :param str pricing_catalog_url: (optional) URL to the entry for this plan on the
          pricing catalog.
    :param List[str] sales_avenue: (optional) Tags describing how this plan was
          purchased (catalog [default], seller, private offer). Currently only settable on
          MCSP subscription plans.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        origin: Optional[str] = None,
        starting_price: Optional['StartingPrice'] = None,
        deployment_id: Optional[str] = None,
        deployment_location: Optional[str] = None,
        deployment_region: Optional[str] = None,
        deployment_location_no_price_available: Optional[bool] = None,
        metrics: Optional[List['Metrics']] = None,
        deployment_regions: Optional[List[str]] = None,
        effective_from: Optional[datetime] = None,
        effective_until: Optional[datetime] = None,
        require_login: Optional[bool] = None,
        pricing_catalog_url: Optional[str] = None,
        sales_avenue: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a CatalogEntryMetadataPricing object.

        :param str type: (optional) Type of plan. Valid values are `free`, `trial`,
               `paygo`, `paid`, `subscription`.
        :param str origin: (optional) Defines where the pricing originates.
        :param StartingPrice starting_price: (optional) Plan-specific starting
               price information.
        :param str deployment_id: (optional) The deployment object id this pricing
               is from. Only set if object kind is deployment.
        :param str deployment_location: (optional) The deployment location this
               pricing is from. Only set if object kind is deployment.
        :param str deployment_region: (optional) If price is for a deployment
               object then the region in the pricing catalog of the deployment object will
               be here. To be valid, this value must be contained within
               deployment_regions.
        :param bool deployment_location_no_price_available: (optional) Is the
               location price not available. Only set in api /pricing/deployment and only
               set if true. This means for the given deployment object there was no
               pricing set in pricing catalog.
        :param List[Metrics] metrics: (optional) Plan-specific cost metric
               structure.
        :param List[str] deployment_regions: (optional) List of regions where
               region pricing is available. Only set on global deployments if enabled by
               owner.
        :param datetime effective_from: (optional) The start date-time indicating
               when this pricing plan takes effect.
        :param datetime effective_until: (optional) The end date-time indicating
               when this pricing plan is no longer in effect.
        :param bool require_login: (optional) Boolean value indicating whether or
               not this pricing plan requires login to get pricing data.
        :param str pricing_catalog_url: (optional) URL to the entry for this plan
               on the pricing catalog.
        :param List[str] sales_avenue: (optional) Tags describing how this plan was
               purchased (catalog [default], seller, private offer). Currently only
               settable on MCSP subscription plans.
        """
        self.type = type
        self.origin = origin
        self.starting_price = starting_price
        self.deployment_id = deployment_id
        self.deployment_location = deployment_location
        self.deployment_region = deployment_region
        self.deployment_location_no_price_available = deployment_location_no_price_available
        self.metrics = metrics
        self.deployment_regions = deployment_regions
        self.effective_from = effective_from
        self.effective_until = effective_until
        self.require_login = require_login
        self.pricing_catalog_url = pricing_catalog_url
        self.sales_avenue = sales_avenue

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CatalogEntryMetadataPricing':
        """Initialize a CatalogEntryMetadataPricing object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (origin := _dict.get('origin')) is not None:
            args['origin'] = origin
        if (starting_price := _dict.get('starting_price')) is not None:
            args['starting_price'] = StartingPrice.from_dict(starting_price)
        if (deployment_id := _dict.get('deployment_id')) is not None:
            args['deployment_id'] = deployment_id
        if (deployment_location := _dict.get('deployment_location')) is not None:
            args['deployment_location'] = deployment_location
        if (deployment_region := _dict.get('deployment_region')) is not None:
            args['deployment_region'] = deployment_region
        if (deployment_location_no_price_available := _dict.get('deployment_location_no_price_available')) is not None:
            args['deployment_location_no_price_available'] = deployment_location_no_price_available
        if (metrics := _dict.get('metrics')) is not None:
            args['metrics'] = [Metrics.from_dict(v) for v in metrics]
        if (deployment_regions := _dict.get('deployment_regions')) is not None:
            args['deployment_regions'] = deployment_regions
        if (effective_from := _dict.get('effective_from')) is not None:
            args['effective_from'] = string_to_datetime(effective_from)
        if (effective_until := _dict.get('effective_until')) is not None:
            args['effective_until'] = string_to_datetime(effective_until)
        if (require_login := _dict.get('require_login')) is not None:
            args['require_login'] = require_login
        if (pricing_catalog_url := _dict.get('pricing_catalog_url')) is not None:
            args['pricing_catalog_url'] = pricing_catalog_url
        if (sales_avenue := _dict.get('sales_avenue')) is not None:
            args['sales_avenue'] = sales_avenue
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CatalogEntryMetadataPricing object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'origin') and self.origin is not None:
            _dict['origin'] = self.origin
        if hasattr(self, 'starting_price') and self.starting_price is not None:
            if isinstance(self.starting_price, dict):
                _dict['starting_price'] = self.starting_price
            else:
                _dict['starting_price'] = self.starting_price.to_dict()
        if hasattr(self, 'deployment_id') and self.deployment_id is not None:
            _dict['deployment_id'] = self.deployment_id
        if hasattr(self, 'deployment_location') and self.deployment_location is not None:
            _dict['deployment_location'] = self.deployment_location
        if hasattr(self, 'deployment_region') and self.deployment_region is not None:
            _dict['deployment_region'] = self.deployment_region
        if (
            hasattr(self, 'deployment_location_no_price_available')
            and self.deployment_location_no_price_available is not None
        ):
            _dict['deployment_location_no_price_available'] = self.deployment_location_no_price_available
        if hasattr(self, 'metrics') and self.metrics is not None:
            metrics_list = []
            for v in self.metrics:
                if isinstance(v, dict):
                    metrics_list.append(v)
                else:
                    metrics_list.append(v.to_dict())
            _dict['metrics'] = metrics_list
        if hasattr(self, 'deployment_regions') and self.deployment_regions is not None:
            _dict['deployment_regions'] = self.deployment_regions
        if hasattr(self, 'effective_from') and self.effective_from is not None:
            _dict['effective_from'] = datetime_to_string(self.effective_from)
        if hasattr(self, 'effective_until') and self.effective_until is not None:
            _dict['effective_until'] = datetime_to_string(self.effective_until)
        if hasattr(self, 'require_login') and self.require_login is not None:
            _dict['require_login'] = self.require_login
        if hasattr(self, 'pricing_catalog_url') and self.pricing_catalog_url is not None:
            _dict['pricing_catalog_url'] = self.pricing_catalog_url
        if hasattr(self, 'sales_avenue') and self.sales_avenue is not None:
            _dict['sales_avenue'] = self.sales_avenue
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CatalogEntryMetadataPricing object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CatalogEntryMetadataPricing') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CatalogEntryMetadataPricing') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DRMetaData:
    """
    SLA Disaster Recovery-related metadata.

    :param bool dr: (optional) Required boolean value that describes whether
          disaster recovery is on.
    :param str description: (optional) Description of the disaster recovery
          implementation.
    """

    def __init__(
        self,
        *,
        dr: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> None:
        """
        Initialize a DRMetaData object.

        :param bool dr: (optional) Required boolean value that describes whether
               disaster recovery is on.
        :param str description: (optional) Description of the disaster recovery
               implementation.
        """
        self.dr = dr
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DRMetaData':
        """Initialize a DRMetaData object from a json dictionary."""
        args = {}
        if (dr := _dict.get('dr')) is not None:
            args['dr'] = dr
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DRMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dr') and self.dr is not None:
            _dict['dr'] = self.dr
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DRMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DRMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DRMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeploymentBase:
    """
    Deployment-related metadata.

    :param str location: (optional) Describes the region where the service is
          located.
    :param str location_url: (optional) URL of deployment.
    :param str original_location: (optional) The original region in which this
          deployment existed.
    :param str target_crn: (optional) A CRN that describes the deployment.
          crn:v1:[cname]:[ctype]:[location]:[scope]::[resource-type]:[resource].
    :param str service_crn: (optional) Cloud resource name for this deployment.
    :param str mccp_id: (optional) Deprecated: ID of the multi cloud connectivity
          platform.
    :param Broker broker: (optional) The broker associated with a catalog entry.
    :param bool supports_rc_migration: (optional) Deprecated: This deployment not
          only supports RC but is ready to migrate and support the RC broker for a
          location.
    :param str target_network: (optional) When using the service_endpoint_supported
          tag for a deployment, this optional field can be set on a deployment to denote
          the supported service endpoint type (cse_private, public, or
          cse_private+public).
    """

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        location_url: Optional[str] = None,
        original_location: Optional[str] = None,
        target_crn: Optional[str] = None,
        service_crn: Optional[str] = None,
        mccp_id: Optional[str] = None,
        broker: Optional['Broker'] = None,
        supports_rc_migration: Optional[bool] = None,
        target_network: Optional[str] = None,
    ) -> None:
        """
        Initialize a DeploymentBase object.

        :param str location: (optional) Describes the region where the service is
               located.
        :param str location_url: (optional) URL of deployment.
        :param str original_location: (optional) The original region in which this
               deployment existed.
        :param str target_crn: (optional) A CRN that describes the deployment.
               crn:v1:[cname]:[ctype]:[location]:[scope]::[resource-type]:[resource].
        :param str service_crn: (optional) Cloud resource name for this deployment.
        :param str mccp_id: (optional) Deprecated: ID of the multi cloud
               connectivity platform.
        :param Broker broker: (optional) The broker associated with a catalog
               entry.
        :param bool supports_rc_migration: (optional) Deprecated: This deployment
               not only supports RC but is ready to migrate and support the RC broker for
               a location.
        :param str target_network: (optional) When using the
               service_endpoint_supported tag for a deployment, this optional field can be
               set on a deployment to denote the supported service endpoint type
               (cse_private, public, or cse_private+public).
        """
        self.location = location
        self.location_url = location_url
        self.original_location = original_location
        self.target_crn = target_crn
        self.service_crn = service_crn
        self.mccp_id = mccp_id
        self.broker = broker
        self.supports_rc_migration = supports_rc_migration
        self.target_network = target_network

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeploymentBase':
        """Initialize a DeploymentBase object from a json dictionary."""
        args = {}
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        if (location_url := _dict.get('location_url')) is not None:
            args['location_url'] = location_url
        if (original_location := _dict.get('original_location')) is not None:
            args['original_location'] = original_location
        if (target_crn := _dict.get('target_crn')) is not None:
            args['target_crn'] = target_crn
        if (service_crn := _dict.get('service_crn')) is not None:
            args['service_crn'] = service_crn
        if (mccp_id := _dict.get('mccp_id')) is not None:
            args['mccp_id'] = mccp_id
        if (broker := _dict.get('broker')) is not None:
            args['broker'] = Broker.from_dict(broker)
        if (supports_rc_migration := _dict.get('supports_rc_migration')) is not None:
            args['supports_rc_migration'] = supports_rc_migration
        if (target_network := _dict.get('target_network')) is not None:
            args['target_network'] = target_network
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeploymentBase object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'location_url') and self.location_url is not None:
            _dict['location_url'] = self.location_url
        if hasattr(self, 'original_location') and self.original_location is not None:
            _dict['original_location'] = self.original_location
        if hasattr(self, 'target_crn') and self.target_crn is not None:
            _dict['target_crn'] = self.target_crn
        if hasattr(self, 'service_crn') and self.service_crn is not None:
            _dict['service_crn'] = self.service_crn
        if hasattr(self, 'mccp_id') and self.mccp_id is not None:
            _dict['mccp_id'] = self.mccp_id
        if hasattr(self, 'broker') and self.broker is not None:
            if isinstance(self.broker, dict):
                _dict['broker'] = self.broker
            else:
                _dict['broker'] = self.broker.to_dict()
        if hasattr(self, 'supports_rc_migration') and self.supports_rc_migration is not None:
            _dict['supports_rc_migration'] = self.supports_rc_migration
        if hasattr(self, 'target_network') and self.target_network is not None:
            _dict['target_network'] = self.target_network
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeploymentBase object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeploymentBase') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeploymentBase') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntrySearchResult:
    """
    A paginated search result containing catalog entries.

    :param int offset: (optional) The offset (origin 0) of the first resource in
          this page of search results.
    :param int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :param int count: (optional) The overall total number of resources in the search
          result set.
    :param int resource_count: (optional) The number of resources returned in this
          page of search results.
    :param str first: (optional) A URL for retrieving the first page of search
          results.
    :param str last: (optional) A URL for retrieving the last page of search
          results.
    :param str prev: (optional) A URL for retrieving the previous page of search
          results.
    :param str next: (optional) A URL for retrieving the next page of search
          results.
    :param List[CatalogEntry] resources: (optional) The resources (catalog entries)
          contained in this page of search results.
    """

    def __init__(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        count: Optional[int] = None,
        resource_count: Optional[int] = None,
        first: Optional[str] = None,
        last: Optional[str] = None,
        prev: Optional[str] = None,
        next: Optional[str] = None,
        resources: Optional[List['CatalogEntry']] = None,
    ) -> None:
        """
        Initialize a EntrySearchResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int count: (optional) The overall total number of resources in the
               search result set.
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
        :param List[CatalogEntry] resources: (optional) The resources (catalog
               entries) contained in this page of search results.
        """
        self.offset = offset
        self.limit = limit
        self.count = count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntrySearchResult':
        """Initialize a EntrySearchResult object from a json dictionary."""
        args = {}
        if (offset := _dict.get('offset')) is not None:
            args['offset'] = offset
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (resource_count := _dict.get('resource_count')) is not None:
            args['resource_count'] = resource_count
        if (first := _dict.get('first')) is not None:
            args['first'] = first
        if (last := _dict.get('last')) is not None:
            args['last'] = last
        if (prev := _dict.get('prev')) is not None:
            args['prev'] = prev
        if (next := _dict.get('next')) is not None:
            args['next'] = next
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [CatalogEntry.from_dict(v) for v in resources]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntrySearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
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
            resources_list = []
            for v in self.resources:
                if isinstance(v, dict):
                    resources_list.append(v)
                else:
                    resources_list.append(v.to_dict())
            _dict['resources'] = resources_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EntrySearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EntrySearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntrySearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Image:
    """
    Image annotation for this catalog entry. The image is a URL.

    :param str image: URL for the large, default image.
    :param str small_image: (optional) URL for a small image.
    :param str medium_image: (optional) URL for a medium image.
    :param str feature_image: (optional) URL for a featured image.
    """

    def __init__(
        self,
        image: str,
        *,
        small_image: Optional[str] = None,
        medium_image: Optional[str] = None,
        feature_image: Optional[str] = None,
    ) -> None:
        """
        Initialize a Image object.

        :param str image: URL for the large, default image.
        :param str small_image: (optional) URL for a small image.
        :param str medium_image: (optional) URL for a medium image.
        :param str feature_image: (optional) URL for a featured image.
        """
        self.image = image
        self.small_image = small_image
        self.medium_image = medium_image
        self.feature_image = feature_image

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Image':
        """Initialize a Image object from a json dictionary."""
        args = {}
        if (image := _dict.get('image')) is not None:
            args['image'] = image
        else:
            raise ValueError('Required property \'image\' not present in Image JSON')
        if (small_image := _dict.get('small_image')) is not None:
            args['small_image'] = small_image
        if (medium_image := _dict.get('medium_image')) is not None:
            args['medium_image'] = medium_image
        if (feature_image := _dict.get('feature_image')) is not None:
            args['feature_image'] = feature_image
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
        if hasattr(self, 'small_image') and self.small_image is not None:
            _dict['small_image'] = self.small_image
        if hasattr(self, 'medium_image') and self.medium_image is not None:
            _dict['medium_image'] = self.medium_image
        if hasattr(self, 'feature_image') and self.feature_image is not None:
            _dict['feature_image'] = self.feature_image
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


class Message:
    """
    log object describing who did what.

    :param str id: (optional) id of catalog entry.
    :param Visibility effective: (optional) Information related to the visibility of
          a catalog entry.
    :param datetime time: (optional) time of action.
    :param str who_id: (optional) user ID of person who did action.
    :param str who_name: (optional) name of person who did action.
    :param str who_email: (optional) user email of person who did action.
    :param str instance: (optional) Global catalog instance where this occured.
    :param str gid: (optional) transaction id associatd with action.
    :param str type: (optional) type of action taken.
    :param str message: (optional) message describing action.
    :param dict data: (optional) An object containing details on changes made to
          object data.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        effective: Optional['Visibility'] = None,
        time: Optional[datetime] = None,
        who_id: Optional[str] = None,
        who_name: Optional[str] = None,
        who_email: Optional[str] = None,
        instance: Optional[str] = None,
        gid: Optional[str] = None,
        type: Optional[str] = None,
        message: Optional[str] = None,
        data: Optional[dict] = None,
    ) -> None:
        """
        Initialize a Message object.

        :param str id: (optional) id of catalog entry.
        :param Visibility effective: (optional) Information related to the
               visibility of a catalog entry.
        :param datetime time: (optional) time of action.
        :param str who_id: (optional) user ID of person who did action.
        :param str who_name: (optional) name of person who did action.
        :param str who_email: (optional) user email of person who did action.
        :param str instance: (optional) Global catalog instance where this occured.
        :param str gid: (optional) transaction id associatd with action.
        :param str type: (optional) type of action taken.
        :param str message: (optional) message describing action.
        :param dict data: (optional) An object containing details on changes made
               to object data.
        """
        self.id = id
        self.effective = effective
        self.time = time
        self.who_id = who_id
        self.who_name = who_name
        self.who_email = who_email
        self.instance = instance
        self.gid = gid
        self.type = type
        self.message = message
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Message':
        """Initialize a Message object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (effective := _dict.get('effective')) is not None:
            args['effective'] = Visibility.from_dict(effective)
        if (time := _dict.get('time')) is not None:
            args['time'] = string_to_datetime(time)
        if (who_id := _dict.get('who_id')) is not None:
            args['who_id'] = who_id
        if (who_name := _dict.get('who_name')) is not None:
            args['who_name'] = who_name
        if (who_email := _dict.get('who_email')) is not None:
            args['who_email'] = who_email
        if (instance := _dict.get('instance')) is not None:
            args['instance'] = instance
        if (gid := _dict.get('gid')) is not None:
            args['gid'] = gid
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        if (data := _dict.get('data')) is not None:
            args['data'] = data
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Message object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'effective') and self.effective is not None:
            if isinstance(self.effective, dict):
                _dict['effective'] = self.effective
            else:
                _dict['effective'] = self.effective.to_dict()
        if hasattr(self, 'time') and self.time is not None:
            _dict['time'] = datetime_to_string(self.time)
        if hasattr(self, 'who_id') and self.who_id is not None:
            _dict['who_id'] = self.who_id
        if hasattr(self, 'who_name') and self.who_name is not None:
            _dict['who_name'] = self.who_name
        if hasattr(self, 'who_email') and self.who_email is not None:
            _dict['who_email'] = self.who_email
        if hasattr(self, 'instance') and self.instance is not None:
            _dict['instance'] = self.instance
        if hasattr(self, 'gid') and self.gid is not None:
            _dict['gid'] = self.gid
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Message object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Message') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Message') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Metrics:
    """
    Plan-specific cost metrics information.

    :param str part_ref: (optional) The reference guid for the part.
    :param str metric_id: (optional) The metric ID or part number.
    :param str tier_model: (optional) The pricing tier type used to calculate the
          marginal unit price. Follows simple, graduated or block tier styles.
    :param str charge_unit: (optional) The unit to be charged under this metric.
    :param str charge_unit_name: (optional) The name associated with a charge unit
          to provide context.
    :param int charge_unit_quantity: (optional) The quantity associated with the
          charge unit to determine price change intervals.
    :param str resource_display_name: (optional) The display name of the resource
          tied to the charge unit of this metric.
    :param str charge_unit_display_name: (optional) Display name of the charge unit
          to be rendered human readable by the UI.
    :param int usage_cap_qty: (optional) Upper bound for the usage under the parent
          metric.
    :param int display_cap: (optional) The display capacity for the UI.
    :param datetime effective_from: (optional) The end date-time indicating when
          this metric is no longer in effect.
    :param datetime effective_until: (optional) The start date-time indicating when
          this metric takes effect.
    :param List[Amount] amounts: (optional) The pricing per metric by country and
          currency.
    :param dict additional_properties: (optional) A property-bag like extension to
          metric metadata.
    """

    def __init__(
        self,
        *,
        part_ref: Optional[str] = None,
        metric_id: Optional[str] = None,
        tier_model: Optional[str] = None,
        charge_unit: Optional[str] = None,
        charge_unit_name: Optional[str] = None,
        charge_unit_quantity: Optional[int] = None,
        resource_display_name: Optional[str] = None,
        charge_unit_display_name: Optional[str] = None,
        usage_cap_qty: Optional[int] = None,
        display_cap: Optional[int] = None,
        effective_from: Optional[datetime] = None,
        effective_until: Optional[datetime] = None,
        amounts: Optional[List['Amount']] = None,
        additional_properties: Optional[dict] = None,
    ) -> None:
        """
        Initialize a Metrics object.

        :param str part_ref: (optional) The reference guid for the part.
        :param str metric_id: (optional) The metric ID or part number.
        :param str tier_model: (optional) The pricing tier type used to calculate
               the marginal unit price. Follows simple, graduated or block tier styles.
        :param str charge_unit: (optional) The unit to be charged under this
               metric.
        :param str charge_unit_name: (optional) The name associated with a charge
               unit to provide context.
        :param int charge_unit_quantity: (optional) The quantity associated with
               the charge unit to determine price change intervals.
        :param str resource_display_name: (optional) The display name of the
               resource tied to the charge unit of this metric.
        :param str charge_unit_display_name: (optional) Display name of the charge
               unit to be rendered human readable by the UI.
        :param int usage_cap_qty: (optional) Upper bound for the usage under the
               parent metric.
        :param int display_cap: (optional) The display capacity for the UI.
        :param datetime effective_from: (optional) The end date-time indicating
               when this metric is no longer in effect.
        :param datetime effective_until: (optional) The start date-time indicating
               when this metric takes effect.
        :param List[Amount] amounts: (optional) The pricing per metric by country
               and currency.
        :param dict additional_properties: (optional) A property-bag like extension
               to metric metadata.
        """
        self.part_ref = part_ref
        self.metric_id = metric_id
        self.tier_model = tier_model
        self.charge_unit = charge_unit
        self.charge_unit_name = charge_unit_name
        self.charge_unit_quantity = charge_unit_quantity
        self.resource_display_name = resource_display_name
        self.charge_unit_display_name = charge_unit_display_name
        self.usage_cap_qty = usage_cap_qty
        self.display_cap = display_cap
        self.effective_from = effective_from
        self.effective_until = effective_until
        self.amounts = amounts
        self.additional_properties = additional_properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Metrics':
        """Initialize a Metrics object from a json dictionary."""
        args = {}
        if (part_ref := _dict.get('part_ref')) is not None:
            args['part_ref'] = part_ref
        if (metric_id := _dict.get('metric_id')) is not None:
            args['metric_id'] = metric_id
        if (tier_model := _dict.get('tier_model')) is not None:
            args['tier_model'] = tier_model
        if (charge_unit := _dict.get('charge_unit')) is not None:
            args['charge_unit'] = charge_unit
        if (charge_unit_name := _dict.get('charge_unit_name')) is not None:
            args['charge_unit_name'] = charge_unit_name
        if (charge_unit_quantity := _dict.get('charge_unit_quantity')) is not None:
            args['charge_unit_quantity'] = charge_unit_quantity
        if (resource_display_name := _dict.get('resource_display_name')) is not None:
            args['resource_display_name'] = resource_display_name
        if (charge_unit_display_name := _dict.get('charge_unit_display_name')) is not None:
            args['charge_unit_display_name'] = charge_unit_display_name
        if (usage_cap_qty := _dict.get('usage_cap_qty')) is not None:
            args['usage_cap_qty'] = usage_cap_qty
        if (display_cap := _dict.get('display_cap')) is not None:
            args['display_cap'] = display_cap
        if (effective_from := _dict.get('effective_from')) is not None:
            args['effective_from'] = string_to_datetime(effective_from)
        if (effective_until := _dict.get('effective_until')) is not None:
            args['effective_until'] = string_to_datetime(effective_until)
        if (amounts := _dict.get('amounts')) is not None:
            args['amounts'] = [Amount.from_dict(v) for v in amounts]
        if (additional_properties := _dict.get('additional_properties')) is not None:
            args['additional_properties'] = additional_properties
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Metrics object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'part_ref') and self.part_ref is not None:
            _dict['part_ref'] = self.part_ref
        if hasattr(self, 'metric_id') and self.metric_id is not None:
            _dict['metric_id'] = self.metric_id
        if hasattr(self, 'tier_model') and self.tier_model is not None:
            _dict['tier_model'] = self.tier_model
        if hasattr(self, 'charge_unit') and self.charge_unit is not None:
            _dict['charge_unit'] = self.charge_unit
        if hasattr(self, 'charge_unit_name') and self.charge_unit_name is not None:
            _dict['charge_unit_name'] = self.charge_unit_name
        if hasattr(self, 'charge_unit_quantity') and self.charge_unit_quantity is not None:
            _dict['charge_unit_quantity'] = self.charge_unit_quantity
        if hasattr(self, 'resource_display_name') and self.resource_display_name is not None:
            _dict['resource_display_name'] = self.resource_display_name
        if hasattr(self, 'charge_unit_display_name') and self.charge_unit_display_name is not None:
            _dict['charge_unit_display_name'] = self.charge_unit_display_name
        if hasattr(self, 'usage_cap_qty') and self.usage_cap_qty is not None:
            _dict['usage_cap_qty'] = self.usage_cap_qty
        if hasattr(self, 'display_cap') and self.display_cap is not None:
            _dict['display_cap'] = self.display_cap
        if hasattr(self, 'effective_from') and self.effective_from is not None:
            _dict['effective_from'] = datetime_to_string(self.effective_from)
        if hasattr(self, 'effective_until') and self.effective_until is not None:
            _dict['effective_until'] = datetime_to_string(self.effective_until)
        if hasattr(self, 'amounts') and self.amounts is not None:
            amounts_list = []
            for v in self.amounts:
                if isinstance(v, dict):
                    amounts_list.append(v)
                else:
                    amounts_list.append(v.to_dict())
            _dict['amounts'] = amounts_list
        if hasattr(self, 'additional_properties') and self.additional_properties is not None:
            _dict['additional_properties'] = self.additional_properties
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Metrics object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Metrics') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Metrics') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ObjectMetadataSet:
    """
    Model used to describe metadata object that can be set.

    :param bool rc_compatible: (optional) Boolean value that describes whether the
          service is compatible with the Resource Controller. Only settable for
          deployments, propogated upward.
    :param CFMetaData service: (optional) Service-related metadata.
    :param PlanMetaData plan: (optional) Plan-related metadata.
    :param AliasMetaData alias: (optional) Alias-related metadata.
    :param TemplateMetaData template: (optional) Template-related metadata.
    :param UIMetaData ui: (optional) Information related to the UI presentation
          associated with a catalog entry.
    :param List[str] compliance: (optional) Compliance information for HIPAA and
          PCI.
    :param SLAMetaData sla: (optional) Service Level Agreement related metadata.
    :param Callbacks callbacks: (optional) Callback-related information associated
          with a catalog entry.
    :param str original_name: (optional) The original name of the object.
    :param str version: (optional) Deprecated: Optional version of the object. Only
          valid for templates.
    :param dict other: (optional) Additional information.
    :param PricingSet pricing: (optional) Pricing-related information.
    :param DeploymentBase deployment: (optional) Deployment-related metadata.
    """

    def __init__(
        self,
        *,
        rc_compatible: Optional[bool] = None,
        service: Optional['CFMetaData'] = None,
        plan: Optional['PlanMetaData'] = None,
        alias: Optional['AliasMetaData'] = None,
        template: Optional['TemplateMetaData'] = None,
        ui: Optional['UIMetaData'] = None,
        compliance: Optional[List[str]] = None,
        sla: Optional['SLAMetaData'] = None,
        callbacks: Optional['Callbacks'] = None,
        original_name: Optional[str] = None,
        version: Optional[str] = None,
        other: Optional[dict] = None,
        pricing: Optional['PricingSet'] = None,
        deployment: Optional['DeploymentBase'] = None,
    ) -> None:
        """
        Initialize a ObjectMetadataSet object.

        :param bool rc_compatible: (optional) Boolean value that describes whether
               the service is compatible with the Resource Controller. Only settable for
               deployments, propogated upward.
        :param CFMetaData service: (optional) Service-related metadata.
        :param PlanMetaData plan: (optional) Plan-related metadata.
        :param AliasMetaData alias: (optional) Alias-related metadata.
        :param TemplateMetaData template: (optional) Template-related metadata.
        :param UIMetaData ui: (optional) Information related to the UI presentation
               associated with a catalog entry.
        :param List[str] compliance: (optional) Compliance information for HIPAA
               and PCI.
        :param SLAMetaData sla: (optional) Service Level Agreement related
               metadata.
        :param Callbacks callbacks: (optional) Callback-related information
               associated with a catalog entry.
        :param str original_name: (optional) The original name of the object.
        :param str version: (optional) Deprecated: Optional version of the object.
               Only valid for templates.
        :param dict other: (optional) Additional information.
        :param PricingSet pricing: (optional) Pricing-related information.
        :param DeploymentBase deployment: (optional) Deployment-related metadata.
        """
        self.rc_compatible = rc_compatible
        self.service = service
        self.plan = plan
        self.alias = alias
        self.template = template
        self.ui = ui
        self.compliance = compliance
        self.sla = sla
        self.callbacks = callbacks
        self.original_name = original_name
        self.version = version
        self.other = other
        self.pricing = pricing
        self.deployment = deployment

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectMetadataSet':
        """Initialize a ObjectMetadataSet object from a json dictionary."""
        args = {}
        if (rc_compatible := _dict.get('rc_compatible')) is not None:
            args['rc_compatible'] = rc_compatible
        if (service := _dict.get('service')) is not None:
            args['service'] = CFMetaData.from_dict(service)
        if (plan := _dict.get('plan')) is not None:
            args['plan'] = PlanMetaData.from_dict(plan)
        if (alias := _dict.get('alias')) is not None:
            args['alias'] = AliasMetaData.from_dict(alias)
        if (template := _dict.get('template')) is not None:
            args['template'] = TemplateMetaData.from_dict(template)
        if (ui := _dict.get('ui')) is not None:
            args['ui'] = UIMetaData.from_dict(ui)
        if (compliance := _dict.get('compliance')) is not None:
            args['compliance'] = compliance
        if (sla := _dict.get('sla')) is not None:
            args['sla'] = SLAMetaData.from_dict(sla)
        if (callbacks := _dict.get('callbacks')) is not None:
            args['callbacks'] = Callbacks.from_dict(callbacks)
        if (original_name := _dict.get('original_name')) is not None:
            args['original_name'] = original_name
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        if (other := _dict.get('other')) is not None:
            args['other'] = other
        if (pricing := _dict.get('pricing')) is not None:
            args['pricing'] = PricingSet.from_dict(pricing)
        if (deployment := _dict.get('deployment')) is not None:
            args['deployment'] = DeploymentBase.from_dict(deployment)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectMetadataSet object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rc_compatible') and self.rc_compatible is not None:
            _dict['rc_compatible'] = self.rc_compatible
        if hasattr(self, 'service') and self.service is not None:
            if isinstance(self.service, dict):
                _dict['service'] = self.service
            else:
                _dict['service'] = self.service.to_dict()
        if hasattr(self, 'plan') and self.plan is not None:
            if isinstance(self.plan, dict):
                _dict['plan'] = self.plan
            else:
                _dict['plan'] = self.plan.to_dict()
        if hasattr(self, 'alias') and self.alias is not None:
            if isinstance(self.alias, dict):
                _dict['alias'] = self.alias
            else:
                _dict['alias'] = self.alias.to_dict()
        if hasattr(self, 'template') and self.template is not None:
            if isinstance(self.template, dict):
                _dict['template'] = self.template
            else:
                _dict['template'] = self.template.to_dict()
        if hasattr(self, 'ui') and self.ui is not None:
            if isinstance(self.ui, dict):
                _dict['ui'] = self.ui
            else:
                _dict['ui'] = self.ui.to_dict()
        if hasattr(self, 'compliance') and self.compliance is not None:
            _dict['compliance'] = self.compliance
        if hasattr(self, 'sla') and self.sla is not None:
            if isinstance(self.sla, dict):
                _dict['sla'] = self.sla
            else:
                _dict['sla'] = self.sla.to_dict()
        if hasattr(self, 'callbacks') and self.callbacks is not None:
            if isinstance(self.callbacks, dict):
                _dict['callbacks'] = self.callbacks
            else:
                _dict['callbacks'] = self.callbacks.to_dict()
        if hasattr(self, 'original_name') and self.original_name is not None:
            _dict['original_name'] = self.original_name
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'other') and self.other is not None:
            _dict['other'] = self.other
        if hasattr(self, 'pricing') and self.pricing is not None:
            if isinstance(self.pricing, dict):
                _dict['pricing'] = self.pricing
            else:
                _dict['pricing'] = self.pricing.to_dict()
        if hasattr(self, 'deployment') and self.deployment is not None:
            if isinstance(self.deployment, dict):
                _dict['deployment'] = self.deployment
            else:
                _dict['deployment'] = self.deployment.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectMetadataSet object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ObjectMetadataSet') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectMetadataSet') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Overview:
    """
    Overview is nested in the top level. The key value pair is `[_language_]overview_ui`.

    :param str display_name: The translated display name.
    :param str long_description: The translated long description.
    :param str description: The translated description.
    :param str featured_description: (optional) The translated description that will
          be featured.
    """

    def __init__(
        self,
        display_name: str,
        long_description: str,
        description: str,
        *,
        featured_description: Optional[str] = None,
    ) -> None:
        """
        Initialize a Overview object.

        :param str display_name: The translated display name.
        :param str long_description: The translated long description.
        :param str description: The translated description.
        :param str featured_description: (optional) The translated description that
               will be featured.
        """
        self.display_name = display_name
        self.long_description = long_description
        self.description = description
        self.featured_description = featured_description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Overview':
        """Initialize a Overview object from a json dictionary."""
        args = {}
        if (display_name := _dict.get('display_name')) is not None:
            args['display_name'] = display_name
        else:
            raise ValueError('Required property \'display_name\' not present in Overview JSON')
        if (long_description := _dict.get('long_description')) is not None:
            args['long_description'] = long_description
        else:
            raise ValueError('Required property \'long_description\' not present in Overview JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in Overview JSON')
        if (featured_description := _dict.get('featured_description')) is not None:
            args['featured_description'] = featured_description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Overview object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'long_description') and self.long_description is not None:
            _dict['long_description'] = self.long_description
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'featured_description') and self.featured_description is not None:
            _dict['featured_description'] = self.featured_description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Overview object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Overview') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Overview') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PlanMetaData:
    """
    Plan-related metadata.

    :param bool bindable: (optional) Boolean value that describes whether the
          service can be bound to an application. If true then this will create and use
          resource keys.
    :param bool reservable: (optional) Boolean value that describes whether the
          service can be reserved for pricing subscriptions.
    :param bool allow_internal_users: (optional) Boolean value that describes
          whether the service can be used on IBM accounts. If false this cannot be
          onboarded by an IBM account.
    :param bool async_provisioning_supported: (optional) Deprecated: Boolean value
          that describes whether the service supports asynchronous provisioning. Now
          handled by a 202 response indicating support from the broker on provisioning.
    :param bool async_unprovisioning_supported: (optional) Deprecated: Boolean value
          that describes whether the service supports asynchronous unprovisioning. Now
          handled by a 202 response indicating support from the broker on unprovisioning.
    :param str provision_type: (optional) How the subscription is provisioned
          (managed cloud service provider (mcsp), IBM_cloud, legacy).
    :param int test_check_interval: (optional) Deprecated: A unit of time that
          determines the time in between uptime checks to be performed by the Estado
          testing service.
    :param str single_scope_instance: (optional) Deprecated: String denoting if a
          single instance is shared among a group of users. E.g. org.
    :param bool service_check_enabled: (optional) Deprecated: Boolean value that
          describes whether the Estado testing service will perform uptime tests for this
          service.
    :param dict cf_guid: (optional) Deprecated: If the field is imported from Cloud
          Foundry, the Cloud Foundry region's GUID. This is a required field. For example,
          `us-south=123`.
    """

    def __init__(
        self,
        *,
        bindable: Optional[bool] = None,
        reservable: Optional[bool] = None,
        allow_internal_users: Optional[bool] = None,
        async_provisioning_supported: Optional[bool] = None,
        async_unprovisioning_supported: Optional[bool] = None,
        provision_type: Optional[str] = None,
        test_check_interval: Optional[int] = None,
        single_scope_instance: Optional[str] = None,
        service_check_enabled: Optional[bool] = None,
        cf_guid: Optional[dict] = None,
    ) -> None:
        """
        Initialize a PlanMetaData object.

        :param bool bindable: (optional) Boolean value that describes whether the
               service can be bound to an application. If true then this will create and
               use resource keys.
        :param bool reservable: (optional) Boolean value that describes whether the
               service can be reserved for pricing subscriptions.
        :param bool allow_internal_users: (optional) Boolean value that describes
               whether the service can be used on IBM accounts. If false this cannot be
               onboarded by an IBM account.
        :param bool async_provisioning_supported: (optional) Deprecated: Boolean
               value that describes whether the service supports asynchronous
               provisioning. Now handled by a 202 response indicating support from the
               broker on provisioning.
        :param bool async_unprovisioning_supported: (optional) Deprecated: Boolean
               value that describes whether the service supports asynchronous
               unprovisioning. Now handled by a 202 response indicating support from the
               broker on unprovisioning.
        :param str provision_type: (optional) How the subscription is provisioned
               (managed cloud service provider (mcsp), IBM_cloud, legacy).
        :param int test_check_interval: (optional) Deprecated: A unit of time that
               determines the time in between uptime checks to be performed by the Estado
               testing service.
        :param str single_scope_instance: (optional) Deprecated: String denoting if
               a single instance is shared among a group of users. E.g. org.
        :param bool service_check_enabled: (optional) Deprecated: Boolean value
               that describes whether the Estado testing service will perform uptime tests
               for this service.
        :param dict cf_guid: (optional) Deprecated: If the field is imported from
               Cloud Foundry, the Cloud Foundry region's GUID. This is a required field.
               For example, `us-south=123`.
        """
        self.bindable = bindable
        self.reservable = reservable
        self.allow_internal_users = allow_internal_users
        self.async_provisioning_supported = async_provisioning_supported
        self.async_unprovisioning_supported = async_unprovisioning_supported
        self.provision_type = provision_type
        self.test_check_interval = test_check_interval
        self.single_scope_instance = single_scope_instance
        self.service_check_enabled = service_check_enabled
        self.cf_guid = cf_guid

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PlanMetaData':
        """Initialize a PlanMetaData object from a json dictionary."""
        args = {}
        if (bindable := _dict.get('bindable')) is not None:
            args['bindable'] = bindable
        if (reservable := _dict.get('reservable')) is not None:
            args['reservable'] = reservable
        if (allow_internal_users := _dict.get('allow_internal_users')) is not None:
            args['allow_internal_users'] = allow_internal_users
        if (async_provisioning_supported := _dict.get('async_provisioning_supported')) is not None:
            args['async_provisioning_supported'] = async_provisioning_supported
        if (async_unprovisioning_supported := _dict.get('async_unprovisioning_supported')) is not None:
            args['async_unprovisioning_supported'] = async_unprovisioning_supported
        if (provision_type := _dict.get('provision_type')) is not None:
            args['provision_type'] = provision_type
        if (test_check_interval := _dict.get('test_check_interval')) is not None:
            args['test_check_interval'] = test_check_interval
        if (single_scope_instance := _dict.get('single_scope_instance')) is not None:
            args['single_scope_instance'] = single_scope_instance
        if (service_check_enabled := _dict.get('service_check_enabled')) is not None:
            args['service_check_enabled'] = service_check_enabled
        if (cf_guid := _dict.get('cf_guid')) is not None:
            args['cf_guid'] = cf_guid
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PlanMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bindable') and self.bindable is not None:
            _dict['bindable'] = self.bindable
        if hasattr(self, 'reservable') and self.reservable is not None:
            _dict['reservable'] = self.reservable
        if hasattr(self, 'allow_internal_users') and self.allow_internal_users is not None:
            _dict['allow_internal_users'] = self.allow_internal_users
        if hasattr(self, 'async_provisioning_supported') and self.async_provisioning_supported is not None:
            _dict['async_provisioning_supported'] = self.async_provisioning_supported
        if hasattr(self, 'async_unprovisioning_supported') and self.async_unprovisioning_supported is not None:
            _dict['async_unprovisioning_supported'] = self.async_unprovisioning_supported
        if hasattr(self, 'provision_type') and self.provision_type is not None:
            _dict['provision_type'] = self.provision_type
        if hasattr(self, 'test_check_interval') and self.test_check_interval is not None:
            _dict['test_check_interval'] = self.test_check_interval
        if hasattr(self, 'single_scope_instance') and self.single_scope_instance is not None:
            _dict['single_scope_instance'] = self.single_scope_instance
        if hasattr(self, 'service_check_enabled') and self.service_check_enabled is not None:
            _dict['service_check_enabled'] = self.service_check_enabled
        if hasattr(self, 'cf_guid') and self.cf_guid is not None:
            _dict['cf_guid'] = self.cf_guid
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PlanMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PlanMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PlanMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Price:
    """
    Pricing-related information.

    :param int quantity_tier: (optional) The quantity of _metric_ associated with
          the current price point.
    :param float price: (optional) Price in the selected currency.
    """

    def __init__(
        self,
        *,
        quantity_tier: Optional[int] = None,
        price: Optional[float] = None,
    ) -> None:
        """
        Initialize a Price object.

        :param int quantity_tier: (optional) The quantity of _metric_ associated
               with the current price point.
        :param float price: (optional) Price in the selected currency.
        """
        self.quantity_tier = quantity_tier
        self.price = price

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Price':
        """Initialize a Price object from a json dictionary."""
        args = {}
        if (quantity_tier := _dict.get('quantity_tier')) is not None:
            args['quantity_tier'] = quantity_tier
        if (price := _dict.get('price')) is not None:
            args['price'] = price
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Price object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'quantity_tier') and self.quantity_tier is not None:
            _dict['quantity_tier'] = self.quantity_tier
        if hasattr(self, 'price') and self.price is not None:
            _dict['price'] = self.price
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Price object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Price') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Price') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PricingGet:
    """
    Pricing-related information.

    :param str deployment_id: (optional) The deployment object id this pricing is
          from. Only set if object kind is deployment.
    :param str deployment_location: (optional) The deployment location this pricing
          is from. Only set if object kind is deployment.
    :param str deployment_region: (optional) If price is for a deployment object
          then the region in the pricing catalog of the deployment object will be here. To
          be valid, this value must be contained within deployment_regions.
    :param bool deployment_location_no_price_available: (optional) Is the location
          price not available. Only set in api /pricing/deployment and only set if true.
          This means for the given deployment object there was no pricing set in pricing
          catalog.
    :param str type: (optional) Type of plan. Valid values are `free`, `trial`,
          `paygo`, `paid`, `subscription`.
    :param str origin: (optional) Defines where the pricing originates.
    :param StartingPrice starting_price: (optional) Plan-specific starting price
          information.
    :param List[Metrics] metrics: (optional) Plan-specific cost metric structure.
    :param List[str] deployment_regions: (optional) List of regions where region
          pricing is available. Only set on global deployments if enabled by owner.
    :param datetime effective_from: (optional) The start date-time indicating when
          this pricing plan takes effect.
    :param datetime effective_until: (optional) The end date-time indicating when
          this pricing plan is no longer in effect.
    :param bool require_login: (optional) Boolean value indicating whether or not
          this pricing plan requires login to get pricing data.
    :param str pricing_catalog_url: (optional) URL to the entry for this plan on the
          pricing catalog.
    :param List[str] sales_avenue: (optional) Tags describing how this plan was
          purchased (catalog [default], seller, private offer). Currently only settable on
          MCSP subscription plans.
    """

    def __init__(
        self,
        *,
        deployment_id: Optional[str] = None,
        deployment_location: Optional[str] = None,
        deployment_region: Optional[str] = None,
        deployment_location_no_price_available: Optional[bool] = None,
        type: Optional[str] = None,
        origin: Optional[str] = None,
        starting_price: Optional['StartingPrice'] = None,
        metrics: Optional[List['Metrics']] = None,
        deployment_regions: Optional[List[str]] = None,
        effective_from: Optional[datetime] = None,
        effective_until: Optional[datetime] = None,
        require_login: Optional[bool] = None,
        pricing_catalog_url: Optional[str] = None,
        sales_avenue: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a PricingGet object.

        :param str deployment_id: (optional) The deployment object id this pricing
               is from. Only set if object kind is deployment.
        :param str deployment_location: (optional) The deployment location this
               pricing is from. Only set if object kind is deployment.
        :param str deployment_region: (optional) If price is for a deployment
               object then the region in the pricing catalog of the deployment object will
               be here. To be valid, this value must be contained within
               deployment_regions.
        :param bool deployment_location_no_price_available: (optional) Is the
               location price not available. Only set in api /pricing/deployment and only
               set if true. This means for the given deployment object there was no
               pricing set in pricing catalog.
        :param str type: (optional) Type of plan. Valid values are `free`, `trial`,
               `paygo`, `paid`, `subscription`.
        :param str origin: (optional) Defines where the pricing originates.
        :param StartingPrice starting_price: (optional) Plan-specific starting
               price information.
        :param List[Metrics] metrics: (optional) Plan-specific cost metric
               structure.
        :param List[str] deployment_regions: (optional) List of regions where
               region pricing is available. Only set on global deployments if enabled by
               owner.
        :param datetime effective_from: (optional) The start date-time indicating
               when this pricing plan takes effect.
        :param datetime effective_until: (optional) The end date-time indicating
               when this pricing plan is no longer in effect.
        :param bool require_login: (optional) Boolean value indicating whether or
               not this pricing plan requires login to get pricing data.
        :param str pricing_catalog_url: (optional) URL to the entry for this plan
               on the pricing catalog.
        :param List[str] sales_avenue: (optional) Tags describing how this plan was
               purchased (catalog [default], seller, private offer). Currently only
               settable on MCSP subscription plans.
        """
        self.deployment_id = deployment_id
        self.deployment_location = deployment_location
        self.deployment_region = deployment_region
        self.deployment_location_no_price_available = deployment_location_no_price_available
        self.type = type
        self.origin = origin
        self.starting_price = starting_price
        self.metrics = metrics
        self.deployment_regions = deployment_regions
        self.effective_from = effective_from
        self.effective_until = effective_until
        self.require_login = require_login
        self.pricing_catalog_url = pricing_catalog_url
        self.sales_avenue = sales_avenue

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PricingGet':
        """Initialize a PricingGet object from a json dictionary."""
        args = {}
        if (deployment_id := _dict.get('deployment_id')) is not None:
            args['deployment_id'] = deployment_id
        if (deployment_location := _dict.get('deployment_location')) is not None:
            args['deployment_location'] = deployment_location
        if (deployment_region := _dict.get('deployment_region')) is not None:
            args['deployment_region'] = deployment_region
        if (deployment_location_no_price_available := _dict.get('deployment_location_no_price_available')) is not None:
            args['deployment_location_no_price_available'] = deployment_location_no_price_available
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (origin := _dict.get('origin')) is not None:
            args['origin'] = origin
        if (starting_price := _dict.get('starting_price')) is not None:
            args['starting_price'] = StartingPrice.from_dict(starting_price)
        if (metrics := _dict.get('metrics')) is not None:
            args['metrics'] = [Metrics.from_dict(v) for v in metrics]
        if (deployment_regions := _dict.get('deployment_regions')) is not None:
            args['deployment_regions'] = deployment_regions
        if (effective_from := _dict.get('effective_from')) is not None:
            args['effective_from'] = string_to_datetime(effective_from)
        if (effective_until := _dict.get('effective_until')) is not None:
            args['effective_until'] = string_to_datetime(effective_until)
        if (require_login := _dict.get('require_login')) is not None:
            args['require_login'] = require_login
        if (pricing_catalog_url := _dict.get('pricing_catalog_url')) is not None:
            args['pricing_catalog_url'] = pricing_catalog_url
        if (sales_avenue := _dict.get('sales_avenue')) is not None:
            args['sales_avenue'] = sales_avenue
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PricingGet object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deployment_id') and self.deployment_id is not None:
            _dict['deployment_id'] = self.deployment_id
        if hasattr(self, 'deployment_location') and self.deployment_location is not None:
            _dict['deployment_location'] = self.deployment_location
        if hasattr(self, 'deployment_region') and self.deployment_region is not None:
            _dict['deployment_region'] = self.deployment_region
        if (
            hasattr(self, 'deployment_location_no_price_available')
            and self.deployment_location_no_price_available is not None
        ):
            _dict['deployment_location_no_price_available'] = self.deployment_location_no_price_available
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'origin') and self.origin is not None:
            _dict['origin'] = self.origin
        if hasattr(self, 'starting_price') and self.starting_price is not None:
            if isinstance(self.starting_price, dict):
                _dict['starting_price'] = self.starting_price
            else:
                _dict['starting_price'] = self.starting_price.to_dict()
        if hasattr(self, 'metrics') and self.metrics is not None:
            metrics_list = []
            for v in self.metrics:
                if isinstance(v, dict):
                    metrics_list.append(v)
                else:
                    metrics_list.append(v.to_dict())
            _dict['metrics'] = metrics_list
        if hasattr(self, 'deployment_regions') and self.deployment_regions is not None:
            _dict['deployment_regions'] = self.deployment_regions
        if hasattr(self, 'effective_from') and self.effective_from is not None:
            _dict['effective_from'] = datetime_to_string(self.effective_from)
        if hasattr(self, 'effective_until') and self.effective_until is not None:
            _dict['effective_until'] = datetime_to_string(self.effective_until)
        if hasattr(self, 'require_login') and self.require_login is not None:
            _dict['require_login'] = self.require_login
        if hasattr(self, 'pricing_catalog_url') and self.pricing_catalog_url is not None:
            _dict['pricing_catalog_url'] = self.pricing_catalog_url
        if hasattr(self, 'sales_avenue') and self.sales_avenue is not None:
            _dict['sales_avenue'] = self.sales_avenue
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PricingGet object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PricingGet') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PricingGet') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PricingSearchResult:
    """
    A paginated result containing pricing entries.

    :param int offset: (optional) The offset (origin 0) of the first resource in
          this page of search results.
    :param int limit: (optional) The maximum number of resources returned in each
          page of search results.
    :param int count: (optional) The overall total number of resources in the search
          result set.
    :param int resource_count: (optional) The number of resources returned in this
          page of search results.
    :param str first: (optional) A URL for retrieving the first page of search
          results.
    :param str last: (optional) A URL for retrieving the last page of search
          results.
    :param str prev: (optional) A URL for retrieving the previous page of search
          results.
    :param str next: (optional) A URL for retrieving the next page of search
          results.
    :param List[PricingGet] resources: (optional) The resources (prices) contained
          in this page of search results.
    """

    def __init__(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        count: Optional[int] = None,
        resource_count: Optional[int] = None,
        first: Optional[str] = None,
        last: Optional[str] = None,
        prev: Optional[str] = None,
        next: Optional[str] = None,
        resources: Optional[List['PricingGet']] = None,
    ) -> None:
        """
        Initialize a PricingSearchResult object.

        :param int offset: (optional) The offset (origin 0) of the first resource
               in this page of search results.
        :param int limit: (optional) The maximum number of resources returned in
               each page of search results.
        :param int count: (optional) The overall total number of resources in the
               search result set.
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
        :param List[PricingGet] resources: (optional) The resources (prices)
               contained in this page of search results.
        """
        self.offset = offset
        self.limit = limit
        self.count = count
        self.resource_count = resource_count
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PricingSearchResult':
        """Initialize a PricingSearchResult object from a json dictionary."""
        args = {}
        if (offset := _dict.get('offset')) is not None:
            args['offset'] = offset
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (resource_count := _dict.get('resource_count')) is not None:
            args['resource_count'] = resource_count
        if (first := _dict.get('first')) is not None:
            args['first'] = first
        if (last := _dict.get('last')) is not None:
            args['last'] = last
        if (prev := _dict.get('prev')) is not None:
            args['prev'] = prev
        if (next := _dict.get('next')) is not None:
            args['next'] = next
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [PricingGet.from_dict(v) for v in resources]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PricingSearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
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
            resources_list = []
            for v in self.resources:
                if isinstance(v, dict):
                    resources_list.append(v)
                else:
                    resources_list.append(v.to_dict())
            _dict['resources'] = resources_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PricingSearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PricingSearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PricingSearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PricingSet:
    """
    Pricing-related information.

    :param str type: (optional) Type of plan. Valid values are `free`, `trial`,
          `paygo`, `paid`, `subscription`.
    :param str origin: (optional) Defines where the pricing originates, either the
          pricing catalog or the global catalog.
    :param StartingPrice starting_price: (optional) Plan-specific starting price
          information.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        origin: Optional[str] = None,
        starting_price: Optional['StartingPrice'] = None,
    ) -> None:
        """
        Initialize a PricingSet object.

        :param str type: (optional) Type of plan. Valid values are `free`, `trial`,
               `paygo`, `paid`, `subscription`.
        :param str origin: (optional) Defines where the pricing originates, either
               the pricing catalog or the global catalog.
        :param StartingPrice starting_price: (optional) Plan-specific starting
               price information.
        """
        self.type = type
        self.origin = origin
        self.starting_price = starting_price

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PricingSet':
        """Initialize a PricingSet object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (origin := _dict.get('origin')) is not None:
            args['origin'] = origin
        if (starting_price := _dict.get('starting_price')) is not None:
            args['starting_price'] = StartingPrice.from_dict(starting_price)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PricingSet object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'origin') and self.origin is not None:
            _dict['origin'] = self.origin
        if hasattr(self, 'starting_price') and self.starting_price is not None:
            if isinstance(self.starting_price, dict):
                _dict['starting_price'] = self.starting_price
            else:
                _dict['starting_price'] = self.starting_price.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PricingSet object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PricingSet') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PricingSet') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Provider:
    """
    Information related to the provider associated with a catalog entry.

    :param str email: Provider's email address for this catalog entry.
    :param str name: Provider's name, for example, IBM.
    :param str contact: (optional) Provider's contact name.
    :param str support_email: (optional) Provider's support email.
    :param str phone: (optional) Provider's contact phone.
    """

    def __init__(
        self,
        email: str,
        name: str,
        *,
        contact: Optional[str] = None,
        support_email: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> None:
        """
        Initialize a Provider object.

        :param str email: Provider's email address for this catalog entry.
        :param str name: Provider's name, for example, IBM.
        :param str contact: (optional) Provider's contact name.
        :param str support_email: (optional) Provider's support email.
        :param str phone: (optional) Provider's contact phone.
        """
        self.email = email
        self.name = name
        self.contact = contact
        self.support_email = support_email
        self.phone = phone

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Provider':
        """Initialize a Provider object from a json dictionary."""
        args = {}
        if (email := _dict.get('email')) is not None:
            args['email'] = email
        else:
            raise ValueError('Required property \'email\' not present in Provider JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Provider JSON')
        if (contact := _dict.get('contact')) is not None:
            args['contact'] = contact
        if (support_email := _dict.get('support_email')) is not None:
            args['support_email'] = support_email
        if (phone := _dict.get('phone')) is not None:
            args['phone'] = phone
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Provider object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = self.email
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'contact') and self.contact is not None:
            _dict['contact'] = self.contact
        if hasattr(self, 'support_email') and self.support_email is not None:
            _dict['support_email'] = self.support_email
        if hasattr(self, 'phone') and self.phone is not None:
            _dict['phone'] = self.phone
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Provider object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Provider') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Provider') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SLAMetaData:
    """
    Service Level Agreement related metadata.

    :param str terms: (optional) Required Service License Agreement Terms of Use.
    :param str tenancy: (optional) Required deployment type. Valid values are
          dedicated, local, or public. It can be Single or Multi tennancy, more
          specifically on a Server, VM, Physical, or Pod.
    :param float provisioning: (optional) Provisioning reliability, for example,
          99.95.
    :param float responsiveness: (optional) Uptime reliability of the service, for
          example, 99.95.
    :param DRMetaData dr: (optional) SLA Disaster Recovery-related metadata.
    """

    def __init__(
        self,
        *,
        terms: Optional[str] = None,
        tenancy: Optional[str] = None,
        provisioning: Optional[float] = None,
        responsiveness: Optional[float] = None,
        dr: Optional['DRMetaData'] = None,
    ) -> None:
        """
        Initialize a SLAMetaData object.

        :param str terms: (optional) Required Service License Agreement Terms of
               Use.
        :param str tenancy: (optional) Required deployment type. Valid values are
               dedicated, local, or public. It can be Single or Multi tennancy, more
               specifically on a Server, VM, Physical, or Pod.
        :param float provisioning: (optional) Provisioning reliability, for
               example, 99.95.
        :param float responsiveness: (optional) Uptime reliability of the service,
               for example, 99.95.
        :param DRMetaData dr: (optional) SLA Disaster Recovery-related metadata.
        """
        self.terms = terms
        self.tenancy = tenancy
        self.provisioning = provisioning
        self.responsiveness = responsiveness
        self.dr = dr

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SLAMetaData':
        """Initialize a SLAMetaData object from a json dictionary."""
        args = {}
        if (terms := _dict.get('terms')) is not None:
            args['terms'] = terms
        if (tenancy := _dict.get('tenancy')) is not None:
            args['tenancy'] = tenancy
        if (provisioning := _dict.get('provisioning')) is not None:
            args['provisioning'] = provisioning
        if (responsiveness := _dict.get('responsiveness')) is not None:
            args['responsiveness'] = responsiveness
        if (dr := _dict.get('dr')) is not None:
            args['dr'] = DRMetaData.from_dict(dr)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SLAMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'terms') and self.terms is not None:
            _dict['terms'] = self.terms
        if hasattr(self, 'tenancy') and self.tenancy is not None:
            _dict['tenancy'] = self.tenancy
        if hasattr(self, 'provisioning') and self.provisioning is not None:
            _dict['provisioning'] = self.provisioning
        if hasattr(self, 'responsiveness') and self.responsiveness is not None:
            _dict['responsiveness'] = self.responsiveness
        if hasattr(self, 'dr') and self.dr is not None:
            if isinstance(self.dr, dict):
                _dict['dr'] = self.dr
            else:
                _dict['dr'] = self.dr.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SLAMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SLAMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SLAMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SourceMetaData:
    """
    Location of your applications source files.

    :param str path: (optional) Path to your application.
    :param str type: (optional) Type of source, for example, git.
    :param str url: (optional) URL to source.
    """

    def __init__(
        self,
        *,
        path: Optional[str] = None,
        type: Optional[str] = None,
        url: Optional[str] = None,
    ) -> None:
        """
        Initialize a SourceMetaData object.

        :param str path: (optional) Path to your application.
        :param str type: (optional) Type of source, for example, git.
        :param str url: (optional) URL to source.
        """
        self.path = path
        self.type = type
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SourceMetaData':
        """Initialize a SourceMetaData object from a json dictionary."""
        args = {}
        if (path := _dict.get('path')) is not None:
            args['path'] = path
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SourceMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SourceMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SourceMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SourceMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StartingPrice:
    """
    Plan-specific starting price information.

    :param str plan_id: (optional) ID of the plan the starting price is calculated.
    :param str deployment_id: (optional) ID of the deployment the starting price is
          calculated.
    :param str unit: (optional) Pricing unit.
    :param List[Amount] amount: (optional) The pricing per metric by country and
          currency.
    """

    def __init__(
        self,
        *,
        plan_id: Optional[str] = None,
        deployment_id: Optional[str] = None,
        unit: Optional[str] = None,
        amount: Optional[List['Amount']] = None,
    ) -> None:
        """
        Initialize a StartingPrice object.

        :param str plan_id: (optional) ID of the plan the starting price is
               calculated.
        :param str deployment_id: (optional) ID of the deployment the starting
               price is calculated.
        :param str unit: (optional) Pricing unit.
        :param List[Amount] amount: (optional) The pricing per metric by country
               and currency.
        """
        self.plan_id = plan_id
        self.deployment_id = deployment_id
        self.unit = unit
        self.amount = amount

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StartingPrice':
        """Initialize a StartingPrice object from a json dictionary."""
        args = {}
        if (plan_id := _dict.get('plan_id')) is not None:
            args['plan_id'] = plan_id
        if (deployment_id := _dict.get('deployment_id')) is not None:
            args['deployment_id'] = deployment_id
        if (unit := _dict.get('unit')) is not None:
            args['unit'] = unit
        if (amount := _dict.get('amount')) is not None:
            args['amount'] = [Amount.from_dict(v) for v in amount]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StartingPrice object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'plan_id') and self.plan_id is not None:
            _dict['plan_id'] = self.plan_id
        if hasattr(self, 'deployment_id') and self.deployment_id is not None:
            _dict['deployment_id'] = self.deployment_id
        if hasattr(self, 'unit') and self.unit is not None:
            _dict['unit'] = self.unit
        if hasattr(self, 'amount') and self.amount is not None:
            amount_list = []
            for v in self.amount:
                if isinstance(v, dict):
                    amount_list.append(v)
                else:
                    amount_list.append(v.to_dict())
            _dict['amount'] = amount_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StartingPrice object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StartingPrice') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StartingPrice') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Strings:
    """
    Information related to a translated text message.

    :param List[Bullets] bullets: (optional) Presentation information related to
          list delimiters.
    :param List[UIMetaMedia] media: (optional) Media-related metadata.
    :param str not_creatable_msg: (optional) Warning that a message is not
          creatable.
    :param str not_creatable_robot_msg: (optional) Warning that a robot message is
          not creatable.
    :param str deprecation_warning: (optional) Warning for deprecation.
    :param str popup_warning_message: (optional) Popup warning message.
    :param str instruction: (optional) Instructions for UI strings.
    """

    def __init__(
        self,
        *,
        bullets: Optional[List['Bullets']] = None,
        media: Optional[List['UIMetaMedia']] = None,
        not_creatable_msg: Optional[str] = None,
        not_creatable_robot_msg: Optional[str] = None,
        deprecation_warning: Optional[str] = None,
        popup_warning_message: Optional[str] = None,
        instruction: Optional[str] = None,
    ) -> None:
        """
        Initialize a Strings object.

        :param List[Bullets] bullets: (optional) Presentation information related
               to list delimiters.
        :param List[UIMetaMedia] media: (optional) Media-related metadata.
        :param str not_creatable_msg: (optional) Warning that a message is not
               creatable.
        :param str not_creatable_robot_msg: (optional) Warning that a robot message
               is not creatable.
        :param str deprecation_warning: (optional) Warning for deprecation.
        :param str popup_warning_message: (optional) Popup warning message.
        :param str instruction: (optional) Instructions for UI strings.
        """
        self.bullets = bullets
        self.media = media
        self.not_creatable_msg = not_creatable_msg
        self.not_creatable_robot_msg = not_creatable_robot_msg
        self.deprecation_warning = deprecation_warning
        self.popup_warning_message = popup_warning_message
        self.instruction = instruction

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Strings':
        """Initialize a Strings object from a json dictionary."""
        args = {}
        if (bullets := _dict.get('bullets')) is not None:
            args['bullets'] = [Bullets.from_dict(v) for v in bullets]
        if (media := _dict.get('media')) is not None:
            args['media'] = [UIMetaMedia.from_dict(v) for v in media]
        if (not_creatable_msg := _dict.get('not_creatable_msg')) is not None:
            args['not_creatable_msg'] = not_creatable_msg
        if (not_creatable_robot_msg := _dict.get('not_creatable__robot_msg')) is not None:
            args['not_creatable_robot_msg'] = not_creatable_robot_msg
        if (deprecation_warning := _dict.get('deprecation_warning')) is not None:
            args['deprecation_warning'] = deprecation_warning
        if (popup_warning_message := _dict.get('popup_warning_message')) is not None:
            args['popup_warning_message'] = popup_warning_message
        if (instruction := _dict.get('instruction')) is not None:
            args['instruction'] = instruction
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Strings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bullets') and self.bullets is not None:
            bullets_list = []
            for v in self.bullets:
                if isinstance(v, dict):
                    bullets_list.append(v)
                else:
                    bullets_list.append(v.to_dict())
            _dict['bullets'] = bullets_list
        if hasattr(self, 'media') and self.media is not None:
            media_list = []
            for v in self.media:
                if isinstance(v, dict):
                    media_list.append(v)
                else:
                    media_list.append(v.to_dict())
            _dict['media'] = media_list
        if hasattr(self, 'not_creatable_msg') and self.not_creatable_msg is not None:
            _dict['not_creatable_msg'] = self.not_creatable_msg
        if hasattr(self, 'not_creatable_robot_msg') and self.not_creatable_robot_msg is not None:
            _dict['not_creatable__robot_msg'] = self.not_creatable_robot_msg
        if hasattr(self, 'deprecation_warning') and self.deprecation_warning is not None:
            _dict['deprecation_warning'] = self.deprecation_warning
        if hasattr(self, 'popup_warning_message') and self.popup_warning_message is not None:
            _dict['popup_warning_message'] = self.popup_warning_message
        if hasattr(self, 'instruction') and self.instruction is not None:
            _dict['instruction'] = self.instruction
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Strings object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Strings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Strings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TemplateMetaData:
    """
    Template-related metadata.

    :param List[str] services: (optional) List of required offering or plan IDs.
    :param int default_memory: (optional) Cloud Foundry instance memory value.
    :param str start_cmd: (optional) Command used to start a service.
    :param SourceMetaData source: (optional) Location of your applications source
          files.
    :param str runtime_catalog_id: (optional) ID of the runtime.
    :param str cf_runtime_id: (optional) ID of the Cloud Foundry runtime.
    :param str template_id: (optional) ID of the boilerplate or template.
    :param str executable_file: (optional) File path to the executable file for the
          template.
    :param str buildpack: (optional) ID of the buildpack used by the template.
    :param dict environment_variables: (optional) Environment variables (key/value
          pairs) for the template.
    """

    def __init__(
        self,
        *,
        services: Optional[List[str]] = None,
        default_memory: Optional[int] = None,
        start_cmd: Optional[str] = None,
        source: Optional['SourceMetaData'] = None,
        runtime_catalog_id: Optional[str] = None,
        cf_runtime_id: Optional[str] = None,
        template_id: Optional[str] = None,
        executable_file: Optional[str] = None,
        buildpack: Optional[str] = None,
        environment_variables: Optional[dict] = None,
    ) -> None:
        """
        Initialize a TemplateMetaData object.

        :param List[str] services: (optional) List of required offering or plan
               IDs.
        :param int default_memory: (optional) Cloud Foundry instance memory value.
        :param str start_cmd: (optional) Command used to start a service.
        :param SourceMetaData source: (optional) Location of your applications
               source files.
        :param str runtime_catalog_id: (optional) ID of the runtime.
        :param str cf_runtime_id: (optional) ID of the Cloud Foundry runtime.
        :param str template_id: (optional) ID of the boilerplate or template.
        :param str executable_file: (optional) File path to the executable file for
               the template.
        :param str buildpack: (optional) ID of the buildpack used by the template.
        :param dict environment_variables: (optional) Environment variables
               (key/value pairs) for the template.
        """
        self.services = services
        self.default_memory = default_memory
        self.start_cmd = start_cmd
        self.source = source
        self.runtime_catalog_id = runtime_catalog_id
        self.cf_runtime_id = cf_runtime_id
        self.template_id = template_id
        self.executable_file = executable_file
        self.buildpack = buildpack
        self.environment_variables = environment_variables

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TemplateMetaData':
        """Initialize a TemplateMetaData object from a json dictionary."""
        args = {}
        if (services := _dict.get('services')) is not None:
            args['services'] = services
        if (default_memory := _dict.get('default_memory')) is not None:
            args['default_memory'] = default_memory
        if (start_cmd := _dict.get('start_cmd')) is not None:
            args['start_cmd'] = start_cmd
        if (source := _dict.get('source')) is not None:
            args['source'] = SourceMetaData.from_dict(source)
        if (runtime_catalog_id := _dict.get('runtime_catalog_id')) is not None:
            args['runtime_catalog_id'] = runtime_catalog_id
        if (cf_runtime_id := _dict.get('cf_runtime_id')) is not None:
            args['cf_runtime_id'] = cf_runtime_id
        if (template_id := _dict.get('template_id')) is not None:
            args['template_id'] = template_id
        if (executable_file := _dict.get('executable_file')) is not None:
            args['executable_file'] = executable_file
        if (buildpack := _dict.get('buildpack')) is not None:
            args['buildpack'] = buildpack
        if (environment_variables := _dict.get('environment_variables')) is not None:
            args['environment_variables'] = environment_variables
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TemplateMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'services') and self.services is not None:
            _dict['services'] = self.services
        if hasattr(self, 'default_memory') and self.default_memory is not None:
            _dict['default_memory'] = self.default_memory
        if hasattr(self, 'start_cmd') and self.start_cmd is not None:
            _dict['start_cmd'] = self.start_cmd
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'runtime_catalog_id') and self.runtime_catalog_id is not None:
            _dict['runtime_catalog_id'] = self.runtime_catalog_id
        if hasattr(self, 'cf_runtime_id') and self.cf_runtime_id is not None:
            _dict['cf_runtime_id'] = self.cf_runtime_id
        if hasattr(self, 'template_id') and self.template_id is not None:
            _dict['template_id'] = self.template_id
        if hasattr(self, 'executable_file') and self.executable_file is not None:
            _dict['executable_file'] = self.executable_file
        if hasattr(self, 'buildpack') and self.buildpack is not None:
            _dict['buildpack'] = self.buildpack
        if hasattr(self, 'environment_variables') and self.environment_variables is not None:
            _dict['environment_variables'] = self.environment_variables
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TemplateMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TemplateMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TemplateMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UIMediaSourceMetaData:
    """
    Location of your applications media source files.

    :param str type: (optional) Type of source, for example, git.
    :param str url: (optional) URL to source.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        url: Optional[str] = None,
    ) -> None:
        """
        Initialize a UIMediaSourceMetaData object.

        :param str type: (optional) Type of source, for example, git.
        :param str url: (optional) URL to source.
        """
        self.type = type
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UIMediaSourceMetaData':
        """Initialize a UIMediaSourceMetaData object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UIMediaSourceMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UIMediaSourceMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UIMediaSourceMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UIMediaSourceMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UIMetaData:
    """
    Information related to the UI presentation associated with a catalog entry.

    :param dict strings: (optional) Language specific translation of translation
          properties, like label and description.
    :param URLS urls: (optional) UI based URLs.
    :param str embeddable_dashboard: (optional) Describes how the embeddable
          dashboard is rendered.
    :param bool embeddable_dashboard_full_width: (optional) Describes whether the
          embeddable dashboard is rendered at the full width.
    :param List[str] navigation_order: (optional) Defines the order of information
          presented.
    :param bool not_creatable: (optional) Describes whether this entry is able to be
          created from the UI element or CLI.
    :param str primary_offering_id: (optional) ID of the primary offering for a
          group.
    :param bool accessible_during_provision: (optional) Alert to ACE to allow
          instance UI to be accessible while the provisioning state of instance is in
          progress.
    :param int side_by_side_index: (optional) Specifies a side by side ordering
          weight to the UI.
    :param datetime end_of_service_time: (optional) Date and time the service will
          no longer be available.
    :param bool hidden: (optional) Denotes visibility. Can be set on a
          service/plan/deployment only by an account with bluemix admin privileges.
    :param bool hide_lite_metering: (optional) Denotes lite metering visibility.
    :param bool no_upgrade_next_step: (optional) Denotes whether an upgrade should
          occur.
    """

    def __init__(
        self,
        *,
        strings: Optional[dict] = None,
        urls: Optional['URLS'] = None,
        embeddable_dashboard: Optional[str] = None,
        embeddable_dashboard_full_width: Optional[bool] = None,
        navigation_order: Optional[List[str]] = None,
        not_creatable: Optional[bool] = None,
        primary_offering_id: Optional[str] = None,
        accessible_during_provision: Optional[bool] = None,
        side_by_side_index: Optional[int] = None,
        end_of_service_time: Optional[datetime] = None,
        hidden: Optional[bool] = None,
        hide_lite_metering: Optional[bool] = None,
        no_upgrade_next_step: Optional[bool] = None,
    ) -> None:
        """
        Initialize a UIMetaData object.

        :param dict strings: (optional) Language specific translation of
               translation properties, like label and description.
        :param URLS urls: (optional) UI based URLs.
        :param str embeddable_dashboard: (optional) Describes how the embeddable
               dashboard is rendered.
        :param bool embeddable_dashboard_full_width: (optional) Describes whether
               the embeddable dashboard is rendered at the full width.
        :param List[str] navigation_order: (optional) Defines the order of
               information presented.
        :param bool not_creatable: (optional) Describes whether this entry is able
               to be created from the UI element or CLI.
        :param str primary_offering_id: (optional) ID of the primary offering for a
               group.
        :param bool accessible_during_provision: (optional) Alert to ACE to allow
               instance UI to be accessible while the provisioning state of instance is in
               progress.
        :param int side_by_side_index: (optional) Specifies a side by side ordering
               weight to the UI.
        :param datetime end_of_service_time: (optional) Date and time the service
               will no longer be available.
        :param bool hidden: (optional) Denotes visibility. Can be set on a
               service/plan/deployment only by an account with bluemix admin privileges.
        :param bool hide_lite_metering: (optional) Denotes lite metering
               visibility.
        :param bool no_upgrade_next_step: (optional) Denotes whether an upgrade
               should occur.
        """
        self.strings = strings
        self.urls = urls
        self.embeddable_dashboard = embeddable_dashboard
        self.embeddable_dashboard_full_width = embeddable_dashboard_full_width
        self.navigation_order = navigation_order
        self.not_creatable = not_creatable
        self.primary_offering_id = primary_offering_id
        self.accessible_during_provision = accessible_during_provision
        self.side_by_side_index = side_by_side_index
        self.end_of_service_time = end_of_service_time
        self.hidden = hidden
        self.hide_lite_metering = hide_lite_metering
        self.no_upgrade_next_step = no_upgrade_next_step

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UIMetaData':
        """Initialize a UIMetaData object from a json dictionary."""
        args = {}
        if (strings := _dict.get('strings')) is not None:
            args['strings'] = {k: Strings.from_dict(v) for k, v in strings.items()}
        if (urls := _dict.get('urls')) is not None:
            args['urls'] = URLS.from_dict(urls)
        if (embeddable_dashboard := _dict.get('embeddable_dashboard')) is not None:
            args['embeddable_dashboard'] = embeddable_dashboard
        if (embeddable_dashboard_full_width := _dict.get('embeddable_dashboard_full_width')) is not None:
            args['embeddable_dashboard_full_width'] = embeddable_dashboard_full_width
        if (navigation_order := _dict.get('navigation_order')) is not None:
            args['navigation_order'] = navigation_order
        if (not_creatable := _dict.get('not_creatable')) is not None:
            args['not_creatable'] = not_creatable
        if (primary_offering_id := _dict.get('primary_offering_id')) is not None:
            args['primary_offering_id'] = primary_offering_id
        if (accessible_during_provision := _dict.get('accessible_during_provision')) is not None:
            args['accessible_during_provision'] = accessible_during_provision
        if (side_by_side_index := _dict.get('side_by_side_index')) is not None:
            args['side_by_side_index'] = side_by_side_index
        if (end_of_service_time := _dict.get('end_of_service_time')) is not None:
            args['end_of_service_time'] = string_to_datetime(end_of_service_time)
        if (hidden := _dict.get('hidden')) is not None:
            args['hidden'] = hidden
        if (hide_lite_metering := _dict.get('hide_lite_metering')) is not None:
            args['hide_lite_metering'] = hide_lite_metering
        if (no_upgrade_next_step := _dict.get('no_upgrade_next_step')) is not None:
            args['no_upgrade_next_step'] = no_upgrade_next_step
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UIMetaData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'strings') and self.strings is not None:
            strings_map = {}
            for k, v in self.strings.items():
                if isinstance(v, dict):
                    strings_map[k] = v
                else:
                    strings_map[k] = v.to_dict()
            _dict['strings'] = strings_map
        if hasattr(self, 'urls') and self.urls is not None:
            if isinstance(self.urls, dict):
                _dict['urls'] = self.urls
            else:
                _dict['urls'] = self.urls.to_dict()
        if hasattr(self, 'embeddable_dashboard') and self.embeddable_dashboard is not None:
            _dict['embeddable_dashboard'] = self.embeddable_dashboard
        if hasattr(self, 'embeddable_dashboard_full_width') and self.embeddable_dashboard_full_width is not None:
            _dict['embeddable_dashboard_full_width'] = self.embeddable_dashboard_full_width
        if hasattr(self, 'navigation_order') and self.navigation_order is not None:
            _dict['navigation_order'] = self.navigation_order
        if hasattr(self, 'not_creatable') and self.not_creatable is not None:
            _dict['not_creatable'] = self.not_creatable
        if hasattr(self, 'primary_offering_id') and self.primary_offering_id is not None:
            _dict['primary_offering_id'] = self.primary_offering_id
        if hasattr(self, 'accessible_during_provision') and self.accessible_during_provision is not None:
            _dict['accessible_during_provision'] = self.accessible_during_provision
        if hasattr(self, 'side_by_side_index') and self.side_by_side_index is not None:
            _dict['side_by_side_index'] = self.side_by_side_index
        if hasattr(self, 'end_of_service_time') and self.end_of_service_time is not None:
            _dict['end_of_service_time'] = datetime_to_string(self.end_of_service_time)
        if hasattr(self, 'hidden') and self.hidden is not None:
            _dict['hidden'] = self.hidden
        if hasattr(self, 'hide_lite_metering') and self.hide_lite_metering is not None:
            _dict['hide_lite_metering'] = self.hide_lite_metering
        if hasattr(self, 'no_upgrade_next_step') and self.no_upgrade_next_step is not None:
            _dict['no_upgrade_next_step'] = self.no_upgrade_next_step
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UIMetaData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UIMetaData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UIMetaData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UIMetaMedia:
    """
    Media-related metadata.

    :param str caption: (optional) Caption for an image.
    :param str thumbnail_url: (optional) URL for thumbnail image.
    :param str type: (optional) Type of media.
    :param str url: (optional) URL for media.
    :param List[UIMediaSourceMetaData] source: (optional) UI media source data for
          for UI media data.
    """

    def __init__(
        self,
        *,
        caption: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        type: Optional[str] = None,
        url: Optional[str] = None,
        source: Optional[List['UIMediaSourceMetaData']] = None,
    ) -> None:
        """
        Initialize a UIMetaMedia object.

        :param str caption: (optional) Caption for an image.
        :param str thumbnail_url: (optional) URL for thumbnail image.
        :param str type: (optional) Type of media.
        :param str url: (optional) URL for media.
        :param List[UIMediaSourceMetaData] source: (optional) UI media source data
               for for UI media data.
        """
        self.caption = caption
        self.thumbnail_url = thumbnail_url
        self.type = type
        self.url = url
        self.source = source

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UIMetaMedia':
        """Initialize a UIMetaMedia object from a json dictionary."""
        args = {}
        if (caption := _dict.get('caption')) is not None:
            args['caption'] = caption
        if (thumbnail_url := _dict.get('thumbnail_url')) is not None:
            args['thumbnail_url'] = thumbnail_url
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (url := _dict.get('URL')) is not None:
            args['url'] = url
        if (source := _dict.get('source')) is not None:
            args['source'] = [UIMediaSourceMetaData.from_dict(v) for v in source]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UIMetaMedia object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'caption') and self.caption is not None:
            _dict['caption'] = self.caption
        if hasattr(self, 'thumbnail_url') and self.thumbnail_url is not None:
            _dict['thumbnail_url'] = self.thumbnail_url
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'url') and self.url is not None:
            _dict['URL'] = self.url
        if hasattr(self, 'source') and self.source is not None:
            source_list = []
            for v in self.source:
                if isinstance(v, dict):
                    source_list.append(v)
                else:
                    source_list.append(v.to_dict())
            _dict['source'] = source_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UIMetaMedia object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UIMetaMedia') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UIMetaMedia') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class URLS:
    """
    UI based URLs.

    :param str doc_url: (optional) URL for documentation.
    :param str instructions_url: (optional) URL for usage instructions.
    :param str api_url: (optional) API URL.
    :param str create_url: (optional) URL Creation UI / API.
    :param str sdk_download_url: (optional) URL to downlaod an SDK.
    :param str terms_url: (optional) URL to the terms of use for your service.
    :param str custom_create_page_url: (optional) URL to the custom create page for
          your service.
    :param str catalog_details_url: (optional) URL to the catalog details page for
          your service.
    :param str deprecation_doc_url: (optional) URL for deprecation documentation.
    :param str dashboard_url: (optional) URL for dashboard.
    :param str registration_url: (optional) URL for registration.
    :param str apidocsurl: (optional) URL for API documentation.
    """

    def __init__(
        self,
        *,
        doc_url: Optional[str] = None,
        instructions_url: Optional[str] = None,
        api_url: Optional[str] = None,
        create_url: Optional[str] = None,
        sdk_download_url: Optional[str] = None,
        terms_url: Optional[str] = None,
        custom_create_page_url: Optional[str] = None,
        catalog_details_url: Optional[str] = None,
        deprecation_doc_url: Optional[str] = None,
        dashboard_url: Optional[str] = None,
        registration_url: Optional[str] = None,
        apidocsurl: Optional[str] = None,
    ) -> None:
        """
        Initialize a URLS object.

        :param str doc_url: (optional) URL for documentation.
        :param str instructions_url: (optional) URL for usage instructions.
        :param str api_url: (optional) API URL.
        :param str create_url: (optional) URL Creation UI / API.
        :param str sdk_download_url: (optional) URL to downlaod an SDK.
        :param str terms_url: (optional) URL to the terms of use for your service.
        :param str custom_create_page_url: (optional) URL to the custom create page
               for your service.
        :param str catalog_details_url: (optional) URL to the catalog details page
               for your service.
        :param str deprecation_doc_url: (optional) URL for deprecation
               documentation.
        :param str dashboard_url: (optional) URL for dashboard.
        :param str registration_url: (optional) URL for registration.
        :param str apidocsurl: (optional) URL for API documentation.
        """
        self.doc_url = doc_url
        self.instructions_url = instructions_url
        self.api_url = api_url
        self.create_url = create_url
        self.sdk_download_url = sdk_download_url
        self.terms_url = terms_url
        self.custom_create_page_url = custom_create_page_url
        self.catalog_details_url = catalog_details_url
        self.deprecation_doc_url = deprecation_doc_url
        self.dashboard_url = dashboard_url
        self.registration_url = registration_url
        self.apidocsurl = apidocsurl

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'URLS':
        """Initialize a URLS object from a json dictionary."""
        args = {}
        if (doc_url := _dict.get('doc_url')) is not None:
            args['doc_url'] = doc_url
        if (instructions_url := _dict.get('instructions_url')) is not None:
            args['instructions_url'] = instructions_url
        if (api_url := _dict.get('api_url')) is not None:
            args['api_url'] = api_url
        if (create_url := _dict.get('create_url')) is not None:
            args['create_url'] = create_url
        if (sdk_download_url := _dict.get('sdk_download_url')) is not None:
            args['sdk_download_url'] = sdk_download_url
        if (terms_url := _dict.get('terms_url')) is not None:
            args['terms_url'] = terms_url
        if (custom_create_page_url := _dict.get('custom_create_page_url')) is not None:
            args['custom_create_page_url'] = custom_create_page_url
        if (catalog_details_url := _dict.get('catalog_details_url')) is not None:
            args['catalog_details_url'] = catalog_details_url
        if (deprecation_doc_url := _dict.get('deprecation_doc_url')) is not None:
            args['deprecation_doc_url'] = deprecation_doc_url
        if (dashboard_url := _dict.get('dashboard_url')) is not None:
            args['dashboard_url'] = dashboard_url
        if (registration_url := _dict.get('registration_url')) is not None:
            args['registration_url'] = registration_url
        if (apidocsurl := _dict.get('apidocsurl')) is not None:
            args['apidocsurl'] = apidocsurl
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a URLS object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'doc_url') and self.doc_url is not None:
            _dict['doc_url'] = self.doc_url
        if hasattr(self, 'instructions_url') and self.instructions_url is not None:
            _dict['instructions_url'] = self.instructions_url
        if hasattr(self, 'api_url') and self.api_url is not None:
            _dict['api_url'] = self.api_url
        if hasattr(self, 'create_url') and self.create_url is not None:
            _dict['create_url'] = self.create_url
        if hasattr(self, 'sdk_download_url') and self.sdk_download_url is not None:
            _dict['sdk_download_url'] = self.sdk_download_url
        if hasattr(self, 'terms_url') and self.terms_url is not None:
            _dict['terms_url'] = self.terms_url
        if hasattr(self, 'custom_create_page_url') and self.custom_create_page_url is not None:
            _dict['custom_create_page_url'] = self.custom_create_page_url
        if hasattr(self, 'catalog_details_url') and self.catalog_details_url is not None:
            _dict['catalog_details_url'] = self.catalog_details_url
        if hasattr(self, 'deprecation_doc_url') and self.deprecation_doc_url is not None:
            _dict['deprecation_doc_url'] = self.deprecation_doc_url
        if hasattr(self, 'dashboard_url') and self.dashboard_url is not None:
            _dict['dashboard_url'] = self.dashboard_url
        if hasattr(self, 'registration_url') and self.registration_url is not None:
            _dict['registration_url'] = self.registration_url
        if hasattr(self, 'apidocsurl') and self.apidocsurl is not None:
            _dict['apidocsurl'] = self.apidocsurl
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this URLS object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'URLS') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'URLS') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Visibility:
    """
    Information related to the visibility of a catalog entry.

    :param str restrictions: (optional) This controls the overall visibility. It is
          an enum of *public*, *nonibm_only*, *ibm_only*, and *private*. public means it
          is visible to all. nonibm_only means it is visible to all except IBM unless
          their account is explicitly included, ibm_only means it is visible to all IBM
          unless their account is explicitly excluded. private means it is visible only to
          the included accounts.
    :param str owner: (optional) IAM Scope-related information associated with a
          catalog entry.
    :param bool extendable: (optional) Allows the visibility to be extendable.
    :param VisibilityDetail include: (optional) Visibility details related to a
          catalog entry.
    :param VisibilityDetail exclude: (optional) Visibility details related to a
          catalog entry.
    :param bool approved: (optional) Determines whether the owning account has full
          control over the visibility of the entry such as adding non-IBM accounts to the
          whitelist and making entries `private`, `nonibm_only`, `ibm_only` or `public`.
    """

    def __init__(
        self,
        *,
        restrictions: Optional[str] = None,
        owner: Optional[str] = None,
        extendable: Optional[bool] = None,
        include: Optional['VisibilityDetail'] = None,
        exclude: Optional['VisibilityDetail'] = None,
        approved: Optional[bool] = None,
    ) -> None:
        """
        Initialize a Visibility object.

        :param str restrictions: (optional) This controls the overall visibility.
               It is an enum of *public*, *nonibm_only*, *ibm_only*, and *private*. public
               means it is visible to all. nonibm_only means it is visible to all except
               IBM unless their account is explicitly included, ibm_only means it is
               visible to all IBM unless their account is explicitly excluded. private
               means it is visible only to the included accounts.
        :param bool extendable: (optional) Allows the visibility to be extendable.
        :param VisibilityDetail include: (optional) Visibility details related to a
               catalog entry.
        :param VisibilityDetail exclude: (optional) Visibility details related to a
               catalog entry.
        """
        self.restrictions = restrictions
        self.owner = owner
        self.extendable = extendable
        self.include = include
        self.exclude = exclude
        self.approved = approved

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Visibility':
        """Initialize a Visibility object from a json dictionary."""
        args = {}
        if (restrictions := _dict.get('restrictions')) is not None:
            args['restrictions'] = restrictions
        if (owner := _dict.get('owner')) is not None:
            args['owner'] = owner
        if (extendable := _dict.get('extendable')) is not None:
            args['extendable'] = extendable
        if (include := _dict.get('include')) is not None:
            args['include'] = VisibilityDetail.from_dict(include)
        if (exclude := _dict.get('exclude')) is not None:
            args['exclude'] = VisibilityDetail.from_dict(exclude)
        if (approved := _dict.get('approved')) is not None:
            args['approved'] = approved
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Visibility object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'restrictions') and self.restrictions is not None:
            _dict['restrictions'] = self.restrictions
        if hasattr(self, 'owner') and getattr(self, 'owner') is not None:
            _dict['owner'] = getattr(self, 'owner')
        if hasattr(self, 'extendable') and self.extendable is not None:
            _dict['extendable'] = self.extendable
        if hasattr(self, 'include') and self.include is not None:
            if isinstance(self.include, dict):
                _dict['include'] = self.include
            else:
                _dict['include'] = self.include.to_dict()
        if hasattr(self, 'exclude') and self.exclude is not None:
            if isinstance(self.exclude, dict):
                _dict['exclude'] = self.exclude
            else:
                _dict['exclude'] = self.exclude.to_dict()
        if hasattr(self, 'approved') and getattr(self, 'approved') is not None:
            _dict['approved'] = getattr(self, 'approved')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Visibility object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Visibility') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Visibility') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VisibilityDetail:
    """
    Visibility details related to a catalog entry.

    :param VisibilityDetailAccounts accounts: Information related to the accounts
          for which a catalog entry is visible.
    """

    def __init__(
        self,
        accounts: 'VisibilityDetailAccounts',
    ) -> None:
        """
        Initialize a VisibilityDetail object.

        :param VisibilityDetailAccounts accounts: Information related to the
               accounts for which a catalog entry is visible.
        """
        self.accounts = accounts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VisibilityDetail':
        """Initialize a VisibilityDetail object from a json dictionary."""
        args = {}
        if (accounts := _dict.get('accounts')) is not None:
            args['accounts'] = VisibilityDetailAccounts.from_dict(accounts)
        else:
            raise ValueError('Required property \'accounts\' not present in VisibilityDetail JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VisibilityDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'accounts') and self.accounts is not None:
            if isinstance(self.accounts, dict):
                _dict['accounts'] = self.accounts
            else:
                _dict['accounts'] = self.accounts.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VisibilityDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VisibilityDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VisibilityDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VisibilityDetailAccounts:
    """
    Information related to the accounts for which a catalog entry is visible.

    :param str accountid: (optional) (_accountid_) is the GUID of the account and
          the value is the scope of who set it. For setting visibility use "" as the
          value. It is replaced with the owner scope when saved.
    """

    def __init__(
        self,
        *,
        accountid: Optional[str] = None,
    ) -> None:
        """
        Initialize a VisibilityDetailAccounts object.

        :param str accountid: (optional) (_accountid_) is the GUID of the account
               and the value is the scope of who set it. For setting visibility use "" as
               the value. It is replaced with the owner scope when saved.
        """
        self.accountid = accountid

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VisibilityDetailAccounts':
        """Initialize a VisibilityDetailAccounts object from a json dictionary."""
        args = {}
        if (accountid := _dict.get('_accountid_')) is not None:
            args['accountid'] = accountid
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VisibilityDetailAccounts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'accountid') and self.accountid is not None:
            _dict['_accountid_'] = self.accountid
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VisibilityDetailAccounts object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VisibilityDetailAccounts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VisibilityDetailAccounts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
