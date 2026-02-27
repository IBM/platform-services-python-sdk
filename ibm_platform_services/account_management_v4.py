# coding: utf-8

# (C) Copyright IBM Corp. 2026.
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

# IBM OpenAPI SDK Code Generator Version: 3.111.0-1bfb72c2-20260206-185521

"""
The Account Management API allows for the management of Account

API Version: 4.0.0
"""

from typing import Dict
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class AccountManagementV4(BaseService):
    """The account_management V4 service."""

    DEFAULT_SERVICE_URL = 'https://accounts.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'account_management'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'AccountManagementV4':
        """
        Return a new client for the account_management service using the specified
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
        Construct a new client for the account_management service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # default
    #########################

    def get_account(
        self,
        account_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Account by Account ID.

        Returns the details of an account.

        :param str account_id: The unique identifier of the account you want to
               retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountResponse` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V4',
            operation_id='get_account',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v4/accounts/{account_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AccountResponseTraits:
    """
    AccountResponseTraits.

    :param bool eu_supported:
    :param bool poc:
    :param bool hippa:
    """

    def __init__(
        self,
        eu_supported: bool,
        poc: bool,
        hippa: bool,
    ) -> None:
        """
        Initialize a AccountResponseTraits object.

        :param bool eu_supported:
        :param bool poc:
        :param bool hippa:
        """
        self.eu_supported = eu_supported
        self.poc = poc
        self.hippa = hippa

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountResponseTraits':
        """Initialize a AccountResponseTraits object from a json dictionary."""
        args = {}
        if (eu_supported := _dict.get('eu_supported')) is not None:
            args['eu_supported'] = eu_supported
        else:
            raise ValueError('Required property \'eu_supported\' not present in AccountResponseTraits JSON')
        if (poc := _dict.get('poc')) is not None:
            args['poc'] = poc
        else:
            raise ValueError('Required property \'poc\' not present in AccountResponseTraits JSON')
        if (hippa := _dict.get('hippa')) is not None:
            args['hippa'] = hippa
        else:
            raise ValueError('Required property \'hippa\' not present in AccountResponseTraits JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountResponseTraits object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'eu_supported') and self.eu_supported is not None:
            _dict['eu_supported'] = self.eu_supported
        if hasattr(self, 'poc') and self.poc is not None:
            _dict['poc'] = self.poc
        if hasattr(self, 'hippa') and self.hippa is not None:
            _dict['hippa'] = self.hippa
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountResponseTraits object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountResponseTraits') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountResponseTraits') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AccountResponse:
    """
    AccountResponse.

    :param str name:
    :param str id:
    :param str owner:
    :param str owner_userid:
    :param str owner_iamid:
    :param str type:
    :param str status:
    :param str linked_softlayer_account:
    :param bool team_directory_enabled:
    :param AccountResponseTraits traits:
    """

    def __init__(
        self,
        name: str,
        id: str,
        owner: str,
        owner_userid: str,
        owner_iamid: str,
        type: str,
        status: str,
        linked_softlayer_account: str,
        team_directory_enabled: bool,
        traits: 'AccountResponseTraits',
    ) -> None:
        """
        Initialize a AccountResponse object.

        :param str name:
        :param str id:
        :param str owner:
        :param str owner_userid:
        :param str owner_iamid:
        :param str type:
        :param str status:
        :param str linked_softlayer_account:
        :param bool team_directory_enabled:
        :param AccountResponseTraits traits:
        """
        self.name = name
        self.id = id
        self.owner = owner
        self.owner_userid = owner_userid
        self.owner_iamid = owner_iamid
        self.type = type
        self.status = status
        self.linked_softlayer_account = linked_softlayer_account
        self.team_directory_enabled = team_directory_enabled
        self.traits = traits

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountResponse':
        """Initialize a AccountResponse object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in AccountResponse JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in AccountResponse JSON')
        if (owner := _dict.get('owner')) is not None:
            args['owner'] = owner
        else:
            raise ValueError('Required property \'owner\' not present in AccountResponse JSON')
        if (owner_userid := _dict.get('owner_userid')) is not None:
            args['owner_userid'] = owner_userid
        else:
            raise ValueError('Required property \'owner_userid\' not present in AccountResponse JSON')
        if (owner_iamid := _dict.get('owner_iamid')) is not None:
            args['owner_iamid'] = owner_iamid
        else:
            raise ValueError('Required property \'owner_iamid\' not present in AccountResponse JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in AccountResponse JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in AccountResponse JSON')
        if (linked_softlayer_account := _dict.get('linked_softlayer_account')) is not None:
            args['linked_softlayer_account'] = linked_softlayer_account
        else:
            raise ValueError('Required property \'linked_softlayer_account\' not present in AccountResponse JSON')
        if (team_directory_enabled := _dict.get('team_directory_enabled')) is not None:
            args['team_directory_enabled'] = team_directory_enabled
        else:
            raise ValueError('Required property \'team_directory_enabled\' not present in AccountResponse JSON')
        if (traits := _dict.get('traits')) is not None:
            args['traits'] = AccountResponseTraits.from_dict(traits)
        else:
            raise ValueError('Required property \'traits\' not present in AccountResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'owner') and self.owner is not None:
            _dict['owner'] = self.owner
        if hasattr(self, 'owner_userid') and self.owner_userid is not None:
            _dict['owner_userid'] = self.owner_userid
        if hasattr(self, 'owner_iamid') and self.owner_iamid is not None:
            _dict['owner_iamid'] = self.owner_iamid
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'linked_softlayer_account') and self.linked_softlayer_account is not None:
            _dict['linked_softlayer_account'] = self.linked_softlayer_account
        if hasattr(self, 'team_directory_enabled') and self.team_directory_enabled is not None:
            _dict['team_directory_enabled'] = self.team_directory_enabled
        if hasattr(self, 'traits') and self.traits is not None:
            if isinstance(self.traits, dict):
                _dict['traits'] = self.traits
            else:
                _dict['traits'] = self.traits.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
