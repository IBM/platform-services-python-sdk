# -*- coding: utf-8 -*-
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

"""
Unit Tests for PlatformNotificationsV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.platform_notifications_v1 import *


_service = PlatformNotificationsV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://notifications.cloud.ibm.com/api'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: DistributionLists
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PlatformNotificationsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PlatformNotificationsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PlatformNotificationsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListDistributionListDestinations:
    """
    Test Class for list_distribution_list_destinations
    """

    @responses.activate
    def test_list_distribution_list_destinations_all_params(self):
        """
        list_distribution_list_destinations()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations')
        mock_response = '{"destinations": [{"destination_id": "12345678-1234-1234-1234-123456789012", "destination_type": "event_notifications"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'

        # Invoke method
        response = _service.list_distribution_list_destinations(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_distribution_list_destinations_all_params_with_retries(self):
        # Enable retries and run test_list_distribution_list_destinations_all_params.
        _service.enable_retries()
        self.test_list_distribution_list_destinations_all_params()

        # Disable retries and run test_list_distribution_list_destinations_all_params.
        _service.disable_retries()
        self.test_list_distribution_list_destinations_all_params()

    @responses.activate
    def test_list_distribution_list_destinations_value_error(self):
        """
        test_list_distribution_list_destinations_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations')
        mock_response = '{"destinations": [{"destination_id": "12345678-1234-1234-1234-123456789012", "destination_type": "event_notifications"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_distribution_list_destinations(**req_copy)

    def test_list_distribution_list_destinations_value_error_with_retries(self):
        # Enable retries and run test_list_distribution_list_destinations_value_error.
        _service.enable_retries()
        self.test_list_distribution_list_destinations_value_error()

        # Disable retries and run test_list_distribution_list_destinations_value_error.
        _service.disable_retries()
        self.test_list_distribution_list_destinations_value_error()


class TestCreateDistributionListDestination:
    """
    Test Class for create_distribution_list_destination
    """

    @responses.activate
    def test_create_distribution_list_destination_all_params(self):
        """
        create_distribution_list_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations')
        mock_response = '{"destination_id": "12345678-1234-1234-1234-123456789012", "destination_type": "event_notifications"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AddDestinationPrototypeEventNotificationDestinationPrototype model
        add_destination_prototype_model = {}
        add_destination_prototype_model['destination_id'] = '12345678-1234-1234-1234-123456789012'
        add_destination_prototype_model['destination_type'] = 'event_notifications'

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        add_destination_prototype = add_destination_prototype_model

        # Invoke method
        response = _service.create_distribution_list_destination(
            account_id,
            add_destination_prototype,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == add_destination_prototype

    def test_create_distribution_list_destination_all_params_with_retries(self):
        # Enable retries and run test_create_distribution_list_destination_all_params.
        _service.enable_retries()
        self.test_create_distribution_list_destination_all_params()

        # Disable retries and run test_create_distribution_list_destination_all_params.
        _service.disable_retries()
        self.test_create_distribution_list_destination_all_params()

    @responses.activate
    def test_create_distribution_list_destination_value_error(self):
        """
        test_create_distribution_list_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations')
        mock_response = '{"destination_id": "12345678-1234-1234-1234-123456789012", "destination_type": "event_notifications"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AddDestinationPrototypeEventNotificationDestinationPrototype model
        add_destination_prototype_model = {}
        add_destination_prototype_model['destination_id'] = '12345678-1234-1234-1234-123456789012'
        add_destination_prototype_model['destination_type'] = 'event_notifications'

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        add_destination_prototype = add_destination_prototype_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "add_destination_prototype": add_destination_prototype,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_distribution_list_destination(**req_copy)

    def test_create_distribution_list_destination_value_error_with_retries(self):
        # Enable retries and run test_create_distribution_list_destination_value_error.
        _service.enable_retries()
        self.test_create_distribution_list_destination_value_error()

        # Disable retries and run test_create_distribution_list_destination_value_error.
        _service.disable_retries()
        self.test_create_distribution_list_destination_value_error()


class TestGetDistributionListDestination:
    """
    Test Class for get_distribution_list_destination
    """

    @responses.activate
    def test_get_distribution_list_destination_all_params(self):
        """
        get_distribution_list_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations/12345678-1234-1234-1234-123456789012')
        mock_response = '{"destination_id": "12345678-1234-1234-1234-123456789012", "destination_type": "event_notifications"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        destination_id = '12345678-1234-1234-1234-123456789012'

        # Invoke method
        response = _service.get_distribution_list_destination(
            account_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_distribution_list_destination_all_params_with_retries(self):
        # Enable retries and run test_get_distribution_list_destination_all_params.
        _service.enable_retries()
        self.test_get_distribution_list_destination_all_params()

        # Disable retries and run test_get_distribution_list_destination_all_params.
        _service.disable_retries()
        self.test_get_distribution_list_destination_all_params()

    @responses.activate
    def test_get_distribution_list_destination_value_error(self):
        """
        test_get_distribution_list_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations/12345678-1234-1234-1234-123456789012')
        mock_response = '{"destination_id": "12345678-1234-1234-1234-123456789012", "destination_type": "event_notifications"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        destination_id = '12345678-1234-1234-1234-123456789012'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_distribution_list_destination(**req_copy)

    def test_get_distribution_list_destination_value_error_with_retries(self):
        # Enable retries and run test_get_distribution_list_destination_value_error.
        _service.enable_retries()
        self.test_get_distribution_list_destination_value_error()

        # Disable retries and run test_get_distribution_list_destination_value_error.
        _service.disable_retries()
        self.test_get_distribution_list_destination_value_error()


class TestDeleteDistributionListDestination:
    """
    Test Class for delete_distribution_list_destination
    """

    @responses.activate
    def test_delete_distribution_list_destination_all_params(self):
        """
        delete_distribution_list_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations/12345678-1234-1234-1234-123456789012')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        destination_id = '12345678-1234-1234-1234-123456789012'

        # Invoke method
        response = _service.delete_distribution_list_destination(
            account_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_distribution_list_destination_all_params_with_retries(self):
        # Enable retries and run test_delete_distribution_list_destination_all_params.
        _service.enable_retries()
        self.test_delete_distribution_list_destination_all_params()

        # Disable retries and run test_delete_distribution_list_destination_all_params.
        _service.disable_retries()
        self.test_delete_distribution_list_destination_all_params()

    @responses.activate
    def test_delete_distribution_list_destination_value_error(self):
        """
        test_delete_distribution_list_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations/12345678-1234-1234-1234-123456789012')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        destination_id = '12345678-1234-1234-1234-123456789012'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_distribution_list_destination(**req_copy)

    def test_delete_distribution_list_destination_value_error_with_retries(self):
        # Enable retries and run test_delete_distribution_list_destination_value_error.
        _service.enable_retries()
        self.test_delete_distribution_list_destination_value_error()

        # Disable retries and run test_delete_distribution_list_destination_value_error.
        _service.disable_retries()
        self.test_delete_distribution_list_destination_value_error()


class TestTestDistributionListDestination:
    """
    Test Class for test_distribution_list_destination
    """

    @responses.activate
    def test_test_distribution_list_destination_all_params(self):
        """
        test_distribution_list_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations/12345678-1234-1234-1234-123456789012/test')
        mock_response = '{"message": "success"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype model
        test_destination_request_body_prototype_model = {}
        test_destination_request_body_prototype_model['destination_type'] = 'event_notifications'
        test_destination_request_body_prototype_model['notification_type'] = 'incident'

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        destination_id = '12345678-1234-1234-1234-123456789012'
        test_destination_request_body_prototype = test_destination_request_body_prototype_model

        # Invoke method
        response = _service.test_distribution_list_destination(
            account_id,
            destination_id,
            test_destination_request_body_prototype,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == test_destination_request_body_prototype

    def test_test_distribution_list_destination_all_params_with_retries(self):
        # Enable retries and run test_test_distribution_list_destination_all_params.
        _service.enable_retries()
        self.test_test_distribution_list_destination_all_params()

        # Disable retries and run test_test_distribution_list_destination_all_params.
        _service.disable_retries()
        self.test_test_distribution_list_destination_all_params()

    @responses.activate
    def test_test_distribution_list_destination_value_error(self):
        """
        test_test_distribution_list_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/distribution_lists/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6/destinations/12345678-1234-1234-1234-123456789012/test')
        mock_response = '{"message": "success"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype model
        test_destination_request_body_prototype_model = {}
        test_destination_request_body_prototype_model['destination_type'] = 'event_notifications'
        test_destination_request_body_prototype_model['notification_type'] = 'incident'

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        destination_id = '12345678-1234-1234-1234-123456789012'
        test_destination_request_body_prototype = test_destination_request_body_prototype_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "destination_id": destination_id,
            "test_destination_request_body_prototype": test_destination_request_body_prototype,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.test_distribution_list_destination(**req_copy)

    def test_test_distribution_list_destination_value_error_with_retries(self):
        # Enable retries and run test_test_distribution_list_destination_value_error.
        _service.enable_retries()
        self.test_test_distribution_list_destination_value_error()

        # Disable retries and run test_test_distribution_list_destination_value_error.
        _service.disable_retries()
        self.test_test_distribution_list_destination_value_error()


# endregion
##############################################################################
# End of Service: DistributionLists
##############################################################################

##############################################################################
# Start of Service: UserPreferences
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PlatformNotificationsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PlatformNotificationsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PlatformNotificationsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreatePreferences:
    """
    Test Class for create_preferences
    """

    @responses.activate
    def test_create_preferences_all_params(self):
        """
        create_preferences()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        mock_response = '{"incident_severity1": {"channels": ["email"], "updates": true}, "incident_severity2": {"channels": ["email"], "updates": true}, "incident_severity3": {"channels": ["email"], "updates": true}, "incident_severity4": {"channels": ["email"], "updates": true}, "maintenance_high": {"channels": ["email"], "updates": true}, "maintenance_medium": {"channels": ["email"], "updates": true}, "maintenance_low": {"channels": ["email"], "updates": true}, "announcements_major": {"channels": ["email"]}, "announcements_minor": {"channels": ["email"]}, "security_normal": {"channels": ["email"]}, "account_normal": {"channels": ["email"]}, "billing_and_usage_order": {"channels": ["email"]}, "billing_and_usage_invoices": {"channels": ["email"]}, "billing_and_usage_payments": {"channels": ["email"]}, "billing_and_usage_subscriptions_and_promo_codes": {"channels": ["email"]}, "billing_and_usage_spending_alerts": {"channels": ["email"]}, "resourceactivity_normal": {"channels": ["email"]}, "ordering_review": {"channels": ["email"]}, "ordering_approved": {"channels": ["email"]}, "ordering_approved_vsi": {"channels": ["email"]}, "ordering_approved_server": {"channels": ["email"]}, "provisioning_reload_complete": {"channels": ["email"]}, "provisioning_complete_vsi": {"channels": ["email"]}, "provisioning_complete_server": {"channels": ["email"]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a PreferenceValueWithUpdates model
        preference_value_with_updates_model = {}
        preference_value_with_updates_model['channels'] = ['email']
        preference_value_with_updates_model['updates'] = True

        # Construct a dict representation of a PreferenceValueWithoutUpdates model
        preference_value_without_updates_model = {}
        preference_value_without_updates_model['channels'] = ['email']

        # Set up parameter values
        iam_id = 'IBMid-1234567890'
        incident_severity1 = preference_value_with_updates_model
        incident_severity2 = preference_value_with_updates_model
        incident_severity3 = preference_value_with_updates_model
        incident_severity4 = preference_value_with_updates_model
        maintenance_high = preference_value_with_updates_model
        maintenance_medium = preference_value_with_updates_model
        maintenance_low = preference_value_with_updates_model
        announcements_major = preference_value_without_updates_model
        announcements_minor = preference_value_without_updates_model
        security_normal = preference_value_without_updates_model
        account_normal = preference_value_without_updates_model
        billing_and_usage_order = preference_value_without_updates_model
        billing_and_usage_invoices = preference_value_without_updates_model
        billing_and_usage_payments = preference_value_without_updates_model
        billing_and_usage_subscriptions_and_promo_codes = preference_value_without_updates_model
        billing_and_usage_spending_alerts = preference_value_without_updates_model
        resourceactivity_normal = preference_value_without_updates_model
        ordering_review = preference_value_without_updates_model
        ordering_approved = preference_value_without_updates_model
        ordering_approved_vsi = preference_value_without_updates_model
        ordering_approved_server = preference_value_without_updates_model
        provisioning_reload_complete = preference_value_without_updates_model
        provisioning_complete_vsi = preference_value_without_updates_model
        provisioning_complete_server = preference_value_without_updates_model
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'

        # Invoke method
        response = _service.create_preferences(
            iam_id,
            incident_severity1=incident_severity1,
            incident_severity2=incident_severity2,
            incident_severity3=incident_severity3,
            incident_severity4=incident_severity4,
            maintenance_high=maintenance_high,
            maintenance_medium=maintenance_medium,
            maintenance_low=maintenance_low,
            announcements_major=announcements_major,
            announcements_minor=announcements_minor,
            security_normal=security_normal,
            account_normal=account_normal,
            billing_and_usage_order=billing_and_usage_order,
            billing_and_usage_invoices=billing_and_usage_invoices,
            billing_and_usage_payments=billing_and_usage_payments,
            billing_and_usage_subscriptions_and_promo_codes=billing_and_usage_subscriptions_and_promo_codes,
            billing_and_usage_spending_alerts=billing_and_usage_spending_alerts,
            resourceactivity_normal=resourceactivity_normal,
            ordering_review=ordering_review,
            ordering_approved=ordering_approved,
            ordering_approved_vsi=ordering_approved_vsi,
            ordering_approved_server=ordering_approved_server,
            provisioning_reload_complete=provisioning_reload_complete,
            provisioning_complete_vsi=provisioning_complete_vsi,
            provisioning_complete_server=provisioning_complete_server,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['incident_severity1'] == preference_value_with_updates_model
        assert req_body['incident_severity2'] == preference_value_with_updates_model
        assert req_body['incident_severity3'] == preference_value_with_updates_model
        assert req_body['incident_severity4'] == preference_value_with_updates_model
        assert req_body['maintenance_high'] == preference_value_with_updates_model
        assert req_body['maintenance_medium'] == preference_value_with_updates_model
        assert req_body['maintenance_low'] == preference_value_with_updates_model
        assert req_body['announcements_major'] == preference_value_without_updates_model
        assert req_body['announcements_minor'] == preference_value_without_updates_model
        assert req_body['security_normal'] == preference_value_without_updates_model
        assert req_body['account_normal'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_order'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_invoices'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_payments'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_subscriptions_and_promo_codes'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_spending_alerts'] == preference_value_without_updates_model
        assert req_body['resourceactivity_normal'] == preference_value_without_updates_model
        assert req_body['ordering_review'] == preference_value_without_updates_model
        assert req_body['ordering_approved'] == preference_value_without_updates_model
        assert req_body['ordering_approved_vsi'] == preference_value_without_updates_model
        assert req_body['ordering_approved_server'] == preference_value_without_updates_model
        assert req_body['provisioning_reload_complete'] == preference_value_without_updates_model
        assert req_body['provisioning_complete_vsi'] == preference_value_without_updates_model
        assert req_body['provisioning_complete_server'] == preference_value_without_updates_model

    def test_create_preferences_all_params_with_retries(self):
        # Enable retries and run test_create_preferences_all_params.
        _service.enable_retries()
        self.test_create_preferences_all_params()

        # Disable retries and run test_create_preferences_all_params.
        _service.disable_retries()
        self.test_create_preferences_all_params()

    @responses.activate
    def test_create_preferences_required_params(self):
        """
        test_create_preferences_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        mock_response = '{"incident_severity1": {"channels": ["email"], "updates": true}, "incident_severity2": {"channels": ["email"], "updates": true}, "incident_severity3": {"channels": ["email"], "updates": true}, "incident_severity4": {"channels": ["email"], "updates": true}, "maintenance_high": {"channels": ["email"], "updates": true}, "maintenance_medium": {"channels": ["email"], "updates": true}, "maintenance_low": {"channels": ["email"], "updates": true}, "announcements_major": {"channels": ["email"]}, "announcements_minor": {"channels": ["email"]}, "security_normal": {"channels": ["email"]}, "account_normal": {"channels": ["email"]}, "billing_and_usage_order": {"channels": ["email"]}, "billing_and_usage_invoices": {"channels": ["email"]}, "billing_and_usage_payments": {"channels": ["email"]}, "billing_and_usage_subscriptions_and_promo_codes": {"channels": ["email"]}, "billing_and_usage_spending_alerts": {"channels": ["email"]}, "resourceactivity_normal": {"channels": ["email"]}, "ordering_review": {"channels": ["email"]}, "ordering_approved": {"channels": ["email"]}, "ordering_approved_vsi": {"channels": ["email"]}, "ordering_approved_server": {"channels": ["email"]}, "provisioning_reload_complete": {"channels": ["email"]}, "provisioning_complete_vsi": {"channels": ["email"]}, "provisioning_complete_server": {"channels": ["email"]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a PreferenceValueWithUpdates model
        preference_value_with_updates_model = {}
        preference_value_with_updates_model['channels'] = ['email']
        preference_value_with_updates_model['updates'] = True

        # Construct a dict representation of a PreferenceValueWithoutUpdates model
        preference_value_without_updates_model = {}
        preference_value_without_updates_model['channels'] = ['email']

        # Set up parameter values
        iam_id = 'IBMid-1234567890'
        incident_severity1 = preference_value_with_updates_model
        incident_severity2 = preference_value_with_updates_model
        incident_severity3 = preference_value_with_updates_model
        incident_severity4 = preference_value_with_updates_model
        maintenance_high = preference_value_with_updates_model
        maintenance_medium = preference_value_with_updates_model
        maintenance_low = preference_value_with_updates_model
        announcements_major = preference_value_without_updates_model
        announcements_minor = preference_value_without_updates_model
        security_normal = preference_value_without_updates_model
        account_normal = preference_value_without_updates_model
        billing_and_usage_order = preference_value_without_updates_model
        billing_and_usage_invoices = preference_value_without_updates_model
        billing_and_usage_payments = preference_value_without_updates_model
        billing_and_usage_subscriptions_and_promo_codes = preference_value_without_updates_model
        billing_and_usage_spending_alerts = preference_value_without_updates_model
        resourceactivity_normal = preference_value_without_updates_model
        ordering_review = preference_value_without_updates_model
        ordering_approved = preference_value_without_updates_model
        ordering_approved_vsi = preference_value_without_updates_model
        ordering_approved_server = preference_value_without_updates_model
        provisioning_reload_complete = preference_value_without_updates_model
        provisioning_complete_vsi = preference_value_without_updates_model
        provisioning_complete_server = preference_value_without_updates_model

        # Invoke method
        response = _service.create_preferences(
            iam_id,
            incident_severity1=incident_severity1,
            incident_severity2=incident_severity2,
            incident_severity3=incident_severity3,
            incident_severity4=incident_severity4,
            maintenance_high=maintenance_high,
            maintenance_medium=maintenance_medium,
            maintenance_low=maintenance_low,
            announcements_major=announcements_major,
            announcements_minor=announcements_minor,
            security_normal=security_normal,
            account_normal=account_normal,
            billing_and_usage_order=billing_and_usage_order,
            billing_and_usage_invoices=billing_and_usage_invoices,
            billing_and_usage_payments=billing_and_usage_payments,
            billing_and_usage_subscriptions_and_promo_codes=billing_and_usage_subscriptions_and_promo_codes,
            billing_and_usage_spending_alerts=billing_and_usage_spending_alerts,
            resourceactivity_normal=resourceactivity_normal,
            ordering_review=ordering_review,
            ordering_approved=ordering_approved,
            ordering_approved_vsi=ordering_approved_vsi,
            ordering_approved_server=ordering_approved_server,
            provisioning_reload_complete=provisioning_reload_complete,
            provisioning_complete_vsi=provisioning_complete_vsi,
            provisioning_complete_server=provisioning_complete_server,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['incident_severity1'] == preference_value_with_updates_model
        assert req_body['incident_severity2'] == preference_value_with_updates_model
        assert req_body['incident_severity3'] == preference_value_with_updates_model
        assert req_body['incident_severity4'] == preference_value_with_updates_model
        assert req_body['maintenance_high'] == preference_value_with_updates_model
        assert req_body['maintenance_medium'] == preference_value_with_updates_model
        assert req_body['maintenance_low'] == preference_value_with_updates_model
        assert req_body['announcements_major'] == preference_value_without_updates_model
        assert req_body['announcements_minor'] == preference_value_without_updates_model
        assert req_body['security_normal'] == preference_value_without_updates_model
        assert req_body['account_normal'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_order'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_invoices'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_payments'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_subscriptions_and_promo_codes'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_spending_alerts'] == preference_value_without_updates_model
        assert req_body['resourceactivity_normal'] == preference_value_without_updates_model
        assert req_body['ordering_review'] == preference_value_without_updates_model
        assert req_body['ordering_approved'] == preference_value_without_updates_model
        assert req_body['ordering_approved_vsi'] == preference_value_without_updates_model
        assert req_body['ordering_approved_server'] == preference_value_without_updates_model
        assert req_body['provisioning_reload_complete'] == preference_value_without_updates_model
        assert req_body['provisioning_complete_vsi'] == preference_value_without_updates_model
        assert req_body['provisioning_complete_server'] == preference_value_without_updates_model

    def test_create_preferences_required_params_with_retries(self):
        # Enable retries and run test_create_preferences_required_params.
        _service.enable_retries()
        self.test_create_preferences_required_params()

        # Disable retries and run test_create_preferences_required_params.
        _service.disable_retries()
        self.test_create_preferences_required_params()

    @responses.activate
    def test_create_preferences_value_error(self):
        """
        test_create_preferences_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        mock_response = '{"incident_severity1": {"channels": ["email"], "updates": true}, "incident_severity2": {"channels": ["email"], "updates": true}, "incident_severity3": {"channels": ["email"], "updates": true}, "incident_severity4": {"channels": ["email"], "updates": true}, "maintenance_high": {"channels": ["email"], "updates": true}, "maintenance_medium": {"channels": ["email"], "updates": true}, "maintenance_low": {"channels": ["email"], "updates": true}, "announcements_major": {"channels": ["email"]}, "announcements_minor": {"channels": ["email"]}, "security_normal": {"channels": ["email"]}, "account_normal": {"channels": ["email"]}, "billing_and_usage_order": {"channels": ["email"]}, "billing_and_usage_invoices": {"channels": ["email"]}, "billing_and_usage_payments": {"channels": ["email"]}, "billing_and_usage_subscriptions_and_promo_codes": {"channels": ["email"]}, "billing_and_usage_spending_alerts": {"channels": ["email"]}, "resourceactivity_normal": {"channels": ["email"]}, "ordering_review": {"channels": ["email"]}, "ordering_approved": {"channels": ["email"]}, "ordering_approved_vsi": {"channels": ["email"]}, "ordering_approved_server": {"channels": ["email"]}, "provisioning_reload_complete": {"channels": ["email"]}, "provisioning_complete_vsi": {"channels": ["email"]}, "provisioning_complete_server": {"channels": ["email"]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a PreferenceValueWithUpdates model
        preference_value_with_updates_model = {}
        preference_value_with_updates_model['channels'] = ['email']
        preference_value_with_updates_model['updates'] = True

        # Construct a dict representation of a PreferenceValueWithoutUpdates model
        preference_value_without_updates_model = {}
        preference_value_without_updates_model['channels'] = ['email']

        # Set up parameter values
        iam_id = 'IBMid-1234567890'
        incident_severity1 = preference_value_with_updates_model
        incident_severity2 = preference_value_with_updates_model
        incident_severity3 = preference_value_with_updates_model
        incident_severity4 = preference_value_with_updates_model
        maintenance_high = preference_value_with_updates_model
        maintenance_medium = preference_value_with_updates_model
        maintenance_low = preference_value_with_updates_model
        announcements_major = preference_value_without_updates_model
        announcements_minor = preference_value_without_updates_model
        security_normal = preference_value_without_updates_model
        account_normal = preference_value_without_updates_model
        billing_and_usage_order = preference_value_without_updates_model
        billing_and_usage_invoices = preference_value_without_updates_model
        billing_and_usage_payments = preference_value_without_updates_model
        billing_and_usage_subscriptions_and_promo_codes = preference_value_without_updates_model
        billing_and_usage_spending_alerts = preference_value_without_updates_model
        resourceactivity_normal = preference_value_without_updates_model
        ordering_review = preference_value_without_updates_model
        ordering_approved = preference_value_without_updates_model
        ordering_approved_vsi = preference_value_without_updates_model
        ordering_approved_server = preference_value_without_updates_model
        provisioning_reload_complete = preference_value_without_updates_model
        provisioning_complete_vsi = preference_value_without_updates_model
        provisioning_complete_server = preference_value_without_updates_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_preferences(**req_copy)

    def test_create_preferences_value_error_with_retries(self):
        # Enable retries and run test_create_preferences_value_error.
        _service.enable_retries()
        self.test_create_preferences_value_error()

        # Disable retries and run test_create_preferences_value_error.
        _service.disable_retries()
        self.test_create_preferences_value_error()


class TestGetPreferences:
    """
    Test Class for get_preferences
    """

    @responses.activate
    def test_get_preferences_all_params(self):
        """
        get_preferences()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        mock_response = '{"incident_severity1": {"channels": ["email"], "updates": true}, "incident_severity2": {"channels": ["email"], "updates": true}, "incident_severity3": {"channels": ["email"], "updates": true}, "incident_severity4": {"channels": ["email"], "updates": true}, "maintenance_high": {"channels": ["email"], "updates": true}, "maintenance_medium": {"channels": ["email"], "updates": true}, "maintenance_low": {"channels": ["email"], "updates": true}, "announcements_major": {"channels": ["email"]}, "announcements_minor": {"channels": ["email"]}, "security_normal": {"channels": ["email"]}, "account_normal": {"channels": ["email"]}, "billing_and_usage_order": {"channels": ["email"]}, "billing_and_usage_invoices": {"channels": ["email"]}, "billing_and_usage_payments": {"channels": ["email"]}, "billing_and_usage_subscriptions_and_promo_codes": {"channels": ["email"]}, "billing_and_usage_spending_alerts": {"channels": ["email"]}, "resourceactivity_normal": {"channels": ["email"]}, "ordering_review": {"channels": ["email"]}, "ordering_approved": {"channels": ["email"]}, "ordering_approved_vsi": {"channels": ["email"]}, "ordering_approved_server": {"channels": ["email"]}, "provisioning_reload_complete": {"channels": ["email"]}, "provisioning_complete_vsi": {"channels": ["email"]}, "provisioning_complete_server": {"channels": ["email"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        iam_id = 'IBMid-1234567890'
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'

        # Invoke method
        response = _service.get_preferences(
            iam_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_get_preferences_all_params_with_retries(self):
        # Enable retries and run test_get_preferences_all_params.
        _service.enable_retries()
        self.test_get_preferences_all_params()

        # Disable retries and run test_get_preferences_all_params.
        _service.disable_retries()
        self.test_get_preferences_all_params()

    @responses.activate
    def test_get_preferences_required_params(self):
        """
        test_get_preferences_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        mock_response = '{"incident_severity1": {"channels": ["email"], "updates": true}, "incident_severity2": {"channels": ["email"], "updates": true}, "incident_severity3": {"channels": ["email"], "updates": true}, "incident_severity4": {"channels": ["email"], "updates": true}, "maintenance_high": {"channels": ["email"], "updates": true}, "maintenance_medium": {"channels": ["email"], "updates": true}, "maintenance_low": {"channels": ["email"], "updates": true}, "announcements_major": {"channels": ["email"]}, "announcements_minor": {"channels": ["email"]}, "security_normal": {"channels": ["email"]}, "account_normal": {"channels": ["email"]}, "billing_and_usage_order": {"channels": ["email"]}, "billing_and_usage_invoices": {"channels": ["email"]}, "billing_and_usage_payments": {"channels": ["email"]}, "billing_and_usage_subscriptions_and_promo_codes": {"channels": ["email"]}, "billing_and_usage_spending_alerts": {"channels": ["email"]}, "resourceactivity_normal": {"channels": ["email"]}, "ordering_review": {"channels": ["email"]}, "ordering_approved": {"channels": ["email"]}, "ordering_approved_vsi": {"channels": ["email"]}, "ordering_approved_server": {"channels": ["email"]}, "provisioning_reload_complete": {"channels": ["email"]}, "provisioning_complete_vsi": {"channels": ["email"]}, "provisioning_complete_server": {"channels": ["email"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        iam_id = 'IBMid-1234567890'

        # Invoke method
        response = _service.get_preferences(
            iam_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_preferences_required_params_with_retries(self):
        # Enable retries and run test_get_preferences_required_params.
        _service.enable_retries()
        self.test_get_preferences_required_params()

        # Disable retries and run test_get_preferences_required_params.
        _service.disable_retries()
        self.test_get_preferences_required_params()

    @responses.activate
    def test_get_preferences_value_error(self):
        """
        test_get_preferences_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        mock_response = '{"incident_severity1": {"channels": ["email"], "updates": true}, "incident_severity2": {"channels": ["email"], "updates": true}, "incident_severity3": {"channels": ["email"], "updates": true}, "incident_severity4": {"channels": ["email"], "updates": true}, "maintenance_high": {"channels": ["email"], "updates": true}, "maintenance_medium": {"channels": ["email"], "updates": true}, "maintenance_low": {"channels": ["email"], "updates": true}, "announcements_major": {"channels": ["email"]}, "announcements_minor": {"channels": ["email"]}, "security_normal": {"channels": ["email"]}, "account_normal": {"channels": ["email"]}, "billing_and_usage_order": {"channels": ["email"]}, "billing_and_usage_invoices": {"channels": ["email"]}, "billing_and_usage_payments": {"channels": ["email"]}, "billing_and_usage_subscriptions_and_promo_codes": {"channels": ["email"]}, "billing_and_usage_spending_alerts": {"channels": ["email"]}, "resourceactivity_normal": {"channels": ["email"]}, "ordering_review": {"channels": ["email"]}, "ordering_approved": {"channels": ["email"]}, "ordering_approved_vsi": {"channels": ["email"]}, "ordering_approved_server": {"channels": ["email"]}, "provisioning_reload_complete": {"channels": ["email"]}, "provisioning_complete_vsi": {"channels": ["email"]}, "provisioning_complete_server": {"channels": ["email"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        iam_id = 'IBMid-1234567890'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_preferences(**req_copy)

    def test_get_preferences_value_error_with_retries(self):
        # Enable retries and run test_get_preferences_value_error.
        _service.enable_retries()
        self.test_get_preferences_value_error()

        # Disable retries and run test_get_preferences_value_error.
        _service.disable_retries()
        self.test_get_preferences_value_error()


class TestReplaceNotificationPreferences:
    """
    Test Class for replace_notification_preferences
    """

    @responses.activate
    def test_replace_notification_preferences_all_params(self):
        """
        replace_notification_preferences()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        mock_response = '{"incident_severity1": {"channels": ["email"], "updates": true}, "incident_severity2": {"channels": ["email"], "updates": true}, "incident_severity3": {"channels": ["email"], "updates": true}, "incident_severity4": {"channels": ["email"], "updates": true}, "maintenance_high": {"channels": ["email"], "updates": true}, "maintenance_medium": {"channels": ["email"], "updates": true}, "maintenance_low": {"channels": ["email"], "updates": true}, "announcements_major": {"channels": ["email"]}, "announcements_minor": {"channels": ["email"]}, "security_normal": {"channels": ["email"]}, "account_normal": {"channels": ["email"]}, "billing_and_usage_order": {"channels": ["email"]}, "billing_and_usage_invoices": {"channels": ["email"]}, "billing_and_usage_payments": {"channels": ["email"]}, "billing_and_usage_subscriptions_and_promo_codes": {"channels": ["email"]}, "billing_and_usage_spending_alerts": {"channels": ["email"]}, "resourceactivity_normal": {"channels": ["email"]}, "ordering_review": {"channels": ["email"]}, "ordering_approved": {"channels": ["email"]}, "ordering_approved_vsi": {"channels": ["email"]}, "ordering_approved_server": {"channels": ["email"]}, "provisioning_reload_complete": {"channels": ["email"]}, "provisioning_complete_vsi": {"channels": ["email"]}, "provisioning_complete_server": {"channels": ["email"]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PreferenceValueWithUpdates model
        preference_value_with_updates_model = {}
        preference_value_with_updates_model['channels'] = ['email']
        preference_value_with_updates_model['updates'] = True

        # Construct a dict representation of a PreferenceValueWithoutUpdates model
        preference_value_without_updates_model = {}
        preference_value_without_updates_model['channels'] = ['email']

        # Set up parameter values
        iam_id = 'IBMid-1234567890'
        incident_severity1 = preference_value_with_updates_model
        incident_severity2 = preference_value_with_updates_model
        incident_severity3 = preference_value_with_updates_model
        incident_severity4 = preference_value_with_updates_model
        maintenance_high = preference_value_with_updates_model
        maintenance_medium = preference_value_with_updates_model
        maintenance_low = preference_value_with_updates_model
        announcements_major = preference_value_without_updates_model
        announcements_minor = preference_value_without_updates_model
        security_normal = preference_value_without_updates_model
        account_normal = preference_value_without_updates_model
        billing_and_usage_order = preference_value_without_updates_model
        billing_and_usage_invoices = preference_value_without_updates_model
        billing_and_usage_payments = preference_value_without_updates_model
        billing_and_usage_subscriptions_and_promo_codes = preference_value_without_updates_model
        billing_and_usage_spending_alerts = preference_value_without_updates_model
        resourceactivity_normal = preference_value_without_updates_model
        ordering_review = preference_value_without_updates_model
        ordering_approved = preference_value_without_updates_model
        ordering_approved_vsi = preference_value_without_updates_model
        ordering_approved_server = preference_value_without_updates_model
        provisioning_reload_complete = preference_value_without_updates_model
        provisioning_complete_vsi = preference_value_without_updates_model
        provisioning_complete_server = preference_value_without_updates_model
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'

        # Invoke method
        response = _service.replace_notification_preferences(
            iam_id,
            incident_severity1=incident_severity1,
            incident_severity2=incident_severity2,
            incident_severity3=incident_severity3,
            incident_severity4=incident_severity4,
            maintenance_high=maintenance_high,
            maintenance_medium=maintenance_medium,
            maintenance_low=maintenance_low,
            announcements_major=announcements_major,
            announcements_minor=announcements_minor,
            security_normal=security_normal,
            account_normal=account_normal,
            billing_and_usage_order=billing_and_usage_order,
            billing_and_usage_invoices=billing_and_usage_invoices,
            billing_and_usage_payments=billing_and_usage_payments,
            billing_and_usage_subscriptions_and_promo_codes=billing_and_usage_subscriptions_and_promo_codes,
            billing_and_usage_spending_alerts=billing_and_usage_spending_alerts,
            resourceactivity_normal=resourceactivity_normal,
            ordering_review=ordering_review,
            ordering_approved=ordering_approved,
            ordering_approved_vsi=ordering_approved_vsi,
            ordering_approved_server=ordering_approved_server,
            provisioning_reload_complete=provisioning_reload_complete,
            provisioning_complete_vsi=provisioning_complete_vsi,
            provisioning_complete_server=provisioning_complete_server,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['incident_severity1'] == preference_value_with_updates_model
        assert req_body['incident_severity2'] == preference_value_with_updates_model
        assert req_body['incident_severity3'] == preference_value_with_updates_model
        assert req_body['incident_severity4'] == preference_value_with_updates_model
        assert req_body['maintenance_high'] == preference_value_with_updates_model
        assert req_body['maintenance_medium'] == preference_value_with_updates_model
        assert req_body['maintenance_low'] == preference_value_with_updates_model
        assert req_body['announcements_major'] == preference_value_without_updates_model
        assert req_body['announcements_minor'] == preference_value_without_updates_model
        assert req_body['security_normal'] == preference_value_without_updates_model
        assert req_body['account_normal'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_order'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_invoices'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_payments'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_subscriptions_and_promo_codes'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_spending_alerts'] == preference_value_without_updates_model
        assert req_body['resourceactivity_normal'] == preference_value_without_updates_model
        assert req_body['ordering_review'] == preference_value_without_updates_model
        assert req_body['ordering_approved'] == preference_value_without_updates_model
        assert req_body['ordering_approved_vsi'] == preference_value_without_updates_model
        assert req_body['ordering_approved_server'] == preference_value_without_updates_model
        assert req_body['provisioning_reload_complete'] == preference_value_without_updates_model
        assert req_body['provisioning_complete_vsi'] == preference_value_without_updates_model
        assert req_body['provisioning_complete_server'] == preference_value_without_updates_model

    def test_replace_notification_preferences_all_params_with_retries(self):
        # Enable retries and run test_replace_notification_preferences_all_params.
        _service.enable_retries()
        self.test_replace_notification_preferences_all_params()

        # Disable retries and run test_replace_notification_preferences_all_params.
        _service.disable_retries()
        self.test_replace_notification_preferences_all_params()

    @responses.activate
    def test_replace_notification_preferences_required_params(self):
        """
        test_replace_notification_preferences_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        mock_response = '{"incident_severity1": {"channels": ["email"], "updates": true}, "incident_severity2": {"channels": ["email"], "updates": true}, "incident_severity3": {"channels": ["email"], "updates": true}, "incident_severity4": {"channels": ["email"], "updates": true}, "maintenance_high": {"channels": ["email"], "updates": true}, "maintenance_medium": {"channels": ["email"], "updates": true}, "maintenance_low": {"channels": ["email"], "updates": true}, "announcements_major": {"channels": ["email"]}, "announcements_minor": {"channels": ["email"]}, "security_normal": {"channels": ["email"]}, "account_normal": {"channels": ["email"]}, "billing_and_usage_order": {"channels": ["email"]}, "billing_and_usage_invoices": {"channels": ["email"]}, "billing_and_usage_payments": {"channels": ["email"]}, "billing_and_usage_subscriptions_and_promo_codes": {"channels": ["email"]}, "billing_and_usage_spending_alerts": {"channels": ["email"]}, "resourceactivity_normal": {"channels": ["email"]}, "ordering_review": {"channels": ["email"]}, "ordering_approved": {"channels": ["email"]}, "ordering_approved_vsi": {"channels": ["email"]}, "ordering_approved_server": {"channels": ["email"]}, "provisioning_reload_complete": {"channels": ["email"]}, "provisioning_complete_vsi": {"channels": ["email"]}, "provisioning_complete_server": {"channels": ["email"]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PreferenceValueWithUpdates model
        preference_value_with_updates_model = {}
        preference_value_with_updates_model['channels'] = ['email']
        preference_value_with_updates_model['updates'] = True

        # Construct a dict representation of a PreferenceValueWithoutUpdates model
        preference_value_without_updates_model = {}
        preference_value_without_updates_model['channels'] = ['email']

        # Set up parameter values
        iam_id = 'IBMid-1234567890'
        incident_severity1 = preference_value_with_updates_model
        incident_severity2 = preference_value_with_updates_model
        incident_severity3 = preference_value_with_updates_model
        incident_severity4 = preference_value_with_updates_model
        maintenance_high = preference_value_with_updates_model
        maintenance_medium = preference_value_with_updates_model
        maintenance_low = preference_value_with_updates_model
        announcements_major = preference_value_without_updates_model
        announcements_minor = preference_value_without_updates_model
        security_normal = preference_value_without_updates_model
        account_normal = preference_value_without_updates_model
        billing_and_usage_order = preference_value_without_updates_model
        billing_and_usage_invoices = preference_value_without_updates_model
        billing_and_usage_payments = preference_value_without_updates_model
        billing_and_usage_subscriptions_and_promo_codes = preference_value_without_updates_model
        billing_and_usage_spending_alerts = preference_value_without_updates_model
        resourceactivity_normal = preference_value_without_updates_model
        ordering_review = preference_value_without_updates_model
        ordering_approved = preference_value_without_updates_model
        ordering_approved_vsi = preference_value_without_updates_model
        ordering_approved_server = preference_value_without_updates_model
        provisioning_reload_complete = preference_value_without_updates_model
        provisioning_complete_vsi = preference_value_without_updates_model
        provisioning_complete_server = preference_value_without_updates_model

        # Invoke method
        response = _service.replace_notification_preferences(
            iam_id,
            incident_severity1=incident_severity1,
            incident_severity2=incident_severity2,
            incident_severity3=incident_severity3,
            incident_severity4=incident_severity4,
            maintenance_high=maintenance_high,
            maintenance_medium=maintenance_medium,
            maintenance_low=maintenance_low,
            announcements_major=announcements_major,
            announcements_minor=announcements_minor,
            security_normal=security_normal,
            account_normal=account_normal,
            billing_and_usage_order=billing_and_usage_order,
            billing_and_usage_invoices=billing_and_usage_invoices,
            billing_and_usage_payments=billing_and_usage_payments,
            billing_and_usage_subscriptions_and_promo_codes=billing_and_usage_subscriptions_and_promo_codes,
            billing_and_usage_spending_alerts=billing_and_usage_spending_alerts,
            resourceactivity_normal=resourceactivity_normal,
            ordering_review=ordering_review,
            ordering_approved=ordering_approved,
            ordering_approved_vsi=ordering_approved_vsi,
            ordering_approved_server=ordering_approved_server,
            provisioning_reload_complete=provisioning_reload_complete,
            provisioning_complete_vsi=provisioning_complete_vsi,
            provisioning_complete_server=provisioning_complete_server,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['incident_severity1'] == preference_value_with_updates_model
        assert req_body['incident_severity2'] == preference_value_with_updates_model
        assert req_body['incident_severity3'] == preference_value_with_updates_model
        assert req_body['incident_severity4'] == preference_value_with_updates_model
        assert req_body['maintenance_high'] == preference_value_with_updates_model
        assert req_body['maintenance_medium'] == preference_value_with_updates_model
        assert req_body['maintenance_low'] == preference_value_with_updates_model
        assert req_body['announcements_major'] == preference_value_without_updates_model
        assert req_body['announcements_minor'] == preference_value_without_updates_model
        assert req_body['security_normal'] == preference_value_without_updates_model
        assert req_body['account_normal'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_order'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_invoices'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_payments'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_subscriptions_and_promo_codes'] == preference_value_without_updates_model
        assert req_body['billing_and_usage_spending_alerts'] == preference_value_without_updates_model
        assert req_body['resourceactivity_normal'] == preference_value_without_updates_model
        assert req_body['ordering_review'] == preference_value_without_updates_model
        assert req_body['ordering_approved'] == preference_value_without_updates_model
        assert req_body['ordering_approved_vsi'] == preference_value_without_updates_model
        assert req_body['ordering_approved_server'] == preference_value_without_updates_model
        assert req_body['provisioning_reload_complete'] == preference_value_without_updates_model
        assert req_body['provisioning_complete_vsi'] == preference_value_without_updates_model
        assert req_body['provisioning_complete_server'] == preference_value_without_updates_model

    def test_replace_notification_preferences_required_params_with_retries(self):
        # Enable retries and run test_replace_notification_preferences_required_params.
        _service.enable_retries()
        self.test_replace_notification_preferences_required_params()

        # Disable retries and run test_replace_notification_preferences_required_params.
        _service.disable_retries()
        self.test_replace_notification_preferences_required_params()

    @responses.activate
    def test_replace_notification_preferences_value_error(self):
        """
        test_replace_notification_preferences_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        mock_response = '{"incident_severity1": {"channels": ["email"], "updates": true}, "incident_severity2": {"channels": ["email"], "updates": true}, "incident_severity3": {"channels": ["email"], "updates": true}, "incident_severity4": {"channels": ["email"], "updates": true}, "maintenance_high": {"channels": ["email"], "updates": true}, "maintenance_medium": {"channels": ["email"], "updates": true}, "maintenance_low": {"channels": ["email"], "updates": true}, "announcements_major": {"channels": ["email"]}, "announcements_minor": {"channels": ["email"]}, "security_normal": {"channels": ["email"]}, "account_normal": {"channels": ["email"]}, "billing_and_usage_order": {"channels": ["email"]}, "billing_and_usage_invoices": {"channels": ["email"]}, "billing_and_usage_payments": {"channels": ["email"]}, "billing_and_usage_subscriptions_and_promo_codes": {"channels": ["email"]}, "billing_and_usage_spending_alerts": {"channels": ["email"]}, "resourceactivity_normal": {"channels": ["email"]}, "ordering_review": {"channels": ["email"]}, "ordering_approved": {"channels": ["email"]}, "ordering_approved_vsi": {"channels": ["email"]}, "ordering_approved_server": {"channels": ["email"]}, "provisioning_reload_complete": {"channels": ["email"]}, "provisioning_complete_vsi": {"channels": ["email"]}, "provisioning_complete_server": {"channels": ["email"]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PreferenceValueWithUpdates model
        preference_value_with_updates_model = {}
        preference_value_with_updates_model['channels'] = ['email']
        preference_value_with_updates_model['updates'] = True

        # Construct a dict representation of a PreferenceValueWithoutUpdates model
        preference_value_without_updates_model = {}
        preference_value_without_updates_model['channels'] = ['email']

        # Set up parameter values
        iam_id = 'IBMid-1234567890'
        incident_severity1 = preference_value_with_updates_model
        incident_severity2 = preference_value_with_updates_model
        incident_severity3 = preference_value_with_updates_model
        incident_severity4 = preference_value_with_updates_model
        maintenance_high = preference_value_with_updates_model
        maintenance_medium = preference_value_with_updates_model
        maintenance_low = preference_value_with_updates_model
        announcements_major = preference_value_without_updates_model
        announcements_minor = preference_value_without_updates_model
        security_normal = preference_value_without_updates_model
        account_normal = preference_value_without_updates_model
        billing_and_usage_order = preference_value_without_updates_model
        billing_and_usage_invoices = preference_value_without_updates_model
        billing_and_usage_payments = preference_value_without_updates_model
        billing_and_usage_subscriptions_and_promo_codes = preference_value_without_updates_model
        billing_and_usage_spending_alerts = preference_value_without_updates_model
        resourceactivity_normal = preference_value_without_updates_model
        ordering_review = preference_value_without_updates_model
        ordering_approved = preference_value_without_updates_model
        ordering_approved_vsi = preference_value_without_updates_model
        ordering_approved_server = preference_value_without_updates_model
        provisioning_reload_complete = preference_value_without_updates_model
        provisioning_complete_vsi = preference_value_without_updates_model
        provisioning_complete_server = preference_value_without_updates_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_notification_preferences(**req_copy)

    def test_replace_notification_preferences_value_error_with_retries(self):
        # Enable retries and run test_replace_notification_preferences_value_error.
        _service.enable_retries()
        self.test_replace_notification_preferences_value_error()

        # Disable retries and run test_replace_notification_preferences_value_error.
        _service.disable_retries()
        self.test_replace_notification_preferences_value_error()


class TestDeleteNotificationPreferences:
    """
    Test Class for delete_notification_preferences
    """

    @responses.activate
    def test_delete_notification_preferences_all_params(self):
        """
        delete_notification_preferences()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        iam_id = 'IBMid-1234567890'
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'

        # Invoke method
        response = _service.delete_notification_preferences(
            iam_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_delete_notification_preferences_all_params_with_retries(self):
        # Enable retries and run test_delete_notification_preferences_all_params.
        _service.enable_retries()
        self.test_delete_notification_preferences_all_params()

        # Disable retries and run test_delete_notification_preferences_all_params.
        _service.disable_retries()
        self.test_delete_notification_preferences_all_params()

    @responses.activate
    def test_delete_notification_preferences_required_params(self):
        """
        test_delete_notification_preferences_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        iam_id = 'IBMid-1234567890'

        # Invoke method
        response = _service.delete_notification_preferences(
            iam_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_notification_preferences_required_params_with_retries(self):
        # Enable retries and run test_delete_notification_preferences_required_params.
        _service.enable_retries()
        self.test_delete_notification_preferences_required_params()

        # Disable retries and run test_delete_notification_preferences_required_params.
        _service.disable_retries()
        self.test_delete_notification_preferences_required_params()

    @responses.activate
    def test_delete_notification_preferences_value_error(self):
        """
        test_delete_notification_preferences_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/IBMid-1234567890/preferences')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        iam_id = 'IBMid-1234567890'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "iam_id": iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_notification_preferences(**req_copy)

    def test_delete_notification_preferences_value_error_with_retries(self):
        # Enable retries and run test_delete_notification_preferences_value_error.
        _service.enable_retries()
        self.test_delete_notification_preferences_value_error()

        # Disable retries and run test_delete_notification_preferences_value_error.
        _service.disable_retries()
        self.test_delete_notification_preferences_value_error()


# endregion
##############################################################################
# End of Service: UserPreferences
##############################################################################

##############################################################################
# Start of Service: Notifications
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PlatformNotificationsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PlatformNotificationsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PlatformNotificationsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListNotifications:
    """
    Test Class for list_notifications
    """

    @responses.activate
    def test_list_notifications_all_params(self):
        """
        list_notifications()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications')
        mock_response = '{"limit": 50, "total_count": 232, "first": {"href": "https://api.example.com/v1/notifications?limit=50"}, "previous": {"href": "https://api.example.com/v1/notifications?start=3fe78a36b9aa7f26&limit=50", "start": "3fe78a36b9aa7f26"}, "next": {"href": "https://api.example.com/v1/notifications?start=3fe78a36b9aa7f26&limit=50", "start": "3fe78a36b9aa7f26"}, "last": {"href": "https://api.example.com/v1/notifications?start=3fe78a36b9aa7f26&limit=50", "start": "3fe78a36b9aa7f26"}, "notifications": [{"title": "System Maintenance Scheduled", "body": "Scheduled maintenance will occur on March 15th from 10:00 AM to 11:00 AM UTC.", "id": "12345", "category": "maintenance", "component_names": ["component_names"], "start_time": 1771791490, "is_global": false, "state": "new", "regions": ["regions"], "crn_masks": ["crn_masks"], "record_id": "rec-67890", "source_id": "src-11111", "completion_code": "successful", "end_time": 1771791490, "update_time": 1771791490, "severity": 2, "lucene_query": "region:us-south AND service_name:event-notifications", "resource_link": "https://cloud.ibm.com/status/incident/12345"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        start = '3fe78a36b9aa7f26'
        limit = 50

        # Invoke method
        response = _service.list_notifications(
            account_id=account_id,
            start=start,
            limit=limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_notifications_all_params_with_retries(self):
        # Enable retries and run test_list_notifications_all_params.
        _service.enable_retries()
        self.test_list_notifications_all_params()

        # Disable retries and run test_list_notifications_all_params.
        _service.disable_retries()
        self.test_list_notifications_all_params()

    @responses.activate
    def test_list_notifications_required_params(self):
        """
        test_list_notifications_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications')
        mock_response = '{"limit": 50, "total_count": 232, "first": {"href": "https://api.example.com/v1/notifications?limit=50"}, "previous": {"href": "https://api.example.com/v1/notifications?start=3fe78a36b9aa7f26&limit=50", "start": "3fe78a36b9aa7f26"}, "next": {"href": "https://api.example.com/v1/notifications?start=3fe78a36b9aa7f26&limit=50", "start": "3fe78a36b9aa7f26"}, "last": {"href": "https://api.example.com/v1/notifications?start=3fe78a36b9aa7f26&limit=50", "start": "3fe78a36b9aa7f26"}, "notifications": [{"title": "System Maintenance Scheduled", "body": "Scheduled maintenance will occur on March 15th from 10:00 AM to 11:00 AM UTC.", "id": "12345", "category": "maintenance", "component_names": ["component_names"], "start_time": 1771791490, "is_global": false, "state": "new", "regions": ["regions"], "crn_masks": ["crn_masks"], "record_id": "rec-67890", "source_id": "src-11111", "completion_code": "successful", "end_time": 1771791490, "update_time": 1771791490, "severity": 2, "lucene_query": "region:us-south AND service_name:event-notifications", "resource_link": "https://cloud.ibm.com/status/incident/12345"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_notifications()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_notifications_required_params_with_retries(self):
        # Enable retries and run test_list_notifications_required_params.
        _service.enable_retries()
        self.test_list_notifications_required_params()

        # Disable retries and run test_list_notifications_required_params.
        _service.disable_retries()
        self.test_list_notifications_required_params()

    @responses.activate
    def test_list_notifications_with_pager_get_next(self):
        """
        test_list_notifications_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/notifications')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"notifications":[{"title":"System Maintenance Scheduled","body":"Scheduled maintenance will occur on March 15th from 10:00 AM to 11:00 AM UTC.","id":"12345","category":"maintenance","component_names":["component_names"],"start_time":1771791490,"is_global":false,"state":"new","regions":["regions"],"crn_masks":["crn_masks"],"record_id":"rec-67890","source_id":"src-11111","completion_code":"successful","end_time":1771791490,"update_time":1771791490,"severity":2,"lucene_query":"region:us-south AND service_name:event-notifications","resource_link":"https://cloud.ibm.com/status/incident/12345"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"notifications":[{"title":"System Maintenance Scheduled","body":"Scheduled maintenance will occur on March 15th from 10:00 AM to 11:00 AM UTC.","id":"12345","category":"maintenance","component_names":["component_names"],"start_time":1771791490,"is_global":false,"state":"new","regions":["regions"],"crn_masks":["crn_masks"],"record_id":"rec-67890","source_id":"src-11111","completion_code":"successful","end_time":1771791490,"update_time":1771791490,"severity":2,"lucene_query":"region:us-south AND service_name:event-notifications","resource_link":"https://cloud.ibm.com/status/incident/12345"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = NotificationsPager(
            client=_service,
            account_id='a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6',
            limit=50,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_notifications_with_pager_get_all(self):
        """
        test_list_notifications_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/notifications')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"notifications":[{"title":"System Maintenance Scheduled","body":"Scheduled maintenance will occur on March 15th from 10:00 AM to 11:00 AM UTC.","id":"12345","category":"maintenance","component_names":["component_names"],"start_time":1771791490,"is_global":false,"state":"new","regions":["regions"],"crn_masks":["crn_masks"],"record_id":"rec-67890","source_id":"src-11111","completion_code":"successful","end_time":1771791490,"update_time":1771791490,"severity":2,"lucene_query":"region:us-south AND service_name:event-notifications","resource_link":"https://cloud.ibm.com/status/incident/12345"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"notifications":[{"title":"System Maintenance Scheduled","body":"Scheduled maintenance will occur on March 15th from 10:00 AM to 11:00 AM UTC.","id":"12345","category":"maintenance","component_names":["component_names"],"start_time":1771791490,"is_global":false,"state":"new","regions":["regions"],"crn_masks":["crn_masks"],"record_id":"rec-67890","source_id":"src-11111","completion_code":"successful","end_time":1771791490,"update_time":1771791490,"severity":2,"lucene_query":"region:us-south AND service_name:event-notifications","resource_link":"https://cloud.ibm.com/status/incident/12345"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = NotificationsPager(
            client=_service,
            account_id='a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6',
            limit=50,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetAcknowledgement:
    """
    Test Class for get_acknowledgement
    """

    @responses.activate
    def test_get_acknowledgement_all_params(self):
        """
        get_acknowledgement()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/acknowledgement')
        mock_response = '{"has_unread": true, "latest_notification_id": "1678901234000", "last_acknowledged_id": "1678800000000"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = '1369339417d906e5620b8d861d40cfd7'

        # Invoke method
        response = _service.get_acknowledgement(
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_get_acknowledgement_all_params_with_retries(self):
        # Enable retries and run test_get_acknowledgement_all_params.
        _service.enable_retries()
        self.test_get_acknowledgement_all_params()

        # Disable retries and run test_get_acknowledgement_all_params.
        _service.disable_retries()
        self.test_get_acknowledgement_all_params()

    @responses.activate
    def test_get_acknowledgement_required_params(self):
        """
        test_get_acknowledgement_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/acknowledgement')
        mock_response = '{"has_unread": true, "latest_notification_id": "1678901234000", "last_acknowledged_id": "1678800000000"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_acknowledgement()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_acknowledgement_required_params_with_retries(self):
        # Enable retries and run test_get_acknowledgement_required_params.
        _service.enable_retries()
        self.test_get_acknowledgement_required_params()

        # Disable retries and run test_get_acknowledgement_required_params.
        _service.disable_retries()
        self.test_get_acknowledgement_required_params()


class TestReplaceNotificationAcknowledgement:
    """
    Test Class for replace_notification_acknowledgement
    """

    @responses.activate
    def test_replace_notification_acknowledgement_all_params(self):
        """
        replace_notification_acknowledgement()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/acknowledgement')
        mock_response = '{"has_unread": true, "latest_notification_id": "1678901234000", "last_acknowledged_id": "1678800000000"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        last_acknowledged_id = '1772804159452'
        account_id = '1369339417d906e5620b8d861d40cfd7'

        # Invoke method
        response = _service.replace_notification_acknowledgement(
            last_acknowledged_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['last_acknowledged_id'] == '1772804159452'

    def test_replace_notification_acknowledgement_all_params_with_retries(self):
        # Enable retries and run test_replace_notification_acknowledgement_all_params.
        _service.enable_retries()
        self.test_replace_notification_acknowledgement_all_params()

        # Disable retries and run test_replace_notification_acknowledgement_all_params.
        _service.disable_retries()
        self.test_replace_notification_acknowledgement_all_params()

    @responses.activate
    def test_replace_notification_acknowledgement_required_params(self):
        """
        test_replace_notification_acknowledgement_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/acknowledgement')
        mock_response = '{"has_unread": true, "latest_notification_id": "1678901234000", "last_acknowledged_id": "1678800000000"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        last_acknowledged_id = '1772804159452'

        # Invoke method
        response = _service.replace_notification_acknowledgement(
            last_acknowledged_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['last_acknowledged_id'] == '1772804159452'

    def test_replace_notification_acknowledgement_required_params_with_retries(self):
        # Enable retries and run test_replace_notification_acknowledgement_required_params.
        _service.enable_retries()
        self.test_replace_notification_acknowledgement_required_params()

        # Disable retries and run test_replace_notification_acknowledgement_required_params.
        _service.disable_retries()
        self.test_replace_notification_acknowledgement_required_params()

    @responses.activate
    def test_replace_notification_acknowledgement_value_error(self):
        """
        test_replace_notification_acknowledgement_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/notifications/acknowledgement')
        mock_response = '{"has_unread": true, "latest_notification_id": "1678901234000", "last_acknowledged_id": "1678800000000"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        last_acknowledged_id = '1772804159452'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "last_acknowledged_id": last_acknowledged_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_notification_acknowledgement(**req_copy)

    def test_replace_notification_acknowledgement_value_error_with_retries(self):
        # Enable retries and run test_replace_notification_acknowledgement_value_error.
        _service.enable_retries()
        self.test_replace_notification_acknowledgement_value_error()

        # Disable retries and run test_replace_notification_acknowledgement_value_error.
        _service.disable_retries()
        self.test_replace_notification_acknowledgement_value_error()


# endregion
##############################################################################
# End of Service: Notifications
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AddDestinationCollection:
    """
    Test Class for AddDestinationCollection
    """

    def test_add_destination_collection_serialization(self):
        """
        Test serialization/deserialization for AddDestinationCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        add_destination_model = {}  # AddDestinationEventNotificationDestination
        add_destination_model['destination_id'] = '12345678-1234-1234-1234-123456789012'
        add_destination_model['destination_type'] = 'event_notifications'

        # Construct a json representation of a AddDestinationCollection model
        add_destination_collection_model_json = {}
        add_destination_collection_model_json['destinations'] = [add_destination_model]

        # Construct a model instance of AddDestinationCollection by calling from_dict on the json representation
        add_destination_collection_model = AddDestinationCollection.from_dict(add_destination_collection_model_json)
        assert add_destination_collection_model != False

        # Construct a model instance of AddDestinationCollection by calling from_dict on the json representation
        add_destination_collection_model_dict = AddDestinationCollection.from_dict(add_destination_collection_model_json).__dict__
        add_destination_collection_model2 = AddDestinationCollection(**add_destination_collection_model_dict)

        # Verify the model instances are equivalent
        assert add_destination_collection_model == add_destination_collection_model2

        # Convert model instance back to dict and verify no loss of data
        add_destination_collection_model_json2 = add_destination_collection_model.to_dict()
        assert add_destination_collection_model_json2 == add_destination_collection_model_json


class TestModel_Notification:
    """
    Test Class for Notification
    """

    def test_notification_serialization(self):
        """
        Test serialization/deserialization for Notification
        """

        # Construct a json representation of a Notification model
        notification_model_json = {}
        notification_model_json['title'] = 'System Maintenance Scheduled'
        notification_model_json['body'] = 'Scheduled maintenance will occur on March 15th from 10:00 AM to 11:00 AM UTC.'
        notification_model_json['id'] = '12345'
        notification_model_json['category'] = 'maintenance'
        notification_model_json['component_names'] = ['event-notifications', 'ibm-cloud']
        notification_model_json['start_time'] = 1771791490
        notification_model_json['is_global'] = False
        notification_model_json['state'] = 'new'
        notification_model_json['regions'] = ['us-south', 'us-east']
        notification_model_json['crn_masks'] = ['crn:v1:staging:public:event-notifications:us-south:::']
        notification_model_json['record_id'] = 'rec-67890'
        notification_model_json['source_id'] = 'src-11111'
        notification_model_json['completion_code'] = 'successful'
        notification_model_json['end_time'] = 1771791490
        notification_model_json['update_time'] = 1771791490
        notification_model_json['severity'] = 2
        notification_model_json['lucene_query'] = 'region:us-south AND service_name:event-notifications'
        notification_model_json['resource_link'] = 'https://cloud.ibm.com/status/incident/12345'

        # Construct a model instance of Notification by calling from_dict on the json representation
        notification_model = Notification.from_dict(notification_model_json)
        assert notification_model != False

        # Construct a model instance of Notification by calling from_dict on the json representation
        notification_model_dict = Notification.from_dict(notification_model_json).__dict__
        notification_model2 = Notification(**notification_model_dict)

        # Verify the model instances are equivalent
        assert notification_model == notification_model2

        # Convert model instance back to dict and verify no loss of data
        notification_model_json2 = notification_model.to_dict()
        assert notification_model_json2 == notification_model_json


class TestModel_NotificationCollection:
    """
    Test Class for NotificationCollection
    """

    def test_notification_collection_serialization(self):
        """
        Test serialization/deserialization for NotificationCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pagination_link_model = {}  # PaginationLink
        pagination_link_model['href'] = 'https://api.example.com/v1/notifications?limit=50'

        pagination_link_with_token_model = {}  # PaginationLinkWithToken
        pagination_link_with_token_model['href'] = 'https://api.example.com/v1/notifications?start=3fe78a36b9aa7f26&limit=50'
        pagination_link_with_token_model['start'] = '3fe78a36b9aa7f26'

        notification_model = {}  # Notification
        notification_model['title'] = 'System Maintenance Scheduled'
        notification_model['body'] = 'Scheduled maintenance will occur on March 15th from 10:00 AM to 11:00 AM UTC.'
        notification_model['id'] = '12345'
        notification_model['category'] = 'maintenance'
        notification_model['component_names'] = ['event-notifications', 'ibm-cloud']
        notification_model['start_time'] = 1771791490
        notification_model['is_global'] = False
        notification_model['state'] = 'new'
        notification_model['regions'] = ['us-south', 'us-east']
        notification_model['crn_masks'] = ['crn:v1:staging:public:event-notifications:us-south:::']
        notification_model['record_id'] = 'rec-67890'
        notification_model['source_id'] = 'src-11111'
        notification_model['completion_code'] = 'successful'
        notification_model['end_time'] = 1771791490
        notification_model['update_time'] = 1771791490
        notification_model['severity'] = 2
        notification_model['lucene_query'] = 'region:us-south AND service_name:event-notifications'
        notification_model['resource_link'] = 'https://cloud.ibm.com/status/incident/12345'

        # Construct a json representation of a NotificationCollection model
        notification_collection_model_json = {}
        notification_collection_model_json['limit'] = 50
        notification_collection_model_json['total_count'] = 232
        notification_collection_model_json['first'] = pagination_link_model
        notification_collection_model_json['previous'] = pagination_link_with_token_model
        notification_collection_model_json['next'] = pagination_link_with_token_model
        notification_collection_model_json['last'] = pagination_link_with_token_model
        notification_collection_model_json['notifications'] = [notification_model]

        # Construct a model instance of NotificationCollection by calling from_dict on the json representation
        notification_collection_model = NotificationCollection.from_dict(notification_collection_model_json)
        assert notification_collection_model != False

        # Construct a model instance of NotificationCollection by calling from_dict on the json representation
        notification_collection_model_dict = NotificationCollection.from_dict(notification_collection_model_json).__dict__
        notification_collection_model2 = NotificationCollection(**notification_collection_model_dict)

        # Verify the model instances are equivalent
        assert notification_collection_model == notification_collection_model2

        # Convert model instance back to dict and verify no loss of data
        notification_collection_model_json2 = notification_collection_model.to_dict()
        assert notification_collection_model_json2 == notification_collection_model_json


class TestModel_PaginationLink:
    """
    Test Class for PaginationLink
    """

    def test_pagination_link_serialization(self):
        """
        Test serialization/deserialization for PaginationLink
        """

        # Construct a json representation of a PaginationLink model
        pagination_link_model_json = {}
        pagination_link_model_json['href'] = 'https://api.example.com/v1/notifications?limit=50'

        # Construct a model instance of PaginationLink by calling from_dict on the json representation
        pagination_link_model = PaginationLink.from_dict(pagination_link_model_json)
        assert pagination_link_model != False

        # Construct a model instance of PaginationLink by calling from_dict on the json representation
        pagination_link_model_dict = PaginationLink.from_dict(pagination_link_model_json).__dict__
        pagination_link_model2 = PaginationLink(**pagination_link_model_dict)

        # Verify the model instances are equivalent
        assert pagination_link_model == pagination_link_model2

        # Convert model instance back to dict and verify no loss of data
        pagination_link_model_json2 = pagination_link_model.to_dict()
        assert pagination_link_model_json2 == pagination_link_model_json


class TestModel_PaginationLinkWithToken:
    """
    Test Class for PaginationLinkWithToken
    """

    def test_pagination_link_with_token_serialization(self):
        """
        Test serialization/deserialization for PaginationLinkWithToken
        """

        # Construct a json representation of a PaginationLinkWithToken model
        pagination_link_with_token_model_json = {}
        pagination_link_with_token_model_json['href'] = 'https://api.example.com/v1/notifications?start=3fe78a36b9aa7f26&limit=50'
        pagination_link_with_token_model_json['start'] = '3fe78a36b9aa7f26'

        # Construct a model instance of PaginationLinkWithToken by calling from_dict on the json representation
        pagination_link_with_token_model = PaginationLinkWithToken.from_dict(pagination_link_with_token_model_json)
        assert pagination_link_with_token_model != False

        # Construct a model instance of PaginationLinkWithToken by calling from_dict on the json representation
        pagination_link_with_token_model_dict = PaginationLinkWithToken.from_dict(pagination_link_with_token_model_json).__dict__
        pagination_link_with_token_model2 = PaginationLinkWithToken(**pagination_link_with_token_model_dict)

        # Verify the model instances are equivalent
        assert pagination_link_with_token_model == pagination_link_with_token_model2

        # Convert model instance back to dict and verify no loss of data
        pagination_link_with_token_model_json2 = pagination_link_with_token_model.to_dict()
        assert pagination_link_with_token_model_json2 == pagination_link_with_token_model_json


class TestModel_PreferenceValueWithUpdates:
    """
    Test Class for PreferenceValueWithUpdates
    """

    def test_preference_value_with_updates_serialization(self):
        """
        Test serialization/deserialization for PreferenceValueWithUpdates
        """

        # Construct a json representation of a PreferenceValueWithUpdates model
        preference_value_with_updates_model_json = {}
        preference_value_with_updates_model_json['channels'] = ['email']
        preference_value_with_updates_model_json['updates'] = True

        # Construct a model instance of PreferenceValueWithUpdates by calling from_dict on the json representation
        preference_value_with_updates_model = PreferenceValueWithUpdates.from_dict(preference_value_with_updates_model_json)
        assert preference_value_with_updates_model != False

        # Construct a model instance of PreferenceValueWithUpdates by calling from_dict on the json representation
        preference_value_with_updates_model_dict = PreferenceValueWithUpdates.from_dict(preference_value_with_updates_model_json).__dict__
        preference_value_with_updates_model2 = PreferenceValueWithUpdates(**preference_value_with_updates_model_dict)

        # Verify the model instances are equivalent
        assert preference_value_with_updates_model == preference_value_with_updates_model2

        # Convert model instance back to dict and verify no loss of data
        preference_value_with_updates_model_json2 = preference_value_with_updates_model.to_dict()
        assert preference_value_with_updates_model_json2 == preference_value_with_updates_model_json


class TestModel_PreferenceValueWithoutUpdates:
    """
    Test Class for PreferenceValueWithoutUpdates
    """

    def test_preference_value_without_updates_serialization(self):
        """
        Test serialization/deserialization for PreferenceValueWithoutUpdates
        """

        # Construct a json representation of a PreferenceValueWithoutUpdates model
        preference_value_without_updates_model_json = {}
        preference_value_without_updates_model_json['channels'] = ['email']

        # Construct a model instance of PreferenceValueWithoutUpdates by calling from_dict on the json representation
        preference_value_without_updates_model = PreferenceValueWithoutUpdates.from_dict(preference_value_without_updates_model_json)
        assert preference_value_without_updates_model != False

        # Construct a model instance of PreferenceValueWithoutUpdates by calling from_dict on the json representation
        preference_value_without_updates_model_dict = PreferenceValueWithoutUpdates.from_dict(preference_value_without_updates_model_json).__dict__
        preference_value_without_updates_model2 = PreferenceValueWithoutUpdates(**preference_value_without_updates_model_dict)

        # Verify the model instances are equivalent
        assert preference_value_without_updates_model == preference_value_without_updates_model2

        # Convert model instance back to dict and verify no loss of data
        preference_value_without_updates_model_json2 = preference_value_without_updates_model.to_dict()
        assert preference_value_without_updates_model_json2 == preference_value_without_updates_model_json


class TestModel_PreferencesObject:
    """
    Test Class for PreferencesObject
    """

    def test_preferences_object_serialization(self):
        """
        Test serialization/deserialization for PreferencesObject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        preference_value_with_updates_model = {}  # PreferenceValueWithUpdates
        preference_value_with_updates_model['channels'] = ['email']
        preference_value_with_updates_model['updates'] = True

        preference_value_without_updates_model = {}  # PreferenceValueWithoutUpdates
        preference_value_without_updates_model['channels'] = ['email']

        # Construct a json representation of a PreferencesObject model
        preferences_object_model_json = {}
        preferences_object_model_json['incident_severity1'] = preference_value_with_updates_model
        preferences_object_model_json['incident_severity2'] = preference_value_with_updates_model
        preferences_object_model_json['incident_severity3'] = preference_value_with_updates_model
        preferences_object_model_json['incident_severity4'] = preference_value_with_updates_model
        preferences_object_model_json['maintenance_high'] = preference_value_with_updates_model
        preferences_object_model_json['maintenance_medium'] = preference_value_with_updates_model
        preferences_object_model_json['maintenance_low'] = preference_value_with_updates_model
        preferences_object_model_json['announcements_major'] = preference_value_without_updates_model
        preferences_object_model_json['announcements_minor'] = preference_value_without_updates_model
        preferences_object_model_json['security_normal'] = preference_value_without_updates_model
        preferences_object_model_json['account_normal'] = preference_value_without_updates_model
        preferences_object_model_json['billing_and_usage_order'] = preference_value_without_updates_model
        preferences_object_model_json['billing_and_usage_invoices'] = preference_value_without_updates_model
        preferences_object_model_json['billing_and_usage_payments'] = preference_value_without_updates_model
        preferences_object_model_json['billing_and_usage_subscriptions_and_promo_codes'] = preference_value_without_updates_model
        preferences_object_model_json['billing_and_usage_spending_alerts'] = preference_value_without_updates_model
        preferences_object_model_json['resourceactivity_normal'] = preference_value_without_updates_model
        preferences_object_model_json['ordering_review'] = preference_value_without_updates_model
        preferences_object_model_json['ordering_approved'] = preference_value_without_updates_model
        preferences_object_model_json['ordering_approved_vsi'] = preference_value_without_updates_model
        preferences_object_model_json['ordering_approved_server'] = preference_value_without_updates_model
        preferences_object_model_json['provisioning_reload_complete'] = preference_value_without_updates_model
        preferences_object_model_json['provisioning_complete_vsi'] = preference_value_without_updates_model
        preferences_object_model_json['provisioning_complete_server'] = preference_value_without_updates_model

        # Construct a model instance of PreferencesObject by calling from_dict on the json representation
        preferences_object_model = PreferencesObject.from_dict(preferences_object_model_json)
        assert preferences_object_model != False

        # Construct a model instance of PreferencesObject by calling from_dict on the json representation
        preferences_object_model_dict = PreferencesObject.from_dict(preferences_object_model_json).__dict__
        preferences_object_model2 = PreferencesObject(**preferences_object_model_dict)

        # Verify the model instances are equivalent
        assert preferences_object_model == preferences_object_model2

        # Convert model instance back to dict and verify no loss of data
        preferences_object_model_json2 = preferences_object_model.to_dict()
        assert preferences_object_model_json2 == preferences_object_model_json


class TestModel_TestDestinationResponseBody:
    """
    Test Class for TestDestinationResponseBody
    """

    def test_test_destination_response_body_serialization(self):
        """
        Test serialization/deserialization for TestDestinationResponseBody
        """

        # Construct a json representation of a TestDestinationResponseBody model
        test_destination_response_body_model_json = {}
        test_destination_response_body_model_json['message'] = 'success'

        # Construct a model instance of TestDestinationResponseBody by calling from_dict on the json representation
        test_destination_response_body_model = TestDestinationResponseBody.from_dict(test_destination_response_body_model_json)
        assert test_destination_response_body_model != False

        # Construct a model instance of TestDestinationResponseBody by calling from_dict on the json representation
        test_destination_response_body_model_dict = TestDestinationResponseBody.from_dict(test_destination_response_body_model_json).__dict__
        test_destination_response_body_model2 = TestDestinationResponseBody(**test_destination_response_body_model_dict)

        # Verify the model instances are equivalent
        assert test_destination_response_body_model == test_destination_response_body_model2

        # Convert model instance back to dict and verify no loss of data
        test_destination_response_body_model_json2 = test_destination_response_body_model.to_dict()
        assert test_destination_response_body_model_json2 == test_destination_response_body_model_json


class TestModel_Acknowledgement:
    """
    Test Class for Acknowledgement
    """

    def test_acknowledgement_serialization(self):
        """
        Test serialization/deserialization for Acknowledgement
        """

        # Construct a json representation of a Acknowledgement model
        acknowledgement_model_json = {}
        acknowledgement_model_json['has_unread'] = True
        acknowledgement_model_json['latest_notification_id'] = '1678901234000'
        acknowledgement_model_json['last_acknowledged_id'] = '1678800000000'

        # Construct a model instance of Acknowledgement by calling from_dict on the json representation
        acknowledgement_model = Acknowledgement.from_dict(acknowledgement_model_json)
        assert acknowledgement_model != False

        # Construct a model instance of Acknowledgement by calling from_dict on the json representation
        acknowledgement_model_dict = Acknowledgement.from_dict(acknowledgement_model_json).__dict__
        acknowledgement_model2 = Acknowledgement(**acknowledgement_model_dict)

        # Verify the model instances are equivalent
        assert acknowledgement_model == acknowledgement_model2

        # Convert model instance back to dict and verify no loss of data
        acknowledgement_model_json2 = acknowledgement_model.to_dict()
        assert acknowledgement_model_json2 == acknowledgement_model_json


class TestModel_AddDestinationPrototypeEventNotificationDestinationPrototype:
    """
    Test Class for AddDestinationPrototypeEventNotificationDestinationPrototype
    """

    def test_add_destination_prototype_event_notification_destination_prototype_serialization(self):
        """
        Test serialization/deserialization for AddDestinationPrototypeEventNotificationDestinationPrototype
        """

        # Construct a json representation of a AddDestinationPrototypeEventNotificationDestinationPrototype model
        add_destination_prototype_event_notification_destination_prototype_model_json = {}
        add_destination_prototype_event_notification_destination_prototype_model_json['destination_id'] = '12345678-1234-1234-1234-123456789012'
        add_destination_prototype_event_notification_destination_prototype_model_json['destination_type'] = 'event_notifications'

        # Construct a model instance of AddDestinationPrototypeEventNotificationDestinationPrototype by calling from_dict on the json representation
        add_destination_prototype_event_notification_destination_prototype_model = AddDestinationPrototypeEventNotificationDestinationPrototype.from_dict(add_destination_prototype_event_notification_destination_prototype_model_json)
        assert add_destination_prototype_event_notification_destination_prototype_model != False

        # Construct a model instance of AddDestinationPrototypeEventNotificationDestinationPrototype by calling from_dict on the json representation
        add_destination_prototype_event_notification_destination_prototype_model_dict = AddDestinationPrototypeEventNotificationDestinationPrototype.from_dict(add_destination_prototype_event_notification_destination_prototype_model_json).__dict__
        add_destination_prototype_event_notification_destination_prototype_model2 = AddDestinationPrototypeEventNotificationDestinationPrototype(**add_destination_prototype_event_notification_destination_prototype_model_dict)

        # Verify the model instances are equivalent
        assert add_destination_prototype_event_notification_destination_prototype_model == add_destination_prototype_event_notification_destination_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        add_destination_prototype_event_notification_destination_prototype_model_json2 = add_destination_prototype_event_notification_destination_prototype_model.to_dict()
        assert add_destination_prototype_event_notification_destination_prototype_model_json2 == add_destination_prototype_event_notification_destination_prototype_model_json


class TestModel_AddDestinationEventNotificationDestination:
    """
    Test Class for AddDestinationEventNotificationDestination
    """

    def test_add_destination_event_notification_destination_serialization(self):
        """
        Test serialization/deserialization for AddDestinationEventNotificationDestination
        """

        # Construct a json representation of a AddDestinationEventNotificationDestination model
        add_destination_event_notification_destination_model_json = {}
        add_destination_event_notification_destination_model_json['destination_id'] = '12345678-1234-1234-1234-123456789012'
        add_destination_event_notification_destination_model_json['destination_type'] = 'event_notifications'

        # Construct a model instance of AddDestinationEventNotificationDestination by calling from_dict on the json representation
        add_destination_event_notification_destination_model = AddDestinationEventNotificationDestination.from_dict(add_destination_event_notification_destination_model_json)
        assert add_destination_event_notification_destination_model != False

        # Construct a model instance of AddDestinationEventNotificationDestination by calling from_dict on the json representation
        add_destination_event_notification_destination_model_dict = AddDestinationEventNotificationDestination.from_dict(add_destination_event_notification_destination_model_json).__dict__
        add_destination_event_notification_destination_model2 = AddDestinationEventNotificationDestination(**add_destination_event_notification_destination_model_dict)

        # Verify the model instances are equivalent
        assert add_destination_event_notification_destination_model == add_destination_event_notification_destination_model2

        # Convert model instance back to dict and verify no loss of data
        add_destination_event_notification_destination_model_json2 = add_destination_event_notification_destination_model.to_dict()
        assert add_destination_event_notification_destination_model_json2 == add_destination_event_notification_destination_model_json


class TestModel_TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype:
    """
    Test Class for TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype
    """

    def test_test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_serialization(self):
        """
        Test serialization/deserialization for TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype
        """

        # Construct a json representation of a TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype model
        test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_json = {}
        test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_json['destination_type'] = 'event_notifications'
        test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_json['notification_type'] = 'incident'

        # Construct a model instance of TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype by calling from_dict on the json representation
        test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model = TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype.from_dict(test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_json)
        assert test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model != False

        # Construct a model instance of TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype by calling from_dict on the json representation
        test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_dict = TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype.from_dict(test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_json).__dict__
        test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model2 = TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype(**test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_dict)

        # Verify the model instances are equivalent
        assert test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model == test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_json2 = test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model.to_dict()
        assert test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_json2 == test_destination_request_body_prototype_test_event_notification_destination_request_body_prototype_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
