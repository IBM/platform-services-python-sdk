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

# IBM OpenAPI SDK Code Generator Version: 3.33.0-caf29bd0-20210603-225214

"""
Search for resources with the global and shared resource properties repository integrated
in the IBM Cloud platform. The search repository stores and searches cloud resources
attributes, which categorize or classify resources. A resource is a physical or logical
component that can be created or reserved for an application or service instance and is
owned by resource providers, such as Cloud Foundry, IBM Kubernetes Service, or resource
controller in IBM Cloud. Resources are uniquely identified by a Cloud Resource Name (CRN)
or by an IMS ID. The properties of a resource include tags and system properties. Both
properties are defined in an IBM Cloud billing account, and span across many regions.
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class GlobalSearchV2(BaseService):
    """The global_search V2 service."""

    DEFAULT_SERVICE_URL = 'https://api.global-search-tagging.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'global_search'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'GlobalSearchV2':
        """
        Return a new client for the global_search service using the specified
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
        Construct a new client for the global_search service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Search
    #########################

    def search(
        self,
        *,
        query: str = None,
        fields: List[str] = None,
        search_cursor: str = None,
        transaction_id: str = None,
        account_id: str = None,
        limit: int = None,
        timeout: int = None,
        sort: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Find instances of resources (v3).

        Find Cloud Foundry resources, IAM-enabled resources, or  storage and network
        resources running on classic infrastructure in a  specific account ID. You can
        apply query strings if necessary.
        To filter results, you can insert a string using the Lucene syntax and the  query
        string is parsed into a series of terms and operators. A term can be  a single
        word or a phrase, in which case the search is performed for all  the words, in the
        same order. To filter for a specific value regardless of  the property that
        contains it, type the search term without specifying a  field. Only resources that
        belong to the account ID and that are accessible  by the client are returned.
        You must use `/v3/resources/search` when you need to fetch more than `10000`
        resource items. The `/v2/resources/search` prohibits paginating through such  a
        big number. On the first call, the operation returns a live cursor on the  data
        that you must use on all the subsequent calls to get the next batch of  results
        until you get the empty result set. By default, the fields returned  for every
        resource are "crn", "name", "family", "type", and "account_id". You  can specify
        the subset of the fields you want in your request.

        :param str query: (optional) The Lucene-formatted query string. Default to
               '*' if not set.
        :param List[str] fields: (optional) The list of the fields returned by the
               search. Defaults to all. `crn` is always returned.
        :param str search_cursor: (optional) An opaque search cursor that is
               returned on each operation call and that must be set on next call.
        :param str transaction_id: (optional) An aplhanumeric string that can be
               used to trace a request across services. If not specified it will be
               automatically generated with the prefix "gst-".
        :param str account_id: (optional) The account ID to filter resources.
        :param int limit: (optional) The maximum number of hits to return. Defaults
               to 10.
        :param int timeout: (optional) A search timeout, bounding the search
               request to be executed within the specified time value and bail with the
               hits accumulated up to that point when expired. Defaults to the system
               defined timeout.
        :param List[str] sort: (optional) Comma separated properties names used for
               sorting.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ScanResult` object
        """

        headers = {'transaction-id': transaction_id}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='search'
        )
        headers.update(sdk_headers)

        params = {'account_id': account_id, 'limit': limit, 'timeout': timeout, 'sort': convert_list(sort)}

        data = {'query': query, 'fields': fields, 'search_cursor': search_cursor}
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v3/resources/search'
        request = self.prepare_request(method='POST', url=url, headers=headers, params=params, data=data)

        response = self.send(request)
        return response

    #########################
    # Resource Types
    #########################

    def get_supported_types(self, **kwargs) -> DetailedResponse:
        """
        DEPRECATED. Get all GhoST indices.

        Retrieves a list of all GhoST indices.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SupportedTypesList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_supported_types'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/v2/resources/supported_types'
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class ResultItem:
    """
    A resource returned in a search result.

    :attr str crn: (optional) Resource identifier in CRN format.
    """

    # The set of defined properties for the class
    _properties = frozenset(['crn'])

    def __init__(self, *, crn: str = None, **kwargs) -> None:
        """
        Initialize a ResultItem object.

        :param str crn: (optional) Resource identifier in CRN format.
        :param **kwargs: (optional) Any additional properties.
        """
        self.crn = crn
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResultItem':
        """Initialize a ResultItem object from a json dictionary."""
        args = {}
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        args.update({k: v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        for _key in [k for k in vars(self).keys() if k not in ResultItem._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ScanResult:
    """
    The search scan response.

    :attr str search_cursor: The search cursor to use on all calls after the first
          one.
    :attr int limit: (optional) Value of the limit parameter specified by the user.
    :attr List[ResultItem] items: The array of results. Each item represents a
          resource. An empty array signals the end of the result set, there are no more
          hits to fetch.
    """

    def __init__(self, search_cursor: str, items: List['ResultItem'], *, limit: int = None) -> None:
        """
        Initialize a ScanResult object.

        :param str search_cursor: The search cursor to use on all calls after the
               first one.
        :param List[ResultItem] items: The array of results. Each item represents a
               resource. An empty array signals the end of the result set, there are no
               more hits to fetch.
        :param int limit: (optional) Value of the limit parameter specified by the
               user.
        """
        self.search_cursor = search_cursor
        self.limit = limit
        self.items = items

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScanResult':
        """Initialize a ScanResult object from a json dictionary."""
        args = {}
        if 'search_cursor' in _dict:
            args['search_cursor'] = _dict.get('search_cursor')
        else:
            raise ValueError('Required property \'search_cursor\' not present in ScanResult JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'items' in _dict:
            args['items'] = [ResultItem.from_dict(x) for x in _dict.get('items')]
        else:
            raise ValueError('Required property \'items\' not present in ScanResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScanResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'search_cursor') and self.search_cursor is not None:
            _dict['search_cursor'] = self.search_cursor
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'items') and self.items is not None:
            _dict['items'] = [x.to_dict() for x in self.items]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ScanResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScanResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScanResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SupportedTypesList:
    """
    A list of all GhoST indices.

    :attr List[str] supported_types: (optional) A list of all GhoST indices.
    """

    def __init__(self, *, supported_types: List[str] = None) -> None:
        """
        Initialize a SupportedTypesList object.

        :param List[str] supported_types: (optional) A list of all GhoST indices.
        """
        self.supported_types = supported_types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SupportedTypesList':
        """Initialize a SupportedTypesList object from a json dictionary."""
        args = {}
        if 'supported_types' in _dict:
            args['supported_types'] = _dict.get('supported_types')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SupportedTypesList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'supported_types') and self.supported_types is not None:
            _dict['supported_types'] = self.supported_types
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SupportedTypesList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SupportedTypesList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SupportedTypesList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
