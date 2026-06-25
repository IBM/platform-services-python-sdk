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

# IBM OpenAPI SDK Code Generator Version: 3.108.0-56772134-20251111-102802

"""
API for IBM Cloud account notifications, providing capabilities to:
- View notifications
- Get and update acknowledgements
- Manage user communication preferences
- Manage notification distribution lists

API Version: 1.0.0
"""

from enum import Enum
from typing import Dict, List, Optional
import json
import sys

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class PlatformNotificationsV1(BaseService):
    """The Platform Notifications V1 service."""

    DEFAULT_SERVICE_URL = 'https://notifications.cloud.ibm.com/api'
    DEFAULT_SERVICE_NAME = 'platform_notifications'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'PlatformNotificationsV1':
        """
        Return a new client for the Platform Notifications service using the
               specified parameters and external configuration.
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
        Construct a new client for the Platform Notifications service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Notifications
    #########################

    def list_notifications(
        self,
        *,
        account_id: Optional[str] = None,
        start: Optional[str] = None,
        limit: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get user notifications.

        Retrieve all notifications for the requested user.

        :param str account_id: (optional) The IBM Cloud account ID. If not
               provided, the account ID from the bearer token will be used.
        :param str start: (optional) An opaque page token that specifies the
               resource to start the page on or after. If unspecified, the first page of
               results is returned.
        :param int limit: (optional) The maximum number of items to return per
               page. If unspecified, a default limit of 50 is used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `NotificationCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_notifications',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'start': start,
            'limit': limit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/notifications'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_acknowledgement(
        self,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get acknowledgement.

        Retrieve the ID of the last notification acknowledged by the user for a specific
        account.

        :param str account_id: (optional) The IBM Cloud account ID. If not
               provided, the account ID from the bearer token will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Acknowledgement` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_acknowledgement',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/notifications/acknowledgement'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_notification_acknowledgement(
        self,
        last_acknowledged: int,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update acknowledgement.

        Update the ID of the last notification acknowledged by the user for a specific
        account.

        :param int last_acknowledged: The timestamp of the last acknowledgement.
        :param str account_id: (optional) The IBM Cloud account ID. If not
               provided, the account ID from the bearer token will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Acknowledgement` object
        """

        if last_acknowledged is None:
            raise ValueError('last_acknowledged must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='replace_notification_acknowledgement',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        data = {
            'last_acknowledged': last_acknowledged,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/notifications/acknowledgement'
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
    # distributionLists
    #########################

    def list_distribution_list_destinations(
        self,
        account_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all destination entries.

        Retrieve all destinations in the distribution list for the specified account.

        :param str account_id: The IBM Cloud account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AddDestinationCollection` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_distribution_list_destinations',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/distribution_lists/{account_id}/destinations'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_distribution_list_destination(
        self,
        account_id: str,
        add_destination_prototype: 'AddDestinationPrototype',
        **kwargs,
    ) -> DetailedResponse:
        """
        Add a destination entry.

        Add a destination entry to the distribution list. A maximum of 10 destination
        entries per destination type. In terms of enterprise accounts, you can provide an
        Event Notifications destination that is from a different account than the
        distribution list account, provided these two accounts are from the same
        enterprise and the user has permission to manage the Event Notifications
        destinations on both accounts.

        :param str account_id: The IBM Cloud account ID.
        :param AddDestinationPrototype add_destination_prototype:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AddDestination` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        if add_destination_prototype is None:
            raise ValueError('add_destination_prototype must be provided')
        if isinstance(add_destination_prototype, AddDestinationPrototype):
            add_destination_prototype = convert_model(add_destination_prototype)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_distribution_list_destination',
        )
        headers.update(sdk_headers)

        data = json.dumps(add_destination_prototype)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/distribution_lists/{account_id}/destinations'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_distribution_list_destination(
        self,
        account_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a destination entry.

        Retrieve a specific destination from the distribution list of the account.

        :param str account_id: The IBM Cloud account ID.
        :param str destination_id: The ID of the destination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AddDestination` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_distribution_list_destination',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'destination_id']
        path_param_values = self.encode_path_vars(account_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/distribution_lists/{account_id}/destinations/{destination_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_distribution_list_destination(
        self,
        account_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a destination entry.

        Remove a destination entry.

        :param str account_id: The IBM Cloud account ID.
        :param str destination_id: The ID of the destination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_distribution_list_destination',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['account_id', 'destination_id']
        path_param_values = self.encode_path_vars(account_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/distribution_lists/{account_id}/destinations/{destination_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def test_distribution_list_destination(
        self,
        account_id: str,
        destination_id: str,
        test_destination_request_body_prototype: 'TestDestinationRequestBodyPrototype',
        **kwargs,
    ) -> DetailedResponse:
        """
        Test a destination entry.

        Send a test notification to a destination in the distribution list. This allows
        you to verify that the destination is properly configured and can receive
        notifications.

        :param str account_id: The IBM Cloud account ID.
        :param str destination_id: The ID of the destination.
        :param TestDestinationRequestBodyPrototype
               test_destination_request_body_prototype:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TestDestinationResponseBody` object
        """

        if not account_id:
            raise ValueError('account_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if test_destination_request_body_prototype is None:
            raise ValueError('test_destination_request_body_prototype must be provided')
        if isinstance(test_destination_request_body_prototype, TestDestinationRequestBodyPrototype):
            test_destination_request_body_prototype = convert_model(test_destination_request_body_prototype)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='test_distribution_list_destination',
        )
        headers.update(sdk_headers)

        data = json.dumps(test_destination_request_body_prototype)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'destination_id']
        path_param_values = self.encode_path_vars(account_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/distribution_lists/{account_id}/destinations/{destination_id}/test'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # userPreferences
    #########################

    def get_preferences(
        self,
        iam_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all communication preferences.

        Retrieve all communication preferences of a user in an account.

        :param str iam_id: The IAM ID of the user. Must match the IAM ID in the
               bearer token.
        :param str account_id: (optional) The IBM Cloud account ID. If not
               provided, the account ID from the bearer token will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PreferencesObject` object
        """

        if not iam_id:
            raise ValueError('iam_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_preferences',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['iam_id']
        path_param_values = self.encode_path_vars(iam_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/notifications/{iam_id}/preferences'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_preferences(
        self,
        iam_id: str,
        *,
        incident_severity1: Optional['PreferenceValueWithUpdates'] = None,
        incident_severity2: Optional['PreferenceValueWithUpdates'] = None,
        incident_severity3: Optional['PreferenceValueWithUpdates'] = None,
        incident_severity4: Optional['PreferenceValueWithUpdates'] = None,
        maintenance_high: Optional['PreferenceValueWithUpdates'] = None,
        maintenance_medium: Optional['PreferenceValueWithUpdates'] = None,
        maintenance_low: Optional['PreferenceValueWithUpdates'] = None,
        announcements_major: Optional['PreferenceValueWithoutUpdates'] = None,
        announcements_minor: Optional['PreferenceValueWithoutUpdates'] = None,
        security_normal: Optional['PreferenceValueWithoutUpdates'] = None,
        account_normal: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_order: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_invoices: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_payments: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_subscriptions_and_promo_codes: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_spending_alerts: Optional['PreferenceValueWithoutUpdates'] = None,
        resourceactivity_normal: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_review: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_approved: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_approved_vsi: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_approved_server: Optional['PreferenceValueWithoutUpdates'] = None,
        provisioning_reload_complete: Optional['PreferenceValueWithoutUpdates'] = None,
        provisioning_complete_vsi: Optional['PreferenceValueWithoutUpdates'] = None,
        provisioning_complete_server: Optional['PreferenceValueWithoutUpdates'] = None,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create communication preferences.

        Create communication preferences for the specified account.

        :param str iam_id: The IAM ID of the user. Must match the IAM ID in the
               bearer token.
        :param PreferenceValueWithUpdates incident_severity1: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates incident_severity2: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates incident_severity3: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates incident_severity4: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates maintenance_high: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates maintenance_medium: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates maintenance_low: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithoutUpdates announcements_major: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates announcements_minor: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates security_normal: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates account_normal: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_order: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_invoices: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_payments: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates
               billing_and_usage_subscriptions_and_promo_codes: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_spending_alerts:
               (optional) Preference settings for notification types that do not support
               updates.
        :param PreferenceValueWithoutUpdates resourceactivity_normal: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_review: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_approved: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_approved_vsi: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_approved_server: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates provisioning_reload_complete:
               (optional) Preference settings for notification types that do not support
               updates.
        :param PreferenceValueWithoutUpdates provisioning_complete_vsi: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates provisioning_complete_server:
               (optional) Preference settings for notification types that do not support
               updates.
        :param str account_id: (optional) The IBM Cloud account ID. If not
               provided, the account ID from the bearer token will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PreferencesObject` object
        """

        if not iam_id:
            raise ValueError('iam_id must be provided')
        if incident_severity1 is not None:
            incident_severity1 = convert_model(incident_severity1)
        if incident_severity2 is not None:
            incident_severity2 = convert_model(incident_severity2)
        if incident_severity3 is not None:
            incident_severity3 = convert_model(incident_severity3)
        if incident_severity4 is not None:
            incident_severity4 = convert_model(incident_severity4)
        if maintenance_high is not None:
            maintenance_high = convert_model(maintenance_high)
        if maintenance_medium is not None:
            maintenance_medium = convert_model(maintenance_medium)
        if maintenance_low is not None:
            maintenance_low = convert_model(maintenance_low)
        if announcements_major is not None:
            announcements_major = convert_model(announcements_major)
        if announcements_minor is not None:
            announcements_minor = convert_model(announcements_minor)
        if security_normal is not None:
            security_normal = convert_model(security_normal)
        if account_normal is not None:
            account_normal = convert_model(account_normal)
        if billing_and_usage_order is not None:
            billing_and_usage_order = convert_model(billing_and_usage_order)
        if billing_and_usage_invoices is not None:
            billing_and_usage_invoices = convert_model(billing_and_usage_invoices)
        if billing_and_usage_payments is not None:
            billing_and_usage_payments = convert_model(billing_and_usage_payments)
        if billing_and_usage_subscriptions_and_promo_codes is not None:
            billing_and_usage_subscriptions_and_promo_codes = convert_model(
                billing_and_usage_subscriptions_and_promo_codes
            )
        if billing_and_usage_spending_alerts is not None:
            billing_and_usage_spending_alerts = convert_model(billing_and_usage_spending_alerts)
        if resourceactivity_normal is not None:
            resourceactivity_normal = convert_model(resourceactivity_normal)
        if ordering_review is not None:
            ordering_review = convert_model(ordering_review)
        if ordering_approved is not None:
            ordering_approved = convert_model(ordering_approved)
        if ordering_approved_vsi is not None:
            ordering_approved_vsi = convert_model(ordering_approved_vsi)
        if ordering_approved_server is not None:
            ordering_approved_server = convert_model(ordering_approved_server)
        if provisioning_reload_complete is not None:
            provisioning_reload_complete = convert_model(provisioning_reload_complete)
        if provisioning_complete_vsi is not None:
            provisioning_complete_vsi = convert_model(provisioning_complete_vsi)
        if provisioning_complete_server is not None:
            provisioning_complete_server = convert_model(provisioning_complete_server)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_preferences',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        data = {
            'incident_severity1': incident_severity1,
            'incident_severity2': incident_severity2,
            'incident_severity3': incident_severity3,
            'incident_severity4': incident_severity4,
            'maintenance_high': maintenance_high,
            'maintenance_medium': maintenance_medium,
            'maintenance_low': maintenance_low,
            'announcements_major': announcements_major,
            'announcements_minor': announcements_minor,
            'security_normal': security_normal,
            'account_normal': account_normal,
            'billing_and_usage_order': billing_and_usage_order,
            'billing_and_usage_invoices': billing_and_usage_invoices,
            'billing_and_usage_payments': billing_and_usage_payments,
            'billing_and_usage_subscriptions_and_promo_codes': billing_and_usage_subscriptions_and_promo_codes,
            'billing_and_usage_spending_alerts': billing_and_usage_spending_alerts,
            'resourceactivity_normal': resourceactivity_normal,
            'ordering_review': ordering_review,
            'ordering_approved': ordering_approved,
            'ordering_approved_vsi': ordering_approved_vsi,
            'ordering_approved_server': ordering_approved_server,
            'provisioning_reload_complete': provisioning_reload_complete,
            'provisioning_complete_vsi': provisioning_complete_vsi,
            'provisioning_complete_server': provisioning_complete_server,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['iam_id']
        path_param_values = self.encode_path_vars(iam_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/notifications/{iam_id}/preferences'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_notification_preferences(
        self,
        iam_id: str,
        *,
        incident_severity1: Optional['PreferenceValueWithUpdates'] = None,
        incident_severity2: Optional['PreferenceValueWithUpdates'] = None,
        incident_severity3: Optional['PreferenceValueWithUpdates'] = None,
        incident_severity4: Optional['PreferenceValueWithUpdates'] = None,
        maintenance_high: Optional['PreferenceValueWithUpdates'] = None,
        maintenance_medium: Optional['PreferenceValueWithUpdates'] = None,
        maintenance_low: Optional['PreferenceValueWithUpdates'] = None,
        announcements_major: Optional['PreferenceValueWithoutUpdates'] = None,
        announcements_minor: Optional['PreferenceValueWithoutUpdates'] = None,
        security_normal: Optional['PreferenceValueWithoutUpdates'] = None,
        account_normal: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_order: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_invoices: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_payments: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_subscriptions_and_promo_codes: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_spending_alerts: Optional['PreferenceValueWithoutUpdates'] = None,
        resourceactivity_normal: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_review: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_approved: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_approved_vsi: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_approved_server: Optional['PreferenceValueWithoutUpdates'] = None,
        provisioning_reload_complete: Optional['PreferenceValueWithoutUpdates'] = None,
        provisioning_complete_vsi: Optional['PreferenceValueWithoutUpdates'] = None,
        provisioning_complete_server: Optional['PreferenceValueWithoutUpdates'] = None,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update communication preferences.

        Update communication preferences for the specified account.

        :param str iam_id: The IAM ID of the user. Must match the IAM ID in the
               bearer token.
        :param PreferenceValueWithUpdates incident_severity1: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates incident_severity2: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates incident_severity3: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates incident_severity4: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates maintenance_high: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates maintenance_medium: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates maintenance_low: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithoutUpdates announcements_major: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates announcements_minor: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates security_normal: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates account_normal: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_order: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_invoices: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_payments: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates
               billing_and_usage_subscriptions_and_promo_codes: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_spending_alerts:
               (optional) Preference settings for notification types that do not support
               updates.
        :param PreferenceValueWithoutUpdates resourceactivity_normal: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_review: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_approved: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_approved_vsi: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_approved_server: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates provisioning_reload_complete:
               (optional) Preference settings for notification types that do not support
               updates.
        :param PreferenceValueWithoutUpdates provisioning_complete_vsi: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates provisioning_complete_server:
               (optional) Preference settings for notification types that do not support
               updates.
        :param str account_id: (optional) The IBM Cloud account ID. If not
               provided, the account ID from the bearer token will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PreferencesObject` object
        """

        if not iam_id:
            raise ValueError('iam_id must be provided')
        if incident_severity1 is not None:
            incident_severity1 = convert_model(incident_severity1)
        if incident_severity2 is not None:
            incident_severity2 = convert_model(incident_severity2)
        if incident_severity3 is not None:
            incident_severity3 = convert_model(incident_severity3)
        if incident_severity4 is not None:
            incident_severity4 = convert_model(incident_severity4)
        if maintenance_high is not None:
            maintenance_high = convert_model(maintenance_high)
        if maintenance_medium is not None:
            maintenance_medium = convert_model(maintenance_medium)
        if maintenance_low is not None:
            maintenance_low = convert_model(maintenance_low)
        if announcements_major is not None:
            announcements_major = convert_model(announcements_major)
        if announcements_minor is not None:
            announcements_minor = convert_model(announcements_minor)
        if security_normal is not None:
            security_normal = convert_model(security_normal)
        if account_normal is not None:
            account_normal = convert_model(account_normal)
        if billing_and_usage_order is not None:
            billing_and_usage_order = convert_model(billing_and_usage_order)
        if billing_and_usage_invoices is not None:
            billing_and_usage_invoices = convert_model(billing_and_usage_invoices)
        if billing_and_usage_payments is not None:
            billing_and_usage_payments = convert_model(billing_and_usage_payments)
        if billing_and_usage_subscriptions_and_promo_codes is not None:
            billing_and_usage_subscriptions_and_promo_codes = convert_model(
                billing_and_usage_subscriptions_and_promo_codes
            )
        if billing_and_usage_spending_alerts is not None:
            billing_and_usage_spending_alerts = convert_model(billing_and_usage_spending_alerts)
        if resourceactivity_normal is not None:
            resourceactivity_normal = convert_model(resourceactivity_normal)
        if ordering_review is not None:
            ordering_review = convert_model(ordering_review)
        if ordering_approved is not None:
            ordering_approved = convert_model(ordering_approved)
        if ordering_approved_vsi is not None:
            ordering_approved_vsi = convert_model(ordering_approved_vsi)
        if ordering_approved_server is not None:
            ordering_approved_server = convert_model(ordering_approved_server)
        if provisioning_reload_complete is not None:
            provisioning_reload_complete = convert_model(provisioning_reload_complete)
        if provisioning_complete_vsi is not None:
            provisioning_complete_vsi = convert_model(provisioning_complete_vsi)
        if provisioning_complete_server is not None:
            provisioning_complete_server = convert_model(provisioning_complete_server)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='replace_notification_preferences',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        data = {
            'incident_severity1': incident_severity1,
            'incident_severity2': incident_severity2,
            'incident_severity3': incident_severity3,
            'incident_severity4': incident_severity4,
            'maintenance_high': maintenance_high,
            'maintenance_medium': maintenance_medium,
            'maintenance_low': maintenance_low,
            'announcements_major': announcements_major,
            'announcements_minor': announcements_minor,
            'security_normal': security_normal,
            'account_normal': account_normal,
            'billing_and_usage_order': billing_and_usage_order,
            'billing_and_usage_invoices': billing_and_usage_invoices,
            'billing_and_usage_payments': billing_and_usage_payments,
            'billing_and_usage_subscriptions_and_promo_codes': billing_and_usage_subscriptions_and_promo_codes,
            'billing_and_usage_spending_alerts': billing_and_usage_spending_alerts,
            'resourceactivity_normal': resourceactivity_normal,
            'ordering_review': ordering_review,
            'ordering_approved': ordering_approved,
            'ordering_approved_vsi': ordering_approved_vsi,
            'ordering_approved_server': ordering_approved_server,
            'provisioning_reload_complete': provisioning_reload_complete,
            'provisioning_complete_vsi': provisioning_complete_vsi,
            'provisioning_complete_server': provisioning_complete_server,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['iam_id']
        path_param_values = self.encode_path_vars(iam_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/notifications/{iam_id}/preferences'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_notification_preferences(
        self,
        iam_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Reset all preferences to their default values.

        Delete all communication preferences for the specified account, and reset all
        preferences to their default values.

        :param str iam_id: The IAM ID of the user. Must match the IAM ID in the
               bearer token.
        :param str account_id: (optional) The IBM Cloud account ID. If not
               provided, the account ID from the bearer token will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not iam_id:
            raise ValueError('iam_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_notification_preferences',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['iam_id']
        path_param_values = self.encode_path_vars(iam_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/notifications/{iam_id}/preferences'.format(**path_param_dict)
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


class Acknowledgement:
    """
    Status indicating whether the user has unread notifications.

    :param bool has_unread: Indicates whether the user has unread notifications.
    :param int last_acknowledged: The timestamp of the last acknowledgement.
    """

    def __init__(
        self,
        has_unread: bool,
        last_acknowledged: int,
    ) -> None:
        """
        Initialize a Acknowledgement object.

        :param bool has_unread: Indicates whether the user has unread
               notifications.
        :param int last_acknowledged: The timestamp of the last acknowledgement.
        """
        self.has_unread = has_unread
        self.last_acknowledged = last_acknowledged

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Acknowledgement':
        """Initialize a Acknowledgement object from a json dictionary."""
        args = {}
        if (has_unread := _dict.get('has_unread')) is not None:
            args['has_unread'] = has_unread
        else:
            raise ValueError('Required property \'has_unread\' not present in Acknowledgement JSON')
        if (last_acknowledged := _dict.get('last_acknowledged')) is not None:
            args['last_acknowledged'] = last_acknowledged
        else:
            raise ValueError('Required property \'last_acknowledged\' not present in Acknowledgement JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Acknowledgement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'has_unread') and self.has_unread is not None:
            _dict['has_unread'] = self.has_unread
        if hasattr(self, 'last_acknowledged') and self.last_acknowledged is not None:
            _dict['last_acknowledged'] = self.last_acknowledged
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Acknowledgement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Acknowledgement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Acknowledgement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AddDestination:
    """
    AddDestination.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a AddDestination object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['AddDestinationEventNotificationDestination'])
        )
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddDestination':
        """Initialize a AddDestination object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = "Cannot convert dictionary into an instance of base class 'AddDestination'. The discriminator value should map to a valid subclass: {1}".format(
            ", ".join(['AddDestinationEventNotificationDestination'])
        )
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a AddDestination object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['event_notifications'] = 'AddDestinationEventNotificationDestination'
        disc_value = _dict.get('destination_type')
        if disc_value is None:
            raise ValueError('Discriminator property \'destination_type\' not found in AddDestination JSON')
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)


class AddDestinationCollection:
    """
    List of destinations in the distribution list.

    :param List[AddDestination] destinations: Array of destination entries.
    """

    def __init__(
        self,
        destinations: List['AddDestination'],
    ) -> None:
        """
        Initialize a AddDestinationCollection object.

        :param List[AddDestination] destinations: Array of destination entries.
        """
        self.destinations = destinations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddDestinationCollection':
        """Initialize a AddDestinationCollection object from a json dictionary."""
        args = {}
        if (destinations := _dict.get('destinations')) is not None:
            args['destinations'] = [AddDestination.from_dict(v) for v in destinations]
        else:
            raise ValueError('Required property \'destinations\' not present in AddDestinationCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddDestinationCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'destinations') and self.destinations is not None:
            destinations_list = []
            for v in self.destinations:
                if isinstance(v, dict):
                    destinations_list.append(v)
                else:
                    destinations_list.append(v.to_dict())
            _dict['destinations'] = destinations_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddDestinationCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddDestinationCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddDestinationCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AddDestinationPrototype:
    """
    AddDestinationPrototype.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a AddDestinationPrototype object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['AddDestinationPrototypeEventNotificationDestinationPrototype'])
        )
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddDestinationPrototype':
        """Initialize a AddDestinationPrototype object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = "Cannot convert dictionary into an instance of base class 'AddDestinationPrototype'. The discriminator value should map to a valid subclass: {1}".format(
            ", ".join(['AddDestinationPrototypeEventNotificationDestinationPrototype'])
        )
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a AddDestinationPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['event_notifications'] = 'AddDestinationPrototypeEventNotificationDestinationPrototype'
        disc_value = _dict.get('destination_type')
        if disc_value is None:
            raise ValueError('Discriminator property \'destination_type\' not found in AddDestinationPrototype JSON')
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)


class Notification:
    """
    A notification entry.

    :param str title: The title of the notification.
    :param str body: The body content of the notification.
    :param str id: The unique identifier for the notification.
    :param str category: The category of the notification.
    :param List[str] component_names: Array of component/service names affected by
          this notification.
    :param int start_time: (optional) The start time of the notification in Unix
          timestamp (seconds).
    :param bool is_global: Indicates if the notification is global.
    :param str state: (optional) The current state of the notification.
    :param List[str] regions: Array of region identifiers affected by this
          notification.
    :param List[str] crn_masks: Array of CRN masks that define the scope of affected
          resources.
    :param str record_id: (optional) The record identifier for tracking purposes.
    :param str source_id: (optional) The source identifier of the notification.
    :param str completion_code: (optional) The completion code of the notification.
    :param int end_time: (optional) The end time of the notification in Unix
          timestamp (seconds).
    :param int update_time: (optional) The last update time of the notification in
          Unix timestamp (seconds).
    :param int severity: The severity level of the notification (0-3). The display
          value depends on the notification type:
          **Incidents:**
          - 1 = Severity 1
          - 2 = Severity 2
          - 3 = Severity 3
          - 0 = Severity 4
          **Maintenance:**
          - 1 = High
          - 2 = Medium
          - 3 = Low
          **Announcements:**
          - 1 = Major
          - 0 = Minor.
    :param str lucene_query: (optional) Lucene query string for filtering affected
          resources. Only present when instance targets are specified and resource_link is
          not available. Mutually exclusive with resource_link.
    :param str resource_link: (optional) Link to additional resource information or
          documentation. Takes precedence over lucene_query when both are available.
          Mutually exclusive with lucene_query.
    :param int creation_timestamp: The timestamp when the notification was created.
    """

    def __init__(
        self,
        title: str,
        body: str,
        id: str,
        category: str,
        component_names: List[str],
        is_global: bool,
        regions: List[str],
        crn_masks: List[str],
        severity: int,
        creation_timestamp: int,
        *,
        start_time: Optional[int] = None,
        state: Optional[str] = None,
        record_id: Optional[str] = None,
        source_id: Optional[str] = None,
        completion_code: Optional[str] = None,
        end_time: Optional[int] = None,
        update_time: Optional[int] = None,
        lucene_query: Optional[str] = None,
        resource_link: Optional[str] = None,
    ) -> None:
        """
        Initialize a Notification object.

        :param str title: The title of the notification.
        :param str body: The body content of the notification.
        :param str id: The unique identifier for the notification.
        :param str category: The category of the notification.
        :param List[str] component_names: Array of component/service names affected
               by this notification.
        :param bool is_global: Indicates if the notification is global.
        :param List[str] regions: Array of region identifiers affected by this
               notification.
        :param List[str] crn_masks: Array of CRN masks that define the scope of
               affected resources.
        :param int severity: The severity level of the notification (0-3). The
               display value depends on the notification type:
               **Incidents:**
               - 1 = Severity 1
               - 2 = Severity 2
               - 3 = Severity 3
               - 0 = Severity 4
               **Maintenance:**
               - 1 = High
               - 2 = Medium
               - 3 = Low
               **Announcements:**
               - 1 = Major
               - 0 = Minor.
        :param int creation_timestamp: The timestamp when the notification was
               created.
        :param int start_time: (optional) The start time of the notification in
               Unix timestamp (seconds).
        :param str state: (optional) The current state of the notification.
        :param str record_id: (optional) The record identifier for tracking
               purposes.
        :param str source_id: (optional) The source identifier of the notification.
        :param str completion_code: (optional) The completion code of the
               notification.
        :param int end_time: (optional) The end time of the notification in Unix
               timestamp (seconds).
        :param int update_time: (optional) The last update time of the notification
               in Unix timestamp (seconds).
        :param str lucene_query: (optional) Lucene query string for filtering
               affected resources. Only present when instance targets are specified and
               resource_link is not available. Mutually exclusive with resource_link.
        :param str resource_link: (optional) Link to additional resource
               information or documentation. Takes precedence over lucene_query when both
               are available. Mutually exclusive with lucene_query.
        """
        self.title = title
        self.body = body
        self.id = id
        self.category = category
        self.component_names = component_names
        self.start_time = start_time
        self.is_global = is_global
        self.state = state
        self.regions = regions
        self.crn_masks = crn_masks
        self.record_id = record_id
        self.source_id = source_id
        self.completion_code = completion_code
        self.end_time = end_time
        self.update_time = update_time
        self.severity = severity
        self.lucene_query = lucene_query
        self.resource_link = resource_link
        self.creation_timestamp = creation_timestamp

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Notification':
        """Initialize a Notification object from a json dictionary."""
        args = {}
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        else:
            raise ValueError('Required property \'title\' not present in Notification JSON')
        if (body := _dict.get('body')) is not None:
            args['body'] = body
        else:
            raise ValueError('Required property \'body\' not present in Notification JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Notification JSON')
        if (category := _dict.get('category')) is not None:
            args['category'] = category
        else:
            raise ValueError('Required property \'category\' not present in Notification JSON')
        if (component_names := _dict.get('component_names')) is not None:
            args['component_names'] = component_names
        else:
            raise ValueError('Required property \'component_names\' not present in Notification JSON')
        if (start_time := _dict.get('start_time')) is not None:
            args['start_time'] = start_time
        if (is_global := _dict.get('is_global')) is not None:
            args['is_global'] = is_global
        else:
            raise ValueError('Required property \'is_global\' not present in Notification JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        if (regions := _dict.get('regions')) is not None:
            args['regions'] = regions
        else:
            raise ValueError('Required property \'regions\' not present in Notification JSON')
        if (crn_masks := _dict.get('crn_masks')) is not None:
            args['crn_masks'] = crn_masks
        else:
            raise ValueError('Required property \'crn_masks\' not present in Notification JSON')
        if (record_id := _dict.get('record_id')) is not None:
            args['record_id'] = record_id
        if (source_id := _dict.get('source_id')) is not None:
            args['source_id'] = source_id
        if (completion_code := _dict.get('completion_code')) is not None:
            args['completion_code'] = completion_code
        if (end_time := _dict.get('end_time')) is not None:
            args['end_time'] = end_time
        if (update_time := _dict.get('update_time')) is not None:
            args['update_time'] = update_time
        if (severity := _dict.get('severity')) is not None:
            args['severity'] = severity
        else:
            raise ValueError('Required property \'severity\' not present in Notification JSON')
        if (lucene_query := _dict.get('lucene_query')) is not None:
            args['lucene_query'] = lucene_query
        if (resource_link := _dict.get('resource_link')) is not None:
            args['resource_link'] = resource_link
        if (creation_timestamp := _dict.get('creation_timestamp')) is not None:
            args['creation_timestamp'] = creation_timestamp
        else:
            raise ValueError('Required property \'creation_timestamp\' not present in Notification JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Notification object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'category') and self.category is not None:
            _dict['category'] = self.category
        if hasattr(self, 'component_names') and self.component_names is not None:
            _dict['component_names'] = self.component_names
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'is_global') and self.is_global is not None:
            _dict['is_global'] = self.is_global
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'regions') and self.regions is not None:
            _dict['regions'] = self.regions
        if hasattr(self, 'crn_masks') and self.crn_masks is not None:
            _dict['crn_masks'] = self.crn_masks
        if hasattr(self, 'record_id') and self.record_id is not None:
            _dict['record_id'] = self.record_id
        if hasattr(self, 'source_id') and self.source_id is not None:
            _dict['source_id'] = self.source_id
        if hasattr(self, 'completion_code') and self.completion_code is not None:
            _dict['completion_code'] = self.completion_code
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'update_time') and self.update_time is not None:
            _dict['update_time'] = self.update_time
        if hasattr(self, 'severity') and self.severity is not None:
            _dict['severity'] = self.severity
        if hasattr(self, 'lucene_query') and self.lucene_query is not None:
            _dict['lucene_query'] = self.lucene_query
        if hasattr(self, 'resource_link') and self.resource_link is not None:
            _dict['resource_link'] = self.resource_link
        if hasattr(self, 'creation_timestamp') and self.creation_timestamp is not None:
            _dict['creation_timestamp'] = self.creation_timestamp
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Notification object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Notification') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Notification') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CategoryEnum(str, Enum):
        """
        The category of the notification.
        """

        INCIDENT = 'incident'
        MAINTENANCE = 'maintenance'
        ANNOUNCEMENTS = 'announcements'
        SECURITY_BULLETINS = 'security_bulletins'
        SECURITY = 'security'
        RESOURCE = 'resource'
        BILLING_AND_USAGE = 'billing_and_usage'
        ORDERING = 'ordering'
        PROVISIONING = 'provisioning'
        ACCOUNT = 'account'

    class StateEnum(str, Enum):
        """
        The current state of the notification.
        """

        NEW = 'new'
        IN_PROGRESS = 'in-progress'
        COMPLETE = 'complete'
        RESOLVED = 'resolved'

    class CompletionCodeEnum(str, Enum):
        """
        The completion code of the notification.
        """

        SUCCESSFUL = 'successful'
        FAILED = 'failed'
        CANCELLED = 'cancelled'


class NotificationCollection:
    """
    Collection of user notifications with token-based pagination metadata.

    :param int limit: The maximum number of items returned in this response.
    :param int total_count: The total number of notifications in the collection.
    :param PaginationLink first: A pagination link object containing the URL to a
          page.
    :param PaginationLinkWithToken previous: (optional) A pagination link object
          with a page token. Used for next, previous, and last page links.
    :param PaginationLinkWithToken next: (optional) A pagination link object with a
          page token. Used for next, previous, and last page links.
    :param PaginationLinkWithToken last: (optional) A pagination link object with a
          page token. Used for next, previous, and last page links.
    :param List[Notification] notifications: Array of notification entries.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        first: 'PaginationLink',
        notifications: List['Notification'],
        *,
        previous: Optional['PaginationLinkWithToken'] = None,
        next: Optional['PaginationLinkWithToken'] = None,
        last: Optional['PaginationLinkWithToken'] = None,
    ) -> None:
        """
        Initialize a NotificationCollection object.

        :param int limit: The maximum number of items returned in this response.
        :param int total_count: The total number of notifications in the
               collection.
        :param PaginationLink first: A pagination link object containing the URL to
               a page.
        :param List[Notification] notifications: Array of notification entries.
        :param PaginationLinkWithToken previous: (optional) A pagination link
               object with a page token. Used for next, previous, and last page links.
        :param PaginationLinkWithToken next: (optional) A pagination link object
               with a page token. Used for next, previous, and last page links.
        :param PaginationLinkWithToken last: (optional) A pagination link object
               with a page token. Used for next, previous, and last page links.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.previous = previous
        self.next = next
        self.last = last
        self.notifications = notifications

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationCollection':
        """Initialize a NotificationCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in NotificationCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in NotificationCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PaginationLink.from_dict(first)
        else:
            raise ValueError('Required property \'first\' not present in NotificationCollection JSON')
        if (previous := _dict.get('previous')) is not None:
            args['previous'] = PaginationLinkWithToken.from_dict(previous)
        if (next := _dict.get('next')) is not None:
            args['next'] = PaginationLinkWithToken.from_dict(next)
        if (last := _dict.get('last')) is not None:
            args['last'] = PaginationLinkWithToken.from_dict(last)
        if (notifications := _dict.get('notifications')) is not None:
            args['notifications'] = [Notification.from_dict(v) for v in notifications]
        else:
            raise ValueError('Required property \'notifications\' not present in NotificationCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            if isinstance(self.previous, dict):
                _dict['previous'] = self.previous
            else:
                _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            if isinstance(self.last, dict):
                _dict['last'] = self.last
            else:
                _dict['last'] = self.last.to_dict()
        if hasattr(self, 'notifications') and self.notifications is not None:
            notifications_list = []
            for v in self.notifications:
                if isinstance(v, dict):
                    notifications_list.append(v)
                else:
                    notifications_list.append(v.to_dict())
            _dict['notifications'] = notifications_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NotificationCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PaginationLink:
    """
    A pagination link object containing the URL to a page.

    :param str href: The full URL path to the page.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a PaginationLink object.

        :param str href: The full URL path to the page.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PaginationLink':
        """Initialize a PaginationLink object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in PaginationLink JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PaginationLink object from a json dictionary."""
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
        """Return a `str` version of this PaginationLink object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PaginationLink') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PaginationLink') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PaginationLinkWithToken:
    """
    A pagination link object with a page token. Used for next, previous, and last page
    links.

    :param str href: Complete URL to the page.
    :param str start: Opaque page token that can be used to retrieve the page.
    """

    def __init__(
        self,
        href: str,
        start: str,
    ) -> None:
        """
        Initialize a PaginationLinkWithToken object.

        :param str href: Complete URL to the page.
        :param str start: Opaque page token that can be used to retrieve the page.
        """
        self.href = href
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PaginationLinkWithToken':
        """Initialize a PaginationLinkWithToken object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in PaginationLinkWithToken JSON')
        if (start := _dict.get('start')) is not None:
            args['start'] = start
        else:
            raise ValueError('Required property \'start\' not present in PaginationLinkWithToken JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PaginationLinkWithToken object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PaginationLinkWithToken object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PaginationLinkWithToken') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PaginationLinkWithToken') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PreferenceValueWithUpdates:
    """
    Preference settings for notification types that support updates.

    :param List[str] channels: Array of communication channels for this preference.
    :param bool updates: (optional) Whether to receive updates for this preference.
          Optional, defaults to false if not provided.
    """

    def __init__(
        self,
        channels: List[str],
        *,
        updates: Optional[bool] = None,
    ) -> None:
        """
        Initialize a PreferenceValueWithUpdates object.

        :param List[str] channels: Array of communication channels for this
               preference.
        :param bool updates: (optional) Whether to receive updates for this
               preference. Optional, defaults to false if not provided.
        """
        self.channels = channels
        self.updates = updates

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PreferenceValueWithUpdates':
        """Initialize a PreferenceValueWithUpdates object from a json dictionary."""
        args = {}
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = channels
        else:
            raise ValueError('Required property \'channels\' not present in PreferenceValueWithUpdates JSON')
        if (updates := _dict.get('updates')) is not None:
            args['updates'] = updates
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PreferenceValueWithUpdates object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channels') and self.channels is not None:
            _dict['channels'] = self.channels
        if hasattr(self, 'updates') and self.updates is not None:
            _dict['updates'] = self.updates
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PreferenceValueWithUpdates object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PreferenceValueWithUpdates') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PreferenceValueWithUpdates') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ChannelsEnum(str, Enum):
        """
        channels.
        """

        EMAIL = 'email'


class PreferenceValueWithoutUpdates:
    """
    Preference settings for notification types that do not support updates.

    :param List[str] channels: Array of communication channels for this preference.
    """

    def __init__(
        self,
        channels: List[str],
    ) -> None:
        """
        Initialize a PreferenceValueWithoutUpdates object.

        :param List[str] channels: Array of communication channels for this
               preference.
        """
        self.channels = channels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PreferenceValueWithoutUpdates':
        """Initialize a PreferenceValueWithoutUpdates object from a json dictionary."""
        args = {}
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = channels
        else:
            raise ValueError('Required property \'channels\' not present in PreferenceValueWithoutUpdates JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PreferenceValueWithoutUpdates object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channels') and self.channels is not None:
            _dict['channels'] = self.channels
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PreferenceValueWithoutUpdates object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PreferenceValueWithoutUpdates') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PreferenceValueWithoutUpdates') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ChannelsEnum(str, Enum):
        """
        channels.
        """

        EMAIL = 'email'


class PreferencesObject:
    """
    User communication preferences object. Only include preferences where communication is
    desired; absence of a key means no communication for that preference type.

    :param PreferenceValueWithUpdates incident_severity1: (optional) Preference
          settings for notification types that support updates.
    :param PreferenceValueWithUpdates incident_severity2: (optional) Preference
          settings for notification types that support updates.
    :param PreferenceValueWithUpdates incident_severity3: (optional) Preference
          settings for notification types that support updates.
    :param PreferenceValueWithUpdates incident_severity4: (optional) Preference
          settings for notification types that support updates.
    :param PreferenceValueWithUpdates maintenance_high: (optional) Preference
          settings for notification types that support updates.
    :param PreferenceValueWithUpdates maintenance_medium: (optional) Preference
          settings for notification types that support updates.
    :param PreferenceValueWithUpdates maintenance_low: (optional) Preference
          settings for notification types that support updates.
    :param PreferenceValueWithoutUpdates announcements_major: (optional) Preference
          settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates announcements_minor: (optional) Preference
          settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates security_normal: (optional) Preference
          settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates account_normal: (optional) Preference
          settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates billing_and_usage_order: (optional)
          Preference settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates billing_and_usage_invoices: (optional)
          Preference settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates billing_and_usage_payments: (optional)
          Preference settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates
          billing_and_usage_subscriptions_and_promo_codes: (optional) Preference settings
          for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates billing_and_usage_spending_alerts:
          (optional) Preference settings for notification types that do not support
          updates.
    :param PreferenceValueWithoutUpdates resourceactivity_normal: (optional)
          Preference settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates ordering_review: (optional) Preference
          settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates ordering_approved: (optional) Preference
          settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates ordering_approved_vsi: (optional)
          Preference settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates ordering_approved_server: (optional)
          Preference settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates provisioning_reload_complete: (optional)
          Preference settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates provisioning_complete_vsi: (optional)
          Preference settings for notification types that do not support updates.
    :param PreferenceValueWithoutUpdates provisioning_complete_server: (optional)
          Preference settings for notification types that do not support updates.
    """

    def __init__(
        self,
        *,
        incident_severity1: Optional['PreferenceValueWithUpdates'] = None,
        incident_severity2: Optional['PreferenceValueWithUpdates'] = None,
        incident_severity3: Optional['PreferenceValueWithUpdates'] = None,
        incident_severity4: Optional['PreferenceValueWithUpdates'] = None,
        maintenance_high: Optional['PreferenceValueWithUpdates'] = None,
        maintenance_medium: Optional['PreferenceValueWithUpdates'] = None,
        maintenance_low: Optional['PreferenceValueWithUpdates'] = None,
        announcements_major: Optional['PreferenceValueWithoutUpdates'] = None,
        announcements_minor: Optional['PreferenceValueWithoutUpdates'] = None,
        security_normal: Optional['PreferenceValueWithoutUpdates'] = None,
        account_normal: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_order: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_invoices: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_payments: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_subscriptions_and_promo_codes: Optional['PreferenceValueWithoutUpdates'] = None,
        billing_and_usage_spending_alerts: Optional['PreferenceValueWithoutUpdates'] = None,
        resourceactivity_normal: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_review: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_approved: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_approved_vsi: Optional['PreferenceValueWithoutUpdates'] = None,
        ordering_approved_server: Optional['PreferenceValueWithoutUpdates'] = None,
        provisioning_reload_complete: Optional['PreferenceValueWithoutUpdates'] = None,
        provisioning_complete_vsi: Optional['PreferenceValueWithoutUpdates'] = None,
        provisioning_complete_server: Optional['PreferenceValueWithoutUpdates'] = None,
    ) -> None:
        """
        Initialize a PreferencesObject object.

        :param PreferenceValueWithUpdates incident_severity1: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates incident_severity2: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates incident_severity3: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates incident_severity4: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates maintenance_high: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates maintenance_medium: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithUpdates maintenance_low: (optional) Preference
               settings for notification types that support updates.
        :param PreferenceValueWithoutUpdates announcements_major: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates announcements_minor: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates security_normal: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates account_normal: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_order: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_invoices: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_payments: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates
               billing_and_usage_subscriptions_and_promo_codes: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates billing_and_usage_spending_alerts:
               (optional) Preference settings for notification types that do not support
               updates.
        :param PreferenceValueWithoutUpdates resourceactivity_normal: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_review: (optional) Preference
               settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_approved: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_approved_vsi: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates ordering_approved_server: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates provisioning_reload_complete:
               (optional) Preference settings for notification types that do not support
               updates.
        :param PreferenceValueWithoutUpdates provisioning_complete_vsi: (optional)
               Preference settings for notification types that do not support updates.
        :param PreferenceValueWithoutUpdates provisioning_complete_server:
               (optional) Preference settings for notification types that do not support
               updates.
        """
        self.incident_severity1 = incident_severity1
        self.incident_severity2 = incident_severity2
        self.incident_severity3 = incident_severity3
        self.incident_severity4 = incident_severity4
        self.maintenance_high = maintenance_high
        self.maintenance_medium = maintenance_medium
        self.maintenance_low = maintenance_low
        self.announcements_major = announcements_major
        self.announcements_minor = announcements_minor
        self.security_normal = security_normal
        self.account_normal = account_normal
        self.billing_and_usage_order = billing_and_usage_order
        self.billing_and_usage_invoices = billing_and_usage_invoices
        self.billing_and_usage_payments = billing_and_usage_payments
        self.billing_and_usage_subscriptions_and_promo_codes = billing_and_usage_subscriptions_and_promo_codes
        self.billing_and_usage_spending_alerts = billing_and_usage_spending_alerts
        self.resourceactivity_normal = resourceactivity_normal
        self.ordering_review = ordering_review
        self.ordering_approved = ordering_approved
        self.ordering_approved_vsi = ordering_approved_vsi
        self.ordering_approved_server = ordering_approved_server
        self.provisioning_reload_complete = provisioning_reload_complete
        self.provisioning_complete_vsi = provisioning_complete_vsi
        self.provisioning_complete_server = provisioning_complete_server

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PreferencesObject':
        """Initialize a PreferencesObject object from a json dictionary."""
        args = {}
        if (incident_severity1 := _dict.get('incident_severity1')) is not None:
            args['incident_severity1'] = PreferenceValueWithUpdates.from_dict(incident_severity1)
        if (incident_severity2 := _dict.get('incident_severity2')) is not None:
            args['incident_severity2'] = PreferenceValueWithUpdates.from_dict(incident_severity2)
        if (incident_severity3 := _dict.get('incident_severity3')) is not None:
            args['incident_severity3'] = PreferenceValueWithUpdates.from_dict(incident_severity3)
        if (incident_severity4 := _dict.get('incident_severity4')) is not None:
            args['incident_severity4'] = PreferenceValueWithUpdates.from_dict(incident_severity4)
        if (maintenance_high := _dict.get('maintenance_high')) is not None:
            args['maintenance_high'] = PreferenceValueWithUpdates.from_dict(maintenance_high)
        if (maintenance_medium := _dict.get('maintenance_medium')) is not None:
            args['maintenance_medium'] = PreferenceValueWithUpdates.from_dict(maintenance_medium)
        if (maintenance_low := _dict.get('maintenance_low')) is not None:
            args['maintenance_low'] = PreferenceValueWithUpdates.from_dict(maintenance_low)
        if (announcements_major := _dict.get('announcements_major')) is not None:
            args['announcements_major'] = PreferenceValueWithoutUpdates.from_dict(announcements_major)
        if (announcements_minor := _dict.get('announcements_minor')) is not None:
            args['announcements_minor'] = PreferenceValueWithoutUpdates.from_dict(announcements_minor)
        if (security_normal := _dict.get('security_normal')) is not None:
            args['security_normal'] = PreferenceValueWithoutUpdates.from_dict(security_normal)
        if (account_normal := _dict.get('account_normal')) is not None:
            args['account_normal'] = PreferenceValueWithoutUpdates.from_dict(account_normal)
        if (billing_and_usage_order := _dict.get('billing_and_usage_order')) is not None:
            args['billing_and_usage_order'] = PreferenceValueWithoutUpdates.from_dict(billing_and_usage_order)
        if (billing_and_usage_invoices := _dict.get('billing_and_usage_invoices')) is not None:
            args['billing_and_usage_invoices'] = PreferenceValueWithoutUpdates.from_dict(billing_and_usage_invoices)
        if (billing_and_usage_payments := _dict.get('billing_and_usage_payments')) is not None:
            args['billing_and_usage_payments'] = PreferenceValueWithoutUpdates.from_dict(billing_and_usage_payments)
        if (
            billing_and_usage_subscriptions_and_promo_codes := _dict.get(
                'billing_and_usage_subscriptions_and_promo_codes'
            )
        ) is not None:
            args['billing_and_usage_subscriptions_and_promo_codes'] = PreferenceValueWithoutUpdates.from_dict(
                billing_and_usage_subscriptions_and_promo_codes
            )
        if (billing_and_usage_spending_alerts := _dict.get('billing_and_usage_spending_alerts')) is not None:
            args['billing_and_usage_spending_alerts'] = PreferenceValueWithoutUpdates.from_dict(
                billing_and_usage_spending_alerts
            )
        if (resourceactivity_normal := _dict.get('resourceactivity_normal')) is not None:
            args['resourceactivity_normal'] = PreferenceValueWithoutUpdates.from_dict(resourceactivity_normal)
        if (ordering_review := _dict.get('ordering_review')) is not None:
            args['ordering_review'] = PreferenceValueWithoutUpdates.from_dict(ordering_review)
        if (ordering_approved := _dict.get('ordering_approved')) is not None:
            args['ordering_approved'] = PreferenceValueWithoutUpdates.from_dict(ordering_approved)
        if (ordering_approved_vsi := _dict.get('ordering_approved_vsi')) is not None:
            args['ordering_approved_vsi'] = PreferenceValueWithoutUpdates.from_dict(ordering_approved_vsi)
        if (ordering_approved_server := _dict.get('ordering_approved_server')) is not None:
            args['ordering_approved_server'] = PreferenceValueWithoutUpdates.from_dict(ordering_approved_server)
        if (provisioning_reload_complete := _dict.get('provisioning_reload_complete')) is not None:
            args['provisioning_reload_complete'] = PreferenceValueWithoutUpdates.from_dict(provisioning_reload_complete)
        if (provisioning_complete_vsi := _dict.get('provisioning_complete_vsi')) is not None:
            args['provisioning_complete_vsi'] = PreferenceValueWithoutUpdates.from_dict(provisioning_complete_vsi)
        if (provisioning_complete_server := _dict.get('provisioning_complete_server')) is not None:
            args['provisioning_complete_server'] = PreferenceValueWithoutUpdates.from_dict(provisioning_complete_server)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PreferencesObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'incident_severity1') and self.incident_severity1 is not None:
            if isinstance(self.incident_severity1, dict):
                _dict['incident_severity1'] = self.incident_severity1
            else:
                _dict['incident_severity1'] = self.incident_severity1.to_dict()
        if hasattr(self, 'incident_severity2') and self.incident_severity2 is not None:
            if isinstance(self.incident_severity2, dict):
                _dict['incident_severity2'] = self.incident_severity2
            else:
                _dict['incident_severity2'] = self.incident_severity2.to_dict()
        if hasattr(self, 'incident_severity3') and self.incident_severity3 is not None:
            if isinstance(self.incident_severity3, dict):
                _dict['incident_severity3'] = self.incident_severity3
            else:
                _dict['incident_severity3'] = self.incident_severity3.to_dict()
        if hasattr(self, 'incident_severity4') and self.incident_severity4 is not None:
            if isinstance(self.incident_severity4, dict):
                _dict['incident_severity4'] = self.incident_severity4
            else:
                _dict['incident_severity4'] = self.incident_severity4.to_dict()
        if hasattr(self, 'maintenance_high') and self.maintenance_high is not None:
            if isinstance(self.maintenance_high, dict):
                _dict['maintenance_high'] = self.maintenance_high
            else:
                _dict['maintenance_high'] = self.maintenance_high.to_dict()
        if hasattr(self, 'maintenance_medium') and self.maintenance_medium is not None:
            if isinstance(self.maintenance_medium, dict):
                _dict['maintenance_medium'] = self.maintenance_medium
            else:
                _dict['maintenance_medium'] = self.maintenance_medium.to_dict()
        if hasattr(self, 'maintenance_low') and self.maintenance_low is not None:
            if isinstance(self.maintenance_low, dict):
                _dict['maintenance_low'] = self.maintenance_low
            else:
                _dict['maintenance_low'] = self.maintenance_low.to_dict()
        if hasattr(self, 'announcements_major') and self.announcements_major is not None:
            if isinstance(self.announcements_major, dict):
                _dict['announcements_major'] = self.announcements_major
            else:
                _dict['announcements_major'] = self.announcements_major.to_dict()
        if hasattr(self, 'announcements_minor') and self.announcements_minor is not None:
            if isinstance(self.announcements_minor, dict):
                _dict['announcements_minor'] = self.announcements_minor
            else:
                _dict['announcements_minor'] = self.announcements_minor.to_dict()
        if hasattr(self, 'security_normal') and self.security_normal is not None:
            if isinstance(self.security_normal, dict):
                _dict['security_normal'] = self.security_normal
            else:
                _dict['security_normal'] = self.security_normal.to_dict()
        if hasattr(self, 'account_normal') and self.account_normal is not None:
            if isinstance(self.account_normal, dict):
                _dict['account_normal'] = self.account_normal
            else:
                _dict['account_normal'] = self.account_normal.to_dict()
        if hasattr(self, 'billing_and_usage_order') and self.billing_and_usage_order is not None:
            if isinstance(self.billing_and_usage_order, dict):
                _dict['billing_and_usage_order'] = self.billing_and_usage_order
            else:
                _dict['billing_and_usage_order'] = self.billing_and_usage_order.to_dict()
        if hasattr(self, 'billing_and_usage_invoices') and self.billing_and_usage_invoices is not None:
            if isinstance(self.billing_and_usage_invoices, dict):
                _dict['billing_and_usage_invoices'] = self.billing_and_usage_invoices
            else:
                _dict['billing_and_usage_invoices'] = self.billing_and_usage_invoices.to_dict()
        if hasattr(self, 'billing_and_usage_payments') and self.billing_and_usage_payments is not None:
            if isinstance(self.billing_and_usage_payments, dict):
                _dict['billing_and_usage_payments'] = self.billing_and_usage_payments
            else:
                _dict['billing_and_usage_payments'] = self.billing_and_usage_payments.to_dict()
        if (
            hasattr(self, 'billing_and_usage_subscriptions_and_promo_codes')
            and self.billing_and_usage_subscriptions_and_promo_codes is not None
        ):
            if isinstance(self.billing_and_usage_subscriptions_and_promo_codes, dict):
                _dict['billing_and_usage_subscriptions_and_promo_codes'] = (
                    self.billing_and_usage_subscriptions_and_promo_codes
                )
            else:
                _dict['billing_and_usage_subscriptions_and_promo_codes'] = (
                    self.billing_and_usage_subscriptions_and_promo_codes.to_dict()
                )
        if hasattr(self, 'billing_and_usage_spending_alerts') and self.billing_and_usage_spending_alerts is not None:
            if isinstance(self.billing_and_usage_spending_alerts, dict):
                _dict['billing_and_usage_spending_alerts'] = self.billing_and_usage_spending_alerts
            else:
                _dict['billing_and_usage_spending_alerts'] = self.billing_and_usage_spending_alerts.to_dict()
        if hasattr(self, 'resourceactivity_normal') and self.resourceactivity_normal is not None:
            if isinstance(self.resourceactivity_normal, dict):
                _dict['resourceactivity_normal'] = self.resourceactivity_normal
            else:
                _dict['resourceactivity_normal'] = self.resourceactivity_normal.to_dict()
        if hasattr(self, 'ordering_review') and self.ordering_review is not None:
            if isinstance(self.ordering_review, dict):
                _dict['ordering_review'] = self.ordering_review
            else:
                _dict['ordering_review'] = self.ordering_review.to_dict()
        if hasattr(self, 'ordering_approved') and self.ordering_approved is not None:
            if isinstance(self.ordering_approved, dict):
                _dict['ordering_approved'] = self.ordering_approved
            else:
                _dict['ordering_approved'] = self.ordering_approved.to_dict()
        if hasattr(self, 'ordering_approved_vsi') and self.ordering_approved_vsi is not None:
            if isinstance(self.ordering_approved_vsi, dict):
                _dict['ordering_approved_vsi'] = self.ordering_approved_vsi
            else:
                _dict['ordering_approved_vsi'] = self.ordering_approved_vsi.to_dict()
        if hasattr(self, 'ordering_approved_server') and self.ordering_approved_server is not None:
            if isinstance(self.ordering_approved_server, dict):
                _dict['ordering_approved_server'] = self.ordering_approved_server
            else:
                _dict['ordering_approved_server'] = self.ordering_approved_server.to_dict()
        if hasattr(self, 'provisioning_reload_complete') and self.provisioning_reload_complete is not None:
            if isinstance(self.provisioning_reload_complete, dict):
                _dict['provisioning_reload_complete'] = self.provisioning_reload_complete
            else:
                _dict['provisioning_reload_complete'] = self.provisioning_reload_complete.to_dict()
        if hasattr(self, 'provisioning_complete_vsi') and self.provisioning_complete_vsi is not None:
            if isinstance(self.provisioning_complete_vsi, dict):
                _dict['provisioning_complete_vsi'] = self.provisioning_complete_vsi
            else:
                _dict['provisioning_complete_vsi'] = self.provisioning_complete_vsi.to_dict()
        if hasattr(self, 'provisioning_complete_server') and self.provisioning_complete_server is not None:
            if isinstance(self.provisioning_complete_server, dict):
                _dict['provisioning_complete_server'] = self.provisioning_complete_server
            else:
                _dict['provisioning_complete_server'] = self.provisioning_complete_server.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PreferencesObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PreferencesObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PreferencesObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TestDestinationRequestBodyPrototype:
    """
    TestDestinationRequestBodyPrototype.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a TestDestinationRequestBodyPrototype object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype'])
        )
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TestDestinationRequestBodyPrototype':
        """Initialize a TestDestinationRequestBodyPrototype object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = "Cannot convert dictionary into an instance of base class 'TestDestinationRequestBodyPrototype'. The discriminator value should map to a valid subclass: {1}".format(
            ", ".join(['TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype'])
        )
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a TestDestinationRequestBodyPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['event_notifications'] = (
            'TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype'
        )
        disc_value = _dict.get('destination_type')
        if disc_value is None:
            raise ValueError(
                'Discriminator property \'destination_type\' not found in TestDestinationRequestBodyPrototype JSON'
            )
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)


class TestDestinationResponseBody:
    """
    Response from the test notification endpoint.

    :param str message: The status message that indicates the test result.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initialize a TestDestinationResponseBody object.

        :param str message: The status message that indicates the test result.
        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TestDestinationResponseBody':
        """Initialize a TestDestinationResponseBody object from a json dictionary."""
        args = {}
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        else:
            raise ValueError('Required property \'message\' not present in TestDestinationResponseBody JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TestDestinationResponseBody object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TestDestinationResponseBody object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TestDestinationResponseBody') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TestDestinationResponseBody') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AddDestinationPrototypeEventNotificationDestinationPrototype(AddDestinationPrototype):
    """
    Prototype for creating an Event Notifications destination entry.

    :param str destination_id: The GUID of the Event Notifications instance.
    :param str destination_type: The type of the destination.
    """

    def __init__(
        self,
        destination_id: str,
        destination_type: str,
    ) -> None:
        """
        Initialize a AddDestinationPrototypeEventNotificationDestinationPrototype object.

        :param str destination_id: The GUID of the Event Notifications instance.
        :param str destination_type: The type of the destination.
        """
        # pylint: disable=super-init-not-called
        self.destination_id = destination_id
        self.destination_type = destination_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddDestinationPrototypeEventNotificationDestinationPrototype':
        """Initialize a AddDestinationPrototypeEventNotificationDestinationPrototype object from a json dictionary."""
        args = {}
        if (destination_id := _dict.get('destination_id')) is not None:
            args['destination_id'] = destination_id
        else:
            raise ValueError(
                'Required property \'destination_id\' not present in AddDestinationPrototypeEventNotificationDestinationPrototype JSON'
            )
        if (destination_type := _dict.get('destination_type')) is not None:
            args['destination_type'] = destination_type
        else:
            raise ValueError(
                'Required property \'destination_type\' not present in AddDestinationPrototypeEventNotificationDestinationPrototype JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddDestinationPrototypeEventNotificationDestinationPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'destination_id') and self.destination_id is not None:
            _dict['destination_id'] = self.destination_id
        if hasattr(self, 'destination_type') and self.destination_type is not None:
            _dict['destination_type'] = self.destination_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddDestinationPrototypeEventNotificationDestinationPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddDestinationPrototypeEventNotificationDestinationPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddDestinationPrototypeEventNotificationDestinationPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DestinationTypeEnum(str, Enum):
        """
        The type of the destination.
        """

        EVENT_NOTIFICATIONS = 'event_notifications'


class AddDestinationEventNotificationDestination(AddDestination):
    """
    An Event Notifications destination entry in the distribution list.

    :param str destination_id: The GUID of the Event Notifications instance.
    :param str destination_type: The type of the destination.
    """

    def __init__(
        self,
        destination_id: str,
        destination_type: str,
    ) -> None:
        """
        Initialize a AddDestinationEventNotificationDestination object.

        :param str destination_id: The GUID of the Event Notifications instance.
        :param str destination_type: The type of the destination.
        """
        # pylint: disable=super-init-not-called
        self.destination_id = destination_id
        self.destination_type = destination_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddDestinationEventNotificationDestination':
        """Initialize a AddDestinationEventNotificationDestination object from a json dictionary."""
        args = {}
        if (destination_id := _dict.get('destination_id')) is not None:
            args['destination_id'] = destination_id
        else:
            raise ValueError(
                'Required property \'destination_id\' not present in AddDestinationEventNotificationDestination JSON'
            )
        if (destination_type := _dict.get('destination_type')) is not None:
            args['destination_type'] = destination_type
        else:
            raise ValueError(
                'Required property \'destination_type\' not present in AddDestinationEventNotificationDestination JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddDestinationEventNotificationDestination object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'destination_id') and self.destination_id is not None:
            _dict['destination_id'] = self.destination_id
        if hasattr(self, 'destination_type') and self.destination_type is not None:
            _dict['destination_type'] = self.destination_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddDestinationEventNotificationDestination object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddDestinationEventNotificationDestination') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddDestinationEventNotificationDestination') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DestinationTypeEnum(str, Enum):
        """
        The type of the destination.
        """

        EVENT_NOTIFICATIONS = 'event_notifications'


class TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype(
    TestDestinationRequestBodyPrototype
):
    """
    Request body for testing an Event Notifications destination.

    :param str destination_type: The type of the destination.
    :param str notification_type: The type of the notification to test.
    """

    def __init__(
        self,
        destination_type: str,
        notification_type: str,
    ) -> None:
        """
        Initialize a TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype object.

        :param str destination_type: The type of the destination.
        :param str notification_type: The type of the notification to test.
        """
        # pylint: disable=super-init-not-called
        self.destination_type = destination_type
        self.notification_type = notification_type

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype':
        """Initialize a TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype object from a json dictionary."""
        args = {}
        if (destination_type := _dict.get('destination_type')) is not None:
            args['destination_type'] = destination_type
        else:
            raise ValueError(
                'Required property \'destination_type\' not present in TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype JSON'
            )
        if (notification_type := _dict.get('notification_type')) is not None:
            args['notification_type'] = notification_type
        else:
            raise ValueError(
                'Required property \'notification_type\' not present in TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'destination_type') and self.destination_type is not None:
            _dict['destination_type'] = self.destination_type
        if hasattr(self, 'notification_type') and self.notification_type is not None:
            _dict['notification_type'] = self.notification_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DestinationTypeEnum(str, Enum):
        """
        The type of the destination.
        """

        EVENT_NOTIFICATIONS = 'event_notifications'

    class NotificationTypeEnum(str, Enum):
        """
        The type of the notification to test.
        """

        INCIDENT = 'incident'
        ANNOUNCEMENTS = 'announcements'
        MAINTENANCE = 'maintenance'
        SECURITY_BULLETINS = 'security_bulletins'
        RESOURCE = 'resource'
        BILLING_AND_USAGE = 'billing_and_usage'


##############################################################################
# Pagers
##############################################################################


class NotificationsPager:
    """
    NotificationsPager can be used to simplify the use of the "list_notifications" method.
    """

    def __init__(
        self,
        *,
        client: PlatformNotificationsV1,
        account_id: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a NotificationsPager object.
        :param str account_id: (optional) The IBM Cloud account ID. If not
               provided, the account ID from the bearer token will be used.
        :param int limit: (optional) The maximum number of items to return per
               page. If unspecified, a default limit of 50 is used.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._account_id = account_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Notification.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_notifications(
            account_id=self._account_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('notifications')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Notification.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
