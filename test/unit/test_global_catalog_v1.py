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
import json
import pytest
import requests
import responses
from platform_services.global_catalog_v1 import *


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
        mock_response = '{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}'
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
            complete=complete
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
        mock_response = '{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}'
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
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString' 
        overview_model['long_description'] = 'testString' 
        overview_model['description'] = 'testString' 

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['language'] = overview_model 

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
        bullets_model['quantity'] = 'testString' 

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38 
        price_model['price'] = 36.0 

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString' 
        ui_meta_media_model['thumbnail_url'] = 'testString' 
        ui_meta_media_model['type'] = 'testString' 
        ui_meta_media_model['url'] = 'testString' 
        ui_meta_media_model['source'] = bullets_model 

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString' 
        amount_model['currency'] = 'testString' 
        amount_model['prices'] = [price_model] 

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString' 
        object_meta_data_deployment_broker_password_model['key'] = 'testString' 
        object_meta_data_deployment_broker_password_model['iv'] = 'testString' 

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model] 
        strings_model['media'] = [ui_meta_media_model] 
        strings_model['not_creatable_msg'] = 'testString' 
        strings_model['not_creatable_robot_msg'] = 'testString' 
        strings_model['deprecation_warning'] = 'testString' 
        strings_model['popup_warning_message'] = 'testString' 
        strings_model['instruction'] = 'testString' 

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['language'] = strings_model 

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString' 
        metrics_model['tier_model'] = 'testString' 
        metrics_model['charge_unit_name'] = 'testString' 
        metrics_model['charge_unit_quantity'] = 'testString' 
        metrics_model['resource_display_name'] = 'testString' 
        metrics_model['charge_unit_display_name'] = 'testString' 
        metrics_model['usage_cap_qty'] = 38 
        metrics_model['amounts'] = [amount_model] 

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString' 
        object_meta_data_deployment_broker_model['guid'] = 'testString' 
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model 

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True 
        object_meta_data_sla_dr_model['description'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['key'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString' 
        object_meta_data_template_source_model['type'] = 'testString' 
        object_meta_data_template_source_model['url'] = 'testString' 

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString' 
        starting_price_model['deployment_id'] = 'testString' 
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

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString' 
        callbacks_model['broker_proxy_url'] = 'testString' 
        callbacks_model['dashboard_url'] = 'testString' 
        callbacks_model['dashboard_data_url'] = 'testString' 
        callbacks_model['dashboard_detail_tab_url'] = 'testString' 
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString' 
        callbacks_model['service_monitor_api'] = 'testString' 
        callbacks_model['service_monitor_app'] = 'testString' 
        callbacks_model['service_staging_url'] = 'testString' 
        callbacks_model['service_production_url'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString' 
        object_meta_data_alias_model['plan_id'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString' 
        object_meta_data_deployment_model['location_url'] = 'testString' 
        object_meta_data_deployment_model['target_crn'] = 'testString' 
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model 
        object_meta_data_deployment_model['supports_rc_migration'] = True 

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True 
        object_meta_data_plan_model['reservable'] = True 
        object_meta_data_plan_model['allow_internal_users'] = True 
        object_meta_data_plan_model['async_provisioning_supported'] = True 
        object_meta_data_plan_model['async_unprovisioning_supported'] = True 
        object_meta_data_plan_model['test_check_interval'] = 38 
        object_meta_data_plan_model['single_scope_instance'] = 'testString' 
        object_meta_data_plan_model['service_check_enabled'] = True 
        object_meta_data_plan_model['cf_guid'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString' 
        object_meta_data_service_model['iam_compatible'] = True 
        object_meta_data_service_model['unique_api_key'] = True 
        object_meta_data_service_model['provisionable'] = True 
        object_meta_data_service_model['async_provisioning_supported'] = True 
        object_meta_data_service_model['async_unprovisioning_supported'] = True 
        object_meta_data_service_model['cf_guid'] = 'testString' 
        object_meta_data_service_model['bindable'] = True 
        object_meta_data_service_model['requires'] = ['testString'] 
        object_meta_data_service_model['plan_updateable'] = True 
        object_meta_data_service_model['state'] = 'testString' 
        object_meta_data_service_model['service_check_enabled'] = True 
        object_meta_data_service_model['test_check_interval'] = 38 
        object_meta_data_service_model['service_key_supported'] = True 

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString' 
        object_meta_data_sla_model['tenancy'] = 'testString' 
        object_meta_data_sla_model['provisioning'] = 'testString' 
        object_meta_data_sla_model['responsiveness'] = 'testString' 
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model 

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString'] 
        object_meta_data_template_model['default_memory'] = 38 
        object_meta_data_template_model['start_cmd'] = 'testString' 
        object_meta_data_template_model['source'] = object_meta_data_template_source_model 
        object_meta_data_template_model['runtime_catalog_id'] = 'testString' 
        object_meta_data_template_model['cf_runtime_id'] = 'testString' 
        object_meta_data_template_model['template_id'] = 'testString' 
        object_meta_data_template_model['executable_file'] = 'testString' 
        object_meta_data_template_model['buildpack'] = 'testString' 
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model 

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString' 
        pricing_model['origin'] = 'testString' 
        pricing_model['starting_price'] = starting_price_model 
        pricing_model['metrics'] = [metrics_model] 

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model 
        ui_meta_data_model['urls'] = urls_model 
        ui_meta_data_model['embeddable_dashboard'] = 'testString' 
        ui_meta_data_model['embeddable_dashboard_full_width'] = True 
        ui_meta_data_model['navigation_order'] = ['testString'] 
        ui_meta_data_model['not_creatable'] = True 
        ui_meta_data_model['reservable'] = True 
        ui_meta_data_model['primary_offering_id'] = 'testString' 
        ui_meta_data_model['accessible_during_provision'] = True 
        ui_meta_data_model['side_by_side_index'] = 38 
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z' 

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True 
        object_meta_data_model['ui'] = ui_meta_data_model 
        object_meta_data_model['pricing'] = pricing_model 
        object_meta_data_model['compliance'] = ['testString'] 
        object_meta_data_model['service'] = object_meta_data_service_model 
        object_meta_data_model['plan'] = object_meta_data_plan_model 
        object_meta_data_model['template'] = object_meta_data_template_model 
        object_meta_data_model['deployment'] = object_meta_data_deployment_model 
        object_meta_data_model['alias'] = object_meta_data_alias_model 
        object_meta_data_model['sla'] = object_meta_data_sla_model 
        object_meta_data_model['callbacks'] = callbacks_model 
        object_meta_data_model['version'] = 'testString' 
        object_meta_data_model['origin_name'] = 'testString' 
        object_meta_data_model['other'] = { 'foo': 'bar' } 

        # Construct a dict representation of a CatalogEntry model
        catalog_entry_model = {}
        catalog_entry_model['id'] = 'testString' 
        catalog_entry_model['catalog_crn'] = 'testString' 
        catalog_entry_model['url'] = 'testString' 
        catalog_entry_model['name'] = 'testString' 
        catalog_entry_model['overview_ui'] = overview_ui_model 
        catalog_entry_model['kind'] = 'testString' 
        catalog_entry_model['images'] = image_model 
        catalog_entry_model['parent_id'] = 'testString' 
        catalog_entry_model['children_url'] = 'testString' 
        catalog_entry_model['parent_url'] = 'testString' 
        catalog_entry_model['disabled'] = True 
        catalog_entry_model['tags'] = ['testString'] 
        catalog_entry_model['geo_tags'] = ['testString'] 
        catalog_entry_model['pricing_tags'] = ['testString'] 
        catalog_entry_model['group'] = True 
        catalog_entry_model['provider'] = provider_model 
        catalog_entry_model['created'] = '2020-01-28T18:40:40.123456Z' 
        catalog_entry_model['updated'] = '2020-01-28T18:40:40.123456Z' 
        catalog_entry_model['metadata'] = object_meta_data_model 
        catalog_entry_model['active'] = True 

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        overview_ui = overview_ui_model
        kind = 'testString'
        images = image_model
        disabled = True
        tags = ['testString']
        geo_tags = ['testString']
        pricing_tags = ['testString']
        group = True
        provider = provider_model
        catalog_crn = 'testString'
        url = 'testString'
        parent_id = 'testString'
        children_url = 'testString'
        parent_url = 'testString'
        created = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        updated = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        metadata = object_meta_data_model
        active = True
        children = [catalog_entry_model]
        account = 'testString'

        # Invoke method
        response = service.create_catalog_entry(
            id,
            name,
            overview_ui,
            kind,
            images,
            disabled,
            tags,
            geo_tags,
            pricing_tags,
            group,
            provider,
            catalog_crn=catalog_crn,
            url=url,
            parent_id=parent_id,
            children_url=children_url,
            parent_url=parent_url,
            created=created,
            updated=updated,
            metadata=metadata,
            active=active,
            children=children,
            account=account
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
        assert req_body['id'] == id
        assert req_body['name'] == name
        assert req_body['overview_ui'] == overview_ui
        assert req_body['kind'] == kind
        assert req_body['images'] == images
        assert req_body['disabled'] == disabled
        assert req_body['tags'] == tags
        assert req_body['geo_tags'] == geo_tags
        assert req_body['pricing_tags'] == pricing_tags
        assert req_body['group'] == group
        assert req_body['provider'] == provider
        assert req_body['catalog_crn'] == catalog_crn
        assert req_body['url'] == url
        assert req_body['parent_id'] == parent_id
        assert req_body['children_url'] == children_url
        assert req_body['parent_url'] == parent_url
        assert req_body['created'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['updated'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['metadata'] == metadata
        assert req_body['active'] == active
        assert req_body['children'] == children


    #--------------------------------------------------------
    # test_create_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/'
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString' 
        overview_model['long_description'] = 'testString' 
        overview_model['description'] = 'testString' 

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['language'] = overview_model 

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
        bullets_model['quantity'] = 'testString' 

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38 
        price_model['price'] = 36.0 

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString' 
        ui_meta_media_model['thumbnail_url'] = 'testString' 
        ui_meta_media_model['type'] = 'testString' 
        ui_meta_media_model['url'] = 'testString' 
        ui_meta_media_model['source'] = bullets_model 

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString' 
        amount_model['currency'] = 'testString' 
        amount_model['prices'] = [price_model] 

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString' 
        object_meta_data_deployment_broker_password_model['key'] = 'testString' 
        object_meta_data_deployment_broker_password_model['iv'] = 'testString' 

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model] 
        strings_model['media'] = [ui_meta_media_model] 
        strings_model['not_creatable_msg'] = 'testString' 
        strings_model['not_creatable_robot_msg'] = 'testString' 
        strings_model['deprecation_warning'] = 'testString' 
        strings_model['popup_warning_message'] = 'testString' 
        strings_model['instruction'] = 'testString' 

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['language'] = strings_model 

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString' 
        metrics_model['tier_model'] = 'testString' 
        metrics_model['charge_unit_name'] = 'testString' 
        metrics_model['charge_unit_quantity'] = 'testString' 
        metrics_model['resource_display_name'] = 'testString' 
        metrics_model['charge_unit_display_name'] = 'testString' 
        metrics_model['usage_cap_qty'] = 38 
        metrics_model['amounts'] = [amount_model] 

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString' 
        object_meta_data_deployment_broker_model['guid'] = 'testString' 
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model 

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True 
        object_meta_data_sla_dr_model['description'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['key'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString' 
        object_meta_data_template_source_model['type'] = 'testString' 
        object_meta_data_template_source_model['url'] = 'testString' 

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString' 
        starting_price_model['deployment_id'] = 'testString' 
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

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString' 
        callbacks_model['broker_proxy_url'] = 'testString' 
        callbacks_model['dashboard_url'] = 'testString' 
        callbacks_model['dashboard_data_url'] = 'testString' 
        callbacks_model['dashboard_detail_tab_url'] = 'testString' 
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString' 
        callbacks_model['service_monitor_api'] = 'testString' 
        callbacks_model['service_monitor_app'] = 'testString' 
        callbacks_model['service_staging_url'] = 'testString' 
        callbacks_model['service_production_url'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString' 
        object_meta_data_alias_model['plan_id'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString' 
        object_meta_data_deployment_model['location_url'] = 'testString' 
        object_meta_data_deployment_model['target_crn'] = 'testString' 
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model 
        object_meta_data_deployment_model['supports_rc_migration'] = True 

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True 
        object_meta_data_plan_model['reservable'] = True 
        object_meta_data_plan_model['allow_internal_users'] = True 
        object_meta_data_plan_model['async_provisioning_supported'] = True 
        object_meta_data_plan_model['async_unprovisioning_supported'] = True 
        object_meta_data_plan_model['test_check_interval'] = 38 
        object_meta_data_plan_model['single_scope_instance'] = 'testString' 
        object_meta_data_plan_model['service_check_enabled'] = True 
        object_meta_data_plan_model['cf_guid'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString' 
        object_meta_data_service_model['iam_compatible'] = True 
        object_meta_data_service_model['unique_api_key'] = True 
        object_meta_data_service_model['provisionable'] = True 
        object_meta_data_service_model['async_provisioning_supported'] = True 
        object_meta_data_service_model['async_unprovisioning_supported'] = True 
        object_meta_data_service_model['cf_guid'] = 'testString' 
        object_meta_data_service_model['bindable'] = True 
        object_meta_data_service_model['requires'] = ['testString'] 
        object_meta_data_service_model['plan_updateable'] = True 
        object_meta_data_service_model['state'] = 'testString' 
        object_meta_data_service_model['service_check_enabled'] = True 
        object_meta_data_service_model['test_check_interval'] = 38 
        object_meta_data_service_model['service_key_supported'] = True 

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString' 
        object_meta_data_sla_model['tenancy'] = 'testString' 
        object_meta_data_sla_model['provisioning'] = 'testString' 
        object_meta_data_sla_model['responsiveness'] = 'testString' 
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model 

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString'] 
        object_meta_data_template_model['default_memory'] = 38 
        object_meta_data_template_model['start_cmd'] = 'testString' 
        object_meta_data_template_model['source'] = object_meta_data_template_source_model 
        object_meta_data_template_model['runtime_catalog_id'] = 'testString' 
        object_meta_data_template_model['cf_runtime_id'] = 'testString' 
        object_meta_data_template_model['template_id'] = 'testString' 
        object_meta_data_template_model['executable_file'] = 'testString' 
        object_meta_data_template_model['buildpack'] = 'testString' 
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model 

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString' 
        pricing_model['origin'] = 'testString' 
        pricing_model['starting_price'] = starting_price_model 
        pricing_model['metrics'] = [metrics_model] 

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model 
        ui_meta_data_model['urls'] = urls_model 
        ui_meta_data_model['embeddable_dashboard'] = 'testString' 
        ui_meta_data_model['embeddable_dashboard_full_width'] = True 
        ui_meta_data_model['navigation_order'] = ['testString'] 
        ui_meta_data_model['not_creatable'] = True 
        ui_meta_data_model['reservable'] = True 
        ui_meta_data_model['primary_offering_id'] = 'testString' 
        ui_meta_data_model['accessible_during_provision'] = True 
        ui_meta_data_model['side_by_side_index'] = 38 
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z' 

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True 
        object_meta_data_model['ui'] = ui_meta_data_model 
        object_meta_data_model['pricing'] = pricing_model 
        object_meta_data_model['compliance'] = ['testString'] 
        object_meta_data_model['service'] = object_meta_data_service_model 
        object_meta_data_model['plan'] = object_meta_data_plan_model 
        object_meta_data_model['template'] = object_meta_data_template_model 
        object_meta_data_model['deployment'] = object_meta_data_deployment_model 
        object_meta_data_model['alias'] = object_meta_data_alias_model 
        object_meta_data_model['sla'] = object_meta_data_sla_model 
        object_meta_data_model['callbacks'] = callbacks_model 
        object_meta_data_model['version'] = 'testString' 
        object_meta_data_model['origin_name'] = 'testString' 
        object_meta_data_model['other'] = { 'foo': 'bar' } 

        # Construct a dict representation of a CatalogEntry model
        catalog_entry_model = {}
        catalog_entry_model['id'] = 'testString' 
        catalog_entry_model['catalog_crn'] = 'testString' 
        catalog_entry_model['url'] = 'testString' 
        catalog_entry_model['name'] = 'testString' 
        catalog_entry_model['overview_ui'] = overview_ui_model 
        catalog_entry_model['kind'] = 'testString' 
        catalog_entry_model['images'] = image_model 
        catalog_entry_model['parent_id'] = 'testString' 
        catalog_entry_model['children_url'] = 'testString' 
        catalog_entry_model['parent_url'] = 'testString' 
        catalog_entry_model['disabled'] = True 
        catalog_entry_model['tags'] = ['testString'] 
        catalog_entry_model['geo_tags'] = ['testString'] 
        catalog_entry_model['pricing_tags'] = ['testString'] 
        catalog_entry_model['group'] = True 
        catalog_entry_model['provider'] = provider_model 
        catalog_entry_model['created'] = '2020-01-28T18:40:40.123456Z' 
        catalog_entry_model['updated'] = '2020-01-28T18:40:40.123456Z' 
        catalog_entry_model['metadata'] = object_meta_data_model 
        catalog_entry_model['active'] = True 

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        overview_ui = overview_ui_model
        kind = 'testString'
        images = image_model
        disabled = True
        tags = ['testString']
        geo_tags = ['testString']
        pricing_tags = ['testString']
        group = True
        provider = provider_model
        catalog_crn = 'testString'
        url = 'testString'
        parent_id = 'testString'
        children_url = 'testString'
        parent_url = 'testString'
        created = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        updated = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        metadata = object_meta_data_model
        active = True
        children = [catalog_entry_model]

        # Invoke method
        response = service.create_catalog_entry(
            id,
            name,
            overview_ui,
            kind,
            images,
            disabled,
            tags,
            geo_tags,
            pricing_tags,
            group,
            provider,
            catalog_crn=catalog_crn,
            url=url,
            parent_id=parent_id,
            children_url=children_url,
            parent_url=parent_url,
            created=created,
            updated=updated,
            metadata=metadata,
            active=active,
            children=children,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == id
        assert req_body['name'] == name
        assert req_body['overview_ui'] == overview_ui
        assert req_body['kind'] == kind
        assert req_body['images'] == images
        assert req_body['disabled'] == disabled
        assert req_body['tags'] == tags
        assert req_body['geo_tags'] == geo_tags
        assert req_body['pricing_tags'] == pricing_tags
        assert req_body['group'] == group
        assert req_body['provider'] == provider
        assert req_body['catalog_crn'] == catalog_crn
        assert req_body['url'] == url
        assert req_body['parent_id'] == parent_id
        assert req_body['children_url'] == children_url
        assert req_body['parent_url'] == parent_url
        assert req_body['created'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['updated'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['metadata'] == metadata
        assert req_body['active'] == active
        assert req_body['children'] == children


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
        mock_response = '{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url", "source": {"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url", "source": {"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url", "source": {"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url", "source": {"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url"}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [], "media": [], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": []}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": []}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": []}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": []}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "metrics": []}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack"}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness"}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "compliance": ["compliance"], "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "kind": "kind", "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "active": true, "children": []}]}]}]}]}]}]}]}]}]}'
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
            depth=depth
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
        mock_response = '{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url", "source": {"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url", "source": {"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url", "source": {"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url", "source": {"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [{"title": "title", "description": "description", "icon": "icon", "quantity": "quantity"}], "media": [{"caption": "caption", "thumbnail_url": "thumbnail_url", "type": "type", "URL": "url"}], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {"_language_": {"bullets": [], "media": [], "not_creatable_msg": "not_creatable_msg", "not_creatable__robot_msg": "not_creatable_robot_msg", "deprecation_warning": "deprecation_warning", "popup_warning_message": "popup_warning_message", "instruction": "instruction"}}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": []}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": []}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": []}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": []}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {"_language_": {"display_name": "display_name", "long_description": "long_description", "description": "description"}}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "metrics": []}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack"}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness"}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "compliance": ["compliance"], "version": "version", "origin_name": "origin_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "kind": "kind", "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "active": true, "children": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_catalog_entry(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString' 
        overview_model['long_description'] = 'testString' 
        overview_model['description'] = 'testString' 

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['language'] = overview_model 

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
        bullets_model['quantity'] = 'testString' 

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38 
        price_model['price'] = 36.0 

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString' 
        ui_meta_media_model['thumbnail_url'] = 'testString' 
        ui_meta_media_model['type'] = 'testString' 
        ui_meta_media_model['url'] = 'testString' 
        ui_meta_media_model['source'] = bullets_model 

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString' 
        amount_model['currency'] = 'testString' 
        amount_model['prices'] = [price_model] 

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString' 
        object_meta_data_deployment_broker_password_model['key'] = 'testString' 
        object_meta_data_deployment_broker_password_model['iv'] = 'testString' 

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model] 
        strings_model['media'] = [ui_meta_media_model] 
        strings_model['not_creatable_msg'] = 'testString' 
        strings_model['not_creatable_robot_msg'] = 'testString' 
        strings_model['deprecation_warning'] = 'testString' 
        strings_model['popup_warning_message'] = 'testString' 
        strings_model['instruction'] = 'testString' 

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['language'] = strings_model 

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString' 
        metrics_model['tier_model'] = 'testString' 
        metrics_model['charge_unit_name'] = 'testString' 
        metrics_model['charge_unit_quantity'] = 'testString' 
        metrics_model['resource_display_name'] = 'testString' 
        metrics_model['charge_unit_display_name'] = 'testString' 
        metrics_model['usage_cap_qty'] = 38 
        metrics_model['amounts'] = [amount_model] 

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString' 
        object_meta_data_deployment_broker_model['guid'] = 'testString' 
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model 

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True 
        object_meta_data_sla_dr_model['description'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['key'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString' 
        object_meta_data_template_source_model['type'] = 'testString' 
        object_meta_data_template_source_model['url'] = 'testString' 

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString' 
        starting_price_model['deployment_id'] = 'testString' 
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

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString' 
        callbacks_model['broker_proxy_url'] = 'testString' 
        callbacks_model['dashboard_url'] = 'testString' 
        callbacks_model['dashboard_data_url'] = 'testString' 
        callbacks_model['dashboard_detail_tab_url'] = 'testString' 
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString' 
        callbacks_model['service_monitor_api'] = 'testString' 
        callbacks_model['service_monitor_app'] = 'testString' 
        callbacks_model['service_staging_url'] = 'testString' 
        callbacks_model['service_production_url'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString' 
        object_meta_data_alias_model['plan_id'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString' 
        object_meta_data_deployment_model['location_url'] = 'testString' 
        object_meta_data_deployment_model['target_crn'] = 'testString' 
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model 
        object_meta_data_deployment_model['supports_rc_migration'] = True 

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True 
        object_meta_data_plan_model['reservable'] = True 
        object_meta_data_plan_model['allow_internal_users'] = True 
        object_meta_data_plan_model['async_provisioning_supported'] = True 
        object_meta_data_plan_model['async_unprovisioning_supported'] = True 
        object_meta_data_plan_model['test_check_interval'] = 38 
        object_meta_data_plan_model['single_scope_instance'] = 'testString' 
        object_meta_data_plan_model['service_check_enabled'] = True 
        object_meta_data_plan_model['cf_guid'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString' 
        object_meta_data_service_model['iam_compatible'] = True 
        object_meta_data_service_model['unique_api_key'] = True 
        object_meta_data_service_model['provisionable'] = True 
        object_meta_data_service_model['async_provisioning_supported'] = True 
        object_meta_data_service_model['async_unprovisioning_supported'] = True 
        object_meta_data_service_model['cf_guid'] = 'testString' 
        object_meta_data_service_model['bindable'] = True 
        object_meta_data_service_model['requires'] = ['testString'] 
        object_meta_data_service_model['plan_updateable'] = True 
        object_meta_data_service_model['state'] = 'testString' 
        object_meta_data_service_model['service_check_enabled'] = True 
        object_meta_data_service_model['test_check_interval'] = 38 
        object_meta_data_service_model['service_key_supported'] = True 

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString' 
        object_meta_data_sla_model['tenancy'] = 'testString' 
        object_meta_data_sla_model['provisioning'] = 'testString' 
        object_meta_data_sla_model['responsiveness'] = 'testString' 
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model 

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString'] 
        object_meta_data_template_model['default_memory'] = 38 
        object_meta_data_template_model['start_cmd'] = 'testString' 
        object_meta_data_template_model['source'] = object_meta_data_template_source_model 
        object_meta_data_template_model['runtime_catalog_id'] = 'testString' 
        object_meta_data_template_model['cf_runtime_id'] = 'testString' 
        object_meta_data_template_model['template_id'] = 'testString' 
        object_meta_data_template_model['executable_file'] = 'testString' 
        object_meta_data_template_model['buildpack'] = 'testString' 
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model 

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString' 
        pricing_model['origin'] = 'testString' 
        pricing_model['starting_price'] = starting_price_model 
        pricing_model['metrics'] = [metrics_model] 

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model 
        ui_meta_data_model['urls'] = urls_model 
        ui_meta_data_model['embeddable_dashboard'] = 'testString' 
        ui_meta_data_model['embeddable_dashboard_full_width'] = True 
        ui_meta_data_model['navigation_order'] = ['testString'] 
        ui_meta_data_model['not_creatable'] = True 
        ui_meta_data_model['reservable'] = True 
        ui_meta_data_model['primary_offering_id'] = 'testString' 
        ui_meta_data_model['accessible_during_provision'] = True 
        ui_meta_data_model['side_by_side_index'] = 38 
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z' 

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True 
        object_meta_data_model['ui'] = ui_meta_data_model 
        object_meta_data_model['pricing'] = pricing_model 
        object_meta_data_model['compliance'] = ['testString'] 
        object_meta_data_model['service'] = object_meta_data_service_model 
        object_meta_data_model['plan'] = object_meta_data_plan_model 
        object_meta_data_model['template'] = object_meta_data_template_model 
        object_meta_data_model['deployment'] = object_meta_data_deployment_model 
        object_meta_data_model['alias'] = object_meta_data_alias_model 
        object_meta_data_model['sla'] = object_meta_data_sla_model 
        object_meta_data_model['callbacks'] = callbacks_model 
        object_meta_data_model['version'] = 'testString' 
        object_meta_data_model['origin_name'] = 'testString' 
        object_meta_data_model['other'] = { 'foo': 'bar' } 

        # Construct a dict representation of a CatalogEntry model
        catalog_entry_model = {}
        catalog_entry_model['id'] = 'testString' 
        catalog_entry_model['catalog_crn'] = 'testString' 
        catalog_entry_model['url'] = 'testString' 
        catalog_entry_model['name'] = 'testString' 
        catalog_entry_model['overview_ui'] = overview_ui_model 
        catalog_entry_model['kind'] = 'testString' 
        catalog_entry_model['images'] = image_model 
        catalog_entry_model['parent_id'] = 'testString' 
        catalog_entry_model['children_url'] = 'testString' 
        catalog_entry_model['parent_url'] = 'testString' 
        catalog_entry_model['disabled'] = True 
        catalog_entry_model['tags'] = ['testString'] 
        catalog_entry_model['geo_tags'] = ['testString'] 
        catalog_entry_model['pricing_tags'] = ['testString'] 
        catalog_entry_model['group'] = True 
        catalog_entry_model['provider'] = provider_model 
        catalog_entry_model['created'] = '2020-01-28T18:40:40.123456Z' 
        catalog_entry_model['updated'] = '2020-01-28T18:40:40.123456Z' 
        catalog_entry_model['metadata'] = object_meta_data_model 
        catalog_entry_model['active'] = True 

        # Set up parameter values
        id = 'testString'
        new_id = 'testString'
        new_name = 'testString'
        new_overview_ui = overview_ui_model
        new_kind = 'testString'
        new_images = image_model
        new_disabled = True
        new_tags = ['testString']
        new_geo_tags = ['testString']
        new_pricing_tags = ['testString']
        new_group = True
        new_provider = provider_model
        new_catalog_crn = 'testString'
        new_url = 'testString'
        new_parent_id = 'testString'
        new_children_url = 'testString'
        new_parent_url = 'testString'
        new_created = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        new_updated = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        new_metadata = object_meta_data_model
        new_active = True
        new_children = [catalog_entry_model]
        account = 'testString'
        move = 'testString'

        # Invoke method
        response = service.update_catalog_entry(
            id,
            new_id,
            new_name,
            new_overview_ui,
            new_kind,
            new_images,
            new_disabled,
            new_tags,
            new_geo_tags,
            new_pricing_tags,
            new_group,
            new_provider,
            new_catalog_crn=new_catalog_crn,
            new_url=new_url,
            new_parent_id=new_parent_id,
            new_children_url=new_children_url,
            new_parent_url=new_parent_url,
            new_created=new_created,
            new_updated=new_updated,
            new_metadata=new_metadata,
            new_active=new_active,
            new_children=new_children,
            account=account,
            move=move
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
        assert req_body['id'] == new_id
        assert req_body['name'] == new_name
        assert req_body['overview_ui'] == new_overview_ui
        assert req_body['kind'] == new_kind
        assert req_body['images'] == new_images
        assert req_body['disabled'] == new_disabled
        assert req_body['tags'] == new_tags
        assert req_body['geo_tags'] == new_geo_tags
        assert req_body['pricing_tags'] == new_pricing_tags
        assert req_body['group'] == new_group
        assert req_body['provider'] == new_provider
        assert req_body['catalog_crn'] == new_catalog_crn
        assert req_body['url'] == new_url
        assert req_body['parent_id'] == new_parent_id
        assert req_body['children_url'] == new_children_url
        assert req_body['parent_url'] == new_parent_url
        assert req_body['created'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['updated'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['metadata'] == new_metadata
        assert req_body['active'] == new_active
        assert req_body['children'] == new_children


    #--------------------------------------------------------
    # test_update_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString' 
        overview_model['long_description'] = 'testString' 
        overview_model['description'] = 'testString' 

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['language'] = overview_model 

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
        bullets_model['quantity'] = 'testString' 

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38 
        price_model['price'] = 36.0 

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString' 
        ui_meta_media_model['thumbnail_url'] = 'testString' 
        ui_meta_media_model['type'] = 'testString' 
        ui_meta_media_model['url'] = 'testString' 
        ui_meta_media_model['source'] = bullets_model 

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString' 
        amount_model['currency'] = 'testString' 
        amount_model['prices'] = [price_model] 

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString' 
        object_meta_data_deployment_broker_password_model['key'] = 'testString' 
        object_meta_data_deployment_broker_password_model['iv'] = 'testString' 

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model] 
        strings_model['media'] = [ui_meta_media_model] 
        strings_model['not_creatable_msg'] = 'testString' 
        strings_model['not_creatable_robot_msg'] = 'testString' 
        strings_model['deprecation_warning'] = 'testString' 
        strings_model['popup_warning_message'] = 'testString' 
        strings_model['instruction'] = 'testString' 

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['language'] = strings_model 

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString' 
        metrics_model['tier_model'] = 'testString' 
        metrics_model['charge_unit_name'] = 'testString' 
        metrics_model['charge_unit_quantity'] = 'testString' 
        metrics_model['resource_display_name'] = 'testString' 
        metrics_model['charge_unit_display_name'] = 'testString' 
        metrics_model['usage_cap_qty'] = 38 
        metrics_model['amounts'] = [amount_model] 

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString' 
        object_meta_data_deployment_broker_model['guid'] = 'testString' 
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model 

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True 
        object_meta_data_sla_dr_model['description'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['key'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString' 
        object_meta_data_template_source_model['type'] = 'testString' 
        object_meta_data_template_source_model['url'] = 'testString' 

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString' 
        starting_price_model['deployment_id'] = 'testString' 
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

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString' 
        callbacks_model['broker_proxy_url'] = 'testString' 
        callbacks_model['dashboard_url'] = 'testString' 
        callbacks_model['dashboard_data_url'] = 'testString' 
        callbacks_model['dashboard_detail_tab_url'] = 'testString' 
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString' 
        callbacks_model['service_monitor_api'] = 'testString' 
        callbacks_model['service_monitor_app'] = 'testString' 
        callbacks_model['service_staging_url'] = 'testString' 
        callbacks_model['service_production_url'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString' 
        object_meta_data_alias_model['plan_id'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString' 
        object_meta_data_deployment_model['location_url'] = 'testString' 
        object_meta_data_deployment_model['target_crn'] = 'testString' 
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model 
        object_meta_data_deployment_model['supports_rc_migration'] = True 

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True 
        object_meta_data_plan_model['reservable'] = True 
        object_meta_data_plan_model['allow_internal_users'] = True 
        object_meta_data_plan_model['async_provisioning_supported'] = True 
        object_meta_data_plan_model['async_unprovisioning_supported'] = True 
        object_meta_data_plan_model['test_check_interval'] = 38 
        object_meta_data_plan_model['single_scope_instance'] = 'testString' 
        object_meta_data_plan_model['service_check_enabled'] = True 
        object_meta_data_plan_model['cf_guid'] = 'testString' 

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString' 
        object_meta_data_service_model['iam_compatible'] = True 
        object_meta_data_service_model['unique_api_key'] = True 
        object_meta_data_service_model['provisionable'] = True 
        object_meta_data_service_model['async_provisioning_supported'] = True 
        object_meta_data_service_model['async_unprovisioning_supported'] = True 
        object_meta_data_service_model['cf_guid'] = 'testString' 
        object_meta_data_service_model['bindable'] = True 
        object_meta_data_service_model['requires'] = ['testString'] 
        object_meta_data_service_model['plan_updateable'] = True 
        object_meta_data_service_model['state'] = 'testString' 
        object_meta_data_service_model['service_check_enabled'] = True 
        object_meta_data_service_model['test_check_interval'] = 38 
        object_meta_data_service_model['service_key_supported'] = True 

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString' 
        object_meta_data_sla_model['tenancy'] = 'testString' 
        object_meta_data_sla_model['provisioning'] = 'testString' 
        object_meta_data_sla_model['responsiveness'] = 'testString' 
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model 

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString'] 
        object_meta_data_template_model['default_memory'] = 38 
        object_meta_data_template_model['start_cmd'] = 'testString' 
        object_meta_data_template_model['source'] = object_meta_data_template_source_model 
        object_meta_data_template_model['runtime_catalog_id'] = 'testString' 
        object_meta_data_template_model['cf_runtime_id'] = 'testString' 
        object_meta_data_template_model['template_id'] = 'testString' 
        object_meta_data_template_model['executable_file'] = 'testString' 
        object_meta_data_template_model['buildpack'] = 'testString' 
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model 

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString' 
        pricing_model['origin'] = 'testString' 
        pricing_model['starting_price'] = starting_price_model 
        pricing_model['metrics'] = [metrics_model] 

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model 
        ui_meta_data_model['urls'] = urls_model 
        ui_meta_data_model['embeddable_dashboard'] = 'testString' 
        ui_meta_data_model['embeddable_dashboard_full_width'] = True 
        ui_meta_data_model['navigation_order'] = ['testString'] 
        ui_meta_data_model['not_creatable'] = True 
        ui_meta_data_model['reservable'] = True 
        ui_meta_data_model['primary_offering_id'] = 'testString' 
        ui_meta_data_model['accessible_during_provision'] = True 
        ui_meta_data_model['side_by_side_index'] = 38 
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z' 

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True 
        object_meta_data_model['ui'] = ui_meta_data_model 
        object_meta_data_model['pricing'] = pricing_model 
        object_meta_data_model['compliance'] = ['testString'] 
        object_meta_data_model['service'] = object_meta_data_service_model 
        object_meta_data_model['plan'] = object_meta_data_plan_model 
        object_meta_data_model['template'] = object_meta_data_template_model 
        object_meta_data_model['deployment'] = object_meta_data_deployment_model 
        object_meta_data_model['alias'] = object_meta_data_alias_model 
        object_meta_data_model['sla'] = object_meta_data_sla_model 
        object_meta_data_model['callbacks'] = callbacks_model 
        object_meta_data_model['version'] = 'testString' 
        object_meta_data_model['origin_name'] = 'testString' 
        object_meta_data_model['other'] = { 'foo': 'bar' } 

        # Construct a dict representation of a CatalogEntry model
        catalog_entry_model = {}
        catalog_entry_model['id'] = 'testString' 
        catalog_entry_model['catalog_crn'] = 'testString' 
        catalog_entry_model['url'] = 'testString' 
        catalog_entry_model['name'] = 'testString' 
        catalog_entry_model['overview_ui'] = overview_ui_model 
        catalog_entry_model['kind'] = 'testString' 
        catalog_entry_model['images'] = image_model 
        catalog_entry_model['parent_id'] = 'testString' 
        catalog_entry_model['children_url'] = 'testString' 
        catalog_entry_model['parent_url'] = 'testString' 
        catalog_entry_model['disabled'] = True 
        catalog_entry_model['tags'] = ['testString'] 
        catalog_entry_model['geo_tags'] = ['testString'] 
        catalog_entry_model['pricing_tags'] = ['testString'] 
        catalog_entry_model['group'] = True 
        catalog_entry_model['provider'] = provider_model 
        catalog_entry_model['created'] = '2020-01-28T18:40:40.123456Z' 
        catalog_entry_model['updated'] = '2020-01-28T18:40:40.123456Z' 
        catalog_entry_model['metadata'] = object_meta_data_model 
        catalog_entry_model['active'] = True 

        # Set up parameter values
        id = 'testString'
        new_id = 'testString'
        new_name = 'testString'
        new_overview_ui = overview_ui_model
        new_kind = 'testString'
        new_images = image_model
        new_disabled = True
        new_tags = ['testString']
        new_geo_tags = ['testString']
        new_pricing_tags = ['testString']
        new_group = True
        new_provider = provider_model
        new_catalog_crn = 'testString'
        new_url = 'testString'
        new_parent_id = 'testString'
        new_children_url = 'testString'
        new_parent_url = 'testString'
        new_created = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        new_updated = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        new_metadata = object_meta_data_model
        new_active = True
        new_children = [catalog_entry_model]

        # Invoke method
        response = service.update_catalog_entry(
            id,
            new_id,
            new_name,
            new_overview_ui,
            new_kind,
            new_images,
            new_disabled,
            new_tags,
            new_geo_tags,
            new_pricing_tags,
            new_group,
            new_provider,
            new_catalog_crn=new_catalog_crn,
            new_url=new_url,
            new_parent_id=new_parent_id,
            new_children_url=new_children_url,
            new_parent_url=new_parent_url,
            new_created=new_created,
            new_updated=new_updated,
            new_metadata=new_metadata,
            new_active=new_active,
            new_children=new_children,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == new_id
        assert req_body['name'] == new_name
        assert req_body['overview_ui'] == new_overview_ui
        assert req_body['kind'] == new_kind
        assert req_body['images'] == new_images
        assert req_body['disabled'] == new_disabled
        assert req_body['tags'] == new_tags
        assert req_body['geo_tags'] == new_geo_tags
        assert req_body['pricing_tags'] == new_pricing_tags
        assert req_body['group'] == new_group
        assert req_body['provider'] == new_provider
        assert req_body['catalog_crn'] == new_catalog_crn
        assert req_body['url'] == new_url
        assert req_body['parent_id'] == new_parent_id
        assert req_body['children_url'] == new_children_url
        assert req_body['parent_url'] == new_parent_url
        assert req_body['created'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['updated'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['metadata'] == new_metadata
        assert req_body['active'] == new_active
        assert req_body['children'] == new_children


#-----------------------------------------------------------------------------
# Test Class for archive_catalog_entry
#-----------------------------------------------------------------------------
class TestArchiveCatalogEntry():

    #--------------------------------------------------------
    # archive_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_archive_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.archive_catalog_entry(
            id,
            account=account
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_archive_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_archive_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.archive_catalog_entry(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


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
        mock_response = '[{}]'
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
            complete=complete
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
        mock_response = '[{}]'
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
            kind
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
            account=account
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
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


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
        mock_response = '{"restrictions": "restrictions", "owner": {"type": "type", "value": "value"}, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}'
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
            account=account
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
        mock_response = '{"restrictions": "restrictions", "owner": {"type": "type", "value": "value"}, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_visibility(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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

        # Construct a dict representation of a Scope model
        scope_model = {}
        scope_model['type'] = 'testString' 
        scope_model['value'] = 'testString' 

        # Construct a dict representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model = {}
        visibility_detail_accounts_model['accountid'] = 'testString' 

        # Construct a dict representation of a VisibilityDetail model
        visibility_detail_model = {}
        visibility_detail_model['accounts'] = visibility_detail_accounts_model 

        # Set up parameter values
        id = 'testString'
        restrictions = 'testString'
        owner = scope_model
        include = visibility_detail_model
        exclude = visibility_detail_model
        approved = True
        account = 'testString'

        # Invoke method
        response = service.update_visibility(
            id,
            restrictions=restrictions,
            owner=owner,
            include=include,
            exclude=exclude,
            approved=approved,
            account=account
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
        assert req_body['restrictions'] == restrictions
        assert req_body['owner'] == owner
        assert req_body['include'] == include
        assert req_body['exclude'] == exclude
        assert req_body['approved'] == approved


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

        # Construct a dict representation of a Scope model
        scope_model = {}
        scope_model['type'] = 'testString' 
        scope_model['value'] = 'testString' 

        # Construct a dict representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model = {}
        visibility_detail_accounts_model['accountid'] = 'testString' 

        # Construct a dict representation of a VisibilityDetail model
        visibility_detail_model = {}
        visibility_detail_model['accounts'] = visibility_detail_accounts_model 

        # Set up parameter values
        id = 'testString'
        restrictions = 'testString'
        owner = scope_model
        include = visibility_detail_model
        exclude = visibility_detail_model
        approved = True

        # Invoke method
        response = service.update_visibility(
            id,
            restrictions=restrictions,
            owner=owner,
            include=include,
            exclude=exclude,
            approved=approved,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['restrictions'] == restrictions
        assert req_body['owner'] == owner
        assert req_body['include'] == include
        assert req_body['exclude'] == exclude
        assert req_body['approved'] == approved


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
        mock_response = '{"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}'
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
            account=account
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
        mock_response = '{"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_pricing(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
        mock_response = '{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}'
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
            limit=limit
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
        mock_response = '{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_audit_logs(
            id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
        mock_response = '{"count": 5, "resources": [{"name": "name", "updated": "updated", "url": "url", "etag": "etag", "size": 4}]}'
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
            account=account
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
        mock_response = '{"count": 5, "resources": [{"name": "name", "updated": "updated", "url": "url", "etag": "etag", "size": 4}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        object_id = 'testString'

        # Invoke method
        response = service.list_artifacts(
            object_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.get_artifact(
            object_id,
            artifact_id,
            account=account
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
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Invoke method
        response = service.get_artifact(
            object_id,
            artifact_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
        account = 'testString'

        # Invoke method
        response = service.upload_artifact(
            object_id,
            artifact_id,
            account=account
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


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
            artifact_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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
            account=account
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
            artifact_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Artifact
##############################################################################

