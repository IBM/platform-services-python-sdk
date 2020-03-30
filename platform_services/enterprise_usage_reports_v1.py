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
Usage reports for IBM Cloud enterprise entities
"""

from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class EnterpriseUsageReportsV1(BaseService):
    """The Enterprise Usage Reports V1 service."""

    DEFAULT_SERVICE_URL = 'https://enterprise.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'enterprise_usage_reports'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'EnterpriseUsageReportsV1':
        """
        Return a new client for the Enterprise Usage Reports service using the
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
        Construct a new client for the Enterprise Usage Reports service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # default
    #########################


    def list_resource_usage_report(self, *, enterprise_id: str = None, account_group_id: str = None, account_id: str = None, children: bool = None, month: str = None, billing_unit_id: str = None, **kwargs) -> DetailedResponse:
        """
        Get usage reports for enterprise entities.

        Usage reports for entities in the IBM Cloud enterprise. These entities can be the
        enterprise, an account group, or an account.

        :param str enterprise_id: (optional) The ID of the enterprise for which the
               reports are queried. This parameter cannot be used with the `account_id` or
               `account_group_id` query parameters.
        :param str account_group_id: (optional) The ID of the account group for
               which the reports are queried. This parameter cannot be used with the
               `account_id` or `enterprise_id` query parameters.
        :param str account_id: (optional) The ID of the account for which the
               reports are queried. This parameter cannot be used with the
               `account_group_id` or `enterprise_id` query parameters.
        :param bool children: (optional) Returns the reports for the immediate
               child entities under the current account group or enterprise. This
               parameter cannot be used with the `account_id` query parameter.
        :param str month: (optional) The billing month for which the usage report
               is requested. The format is in yyyy-mm. Defaults to the month in which the
               report is queried.
        :param str billing_unit_id: (optional) The ID of the billing unit by which
               to filter the reports.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Reports` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_resource_usage_report')
        headers.update(sdk_headers)

        params = {
            'enterprise_id': enterprise_id,
            'account_group_id': account_group_id,
            'account_id': account_id,
            'children': children,
            'month': month,
            'billing_unit_id': billing_unit_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/resource-usage-reports'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class MetricUsageModel():
    """
    An object that represents a metric.

    :attr str metric: The name of the metric.
    :attr str unit: A unit to qualify the quantity.
    :attr float quantity: The aggregated value for the metric.
    :attr float rateable_quantity: The quantity that is used for calculating
          charges.
    :attr float cost: The cost that was incurred by the metric.
    :attr float rated_cost: The pre-discounted cost that was incurred by the metric.
    :attr List[object] price: (optional) The price with which cost was calculated.
    """

    def __init__(self, metric: str, unit: str, quantity: float, rateable_quantity: float, cost: float, rated_cost: float, *, price: List[object] = None) -> None:
        """
        Initialize a MetricUsageModel object.

        :param str metric: The name of the metric.
        :param str unit: A unit to qualify the quantity.
        :param float quantity: The aggregated value for the metric.
        :param float rateable_quantity: The quantity that is used for calculating
               charges.
        :param float cost: The cost that was incurred by the metric.
        :param float rated_cost: The pre-discounted cost that was incurred by the
               metric.
        :param List[object] price: (optional) The price with which cost was
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
    def from_dict(cls, _dict: Dict) -> 'MetricUsageModel':
        """Initialize a MetricUsageModel object from a json dictionary."""
        args = {}
        if 'metric' in _dict:
            args['metric'] = _dict.get('metric')
        else:
            raise ValueError('Required property \'metric\' not present in MetricUsageModel JSON')
        if 'unit' in _dict:
            args['unit'] = _dict.get('unit')
        else:
            raise ValueError('Required property \'unit\' not present in MetricUsageModel JSON')
        if 'quantity' in _dict:
            args['quantity'] = _dict.get('quantity')
        else:
            raise ValueError('Required property \'quantity\' not present in MetricUsageModel JSON')
        if 'rateable_quantity' in _dict:
            args['rateable_quantity'] = _dict.get('rateable_quantity')
        else:
            raise ValueError('Required property \'rateable_quantity\' not present in MetricUsageModel JSON')
        if 'cost' in _dict:
            args['cost'] = _dict.get('cost')
        else:
            raise ValueError('Required property \'cost\' not present in MetricUsageModel JSON')
        if 'rated_cost' in _dict:
            args['rated_cost'] = _dict.get('rated_cost')
        else:
            raise ValueError('Required property \'rated_cost\' not present in MetricUsageModel JSON')
        if 'price' in _dict:
            args['price'] = [object.from_dict(x) for x in _dict.get('price')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricUsageModel object from a json dictionary."""
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
            _dict['price'] = [x.to_dict() for x in self.price]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetricUsageModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MetricUsageModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetricUsageModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PlanUsageModel():
    """
    Aggregated values for the plan.

    :attr str plan_id: The ID of the plan.
    :attr str pricing_region: (optional) The pricing region for the plan.
    :attr str pricing_plan_id: (optional) The pricing plan with which the usage was
          rated.
    :attr bool billable: Whether the plan charges are billed to the customer.
    :attr float cost: The total cost that was incurred by the plan.
    :attr float rated_cost: The total pre-discounted cost that was incurred by the
          plan.
    :attr List[MetricUsageModel] usage: All of the metrics in the plan.
    """

    def __init__(self, plan_id: str, billable: bool, cost: float, rated_cost: float, usage: List['MetricUsageModel'], *, pricing_region: str = None, pricing_plan_id: str = None) -> None:
        """
        Initialize a PlanUsageModel object.

        :param str plan_id: The ID of the plan.
        :param bool billable: Whether the plan charges are billed to the customer.
        :param float cost: The total cost that was incurred by the plan.
        :param float rated_cost: The total pre-discounted cost that was incurred by
               the plan.
        :param List[MetricUsageModel] usage: All of the metrics in the plan.
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
    def from_dict(cls, _dict: Dict) -> 'PlanUsageModel':
        """Initialize a PlanUsageModel object from a json dictionary."""
        args = {}
        if 'plan_id' in _dict:
            args['plan_id'] = _dict.get('plan_id')
        else:
            raise ValueError('Required property \'plan_id\' not present in PlanUsageModel JSON')
        if 'pricing_region' in _dict:
            args['pricing_region'] = _dict.get('pricing_region')
        if 'pricing_plan_id' in _dict:
            args['pricing_plan_id'] = _dict.get('pricing_plan_id')
        if 'billable' in _dict:
            args['billable'] = _dict.get('billable')
        else:
            raise ValueError('Required property \'billable\' not present in PlanUsageModel JSON')
        if 'cost' in _dict:
            args['cost'] = _dict.get('cost')
        else:
            raise ValueError('Required property \'cost\' not present in PlanUsageModel JSON')
        if 'rated_cost' in _dict:
            args['rated_cost'] = _dict.get('rated_cost')
        else:
            raise ValueError('Required property \'rated_cost\' not present in PlanUsageModel JSON')
        if 'usage' in _dict:
            args['usage'] = [MetricUsageModel.from_dict(x) for x in _dict.get('usage')]
        else:
            raise ValueError('Required property \'usage\' not present in PlanUsageModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PlanUsageModel object from a json dictionary."""
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
            _dict['usage'] = [x.to_dict() for x in self.usage]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PlanUsageModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PlanUsageModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PlanUsageModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Reports():
    """
    Resource Usage Reports API response.

    :attr float limit: (optional) The maximum number of reports in the response.
    :attr ReportsFirst first: (optional) An object that contains the link to the
          first page of the search query.
    :attr ReportsNext next: (optional) An object that contains the link to the first
          page of the search query.
    :attr List[ResourceUsageReportModel] reports: (optional) The list of usage
          reports.
    """

    def __init__(self, *, limit: float = None, first: 'ReportsFirst' = None, next: 'ReportsNext' = None, reports: List['ResourceUsageReportModel'] = None) -> None:
        """
        Initialize a Reports object.

        :param float limit: (optional) The maximum number of reports in the
               response.
        :param ReportsFirst first: (optional) An object that contains the link to
               the first page of the search query.
        :param ReportsNext next: (optional) An object that contains the link to the
               first page of the search query.
        :param List[ResourceUsageReportModel] reports: (optional) The list of usage
               reports.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.reports = reports

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Reports':
        """Initialize a Reports object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'first' in _dict:
            args['first'] = ReportsFirst.from_dict(_dict.get('first'))
        if 'next' in _dict:
            args['next'] = ReportsNext.from_dict(_dict.get('next'))
        if 'reports' in _dict:
            args['reports'] = [ResourceUsageReportModel.from_dict(x) for x in _dict.get('reports')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Reports object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        if hasattr(self, 'reports') and self.reports is not None:
            _dict['reports'] = [x.to_dict() for x in self.reports]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Reports object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Reports') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Reports') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportsFirst():
    """
    An object that contains the link to the first page of the search query.

    :attr str href: (optional) A link to the first page of the search query.
    """

    def __init__(self, *, href: str = None) -> None:
        """
        Initialize a ReportsFirst object.

        :param str href: (optional) A link to the first page of the search query.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportsFirst':
        """Initialize a ReportsFirst object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportsFirst object from a json dictionary."""
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
        """Return a `str` version of this ReportsFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportsFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportsFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportsNext():
    """
    An object that contains the link to the first page of the search query.

    :attr str href: (optional) A link to the first page of the search query.
    """

    def __init__(self, *, href: str = None) -> None:
        """
        Initialize a ReportsNext object.

        :param str href: (optional) A link to the first page of the search query.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportsNext':
        """Initialize a ReportsNext object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportsNext object from a json dictionary."""
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
        """Return a `str` version of this ReportsNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportsNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportsNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceUsageModel():
    """
    A container for all the plans in the resource.

    :attr str resource_id: The ID of the resource.
    :attr float billable_cost: The billable charges for the account.
    :attr float billable_rated_cost: The pre-discounted billable charges for the
          account.
    :attr float non_billable_cost: The non-billable charges for the account.
    :attr float non_billable_rated_cost: The pre-discounted, non-billable charges
          for the account.
    :attr List[PlanUsageModel] plans: All of the plans in the resource.
    """

    def __init__(self, resource_id: str, billable_cost: float, billable_rated_cost: float, non_billable_cost: float, non_billable_rated_cost: float, plans: List['PlanUsageModel']) -> None:
        """
        Initialize a ResourceUsageModel object.

        :param str resource_id: The ID of the resource.
        :param float billable_cost: The billable charges for the account.
        :param float billable_rated_cost: The pre-discounted billable charges for
               the account.
        :param float non_billable_cost: The non-billable charges for the account.
        :param float non_billable_rated_cost: The pre-discounted, non-billable
               charges for the account.
        :param List[PlanUsageModel] plans: All of the plans in the resource.
        """
        self.resource_id = resource_id
        self.billable_cost = billable_cost
        self.billable_rated_cost = billable_rated_cost
        self.non_billable_cost = non_billable_cost
        self.non_billable_rated_cost = non_billable_rated_cost
        self.plans = plans

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceUsageModel':
        """Initialize a ResourceUsageModel object from a json dictionary."""
        args = {}
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        else:
            raise ValueError('Required property \'resource_id\' not present in ResourceUsageModel JSON')
        if 'billable_cost' in _dict:
            args['billable_cost'] = _dict.get('billable_cost')
        else:
            raise ValueError('Required property \'billable_cost\' not present in ResourceUsageModel JSON')
        if 'billable_rated_cost' in _dict:
            args['billable_rated_cost'] = _dict.get('billable_rated_cost')
        else:
            raise ValueError('Required property \'billable_rated_cost\' not present in ResourceUsageModel JSON')
        if 'non_billable_cost' in _dict:
            args['non_billable_cost'] = _dict.get('non_billable_cost')
        else:
            raise ValueError('Required property \'non_billable_cost\' not present in ResourceUsageModel JSON')
        if 'non_billable_rated_cost' in _dict:
            args['non_billable_rated_cost'] = _dict.get('non_billable_rated_cost')
        else:
            raise ValueError('Required property \'non_billable_rated_cost\' not present in ResourceUsageModel JSON')
        if 'plans' in _dict:
            args['plans'] = [PlanUsageModel.from_dict(x) for x in _dict.get('plans')]
        else:
            raise ValueError('Required property \'plans\' not present in ResourceUsageModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceUsageModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceUsageModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceUsageModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceUsageModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceUsageReportModel():
    """
    An object that represents a usage report.

    :attr str entity_id: The ID of the entity.
    :attr str entity_type: The entity type.
    :attr str entity_crn: The Cloud Resource Name (CRN) of the entity towards which
          the resource usages were rolled up.
    :attr str entity_name: A user-defined name for the entity, such as the
          enterprise name or account group name.
    :attr str billing_unit_id: The ID of the billing unit.
    :attr str billing_unit_crn: The CRN of the billing unit.
    :attr str billing_unit_name: The name of the billing unit.
    :attr str country_code: The country code of the billing unit.
    :attr str currency_code: The currency code of the billing unit.
    :attr str month: Billing month.
    :attr float billable_cost: Billable charges that are aggregated from all
          entities in the report.
    :attr float non_billable_cost: Non-billable charges that are aggregated from all
          entities in the report.
    :attr float billable_rated_cost: Aggregated billable charges before discounts.
    :attr float non_billable_rated_cost: Aggregated non-billable charges before
          discounts.
    :attr List[ResourceUsageModel] resources: Details about all the resources that
          are included in the aggregated charges.
    """

    def __init__(self, entity_id: str, entity_type: str, entity_crn: str, entity_name: str, billing_unit_id: str, billing_unit_crn: str, billing_unit_name: str, country_code: str, currency_code: str, month: str, billable_cost: float, non_billable_cost: float, billable_rated_cost: float, non_billable_rated_cost: float, resources: List['ResourceUsageModel']) -> None:
        """
        Initialize a ResourceUsageReportModel object.

        :param str entity_id: The ID of the entity.
        :param str entity_type: The entity type.
        :param str entity_crn: The Cloud Resource Name (CRN) of the entity towards
               which the resource usages were rolled up.
        :param str entity_name: A user-defined name for the entity, such as the
               enterprise name or account group name.
        :param str billing_unit_id: The ID of the billing unit.
        :param str billing_unit_crn: The CRN of the billing unit.
        :param str billing_unit_name: The name of the billing unit.
        :param str country_code: The country code of the billing unit.
        :param str currency_code: The currency code of the billing unit.
        :param str month: Billing month.
        :param float billable_cost: Billable charges that are aggregated from all
               entities in the report.
        :param float non_billable_cost: Non-billable charges that are aggregated
               from all entities in the report.
        :param float billable_rated_cost: Aggregated billable charges before
               discounts.
        :param float non_billable_rated_cost: Aggregated non-billable charges
               before discounts.
        :param List[ResourceUsageModel] resources: Details about all the resources
               that are included in the aggregated charges.
        """
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.entity_crn = entity_crn
        self.entity_name = entity_name
        self.billing_unit_id = billing_unit_id
        self.billing_unit_crn = billing_unit_crn
        self.billing_unit_name = billing_unit_name
        self.country_code = country_code
        self.currency_code = currency_code
        self.month = month
        self.billable_cost = billable_cost
        self.non_billable_cost = non_billable_cost
        self.billable_rated_cost = billable_rated_cost
        self.non_billable_rated_cost = non_billable_rated_cost
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceUsageReportModel':
        """Initialize a ResourceUsageReportModel object from a json dictionary."""
        args = {}
        if 'entity_id' in _dict:
            args['entity_id'] = _dict.get('entity_id')
        else:
            raise ValueError('Required property \'entity_id\' not present in ResourceUsageReportModel JSON')
        if 'entity_type' in _dict:
            args['entity_type'] = _dict.get('entity_type')
        else:
            raise ValueError('Required property \'entity_type\' not present in ResourceUsageReportModel JSON')
        if 'entity_crn' in _dict:
            args['entity_crn'] = _dict.get('entity_crn')
        else:
            raise ValueError('Required property \'entity_crn\' not present in ResourceUsageReportModel JSON')
        if 'entity_name' in _dict:
            args['entity_name'] = _dict.get('entity_name')
        else:
            raise ValueError('Required property \'entity_name\' not present in ResourceUsageReportModel JSON')
        if 'billing_unit_id' in _dict:
            args['billing_unit_id'] = _dict.get('billing_unit_id')
        else:
            raise ValueError('Required property \'billing_unit_id\' not present in ResourceUsageReportModel JSON')
        if 'billing_unit_crn' in _dict:
            args['billing_unit_crn'] = _dict.get('billing_unit_crn')
        else:
            raise ValueError('Required property \'billing_unit_crn\' not present in ResourceUsageReportModel JSON')
        if 'billing_unit_name' in _dict:
            args['billing_unit_name'] = _dict.get('billing_unit_name')
        else:
            raise ValueError('Required property \'billing_unit_name\' not present in ResourceUsageReportModel JSON')
        if 'country_code' in _dict:
            args['country_code'] = _dict.get('country_code')
        else:
            raise ValueError('Required property \'country_code\' not present in ResourceUsageReportModel JSON')
        if 'currency_code' in _dict:
            args['currency_code'] = _dict.get('currency_code')
        else:
            raise ValueError('Required property \'currency_code\' not present in ResourceUsageReportModel JSON')
        if 'month' in _dict:
            args['month'] = _dict.get('month')
        else:
            raise ValueError('Required property \'month\' not present in ResourceUsageReportModel JSON')
        if 'billable_cost' in _dict:
            args['billable_cost'] = _dict.get('billable_cost')
        else:
            raise ValueError('Required property \'billable_cost\' not present in ResourceUsageReportModel JSON')
        if 'non_billable_cost' in _dict:
            args['non_billable_cost'] = _dict.get('non_billable_cost')
        else:
            raise ValueError('Required property \'non_billable_cost\' not present in ResourceUsageReportModel JSON')
        if 'billable_rated_cost' in _dict:
            args['billable_rated_cost'] = _dict.get('billable_rated_cost')
        else:
            raise ValueError('Required property \'billable_rated_cost\' not present in ResourceUsageReportModel JSON')
        if 'non_billable_rated_cost' in _dict:
            args['non_billable_rated_cost'] = _dict.get('non_billable_rated_cost')
        else:
            raise ValueError('Required property \'non_billable_rated_cost\' not present in ResourceUsageReportModel JSON')
        if 'resources' in _dict:
            args['resources'] = [ResourceUsageModel.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in ResourceUsageReportModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceUsageReportModel object from a json dictionary."""
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
        if hasattr(self, 'billing_unit_id') and self.billing_unit_id is not None:
            _dict['billing_unit_id'] = self.billing_unit_id
        if hasattr(self, 'billing_unit_crn') and self.billing_unit_crn is not None:
            _dict['billing_unit_crn'] = self.billing_unit_crn
        if hasattr(self, 'billing_unit_name') and self.billing_unit_name is not None:
            _dict['billing_unit_name'] = self.billing_unit_name
        if hasattr(self, 'country_code') and self.country_code is not None:
            _dict['country_code'] = self.country_code
        if hasattr(self, 'currency_code') and self.currency_code is not None:
            _dict['currency_code'] = self.currency_code
        if hasattr(self, 'month') and self.month is not None:
            _dict['month'] = self.month
        if hasattr(self, 'billable_cost') and self.billable_cost is not None:
            _dict['billable_cost'] = self.billable_cost
        if hasattr(self, 'non_billable_cost') and self.non_billable_cost is not None:
            _dict['non_billable_cost'] = self.non_billable_cost
        if hasattr(self, 'billable_rated_cost') and self.billable_rated_cost is not None:
            _dict['billable_rated_cost'] = self.billable_rated_cost
        if hasattr(self, 'non_billable_rated_cost') and self.non_billable_rated_cost is not None:
            _dict['non_billable_rated_cost'] = self.non_billable_rated_cost
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceUsageReportModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceUsageReportModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceUsageReportModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class EntityTypeEnum(Enum):
        """
        The entity type.
        """
        ENTERPRISE = "enterprise"
        ACCOUNT_GROUP = "account-group"
        ACCOUNT = "account"


