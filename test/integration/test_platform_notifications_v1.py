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
Integration Tests for PlatformNotificationsV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_platform_services.platform_notifications_v1 import *

# Config file name
# required variables in platform_notifications_v1.env
# PLATFORM_NOTIFICATIONS_URL
# PLATFORM_NOTIFICATIONS_AUTH_TYPE
# PLATFORM_NOTIFICATIONS_AUTH_URL
# PLATFORM_NOTIFICATIONS_APIKEY
# PLATFORM_NOTIFICATIONS_ACCOUNT_ID
# PLATFORM_NOTIFICATIONS_DESTINATION_ID
# PLATFORM_NOTIFICATIONS_IAM_ID
config_file = 'platform_notifications_v1.env'

account_id = ''
destination_id = ''
iam_id = ''
service_url = ''

class TestPlatformNotificationsV1:
    """
    Integration Test Class for PlatformNotificationsV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.platform_notifications_service = PlatformNotificationsV1.new_instance(
            )
            assert cls.platform_notifications_service is not None

            cls.config = read_external_sources(PlatformNotificationsV1.DEFAULT_SERVICE_NAME)
            global account_id, destination_id, iam_id, service_url
            account_id = cls.config['ACCOUNT_ID']
            destination_id = cls.config['DESTINATION_ID']
            iam_id = cls.config['IAM_ID']
            service_url = cls.config['SERVICE_URL']
            assert cls.config is not None

            # Set service URL if provided in config
            if service_url:
                cls.platform_notifications_service.set_service_url(service_url)

            cls.platform_notifications_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_test_distribution_list_destination(self):
        # Construct a dict representation of a TestDestinationRequestBodyPrototypeTestEventNotificationDestinationRequestBodyPrototype model
        test_destination_request_body_prototype_model = {
            'destination_type': 'event_notifications',
            'notification_type': 'incident',
        }

        response = self.platform_notifications_service.test_distribution_list_destination(
            account_id=account_id,
            destination_id=destination_id,
            test_destination_request_body_prototype=test_destination_request_body_prototype_model,
        )

        assert response.get_status_code() == 200
        test_destination_response_body = response.get_result()
        assert test_destination_response_body is not None

    @needscredentials
    def test_delete_distribution_list_destination(self):
        response = self.platform_notifications_service.delete_distribution_list_destination(
            account_id=account_id,
            destination_id=destination_id,
        )

        assert response.get_status_code() == 204
    
    @needscredentials
    def test_create_distribution_list_destination(self):
        # Construct a dict representation of a AddDestinationPrototypeEventNotificationDestinationPrototype model
        add_destination_prototype_model = {
            'destination_id': destination_id,
            'destination_type': 'event_notifications',
        }

        response = self.platform_notifications_service.create_distribution_list_destination(
            account_id=account_id,
            add_destination_prototype=add_destination_prototype_model,
        )

        assert response.get_status_code() == 201
        add_destination = response.get_result()
        assert add_destination is not None

    @needscredentials
    def test_list_distribution_list_destinations(self):
        response = self.platform_notifications_service.list_distribution_list_destinations(
            account_id=account_id,
        )

        assert response.get_status_code() == 200
        add_destination_collection = response.get_result()
        assert add_destination_collection is not None

    @needscredentials
    def test_get_distribution_list_destination(self):
        response = self.platform_notifications_service.get_distribution_list_destination(
            account_id=account_id,
            destination_id=destination_id,
        )

        assert response.get_status_code() == 200
        add_destination = response.get_result()
        assert add_destination is not None

    @needscredentials
    def test_create_preferences(self):
        # Construct a dict representation of a PreferenceValueWithUpdates model
        preference_value_with_updates_model = {
            'channels': ['email'],
            'updates': True,
        }
        # Construct a dict representation of a PreferenceValueWithoutUpdates model
        preference_value_without_updates_model = {
            'channels': ['email'],
        }

        response = self.platform_notifications_service.create_preferences(
            iam_id=iam_id,
            incident_severity1=preference_value_with_updates_model,
            incident_severity2=preference_value_with_updates_model,
            incident_severity3=preference_value_with_updates_model,
            incident_severity4=preference_value_with_updates_model,
            maintenance_high=preference_value_with_updates_model,
            maintenance_medium=preference_value_with_updates_model,
            maintenance_low=preference_value_with_updates_model,
            announcements_major=preference_value_without_updates_model,
            announcements_minor=preference_value_without_updates_model,
            security_normal=preference_value_without_updates_model,
            account_normal=preference_value_without_updates_model,
            billing_and_usage_order=preference_value_without_updates_model,
            billing_and_usage_invoices=preference_value_without_updates_model,
            billing_and_usage_payments=preference_value_without_updates_model,
            billing_and_usage_subscriptions_and_promo_codes=preference_value_without_updates_model,
            billing_and_usage_spending_alerts=preference_value_without_updates_model,
            resourceactivity_normal=preference_value_without_updates_model,
            ordering_review=preference_value_without_updates_model,
            ordering_approved=preference_value_without_updates_model,
            ordering_approved_vsi=preference_value_without_updates_model,
            ordering_approved_server=preference_value_without_updates_model,
            provisioning_reload_complete=preference_value_without_updates_model,
            provisioning_complete_vsi=preference_value_without_updates_model,
            provisioning_complete_server=preference_value_without_updates_model,
            account_id=account_id,
        )

        assert response.get_status_code() == 201
        preferences_object = response.get_result()
        assert preferences_object is not None

    @needscredentials
    def test_get_preferences(self):
        response = self.platform_notifications_service.get_preferences(
            iam_id=iam_id,
            account_id=account_id,
        )

        assert response.get_status_code() == 200
        preferences_object = response.get_result()
        assert preferences_object is not None

    @needscredentials
    def test_replace_notification_preferences(self):
        # Construct a dict representation of a PreferenceValueWithUpdates model
        preference_value_with_updates_model = {
            'channels': ['email'],
            'updates': True,
        }
        # Construct a dict representation of a PreferenceValueWithoutUpdates model
        preference_value_without_updates_model = {
            'channels': ['email'],
        }

        response = self.platform_notifications_service.replace_notification_preferences(
            iam_id=iam_id,
            incident_severity1=preference_value_with_updates_model,
            incident_severity2=preference_value_with_updates_model,
            incident_severity3=preference_value_with_updates_model,
            incident_severity4=preference_value_with_updates_model,
            maintenance_high=preference_value_with_updates_model,
            maintenance_medium=preference_value_with_updates_model,
            maintenance_low=preference_value_with_updates_model,
            announcements_major=preference_value_without_updates_model,
            announcements_minor=preference_value_without_updates_model,
            security_normal=preference_value_without_updates_model,
            account_normal=preference_value_without_updates_model,
            billing_and_usage_order=preference_value_without_updates_model,
            billing_and_usage_invoices=preference_value_without_updates_model,
            billing_and_usage_payments=preference_value_without_updates_model,
            billing_and_usage_subscriptions_and_promo_codes=preference_value_without_updates_model,
            billing_and_usage_spending_alerts=preference_value_without_updates_model,
            resourceactivity_normal=preference_value_without_updates_model,
            ordering_review=preference_value_without_updates_model,
            ordering_approved=preference_value_without_updates_model,
            ordering_approved_vsi=preference_value_without_updates_model,
            ordering_approved_server=preference_value_without_updates_model,
            provisioning_reload_complete=preference_value_without_updates_model,
            provisioning_complete_vsi=preference_value_without_updates_model,
            provisioning_complete_server=preference_value_without_updates_model,
            account_id=account_id,
        )

        assert response.get_status_code() == 200
        preferences_object = response.get_result()
        assert preferences_object is not None

    @needscredentials
    def test_list_notifications(self):
        response = self.platform_notifications_service.list_notifications(
            account_id=account_id,
        )

        assert response.get_status_code() == 200
        notification_collection = response.get_result()
        assert notification_collection is not None

    @needscredentials
    def test_list_notifications_with_pager(self):
        all_results = []

        # Test get_next().
        pager = NotificationsPager(
            client=self.platform_notifications_service,
            account_id=account_id,
            limit=50,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = NotificationsPager(
            client=self.platform_notifications_service,
            account_id=account_id,
            limit=50,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_notifications() returned a total of {len(all_results)} items(s) using NotificationsPager.')

    @needscredentials
    def test_get_acknowledgement(self):
        response = self.platform_notifications_service.get_acknowledgement(
            account_id=account_id,
        )

        assert response.get_status_code() == 200
        acknowledgement = response.get_result()
        assert acknowledgement is not None

    @needscredentials
    def test_replace_notification_acknowledgement(self):
        response = self.platform_notifications_service.replace_notification_acknowledgement(
            last_acknowledged_id='1772804159452',
            account_id=account_id,
        )

        assert response.get_status_code() == 200
        acknowledgement = response.get_result()
        assert acknowledgement is not None


    @needscredentials
    def test_delete_notification_preferences(self):
        response = self.platform_notifications_service.delete_notification_preferences(
            iam_id=iam_id,
            account_id=account_id,
        )

        assert response.get_status_code() == 204
