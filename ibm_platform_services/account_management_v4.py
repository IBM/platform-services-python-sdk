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

# IBM OpenAPI SDK Code Generator Version: 3.70.0-7df966bf-20230419-195904

"""
Manage the lifecycle of your users using Account Management APIs.

API Version: 1.0
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse, get_query_param
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

class AccountManagementV4(BaseService):
    """The Account Management V4 service."""

    DEFAULT_SERVICE_URL = 'https://accounts.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'account_management'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'AccountManagementV4':
        """
        Return a new client for the account management service using the specified
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
        Construct a new client for the Account Management service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Accounts
    #########################
    def get_account_info(
        self,
        account_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get account info.

        Retrieve an account info by the account id in your account. You can use the
        IAM service token or an account user token for authorization. To use this method, the
        requesting user or service ID must have at least the viewer, editor, or
        administrator role on the Account management service.

        :param str account_id: The account ID of the specified account.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `accountInfo` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V4',
            operation_id='get_account_info',
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