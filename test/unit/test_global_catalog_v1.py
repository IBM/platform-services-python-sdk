# -*- coding: utf-8 -*-
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

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import io
import json
import pytest
import requests
import responses
import tempfile
from ibm_platform_services.global_catalog_v1 import *


service = GlobalCatalogV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://globalcatalog.cloud.ibm.com/api/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Object
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_catalog_entries
#-----------------------------------------------------------------------------
class TestListCatalogEntries():

    #--------------------------------------------------------
    # list_catalog_entries()
    #--------------------------------------------------------
    @responses.activate
    def test_list_catalog_entries_all_params(self):
        # Set up mock
        url = base_url + '/'
        mock_response = '{"offset": 6, "limit": 5, "count": 5, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account = 'testString'
        include = 'testString'
        q = 'testString'
        sort_by = 'testString'
        descending = 'testString'
        languages = 'testString'
        complete = 'testString'

        # Invoke method
        response = service.list_catalog_entries(
            account=account,
            include=include,
            q=q,
            sort_by=sort_by,
            descending=descending,
            languages=languages,
            complete=complete,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'include={}'.format(include) in query_string
        assert 'q={}'.format(q) in query_string
        assert 'sort-by={}'.format(sort_by) in query_string
        assert 'descending={}'.format(descending) in query_string
        assert 'languages={}'.format(languages) in query_string
        assert 'complete={}'.format(complete) in query_string


    #--------------------------------------------------------
    # test_list_catalog_entries_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_catalog_entries_required_params(self):
        # Set up mock
        url = base_url + '/'
        mock_response = '{"offset": 6, "limit": 5, "count": 5, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_catalog_entries()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_catalog_entry
#-----------------------------------------------------------------------------
class TestCreateCatalogEntry():

    #--------------------------------------------------------
    # create_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_create_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/'
        mock_response = '{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'
        overview_model['featured_description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a Broker model
        broker_model = {}
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        # Construct a dict representation of a DRMetaData model
        dr_meta_data_model = {}
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a SourceMetaData model
        source_meta_data_model = {}
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        # Construct a dict representation of a AliasMetaData model
        alias_meta_data_model = {}
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        # Construct a dict representation of a CFMetaData model
        cf_meta_data_model = {}
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        # Construct a dict representation of a DeploymentBase model
        deployment_base_model = {}
        deployment_base_model['location'] = 'testString'
        deployment_base_model['location_url'] = 'testString'
        deployment_base_model['original_location'] = 'testString'
        deployment_base_model['target_crn'] = 'testString'
        deployment_base_model['service_crn'] = 'testString'
        deployment_base_model['mccp_id'] = 'testString'
        deployment_base_model['broker'] = broker_model
        deployment_base_model['supports_rc_migration'] = True
        deployment_base_model['target_network'] = 'testString'

        # Construct a dict representation of a PlanMetaData model
        plan_meta_data_model = {}
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a PricingSet model
        pricing_set_model = {}
        pricing_set_model['type'] = 'testString'
        pricing_set_model['origin'] = 'testString'
        pricing_set_model['starting_price'] = starting_price_model

        # Construct a dict representation of a SLAMetaData model
        sla_meta_data_model = {}
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        # Construct a dict representation of a TemplateMetaData model
        template_meta_data_model = {}
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        # Construct a dict representation of a ObjectMetadataSet model
        object_metadata_set_model = {}
        object_metadata_set_model['rc_compatible'] = True
        object_metadata_set_model['service'] = cf_meta_data_model
        object_metadata_set_model['plan'] = plan_meta_data_model
        object_metadata_set_model['alias'] = alias_meta_data_model
        object_metadata_set_model['template'] = template_meta_data_model
        object_metadata_set_model['ui'] = ui_meta_data_model
        object_metadata_set_model['compliance'] = ['testString']
        object_metadata_set_model['sla'] = sla_meta_data_model
        object_metadata_set_model['callbacks'] = callbacks_model
        object_metadata_set_model['original_name'] = 'testString'
        object_metadata_set_model['version'] = 'testString'
        object_metadata_set_model['other'] = {}
        object_metadata_set_model['pricing'] = pricing_set_model
        object_metadata_set_model['deployment'] = deployment_base_model

        # Set up parameter values
        name = 'testString'
        kind = 'service'
        overview_ui = overview_ui_model
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        id = 'testString'
        parent_id = 'testString'
        group = True
        active = True
        metadata = object_metadata_set_model
        account = 'testString'

        # Invoke method
        response = service.create_catalog_entry(
            name,
            kind,
            overview_ui,
            images,
            disabled,
            tags,
            provider,
            id,
            parent_id=parent_id,
            group=group,
            active=active,
            metadata=metadata,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['kind'] == 'service'
        assert req_body['overview_ui'] == overview_ui_model
        assert req_body['images'] == image_model
        assert req_body['disabled'] == True
        assert req_body['tags'] == ['testString']
        assert req_body['provider'] == provider_model
        assert req_body['id'] == 'testString'
        assert req_body['parent_id'] == 'testString'
        assert req_body['group'] == True
        assert req_body['active'] == True
        assert req_body['metadata'] == object_metadata_set_model


    #--------------------------------------------------------
    # test_create_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/'
        mock_response = '{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'
        overview_model['featured_description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a Broker model
        broker_model = {}
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        # Construct a dict representation of a DRMetaData model
        dr_meta_data_model = {}
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a SourceMetaData model
        source_meta_data_model = {}
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        # Construct a dict representation of a AliasMetaData model
        alias_meta_data_model = {}
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        # Construct a dict representation of a CFMetaData model
        cf_meta_data_model = {}
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        # Construct a dict representation of a DeploymentBase model
        deployment_base_model = {}
        deployment_base_model['location'] = 'testString'
        deployment_base_model['location_url'] = 'testString'
        deployment_base_model['original_location'] = 'testString'
        deployment_base_model['target_crn'] = 'testString'
        deployment_base_model['service_crn'] = 'testString'
        deployment_base_model['mccp_id'] = 'testString'
        deployment_base_model['broker'] = broker_model
        deployment_base_model['supports_rc_migration'] = True
        deployment_base_model['target_network'] = 'testString'

        # Construct a dict representation of a PlanMetaData model
        plan_meta_data_model = {}
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a PricingSet model
        pricing_set_model = {}
        pricing_set_model['type'] = 'testString'
        pricing_set_model['origin'] = 'testString'
        pricing_set_model['starting_price'] = starting_price_model

        # Construct a dict representation of a SLAMetaData model
        sla_meta_data_model = {}
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        # Construct a dict representation of a TemplateMetaData model
        template_meta_data_model = {}
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        # Construct a dict representation of a ObjectMetadataSet model
        object_metadata_set_model = {}
        object_metadata_set_model['rc_compatible'] = True
        object_metadata_set_model['service'] = cf_meta_data_model
        object_metadata_set_model['plan'] = plan_meta_data_model
        object_metadata_set_model['alias'] = alias_meta_data_model
        object_metadata_set_model['template'] = template_meta_data_model
        object_metadata_set_model['ui'] = ui_meta_data_model
        object_metadata_set_model['compliance'] = ['testString']
        object_metadata_set_model['sla'] = sla_meta_data_model
        object_metadata_set_model['callbacks'] = callbacks_model
        object_metadata_set_model['original_name'] = 'testString'
        object_metadata_set_model['version'] = 'testString'
        object_metadata_set_model['other'] = {}
        object_metadata_set_model['pricing'] = pricing_set_model
        object_metadata_set_model['deployment'] = deployment_base_model

        # Set up parameter values
        name = 'testString'
        kind = 'service'
        overview_ui = overview_ui_model
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        id = 'testString'
        parent_id = 'testString'
        group = True
        active = True
        metadata = object_metadata_set_model

        # Invoke method
        response = service.create_catalog_entry(
            name,
            kind,
            overview_ui,
            images,
            disabled,
            tags,
            provider,
            id,
            parent_id=parent_id,
            group=group,
            active=active,
            metadata=metadata,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['kind'] == 'service'
        assert req_body['overview_ui'] == overview_ui_model
        assert req_body['images'] == image_model
        assert req_body['disabled'] == True
        assert req_body['tags'] == ['testString']
        assert req_body['provider'] == provider_model
        assert req_body['id'] == 'testString'
        assert req_body['parent_id'] == 'testString'
        assert req_body['group'] == True
        assert req_body['active'] == True
        assert req_body['metadata'] == object_metadata_set_model


    #--------------------------------------------------------
    # test_create_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/'
        mock_response = '{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'
        overview_model['featured_description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a Broker model
        broker_model = {}
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        # Construct a dict representation of a DRMetaData model
        dr_meta_data_model = {}
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a SourceMetaData model
        source_meta_data_model = {}
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        # Construct a dict representation of a AliasMetaData model
        alias_meta_data_model = {}
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        # Construct a dict representation of a CFMetaData model
        cf_meta_data_model = {}
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        # Construct a dict representation of a DeploymentBase model
        deployment_base_model = {}
        deployment_base_model['location'] = 'testString'
        deployment_base_model['location_url'] = 'testString'
        deployment_base_model['original_location'] = 'testString'
        deployment_base_model['target_crn'] = 'testString'
        deployment_base_model['service_crn'] = 'testString'
        deployment_base_model['mccp_id'] = 'testString'
        deployment_base_model['broker'] = broker_model
        deployment_base_model['supports_rc_migration'] = True
        deployment_base_model['target_network'] = 'testString'

        # Construct a dict representation of a PlanMetaData model
        plan_meta_data_model = {}
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a PricingSet model
        pricing_set_model = {}
        pricing_set_model['type'] = 'testString'
        pricing_set_model['origin'] = 'testString'
        pricing_set_model['starting_price'] = starting_price_model

        # Construct a dict representation of a SLAMetaData model
        sla_meta_data_model = {}
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        # Construct a dict representation of a TemplateMetaData model
        template_meta_data_model = {}
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        # Construct a dict representation of a ObjectMetadataSet model
        object_metadata_set_model = {}
        object_metadata_set_model['rc_compatible'] = True
        object_metadata_set_model['service'] = cf_meta_data_model
        object_metadata_set_model['plan'] = plan_meta_data_model
        object_metadata_set_model['alias'] = alias_meta_data_model
        object_metadata_set_model['template'] = template_meta_data_model
        object_metadata_set_model['ui'] = ui_meta_data_model
        object_metadata_set_model['compliance'] = ['testString']
        object_metadata_set_model['sla'] = sla_meta_data_model
        object_metadata_set_model['callbacks'] = callbacks_model
        object_metadata_set_model['original_name'] = 'testString'
        object_metadata_set_model['version'] = 'testString'
        object_metadata_set_model['other'] = {}
        object_metadata_set_model['pricing'] = pricing_set_model
        object_metadata_set_model['deployment'] = deployment_base_model

        # Set up parameter values
        name = 'testString'
        kind = 'service'
        overview_ui = overview_ui_model
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        id = 'testString'
        parent_id = 'testString'
        group = True
        active = True
        metadata = object_metadata_set_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "kind": kind,
            "overview_ui": overview_ui,
            "images": images,
            "disabled": disabled,
            "tags": tags,
            "provider": provider,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_catalog_entry(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_catalog_entry
#-----------------------------------------------------------------------------
class TestGetCatalogEntry():

    #--------------------------------------------------------
    # get_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/testString'
        mock_response = '{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        account = 'testString'
        include = 'testString'
        languages = 'testString'
        complete = 'testString'
        depth = 38

        # Invoke method
        response = service.get_catalog_entry(
            id,
            account=account,
            include=include,
            languages=languages,
            complete=complete,
            depth=depth,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'include={}'.format(include) in query_string
        assert 'languages={}'.format(languages) in query_string
        assert 'complete={}'.format(complete) in query_string
        assert 'depth={}'.format(depth) in query_string


    #--------------------------------------------------------
    # test_get_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString'
        mock_response = '{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_catalog_entry(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/testString'
        mock_response = '{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_catalog_entry(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_catalog_entry
#-----------------------------------------------------------------------------
class TestUpdateCatalogEntry():

    #--------------------------------------------------------
    # update_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_update_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/testString'
        mock_response = '{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'
        overview_model['featured_description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a Broker model
        broker_model = {}
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        # Construct a dict representation of a DRMetaData model
        dr_meta_data_model = {}
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a SourceMetaData model
        source_meta_data_model = {}
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        # Construct a dict representation of a AliasMetaData model
        alias_meta_data_model = {}
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        # Construct a dict representation of a CFMetaData model
        cf_meta_data_model = {}
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        # Construct a dict representation of a DeploymentBase model
        deployment_base_model = {}
        deployment_base_model['location'] = 'testString'
        deployment_base_model['location_url'] = 'testString'
        deployment_base_model['original_location'] = 'testString'
        deployment_base_model['target_crn'] = 'testString'
        deployment_base_model['service_crn'] = 'testString'
        deployment_base_model['mccp_id'] = 'testString'
        deployment_base_model['broker'] = broker_model
        deployment_base_model['supports_rc_migration'] = True
        deployment_base_model['target_network'] = 'testString'

        # Construct a dict representation of a PlanMetaData model
        plan_meta_data_model = {}
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a PricingSet model
        pricing_set_model = {}
        pricing_set_model['type'] = 'testString'
        pricing_set_model['origin'] = 'testString'
        pricing_set_model['starting_price'] = starting_price_model

        # Construct a dict representation of a SLAMetaData model
        sla_meta_data_model = {}
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        # Construct a dict representation of a TemplateMetaData model
        template_meta_data_model = {}
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        # Construct a dict representation of a ObjectMetadataSet model
        object_metadata_set_model = {}
        object_metadata_set_model['rc_compatible'] = True
        object_metadata_set_model['service'] = cf_meta_data_model
        object_metadata_set_model['plan'] = plan_meta_data_model
        object_metadata_set_model['alias'] = alias_meta_data_model
        object_metadata_set_model['template'] = template_meta_data_model
        object_metadata_set_model['ui'] = ui_meta_data_model
        object_metadata_set_model['compliance'] = ['testString']
        object_metadata_set_model['sla'] = sla_meta_data_model
        object_metadata_set_model['callbacks'] = callbacks_model
        object_metadata_set_model['original_name'] = 'testString'
        object_metadata_set_model['version'] = 'testString'
        object_metadata_set_model['other'] = {}
        object_metadata_set_model['pricing'] = pricing_set_model
        object_metadata_set_model['deployment'] = deployment_base_model

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        kind = 'service'
        overview_ui = overview_ui_model
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        parent_id = 'testString'
        group = True
        active = True
        metadata = object_metadata_set_model
        account = 'testString'
        move = 'testString'

        # Invoke method
        response = service.update_catalog_entry(
            id,
            name,
            kind,
            overview_ui,
            images,
            disabled,
            tags,
            provider,
            parent_id=parent_id,
            group=group,
            active=active,
            metadata=metadata,
            account=account,
            move=move,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'move={}'.format(move) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['kind'] == 'service'
        assert req_body['overview_ui'] == overview_ui_model
        assert req_body['images'] == image_model
        assert req_body['disabled'] == True
        assert req_body['tags'] == ['testString']
        assert req_body['provider'] == provider_model
        assert req_body['parent_id'] == 'testString'
        assert req_body['group'] == True
        assert req_body['active'] == True
        assert req_body['metadata'] == object_metadata_set_model


    #--------------------------------------------------------
    # test_update_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString'
        mock_response = '{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'
        overview_model['featured_description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a Broker model
        broker_model = {}
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        # Construct a dict representation of a DRMetaData model
        dr_meta_data_model = {}
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a SourceMetaData model
        source_meta_data_model = {}
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        # Construct a dict representation of a AliasMetaData model
        alias_meta_data_model = {}
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        # Construct a dict representation of a CFMetaData model
        cf_meta_data_model = {}
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        # Construct a dict representation of a DeploymentBase model
        deployment_base_model = {}
        deployment_base_model['location'] = 'testString'
        deployment_base_model['location_url'] = 'testString'
        deployment_base_model['original_location'] = 'testString'
        deployment_base_model['target_crn'] = 'testString'
        deployment_base_model['service_crn'] = 'testString'
        deployment_base_model['mccp_id'] = 'testString'
        deployment_base_model['broker'] = broker_model
        deployment_base_model['supports_rc_migration'] = True
        deployment_base_model['target_network'] = 'testString'

        # Construct a dict representation of a PlanMetaData model
        plan_meta_data_model = {}
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a PricingSet model
        pricing_set_model = {}
        pricing_set_model['type'] = 'testString'
        pricing_set_model['origin'] = 'testString'
        pricing_set_model['starting_price'] = starting_price_model

        # Construct a dict representation of a SLAMetaData model
        sla_meta_data_model = {}
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        # Construct a dict representation of a TemplateMetaData model
        template_meta_data_model = {}
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        # Construct a dict representation of a ObjectMetadataSet model
        object_metadata_set_model = {}
        object_metadata_set_model['rc_compatible'] = True
        object_metadata_set_model['service'] = cf_meta_data_model
        object_metadata_set_model['plan'] = plan_meta_data_model
        object_metadata_set_model['alias'] = alias_meta_data_model
        object_metadata_set_model['template'] = template_meta_data_model
        object_metadata_set_model['ui'] = ui_meta_data_model
        object_metadata_set_model['compliance'] = ['testString']
        object_metadata_set_model['sla'] = sla_meta_data_model
        object_metadata_set_model['callbacks'] = callbacks_model
        object_metadata_set_model['original_name'] = 'testString'
        object_metadata_set_model['version'] = 'testString'
        object_metadata_set_model['other'] = {}
        object_metadata_set_model['pricing'] = pricing_set_model
        object_metadata_set_model['deployment'] = deployment_base_model

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        kind = 'service'
        overview_ui = overview_ui_model
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        parent_id = 'testString'
        group = True
        active = True
        metadata = object_metadata_set_model

        # Invoke method
        response = service.update_catalog_entry(
            id,
            name,
            kind,
            overview_ui,
            images,
            disabled,
            tags,
            provider,
            parent_id=parent_id,
            group=group,
            active=active,
            metadata=metadata,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['kind'] == 'service'
        assert req_body['overview_ui'] == overview_ui_model
        assert req_body['images'] == image_model
        assert req_body['disabled'] == True
        assert req_body['tags'] == ['testString']
        assert req_body['provider'] == provider_model
        assert req_body['parent_id'] == 'testString'
        assert req_body['group'] == True
        assert req_body['active'] == True
        assert req_body['metadata'] == object_metadata_set_model


    #--------------------------------------------------------
    # test_update_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/testString'
        mock_response = '{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'
        overview_model['featured_description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a Broker model
        broker_model = {}
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        # Construct a dict representation of a DRMetaData model
        dr_meta_data_model = {}
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a SourceMetaData model
        source_meta_data_model = {}
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        # Construct a dict representation of a AliasMetaData model
        alias_meta_data_model = {}
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        # Construct a dict representation of a CFMetaData model
        cf_meta_data_model = {}
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        # Construct a dict representation of a DeploymentBase model
        deployment_base_model = {}
        deployment_base_model['location'] = 'testString'
        deployment_base_model['location_url'] = 'testString'
        deployment_base_model['original_location'] = 'testString'
        deployment_base_model['target_crn'] = 'testString'
        deployment_base_model['service_crn'] = 'testString'
        deployment_base_model['mccp_id'] = 'testString'
        deployment_base_model['broker'] = broker_model
        deployment_base_model['supports_rc_migration'] = True
        deployment_base_model['target_network'] = 'testString'

        # Construct a dict representation of a PlanMetaData model
        plan_meta_data_model = {}
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        # Construct a dict representation of a PricingSet model
        pricing_set_model = {}
        pricing_set_model['type'] = 'testString'
        pricing_set_model['origin'] = 'testString'
        pricing_set_model['starting_price'] = starting_price_model

        # Construct a dict representation of a SLAMetaData model
        sla_meta_data_model = {}
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        # Construct a dict representation of a TemplateMetaData model
        template_meta_data_model = {}
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        # Construct a dict representation of a ObjectMetadataSet model
        object_metadata_set_model = {}
        object_metadata_set_model['rc_compatible'] = True
        object_metadata_set_model['service'] = cf_meta_data_model
        object_metadata_set_model['plan'] = plan_meta_data_model
        object_metadata_set_model['alias'] = alias_meta_data_model
        object_metadata_set_model['template'] = template_meta_data_model
        object_metadata_set_model['ui'] = ui_meta_data_model
        object_metadata_set_model['compliance'] = ['testString']
        object_metadata_set_model['sla'] = sla_meta_data_model
        object_metadata_set_model['callbacks'] = callbacks_model
        object_metadata_set_model['original_name'] = 'testString'
        object_metadata_set_model['version'] = 'testString'
        object_metadata_set_model['other'] = {}
        object_metadata_set_model['pricing'] = pricing_set_model
        object_metadata_set_model['deployment'] = deployment_base_model

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        kind = 'service'
        overview_ui = overview_ui_model
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        parent_id = 'testString'
        group = True
        active = True
        metadata = object_metadata_set_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "name": name,
            "kind": kind,
            "overview_ui": overview_ui,
            "images": images,
            "disabled": disabled,
            "tags": tags,
            "provider": provider,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_catalog_entry(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_catalog_entry
#-----------------------------------------------------------------------------
class TestDeleteCatalogEntry():

    #--------------------------------------------------------
    # delete_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'
        account = 'testString'
        force = True

        # Invoke method
        response = service.delete_catalog_entry(
            id,
            account=account,
            force=force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'force={}'.format('true' if force else 'false') in query_string


    #--------------------------------------------------------
    # test_delete_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_catalog_entry(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_catalog_entry(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_child_objects
#-----------------------------------------------------------------------------
class TestGetChildObjects():

    #--------------------------------------------------------
    # get_child_objects()
    #--------------------------------------------------------
    @responses.activate
    def test_get_child_objects_all_params(self):
        # Set up mock
        url = base_url + '/testString/testString'
        mock_response = '{"offset": 6, "limit": 5, "count": 5, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        kind = 'testString'
        account = 'testString'
        include = 'testString'
        q = 'testString'
        sort_by = 'testString'
        descending = 'testString'
        languages = 'testString'
        complete = 'testString'

        # Invoke method
        response = service.get_child_objects(
            id,
            kind,
            account=account,
            include=include,
            q=q,
            sort_by=sort_by,
            descending=descending,
            languages=languages,
            complete=complete,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'include={}'.format(include) in query_string
        assert 'q={}'.format(q) in query_string
        assert 'sort-by={}'.format(sort_by) in query_string
        assert 'descending={}'.format(descending) in query_string
        assert 'languages={}'.format(languages) in query_string
        assert 'complete={}'.format(complete) in query_string


    #--------------------------------------------------------
    # test_get_child_objects_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_child_objects_required_params(self):
        # Set up mock
        url = base_url + '/testString/testString'
        mock_response = '{"offset": 6, "limit": 5, "count": 5, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        kind = 'testString'

        # Invoke method
        response = service.get_child_objects(
            id,
            kind,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_child_objects_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_child_objects_value_error(self):
        # Set up mock
        url = base_url + '/testString/testString'
        mock_response = '{"offset": 6, "limit": 5, "count": 5, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"name": "name", "kind": "service", "overview_ui": {}, "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "disabled": true, "tags": ["tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "active": true, "metadata": {"rc_compatible": false, "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "bindable": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false, "cf_guid": {"mapKey": "inner"}}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": {"mapKey": "inner"}}, "alias": {"type": "type", "plan_id": "plan_id"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"mapKey": "inner"}}, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url", "dashboard_url": "dashboard_url", "registration_url": "registration_url", "apidocsurl": "apidocsurl"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00", "hidden": true, "hide_lite_metering": true, "no_upgrade_next_step": true}, "compliance": ["compliance"], "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"controller_url": "controller_url", "broker_url": "broker_url", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "api_endpoint": {"mapKey": "inner"}}, "original_name": "original_name", "version": "version", "other": {"mapKey": {"anyKey": "anyValue"}}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "deployment": {"location": "location", "location_url": "location_url", "original_location": "original_location", "target_crn": "target_crn", "service_crn": "service_crn", "mccp_id": "mccp_id", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false, "target_network": "target_network"}}, "id": "id", "catalog_crn": {"anyKey": "anyValue"}, "url": {"anyKey": "anyValue"}, "children_url": {"anyKey": "anyValue"}, "geo_tags": {"anyKey": "anyValue"}, "pricing_tags": {"anyKey": "anyValue"}, "created": {"anyKey": "anyValue"}, "updated": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        kind = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "kind": kind,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_child_objects(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for restore_catalog_entry
#-----------------------------------------------------------------------------
class TestRestoreCatalogEntry():

    #--------------------------------------------------------
    # restore_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_restore_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/testString/restore'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.restore_catalog_entry(
            id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_restore_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_restore_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString/restore'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.restore_catalog_entry(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_restore_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_restore_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/testString/restore'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.restore_catalog_entry(**req_copy)



# endregion
##############################################################################
# End of Service: Object
##############################################################################

##############################################################################
# Start of Service: Visibility
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_visibility
#-----------------------------------------------------------------------------
class TestGetVisibility():

    #--------------------------------------------------------
    # get_visibility()
    #--------------------------------------------------------
    @responses.activate
    def test_get_visibility_all_params(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        mock_response = '{"restrictions": "restrictions", "owner": "owner", "extendable": true, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.get_visibility(
            id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_get_visibility_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_visibility_required_params(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        mock_response = '{"restrictions": "restrictions", "owner": "owner", "extendable": true, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_visibility(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_visibility_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_visibility_value_error(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        mock_response = '{"restrictions": "restrictions", "owner": "owner", "extendable": true, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_visibility(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_visibility
#-----------------------------------------------------------------------------
class TestUpdateVisibility():

    #--------------------------------------------------------
    # update_visibility()
    #--------------------------------------------------------
    @responses.activate
    def test_update_visibility_all_params(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model = {}
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        # Construct a dict representation of a VisibilityDetail model
        visibility_detail_model = {}
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        # Set up parameter values
        id = 'testString'
        extendable = True
        include = visibility_detail_model
        exclude = visibility_detail_model
        account = 'testString'

        # Invoke method
        response = service.update_visibility(
            id,
            extendable=extendable,
            include=include,
            exclude=exclude,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['extendable'] == True
        assert req_body['include'] == visibility_detail_model
        assert req_body['exclude'] == visibility_detail_model


    #--------------------------------------------------------
    # test_update_visibility_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_visibility_required_params(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model = {}
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        # Construct a dict representation of a VisibilityDetail model
        visibility_detail_model = {}
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        # Set up parameter values
        id = 'testString'
        extendable = True
        include = visibility_detail_model
        exclude = visibility_detail_model

        # Invoke method
        response = service.update_visibility(
            id,
            extendable=extendable,
            include=include,
            exclude=exclude,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['extendable'] == True
        assert req_body['include'] == visibility_detail_model
        assert req_body['exclude'] == visibility_detail_model


    #--------------------------------------------------------
    # test_update_visibility_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_visibility_value_error(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model = {}
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        # Construct a dict representation of a VisibilityDetail model
        visibility_detail_model = {}
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        # Set up parameter values
        id = 'testString'
        extendable = True
        include = visibility_detail_model
        exclude = visibility_detail_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_visibility(**req_copy)



# endregion
##############################################################################
# End of Service: Visibility
##############################################################################

##############################################################################
# Start of Service: Pricing
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_pricing
#-----------------------------------------------------------------------------
class TestGetPricing():

    #--------------------------------------------------------
    # get_pricing()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pricing_all_params(self):
        # Set up mock
        url = base_url + '/testString/pricing'
        mock_response = '{"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.get_pricing(
            id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_get_pricing_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pricing_required_params(self):
        # Set up mock
        url = base_url + '/testString/pricing'
        mock_response = '{"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_pricing(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_pricing_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pricing_value_error(self):
        # Set up mock
        url = base_url + '/testString/pricing'
        mock_response = '{"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "unit": "unit", "amount": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"part_ref": "part_ref", "metric_id": "metric_id", "tier_model": "tier_model", "charge_unit": "charge_unit", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "display_cap": 11, "effective_from": "2019-01-01T12:00:00", "effective_until": "2019-01-01T12:00:00", "amounts": [{"country": "country", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_pricing(**req_copy)



# endregion
##############################################################################
# End of Service: Pricing
##############################################################################

##############################################################################
# Start of Service: Audit
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_audit_logs
#-----------------------------------------------------------------------------
class TestGetAuditLogs():

    #--------------------------------------------------------
    # get_audit_logs()
    #--------------------------------------------------------
    @responses.activate
    def test_get_audit_logs_all_params(self):
        # Set up mock
        url = base_url + '/testString/logs'
        mock_response = '{"offset": 6, "limit": 5, "count": 5, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "effective": {"restrictions": "restrictions", "owner": "owner", "extendable": true, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}, "time": "2019-01-01T12:00:00", "who_id": "who_id", "who_name": "who_name", "who_email": "who_email", "instance": "instance", "gid": "gid", "type": "type", "message": "message", "data": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        account = 'testString'
        ascending = 'testString'
        startat = 'testString'
        offset = 38
        limit = 38

        # Invoke method
        response = service.get_audit_logs(
            id,
            account=account,
            ascending=ascending,
            startat=startat,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'ascending={}'.format(ascending) in query_string
        assert 'startat={}'.format(startat) in query_string
        assert '_offset={}'.format(offset) in query_string
        assert '_limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_get_audit_logs_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_audit_logs_required_params(self):
        # Set up mock
        url = base_url + '/testString/logs'
        mock_response = '{"offset": 6, "limit": 5, "count": 5, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "effective": {"restrictions": "restrictions", "owner": "owner", "extendable": true, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}, "time": "2019-01-01T12:00:00", "who_id": "who_id", "who_name": "who_name", "who_email": "who_email", "instance": "instance", "gid": "gid", "type": "type", "message": "message", "data": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_audit_logs(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_audit_logs_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_audit_logs_value_error(self):
        # Set up mock
        url = base_url + '/testString/logs'
        mock_response = '{"offset": 6, "limit": 5, "count": 5, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "effective": {"restrictions": "restrictions", "owner": "owner", "extendable": true, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}, "time": "2019-01-01T12:00:00", "who_id": "who_id", "who_name": "who_name", "who_email": "who_email", "instance": "instance", "gid": "gid", "type": "type", "message": "message", "data": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_audit_logs(**req_copy)



# endregion
##############################################################################
# End of Service: Audit
##############################################################################

##############################################################################
# Start of Service: Artifact
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_artifacts
#-----------------------------------------------------------------------------
class TestListArtifacts():

    #--------------------------------------------------------
    # list_artifacts()
    #--------------------------------------------------------
    @responses.activate
    def test_list_artifacts_all_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts'
        mock_response = '{"count": 5, "resources": [{"name": "name", "updated": "2019-01-01T12:00:00", "url": "url", "etag": "etag", "size": 4}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.list_artifacts(
            object_id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_list_artifacts_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_artifacts_required_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts'
        mock_response = '{"count": 5, "resources": [{"name": "name", "updated": "2019-01-01T12:00:00", "url": "url", "etag": "etag", "size": 4}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        object_id = 'testString'

        # Invoke method
        response = service.list_artifacts(
            object_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_artifacts_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_artifacts_value_error(self):
        # Set up mock
        url = base_url + '/testString/artifacts'
        mock_response = '{"count": 5, "resources": [{"name": "name", "updated": "2019-01-01T12:00:00", "url": "url", "etag": "etag", "size": 4}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        object_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "object_id": object_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_artifacts(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_artifact
#-----------------------------------------------------------------------------
class TestGetArtifact():

    #--------------------------------------------------------
    # get_artifact()
    #--------------------------------------------------------
    @responses.activate
    def test_get_artifact_all_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        mock_response = 'Contents of response byte-stream...'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.get_artifact(
            object_id,
            artifact_id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_get_artifact_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_artifact_required_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        mock_response = 'Contents of response byte-stream...'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Invoke method
        response = service.get_artifact(
            object_id,
            artifact_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_artifact_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_artifact_value_error(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        mock_response = 'Contents of response byte-stream...'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "object_id": object_id,
            "artifact_id": artifact_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_artifact(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for upload_artifact
#-----------------------------------------------------------------------------
class TestUploadArtifact():

    #--------------------------------------------------------
    # upload_artifact()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_artifact_all_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'
        artifact = io.BytesIO(b'This is a mock file.').getvalue()
        content_type = 'testString'
        account = 'testString'

        # Invoke method
        response = service.upload_artifact(
            object_id,
            artifact_id,
            artifact=artifact,
            content_type=content_type,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        # Validate body params


    #--------------------------------------------------------
    # test_upload_artifact_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_artifact_required_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Invoke method
        response = service.upload_artifact(
            object_id,
            artifact_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_upload_artifact_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_artifact_value_error(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "object_id": object_id,
            "artifact_id": artifact_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.upload_artifact(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_artifact
#-----------------------------------------------------------------------------
class TestDeleteArtifact():

    #--------------------------------------------------------
    # delete_artifact()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_artifact_all_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.delete_artifact(
            object_id,
            artifact_id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_delete_artifact_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_artifact_required_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Invoke method
        response = service.delete_artifact(
            object_id,
            artifact_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_artifact_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_artifact_value_error(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "object_id": object_id,
            "artifact_id": artifact_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_artifact(**req_copy)



# endregion
##############################################################################
# End of Service: Artifact
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for AliasMetaData
#-----------------------------------------------------------------------------
class TestAliasMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for AliasMetaData
    #--------------------------------------------------------
    def test_alias_meta_data_serialization(self):

        # Construct a json representation of a AliasMetaData model
        alias_meta_data_model_json = {}
        alias_meta_data_model_json['type'] = 'testString'
        alias_meta_data_model_json['plan_id'] = 'testString'

        # Construct a model instance of AliasMetaData by calling from_dict on the json representation
        alias_meta_data_model = AliasMetaData.from_dict(alias_meta_data_model_json)
        assert alias_meta_data_model != False

        # Construct a model instance of AliasMetaData by calling from_dict on the json representation
        alias_meta_data_model_dict = AliasMetaData.from_dict(alias_meta_data_model_json).__dict__
        alias_meta_data_model2 = AliasMetaData(**alias_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert alias_meta_data_model == alias_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        alias_meta_data_model_json2 = alias_meta_data_model.to_dict()
        assert alias_meta_data_model_json2 == alias_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for Amount
#-----------------------------------------------------------------------------
class TestAmount():

    #--------------------------------------------------------
    # Test serialization/deserialization for Amount
    #--------------------------------------------------------
    def test_amount_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a json representation of a Amount model
        amount_model_json = {}
        amount_model_json['country'] = 'testString'
        amount_model_json['currency'] = 'testString'
        amount_model_json['prices'] = [price_model]

        # Construct a model instance of Amount by calling from_dict on the json representation
        amount_model = Amount.from_dict(amount_model_json)
        assert amount_model != False

        # Construct a model instance of Amount by calling from_dict on the json representation
        amount_model_dict = Amount.from_dict(amount_model_json).__dict__
        amount_model2 = Amount(**amount_model_dict)

        # Verify the model instances are equivalent
        assert amount_model == amount_model2

        # Convert model instance back to dict and verify no loss of data
        amount_model_json2 = amount_model.to_dict()
        assert amount_model_json2 == amount_model_json

#-----------------------------------------------------------------------------
# Test Class for Artifact
#-----------------------------------------------------------------------------
class TestArtifact():

    #--------------------------------------------------------
    # Test serialization/deserialization for Artifact
    #--------------------------------------------------------
    def test_artifact_serialization(self):

        # Construct a json representation of a Artifact model
        artifact_model_json = {}
        artifact_model_json['name'] = 'testString'
        artifact_model_json['updated'] = '2020-01-28T18:40:40.123456Z'
        artifact_model_json['url'] = 'testString'
        artifact_model_json['etag'] = 'testString'
        artifact_model_json['size'] = 38

        # Construct a model instance of Artifact by calling from_dict on the json representation
        artifact_model = Artifact.from_dict(artifact_model_json)
        assert artifact_model != False

        # Construct a model instance of Artifact by calling from_dict on the json representation
        artifact_model_dict = Artifact.from_dict(artifact_model_json).__dict__
        artifact_model2 = Artifact(**artifact_model_dict)

        # Verify the model instances are equivalent
        assert artifact_model == artifact_model2

        # Convert model instance back to dict and verify no loss of data
        artifact_model_json2 = artifact_model.to_dict()
        assert artifact_model_json2 == artifact_model_json

#-----------------------------------------------------------------------------
# Test Class for Artifacts
#-----------------------------------------------------------------------------
class TestArtifacts():

    #--------------------------------------------------------
    # Test serialization/deserialization for Artifacts
    #--------------------------------------------------------
    def test_artifacts_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        artifact_model = {} # Artifact
        artifact_model['name'] = 'testString'
        artifact_model['updated'] = '2020-01-28T18:40:40.123456Z'
        artifact_model['url'] = 'testString'
        artifact_model['etag'] = 'testString'
        artifact_model['size'] = 38

        # Construct a json representation of a Artifacts model
        artifacts_model_json = {}
        artifacts_model_json['count'] = 38
        artifacts_model_json['resources'] = [artifact_model]

        # Construct a model instance of Artifacts by calling from_dict on the json representation
        artifacts_model = Artifacts.from_dict(artifacts_model_json)
        assert artifacts_model != False

        # Construct a model instance of Artifacts by calling from_dict on the json representation
        artifacts_model_dict = Artifacts.from_dict(artifacts_model_json).__dict__
        artifacts_model2 = Artifacts(**artifacts_model_dict)

        # Verify the model instances are equivalent
        assert artifacts_model == artifacts_model2

        # Convert model instance back to dict and verify no loss of data
        artifacts_model_json2 = artifacts_model.to_dict()
        assert artifacts_model_json2 == artifacts_model_json

#-----------------------------------------------------------------------------
# Test Class for AuditSearchResult
#-----------------------------------------------------------------------------
class TestAuditSearchResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for AuditSearchResult
    #--------------------------------------------------------
    def test_audit_search_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        visibility_detail_accounts_model = {} # VisibilityDetailAccounts
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        visibility_detail_model = {} # VisibilityDetail
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        visibility_model = {} # Visibility
        visibility_model['restrictions'] = 'testString'
        visibility_model['owner'] = 'testString'
        visibility_model['extendable'] = True
        visibility_model['include'] = visibility_detail_model
        visibility_model['exclude'] = visibility_detail_model
        visibility_model['approved'] = True

        message_model = {} # Message
        message_model['id'] = 'testString'
        message_model['effective'] = visibility_model
        message_model['time'] = '2020-01-28T18:40:40.123456Z'
        message_model['who_id'] = 'testString'
        message_model['who_name'] = 'testString'
        message_model['who_email'] = 'testString'
        message_model['instance'] = 'testString'
        message_model['gid'] = 'testString'
        message_model['type'] = 'testString'
        message_model['message'] = 'testString'
        message_model['data'] = { 'foo': 'bar' }

        # Construct a json representation of a AuditSearchResult model
        audit_search_result_model_json = {}
        audit_search_result_model_json['offset'] = 38
        audit_search_result_model_json['limit'] = 38
        audit_search_result_model_json['count'] = 38
        audit_search_result_model_json['resource_count'] = 38
        audit_search_result_model_json['first'] = 'testString'
        audit_search_result_model_json['last'] = 'testString'
        audit_search_result_model_json['prev'] = 'testString'
        audit_search_result_model_json['next'] = 'testString'
        audit_search_result_model_json['resources'] = [message_model]

        # Construct a model instance of AuditSearchResult by calling from_dict on the json representation
        audit_search_result_model = AuditSearchResult.from_dict(audit_search_result_model_json)
        assert audit_search_result_model != False

        # Construct a model instance of AuditSearchResult by calling from_dict on the json representation
        audit_search_result_model_dict = AuditSearchResult.from_dict(audit_search_result_model_json).__dict__
        audit_search_result_model2 = AuditSearchResult(**audit_search_result_model_dict)

        # Verify the model instances are equivalent
        assert audit_search_result_model == audit_search_result_model2

        # Convert model instance back to dict and verify no loss of data
        audit_search_result_model_json2 = audit_search_result_model.to_dict()
        assert audit_search_result_model_json2 == audit_search_result_model_json

#-----------------------------------------------------------------------------
# Test Class for Broker
#-----------------------------------------------------------------------------
class TestBroker():

    #--------------------------------------------------------
    # Test serialization/deserialization for Broker
    #--------------------------------------------------------
    def test_broker_serialization(self):

        # Construct a json representation of a Broker model
        broker_model_json = {}
        broker_model_json['name'] = 'testString'
        broker_model_json['guid'] = 'testString'

        # Construct a model instance of Broker by calling from_dict on the json representation
        broker_model = Broker.from_dict(broker_model_json)
        assert broker_model != False

        # Construct a model instance of Broker by calling from_dict on the json representation
        broker_model_dict = Broker.from_dict(broker_model_json).__dict__
        broker_model2 = Broker(**broker_model_dict)

        # Verify the model instances are equivalent
        assert broker_model == broker_model2

        # Convert model instance back to dict and verify no loss of data
        broker_model_json2 = broker_model.to_dict()
        assert broker_model_json2 == broker_model_json

#-----------------------------------------------------------------------------
# Test Class for Bullets
#-----------------------------------------------------------------------------
class TestBullets():

    #--------------------------------------------------------
    # Test serialization/deserialization for Bullets
    #--------------------------------------------------------
    def test_bullets_serialization(self):

        # Construct a json representation of a Bullets model
        bullets_model_json = {}
        bullets_model_json['title'] = 'testString'
        bullets_model_json['description'] = 'testString'
        bullets_model_json['icon'] = 'testString'
        bullets_model_json['quantity'] = 38

        # Construct a model instance of Bullets by calling from_dict on the json representation
        bullets_model = Bullets.from_dict(bullets_model_json)
        assert bullets_model != False

        # Construct a model instance of Bullets by calling from_dict on the json representation
        bullets_model_dict = Bullets.from_dict(bullets_model_json).__dict__
        bullets_model2 = Bullets(**bullets_model_dict)

        # Verify the model instances are equivalent
        assert bullets_model == bullets_model2

        # Convert model instance back to dict and verify no loss of data
        bullets_model_json2 = bullets_model.to_dict()
        assert bullets_model_json2 == bullets_model_json

#-----------------------------------------------------------------------------
# Test Class for CFMetaData
#-----------------------------------------------------------------------------
class TestCFMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for CFMetaData
    #--------------------------------------------------------
    def test_cf_meta_data_serialization(self):

        # Construct a json representation of a CFMetaData model
        cf_meta_data_model_json = {}
        cf_meta_data_model_json['type'] = 'testString'
        cf_meta_data_model_json['iam_compatible'] = True
        cf_meta_data_model_json['unique_api_key'] = True
        cf_meta_data_model_json['provisionable'] = True
        cf_meta_data_model_json['bindable'] = True
        cf_meta_data_model_json['async_provisioning_supported'] = True
        cf_meta_data_model_json['async_unprovisioning_supported'] = True
        cf_meta_data_model_json['requires'] = ['testString']
        cf_meta_data_model_json['plan_updateable'] = True
        cf_meta_data_model_json['state'] = 'testString'
        cf_meta_data_model_json['service_check_enabled'] = True
        cf_meta_data_model_json['test_check_interval'] = 38
        cf_meta_data_model_json['service_key_supported'] = True
        cf_meta_data_model_json['cf_guid'] = {}

        # Construct a model instance of CFMetaData by calling from_dict on the json representation
        cf_meta_data_model = CFMetaData.from_dict(cf_meta_data_model_json)
        assert cf_meta_data_model != False

        # Construct a model instance of CFMetaData by calling from_dict on the json representation
        cf_meta_data_model_dict = CFMetaData.from_dict(cf_meta_data_model_json).__dict__
        cf_meta_data_model2 = CFMetaData(**cf_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert cf_meta_data_model == cf_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        cf_meta_data_model_json2 = cf_meta_data_model.to_dict()
        assert cf_meta_data_model_json2 == cf_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for Callbacks
#-----------------------------------------------------------------------------
class TestCallbacks():

    #--------------------------------------------------------
    # Test serialization/deserialization for Callbacks
    #--------------------------------------------------------
    def test_callbacks_serialization(self):

        # Construct a json representation of a Callbacks model
        callbacks_model_json = {}
        callbacks_model_json['controller_url'] = 'testString'
        callbacks_model_json['broker_url'] = 'testString'
        callbacks_model_json['broker_proxy_url'] = 'testString'
        callbacks_model_json['dashboard_url'] = 'testString'
        callbacks_model_json['dashboard_data_url'] = 'testString'
        callbacks_model_json['dashboard_detail_tab_url'] = 'testString'
        callbacks_model_json['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model_json['service_monitor_api'] = 'testString'
        callbacks_model_json['service_monitor_app'] = 'testString'
        callbacks_model_json['api_endpoint'] = {}

        # Construct a model instance of Callbacks by calling from_dict on the json representation
        callbacks_model = Callbacks.from_dict(callbacks_model_json)
        assert callbacks_model != False

        # Construct a model instance of Callbacks by calling from_dict on the json representation
        callbacks_model_dict = Callbacks.from_dict(callbacks_model_json).__dict__
        callbacks_model2 = Callbacks(**callbacks_model_dict)

        # Verify the model instances are equivalent
        assert callbacks_model == callbacks_model2

        # Convert model instance back to dict and verify no loss of data
        callbacks_model_json2 = callbacks_model.to_dict()
        assert callbacks_model_json2 == callbacks_model_json

#-----------------------------------------------------------------------------
# Test Class for CatalogEntry
#-----------------------------------------------------------------------------
class TestCatalogEntry():

    #--------------------------------------------------------
    # Test serialization/deserialization for CatalogEntry
    #--------------------------------------------------------
    def test_catalog_entry_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        amount_model = {} # Amount
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        broker_model = {} # Broker
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        dr_meta_data_model = {} # DRMetaData
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        i18_n_model = {} # I18N
        i18_n_model['foo'] = strings_model

        metrics_model = {} # Metrics
        metrics_model['part_ref'] = 'testString'
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['display_cap'] = 38
        metrics_model['effective_from'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['effective_until'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['amounts'] = [amount_model]

        source_meta_data_model = {} # SourceMetaData
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        urls_model = {} # URLS
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        alias_meta_data_model = {} # AliasMetaData
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        cf_meta_data_model = {} # CFMetaData
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        callbacks_model = {} # Callbacks
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        catalog_entry_metadata_deployment_model = {} # CatalogEntryMetadataDeployment
        catalog_entry_metadata_deployment_model['location'] = 'testString'
        catalog_entry_metadata_deployment_model['location_url'] = 'testString'
        catalog_entry_metadata_deployment_model['original_location'] = 'testString'
        catalog_entry_metadata_deployment_model['target_crn'] = 'testString'
        catalog_entry_metadata_deployment_model['service_crn'] = 'testString'
        catalog_entry_metadata_deployment_model['mccp_id'] = 'testString'
        catalog_entry_metadata_deployment_model['broker'] = broker_model
        catalog_entry_metadata_deployment_model['supports_rc_migration'] = True
        catalog_entry_metadata_deployment_model['target_network'] = 'testString'

        catalog_entry_metadata_pricing_model = {} # CatalogEntryMetadataPricing
        catalog_entry_metadata_pricing_model['type'] = 'testString'
        catalog_entry_metadata_pricing_model['origin'] = 'testString'
        catalog_entry_metadata_pricing_model['starting_price'] = starting_price_model
        catalog_entry_metadata_pricing_model['metrics'] = [metrics_model]

        overview_model = {} # Overview
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'
        overview_model['featured_description'] = 'testString'

        plan_meta_data_model = {} # PlanMetaData
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        sla_meta_data_model = {} # SLAMetaData
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        template_meta_data_model = {} # TemplateMetaData
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        ui_meta_data_model = {} # UIMetaData
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        catalog_entry_metadata_model = {} # CatalogEntryMetadata
        catalog_entry_metadata_model['rc_compatible'] = True
        catalog_entry_metadata_model['service'] = cf_meta_data_model
        catalog_entry_metadata_model['plan'] = plan_meta_data_model
        catalog_entry_metadata_model['alias'] = alias_meta_data_model
        catalog_entry_metadata_model['template'] = template_meta_data_model
        catalog_entry_metadata_model['ui'] = ui_meta_data_model
        catalog_entry_metadata_model['compliance'] = ['testString']
        catalog_entry_metadata_model['sla'] = sla_meta_data_model
        catalog_entry_metadata_model['callbacks'] = callbacks_model
        catalog_entry_metadata_model['original_name'] = 'testString'
        catalog_entry_metadata_model['version'] = 'testString'
        catalog_entry_metadata_model['other'] = {}
        catalog_entry_metadata_model['pricing'] = catalog_entry_metadata_pricing_model
        catalog_entry_metadata_model['deployment'] = catalog_entry_metadata_deployment_model

        image_model = {} # Image
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        overview_ui_model = {} # OverviewUI
        overview_ui_model['foo'] = overview_model

        provider_model = {} # Provider
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a json representation of a CatalogEntry model
        catalog_entry_model_json = {}
        catalog_entry_model_json['name'] = 'testString'
        catalog_entry_model_json['kind'] = 'service'
        catalog_entry_model_json['overview_ui'] = overview_ui_model
        catalog_entry_model_json['images'] = image_model
        catalog_entry_model_json['parent_id'] = 'testString'
        catalog_entry_model_json['disabled'] = True
        catalog_entry_model_json['tags'] = ['testString']
        catalog_entry_model_json['group'] = True
        catalog_entry_model_json['provider'] = provider_model
        catalog_entry_model_json['active'] = True
        catalog_entry_model_json['metadata'] = catalog_entry_metadata_model
        catalog_entry_model_json['id'] = 'testString'
        catalog_entry_model_json['catalog_crn'] = { 'foo': 'bar' }
        catalog_entry_model_json['url'] = { 'foo': 'bar' }
        catalog_entry_model_json['children_url'] = { 'foo': 'bar' }
        catalog_entry_model_json['geo_tags'] = { 'foo': 'bar' }
        catalog_entry_model_json['pricing_tags'] = { 'foo': 'bar' }
        catalog_entry_model_json['created'] = { 'foo': 'bar' }
        catalog_entry_model_json['updated'] = { 'foo': 'bar' }

        # Construct a model instance of CatalogEntry by calling from_dict on the json representation
        catalog_entry_model = CatalogEntry.from_dict(catalog_entry_model_json)
        assert catalog_entry_model != False

        # Construct a model instance of CatalogEntry by calling from_dict on the json representation
        catalog_entry_model_dict = CatalogEntry.from_dict(catalog_entry_model_json).__dict__
        catalog_entry_model2 = CatalogEntry(**catalog_entry_model_dict)

        # Verify the model instances are equivalent
        assert catalog_entry_model == catalog_entry_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_entry_model_json2 = catalog_entry_model.to_dict()
        assert catalog_entry_model_json2 == catalog_entry_model_json

#-----------------------------------------------------------------------------
# Test Class for CatalogEntryMetadata
#-----------------------------------------------------------------------------
class TestCatalogEntryMetadata():

    #--------------------------------------------------------
    # Test serialization/deserialization for CatalogEntryMetadata
    #--------------------------------------------------------
    def test_catalog_entry_metadata_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        amount_model = {} # Amount
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        broker_model = {} # Broker
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        dr_meta_data_model = {} # DRMetaData
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        i18_n_model = {} # I18N
        i18_n_model['foo'] = strings_model

        metrics_model = {} # Metrics
        metrics_model['part_ref'] = 'testString'
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['display_cap'] = 38
        metrics_model['effective_from'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['effective_until'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['amounts'] = [amount_model]

        source_meta_data_model = {} # SourceMetaData
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        urls_model = {} # URLS
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        alias_meta_data_model = {} # AliasMetaData
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        cf_meta_data_model = {} # CFMetaData
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        callbacks_model = {} # Callbacks
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        catalog_entry_metadata_deployment_model = {} # CatalogEntryMetadataDeployment
        catalog_entry_metadata_deployment_model['location'] = 'testString'
        catalog_entry_metadata_deployment_model['location_url'] = 'testString'
        catalog_entry_metadata_deployment_model['original_location'] = 'testString'
        catalog_entry_metadata_deployment_model['target_crn'] = 'testString'
        catalog_entry_metadata_deployment_model['service_crn'] = 'testString'
        catalog_entry_metadata_deployment_model['mccp_id'] = 'testString'
        catalog_entry_metadata_deployment_model['broker'] = broker_model
        catalog_entry_metadata_deployment_model['supports_rc_migration'] = True
        catalog_entry_metadata_deployment_model['target_network'] = 'testString'

        catalog_entry_metadata_pricing_model = {} # CatalogEntryMetadataPricing
        catalog_entry_metadata_pricing_model['type'] = 'testString'
        catalog_entry_metadata_pricing_model['origin'] = 'testString'
        catalog_entry_metadata_pricing_model['starting_price'] = starting_price_model
        catalog_entry_metadata_pricing_model['metrics'] = [metrics_model]

        plan_meta_data_model = {} # PlanMetaData
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        sla_meta_data_model = {} # SLAMetaData
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        template_meta_data_model = {} # TemplateMetaData
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        ui_meta_data_model = {} # UIMetaData
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        # Construct a json representation of a CatalogEntryMetadata model
        catalog_entry_metadata_model_json = {}
        catalog_entry_metadata_model_json['rc_compatible'] = True
        catalog_entry_metadata_model_json['service'] = cf_meta_data_model
        catalog_entry_metadata_model_json['plan'] = plan_meta_data_model
        catalog_entry_metadata_model_json['alias'] = alias_meta_data_model
        catalog_entry_metadata_model_json['template'] = template_meta_data_model
        catalog_entry_metadata_model_json['ui'] = ui_meta_data_model
        catalog_entry_metadata_model_json['compliance'] = ['testString']
        catalog_entry_metadata_model_json['sla'] = sla_meta_data_model
        catalog_entry_metadata_model_json['callbacks'] = callbacks_model
        catalog_entry_metadata_model_json['original_name'] = 'testString'
        catalog_entry_metadata_model_json['version'] = 'testString'
        catalog_entry_metadata_model_json['other'] = {}
        catalog_entry_metadata_model_json['pricing'] = catalog_entry_metadata_pricing_model
        catalog_entry_metadata_model_json['deployment'] = catalog_entry_metadata_deployment_model

        # Construct a model instance of CatalogEntryMetadata by calling from_dict on the json representation
        catalog_entry_metadata_model = CatalogEntryMetadata.from_dict(catalog_entry_metadata_model_json)
        assert catalog_entry_metadata_model != False

        # Construct a model instance of CatalogEntryMetadata by calling from_dict on the json representation
        catalog_entry_metadata_model_dict = CatalogEntryMetadata.from_dict(catalog_entry_metadata_model_json).__dict__
        catalog_entry_metadata_model2 = CatalogEntryMetadata(**catalog_entry_metadata_model_dict)

        # Verify the model instances are equivalent
        assert catalog_entry_metadata_model == catalog_entry_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_entry_metadata_model_json2 = catalog_entry_metadata_model.to_dict()
        assert catalog_entry_metadata_model_json2 == catalog_entry_metadata_model_json

#-----------------------------------------------------------------------------
# Test Class for CatalogEntryMetadataDeployment
#-----------------------------------------------------------------------------
class TestCatalogEntryMetadataDeployment():

    #--------------------------------------------------------
    # Test serialization/deserialization for CatalogEntryMetadataDeployment
    #--------------------------------------------------------
    def test_catalog_entry_metadata_deployment_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        broker_model = {} # Broker
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        # Construct a json representation of a CatalogEntryMetadataDeployment model
        catalog_entry_metadata_deployment_model_json = {}
        catalog_entry_metadata_deployment_model_json['location'] = 'testString'
        catalog_entry_metadata_deployment_model_json['location_url'] = 'testString'
        catalog_entry_metadata_deployment_model_json['original_location'] = 'testString'
        catalog_entry_metadata_deployment_model_json['target_crn'] = 'testString'
        catalog_entry_metadata_deployment_model_json['service_crn'] = 'testString'
        catalog_entry_metadata_deployment_model_json['mccp_id'] = 'testString'
        catalog_entry_metadata_deployment_model_json['broker'] = broker_model
        catalog_entry_metadata_deployment_model_json['supports_rc_migration'] = True
        catalog_entry_metadata_deployment_model_json['target_network'] = 'testString'

        # Construct a model instance of CatalogEntryMetadataDeployment by calling from_dict on the json representation
        catalog_entry_metadata_deployment_model = CatalogEntryMetadataDeployment.from_dict(catalog_entry_metadata_deployment_model_json)
        assert catalog_entry_metadata_deployment_model != False

        # Construct a model instance of CatalogEntryMetadataDeployment by calling from_dict on the json representation
        catalog_entry_metadata_deployment_model_dict = CatalogEntryMetadataDeployment.from_dict(catalog_entry_metadata_deployment_model_json).__dict__
        catalog_entry_metadata_deployment_model2 = CatalogEntryMetadataDeployment(**catalog_entry_metadata_deployment_model_dict)

        # Verify the model instances are equivalent
        assert catalog_entry_metadata_deployment_model == catalog_entry_metadata_deployment_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_entry_metadata_deployment_model_json2 = catalog_entry_metadata_deployment_model.to_dict()
        assert catalog_entry_metadata_deployment_model_json2 == catalog_entry_metadata_deployment_model_json

#-----------------------------------------------------------------------------
# Test Class for CatalogEntryMetadataPricing
#-----------------------------------------------------------------------------
class TestCatalogEntryMetadataPricing():

    #--------------------------------------------------------
    # Test serialization/deserialization for CatalogEntryMetadataPricing
    #--------------------------------------------------------
    def test_catalog_entry_metadata_pricing_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        amount_model = {} # Amount
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        metrics_model = {} # Metrics
        metrics_model['part_ref'] = 'testString'
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['display_cap'] = 38
        metrics_model['effective_from'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['effective_until'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['amounts'] = [amount_model]

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a json representation of a CatalogEntryMetadataPricing model
        catalog_entry_metadata_pricing_model_json = {}
        catalog_entry_metadata_pricing_model_json['type'] = 'testString'
        catalog_entry_metadata_pricing_model_json['origin'] = 'testString'
        catalog_entry_metadata_pricing_model_json['starting_price'] = starting_price_model
        catalog_entry_metadata_pricing_model_json['metrics'] = [metrics_model]

        # Construct a model instance of CatalogEntryMetadataPricing by calling from_dict on the json representation
        catalog_entry_metadata_pricing_model = CatalogEntryMetadataPricing.from_dict(catalog_entry_metadata_pricing_model_json)
        assert catalog_entry_metadata_pricing_model != False

        # Construct a model instance of CatalogEntryMetadataPricing by calling from_dict on the json representation
        catalog_entry_metadata_pricing_model_dict = CatalogEntryMetadataPricing.from_dict(catalog_entry_metadata_pricing_model_json).__dict__
        catalog_entry_metadata_pricing_model2 = CatalogEntryMetadataPricing(**catalog_entry_metadata_pricing_model_dict)

        # Verify the model instances are equivalent
        assert catalog_entry_metadata_pricing_model == catalog_entry_metadata_pricing_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_entry_metadata_pricing_model_json2 = catalog_entry_metadata_pricing_model.to_dict()
        assert catalog_entry_metadata_pricing_model_json2 == catalog_entry_metadata_pricing_model_json

#-----------------------------------------------------------------------------
# Test Class for DRMetaData
#-----------------------------------------------------------------------------
class TestDRMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for DRMetaData
    #--------------------------------------------------------
    def test_dr_meta_data_serialization(self):

        # Construct a json representation of a DRMetaData model
        dr_meta_data_model_json = {}
        dr_meta_data_model_json['dr'] = True
        dr_meta_data_model_json['description'] = 'testString'

        # Construct a model instance of DRMetaData by calling from_dict on the json representation
        dr_meta_data_model = DRMetaData.from_dict(dr_meta_data_model_json)
        assert dr_meta_data_model != False

        # Construct a model instance of DRMetaData by calling from_dict on the json representation
        dr_meta_data_model_dict = DRMetaData.from_dict(dr_meta_data_model_json).__dict__
        dr_meta_data_model2 = DRMetaData(**dr_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert dr_meta_data_model == dr_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        dr_meta_data_model_json2 = dr_meta_data_model.to_dict()
        assert dr_meta_data_model_json2 == dr_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for DeploymentBase
#-----------------------------------------------------------------------------
class TestDeploymentBase():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeploymentBase
    #--------------------------------------------------------
    def test_deployment_base_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        broker_model = {} # Broker
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        # Construct a json representation of a DeploymentBase model
        deployment_base_model_json = {}
        deployment_base_model_json['location'] = 'testString'
        deployment_base_model_json['location_url'] = 'testString'
        deployment_base_model_json['original_location'] = 'testString'
        deployment_base_model_json['target_crn'] = 'testString'
        deployment_base_model_json['service_crn'] = 'testString'
        deployment_base_model_json['mccp_id'] = 'testString'
        deployment_base_model_json['broker'] = broker_model
        deployment_base_model_json['supports_rc_migration'] = True
        deployment_base_model_json['target_network'] = 'testString'

        # Construct a model instance of DeploymentBase by calling from_dict on the json representation
        deployment_base_model = DeploymentBase.from_dict(deployment_base_model_json)
        assert deployment_base_model != False

        # Construct a model instance of DeploymentBase by calling from_dict on the json representation
        deployment_base_model_dict = DeploymentBase.from_dict(deployment_base_model_json).__dict__
        deployment_base_model2 = DeploymentBase(**deployment_base_model_dict)

        # Verify the model instances are equivalent
        assert deployment_base_model == deployment_base_model2

        # Convert model instance back to dict and verify no loss of data
        deployment_base_model_json2 = deployment_base_model.to_dict()
        assert deployment_base_model_json2 == deployment_base_model_json

#-----------------------------------------------------------------------------
# Test Class for EntrySearchResult
#-----------------------------------------------------------------------------
class TestEntrySearchResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for EntrySearchResult
    #--------------------------------------------------------
    def test_entry_search_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        amount_model = {} # Amount
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        broker_model = {} # Broker
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        dr_meta_data_model = {} # DRMetaData
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        i18_n_model = {} # I18N
        i18_n_model['foo'] = strings_model

        metrics_model = {} # Metrics
        metrics_model['part_ref'] = 'testString'
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['display_cap'] = 38
        metrics_model['effective_from'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['effective_until'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['amounts'] = [amount_model]

        source_meta_data_model = {} # SourceMetaData
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        urls_model = {} # URLS
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        alias_meta_data_model = {} # AliasMetaData
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        cf_meta_data_model = {} # CFMetaData
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        callbacks_model = {} # Callbacks
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        catalog_entry_metadata_deployment_model = {} # CatalogEntryMetadataDeployment
        catalog_entry_metadata_deployment_model['location'] = 'testString'
        catalog_entry_metadata_deployment_model['location_url'] = 'testString'
        catalog_entry_metadata_deployment_model['original_location'] = 'testString'
        catalog_entry_metadata_deployment_model['target_crn'] = 'testString'
        catalog_entry_metadata_deployment_model['service_crn'] = 'testString'
        catalog_entry_metadata_deployment_model['mccp_id'] = 'testString'
        catalog_entry_metadata_deployment_model['broker'] = broker_model
        catalog_entry_metadata_deployment_model['supports_rc_migration'] = True
        catalog_entry_metadata_deployment_model['target_network'] = 'testString'

        catalog_entry_metadata_pricing_model = {} # CatalogEntryMetadataPricing
        catalog_entry_metadata_pricing_model['type'] = 'testString'
        catalog_entry_metadata_pricing_model['origin'] = 'testString'
        catalog_entry_metadata_pricing_model['starting_price'] = starting_price_model
        catalog_entry_metadata_pricing_model['metrics'] = [metrics_model]

        overview_model = {} # Overview
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'
        overview_model['featured_description'] = 'testString'

        plan_meta_data_model = {} # PlanMetaData
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        sla_meta_data_model = {} # SLAMetaData
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        template_meta_data_model = {} # TemplateMetaData
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        ui_meta_data_model = {} # UIMetaData
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        catalog_entry_metadata_model = {} # CatalogEntryMetadata
        catalog_entry_metadata_model['rc_compatible'] = True
        catalog_entry_metadata_model['service'] = cf_meta_data_model
        catalog_entry_metadata_model['plan'] = plan_meta_data_model
        catalog_entry_metadata_model['alias'] = alias_meta_data_model
        catalog_entry_metadata_model['template'] = template_meta_data_model
        catalog_entry_metadata_model['ui'] = ui_meta_data_model
        catalog_entry_metadata_model['compliance'] = ['testString']
        catalog_entry_metadata_model['sla'] = sla_meta_data_model
        catalog_entry_metadata_model['callbacks'] = callbacks_model
        catalog_entry_metadata_model['original_name'] = 'testString'
        catalog_entry_metadata_model['version'] = 'testString'
        catalog_entry_metadata_model['other'] = {}
        catalog_entry_metadata_model['pricing'] = catalog_entry_metadata_pricing_model
        catalog_entry_metadata_model['deployment'] = catalog_entry_metadata_deployment_model

        image_model = {} # Image
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        overview_ui_model = {} # OverviewUI
        overview_ui_model['foo'] = overview_model

        provider_model = {} # Provider
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        catalog_entry_model = {} # CatalogEntry
        catalog_entry_model['name'] = 'testString'
        catalog_entry_model['kind'] = 'service'
        catalog_entry_model['overview_ui'] = overview_ui_model
        catalog_entry_model['images'] = image_model
        catalog_entry_model['parent_id'] = 'testString'
        catalog_entry_model['disabled'] = True
        catalog_entry_model['tags'] = ['testString']
        catalog_entry_model['group'] = True
        catalog_entry_model['provider'] = provider_model
        catalog_entry_model['active'] = True
        catalog_entry_model['metadata'] = catalog_entry_metadata_model
        catalog_entry_model['id'] = 'testString'
        catalog_entry_model['catalog_crn'] = { 'foo': 'bar' }
        catalog_entry_model['url'] = { 'foo': 'bar' }
        catalog_entry_model['children_url'] = { 'foo': 'bar' }
        catalog_entry_model['geo_tags'] = { 'foo': 'bar' }
        catalog_entry_model['pricing_tags'] = { 'foo': 'bar' }
        catalog_entry_model['created'] = { 'foo': 'bar' }
        catalog_entry_model['updated'] = { 'foo': 'bar' }

        # Construct a json representation of a EntrySearchResult model
        entry_search_result_model_json = {}
        entry_search_result_model_json['offset'] = 38
        entry_search_result_model_json['limit'] = 38
        entry_search_result_model_json['count'] = 38
        entry_search_result_model_json['resource_count'] = 38
        entry_search_result_model_json['first'] = 'testString'
        entry_search_result_model_json['last'] = 'testString'
        entry_search_result_model_json['prev'] = 'testString'
        entry_search_result_model_json['next'] = 'testString'
        entry_search_result_model_json['resources'] = [catalog_entry_model]

        # Construct a model instance of EntrySearchResult by calling from_dict on the json representation
        entry_search_result_model = EntrySearchResult.from_dict(entry_search_result_model_json)
        assert entry_search_result_model != False

        # Construct a model instance of EntrySearchResult by calling from_dict on the json representation
        entry_search_result_model_dict = EntrySearchResult.from_dict(entry_search_result_model_json).__dict__
        entry_search_result_model2 = EntrySearchResult(**entry_search_result_model_dict)

        # Verify the model instances are equivalent
        assert entry_search_result_model == entry_search_result_model2

        # Convert model instance back to dict and verify no loss of data
        entry_search_result_model_json2 = entry_search_result_model.to_dict()
        assert entry_search_result_model_json2 == entry_search_result_model_json

#-----------------------------------------------------------------------------
# Test Class for I18N
#-----------------------------------------------------------------------------
class TestI18N():

    #--------------------------------------------------------
    # Test serialization/deserialization for I18N
    #--------------------------------------------------------
    def test_i18_n_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a json representation of a I18N model
        i18_n_model_json = {}
        i18_n_model_json['foo'] = strings_model

        # Construct a model instance of I18N by calling from_dict on the json representation
        i18_n_model = I18N.from_dict(i18_n_model_json)
        assert i18_n_model != False

        # Construct a model instance of I18N by calling from_dict on the json representation
        i18_n_model_dict = I18N.from_dict(i18_n_model_json).__dict__
        i18_n_model2 = I18N(**i18_n_model_dict)

        # Verify the model instances are equivalent
        assert i18_n_model == i18_n_model2

        # Convert model instance back to dict and verify no loss of data
        i18_n_model_json2 = i18_n_model.to_dict()
        assert i18_n_model_json2 == i18_n_model_json

#-----------------------------------------------------------------------------
# Test Class for Image
#-----------------------------------------------------------------------------
class TestImage():

    #--------------------------------------------------------
    # Test serialization/deserialization for Image
    #--------------------------------------------------------
    def test_image_serialization(self):

        # Construct a json representation of a Image model
        image_model_json = {}
        image_model_json['image'] = 'testString'
        image_model_json['small_image'] = 'testString'
        image_model_json['medium_image'] = 'testString'
        image_model_json['feature_image'] = 'testString'

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model = Image.from_dict(image_model_json)
        assert image_model != False

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model_dict = Image.from_dict(image_model_json).__dict__
        image_model2 = Image(**image_model_dict)

        # Verify the model instances are equivalent
        assert image_model == image_model2

        # Convert model instance back to dict and verify no loss of data
        image_model_json2 = image_model.to_dict()
        assert image_model_json2 == image_model_json

#-----------------------------------------------------------------------------
# Test Class for Message
#-----------------------------------------------------------------------------
class TestMessage():

    #--------------------------------------------------------
    # Test serialization/deserialization for Message
    #--------------------------------------------------------
    def test_message_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        visibility_detail_accounts_model = {} # VisibilityDetailAccounts
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        visibility_detail_model = {} # VisibilityDetail
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        visibility_model = {} # Visibility
        visibility_model['restrictions'] = 'testString'
        visibility_model['owner'] = 'testString'
        visibility_model['extendable'] = True
        visibility_model['include'] = visibility_detail_model
        visibility_model['exclude'] = visibility_detail_model
        visibility_model['approved'] = True

        # Construct a json representation of a Message model
        message_model_json = {}
        message_model_json['id'] = 'testString'
        message_model_json['effective'] = visibility_model
        message_model_json['time'] = '2020-01-28T18:40:40.123456Z'
        message_model_json['who_id'] = 'testString'
        message_model_json['who_name'] = 'testString'
        message_model_json['who_email'] = 'testString'
        message_model_json['instance'] = 'testString'
        message_model_json['gid'] = 'testString'
        message_model_json['type'] = 'testString'
        message_model_json['message'] = 'testString'
        message_model_json['data'] = { 'foo': 'bar' }

        # Construct a model instance of Message by calling from_dict on the json representation
        message_model = Message.from_dict(message_model_json)
        assert message_model != False

        # Construct a model instance of Message by calling from_dict on the json representation
        message_model_dict = Message.from_dict(message_model_json).__dict__
        message_model2 = Message(**message_model_dict)

        # Verify the model instances are equivalent
        assert message_model == message_model2

        # Convert model instance back to dict and verify no loss of data
        message_model_json2 = message_model.to_dict()
        assert message_model_json2 == message_model_json

#-----------------------------------------------------------------------------
# Test Class for Metrics
#-----------------------------------------------------------------------------
class TestMetrics():

    #--------------------------------------------------------
    # Test serialization/deserialization for Metrics
    #--------------------------------------------------------
    def test_metrics_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        amount_model = {} # Amount
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a json representation of a Metrics model
        metrics_model_json = {}
        metrics_model_json['part_ref'] = 'testString'
        metrics_model_json['metric_id'] = 'testString'
        metrics_model_json['tier_model'] = 'testString'
        metrics_model_json['charge_unit'] = 'testString'
        metrics_model_json['charge_unit_name'] = 'testString'
        metrics_model_json['charge_unit_quantity'] = 'testString'
        metrics_model_json['resource_display_name'] = 'testString'
        metrics_model_json['charge_unit_display_name'] = 'testString'
        metrics_model_json['usage_cap_qty'] = 38
        metrics_model_json['display_cap'] = 38
        metrics_model_json['effective_from'] = '2020-01-28T18:40:40.123456Z'
        metrics_model_json['effective_until'] = '2020-01-28T18:40:40.123456Z'
        metrics_model_json['amounts'] = [amount_model]

        # Construct a model instance of Metrics by calling from_dict on the json representation
        metrics_model = Metrics.from_dict(metrics_model_json)
        assert metrics_model != False

        # Construct a model instance of Metrics by calling from_dict on the json representation
        metrics_model_dict = Metrics.from_dict(metrics_model_json).__dict__
        metrics_model2 = Metrics(**metrics_model_dict)

        # Verify the model instances are equivalent
        assert metrics_model == metrics_model2

        # Convert model instance back to dict and verify no loss of data
        metrics_model_json2 = metrics_model.to_dict()
        assert metrics_model_json2 == metrics_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetadataSet
#-----------------------------------------------------------------------------
class TestObjectMetadataSet():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetadataSet
    #--------------------------------------------------------
    def test_object_metadata_set_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        amount_model = {} # Amount
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        broker_model = {} # Broker
        broker_model['name'] = 'testString'
        broker_model['guid'] = 'testString'

        dr_meta_data_model = {} # DRMetaData
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        i18_n_model = {} # I18N
        i18_n_model['foo'] = strings_model

        source_meta_data_model = {} # SourceMetaData
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        urls_model = {} # URLS
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        alias_meta_data_model = {} # AliasMetaData
        alias_meta_data_model['type'] = 'testString'
        alias_meta_data_model['plan_id'] = 'testString'

        cf_meta_data_model = {} # CFMetaData
        cf_meta_data_model['type'] = 'testString'
        cf_meta_data_model['iam_compatible'] = True
        cf_meta_data_model['unique_api_key'] = True
        cf_meta_data_model['provisionable'] = True
        cf_meta_data_model['bindable'] = True
        cf_meta_data_model['async_provisioning_supported'] = True
        cf_meta_data_model['async_unprovisioning_supported'] = True
        cf_meta_data_model['requires'] = ['testString']
        cf_meta_data_model['plan_updateable'] = True
        cf_meta_data_model['state'] = 'testString'
        cf_meta_data_model['service_check_enabled'] = True
        cf_meta_data_model['test_check_interval'] = 38
        cf_meta_data_model['service_key_supported'] = True
        cf_meta_data_model['cf_guid'] = {}

        callbacks_model = {} # Callbacks
        callbacks_model['controller_url'] = 'testString'
        callbacks_model['broker_url'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['api_endpoint'] = {}

        deployment_base_model = {} # DeploymentBase
        deployment_base_model['location'] = 'testString'
        deployment_base_model['location_url'] = 'testString'
        deployment_base_model['original_location'] = 'testString'
        deployment_base_model['target_crn'] = 'testString'
        deployment_base_model['service_crn'] = 'testString'
        deployment_base_model['mccp_id'] = 'testString'
        deployment_base_model['broker'] = broker_model
        deployment_base_model['supports_rc_migration'] = True
        deployment_base_model['target_network'] = 'testString'

        plan_meta_data_model = {} # PlanMetaData
        plan_meta_data_model['bindable'] = True
        plan_meta_data_model['reservable'] = True
        plan_meta_data_model['allow_internal_users'] = True
        plan_meta_data_model['async_provisioning_supported'] = True
        plan_meta_data_model['async_unprovisioning_supported'] = True
        plan_meta_data_model['test_check_interval'] = 38
        plan_meta_data_model['single_scope_instance'] = 'testString'
        plan_meta_data_model['service_check_enabled'] = True
        plan_meta_data_model['cf_guid'] = {}

        pricing_set_model = {} # PricingSet
        pricing_set_model['type'] = 'testString'
        pricing_set_model['origin'] = 'testString'
        pricing_set_model['starting_price'] = starting_price_model

        sla_meta_data_model = {} # SLAMetaData
        sla_meta_data_model['terms'] = 'testString'
        sla_meta_data_model['tenancy'] = 'testString'
        sla_meta_data_model['provisioning'] = 'testString'
        sla_meta_data_model['responsiveness'] = 'testString'
        sla_meta_data_model['dr'] = dr_meta_data_model

        template_meta_data_model = {} # TemplateMetaData
        template_meta_data_model['services'] = ['testString']
        template_meta_data_model['default_memory'] = 38
        template_meta_data_model['start_cmd'] = 'testString'
        template_meta_data_model['source'] = source_meta_data_model
        template_meta_data_model['runtime_catalog_id'] = 'testString'
        template_meta_data_model['cf_runtime_id'] = 'testString'
        template_meta_data_model['template_id'] = 'testString'
        template_meta_data_model['executable_file'] = 'testString'
        template_meta_data_model['buildpack'] = 'testString'
        template_meta_data_model['environment_variables'] = {}

        ui_meta_data_model = {} # UIMetaData
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model['hidden'] = True
        ui_meta_data_model['hide_lite_metering'] = True
        ui_meta_data_model['no_upgrade_next_step'] = True

        # Construct a json representation of a ObjectMetadataSet model
        object_metadata_set_model_json = {}
        object_metadata_set_model_json['rc_compatible'] = True
        object_metadata_set_model_json['service'] = cf_meta_data_model
        object_metadata_set_model_json['plan'] = plan_meta_data_model
        object_metadata_set_model_json['alias'] = alias_meta_data_model
        object_metadata_set_model_json['template'] = template_meta_data_model
        object_metadata_set_model_json['ui'] = ui_meta_data_model
        object_metadata_set_model_json['compliance'] = ['testString']
        object_metadata_set_model_json['sla'] = sla_meta_data_model
        object_metadata_set_model_json['callbacks'] = callbacks_model
        object_metadata_set_model_json['original_name'] = 'testString'
        object_metadata_set_model_json['version'] = 'testString'
        object_metadata_set_model_json['other'] = {}
        object_metadata_set_model_json['pricing'] = pricing_set_model
        object_metadata_set_model_json['deployment'] = deployment_base_model

        # Construct a model instance of ObjectMetadataSet by calling from_dict on the json representation
        object_metadata_set_model = ObjectMetadataSet.from_dict(object_metadata_set_model_json)
        assert object_metadata_set_model != False

        # Construct a model instance of ObjectMetadataSet by calling from_dict on the json representation
        object_metadata_set_model_dict = ObjectMetadataSet.from_dict(object_metadata_set_model_json).__dict__
        object_metadata_set_model2 = ObjectMetadataSet(**object_metadata_set_model_dict)

        # Verify the model instances are equivalent
        assert object_metadata_set_model == object_metadata_set_model2

        # Convert model instance back to dict and verify no loss of data
        object_metadata_set_model_json2 = object_metadata_set_model.to_dict()
        assert object_metadata_set_model_json2 == object_metadata_set_model_json

#-----------------------------------------------------------------------------
# Test Class for Overview
#-----------------------------------------------------------------------------
class TestOverview():

    #--------------------------------------------------------
    # Test serialization/deserialization for Overview
    #--------------------------------------------------------
    def test_overview_serialization(self):

        # Construct a json representation of a Overview model
        overview_model_json = {}
        overview_model_json['display_name'] = 'testString'
        overview_model_json['long_description'] = 'testString'
        overview_model_json['description'] = 'testString'
        overview_model_json['featured_description'] = 'testString'

        # Construct a model instance of Overview by calling from_dict on the json representation
        overview_model = Overview.from_dict(overview_model_json)
        assert overview_model != False

        # Construct a model instance of Overview by calling from_dict on the json representation
        overview_model_dict = Overview.from_dict(overview_model_json).__dict__
        overview_model2 = Overview(**overview_model_dict)

        # Verify the model instances are equivalent
        assert overview_model == overview_model2

        # Convert model instance back to dict and verify no loss of data
        overview_model_json2 = overview_model.to_dict()
        assert overview_model_json2 == overview_model_json

#-----------------------------------------------------------------------------
# Test Class for OverviewUI
#-----------------------------------------------------------------------------
class TestOverviewUI():

    #--------------------------------------------------------
    # Test serialization/deserialization for OverviewUI
    #--------------------------------------------------------
    def test_overview_ui_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        overview_model = {} # Overview
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'
        overview_model['featured_description'] = 'testString'

        # Construct a json representation of a OverviewUI model
        overview_ui_model_json = {}
        overview_ui_model_json['foo'] = overview_model

        # Construct a model instance of OverviewUI by calling from_dict on the json representation
        overview_ui_model = OverviewUI.from_dict(overview_ui_model_json)
        assert overview_ui_model != False

        # Construct a model instance of OverviewUI by calling from_dict on the json representation
        overview_ui_model_dict = OverviewUI.from_dict(overview_ui_model_json).__dict__
        overview_ui_model2 = OverviewUI(**overview_ui_model_dict)

        # Verify the model instances are equivalent
        assert overview_ui_model == overview_ui_model2

        # Convert model instance back to dict and verify no loss of data
        overview_ui_model_json2 = overview_ui_model.to_dict()
        assert overview_ui_model_json2 == overview_ui_model_json

#-----------------------------------------------------------------------------
# Test Class for PlanMetaData
#-----------------------------------------------------------------------------
class TestPlanMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for PlanMetaData
    #--------------------------------------------------------
    def test_plan_meta_data_serialization(self):

        # Construct a json representation of a PlanMetaData model
        plan_meta_data_model_json = {}
        plan_meta_data_model_json['bindable'] = True
        plan_meta_data_model_json['reservable'] = True
        plan_meta_data_model_json['allow_internal_users'] = True
        plan_meta_data_model_json['async_provisioning_supported'] = True
        plan_meta_data_model_json['async_unprovisioning_supported'] = True
        plan_meta_data_model_json['test_check_interval'] = 38
        plan_meta_data_model_json['single_scope_instance'] = 'testString'
        plan_meta_data_model_json['service_check_enabled'] = True
        plan_meta_data_model_json['cf_guid'] = {}

        # Construct a model instance of PlanMetaData by calling from_dict on the json representation
        plan_meta_data_model = PlanMetaData.from_dict(plan_meta_data_model_json)
        assert plan_meta_data_model != False

        # Construct a model instance of PlanMetaData by calling from_dict on the json representation
        plan_meta_data_model_dict = PlanMetaData.from_dict(plan_meta_data_model_json).__dict__
        plan_meta_data_model2 = PlanMetaData(**plan_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert plan_meta_data_model == plan_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        plan_meta_data_model_json2 = plan_meta_data_model.to_dict()
        assert plan_meta_data_model_json2 == plan_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for Price
#-----------------------------------------------------------------------------
class TestPrice():

    #--------------------------------------------------------
    # Test serialization/deserialization for Price
    #--------------------------------------------------------
    def test_price_serialization(self):

        # Construct a json representation of a Price model
        price_model_json = {}
        price_model_json['quantity_tier'] = 38
        price_model_json['Price'] = 36.0

        # Construct a model instance of Price by calling from_dict on the json representation
        price_model = Price.from_dict(price_model_json)
        assert price_model != False

        # Construct a model instance of Price by calling from_dict on the json representation
        price_model_dict = Price.from_dict(price_model_json).__dict__
        price_model2 = Price(**price_model_dict)

        # Verify the model instances are equivalent
        assert price_model == price_model2

        # Convert model instance back to dict and verify no loss of data
        price_model_json2 = price_model.to_dict()
        assert price_model_json2 == price_model_json

#-----------------------------------------------------------------------------
# Test Class for PricingGet
#-----------------------------------------------------------------------------
class TestPricingGet():

    #--------------------------------------------------------
    # Test serialization/deserialization for PricingGet
    #--------------------------------------------------------
    def test_pricing_get_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        amount_model = {} # Amount
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        metrics_model = {} # Metrics
        metrics_model['part_ref'] = 'testString'
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['display_cap'] = 38
        metrics_model['effective_from'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['effective_until'] = '2020-01-28T18:40:40.123456Z'
        metrics_model['amounts'] = [amount_model]

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a json representation of a PricingGet model
        pricing_get_model_json = {}
        pricing_get_model_json['type'] = 'testString'
        pricing_get_model_json['origin'] = 'testString'
        pricing_get_model_json['starting_price'] = starting_price_model
        pricing_get_model_json['metrics'] = [metrics_model]

        # Construct a model instance of PricingGet by calling from_dict on the json representation
        pricing_get_model = PricingGet.from_dict(pricing_get_model_json)
        assert pricing_get_model != False

        # Construct a model instance of PricingGet by calling from_dict on the json representation
        pricing_get_model_dict = PricingGet.from_dict(pricing_get_model_json).__dict__
        pricing_get_model2 = PricingGet(**pricing_get_model_dict)

        # Verify the model instances are equivalent
        assert pricing_get_model == pricing_get_model2

        # Convert model instance back to dict and verify no loss of data
        pricing_get_model_json2 = pricing_get_model.to_dict()
        assert pricing_get_model_json2 == pricing_get_model_json

#-----------------------------------------------------------------------------
# Test Class for PricingSet
#-----------------------------------------------------------------------------
class TestPricingSet():

    #--------------------------------------------------------
    # Test serialization/deserialization for PricingSet
    #--------------------------------------------------------
    def test_pricing_set_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        amount_model = {} # Amount
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['unit'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a json representation of a PricingSet model
        pricing_set_model_json = {}
        pricing_set_model_json['type'] = 'testString'
        pricing_set_model_json['origin'] = 'testString'
        pricing_set_model_json['starting_price'] = starting_price_model

        # Construct a model instance of PricingSet by calling from_dict on the json representation
        pricing_set_model = PricingSet.from_dict(pricing_set_model_json)
        assert pricing_set_model != False

        # Construct a model instance of PricingSet by calling from_dict on the json representation
        pricing_set_model_dict = PricingSet.from_dict(pricing_set_model_json).__dict__
        pricing_set_model2 = PricingSet(**pricing_set_model_dict)

        # Verify the model instances are equivalent
        assert pricing_set_model == pricing_set_model2

        # Convert model instance back to dict and verify no loss of data
        pricing_set_model_json2 = pricing_set_model.to_dict()
        assert pricing_set_model_json2 == pricing_set_model_json

#-----------------------------------------------------------------------------
# Test Class for Provider
#-----------------------------------------------------------------------------
class TestProvider():

    #--------------------------------------------------------
    # Test serialization/deserialization for Provider
    #--------------------------------------------------------
    def test_provider_serialization(self):

        # Construct a json representation of a Provider model
        provider_model_json = {}
        provider_model_json['email'] = 'testString'
        provider_model_json['name'] = 'testString'
        provider_model_json['contact'] = 'testString'
        provider_model_json['support_email'] = 'testString'
        provider_model_json['phone'] = 'testString'

        # Construct a model instance of Provider by calling from_dict on the json representation
        provider_model = Provider.from_dict(provider_model_json)
        assert provider_model != False

        # Construct a model instance of Provider by calling from_dict on the json representation
        provider_model_dict = Provider.from_dict(provider_model_json).__dict__
        provider_model2 = Provider(**provider_model_dict)

        # Verify the model instances are equivalent
        assert provider_model == provider_model2

        # Convert model instance back to dict and verify no loss of data
        provider_model_json2 = provider_model.to_dict()
        assert provider_model_json2 == provider_model_json

#-----------------------------------------------------------------------------
# Test Class for SLAMetaData
#-----------------------------------------------------------------------------
class TestSLAMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for SLAMetaData
    #--------------------------------------------------------
    def test_sla_meta_data_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        dr_meta_data_model = {} # DRMetaData
        dr_meta_data_model['dr'] = True
        dr_meta_data_model['description'] = 'testString'

        # Construct a json representation of a SLAMetaData model
        sla_meta_data_model_json = {}
        sla_meta_data_model_json['terms'] = 'testString'
        sla_meta_data_model_json['tenancy'] = 'testString'
        sla_meta_data_model_json['provisioning'] = 'testString'
        sla_meta_data_model_json['responsiveness'] = 'testString'
        sla_meta_data_model_json['dr'] = dr_meta_data_model

        # Construct a model instance of SLAMetaData by calling from_dict on the json representation
        sla_meta_data_model = SLAMetaData.from_dict(sla_meta_data_model_json)
        assert sla_meta_data_model != False

        # Construct a model instance of SLAMetaData by calling from_dict on the json representation
        sla_meta_data_model_dict = SLAMetaData.from_dict(sla_meta_data_model_json).__dict__
        sla_meta_data_model2 = SLAMetaData(**sla_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert sla_meta_data_model == sla_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        sla_meta_data_model_json2 = sla_meta_data_model.to_dict()
        assert sla_meta_data_model_json2 == sla_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for SourceMetaData
#-----------------------------------------------------------------------------
class TestSourceMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for SourceMetaData
    #--------------------------------------------------------
    def test_source_meta_data_serialization(self):

        # Construct a json representation of a SourceMetaData model
        source_meta_data_model_json = {}
        source_meta_data_model_json['path'] = 'testString'
        source_meta_data_model_json['type'] = 'testString'
        source_meta_data_model_json['url'] = 'testString'

        # Construct a model instance of SourceMetaData by calling from_dict on the json representation
        source_meta_data_model = SourceMetaData.from_dict(source_meta_data_model_json)
        assert source_meta_data_model != False

        # Construct a model instance of SourceMetaData by calling from_dict on the json representation
        source_meta_data_model_dict = SourceMetaData.from_dict(source_meta_data_model_json).__dict__
        source_meta_data_model2 = SourceMetaData(**source_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert source_meta_data_model == source_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        source_meta_data_model_json2 = source_meta_data_model.to_dict()
        assert source_meta_data_model_json2 == source_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for StartingPrice
#-----------------------------------------------------------------------------
class TestStartingPrice():

    #--------------------------------------------------------
    # Test serialization/deserialization for StartingPrice
    #--------------------------------------------------------
    def test_starting_price_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        amount_model = {} # Amount
        amount_model['country'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a json representation of a StartingPrice model
        starting_price_model_json = {}
        starting_price_model_json['plan_id'] = 'testString'
        starting_price_model_json['deployment_id'] = 'testString'
        starting_price_model_json['unit'] = 'testString'
        starting_price_model_json['amount'] = [amount_model]

        # Construct a model instance of StartingPrice by calling from_dict on the json representation
        starting_price_model = StartingPrice.from_dict(starting_price_model_json)
        assert starting_price_model != False

        # Construct a model instance of StartingPrice by calling from_dict on the json representation
        starting_price_model_dict = StartingPrice.from_dict(starting_price_model_json).__dict__
        starting_price_model2 = StartingPrice(**starting_price_model_dict)

        # Verify the model instances are equivalent
        assert starting_price_model == starting_price_model2

        # Convert model instance back to dict and verify no loss of data
        starting_price_model_json2 = starting_price_model.to_dict()
        assert starting_price_model_json2 == starting_price_model_json

#-----------------------------------------------------------------------------
# Test Class for Strings
#-----------------------------------------------------------------------------
class TestStrings():

    #--------------------------------------------------------
    # Test serialization/deserialization for Strings
    #--------------------------------------------------------
    def test_strings_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a json representation of a Strings model
        strings_model_json = {}
        strings_model_json['bullets'] = [bullets_model]
        strings_model_json['media'] = [ui_meta_media_model]
        strings_model_json['not_creatable_msg'] = 'testString'
        strings_model_json['not_creatable__robot_msg'] = 'testString'
        strings_model_json['deprecation_warning'] = 'testString'
        strings_model_json['popup_warning_message'] = 'testString'
        strings_model_json['instruction'] = 'testString'

        # Construct a model instance of Strings by calling from_dict on the json representation
        strings_model = Strings.from_dict(strings_model_json)
        assert strings_model != False

        # Construct a model instance of Strings by calling from_dict on the json representation
        strings_model_dict = Strings.from_dict(strings_model_json).__dict__
        strings_model2 = Strings(**strings_model_dict)

        # Verify the model instances are equivalent
        assert strings_model == strings_model2

        # Convert model instance back to dict and verify no loss of data
        strings_model_json2 = strings_model.to_dict()
        assert strings_model_json2 == strings_model_json

#-----------------------------------------------------------------------------
# Test Class for TemplateMetaData
#-----------------------------------------------------------------------------
class TestTemplateMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for TemplateMetaData
    #--------------------------------------------------------
    def test_template_meta_data_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        source_meta_data_model = {} # SourceMetaData
        source_meta_data_model['path'] = 'testString'
        source_meta_data_model['type'] = 'testString'
        source_meta_data_model['url'] = 'testString'

        # Construct a json representation of a TemplateMetaData model
        template_meta_data_model_json = {}
        template_meta_data_model_json['services'] = ['testString']
        template_meta_data_model_json['default_memory'] = 38
        template_meta_data_model_json['start_cmd'] = 'testString'
        template_meta_data_model_json['source'] = source_meta_data_model
        template_meta_data_model_json['runtime_catalog_id'] = 'testString'
        template_meta_data_model_json['cf_runtime_id'] = 'testString'
        template_meta_data_model_json['template_id'] = 'testString'
        template_meta_data_model_json['executable_file'] = 'testString'
        template_meta_data_model_json['buildpack'] = 'testString'
        template_meta_data_model_json['environment_variables'] = {}

        # Construct a model instance of TemplateMetaData by calling from_dict on the json representation
        template_meta_data_model = TemplateMetaData.from_dict(template_meta_data_model_json)
        assert template_meta_data_model != False

        # Construct a model instance of TemplateMetaData by calling from_dict on the json representation
        template_meta_data_model_dict = TemplateMetaData.from_dict(template_meta_data_model_json).__dict__
        template_meta_data_model2 = TemplateMetaData(**template_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert template_meta_data_model == template_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        template_meta_data_model_json2 = template_meta_data_model.to_dict()
        assert template_meta_data_model_json2 == template_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for UIMetaData
#-----------------------------------------------------------------------------
class TestUIMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for UIMetaData
    #--------------------------------------------------------
    def test_ui_meta_data_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        i18_n_model = {} # I18N
        i18_n_model['foo'] = strings_model

        urls_model = {} # URLS
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'
        urls_model['dashboard_url'] = 'testString'
        urls_model['registration_url'] = 'testString'
        urls_model['apidocsurl'] = 'testString'

        # Construct a json representation of a UIMetaData model
        ui_meta_data_model_json = {}
        ui_meta_data_model_json['strings'] = i18_n_model
        ui_meta_data_model_json['urls'] = urls_model
        ui_meta_data_model_json['embeddable_dashboard'] = 'testString'
        ui_meta_data_model_json['embeddable_dashboard_full_width'] = True
        ui_meta_data_model_json['navigation_order'] = ['testString']
        ui_meta_data_model_json['not_creatable'] = True
        ui_meta_data_model_json['primary_offering_id'] = 'testString'
        ui_meta_data_model_json['accessible_during_provision'] = True
        ui_meta_data_model_json['side_by_side_index'] = 38
        ui_meta_data_model_json['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'
        ui_meta_data_model_json['hidden'] = True
        ui_meta_data_model_json['hide_lite_metering'] = True
        ui_meta_data_model_json['no_upgrade_next_step'] = True

        # Construct a model instance of UIMetaData by calling from_dict on the json representation
        ui_meta_data_model = UIMetaData.from_dict(ui_meta_data_model_json)
        assert ui_meta_data_model != False

        # Construct a model instance of UIMetaData by calling from_dict on the json representation
        ui_meta_data_model_dict = UIMetaData.from_dict(ui_meta_data_model_json).__dict__
        ui_meta_data_model2 = UIMetaData(**ui_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert ui_meta_data_model == ui_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        ui_meta_data_model_json2 = ui_meta_data_model.to_dict()
        assert ui_meta_data_model_json2 == ui_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for UIMetaMedia
#-----------------------------------------------------------------------------
class TestUIMetaMedia():

    #--------------------------------------------------------
    # Test serialization/deserialization for UIMetaMedia
    #--------------------------------------------------------
    def test_ui_meta_media_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 38

        # Construct a json representation of a UIMetaMedia model
        ui_meta_media_model_json = {}
        ui_meta_media_model_json['caption'] = 'testString'
        ui_meta_media_model_json['thumbnail_url'] = 'testString'
        ui_meta_media_model_json['type'] = 'testString'
        ui_meta_media_model_json['URL'] = 'testString'
        ui_meta_media_model_json['source'] = bullets_model

        # Construct a model instance of UIMetaMedia by calling from_dict on the json representation
        ui_meta_media_model = UIMetaMedia.from_dict(ui_meta_media_model_json)
        assert ui_meta_media_model != False

        # Construct a model instance of UIMetaMedia by calling from_dict on the json representation
        ui_meta_media_model_dict = UIMetaMedia.from_dict(ui_meta_media_model_json).__dict__
        ui_meta_media_model2 = UIMetaMedia(**ui_meta_media_model_dict)

        # Verify the model instances are equivalent
        assert ui_meta_media_model == ui_meta_media_model2

        # Convert model instance back to dict and verify no loss of data
        ui_meta_media_model_json2 = ui_meta_media_model.to_dict()
        assert ui_meta_media_model_json2 == ui_meta_media_model_json

#-----------------------------------------------------------------------------
# Test Class for URLS
#-----------------------------------------------------------------------------
class TestURLS():

    #--------------------------------------------------------
    # Test serialization/deserialization for URLS
    #--------------------------------------------------------
    def test_urls_serialization(self):

        # Construct a json representation of a URLS model
        urls_model_json = {}
        urls_model_json['doc_url'] = 'testString'
        urls_model_json['instructions_url'] = 'testString'
        urls_model_json['api_url'] = 'testString'
        urls_model_json['create_url'] = 'testString'
        urls_model_json['sdk_download_url'] = 'testString'
        urls_model_json['terms_url'] = 'testString'
        urls_model_json['custom_create_page_url'] = 'testString'
        urls_model_json['catalog_details_url'] = 'testString'
        urls_model_json['deprecation_doc_url'] = 'testString'
        urls_model_json['dashboard_url'] = 'testString'
        urls_model_json['registration_url'] = 'testString'
        urls_model_json['apidocsurl'] = 'testString'

        # Construct a model instance of URLS by calling from_dict on the json representation
        urls_model = URLS.from_dict(urls_model_json)
        assert urls_model != False

        # Construct a model instance of URLS by calling from_dict on the json representation
        urls_model_dict = URLS.from_dict(urls_model_json).__dict__
        urls_model2 = URLS(**urls_model_dict)

        # Verify the model instances are equivalent
        assert urls_model == urls_model2

        # Convert model instance back to dict and verify no loss of data
        urls_model_json2 = urls_model.to_dict()
        assert urls_model_json2 == urls_model_json

#-----------------------------------------------------------------------------
# Test Class for Visibility
#-----------------------------------------------------------------------------
class TestVisibility():

    #--------------------------------------------------------
    # Test serialization/deserialization for Visibility
    #--------------------------------------------------------
    def test_visibility_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        visibility_detail_accounts_model = {} # VisibilityDetailAccounts
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        visibility_detail_model = {} # VisibilityDetail
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        # Construct a json representation of a Visibility model
        visibility_model_json = {}
        visibility_model_json['restrictions'] = 'testString'
        visibility_model_json['owner'] = 'testString'
        visibility_model_json['extendable'] = True
        visibility_model_json['include'] = visibility_detail_model
        visibility_model_json['exclude'] = visibility_detail_model
        visibility_model_json['approved'] = True

        # Construct a model instance of Visibility by calling from_dict on the json representation
        visibility_model = Visibility.from_dict(visibility_model_json)
        assert visibility_model != False

        # Construct a model instance of Visibility by calling from_dict on the json representation
        visibility_model_dict = Visibility.from_dict(visibility_model_json).__dict__
        visibility_model2 = Visibility(**visibility_model_dict)

        # Verify the model instances are equivalent
        assert visibility_model == visibility_model2

        # Convert model instance back to dict and verify no loss of data
        visibility_model_json2 = visibility_model.to_dict()
        assert visibility_model_json2 == visibility_model_json

#-----------------------------------------------------------------------------
# Test Class for VisibilityDetail
#-----------------------------------------------------------------------------
class TestVisibilityDetail():

    #--------------------------------------------------------
    # Test serialization/deserialization for VisibilityDetail
    #--------------------------------------------------------
    def test_visibility_detail_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        visibility_detail_accounts_model = {} # VisibilityDetailAccounts
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        # Construct a json representation of a VisibilityDetail model
        visibility_detail_model_json = {}
        visibility_detail_model_json['accounts'] = visibility_detail_accounts_model

        # Construct a model instance of VisibilityDetail by calling from_dict on the json representation
        visibility_detail_model = VisibilityDetail.from_dict(visibility_detail_model_json)
        assert visibility_detail_model != False

        # Construct a model instance of VisibilityDetail by calling from_dict on the json representation
        visibility_detail_model_dict = VisibilityDetail.from_dict(visibility_detail_model_json).__dict__
        visibility_detail_model2 = VisibilityDetail(**visibility_detail_model_dict)

        # Verify the model instances are equivalent
        assert visibility_detail_model == visibility_detail_model2

        # Convert model instance back to dict and verify no loss of data
        visibility_detail_model_json2 = visibility_detail_model.to_dict()
        assert visibility_detail_model_json2 == visibility_detail_model_json

#-----------------------------------------------------------------------------
# Test Class for VisibilityDetailAccounts
#-----------------------------------------------------------------------------
class TestVisibilityDetailAccounts():

    #--------------------------------------------------------
    # Test serialization/deserialization for VisibilityDetailAccounts
    #--------------------------------------------------------
    def test_visibility_detail_accounts_serialization(self):

        # Construct a json representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model_json = {}
        visibility_detail_accounts_model_json['_accountid_'] = 'testString'

        # Construct a model instance of VisibilityDetailAccounts by calling from_dict on the json representation
        visibility_detail_accounts_model = VisibilityDetailAccounts.from_dict(visibility_detail_accounts_model_json)
        assert visibility_detail_accounts_model != False

        # Construct a model instance of VisibilityDetailAccounts by calling from_dict on the json representation
        visibility_detail_accounts_model_dict = VisibilityDetailAccounts.from_dict(visibility_detail_accounts_model_json).__dict__
        visibility_detail_accounts_model2 = VisibilityDetailAccounts(**visibility_detail_accounts_model_dict)

        # Verify the model instances are equivalent
        assert visibility_detail_accounts_model == visibility_detail_accounts_model2

        # Convert model instance back to dict and verify no loss of data
        visibility_detail_accounts_model_json2 = visibility_detail_accounts_model.to_dict()
        assert visibility_detail_accounts_model_json2 == visibility_detail_accounts_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
