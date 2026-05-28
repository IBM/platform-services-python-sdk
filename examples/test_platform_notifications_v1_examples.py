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
Examples for PlatformNotificationsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_platform_services.platform_notifications_v1 import *

#
# This file provides an example of how to use the Platform Notifications service.
#
# The following configuration properties are assumed to be defined:
# PLATFORM_NOTIFICATIONS_URL=<service base url>
# PLATFORM_NOTIFICATIONS_AUTH_TYPE=iam
# PLATFORM_NOTIFICATIONS_APIKEY=<IAM apikey>
# PLATFORM_NOTIFICATIONS_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'platform_notifications_v1.env'

platform_notifications_service = None

config = None

account_id = None

destination_id = None

iam_id = None

service_url = None


##############################################################################
# Start of Examples for Service: PlatformNotificationsV1
##############################################################################
# region
class TestPlatformNotificationsV1Examples:
    """
    Example Test Class for PlatformNotificationsV1
    """

    @classmethod
    def setup_class(cls):
        global platform_notifications_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            platform_notifications_service = PlatformNotificationsV1.new_instance()

            # end-common
            assert platform_notifications_service is not None

            # Load the configuration
            global config
            config = read_external_sources(PlatformNotificationsV1.DEFAULT_SERVICE_NAME)
            global account_id, destination_id, iam_id, service_url
            account_id = config['ACCOUNT_ID']
            destination_id = config['DESTINATION_ID']
            iam_id = config['IAM_ID']
            service_url = config['SERVICE_URL']
            # Set service URL if provided in config
            if service_url:
                platform_notifications_service.set_service_url(service_url)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_distribution_list_destinations_example(self):
        """
        list_distribution_list_destinations request example
        """
        try:
            print('\nlist_distribution_list_destinations() result:')

            # begin-list_distribution_list_destinations

            response = platform_notifications_service.list_distribution_list_destinations(
                account_id=account_id,
            )
            add_destination_collection = response.get_result()

            print(json.dumps(add_destination_collection, indent=2))

            # end-list_distribution_list_destinations

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_distribution_list_destination_example(self):
        """
        create_distribution_list_destination request example
        """
        try:
            print('\ncreate_distribution_list_destination() result:')

            # begin-create_distribution_list_destination

            add_destination_prototype_model = {
                'destination_id': destination_id,
                'destination_type': 'event_notifications',
            }

            response = platform_notifications_service.create_distribution_list_destination(
                account_id=account_id,
                add_destination_prototype=add_destination_prototype_model,
            )
            add_destination = response.get_result()

            print(json.dumps(add_destination, indent=2))

            # end-create_distribution_list_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_distribution_list_destination_example(self):
        """
        get_distribution_list_destination request example
        """
        try:
            print('\nget_distribution_list_destination() result:')

            # begin-get_distribution_list_destination

            response = platform_notifications_service.get_distribution_list_destination(
                account_id=account_id,
                destination_id=destination_id,
            )
            add_destination = response.get_result()

            print(json.dumps(add_destination, indent=2))

            # end-get_distribution_list_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_test_distribution_list_destination_example(self):
        """
        test_distribution_list_destination request example
        """
        try:
            print('\ntest_distribution_list_destination() result:')

            # begin-test_distribution_list_destination

            test_destination_request_body_prototype_model = {
                'destination_type': 'event_notifications',
                'notification_type': 'incident',
            }

            response = platform_notifications_service.test_distribution_list_destination(
                account_id=account_id,
                destination_id=destination_id,
                test_destination_request_body_prototype=test_destination_request_body_prototype_model,
            )
            test_destination_response_body = response.get_result()

            print(json.dumps(test_destination_response_body, indent=2))

            # end-test_distribution_list_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_preferences_example(self):
        """
        create_preferences request example
        """
        try:
            print('\ncreate_preferences() result:')

            # begin-create_preferences

            preference_value_with_updates_model = {
                'channels': ['email'],
                'updates': True,
            }

            preference_value_without_updates_model = {
                'channels': ['email'],
            }

            response = platform_notifications_service.create_preferences(
                iam_id=iam_id,
                incident_severity1=preference_value_with_updates_model,
                ordering_review=preference_value_without_updates_model,
                account_id=account_id,
            )
            preferences_object = response.get_result()

            print(json.dumps(preferences_object, indent=2))

            # end-create_preferences

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_preferences_example(self):
        """
        get_preferences request example
        """
        try:
            print('\nget_preferences() result:')

            # begin-get_preferences

            response = platform_notifications_service.get_preferences(
                iam_id=iam_id,
                account_id=account_id,
            )
            preferences_object = response.get_result()

            print(json.dumps(preferences_object, indent=2))

            # end-get_preferences

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_notification_preferences_example(self):
        """
        replace_notification_preferences request example
        """
        try:
            print('\nreplace_notification_preferences() result:')

            # begin-replace_notification_preferences

            preference_value_with_updates_model = {
                'channels': ['email'],
                'updates': True,
            }

            preference_value_without_updates_model = {
                'channels': ['email'],
            }

            response = platform_notifications_service.replace_notification_preferences(
                iam_id=iam_id,
                incident_severity1=preference_value_with_updates_model,
                ordering_review=preference_value_without_updates_model,
                account_id=account_id,
            )
            preferences_object = response.get_result()

            print(json.dumps(preferences_object, indent=2))

            # end-replace_notification_preferences

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_notifications_example(self):
        """
        list_notifications request example
        """
        try:
            print('\nlist_notifications() result:')

            # begin-list_notifications

            all_results = []
            pager = NotificationsPager(
                client=platform_notifications_service,
                account_id=account_id,
                limit=50,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_notifications
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_acknowledgement_example(self):
        """
        get_acknowledgement request example
        """
        try:
            print('\nget_acknowledgement() result:')

            # begin-get_acknowledgement

            response = platform_notifications_service.get_acknowledgement(
                account_id=account_id,
            )
            acknowledgement = response.get_result()

            print(json.dumps(acknowledgement, indent=2))

            # end-get_acknowledgement

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_notification_acknowledgement_example(self):
        """
        replace_notification_acknowledgement request example
        """
        try:
            print('\nreplace_notification_acknowledgement() result:')

            # begin-replace_notification_acknowledgement

            response = platform_notifications_service.replace_notification_acknowledgement(
                last_acknowledged_id='1772804159452',
                account_id=account_id,
            )
            acknowledgement = response.get_result()

            print(json.dumps(acknowledgement, indent=2))

            # end-replace_notification_acknowledgement

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_distribution_list_destination_example(self):
        """
        delete_distribution_list_destination request example
        """
        try:
            # begin-delete_distribution_list_destination

            response = platform_notifications_service.delete_distribution_list_destination(
                account_id=account_id,
                destination_id=destination_id,
            )

            # end-delete_distribution_list_destination
            print('\ndelete_distribution_list_destination() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_notification_preferences_example(self):
        """
        delete_notification_preferences request example
        """
        try:
            # begin-delete_notification_preferences

            response = platform_notifications_service.delete_notification_preferences(
                iam_id=iam_id,
                account_id=account_id,
            )

            # end-delete_notification_preferences
            print('\ndelete_notification_preferences() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: PlatformNotificationsV1
##############################################################################
