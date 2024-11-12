# coding: utf-8

# (C) Copyright IBM Corp. 2024.
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

# IBM OpenAPI SDK Code Generator Version: 3.96.0-d6dec9d7-20241008-212902

"""
The Partner Management APIs enable you to manage the IBM Cloud partner entities and fetch
multiple reports in different formats.

API Version: 1.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class PartnerManagementV1(BaseService):
    """The Partner Management V1 service."""

    DEFAULT_SERVICE_URL = 'https://partner.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'partner_management'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'PartnerManagementV1':
        """
        Return a new client for the Partner Management service using the specified
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
        Construct a new client for the Partner Management service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Usage Reports
    #########################

    def get_resource_usage_report(
        self,
        partner_id: str,
        *,
        reseller_id: Optional[str] = None,
        customer_id: Optional[str] = None,
        children: Optional[bool] = None,
        month: Optional[str] = None,
        viewpoint: Optional[str] = None,
        recurse: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get partner resource usage report.

        Returns the summary for the partner for a given month. Partner billing managers
        are authorized to access this report.

        :param str partner_id: Enterprise ID of the distributor or reseller for
               which the report is requested.
        :param str reseller_id: (optional) Enterprise ID of the reseller for which
               the report is requested. This parameter cannot be used along with
               `customer_id` query parameter.
        :param str customer_id: (optional) Account ID/Enterprise ID of the end
               customer for which the report is requested. This parameter cannot be used
               along with `reseller_id` query parameter.
        :param bool children: (optional) Get report rolled-up to the direct
               children of the requested entity. Defaults to false. This parameter cannot
               be used along with `customer_id` query parameter.
        :param str month: (optional) The billing month for which the usage report
               is requested. Format is `yyyy-mm`. Defaults to current month.
        :param str viewpoint: (optional) Enables partner to view the cost of
               provisioned services as applicable at the given level. Defaults to the type
               of the calling partner. The valid values are `DISTRIBUTOR`, `RESELLER` and
               `END_CUSTOMER`.
        :param bool recurse: (optional) Get usage report rolled-up to the end
               customers of the requesting partner. Defaults to false. This parameter
               cannot be used along with `reseller_id` query parameter or `customer_id`
               query parameter.
        :param int limit: (optional) Number of usage records to be returned. The
               default value is 30. Maximum value is 100.
        :param str offset: (optional) An opaque value representing the offset of
               the first item to be returned by a search query. If not specified, then the
               first page of results is returned. To retrieve the next page of search
               results, use the 'offset' query parameter value within the 'next.href' URL
               found within a prior search query response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PartnerUsageReportSummary` object
        """

        if not partner_id:
            raise ValueError('partner_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_resource_usage_report',
        )
        headers.update(sdk_headers)

        params = {
            'partner_id': partner_id,
            'reseller_id': reseller_id,
            'customer_id': customer_id,
            'children': children,
            'month': month,
            'viewpoint': viewpoint,
            'recurse': recurse,
            'limit': limit,
            'offset': offset,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/resource-usage-reports'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Billing Options
    #########################

    def get_billing_options(
        self,
        partner_id: str,
        *,
        customer_id: Optional[str] = None,
        reseller_id: Optional[str] = None,
        date: Optional[str] = None,
        limit: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get customers billing options.

        Returns the billing options for the requested customer for a given month.

        :param str partner_id: Enterprise ID of the distributor or reseller for
               which the report is requested.
        :param str customer_id: (optional) Account ID/Enterprise ID of the end
               customer for which the report is requested. This parameter cannot be used
               along with `reseller_id` query parameter.
        :param str reseller_id: (optional) Enterprise ID of the reseller for which
               the report is requested. This parameter cannot be used along with
               `customer_id` query parameter.
        :param str date: (optional) The billing month for which the report is
               requested. Format is yyyy-mm. Defaults to current month.
        :param int limit: (optional) Number of billing option reports returned. The
               default value is 200. Maximum value is 200.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BillingOptionsSummary` object
        """

        if not partner_id:
            raise ValueError('partner_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_billing_options',
        )
        headers.update(sdk_headers)

        params = {
            'partner_id': partner_id,
            'customer_id': customer_id,
            'reseller_id': reseller_id,
            'date': date,
            'limit': limit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/billing-options'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Credit Pools
    #########################

    def get_credit_pools_report(
        self,
        partner_id: str,
        *,
        customer_id: Optional[str] = None,
        reseller_id: Optional[str] = None,
        date: Optional[str] = None,
        limit: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get credit pools report.

        Returns the subscription or commitment burn-down reports for the end customers for
        a given month.

        :param str partner_id: Enterprise ID of the distributor or reseller for
               which the report is requested.
        :param str customer_id: (optional) Account ID/Enterprise ID of the end
               customer for which the report is requested. This parameter cannot be used
               along with `reseller_id` query parameter.
        :param str reseller_id: (optional) Enterprise ID of the reseller for which
               the report is requested. This parameter cannot be used along with
               `customer_id` query parameter.
        :param str date: (optional) The billing month for which the report is
               requested. Format is yyyy-mm. Defaults to current month.
        :param int limit: (optional) Number of billing units fetched to get the
               credit pools report. The default value is 30. Maximum value is 30.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreditPoolsReportSummary` object
        """

        if not partner_id:
            raise ValueError('partner_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_credit_pools_report',
        )
        headers.update(sdk_headers)

        params = {
            'partner_id': partner_id,
            'customer_id': customer_id,
            'reseller_id': reseller_id,
            'date': date,
            'limit': limit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/credit-pools'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response


class GetResourceUsageReportEnums:
    """
    Enums for get_resource_usage_report parameters.
    """

    class Viewpoint(str, Enum):
        """
        Enables partner to view the cost of provisioned services as applicable at the
        given level. Defaults to the type of the calling partner. The valid values are
        `DISTRIBUTOR`, `RESELLER` and `END_CUSTOMER`.
        """

        DISTRIBUTOR = 'DISTRIBUTOR'
        RESELLER = 'RESELLER'
        END_CUSTOMER = 'END_CUSTOMER'


##############################################################################
# Models
##############################################################################


class BillingOption:
    """
    Billing options report for the end customers.

    :param str id: (optional) The ID of the billing option.
    :param str billing_unit_id: (optional) The ID of the billing unit that's
          associated with the billing option.
    :param str customer_id: (optional) Account ID of the customer.
    :param str customer_type: (optional) The customer type. The valid values are
          `ENTERPRISE`, `ACCOUNT`, and `ACCOUNT_GROUP`.
    :param str customer_name: (optional) A user-defined name for the customer.
    :param str reseller_id: (optional) ID of the reseller in the heirarchy of the
          requested customer.
    :param str reseller_name: (optional) Name of the reseller in the heirarchy of
          the requested customer.
    :param str month: (optional) The billing month for which the burn-down report is
          requested. Format is yyyy-mm. Defaults to current month.
    :param List[dict] errors: (optional) Errors in the billing.
    :param str type: (optional) The type of billing option. The valid values are
          `SUBSCRIPTION` and `OFFER`.
    :param datetime start_date: (optional) The start date of billing option.
    :param datetime end_date: (optional) The end date of billing option.
    :param str state: (optional) The state of the billing option. The valid values
          include `ACTIVE, `SUSPENDED`, and `CANCELED`.
    :param str category: (optional) The category of the billing option. The valid
          values are `PLATFORM`, `SERVICE`, and `SUPPORT`.
    :param dict payment_instrument: (optional) The payment method for support.
    :param str part_number: (optional) Part number of the offering.
    :param str catalog_id: (optional) ID of the catalog containing this offering.
    :param str order_id: (optional) ID of the order containing this offering.
    :param str po_number: (optional) PO Number of the offering.
    :param str subscription_model: (optional) Subscription model.
    :param int duration_in_months: (optional) The duration of the billing options in
          months.
    :param float monthly_amount: (optional) Amount billed monthly for this offering.
    :param dict billing_system: (optional) The support billing system.
    :param str country_code: (optional) The country code for the billing unit.
    :param str currency_code: (optional) The currency code of the billing unit.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        billing_unit_id: Optional[str] = None,
        customer_id: Optional[str] = None,
        customer_type: Optional[str] = None,
        customer_name: Optional[str] = None,
        reseller_id: Optional[str] = None,
        reseller_name: Optional[str] = None,
        month: Optional[str] = None,
        errors: Optional[List[dict]] = None,
        type: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        state: Optional[str] = None,
        category: Optional[str] = None,
        payment_instrument: Optional[dict] = None,
        part_number: Optional[str] = None,
        catalog_id: Optional[str] = None,
        order_id: Optional[str] = None,
        po_number: Optional[str] = None,
        subscription_model: Optional[str] = None,
        duration_in_months: Optional[int] = None,
        monthly_amount: Optional[float] = None,
        billing_system: Optional[dict] = None,
        country_code: Optional[str] = None,
        currency_code: Optional[str] = None,
    ) -> None:
        """
        Initialize a BillingOption object.

        :param str id: (optional) The ID of the billing option.
        :param str billing_unit_id: (optional) The ID of the billing unit that's
               associated with the billing option.
        :param str customer_id: (optional) Account ID of the customer.
        :param str customer_type: (optional) The customer type. The valid values
               are `ENTERPRISE`, `ACCOUNT`, and `ACCOUNT_GROUP`.
        :param str customer_name: (optional) A user-defined name for the customer.
        :param str reseller_id: (optional) ID of the reseller in the heirarchy of
               the requested customer.
        :param str reseller_name: (optional) Name of the reseller in the heirarchy
               of the requested customer.
        :param str month: (optional) The billing month for which the burn-down
               report is requested. Format is yyyy-mm. Defaults to current month.
        :param List[dict] errors: (optional) Errors in the billing.
        :param str type: (optional) The type of billing option. The valid values
               are `SUBSCRIPTION` and `OFFER`.
        :param datetime start_date: (optional) The start date of billing option.
        :param datetime end_date: (optional) The end date of billing option.
        :param str state: (optional) The state of the billing option. The valid
               values include `ACTIVE, `SUSPENDED`, and `CANCELED`.
        :param str category: (optional) The category of the billing option. The
               valid values are `PLATFORM`, `SERVICE`, and `SUPPORT`.
        :param dict payment_instrument: (optional) The payment method for support.
        :param str part_number: (optional) Part number of the offering.
        :param str catalog_id: (optional) ID of the catalog containing this
               offering.
        :param str order_id: (optional) ID of the order containing this offering.
        :param str po_number: (optional) PO Number of the offering.
        :param str subscription_model: (optional) Subscription model.
        :param int duration_in_months: (optional) The duration of the billing
               options in months.
        :param float monthly_amount: (optional) Amount billed monthly for this
               offering.
        :param dict billing_system: (optional) The support billing system.
        :param str country_code: (optional) The country code for the billing unit.
        :param str currency_code: (optional) The currency code of the billing unit.
        """
        self.id = id
        self.billing_unit_id = billing_unit_id
        self.customer_id = customer_id
        self.customer_type = customer_type
        self.customer_name = customer_name
        self.reseller_id = reseller_id
        self.reseller_name = reseller_name
        self.month = month
        self.errors = errors
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.state = state
        self.category = category
        self.payment_instrument = payment_instrument
        self.part_number = part_number
        self.catalog_id = catalog_id
        self.order_id = order_id
        self.po_number = po_number
        self.subscription_model = subscription_model
        self.duration_in_months = duration_in_months
        self.monthly_amount = monthly_amount
        self.billing_system = billing_system
        self.country_code = country_code
        self.currency_code = currency_code

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BillingOption':
        """Initialize a BillingOption object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (billing_unit_id := _dict.get('billing_unit_id')) is not None:
            args['billing_unit_id'] = billing_unit_id
        if (customer_id := _dict.get('customer_id')) is not None:
            args['customer_id'] = customer_id
        if (customer_type := _dict.get('customer_type')) is not None:
            args['customer_type'] = customer_type
        if (customer_name := _dict.get('customer_name')) is not None:
            args['customer_name'] = customer_name
        if (reseller_id := _dict.get('reseller_id')) is not None:
            args['reseller_id'] = reseller_id
        if (reseller_name := _dict.get('reseller_name')) is not None:
            args['reseller_name'] = reseller_name
        if (month := _dict.get('month')) is not None:
            args['month'] = month
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (start_date := _dict.get('start_date')) is not None:
            args['start_date'] = string_to_datetime(start_date)
        if (end_date := _dict.get('end_date')) is not None:
            args['end_date'] = string_to_datetime(end_date)
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        if (category := _dict.get('category')) is not None:
            args['category'] = category
        if (payment_instrument := _dict.get('payment_instrument')) is not None:
            args['payment_instrument'] = payment_instrument
        if (part_number := _dict.get('part_number')) is not None:
            args['part_number'] = part_number
        if (catalog_id := _dict.get('catalog_id')) is not None:
            args['catalog_id'] = catalog_id
        if (order_id := _dict.get('order_id')) is not None:
            args['order_id'] = order_id
        if (po_number := _dict.get('po_number')) is not None:
            args['po_number'] = po_number
        if (subscription_model := _dict.get('subscription_model')) is not None:
            args['subscription_model'] = subscription_model
        if (duration_in_months := _dict.get('duration_in_months')) is not None:
            args['duration_in_months'] = duration_in_months
        if (monthly_amount := _dict.get('monthly_amount')) is not None:
            args['monthly_amount'] = monthly_amount
        if (billing_system := _dict.get('billing_system')) is not None:
            args['billing_system'] = billing_system
        if (country_code := _dict.get('country_code')) is not None:
            args['country_code'] = country_code
        if (currency_code := _dict.get('currency_code')) is not None:
            args['currency_code'] = currency_code
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BillingOption object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'billing_unit_id') and self.billing_unit_id is not None:
            _dict['billing_unit_id'] = self.billing_unit_id
        if hasattr(self, 'customer_id') and self.customer_id is not None:
            _dict['customer_id'] = self.customer_id
        if hasattr(self, 'customer_type') and self.customer_type is not None:
            _dict['customer_type'] = self.customer_type
        if hasattr(self, 'customer_name') and self.customer_name is not None:
            _dict['customer_name'] = self.customer_name
        if hasattr(self, 'reseller_id') and self.reseller_id is not None:
            _dict['reseller_id'] = self.reseller_id
        if hasattr(self, 'reseller_name') and self.reseller_name is not None:
            _dict['reseller_name'] = self.reseller_name
        if hasattr(self, 'month') and self.month is not None:
            _dict['month'] = self.month
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'start_date') and self.start_date is not None:
            _dict['start_date'] = datetime_to_string(self.start_date)
        if hasattr(self, 'end_date') and self.end_date is not None:
            _dict['end_date'] = datetime_to_string(self.end_date)
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'category') and self.category is not None:
            _dict['category'] = self.category
        if hasattr(self, 'payment_instrument') and self.payment_instrument is not None:
            _dict['payment_instrument'] = self.payment_instrument
        if hasattr(self, 'part_number') and self.part_number is not None:
            _dict['part_number'] = self.part_number
        if hasattr(self, 'catalog_id') and self.catalog_id is not None:
            _dict['catalog_id'] = self.catalog_id
        if hasattr(self, 'order_id') and self.order_id is not None:
            _dict['order_id'] = self.order_id
        if hasattr(self, 'po_number') and self.po_number is not None:
            _dict['po_number'] = self.po_number
        if hasattr(self, 'subscription_model') and self.subscription_model is not None:
            _dict['subscription_model'] = self.subscription_model
        if hasattr(self, 'duration_in_months') and self.duration_in_months is not None:
            _dict['duration_in_months'] = self.duration_in_months
        if hasattr(self, 'monthly_amount') and self.monthly_amount is not None:
            _dict['monthly_amount'] = self.monthly_amount
        if hasattr(self, 'billing_system') and self.billing_system is not None:
            _dict['billing_system'] = self.billing_system
        if hasattr(self, 'country_code') and self.country_code is not None:
            _dict['country_code'] = self.country_code
        if hasattr(self, 'currency_code') and self.currency_code is not None:
            _dict['currency_code'] = self.currency_code
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BillingOption object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BillingOption') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BillingOption') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CustomerTypeEnum(str, Enum):
        """
        The customer type. The valid values are `ENTERPRISE`, `ACCOUNT`, and
        `ACCOUNT_GROUP`.
        """

        ENTERPRISE = 'ENTERPRISE'
        ACCOUNT = 'ACCOUNT'
        ACCOUNT_GROUP = 'ACCOUNT_GROUP'

    class TypeEnum(str, Enum):
        """
        The type of billing option. The valid values are `SUBSCRIPTION` and `OFFER`.
        """

        SUBSCRIPTION = 'SUBSCRIPTION'
        OFFER = 'OFFER'

    class StateEnum(str, Enum):
        """
        The state of the billing option. The valid values include `ACTIVE, `SUSPENDED`,
        and `CANCELED`.
        """

        ACTIVE = 'ACTIVE'
        SUSPENDED = 'SUSPENDED'
        CANCELED = 'CANCELED'

    class CategoryEnum(str, Enum):
        """
        The category of the billing option. The valid values are `PLATFORM`, `SERVICE`,
        and `SUPPORT`.
        """

        PLATFORM = 'PLATFORM'
        SERVICE = 'SERVICE'
        SUPPORT = 'SUPPORT'


class BillingOptionsSummary:
    """
    The billing options report for the customer.

    :param int rows_count: (optional) The max number of reports in the response.
    :param str next_url: (optional) The link to the next page of the search query.
    :param List[BillingOption] resources: (optional) Aggregated usage report of all
          requested partners.
    """

    def __init__(
        self,
        *,
        rows_count: Optional[int] = None,
        next_url: Optional[str] = None,
        resources: Optional[List['BillingOption']] = None,
    ) -> None:
        """
        Initialize a BillingOptionsSummary object.

        :param int rows_count: (optional) The max number of reports in the
               response.
        :param str next_url: (optional) The link to the next page of the search
               query.
        :param List[BillingOption] resources: (optional) Aggregated usage report of
               all requested partners.
        """
        self.rows_count = rows_count
        self.next_url = next_url
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BillingOptionsSummary':
        """Initialize a BillingOptionsSummary object from a json dictionary."""
        args = {}
        if (rows_count := _dict.get('rows_count')) is not None:
            args['rows_count'] = rows_count
        if (next_url := _dict.get('next_url')) is not None:
            args['next_url'] = next_url
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [BillingOption.from_dict(v) for v in resources]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BillingOptionsSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rows_count') and self.rows_count is not None:
            _dict['rows_count'] = self.rows_count
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
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
        """Return a `str` version of this BillingOptionsSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BillingOptionsSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BillingOptionsSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreditPoolsReport:
    """
    Aggregated subscription burn-down report for the end customers.

    :param str type: (optional) The category of the billing option. The valid values
          are `PLATFORM`, `SERVICE` and `SUPPORT`.
    :param str billing_unit_id: (optional) The ID of the billing unit that's
          associated with the billing option.
    :param str customer_id: (optional) Account ID of the customer.
    :param str customer_type: (optional) The customer type. The valid values are
          `ENTERPRISE`, `ACCOUNT`, and `ACCOUNT_GROUP`.
    :param str customer_name: (optional) A user-defined name for the customer.
    :param str reseller_id: (optional) ID of the reseller in the heirarchy of the
          requested customer.
    :param str reseller_name: (optional) Name of the reseller in the heirarchy of
          the requested customer.
    :param str month: (optional) The billing month for which the burn-down report is
          requested. Format is yyyy-mm. Defaults to current month.
    :param str currency_code: (optional) The currency code of the billing unit.
    :param List[TermCredits] term_credits: (optional) A list of active subscription
          terms available within a credit.
    :param Overage overage: (optional) Overage that was generated on the credit
          pool.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        billing_unit_id: Optional[str] = None,
        customer_id: Optional[str] = None,
        customer_type: Optional[str] = None,
        customer_name: Optional[str] = None,
        reseller_id: Optional[str] = None,
        reseller_name: Optional[str] = None,
        month: Optional[str] = None,
        currency_code: Optional[str] = None,
        term_credits: Optional[List['TermCredits']] = None,
        overage: Optional['Overage'] = None,
    ) -> None:
        """
        Initialize a CreditPoolsReport object.

        :param str type: (optional) The category of the billing option. The valid
               values are `PLATFORM`, `SERVICE` and `SUPPORT`.
        :param str billing_unit_id: (optional) The ID of the billing unit that's
               associated with the billing option.
        :param str customer_id: (optional) Account ID of the customer.
        :param str customer_type: (optional) The customer type. The valid values
               are `ENTERPRISE`, `ACCOUNT`, and `ACCOUNT_GROUP`.
        :param str customer_name: (optional) A user-defined name for the customer.
        :param str reseller_id: (optional) ID of the reseller in the heirarchy of
               the requested customer.
        :param str reseller_name: (optional) Name of the reseller in the heirarchy
               of the requested customer.
        :param str month: (optional) The billing month for which the burn-down
               report is requested. Format is yyyy-mm. Defaults to current month.
        :param str currency_code: (optional) The currency code of the billing unit.
        :param List[TermCredits] term_credits: (optional) A list of active
               subscription terms available within a credit.
        :param Overage overage: (optional) Overage that was generated on the credit
               pool.
        """
        self.type = type
        self.billing_unit_id = billing_unit_id
        self.customer_id = customer_id
        self.customer_type = customer_type
        self.customer_name = customer_name
        self.reseller_id = reseller_id
        self.reseller_name = reseller_name
        self.month = month
        self.currency_code = currency_code
        self.term_credits = term_credits
        self.overage = overage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreditPoolsReport':
        """Initialize a CreditPoolsReport object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (billing_unit_id := _dict.get('billing_unit_id')) is not None:
            args['billing_unit_id'] = billing_unit_id
        if (customer_id := _dict.get('customer_id')) is not None:
            args['customer_id'] = customer_id
        if (customer_type := _dict.get('customer_type')) is not None:
            args['customer_type'] = customer_type
        if (customer_name := _dict.get('customer_name')) is not None:
            args['customer_name'] = customer_name
        if (reseller_id := _dict.get('reseller_id')) is not None:
            args['reseller_id'] = reseller_id
        if (reseller_name := _dict.get('reseller_name')) is not None:
            args['reseller_name'] = reseller_name
        if (month := _dict.get('month')) is not None:
            args['month'] = month
        if (currency_code := _dict.get('currency_code')) is not None:
            args['currency_code'] = currency_code
        if (term_credits := _dict.get('term_credits')) is not None:
            args['term_credits'] = [TermCredits.from_dict(v) for v in term_credits]
        if (overage := _dict.get('overage')) is not None:
            args['overage'] = Overage.from_dict(overage)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreditPoolsReport object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'billing_unit_id') and self.billing_unit_id is not None:
            _dict['billing_unit_id'] = self.billing_unit_id
        if hasattr(self, 'customer_id') and self.customer_id is not None:
            _dict['customer_id'] = self.customer_id
        if hasattr(self, 'customer_type') and self.customer_type is not None:
            _dict['customer_type'] = self.customer_type
        if hasattr(self, 'customer_name') and self.customer_name is not None:
            _dict['customer_name'] = self.customer_name
        if hasattr(self, 'reseller_id') and self.reseller_id is not None:
            _dict['reseller_id'] = self.reseller_id
        if hasattr(self, 'reseller_name') and self.reseller_name is not None:
            _dict['reseller_name'] = self.reseller_name
        if hasattr(self, 'month') and self.month is not None:
            _dict['month'] = self.month
        if hasattr(self, 'currency_code') and self.currency_code is not None:
            _dict['currency_code'] = self.currency_code
        if hasattr(self, 'term_credits') and self.term_credits is not None:
            term_credits_list = []
            for v in self.term_credits:
                if isinstance(v, dict):
                    term_credits_list.append(v)
                else:
                    term_credits_list.append(v.to_dict())
            _dict['term_credits'] = term_credits_list
        if hasattr(self, 'overage') and self.overage is not None:
            if isinstance(self.overage, dict):
                _dict['overage'] = self.overage
            else:
                _dict['overage'] = self.overage.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreditPoolsReport object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreditPoolsReport') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreditPoolsReport') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The category of the billing option. The valid values are `PLATFORM`, `SERVICE` and
        `SUPPORT`.
        """

        PLATFORM = 'PLATFORM'
        SERVICE = 'SERVICE'
        SUPPORT = 'SUPPORT'

    class CustomerTypeEnum(str, Enum):
        """
        The customer type. The valid values are `ENTERPRISE`, `ACCOUNT`, and
        `ACCOUNT_GROUP`.
        """

        ENTERPRISE = 'ENTERPRISE'
        ACCOUNT = 'ACCOUNT'
        ACCOUNT_GROUP = 'ACCOUNT_GROUP'


class CreditPoolsReportSummary:
    """
    The aggregated credit pools report.

    :param int rows_count: (optional) The max number of reports in the response.
    :param str next_url: (optional) The link to the next page of the search query.
    :param List[CreditPoolsReport] resources: (optional) Aggregated usage report of
          all requested partners.
    """

    def __init__(
        self,
        *,
        rows_count: Optional[int] = None,
        next_url: Optional[str] = None,
        resources: Optional[List['CreditPoolsReport']] = None,
    ) -> None:
        """
        Initialize a CreditPoolsReportSummary object.

        :param int rows_count: (optional) The max number of reports in the
               response.
        :param str next_url: (optional) The link to the next page of the search
               query.
        :param List[CreditPoolsReport] resources: (optional) Aggregated usage
               report of all requested partners.
        """
        self.rows_count = rows_count
        self.next_url = next_url
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreditPoolsReportSummary':
        """Initialize a CreditPoolsReportSummary object from a json dictionary."""
        args = {}
        if (rows_count := _dict.get('rows_count')) is not None:
            args['rows_count'] = rows_count
        if (next_url := _dict.get('next_url')) is not None:
            args['next_url'] = next_url
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [CreditPoolsReport.from_dict(v) for v in resources]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreditPoolsReportSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rows_count') and self.rows_count is not None:
            _dict['rows_count'] = self.rows_count
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
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
        """Return a `str` version of this CreditPoolsReportSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreditPoolsReportSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreditPoolsReportSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetricUsage:
    """
    An object that represents a metric.

    :param str metric: The name of the metric.
    :param str unit: A unit to qualify the quantity.
    :param float quantity: The aggregated value for the metric.
    :param float rateable_quantity: The quantity that is used for calculating
          charges.
    :param float cost: The cost that was incurred by the metric.
    :param float rated_cost: The pre-discounted cost that was incurred by the
          metric.
    :param List[dict] price: (optional) The price with which cost was calculated.
    """

    def __init__(
        self,
        metric: str,
        unit: str,
        quantity: float,
        rateable_quantity: float,
        cost: float,
        rated_cost: float,
        *,
        price: Optional[List[dict]] = None,
    ) -> None:
        """
        Initialize a MetricUsage object.

        :param str metric: The name of the metric.
        :param str unit: A unit to qualify the quantity.
        :param float quantity: The aggregated value for the metric.
        :param float rateable_quantity: The quantity that is used for calculating
               charges.
        :param float cost: The cost that was incurred by the metric.
        :param float rated_cost: The pre-discounted cost that was incurred by the
               metric.
        :param List[dict] price: (optional) The price with which cost was
               calculated.
        """
        self.metric = metric
        self.unit = unit
        self.quantity = quantity
        self.rateable_quantity = rateable_quantity
        self.cost = cost
        self.rated_cost = rated_cost
        self.price = price

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetricUsage':
        """Initialize a MetricUsage object from a json dictionary."""
        args = {}
        if (metric := _dict.get('metric')) is not None:
            args['metric'] = metric
        else:
            raise ValueError('Required property \'metric\' not present in MetricUsage JSON')
        if (unit := _dict.get('unit')) is not None:
            args['unit'] = unit
        else:
            raise ValueError('Required property \'unit\' not present in MetricUsage JSON')
        if (quantity := _dict.get('quantity')) is not None:
            args['quantity'] = quantity
        else:
            raise ValueError('Required property \'quantity\' not present in MetricUsage JSON')
        if (rateable_quantity := _dict.get('rateable_quantity')) is not None:
            args['rateable_quantity'] = rateable_quantity
        else:
            raise ValueError('Required property \'rateable_quantity\' not present in MetricUsage JSON')
        if (cost := _dict.get('cost')) is not None:
            args['cost'] = cost
        else:
            raise ValueError('Required property \'cost\' not present in MetricUsage JSON')
        if (rated_cost := _dict.get('rated_cost')) is not None:
            args['rated_cost'] = rated_cost
        else:
            raise ValueError('Required property \'rated_cost\' not present in MetricUsage JSON')
        if (price := _dict.get('price')) is not None:
            args['price'] = price
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'metric') and self.metric is not None:
            _dict['metric'] = self.metric
        if hasattr(self, 'unit') and self.unit is not None:
            _dict['unit'] = self.unit
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetricUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MetricUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetricUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Overage:
    """
    Overage that was generated on the credit pool.

    :param float cost: (optional) The number of credits used as overage.
    :param List[dict] resources: (optional) A list of resources that generated
          overage.
    """

    def __init__(
        self,
        *,
        cost: Optional[float] = None,
        resources: Optional[List[dict]] = None,
    ) -> None:
        """
        Initialize a Overage object.

        :param float cost: (optional) The number of credits used as overage.
        :param List[dict] resources: (optional) A list of resources that generated
               overage.
        """
        self.cost = cost
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Overage':
        """Initialize a Overage object from a json dictionary."""
        args = {}
        if (cost := _dict.get('cost')) is not None:
            args['cost'] = cost
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = resources
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Overage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cost') and self.cost is not None:
            _dict['cost'] = self.cost
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = self.resources
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Overage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Overage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Overage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PartnerUsageReportSummaryFirst:
    """
    The link to the first page of the search query.

    :param str href: (optional) A link to a page of query results.
    """

    def __init__(
        self,
        *,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a PartnerUsageReportSummaryFirst object.

        :param str href: (optional) A link to a page of query results.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartnerUsageReportSummaryFirst':
        """Initialize a PartnerUsageReportSummaryFirst object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartnerUsageReportSummaryFirst object from a json dictionary."""
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
        """Return a `str` version of this PartnerUsageReportSummaryFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartnerUsageReportSummaryFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartnerUsageReportSummaryFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PartnerUsageReportSummaryNext:
    """
    The link to the next page of the search query.

    :param str href: (optional) A link to a page of query results.
    :param str offset: (optional) The value of the `_start` query parameter to fetch
          the next page.
    """

    def __init__(
        self,
        *,
        href: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> None:
        """
        Initialize a PartnerUsageReportSummaryNext object.

        :param str href: (optional) A link to a page of query results.
        :param str offset: (optional) The value of the `_start` query parameter to
               fetch the next page.
        """
        self.href = href
        self.offset = offset

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartnerUsageReportSummaryNext':
        """Initialize a PartnerUsageReportSummaryNext object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (offset := _dict.get('offset')) is not None:
            args['offset'] = offset
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartnerUsageReportSummaryNext object from a json dictionary."""
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
        """Return a `str` version of this PartnerUsageReportSummaryNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartnerUsageReportSummaryNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartnerUsageReportSummaryNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PartnerUsageReport:
    """
    Aggregated usage report of a partner.

    :param str entity_id: (optional) The ID of the entity.
    :param str entity_type: (optional) The entity type.
    :param str entity_crn: (optional) The Cloud Resource Name (CRN) of the entity
          towards which the resource usages were rolled up.
    :param str entity_name: (optional) A user-defined name for the entity, such as
          the enterprise name or account name.
    :param str entity_partner_type: (optional) Role of the `entity_id` for which the
          usage report is fetched.
    :param str viewpoint: (optional) Enables partner to view the cost of provisioned
          services as applicable at the given level.
    :param str month: (optional) The billing month for which the usage report is
          requested. Format is yyyy-mm.
    :param str currency_code: (optional) The currency code of the billing unit.
    :param str country_code: (optional) The country code of the billing unit.
    :param float billable_cost: (optional) Billable charges that are aggregated from
          all entities in the report.
    :param float billable_rated_cost: (optional) Aggregated billable charges before
          discounts.
    :param float non_billable_cost: (optional) Non-billable charges that are
          aggregated from all entities in the report.
    :param float non_billable_rated_cost: (optional) Aggregated non-billable charges
          before discounts.
    :param List[ResourceUsage] resources: (optional)
    """

    def __init__(
        self,
        *,
        entity_id: Optional[str] = None,
        entity_type: Optional[str] = None,
        entity_crn: Optional[str] = None,
        entity_name: Optional[str] = None,
        entity_partner_type: Optional[str] = None,
        viewpoint: Optional[str] = None,
        month: Optional[str] = None,
        currency_code: Optional[str] = None,
        country_code: Optional[str] = None,
        billable_cost: Optional[float] = None,
        billable_rated_cost: Optional[float] = None,
        non_billable_cost: Optional[float] = None,
        non_billable_rated_cost: Optional[float] = None,
        resources: Optional[List['ResourceUsage']] = None,
    ) -> None:
        """
        Initialize a PartnerUsageReport object.

        :param str entity_id: (optional) The ID of the entity.
        :param str entity_type: (optional) The entity type.
        :param str entity_crn: (optional) The Cloud Resource Name (CRN) of the
               entity towards which the resource usages were rolled up.
        :param str entity_name: (optional) A user-defined name for the entity, such
               as the enterprise name or account name.
        :param str entity_partner_type: (optional) Role of the `entity_id` for
               which the usage report is fetched.
        :param str viewpoint: (optional) Enables partner to view the cost of
               provisioned services as applicable at the given level.
        :param str month: (optional) The billing month for which the usage report
               is requested. Format is yyyy-mm.
        :param str currency_code: (optional) The currency code of the billing unit.
        :param str country_code: (optional) The country code of the billing unit.
        :param float billable_cost: (optional) Billable charges that are aggregated
               from all entities in the report.
        :param float billable_rated_cost: (optional) Aggregated billable charges
               before discounts.
        :param float non_billable_cost: (optional) Non-billable charges that are
               aggregated from all entities in the report.
        :param float non_billable_rated_cost: (optional) Aggregated non-billable
               charges before discounts.
        :param List[ResourceUsage] resources: (optional)
        """
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.entity_crn = entity_crn
        self.entity_name = entity_name
        self.entity_partner_type = entity_partner_type
        self.viewpoint = viewpoint
        self.month = month
        self.currency_code = currency_code
        self.country_code = country_code
        self.billable_cost = billable_cost
        self.billable_rated_cost = billable_rated_cost
        self.non_billable_cost = non_billable_cost
        self.non_billable_rated_cost = non_billable_rated_cost
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartnerUsageReport':
        """Initialize a PartnerUsageReport object from a json dictionary."""
        args = {}
        if (entity_id := _dict.get('entity_id')) is not None:
            args['entity_id'] = entity_id
        if (entity_type := _dict.get('entity_type')) is not None:
            args['entity_type'] = entity_type
        if (entity_crn := _dict.get('entity_crn')) is not None:
            args['entity_crn'] = entity_crn
        if (entity_name := _dict.get('entity_name')) is not None:
            args['entity_name'] = entity_name
        if (entity_partner_type := _dict.get('entity_partner_type')) is not None:
            args['entity_partner_type'] = entity_partner_type
        if (viewpoint := _dict.get('viewpoint')) is not None:
            args['viewpoint'] = viewpoint
        if (month := _dict.get('month')) is not None:
            args['month'] = month
        if (currency_code := _dict.get('currency_code')) is not None:
            args['currency_code'] = currency_code
        if (country_code := _dict.get('country_code')) is not None:
            args['country_code'] = country_code
        if (billable_cost := _dict.get('billable_cost')) is not None:
            args['billable_cost'] = billable_cost
        if (billable_rated_cost := _dict.get('billable_rated_cost')) is not None:
            args['billable_rated_cost'] = billable_rated_cost
        if (non_billable_cost := _dict.get('non_billable_cost')) is not None:
            args['non_billable_cost'] = non_billable_cost
        if (non_billable_rated_cost := _dict.get('non_billable_rated_cost')) is not None:
            args['non_billable_rated_cost'] = non_billable_rated_cost
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [ResourceUsage.from_dict(v) for v in resources]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartnerUsageReport object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity_id') and self.entity_id is not None:
            _dict['entity_id'] = self.entity_id
        if hasattr(self, 'entity_type') and self.entity_type is not None:
            _dict['entity_type'] = self.entity_type
        if hasattr(self, 'entity_crn') and self.entity_crn is not None:
            _dict['entity_crn'] = self.entity_crn
        if hasattr(self, 'entity_name') and self.entity_name is not None:
            _dict['entity_name'] = self.entity_name
        if hasattr(self, 'entity_partner_type') and self.entity_partner_type is not None:
            _dict['entity_partner_type'] = self.entity_partner_type
        if hasattr(self, 'viewpoint') and self.viewpoint is not None:
            _dict['viewpoint'] = self.viewpoint
        if hasattr(self, 'month') and self.month is not None:
            _dict['month'] = self.month
        if hasattr(self, 'currency_code') and self.currency_code is not None:
            _dict['currency_code'] = self.currency_code
        if hasattr(self, 'country_code') and self.country_code is not None:
            _dict['country_code'] = self.country_code
        if hasattr(self, 'billable_cost') and self.billable_cost is not None:
            _dict['billable_cost'] = self.billable_cost
        if hasattr(self, 'billable_rated_cost') and self.billable_rated_cost is not None:
            _dict['billable_rated_cost'] = self.billable_rated_cost
        if hasattr(self, 'non_billable_cost') and self.non_billable_cost is not None:
            _dict['non_billable_cost'] = self.non_billable_cost
        if hasattr(self, 'non_billable_rated_cost') and self.non_billable_rated_cost is not None:
            _dict['non_billable_rated_cost'] = self.non_billable_rated_cost
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
        """Return a `str` version of this PartnerUsageReport object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartnerUsageReport') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartnerUsageReport') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PartnerUsageReportSummary:
    """
    The aggregated partner usage report.

    :param int limit: (optional) The maximum number of usage records in the
          response.
    :param PartnerUsageReportSummaryFirst first: (optional) The link to the first
          page of the search query.
    :param PartnerUsageReportSummaryNext next: (optional) The link to the next page
          of the search query.
    :param List[PartnerUsageReport] reports: (optional) Aggregated usage report of
          all requested partners.
    """

    def __init__(
        self,
        *,
        limit: Optional[int] = None,
        first: Optional['PartnerUsageReportSummaryFirst'] = None,
        next: Optional['PartnerUsageReportSummaryNext'] = None,
        reports: Optional[List['PartnerUsageReport']] = None,
    ) -> None:
        """
        Initialize a PartnerUsageReportSummary object.

        :param int limit: (optional) The maximum number of usage records in the
               response.
        :param PartnerUsageReportSummaryFirst first: (optional) The link to the
               first page of the search query.
        :param PartnerUsageReportSummaryNext next: (optional) The link to the next
               page of the search query.
        :param List[PartnerUsageReport] reports: (optional) Aggregated usage report
               of all requested partners.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.reports = reports

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartnerUsageReportSummary':
        """Initialize a PartnerUsageReportSummary object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (first := _dict.get('first')) is not None:
            args['first'] = PartnerUsageReportSummaryFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PartnerUsageReportSummaryNext.from_dict(next)
        if (reports := _dict.get('reports')) is not None:
            args['reports'] = [PartnerUsageReport.from_dict(v) for v in reports]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartnerUsageReportSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'reports') and self.reports is not None:
            reports_list = []
            for v in self.reports:
                if isinstance(v, dict):
                    reports_list.append(v)
                else:
                    reports_list.append(v.to_dict())
            _dict['reports'] = reports_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PartnerUsageReportSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartnerUsageReportSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartnerUsageReportSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PlanUsage:
    """
    Aggregated values for the plan.

    :param str plan_id: The ID of the plan.
    :param str pricing_region: (optional) The pricing region for the plan.
    :param str pricing_plan_id: (optional) The pricing plan with which the usage was
          rated.
    :param bool billable: Whether the plan charges are billed to the customer.
    :param float cost: The total cost that was incurred by the plan.
    :param float rated_cost: The total pre-discounted cost that was incurred by the
          plan.
    :param List[MetricUsage] usage: All of the metrics in the plan.
    """

    def __init__(
        self,
        plan_id: str,
        billable: bool,
        cost: float,
        rated_cost: float,
        usage: List['MetricUsage'],
        *,
        pricing_region: Optional[str] = None,
        pricing_plan_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a PlanUsage object.

        :param str plan_id: The ID of the plan.
        :param bool billable: Whether the plan charges are billed to the customer.
        :param float cost: The total cost that was incurred by the plan.
        :param float rated_cost: The total pre-discounted cost that was incurred by
               the plan.
        :param List[MetricUsage] usage: All of the metrics in the plan.
        :param str pricing_region: (optional) The pricing region for the plan.
        :param str pricing_plan_id: (optional) The pricing plan with which the
               usage was rated.
        """
        self.plan_id = plan_id
        self.pricing_region = pricing_region
        self.pricing_plan_id = pricing_plan_id
        self.billable = billable
        self.cost = cost
        self.rated_cost = rated_cost
        self.usage = usage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PlanUsage':
        """Initialize a PlanUsage object from a json dictionary."""
        args = {}
        if (plan_id := _dict.get('plan_id')) is not None:
            args['plan_id'] = plan_id
        else:
            raise ValueError('Required property \'plan_id\' not present in PlanUsage JSON')
        if (pricing_region := _dict.get('pricing_region')) is not None:
            args['pricing_region'] = pricing_region
        if (pricing_plan_id := _dict.get('pricing_plan_id')) is not None:
            args['pricing_plan_id'] = pricing_plan_id
        if (billable := _dict.get('billable')) is not None:
            args['billable'] = billable
        else:
            raise ValueError('Required property \'billable\' not present in PlanUsage JSON')
        if (cost := _dict.get('cost')) is not None:
            args['cost'] = cost
        else:
            raise ValueError('Required property \'cost\' not present in PlanUsage JSON')
        if (rated_cost := _dict.get('rated_cost')) is not None:
            args['rated_cost'] = rated_cost
        else:
            raise ValueError('Required property \'rated_cost\' not present in PlanUsage JSON')
        if (usage := _dict.get('usage')) is not None:
            args['usage'] = [MetricUsage.from_dict(v) for v in usage]
        else:
            raise ValueError('Required property \'usage\' not present in PlanUsage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PlanUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'plan_id') and self.plan_id is not None:
            _dict['plan_id'] = self.plan_id
        if hasattr(self, 'pricing_region') and self.pricing_region is not None:
            _dict['pricing_region'] = self.pricing_region
        if hasattr(self, 'pricing_plan_id') and self.pricing_plan_id is not None:
            _dict['pricing_plan_id'] = self.pricing_plan_id
        if hasattr(self, 'billable') and self.billable is not None:
            _dict['billable'] = self.billable
        if hasattr(self, 'cost') and self.cost is not None:
            _dict['cost'] = self.cost
        if hasattr(self, 'rated_cost') and self.rated_cost is not None:
            _dict['rated_cost'] = self.rated_cost
        if hasattr(self, 'usage') and self.usage is not None:
            usage_list = []
            for v in self.usage:
                if isinstance(v, dict):
                    usage_list.append(v)
                else:
                    usage_list.append(v.to_dict())
            _dict['usage'] = usage_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PlanUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PlanUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PlanUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceUsage:
    """
    A container for all the plans in the resource.

    :param str resource_id: The ID of the resource.
    :param str resource_name: (optional) The name of the resource.
    :param float billable_cost: The billable charges for the partner.
    :param float billable_rated_cost: The pre-discounted billable charges for the
          partner.
    :param float non_billable_cost: The non-billable charges for the partner.
    :param float non_billable_rated_cost: The pre-discounted, non-billable charges
          for the partner.
    :param List[PlanUsage] plans: All of the plans in the resource.
    """

    def __init__(
        self,
        resource_id: str,
        billable_cost: float,
        billable_rated_cost: float,
        non_billable_cost: float,
        non_billable_rated_cost: float,
        plans: List['PlanUsage'],
        *,
        resource_name: Optional[str] = None,
    ) -> None:
        """
        Initialize a ResourceUsage object.

        :param str resource_id: The ID of the resource.
        :param float billable_cost: The billable charges for the partner.
        :param float billable_rated_cost: The pre-discounted billable charges for
               the partner.
        :param float non_billable_cost: The non-billable charges for the partner.
        :param float non_billable_rated_cost: The pre-discounted, non-billable
               charges for the partner.
        :param List[PlanUsage] plans: All of the plans in the resource.
        :param str resource_name: (optional) The name of the resource.
        """
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.billable_cost = billable_cost
        self.billable_rated_cost = billable_rated_cost
        self.non_billable_cost = non_billable_cost
        self.non_billable_rated_cost = non_billable_rated_cost
        self.plans = plans

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceUsage':
        """Initialize a ResourceUsage object from a json dictionary."""
        args = {}
        if (resource_id := _dict.get('resource_id')) is not None:
            args['resource_id'] = resource_id
        else:
            raise ValueError('Required property \'resource_id\' not present in ResourceUsage JSON')
        if (resource_name := _dict.get('resource_name')) is not None:
            args['resource_name'] = resource_name
        if (billable_cost := _dict.get('billable_cost')) is not None:
            args['billable_cost'] = billable_cost
        else:
            raise ValueError('Required property \'billable_cost\' not present in ResourceUsage JSON')
        if (billable_rated_cost := _dict.get('billable_rated_cost')) is not None:
            args['billable_rated_cost'] = billable_rated_cost
        else:
            raise ValueError('Required property \'billable_rated_cost\' not present in ResourceUsage JSON')
        if (non_billable_cost := _dict.get('non_billable_cost')) is not None:
            args['non_billable_cost'] = non_billable_cost
        else:
            raise ValueError('Required property \'non_billable_cost\' not present in ResourceUsage JSON')
        if (non_billable_rated_cost := _dict.get('non_billable_rated_cost')) is not None:
            args['non_billable_rated_cost'] = non_billable_rated_cost
        else:
            raise ValueError('Required property \'non_billable_rated_cost\' not present in ResourceUsage JSON')
        if (plans := _dict.get('plans')) is not None:
            args['plans'] = [PlanUsage.from_dict(v) for v in plans]
        else:
            raise ValueError('Required property \'plans\' not present in ResourceUsage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceUsage object from a json dictionary."""
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
            plans_list = []
            for v in self.plans:
                if isinstance(v, dict):
                    plans_list.append(v)
                else:
                    plans_list.append(v.to_dict())
            _dict['plans'] = plans_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TermCredits:
    """
    The subscription term that is active in the requested month.

    :param str billing_option_id: (optional) The ID of the billing option from which
          the subscription term is derived.
    :param str billing_option_model: (optional) Billing option model.
    :param str category: (optional) The category of the billing option. The valid
          values are `PLATFORM`, `SERVICE`, and `SUPPORT`.
    :param datetime start_date: (optional) The start date of the term in ISO format.
    :param datetime end_date: (optional) The end date of the term in ISO format.
    :param float total_credits: (optional) The total credit available in this term.
    :param float starting_balance: (optional) The balance of available credit at the
          start of the current month.
    :param float used_credits: (optional) The amount of credit used during the
          current month.
    :param float current_balance: (optional) The balance of remaining credit in the
          subscription term.
    :param List[dict] resources: (optional) A list of resources that used credit
          during the month.
    """

    def __init__(
        self,
        *,
        billing_option_id: Optional[str] = None,
        billing_option_model: Optional[str] = None,
        category: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        total_credits: Optional[float] = None,
        starting_balance: Optional[float] = None,
        used_credits: Optional[float] = None,
        current_balance: Optional[float] = None,
        resources: Optional[List[dict]] = None,
    ) -> None:
        """
        Initialize a TermCredits object.

        :param str billing_option_id: (optional) The ID of the billing option from
               which the subscription term is derived.
        :param str billing_option_model: (optional) Billing option model.
        :param str category: (optional) The category of the billing option. The
               valid values are `PLATFORM`, `SERVICE`, and `SUPPORT`.
        :param datetime start_date: (optional) The start date of the term in ISO
               format.
        :param datetime end_date: (optional) The end date of the term in ISO
               format.
        :param float total_credits: (optional) The total credit available in this
               term.
        :param float starting_balance: (optional) The balance of available credit
               at the start of the current month.
        :param float used_credits: (optional) The amount of credit used during the
               current month.
        :param float current_balance: (optional) The balance of remaining credit in
               the subscription term.
        :param List[dict] resources: (optional) A list of resources that used
               credit during the month.
        """
        self.billing_option_id = billing_option_id
        self.billing_option_model = billing_option_model
        self.category = category
        self.start_date = start_date
        self.end_date = end_date
        self.total_credits = total_credits
        self.starting_balance = starting_balance
        self.used_credits = used_credits
        self.current_balance = current_balance
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TermCredits':
        """Initialize a TermCredits object from a json dictionary."""
        args = {}
        if (billing_option_id := _dict.get('billing_option_id')) is not None:
            args['billing_option_id'] = billing_option_id
        if (billing_option_model := _dict.get('billing_option_model')) is not None:
            args['billing_option_model'] = billing_option_model
        if (category := _dict.get('category')) is not None:
            args['category'] = category
        if (start_date := _dict.get('start_date')) is not None:
            args['start_date'] = string_to_datetime(start_date)
        if (end_date := _dict.get('end_date')) is not None:
            args['end_date'] = string_to_datetime(end_date)
        if (total_credits := _dict.get('total_credits')) is not None:
            args['total_credits'] = total_credits
        if (starting_balance := _dict.get('starting_balance')) is not None:
            args['starting_balance'] = starting_balance
        if (used_credits := _dict.get('used_credits')) is not None:
            args['used_credits'] = used_credits
        if (current_balance := _dict.get('current_balance')) is not None:
            args['current_balance'] = current_balance
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = resources
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TermCredits object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'billing_option_id') and self.billing_option_id is not None:
            _dict['billing_option_id'] = self.billing_option_id
        if hasattr(self, 'billing_option_model') and self.billing_option_model is not None:
            _dict['billing_option_model'] = self.billing_option_model
        if hasattr(self, 'category') and self.category is not None:
            _dict['category'] = self.category
        if hasattr(self, 'start_date') and self.start_date is not None:
            _dict['start_date'] = datetime_to_string(self.start_date)
        if hasattr(self, 'end_date') and self.end_date is not None:
            _dict['end_date'] = datetime_to_string(self.end_date)
        if hasattr(self, 'total_credits') and self.total_credits is not None:
            _dict['total_credits'] = self.total_credits
        if hasattr(self, 'starting_balance') and self.starting_balance is not None:
            _dict['starting_balance'] = self.starting_balance
        if hasattr(self, 'used_credits') and self.used_credits is not None:
            _dict['used_credits'] = self.used_credits
        if hasattr(self, 'current_balance') and self.current_balance is not None:
            _dict['current_balance'] = self.current_balance
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = self.resources
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TermCredits object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TermCredits') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TermCredits') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CategoryEnum(str, Enum):
        """
        The category of the billing option. The valid values are `PLATFORM`, `SERVICE`,
        and `SUPPORT`.
        """

        PLATFORM = 'PLATFORM'
        SERVICE = 'SERVICE'
        SUPPORT = 'SUPPORT'


##############################################################################
# Pagers
##############################################################################


class GetResourceUsageReportPager:
    """
    GetResourceUsageReportPager can be used to simplify the use of the "get_resource_usage_report" method.
    """

    def __init__(
        self,
        *,
        client: PartnerManagementV1,
        partner_id: str,
        reseller_id: str = None,
        customer_id: str = None,
        children: bool = None,
        month: str = None,
        viewpoint: str = None,
        recurse: bool = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a GetResourceUsageReportPager object.
        :param str partner_id: Enterprise ID of the distributor or reseller for
               which the report is requested.
        :param str reseller_id: (optional) Enterprise ID of the reseller for which
               the report is requested. This parameter cannot be used along with
               `customer_id` query parameter.
        :param str customer_id: (optional) Account ID/Enterprise ID of the end
               customer for which the report is requested. This parameter cannot be used
               along with `reseller_id` query parameter.
        :param bool children: (optional) Get report rolled-up to the direct
               children of the requested entity. Defaults to false. This parameter cannot
               be used along with `customer_id` query parameter.
        :param str month: (optional) The billing month for which the usage report
               is requested. Format is `yyyy-mm`. Defaults to current month.
        :param str viewpoint: (optional) Enables partner to view the cost of
               provisioned services as applicable at the given level. Defaults to the type
               of the calling partner. The valid values are `DISTRIBUTOR`, `RESELLER` and
               `END_CUSTOMER`.
        :param bool recurse: (optional) Get usage report rolled-up to the end
               customers of the requesting partner. Defaults to false. This parameter
               cannot be used along with `reseller_id` query parameter or `customer_id`
               query parameter.
        :param int limit: (optional) Number of usage records to be returned. The
               default value is 30. Maximum value is 100.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._partner_id = partner_id
        self._reseller_id = reseller_id
        self._customer_id = customer_id
        self._children = children
        self._month = month
        self._viewpoint = viewpoint
        self._recurse = recurse
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of PartnerUsageReport.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.get_resource_usage_report(
            partner_id=self._partner_id,
            reseller_id=self._reseller_id,
            customer_id=self._customer_id,
            children=self._children,
            month=self._month,
            viewpoint=self._viewpoint,
            recurse=self._recurse,
            limit=self._limit,
            offset=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('offset')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('reports')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of PartnerUsageReport.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
