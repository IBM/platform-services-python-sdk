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

# IBM OpenAPI SDK Code Generator Version: 3.36.0-6f5b0381-20210716-180747
 
"""
Usage reports for IBM Cloud accounts
"""

from datetime import datetime
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class UsageReportsV4(BaseService):
    """The Usage Reports V4 service."""

    DEFAULT_SERVICE_URL = 'https://billing.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'usage_reports'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'UsageReportsV4':
        """
        Return a new client for the Usage Reports service using the specified
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
        Construct a new client for the Usage Reports service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Account operations
    #########################


    def get_account_summary(self,
        account_id: str,
        billingmonth: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get account summary.

        Returns the summary for the account for a given month. Account billing managers
        are authorized to access this report.

        :param str account_id: Account ID for which the usage report is requested.
        :param str billingmonth: The billing month for which the usage report is
               requested.  Format is yyyy-mm.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountSummary` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if billingmonth is None:
            raise ValueError('billingmonth must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_account_summary')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'billingmonth']
        path_param_values = self.encode_path_vars(account_id, billingmonth)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v4/accounts/{account_id}/summary/{billingmonth}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_account_usage(self,
        account_id: str,
        billingmonth: str,
        *,
        names: bool = None,
        accept_language: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get account usage.

        Usage for all the resources and plans in an account for a given month. Account
        billing managers are authorized to access this report.

        :param str account_id: Account ID for which the usage report is requested.
        :param str billingmonth: The billing month for which the usage report is
               requested.  Format is yyyy-mm.
        :param bool names: (optional) Include the name of every resource, plan,
               resource instance, organization, and resource group.
        :param str accept_language: (optional) Prioritize the names returned in the
               order of the specified languages. Language will default to English.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountUsage` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if billingmonth is None:
            raise ValueError('billingmonth must be provided')
        headers = {
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_account_usage')
        headers.update(sdk_headers)

        params = {
            '_names': names
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'billingmonth']
        path_param_values = self.encode_path_vars(account_id, billingmonth)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v4/accounts/{account_id}/usage/{billingmonth}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Resource operations
    #########################


    def get_resource_group_usage(self,
        account_id: str,
        resource_group_id: str,
        billingmonth: str,
        *,
        names: bool = None,
        accept_language: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get resource group usage.

        Usage for all the resources and plans in a resource group in a given month.
        Account billing managers or resource group billing managers are authorized to
        access this report.

        :param str account_id: Account ID for which the usage report is requested.
        :param str resource_group_id: Resource group for which the usage report is
               requested.
        :param str billingmonth: The billing month for which the usage report is
               requested.  Format is yyyy-mm.
        :param bool names: (optional) Include the name of every resource, plan,
               resource instance, organization, and resource group.
        :param str accept_language: (optional) Prioritize the names returned in the
               order of the specified languages. Language will default to English.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceGroupUsage` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if resource_group_id is None:
            raise ValueError('resource_group_id must be provided')
        if billingmonth is None:
            raise ValueError('billingmonth must be provided')
        headers = {
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_resource_group_usage')
        headers.update(sdk_headers)

        params = {
            '_names': names
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'resource_group_id', 'billingmonth']
        path_param_values = self.encode_path_vars(account_id, resource_group_id, billingmonth)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v4/accounts/{account_id}/resource_groups/{resource_group_id}/usage/{billingmonth}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_resource_usage_account(self,
        account_id: str,
        billingmonth: str,
        *,
        names: bool = None,
        accept_language: str = None,
        limit: int = None,
        start: str = None,
        resource_group_id: str = None,
        organization_id: str = None,
        resource_instance_id: str = None,
        resource_id: str = None,
        plan_id: str = None,
        region: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get resource instance usage in an account.

        Query for resource instance usage in an account. Filter the results with query
        parameters. Account billing administrator is authorized to access this report.

        :param str account_id: Account ID for which the usage report is requested.
        :param str billingmonth: The billing month for which the usage report is
               requested.  Format is yyyy-mm.
        :param bool names: (optional) Include the name of every resource, plan,
               resource instance, organization, and resource group.
        :param str accept_language: (optional) Prioritize the names returned in the
               order of the specified languages. Language will default to English.
        :param int limit: (optional) Number of usage records returned. The default
               value is 10. Maximum value is 20.
        :param str start: (optional) The offset from which the records must be
               fetched. Offset information is included in the response.
        :param str resource_group_id: (optional) Filter by resource group.
        :param str organization_id: (optional) Filter by organization_id.
        :param str resource_instance_id: (optional) Filter by resource instance_id.
        :param str resource_id: (optional) Filter by resource_id.
        :param str plan_id: (optional) Filter by plan_id.
        :param str region: (optional) Region in which the resource instance is
               provisioned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InstancesUsage` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if billingmonth is None:
            raise ValueError('billingmonth must be provided')
        headers = {
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_resource_usage_account')
        headers.update(sdk_headers)

        params = {
            '_names': names,
            '_limit': limit,
            '_start': start,
            'resource_group_id': resource_group_id,
            'organization_id': organization_id,
            'resource_instance_id': resource_instance_id,
            'resource_id': resource_id,
            'plan_id': plan_id,
            'region': region
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'billingmonth']
        path_param_values = self.encode_path_vars(account_id, billingmonth)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v4/accounts/{account_id}/resource_instances/usage/{billingmonth}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_resource_usage_resource_group(self,
        account_id: str,
        resource_group_id: str,
        billingmonth: str,
        *,
        names: bool = None,
        accept_language: str = None,
        limit: int = None,
        start: str = None,
        resource_instance_id: str = None,
        resource_id: str = None,
        plan_id: str = None,
        region: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get resource instance usage in a resource group.

        Query for resource instance usage in a resource group. Filter the results with
        query parameters. Account billing administrator and resource group billing
        administrators are authorized to access this report.

        :param str account_id: Account ID for which the usage report is requested.
        :param str resource_group_id: Resource group for which the usage report is
               requested.
        :param str billingmonth: The billing month for which the usage report is
               requested.  Format is yyyy-mm.
        :param bool names: (optional) Include the name of every resource, plan,
               resource instance, organization, and resource group.
        :param str accept_language: (optional) Prioritize the names returned in the
               order of the specified languages. Language will default to English.
        :param int limit: (optional) Number of usage records returned. The default
               value is 10. Maximum value is 20.
        :param str start: (optional) The offset from which the records must be
               fetched. Offset information is included in the response.
        :param str resource_instance_id: (optional) Filter by resource instance id.
        :param str resource_id: (optional) Filter by resource_id.
        :param str plan_id: (optional) Filter by plan_id.
        :param str region: (optional) Region in which the resource instance is
               provisioned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InstancesUsage` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if resource_group_id is None:
            raise ValueError('resource_group_id must be provided')
        if billingmonth is None:
            raise ValueError('billingmonth must be provided')
        headers = {
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_resource_usage_resource_group')
        headers.update(sdk_headers)

        params = {
            '_names': names,
            '_limit': limit,
            '_start': start,
            'resource_instance_id': resource_instance_id,
            'resource_id': resource_id,
            'plan_id': plan_id,
            'region': region
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'resource_group_id', 'billingmonth']
        path_param_values = self.encode_path_vars(account_id, resource_group_id, billingmonth)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v4/accounts/{account_id}/resource_groups/{resource_group_id}/resource_instances/usage/{billingmonth}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_resource_usage_org(self,
        account_id: str,
        organization_id: str,
        billingmonth: str,
        *,
        names: bool = None,
        accept_language: str = None,
        limit: int = None,
        start: str = None,
        resource_instance_id: str = None,
        resource_id: str = None,
        plan_id: str = None,
        region: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get resource instance usage in an organization.

        Query for resource instance usage in an organization. Filter the results with
        query parameters. Account billing administrator and organization billing
        administrators are authorized to access this report.

        :param str account_id: Account ID for which the usage report is requested.
        :param str organization_id: ID of the organization.
        :param str billingmonth: The billing month for which the usage report is
               requested.  Format is yyyy-mm.
        :param bool names: (optional) Include the name of every resource, plan,
               resource instance, organization, and resource group.
        :param str accept_language: (optional) Prioritize the names returned in the
               order of the specified languages. Language will default to English.
        :param int limit: (optional) Number of usage records returned. The default
               value is 10. Maximum value is 20.
        :param str start: (optional) The offset from which the records must be
               fetched. Offset information is included in the response.
        :param str resource_instance_id: (optional) Filter by resource instance id.
        :param str resource_id: (optional) Filter by resource_id.
        :param str plan_id: (optional) Filter by plan_id.
        :param str region: (optional) Region in which the resource instance is
               provisioned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InstancesUsage` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if organization_id is None:
            raise ValueError('organization_id must be provided')
        if billingmonth is None:
            raise ValueError('billingmonth must be provided')
        headers = {
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_resource_usage_org')
        headers.update(sdk_headers)

        params = {
            '_names': names,
            '_limit': limit,
            '_start': start,
            'resource_instance_id': resource_instance_id,
            'resource_id': resource_id,
            'plan_id': plan_id,
            'region': region
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'organization_id', 'billingmonth']
        path_param_values = self.encode_path_vars(account_id, organization_id, billingmonth)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v4/accounts/{account_id}/organizations/{organization_id}/resource_instances/usage/{billingmonth}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Organization operations
    #########################


    def get_org_usage(self,
        account_id: str,
        organization_id: str,
        billingmonth: str,
        *,
        names: bool = None,
        accept_language: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get organization usage.

        Usage for all the resources and plans in an organization in a given month. Account
        billing managers or organization billing managers are authorized to access this
        report.

        :param str account_id: Account ID for which the usage report is requested.
        :param str organization_id: ID of the organization.
        :param str billingmonth: The billing month for which the usage report is
               requested.  Format is yyyy-mm.
        :param bool names: (optional) Include the name of every resource, plan,
               resource instance, organization, and resource group.
        :param str accept_language: (optional) Prioritize the names returned in the
               order of the specified languages. Language will default to English.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OrgUsage` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if organization_id is None:
            raise ValueError('organization_id must be provided')
        if billingmonth is None:
            raise ValueError('billingmonth must be provided')
        headers = {
            'Accept-Language': accept_language
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_org_usage')
        headers.update(sdk_headers)

        params = {
            '_names': names
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'organization_id', 'billingmonth']
        path_param_values = self.encode_path_vars(account_id, organization_id, billingmonth)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v4/accounts/{account_id}/organizations/{organization_id}/usage/{billingmonth}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AccountSummary():
    """
    A summary of charges and credits for an account.

    :attr str account_id: The ID of the account.
    :attr str billing_month: The month in which usages were incurred. Represented in
          yyyy-mm format.
    :attr str billing_country_code: Country.
    :attr str billing_currency_code: The currency in which the account is billed.
    :attr ResourcesSummary resources: Charges related to cloud resources.
    :attr List[Offer] offers: The list of offers applicable for the account for the
          month.
    :attr List[SupportSummary] support: Support-related charges.
    :attr SubscriptionSummary subscription: A summary of charges and credits related
          to a subscription.
    """

    def __init__(self,
                 account_id: str,
                 billing_month: str,
                 billing_country_code: str,
                 billing_currency_code: str,
                 resources: 'ResourcesSummary',
                 offers: List['Offer'],
                 support: List['SupportSummary'],
                 subscription: 'SubscriptionSummary') -> None:
        """
        Initialize a AccountSummary object.

        :param str account_id: The ID of the account.
        :param str billing_month: The month in which usages were incurred.
               Represented in yyyy-mm format.
        :param str billing_country_code: Country.
        :param str billing_currency_code: The currency in which the account is
               billed.
        :param ResourcesSummary resources: Charges related to cloud resources.
        :param List[Offer] offers: The list of offers applicable for the account
               for the month.
        :param List[SupportSummary] support: Support-related charges.
        :param SubscriptionSummary subscription: A summary of charges and credits
               related to a subscription.
        """
        self.account_id = account_id
        self.billing_month = billing_month
        self.billing_country_code = billing_country_code
        self.billing_currency_code = billing_currency_code
        self.resources = resources
        self.offers = offers
        self.support = support
        self.subscription = subscription

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountSummary':
        """Initialize a AccountSummary object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in AccountSummary JSON')
        if 'billing_month' in _dict:
            args['billing_month'] = _dict.get('billing_month')
        else:
            raise ValueError('Required property \'billing_month\' not present in AccountSummary JSON')
        if 'billing_country_code' in _dict:
            args['billing_country_code'] = _dict.get('billing_country_code')
        else:
            raise ValueError('Required property \'billing_country_code\' not present in AccountSummary JSON')
        if 'billing_currency_code' in _dict:
            args['billing_currency_code'] = _dict.get('billing_currency_code')
        else:
            raise ValueError('Required property \'billing_currency_code\' not present in AccountSummary JSON')
        if 'resources' in _dict:
            args['resources'] = ResourcesSummary.from_dict(_dict.get('resources'))
        else:
            raise ValueError('Required property \'resources\' not present in AccountSummary JSON')
        if 'offers' in _dict:
            args['offers'] = [Offer.from_dict(x) for x in _dict.get('offers')]
        else:
            raise ValueError('Required property \'offers\' not present in AccountSummary JSON')
        if 'support' in _dict:
            args['support'] = [SupportSummary.from_dict(x) for x in _dict.get('support')]
        else:
            raise ValueError('Required property \'support\' not present in AccountSummary JSON')
        if 'subscription' in _dict:
            args['subscription'] = SubscriptionSummary.from_dict(_dict.get('subscription'))
        else:
            raise ValueError('Required property \'subscription\' not present in AccountSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'billing_month') and self.billing_month is not None:
            _dict['billing_month'] = self.billing_month
        if hasattr(self, 'billing_country_code') and self.billing_country_code is not None:
            _dict['billing_country_code'] = self.billing_country_code
        if hasattr(self, 'billing_currency_code') and self.billing_currency_code is not None:
            _dict['billing_currency_code'] = self.billing_currency_code
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = self.resources.to_dict()
        if hasattr(self, 'offers') and self.offers is not None:
            _dict['offers'] = [x.to_dict() for x in self.offers]
        if hasattr(self, 'support') and self.support is not None:
            _dict['support'] = [x.to_dict() for x in self.support]
        if hasattr(self, 'subscription') and self.subscription is not None:
            _dict['subscription'] = self.subscription.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AccountUsage():
    """
    The aggregated usage and charges for all the plans in the account.

    :attr str account_id: The ID of the account.
    :attr str pricing_country: The target country pricing that should be used.
    :attr str currency_code: The currency for the cost fields in the resources,
          plans and metrics.
    :attr str month: The month.
    :attr List[Resource] resources: All the resource used in the account.
    """

    def __init__(self,
                 account_id: str,
                 pricing_country: str,
                 currency_code: str,
                 month: str,
                 resources: List['Resource']) -> None:
        """
        Initialize a AccountUsage object.

        :param str account_id: The ID of the account.
        :param str pricing_country: The target country pricing that should be used.
        :param str currency_code: The currency for the cost fields in the
               resources, plans and metrics.
        :param str month: The month.
        :param List[Resource] resources: All the resource used in the account.
        """
        self.account_id = account_id
        self.pricing_country = pricing_country
        self.currency_code = currency_code
        self.month = month
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountUsage':
        """Initialize a AccountUsage object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in AccountUsage JSON')
        if 'pricing_country' in _dict:
            args['pricing_country'] = _dict.get('pricing_country')
        else:
            raise ValueError('Required property \'pricing_country\' not present in AccountUsage JSON')
        if 'currency_code' in _dict:
            args['currency_code'] = _dict.get('currency_code')
        else:
            raise ValueError('Required property \'currency_code\' not present in AccountUsage JSON')
        if 'month' in _dict:
            args['month'] = _dict.get('month')
        else:
            raise ValueError('Required property \'month\' not present in AccountUsage JSON')
        if 'resources' in _dict:
            args['resources'] = [Resource.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in AccountUsage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'pricing_country') and self.pricing_country is not None:
            _dict['pricing_country'] = self.pricing_country
        if hasattr(self, 'currency_code') and self.currency_code is not None:
            _dict['currency_code'] = self.currency_code
        if hasattr(self, 'month') and self.month is not None:
            _dict['month'] = self.month
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Discount():
    """
    Information about a discount that is associated with a metric.

    :attr str ref: The reference ID of the discount.
    :attr str name: (optional) The name of the discount indicating category.
    :attr str display_name: (optional) The name of the discount.
    :attr float discount: The discount percentage.
    """

    def __init__(self,
                 ref: str,
                 discount: float,
                 *,
                 name: str = None,
                 display_name: str = None) -> None:
        """
        Initialize a Discount object.

        :param str ref: The reference ID of the discount.
        :param float discount: The discount percentage.
        :param str name: (optional) The name of the discount indicating category.
        :param str display_name: (optional) The name of the discount.
        """
        self.ref = ref
        self.name = name
        self.display_name = display_name
        self.discount = discount

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Discount':
        """Initialize a Discount object from a json dictionary."""
        args = {}
        if 'ref' in _dict:
            args['ref'] = _dict.get('ref')
        else:
            raise ValueError('Required property \'ref\' not present in Discount JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'discount' in _dict:
            args['discount'] = _dict.get('discount')
        else:
            raise ValueError('Required property \'discount\' not present in Discount JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Discount object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ref') and self.ref is not None:
            _dict['ref'] = self.ref
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'discount') and self.discount is not None:
            _dict['discount'] = self.discount
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Discount object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Discount') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Discount') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstanceUsage():
    """
    The aggregated usage and charges for an instance.

    :attr str account_id: The ID of the account.
    :attr str resource_instance_id: The ID of the resource instance.
    :attr str resource_instance_name: (optional) The name of the resource instance.
    :attr str resource_id: The ID of the resource.
    :attr str resource_name: (optional) The name of the resource.
    :attr str resource_group_id: (optional) The ID of the resource group.
    :attr str resource_group_name: (optional) The name of the resource group.
    :attr str organization_id: (optional) The ID of the organization.
    :attr str organization_name: (optional) The name of the organization.
    :attr str space_id: (optional) The ID of the space.
    :attr str space_name: (optional) The name of the space.
    :attr str consumer_id: (optional) The ID of the consumer.
    :attr str region: (optional) The region where instance was provisioned.
    :attr str pricing_region: (optional) The pricing region where the usage that was
          submitted was rated.
    :attr str pricing_country: The target country pricing that should be used.
    :attr str currency_code: The currency for the cost fields in the resources,
          plans and metrics.
    :attr bool billable: Is the cost charged to the account.
    :attr str plan_id: The ID of the plan where the instance was provisioned and
          rated.
    :attr str plan_name: (optional) The name of the plan where the instance was
          provisioned and rated.
    :attr str month: The month.
    :attr List[Metric] usage: All the resource used in the account.
    """

    def __init__(self,
                 account_id: str,
                 resource_instance_id: str,
                 resource_id: str,
                 pricing_country: str,
                 currency_code: str,
                 billable: bool,
                 plan_id: str,
                 month: str,
                 usage: List['Metric'],
                 *,
                 resource_instance_name: str = None,
                 resource_name: str = None,
                 resource_group_id: str = None,
                 resource_group_name: str = None,
                 organization_id: str = None,
                 organization_name: str = None,
                 space_id: str = None,
                 space_name: str = None,
                 consumer_id: str = None,
                 region: str = None,
                 pricing_region: str = None,
                 plan_name: str = None) -> None:
        """
        Initialize a InstanceUsage object.

        :param str account_id: The ID of the account.
        :param str resource_instance_id: The ID of the resource instance.
        :param str resource_id: The ID of the resource.
        :param str pricing_country: The target country pricing that should be used.
        :param str currency_code: The currency for the cost fields in the
               resources, plans and metrics.
        :param bool billable: Is the cost charged to the account.
        :param str plan_id: The ID of the plan where the instance was provisioned
               and rated.
        :param str month: The month.
        :param List[Metric] usage: All the resource used in the account.
        :param str resource_instance_name: (optional) The name of the resource
               instance.
        :param str resource_name: (optional) The name of the resource.
        :param str resource_group_id: (optional) The ID of the resource group.
        :param str resource_group_name: (optional) The name of the resource group.
        :param str organization_id: (optional) The ID of the organization.
        :param str organization_name: (optional) The name of the organization.
        :param str space_id: (optional) The ID of the space.
        :param str space_name: (optional) The name of the space.
        :param str consumer_id: (optional) The ID of the consumer.
        :param str region: (optional) The region where instance was provisioned.
        :param str pricing_region: (optional) The pricing region where the usage
               that was submitted was rated.
        :param str plan_name: (optional) The name of the plan where the instance
               was provisioned and rated.
        """
        self.account_id = account_id
        self.resource_instance_id = resource_instance_id
        self.resource_instance_name = resource_instance_name
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.space_id = space_id
        self.space_name = space_name
        self.consumer_id = consumer_id
        self.region = region
        self.pricing_region = pricing_region
        self.pricing_country = pricing_country
        self.currency_code = currency_code
        self.billable = billable
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.month = month
        self.usage = usage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstanceUsage':
        """Initialize a InstanceUsage object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in InstanceUsage JSON')
        if 'resource_instance_id' in _dict:
            args['resource_instance_id'] = _dict.get('resource_instance_id')
        else:
            raise ValueError('Required property \'resource_instance_id\' not present in InstanceUsage JSON')
        if 'resource_instance_name' in _dict:
            args['resource_instance_name'] = _dict.get('resource_instance_name')
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        else:
            raise ValueError('Required property \'resource_id\' not present in InstanceUsage JSON')
        if 'resource_name' in _dict:
            args['resource_name'] = _dict.get('resource_name')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        if 'resource_group_name' in _dict:
            args['resource_group_name'] = _dict.get('resource_group_name')
        if 'organization_id' in _dict:
            args['organization_id'] = _dict.get('organization_id')
        if 'organization_name' in _dict:
            args['organization_name'] = _dict.get('organization_name')
        if 'space_id' in _dict:
            args['space_id'] = _dict.get('space_id')
        if 'space_name' in _dict:
            args['space_name'] = _dict.get('space_name')
        if 'consumer_id' in _dict:
            args['consumer_id'] = _dict.get('consumer_id')
        if 'region' in _dict:
            args['region'] = _dict.get('region')
        if 'pricing_region' in _dict:
            args['pricing_region'] = _dict.get('pricing_region')
        if 'pricing_country' in _dict:
            args['pricing_country'] = _dict.get('pricing_country')
        else:
            raise ValueError('Required property \'pricing_country\' not present in InstanceUsage JSON')
        if 'currency_code' in _dict:
            args['currency_code'] = _dict.get('currency_code')
        else:
            raise ValueError('Required property \'currency_code\' not present in InstanceUsage JSON')
        if 'billable' in _dict:
            args['billable'] = _dict.get('billable')
        else:
            raise ValueError('Required property \'billable\' not present in InstanceUsage JSON')
        if 'plan_id' in _dict:
            args['plan_id'] = _dict.get('plan_id')
        else:
            raise ValueError('Required property \'plan_id\' not present in InstanceUsage JSON')
        if 'plan_name' in _dict:
            args['plan_name'] = _dict.get('plan_name')
        if 'month' in _dict:
            args['month'] = _dict.get('month')
        else:
            raise ValueError('Required property \'month\' not present in InstanceUsage JSON')
        if 'usage' in _dict:
            args['usage'] = [Metric.from_dict(x) for x in _dict.get('usage')]
        else:
            raise ValueError('Required property \'usage\' not present in InstanceUsage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstanceUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'resource_instance_id') and self.resource_instance_id is not None:
            _dict['resource_instance_id'] = self.resource_instance_id
        if hasattr(self, 'resource_instance_name') and self.resource_instance_name is not None:
            _dict['resource_instance_name'] = self.resource_instance_name
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
        if hasattr(self, 'resource_name') and self.resource_name is not None:
            _dict['resource_name'] = self.resource_name
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'resource_group_name') and self.resource_group_name is not None:
            _dict['resource_group_name'] = self.resource_group_name
        if hasattr(self, 'organization_id') and self.organization_id is not None:
            _dict['organization_id'] = self.organization_id
        if hasattr(self, 'organization_name') and self.organization_name is not None:
            _dict['organization_name'] = self.organization_name
        if hasattr(self, 'space_id') and self.space_id is not None:
            _dict['space_id'] = self.space_id
        if hasattr(self, 'space_name') and self.space_name is not None:
            _dict['space_name'] = self.space_name
        if hasattr(self, 'consumer_id') and self.consumer_id is not None:
            _dict['consumer_id'] = self.consumer_id
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'pricing_region') and self.pricing_region is not None:
            _dict['pricing_region'] = self.pricing_region
        if hasattr(self, 'pricing_country') and self.pricing_country is not None:
            _dict['pricing_country'] = self.pricing_country
        if hasattr(self, 'currency_code') and self.currency_code is not None:
            _dict['currency_code'] = self.currency_code
        if hasattr(self, 'billable') and self.billable is not None:
            _dict['billable'] = self.billable
        if hasattr(self, 'plan_id') and self.plan_id is not None:
            _dict['plan_id'] = self.plan_id
        if hasattr(self, 'plan_name') and self.plan_name is not None:
            _dict['plan_name'] = self.plan_name
        if hasattr(self, 'month') and self.month is not None:
            _dict['month'] = self.month
        if hasattr(self, 'usage') and self.usage is not None:
            _dict['usage'] = [x.to_dict() for x in self.usage]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstanceUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstanceUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstanceUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstancesUsageFirst():
    """
    The link to the first page of the search query.

    :attr str href: (optional) A link to a page of query results.
    """

    def __init__(self,
                 *,
                 href: str = None) -> None:
        """
        Initialize a InstancesUsageFirst object.

        :param str href: (optional) A link to a page of query results.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstancesUsageFirst':
        """Initialize a InstancesUsageFirst object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstancesUsageFirst object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstancesUsageFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstancesUsageFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstancesUsageFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstancesUsageNext():
    """
    The link to the next page of the search query.

    :attr str href: (optional) A link to a page of query results.
    :attr str offset: (optional) The value of the `_start` query parameter to fetch
          the next page.
    """

    def __init__(self,
                 *,
                 href: str = None,
                 offset: str = None) -> None:
        """
        Initialize a InstancesUsageNext object.

        :param str href: (optional) A link to a page of query results.
        :param str offset: (optional) The value of the `_start` query parameter to
               fetch the next page.
        """
        self.href = href
        self.offset = offset

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstancesUsageNext':
        """Initialize a InstancesUsageNext object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstancesUsageNext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstancesUsageNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstancesUsageNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstancesUsageNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstancesUsage():
    """
    The list of instance usage reports.

    :attr int limit: (optional) The max number of reports in the response.
    :attr int count: (optional) The number of reports in the response.
    :attr InstancesUsageFirst first: (optional) The link to the first page of the
          search query.
    :attr InstancesUsageNext next: (optional) The link to the next page of the
          search query.
    :attr List[InstanceUsage] resources: (optional) The list of instance usage
          reports.
    """

    def __init__(self,
                 *,
                 limit: int = None,
                 count: int = None,
                 first: 'InstancesUsageFirst' = None,
                 next: 'InstancesUsageNext' = None,
                 resources: List['InstanceUsage'] = None) -> None:
        """
        Initialize a InstancesUsage object.

        :param int limit: (optional) The max number of reports in the response.
        :param int count: (optional) The number of reports in the response.
        :param InstancesUsageFirst first: (optional) The link to the first page of
               the search query.
        :param InstancesUsageNext next: (optional) The link to the next page of the
               search query.
        :param List[InstanceUsage] resources: (optional) The list of instance usage
               reports.
        """
        self.limit = limit
        self.count = count
        self.first = first
        self.next = next
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstancesUsage':
        """Initialize a InstancesUsage object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'first' in _dict:
            args['first'] = InstancesUsageFirst.from_dict(_dict.get('first'))
        if 'next' in _dict:
            args['next'] = InstancesUsageNext.from_dict(_dict.get('next'))
        if 'resources' in _dict:
            args['resources'] = [InstanceUsage.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstancesUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstancesUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstancesUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstancesUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Metric():
    """
    Information about a metric.

    :attr str metric: The ID of the metric.
    :attr str metric_name: (optional) The name of the metric.
    :attr float quantity: The aggregated value for the metric.
    :attr float rateable_quantity: (optional) The quantity that is used for
          calculating charges.
    :attr float cost: The cost incurred by the metric.
    :attr float rated_cost: Pre-discounted cost incurred by the metric.
    :attr List[object] price: (optional) The price with which the cost was
          calculated.
    :attr str unit: (optional) The unit that qualifies the quantity.
    :attr str unit_name: (optional) The name of the unit.
    :attr bool non_chargeable: (optional) When set to `true`, the cost is for
          informational purpose and is not included while calculating the plan charges.
    :attr List[Discount] discounts: All the discounts applicable to the metric.
    """

    def __init__(self,
                 metric: str,
                 quantity: float,
                 cost: float,
                 rated_cost: float,
                 discounts: List['Discount'],
                 *,
                 metric_name: str = None,
                 rateable_quantity: float = None,
                 price: List[object] = None,
                 unit: str = None,
                 unit_name: str = None,
                 non_chargeable: bool = None) -> None:
        """
        Initialize a Metric object.

        :param str metric: The ID of the metric.
        :param float quantity: The aggregated value for the metric.
        :param float cost: The cost incurred by the metric.
        :param float rated_cost: Pre-discounted cost incurred by the metric.
        :param List[Discount] discounts: All the discounts applicable to the
               metric.
        :param str metric_name: (optional) The name of the metric.
        :param float rateable_quantity: (optional) The quantity that is used for
               calculating charges.
        :param List[object] price: (optional) The price with which the cost was
               calculated.
        :param str unit: (optional) The unit that qualifies the quantity.
        :param str unit_name: (optional) The name of the unit.
        :param bool non_chargeable: (optional) When set to `true`, the cost is for
               informational purpose and is not included while calculating the plan
               charges.
        """
        self.metric = metric
        self.metric_name = metric_name
        self.quantity = quantity
        self.rateable_quantity = rateable_quantity
        self.cost = cost
        self.rated_cost = rated_cost
        self.price = price
        self.unit = unit
        self.unit_name = unit_name
        self.non_chargeable = non_chargeable
        self.discounts = discounts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Metric':
        """Initialize a Metric object from a json dictionary."""
        args = {}
        if 'metric' in _dict:
            args['metric'] = _dict.get('metric')
        else:
            raise ValueError('Required property \'metric\' not present in Metric JSON')
        if 'metric_name' in _dict:
            args['metric_name'] = _dict.get('metric_name')
        if 'quantity' in _dict:
            args['quantity'] = _dict.get('quantity')
        else:
            raise ValueError('Required property \'quantity\' not present in Metric JSON')
        if 'rateable_quantity' in _dict:
            args['rateable_quantity'] = _dict.get('rateable_quantity')
        if 'cost' in _dict:
            args['cost'] = _dict.get('cost')
        else:
            raise ValueError('Required property \'cost\' not present in Metric JSON')
        if 'rated_cost' in _dict:
            args['rated_cost'] = _dict.get('rated_cost')
        else:
            raise ValueError('Required property \'rated_cost\' not present in Metric JSON')
        if 'price' in _dict:
            args['price'] = _dict.get('price')
        if 'unit' in _dict:
            args['unit'] = _dict.get('unit')
        if 'unit_name' in _dict:
            args['unit_name'] = _dict.get('unit_name')
        if 'non_chargeable' in _dict:
            args['non_chargeable'] = _dict.get('non_chargeable')
        if 'discounts' in _dict:
            args['discounts'] = [Discount.from_dict(x) for x in _dict.get('discounts')]
        else:
            raise ValueError('Required property \'discounts\' not present in Metric JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Metric object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'metric') and self.metric is not None:
            _dict['metric'] = self.metric
        if hasattr(self, 'metric_name') and self.metric_name is not None:
            _dict['metric_name'] = self.metric_name
        if hasattr(self, 'quantity') and self.quantity is not None:
            _dict['quantity'] = self.quantity
        if hasattr(self, 'rateable_quantity') and self.rateable_quantity is not None:
            _dict['rateable_quantity'] = self.rateable_quantity
        if hasattr(self, 'cost') and self.cost is not None:
            _dict['cost'] = self.cost
        if hasattr(self, 'rated_cost') and self.rated_cost is not None:
            _dict['rated_cost'] = self.rated_cost
        if hasattr(self, 'price') and self.price is not None:
            _dict['price'] = self.price
        if hasattr(self, 'unit') and self.unit is not None:
            _dict['unit'] = self.unit
        if hasattr(self, 'unit_name') and self.unit_name is not None:
            _dict['unit_name'] = self.unit_name
        if hasattr(self, 'non_chargeable') and self.non_chargeable is not None:
            _dict['non_chargeable'] = self.non_chargeable
        if hasattr(self, 'discounts') and self.discounts is not None:
            _dict['discounts'] = [x.to_dict() for x in self.discounts]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Metric object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Metric') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Metric') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Offer():
    """
    Information about an individual offer.

    :attr str offer_id: The ID of the offer.
    :attr float credits_total: The total credits before applying the offer.
    :attr str offer_template: The template with which the offer was generated.
    :attr datetime valid_from: The date from which the offer is valid.
    :attr datetime expires_on: The date until the offer is valid.
    :attr OfferCredits credits: Credit information related to an offer.
    """

    def __init__(self,
                 offer_id: str,
                 credits_total: float,
                 offer_template: str,
                 valid_from: datetime,
                 expires_on: datetime,
                 credits: 'OfferCredits') -> None:
        """
        Initialize a Offer object.

        :param str offer_id: The ID of the offer.
        :param float credits_total: The total credits before applying the offer.
        :param str offer_template: The template with which the offer was generated.
        :param datetime valid_from: The date from which the offer is valid.
        :param datetime expires_on: The date until the offer is valid.
        :param OfferCredits credits: Credit information related to an offer.
        """
        self.offer_id = offer_id
        self.credits_total = credits_total
        self.offer_template = offer_template
        self.valid_from = valid_from
        self.expires_on = expires_on
        self.credits = credits

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Offer':
        """Initialize a Offer object from a json dictionary."""
        args = {}
        if 'offer_id' in _dict:
            args['offer_id'] = _dict.get('offer_id')
        else:
            raise ValueError('Required property \'offer_id\' not present in Offer JSON')
        if 'credits_total' in _dict:
            args['credits_total'] = _dict.get('credits_total')
        else:
            raise ValueError('Required property \'credits_total\' not present in Offer JSON')
        if 'offer_template' in _dict:
            args['offer_template'] = _dict.get('offer_template')
        else:
            raise ValueError('Required property \'offer_template\' not present in Offer JSON')
        if 'valid_from' in _dict:
            args['valid_from'] = string_to_datetime(_dict.get('valid_from'))
        else:
            raise ValueError('Required property \'valid_from\' not present in Offer JSON')
        if 'expires_on' in _dict:
            args['expires_on'] = string_to_datetime(_dict.get('expires_on'))
        else:
            raise ValueError('Required property \'expires_on\' not present in Offer JSON')
        if 'credits' in _dict:
            args['credits'] = OfferCredits.from_dict(_dict.get('credits'))
        else:
            raise ValueError('Required property \'credits\' not present in Offer JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Offer object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offer_id') and self.offer_id is not None:
            _dict['offer_id'] = self.offer_id
        if hasattr(self, 'credits_total') and self.credits_total is not None:
            _dict['credits_total'] = self.credits_total
        if hasattr(self, 'offer_template') and self.offer_template is not None:
            _dict['offer_template'] = self.offer_template
        if hasattr(self, 'valid_from') and self.valid_from is not None:
            _dict['valid_from'] = datetime_to_string(self.valid_from)
        if hasattr(self, 'expires_on') and self.expires_on is not None:
            _dict['expires_on'] = datetime_to_string(self.expires_on)
        if hasattr(self, 'credits') and self.credits is not None:
            _dict['credits'] = self.credits.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Offer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Offer') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Offer') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OfferCredits():
    """
    Credit information related to an offer.

    :attr float starting_balance: The available credits in the offer at the
          beginning of the month.
    :attr float used: The credits used in this month.
    :attr float balance: The remaining credits in the offer.
    """

    def __init__(self,
                 starting_balance: float,
                 used: float,
                 balance: float) -> None:
        """
        Initialize a OfferCredits object.

        :param float starting_balance: The available credits in the offer at the
               beginning of the month.
        :param float used: The credits used in this month.
        :param float balance: The remaining credits in the offer.
        """
        self.starting_balance = starting_balance
        self.used = used
        self.balance = balance

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OfferCredits':
        """Initialize a OfferCredits object from a json dictionary."""
        args = {}
        if 'starting_balance' in _dict:
            args['starting_balance'] = _dict.get('starting_balance')
        else:
            raise ValueError('Required property \'starting_balance\' not present in OfferCredits JSON')
        if 'used' in _dict:
            args['used'] = _dict.get('used')
        else:
            raise ValueError('Required property \'used\' not present in OfferCredits JSON')
        if 'balance' in _dict:
            args['balance'] = _dict.get('balance')
        else:
            raise ValueError('Required property \'balance\' not present in OfferCredits JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OfferCredits object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'starting_balance') and self.starting_balance is not None:
            _dict['starting_balance'] = self.starting_balance
        if hasattr(self, 'used') and self.used is not None:
            _dict['used'] = self.used
        if hasattr(self, 'balance') and self.balance is not None:
            _dict['balance'] = self.balance
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OfferCredits object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OfferCredits') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OfferCredits') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OrgUsage():
    """
    The aggregated usage and charges for all the plans in the org.

    :attr str account_id: The ID of the account.
    :attr str organization_id: The ID of the organization.
    :attr str organization_name: (optional) The name of the organization.
    :attr str pricing_country: The target country pricing that should be used.
    :attr str currency_code: The currency for the cost fields in the resources,
          plans and metrics.
    :attr str month: The month.
    :attr List[Resource] resources: All the resource used in the account.
    """

    def __init__(self,
                 account_id: str,
                 organization_id: str,
                 pricing_country: str,
                 currency_code: str,
                 month: str,
                 resources: List['Resource'],
                 *,
                 organization_name: str = None) -> None:
        """
        Initialize a OrgUsage object.

        :param str account_id: The ID of the account.
        :param str organization_id: The ID of the organization.
        :param str pricing_country: The target country pricing that should be used.
        :param str currency_code: The currency for the cost fields in the
               resources, plans and metrics.
        :param str month: The month.
        :param List[Resource] resources: All the resource used in the account.
        :param str organization_name: (optional) The name of the organization.
        """
        self.account_id = account_id
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.pricing_country = pricing_country
        self.currency_code = currency_code
        self.month = month
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OrgUsage':
        """Initialize a OrgUsage object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in OrgUsage JSON')
        if 'organization_id' in _dict:
            args['organization_id'] = _dict.get('organization_id')
        else:
            raise ValueError('Required property \'organization_id\' not present in OrgUsage JSON')
        if 'organization_name' in _dict:
            args['organization_name'] = _dict.get('organization_name')
        if 'pricing_country' in _dict:
            args['pricing_country'] = _dict.get('pricing_country')
        else:
            raise ValueError('Required property \'pricing_country\' not present in OrgUsage JSON')
        if 'currency_code' in _dict:
            args['currency_code'] = _dict.get('currency_code')
        else:
            raise ValueError('Required property \'currency_code\' not present in OrgUsage JSON')
        if 'month' in _dict:
            args['month'] = _dict.get('month')
        else:
            raise ValueError('Required property \'month\' not present in OrgUsage JSON')
        if 'resources' in _dict:
            args['resources'] = [Resource.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in OrgUsage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OrgUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'organization_id') and self.organization_id is not None:
            _dict['organization_id'] = self.organization_id
        if hasattr(self, 'organization_name') and self.organization_name is not None:
            _dict['organization_name'] = self.organization_name
        if hasattr(self, 'pricing_country') and self.pricing_country is not None:
            _dict['pricing_country'] = self.pricing_country
        if hasattr(self, 'currency_code') and self.currency_code is not None:
            _dict['currency_code'] = self.currency_code
        if hasattr(self, 'month') and self.month is not None:
            _dict['month'] = self.month
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OrgUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OrgUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OrgUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Plan():
    """
    The aggregated values for the plan.

    :attr str plan_id: The ID of the plan.
    :attr str plan_name: (optional) The name of the plan.
    :attr str pricing_region: (optional) The pricing region for the plan.
    :attr bool billable: Indicates if the plan charges are billed to the customer.
    :attr float cost: The total cost incurred by the plan.
    :attr float rated_cost: Total pre-discounted cost incurred by the plan.
    :attr List[Metric] usage: All the metrics in the plan.
    :attr List[Discount] discounts: All the discounts applicable to the plan.
    """

    def __init__(self,
                 plan_id: str,
                 billable: bool,
                 cost: float,
                 rated_cost: float,
                 usage: List['Metric'],
                 discounts: List['Discount'],
                 *,
                 plan_name: str = None,
                 pricing_region: str = None) -> None:
        """
        Initialize a Plan object.

        :param str plan_id: The ID of the plan.
        :param bool billable: Indicates if the plan charges are billed to the
               customer.
        :param float cost: The total cost incurred by the plan.
        :param float rated_cost: Total pre-discounted cost incurred by the plan.
        :param List[Metric] usage: All the metrics in the plan.
        :param List[Discount] discounts: All the discounts applicable to the plan.
        :param str plan_name: (optional) The name of the plan.
        :param str pricing_region: (optional) The pricing region for the plan.
        """
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.pricing_region = pricing_region
        self.billable = billable
        self.cost = cost
        self.rated_cost = rated_cost
        self.usage = usage
        self.discounts = discounts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Plan':
        """Initialize a Plan object from a json dictionary."""
        args = {}
        if 'plan_id' in _dict:
            args['plan_id'] = _dict.get('plan_id')
        else:
            raise ValueError('Required property \'plan_id\' not present in Plan JSON')
        if 'plan_name' in _dict:
            args['plan_name'] = _dict.get('plan_name')
        if 'pricing_region' in _dict:
            args['pricing_region'] = _dict.get('pricing_region')
        if 'billable' in _dict:
            args['billable'] = _dict.get('billable')
        else:
            raise ValueError('Required property \'billable\' not present in Plan JSON')
        if 'cost' in _dict:
            args['cost'] = _dict.get('cost')
        else:
            raise ValueError('Required property \'cost\' not present in Plan JSON')
        if 'rated_cost' in _dict:
            args['rated_cost'] = _dict.get('rated_cost')
        else:
            raise ValueError('Required property \'rated_cost\' not present in Plan JSON')
        if 'usage' in _dict:
            args['usage'] = [Metric.from_dict(x) for x in _dict.get('usage')]
        else:
            raise ValueError('Required property \'usage\' not present in Plan JSON')
        if 'discounts' in _dict:
            args['discounts'] = [Discount.from_dict(x) for x in _dict.get('discounts')]
        else:
            raise ValueError('Required property \'discounts\' not present in Plan JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Plan object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'plan_id') and self.plan_id is not None:
            _dict['plan_id'] = self.plan_id
        if hasattr(self, 'plan_name') and self.plan_name is not None:
            _dict['plan_name'] = self.plan_name
        if hasattr(self, 'pricing_region') and self.pricing_region is not None:
            _dict['pricing_region'] = self.pricing_region
        if hasattr(self, 'billable') and self.billable is not None:
            _dict['billable'] = self.billable
        if hasattr(self, 'cost') and self.cost is not None:
            _dict['cost'] = self.cost
        if hasattr(self, 'rated_cost') and self.rated_cost is not None:
            _dict['rated_cost'] = self.rated_cost
        if hasattr(self, 'usage') and self.usage is not None:
            _dict['usage'] = [x.to_dict() for x in self.usage]
        if hasattr(self, 'discounts') and self.discounts is not None:
            _dict['discounts'] = [x.to_dict() for x in self.discounts]
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

class Resource():
    """
    The container for all the plans in the resource.

    :attr str resource_id: The ID of the resource.
    :attr str resource_name: (optional) The name of the resource.
    :attr float billable_cost: The billable charges for the account.
    :attr float billable_rated_cost: The pre-discounted billable charges for the
          account.
    :attr float non_billable_cost: The non-billable charges for the account.
    :attr float non_billable_rated_cost: The pre-discounted non-billable charges for
          the account.
    :attr List[Plan] plans: All the plans in the resource.
    :attr List[Discount] discounts: All the discounts applicable to the resource.
    """

    def __init__(self,
                 resource_id: str,
                 billable_cost: float,
                 billable_rated_cost: float,
                 non_billable_cost: float,
                 non_billable_rated_cost: float,
                 plans: List['Plan'],
                 discounts: List['Discount'],
                 *,
                 resource_name: str = None) -> None:
        """
        Initialize a Resource object.

        :param str resource_id: The ID of the resource.
        :param float billable_cost: The billable charges for the account.
        :param float billable_rated_cost: The pre-discounted billable charges for
               the account.
        :param float non_billable_cost: The non-billable charges for the account.
        :param float non_billable_rated_cost: The pre-discounted non-billable
               charges for the account.
        :param List[Plan] plans: All the plans in the resource.
        :param List[Discount] discounts: All the discounts applicable to the
               resource.
        :param str resource_name: (optional) The name of the resource.
        """
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.billable_cost = billable_cost
        self.billable_rated_cost = billable_rated_cost
        self.non_billable_cost = non_billable_cost
        self.non_billable_rated_cost = non_billable_rated_cost
        self.plans = plans
        self.discounts = discounts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Resource':
        """Initialize a Resource object from a json dictionary."""
        args = {}
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        else:
            raise ValueError('Required property \'resource_id\' not present in Resource JSON')
        if 'resource_name' in _dict:
            args['resource_name'] = _dict.get('resource_name')
        if 'billable_cost' in _dict:
            args['billable_cost'] = _dict.get('billable_cost')
        else:
            raise ValueError('Required property \'billable_cost\' not present in Resource JSON')
        if 'billable_rated_cost' in _dict:
            args['billable_rated_cost'] = _dict.get('billable_rated_cost')
        else:
            raise ValueError('Required property \'billable_rated_cost\' not present in Resource JSON')
        if 'non_billable_cost' in _dict:
            args['non_billable_cost'] = _dict.get('non_billable_cost')
        else:
            raise ValueError('Required property \'non_billable_cost\' not present in Resource JSON')
        if 'non_billable_rated_cost' in _dict:
            args['non_billable_rated_cost'] = _dict.get('non_billable_rated_cost')
        else:
            raise ValueError('Required property \'non_billable_rated_cost\' not present in Resource JSON')
        if 'plans' in _dict:
            args['plans'] = [Plan.from_dict(x) for x in _dict.get('plans')]
        else:
            raise ValueError('Required property \'plans\' not present in Resource JSON')
        if 'discounts' in _dict:
            args['discounts'] = [Discount.from_dict(x) for x in _dict.get('discounts')]
        else:
            raise ValueError('Required property \'discounts\' not present in Resource JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Resource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
        if hasattr(self, 'resource_name') and self.resource_name is not None:
            _dict['resource_name'] = self.resource_name
        if hasattr(self, 'billable_cost') and self.billable_cost is not None:
            _dict['billable_cost'] = self.billable_cost
        if hasattr(self, 'billable_rated_cost') and self.billable_rated_cost is not None:
            _dict['billable_rated_cost'] = self.billable_rated_cost
        if hasattr(self, 'non_billable_cost') and self.non_billable_cost is not None:
            _dict['non_billable_cost'] = self.non_billable_cost
        if hasattr(self, 'non_billable_rated_cost') and self.non_billable_rated_cost is not None:
            _dict['non_billable_rated_cost'] = self.non_billable_rated_cost
        if hasattr(self, 'plans') and self.plans is not None:
            _dict['plans'] = [x.to_dict() for x in self.plans]
        if hasattr(self, 'discounts') and self.discounts is not None:
            _dict['discounts'] = [x.to_dict() for x in self.discounts]
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

class ResourceGroupUsage():
    """
    The aggregated usage and charges for all the plans in the resource group.

    :attr str account_id: The ID of the account.
    :attr str resource_group_id: The ID of the resource group.
    :attr str resource_group_name: (optional) The name of the resource group.
    :attr str pricing_country: The target country pricing that should be used.
    :attr str currency_code: The currency for the cost fields in the resources,
          plans and metrics.
    :attr str month: The month.
    :attr List[Resource] resources: All the resource used in the account.
    """

    def __init__(self,
                 account_id: str,
                 resource_group_id: str,
                 pricing_country: str,
                 currency_code: str,
                 month: str,
                 resources: List['Resource'],
                 *,
                 resource_group_name: str = None) -> None:
        """
        Initialize a ResourceGroupUsage object.

        :param str account_id: The ID of the account.
        :param str resource_group_id: The ID of the resource group.
        :param str pricing_country: The target country pricing that should be used.
        :param str currency_code: The currency for the cost fields in the
               resources, plans and metrics.
        :param str month: The month.
        :param List[Resource] resources: All the resource used in the account.
        :param str resource_group_name: (optional) The name of the resource group.
        """
        self.account_id = account_id
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.pricing_country = pricing_country
        self.currency_code = currency_code
        self.month = month
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceGroupUsage':
        """Initialize a ResourceGroupUsage object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in ResourceGroupUsage JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ResourceGroupUsage JSON')
        if 'resource_group_name' in _dict:
            args['resource_group_name'] = _dict.get('resource_group_name')
        if 'pricing_country' in _dict:
            args['pricing_country'] = _dict.get('pricing_country')
        else:
            raise ValueError('Required property \'pricing_country\' not present in ResourceGroupUsage JSON')
        if 'currency_code' in _dict:
            args['currency_code'] = _dict.get('currency_code')
        else:
            raise ValueError('Required property \'currency_code\' not present in ResourceGroupUsage JSON')
        if 'month' in _dict:
            args['month'] = _dict.get('month')
        else:
            raise ValueError('Required property \'month\' not present in ResourceGroupUsage JSON')
        if 'resources' in _dict:
            args['resources'] = [Resource.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in ResourceGroupUsage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceGroupUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'resource_group_name') and self.resource_group_name is not None:
            _dict['resource_group_name'] = self.resource_group_name
        if hasattr(self, 'pricing_country') and self.pricing_country is not None:
            _dict['pricing_country'] = self.pricing_country
        if hasattr(self, 'currency_code') and self.currency_code is not None:
            _dict['currency_code'] = self.currency_code
        if hasattr(self, 'month') and self.month is not None:
            _dict['month'] = self.month
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceGroupUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceGroupUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceGroupUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourcesSummary():
    """
    Charges related to cloud resources.

    :attr float billable_cost: The billable charges for all cloud resources used in
          the account.
    :attr float non_billable_cost: Non-billable charges for all cloud resources used
          in the account.
    """

    def __init__(self,
                 billable_cost: float,
                 non_billable_cost: float) -> None:
        """
        Initialize a ResourcesSummary object.

        :param float billable_cost: The billable charges for all cloud resources
               used in the account.
        :param float non_billable_cost: Non-billable charges for all cloud
               resources used in the account.
        """
        self.billable_cost = billable_cost
        self.non_billable_cost = non_billable_cost

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourcesSummary':
        """Initialize a ResourcesSummary object from a json dictionary."""
        args = {}
        if 'billable_cost' in _dict:
            args['billable_cost'] = _dict.get('billable_cost')
        else:
            raise ValueError('Required property \'billable_cost\' not present in ResourcesSummary JSON')
        if 'non_billable_cost' in _dict:
            args['non_billable_cost'] = _dict.get('non_billable_cost')
        else:
            raise ValueError('Required property \'non_billable_cost\' not present in ResourcesSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourcesSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'billable_cost') and self.billable_cost is not None:
            _dict['billable_cost'] = self.billable_cost
        if hasattr(self, 'non_billable_cost') and self.non_billable_cost is not None:
            _dict['non_billable_cost'] = self.non_billable_cost
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourcesSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourcesSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourcesSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Subscription():
    """
    Subscription.

    :attr str subscription_id: The ID of the subscription.
    :attr str charge_agreement_number: The charge agreement number of the
          subsciption.
    :attr str type: Type of the subscription.
    :attr float subscription_amount: The credits available in the subscription for
          the month.
    :attr datetime start: The date from which the subscription was active.
    :attr datetime end: (optional) The date until which the subscription is active.
          End time is unavailable for PayGO accounts.
    :attr float credits_total: The total credits available in the subscription.
    :attr List[SubscriptionTerm] terms: The terms through which the subscription is
          split into.
    """

    def __init__(self,
                 subscription_id: str,
                 charge_agreement_number: str,
                 type: str,
                 subscription_amount: float,
                 start: datetime,
                 credits_total: float,
                 terms: List['SubscriptionTerm'],
                 *,
                 end: datetime = None) -> None:
        """
        Initialize a Subscription object.

        :param str subscription_id: The ID of the subscription.
        :param str charge_agreement_number: The charge agreement number of the
               subsciption.
        :param str type: Type of the subscription.
        :param float subscription_amount: The credits available in the subscription
               for the month.
        :param datetime start: The date from which the subscription was active.
        :param float credits_total: The total credits available in the
               subscription.
        :param List[SubscriptionTerm] terms: The terms through which the
               subscription is split into.
        :param datetime end: (optional) The date until which the subscription is
               active. End time is unavailable for PayGO accounts.
        """
        self.subscription_id = subscription_id
        self.charge_agreement_number = charge_agreement_number
        self.type = type
        self.subscription_amount = subscription_amount
        self.start = start
        self.end = end
        self.credits_total = credits_total
        self.terms = terms

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Subscription':
        """Initialize a Subscription object from a json dictionary."""
        args = {}
        if 'subscription_id' in _dict:
            args['subscription_id'] = _dict.get('subscription_id')
        else:
            raise ValueError('Required property \'subscription_id\' not present in Subscription JSON')
        if 'charge_agreement_number' in _dict:
            args['charge_agreement_number'] = _dict.get('charge_agreement_number')
        else:
            raise ValueError('Required property \'charge_agreement_number\' not present in Subscription JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in Subscription JSON')
        if 'subscription_amount' in _dict:
            args['subscription_amount'] = _dict.get('subscription_amount')
        else:
            raise ValueError('Required property \'subscription_amount\' not present in Subscription JSON')
        if 'start' in _dict:
            args['start'] = string_to_datetime(_dict.get('start'))
        else:
            raise ValueError('Required property \'start\' not present in Subscription JSON')
        if 'end' in _dict:
            args['end'] = string_to_datetime(_dict.get('end'))
        if 'credits_total' in _dict:
            args['credits_total'] = _dict.get('credits_total')
        else:
            raise ValueError('Required property \'credits_total\' not present in Subscription JSON')
        if 'terms' in _dict:
            args['terms'] = [SubscriptionTerm.from_dict(x) for x in _dict.get('terms')]
        else:
            raise ValueError('Required property \'terms\' not present in Subscription JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Subscription object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'subscription_id') and self.subscription_id is not None:
            _dict['subscription_id'] = self.subscription_id
        if hasattr(self, 'charge_agreement_number') and self.charge_agreement_number is not None:
            _dict['charge_agreement_number'] = self.charge_agreement_number
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'subscription_amount') and self.subscription_amount is not None:
            _dict['subscription_amount'] = self.subscription_amount
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = datetime_to_string(self.start)
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = datetime_to_string(self.end)
        if hasattr(self, 'credits_total') and self.credits_total is not None:
            _dict['credits_total'] = self.credits_total
        if hasattr(self, 'terms') and self.terms is not None:
            _dict['terms'] = [x.to_dict() for x in self.terms]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Subscription object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Subscription') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Subscription') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SubscriptionSummary():
    """
    A summary of charges and credits related to a subscription.

    :attr float overage: (optional) The charges after exhausting subscription
          credits and offers credits.
    :attr List[Subscription] subscriptions: (optional) The list of subscriptions
          applicable for the month.
    """

    def __init__(self,
                 *,
                 overage: float = None,
                 subscriptions: List['Subscription'] = None) -> None:
        """
        Initialize a SubscriptionSummary object.

        :param float overage: (optional) The charges after exhausting subscription
               credits and offers credits.
        :param List[Subscription] subscriptions: (optional) The list of
               subscriptions applicable for the month.
        """
        self.overage = overage
        self.subscriptions = subscriptions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SubscriptionSummary':
        """Initialize a SubscriptionSummary object from a json dictionary."""
        args = {}
        if 'overage' in _dict:
            args['overage'] = _dict.get('overage')
        if 'subscriptions' in _dict:
            args['subscriptions'] = [Subscription.from_dict(x) for x in _dict.get('subscriptions')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SubscriptionSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'overage') and self.overage is not None:
            _dict['overage'] = self.overage
        if hasattr(self, 'subscriptions') and self.subscriptions is not None:
            _dict['subscriptions'] = [x.to_dict() for x in self.subscriptions]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SubscriptionSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SubscriptionSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SubscriptionSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SubscriptionTerm():
    """
    SubscriptionTerm.

    :attr datetime start: The start date of the term.
    :attr datetime end: The end date of the term.
    :attr SubscriptionTermCredits credits: Information about credits related to a
          subscription.
    """

    def __init__(self,
                 start: datetime,
                 end: datetime,
                 credits: 'SubscriptionTermCredits') -> None:
        """
        Initialize a SubscriptionTerm object.

        :param datetime start: The start date of the term.
        :param datetime end: The end date of the term.
        :param SubscriptionTermCredits credits: Information about credits related
               to a subscription.
        """
        self.start = start
        self.end = end
        self.credits = credits

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SubscriptionTerm':
        """Initialize a SubscriptionTerm object from a json dictionary."""
        args = {}
        if 'start' in _dict:
            args['start'] = string_to_datetime(_dict.get('start'))
        else:
            raise ValueError('Required property \'start\' not present in SubscriptionTerm JSON')
        if 'end' in _dict:
            args['end'] = string_to_datetime(_dict.get('end'))
        else:
            raise ValueError('Required property \'end\' not present in SubscriptionTerm JSON')
        if 'credits' in _dict:
            args['credits'] = SubscriptionTermCredits.from_dict(_dict.get('credits'))
        else:
            raise ValueError('Required property \'credits\' not present in SubscriptionTerm JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SubscriptionTerm object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = datetime_to_string(self.start)
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = datetime_to_string(self.end)
        if hasattr(self, 'credits') and self.credits is not None:
            _dict['credits'] = self.credits.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SubscriptionTerm object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SubscriptionTerm') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SubscriptionTerm') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SubscriptionTermCredits():
    """
    Information about credits related to a subscription.

    :attr float total: The total credits available for the term.
    :attr float starting_balance: The unused credits in the term at the beginning of
          the month.
    :attr float used: The credits used in this month.
    :attr float balance: The remaining credits in this term.
    """

    def __init__(self,
                 total: float,
                 starting_balance: float,
                 used: float,
                 balance: float) -> None:
        """
        Initialize a SubscriptionTermCredits object.

        :param float total: The total credits available for the term.
        :param float starting_balance: The unused credits in the term at the
               beginning of the month.
        :param float used: The credits used in this month.
        :param float balance: The remaining credits in this term.
        """
        self.total = total
        self.starting_balance = starting_balance
        self.used = used
        self.balance = balance

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SubscriptionTermCredits':
        """Initialize a SubscriptionTermCredits object from a json dictionary."""
        args = {}
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        else:
            raise ValueError('Required property \'total\' not present in SubscriptionTermCredits JSON')
        if 'starting_balance' in _dict:
            args['starting_balance'] = _dict.get('starting_balance')
        else:
            raise ValueError('Required property \'starting_balance\' not present in SubscriptionTermCredits JSON')
        if 'used' in _dict:
            args['used'] = _dict.get('used')
        else:
            raise ValueError('Required property \'used\' not present in SubscriptionTermCredits JSON')
        if 'balance' in _dict:
            args['balance'] = _dict.get('balance')
        else:
            raise ValueError('Required property \'balance\' not present in SubscriptionTermCredits JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SubscriptionTermCredits object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        if hasattr(self, 'starting_balance') and self.starting_balance is not None:
            _dict['starting_balance'] = self.starting_balance
        if hasattr(self, 'used') and self.used is not None:
            _dict['used'] = self.used
        if hasattr(self, 'balance') and self.balance is not None:
            _dict['balance'] = self.balance
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SubscriptionTermCredits object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SubscriptionTermCredits') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SubscriptionTermCredits') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SupportSummary():
    """
    SupportSummary.

    :attr float cost: The monthly support cost.
    :attr str type: The type of support.
    :attr float overage: Additional support cost for the month.
    """

    def __init__(self,
                 cost: float,
                 type: str,
                 overage: float) -> None:
        """
        Initialize a SupportSummary object.

        :param float cost: The monthly support cost.
        :param str type: The type of support.
        :param float overage: Additional support cost for the month.
        """
        self.cost = cost
        self.type = type
        self.overage = overage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SupportSummary':
        """Initialize a SupportSummary object from a json dictionary."""
        args = {}
        if 'cost' in _dict:
            args['cost'] = _dict.get('cost')
        else:
            raise ValueError('Required property \'cost\' not present in SupportSummary JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in SupportSummary JSON')
        if 'overage' in _dict:
            args['overage'] = _dict.get('overage')
        else:
            raise ValueError('Required property \'overage\' not present in SupportSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SupportSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cost') and self.cost is not None:
            _dict['cost'] = self.cost
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'overage') and self.overage is not None:
            _dict['overage'] = self.overage
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SupportSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SupportSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SupportSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
