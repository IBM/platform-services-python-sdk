# -*- coding: utf-8 -*-
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

"""
Examples for CatalogManagementV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import os
import pytest
from ibm_platform_services.catalog_management_v1 import *

#
# This file provides an example of how to use the Catalog Management service.
#
# The following configuration properties are assumed to be defined:
# CATALOG_MANAGEMENT_URL=<service base url>
# CATALOG_MANAGEMENT_AUTH_TYPE=iam
# CATALOG_MANAGEMENT_APIKEY=<IAM apikey>
# CATALOG_MANAGEMENT_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'catalog_management_v1.env'

catalog_management_service = None

config = None


##############################################################################
# Start of Examples for Service: CatalogManagementV1
##############################################################################
# region
class TestCatalogManagementV1Examples():
    """
    Example Test Class for CatalogManagementV1
    """

    @classmethod
    def setup_class(cls):
        global catalog_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            catalog_management_service = CatalogManagementV1.new_instance(
            )

            # end-common
            assert catalog_management_service is not None

            # Load the configuration
            global config
            config = read_external_sources(CatalogManagementV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_catalog_example(self):
        """
        create_catalog request example
        """
        try:
            print('\ncreate_catalog() result:')
            # begin-create_catalog

            catalog = catalog_management_service.create_catalog().get_result()

            print(json.dumps(catalog, indent=2))

            # end-create_catalog

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_catalog_example(self):
        """
        get_catalog request example
        """
        try:
            print('\nget_catalog() result:')
            # begin-get_catalog

            catalog = catalog_management_service.get_catalog(
                catalog_identifier='testString'
            ).get_result()

            print(json.dumps(catalog, indent=2))

            # end-get_catalog

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_catalog_example(self):
        """
        replace_catalog request example
        """
        try:
            print('\nreplace_catalog() result:')
            # begin-replace_catalog

            catalog = catalog_management_service.replace_catalog(
                catalog_identifier='testString'
            ).get_result()

            print(json.dumps(catalog, indent=2))

            # end-replace_catalog

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_catalogs_example(self):
        """
        list_catalogs request example
        """
        try:
            print('\nlist_catalogs() result:')
            # begin-list_catalogs

            catalog_search_result = catalog_management_service.list_catalogs().get_result()

            print(json.dumps(catalog_search_result, indent=2))

            # end-list_catalogs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_offering_example(self):
        """
        create_offering request example
        """
        try:
            print('\ncreate_offering() result:')
            # begin-create_offering

            offering = catalog_management_service.create_offering(
                catalog_identifier='testString'
            ).get_result()

            print(json.dumps(offering, indent=2))

            # end-create_offering

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_offering_example(self):
        """
        get_offering request example
        """
        try:
            print('\nget_offering() result:')
            # begin-get_offering

            offering = catalog_management_service.get_offering(
                catalog_identifier='testString',
                offering_id='testString'
            ).get_result()

            print(json.dumps(offering, indent=2))

            # end-get_offering

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_offering_example(self):
        """
        replace_offering request example
        """
        try:
            print('\nreplace_offering() result:')
            # begin-replace_offering

            offering = catalog_management_service.replace_offering(
                catalog_identifier='testString',
                offering_id='testString'
            ).get_result()

            print(json.dumps(offering, indent=2))

            # end-replace_offering

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_offerings_example(self):
        """
        list_offerings request example
        """
        try:
            print('\nlist_offerings() result:')
            # begin-list_offerings

            offering_search_result = catalog_management_service.list_offerings(
                catalog_identifier='testString'
            ).get_result()

            print(json.dumps(offering_search_result, indent=2))

            # end-list_offerings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_import_offering_example(self):
        """
        import_offering request example
        """
        try:
            print('\nimport_offering() result:')
            # begin-import_offering

            offering = catalog_management_service.import_offering(
                catalog_identifier='testString'
            ).get_result()

            print(json.dumps(offering, indent=2))

            # end-import_offering

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_reload_offering_example(self):
        """
        reload_offering request example
        """
        try:
            print('\nreload_offering() result:')
            # begin-reload_offering

            offering = catalog_management_service.reload_offering(
                catalog_identifier='testString',
                offering_id='testString',
                target_version='testString'
            ).get_result()

            print(json.dumps(offering, indent=2))

            # end-reload_offering

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_object_example(self):
        """
        create_object request example
        """
        try:
            print('\ncreate_object() result:')
            # begin-create_object

            catalog_object = catalog_management_service.create_object(
                catalog_identifier='testString'
            ).get_result()

            print(json.dumps(catalog_object, indent=2))

            # end-create_object

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_offering_audit_example(self):
        """
        get_offering_audit request example
        """
        try:
            print('\nget_offering_audit() result:')
            # begin-get_offering_audit

            audit_log = catalog_management_service.get_offering_audit(
                catalog_identifier='testString',
                offering_id='testString'
            ).get_result()

            print(json.dumps(audit_log, indent=2))

            # end-get_offering_audit

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_catalog_account_example(self):
        """
        get_catalog_account request example
        """
        try:
            print('\nget_catalog_account() result:')
            # begin-get_catalog_account

            account = catalog_management_service.get_catalog_account().get_result()

            print(json.dumps(account, indent=2))

            # end-get_catalog_account

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_catalog_account_example(self):
        """
        update_catalog_account request example
        """
        try:
            # begin-update_catalog_account

            response = catalog_management_service.update_catalog_account()

            # end-update_catalog_account
            print('\nupdate_catalog_account() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_catalog_account_audit_example(self):
        """
        get_catalog_account_audit request example
        """
        try:
            print('\nget_catalog_account_audit() result:')
            # begin-get_catalog_account_audit

            audit_log = catalog_management_service.get_catalog_account_audit().get_result()

            print(json.dumps(audit_log, indent=2))

            # end-get_catalog_account_audit

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_catalog_account_filters_example(self):
        """
        get_catalog_account_filters request example
        """
        try:
            print('\nget_catalog_account_filters() result:')
            # begin-get_catalog_account_filters

            accumulated_filters = catalog_management_service.get_catalog_account_filters().get_result()

            print(json.dumps(accumulated_filters, indent=2))

            # end-get_catalog_account_filters

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_catalog_audit_example(self):
        """
        get_catalog_audit request example
        """
        try:
            print('\nget_catalog_audit() result:')
            # begin-get_catalog_audit

            audit_log = catalog_management_service.get_catalog_audit(
                catalog_identifier='testString'
            ).get_result()

            print(json.dumps(audit_log, indent=2))

            # end-get_catalog_audit

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_consumption_offerings_example(self):
        """
        get_consumption_offerings request example
        """
        try:
            print('\nget_consumption_offerings() result:')
            # begin-get_consumption_offerings

            offering_search_result = catalog_management_service.get_consumption_offerings().get_result()

            print(json.dumps(offering_search_result, indent=2))

            # end-get_consumption_offerings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_import_offering_version_example(self):
        """
        import_offering_version request example
        """
        try:
            print('\nimport_offering_version() result:')
            # begin-import_offering_version

            offering = catalog_management_service.import_offering_version(
                catalog_identifier='testString',
                offering_id='testString'
            ).get_result()

            print(json.dumps(offering, indent=2))

            # end-import_offering_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_offering_icon_example(self):
        """
        replace_offering_icon request example
        """
        try:
            print('\nreplace_offering_icon() result:')
            # begin-replace_offering_icon

            offering = catalog_management_service.replace_offering_icon(
                catalog_identifier='testString',
                offering_id='testString',
                file_name='testString'
            ).get_result()

            print(json.dumps(offering, indent=2))

            # end-replace_offering_icon

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_offering_ibm_example(self):
        """
        update_offering_ibm request example
        """
        try:
            print('\nupdate_offering_ibm() result:')
            # begin-update_offering_ibm

            approval_result = catalog_management_service.update_offering_ibm(
                catalog_identifier='testString',
                offering_id='testString',
                approval_type='allow_request',
                approved='true'
            ).get_result()

            print(json.dumps(approval_result, indent=2))

            # end-update_offering_ibm

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_offering_updates_example(self):
        """
        get_offering_updates request example
        """
        try:
            print('\nget_offering_updates() result:')
            # begin-get_offering_updates

            list_version_update_descriptor = catalog_management_service.get_offering_updates(
                catalog_identifier='testString',
                offering_id='testString',
                kind='testString'
            ).get_result()

            print(json.dumps(list_version_update_descriptor, indent=2))

            # end-get_offering_updates

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_offering_about_example(self):
        """
        get_offering_about request example
        """
        try:
            print('\nget_offering_about() result:')
            # begin-get_offering_about

            result = catalog_management_service.get_offering_about(
                version_loc_id='testString'
            ).get_result()

            print(json.dumps(result, indent=2))

            # end-get_offering_about

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_offering_license_example(self):
        """
        get_offering_license request example
        """
        try:
            print('\nget_offering_license() result:')
            # begin-get_offering_license

            result = catalog_management_service.get_offering_license(
                version_loc_id='testString',
                license_id='testString'
            ).get_result()

            print(json.dumps(result, indent=2))

            # end-get_offering_license

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_offering_container_images_example(self):
        """
        get_offering_container_images request example
        """
        try:
            print('\nget_offering_container_images() result:')
            # begin-get_offering_container_images

            image_manifest = catalog_management_service.get_offering_container_images(
                version_loc_id='testString'
            ).get_result()

            print(json.dumps(image_manifest, indent=2))

            # end-get_offering_container_images

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_deprecate_version_example(self):
        """
        deprecate_version request example
        """
        try:
            # begin-deprecate_version

            response = catalog_management_service.deprecate_version(
                version_loc_id='testString'
            )

            # end-deprecate_version
            print('\ndeprecate_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_account_publish_version_example(self):
        """
        account_publish_version request example
        """
        try:
            # begin-account_publish_version

            response = catalog_management_service.account_publish_version(
                version_loc_id='testString'
            )

            # end-account_publish_version
            print('\naccount_publish_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_ibm_publish_version_example(self):
        """
        ibm_publish_version request example
        """
        try:
            # begin-ibm_publish_version

            response = catalog_management_service.ibm_publish_version(
                version_loc_id='testString'
            )

            # end-ibm_publish_version
            print('\nibm_publish_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_public_publish_version_example(self):
        """
        public_publish_version request example
        """
        try:
            # begin-public_publish_version

            response = catalog_management_service.public_publish_version(
                version_loc_id='testString'
            )

            # end-public_publish_version
            print('\npublic_publish_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_commit_version_example(self):
        """
        commit_version request example
        """
        try:
            # begin-commit_version

            response = catalog_management_service.commit_version(
                version_loc_id='testString'
            )

            # end-commit_version
            print('\ncommit_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_copy_version_example(self):
        """
        copy_version request example
        """
        try:
            # begin-copy_version

            response = catalog_management_service.copy_version(
                version_loc_id='testString'
            )

            # end-copy_version
            print('\ncopy_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_offering_working_copy_example(self):
        """
        get_offering_working_copy request example
        """
        try:
            print('\nget_offering_working_copy() result:')
            # begin-get_offering_working_copy

            version = catalog_management_service.get_offering_working_copy(
                version_loc_id='testString'
            ).get_result()

            print(json.dumps(version, indent=2))

            # end-get_offering_working_copy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_version_example(self):
        """
        get_version request example
        """
        try:
            print('\nget_version() result:')
            # begin-get_version

            offering = catalog_management_service.get_version(
                version_loc_id='testString'
            ).get_result()

            print(json.dumps(offering, indent=2))

            # end-get_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_cluster_example(self):
        """
        get_cluster request example
        """
        try:
            print('\nget_cluster() result:')
            # begin-get_cluster

            cluster_info = catalog_management_service.get_cluster(
                cluster_id='testString',
                region='testString',
                x_auth_refresh_token='testString'
            ).get_result()

            print(json.dumps(cluster_info, indent=2))

            # end-get_cluster

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_namespaces_example(self):
        """
        get_namespaces request example
        """
        try:
            print('\nget_namespaces() result:')
            # begin-get_namespaces

            namespace_search_result = catalog_management_service.get_namespaces(
                cluster_id='testString',
                region='testString',
                x_auth_refresh_token='testString'
            ).get_result()

            print(json.dumps(namespace_search_result, indent=2))

            # end-get_namespaces

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_deploy_operators_example(self):
        """
        deploy_operators request example
        """
        try:
            print('\ndeploy_operators() result:')
            # begin-deploy_operators

            list_operator_deploy_result = catalog_management_service.deploy_operators(
                x_auth_refresh_token='testString'
            ).get_result()

            print(json.dumps(list_operator_deploy_result, indent=2))

            # end-deploy_operators

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_operators_example(self):
        """
        list_operators request example
        """
        try:
            print('\nlist_operators() result:')
            # begin-list_operators

            list_operator_deploy_result = catalog_management_service.list_operators(
                x_auth_refresh_token='testString',
                cluster_id='testString',
                region='testString',
                version_locator_id='testString'
            ).get_result()

            print(json.dumps(list_operator_deploy_result, indent=2))

            # end-list_operators

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_operators_example(self):
        """
        replace_operators request example
        """
        try:
            print('\nreplace_operators() result:')
            # begin-replace_operators

            list_operator_deploy_result = catalog_management_service.replace_operators(
                x_auth_refresh_token='testString'
            ).get_result()

            print(json.dumps(list_operator_deploy_result, indent=2))

            # end-replace_operators

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_install_version_example(self):
        """
        install_version request example
        """
        try:
            # begin-install_version

            response = catalog_management_service.install_version(
                version_loc_id='testString',
                x_auth_refresh_token='testString'
            )

            # end-install_version
            print('\ninstall_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_preinstall_version_example(self):
        """
        preinstall_version request example
        """
        try:
            # begin-preinstall_version

            response = catalog_management_service.preinstall_version(
                version_loc_id='testString',
                x_auth_refresh_token='testString'
            )

            # end-preinstall_version
            print('\npreinstall_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_preinstall_example(self):
        """
        get_preinstall request example
        """
        try:
            print('\nget_preinstall() result:')
            # begin-get_preinstall

            install_status = catalog_management_service.get_preinstall(
                version_loc_id='testString',
                x_auth_refresh_token='testString'
            ).get_result()

            print(json.dumps(install_status, indent=2))

            # end-get_preinstall

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_validate_install_example(self):
        """
        validate_install request example
        """
        try:
            # begin-validate_install

            response = catalog_management_service.validate_install(
                version_loc_id='testString',
                x_auth_refresh_token='testString'
            )

            # end-validate_install
            print('\nvalidate_install() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_validation_status_example(self):
        """
        get_validation_status request example
        """
        try:
            print('\nget_validation_status() result:')
            # begin-get_validation_status

            validation = catalog_management_service.get_validation_status(
                version_loc_id='testString',
                x_auth_refresh_token='testString'
            ).get_result()

            print(json.dumps(validation, indent=2))

            # end-get_validation_status

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_override_values_example(self):
        """
        get_override_values request example
        """
        try:
            print('\nget_override_values() result:')
            # begin-get_override_values

            get_override_values_response = catalog_management_service.get_override_values(
                version_loc_id='testString'
            ).get_result()

            print(json.dumps(get_override_values_response, indent=2))

            # end-get_override_values

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_search_objects_example(self):
        """
        search_objects request example
        """
        try:
            print('\nsearch_objects() result:')
            # begin-search_objects

            object_search_result = catalog_management_service.search_objects(
                query='testString'
            ).get_result()

            print(json.dumps(object_search_result, indent=2))

            # end-search_objects

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_objects_example(self):
        """
        list_objects request example
        """
        try:
            print('\nlist_objects() result:')
            # begin-list_objects

            object_list_result = catalog_management_service.list_objects(
                catalog_identifier='testString'
            ).get_result()

            print(json.dumps(object_list_result, indent=2))

            # end-list_objects

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_object_example(self):
        """
        replace_object request example
        """
        try:
            print('\nreplace_object() result:')
            # begin-replace_object

            catalog_object = catalog_management_service.replace_object(
                catalog_identifier='testString',
                object_identifier='testString'
            ).get_result()

            print(json.dumps(catalog_object, indent=2))

            # end-replace_object

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_object_example(self):
        """
        get_object request example
        """
        try:
            print('\nget_object() result:')
            # begin-get_object

            catalog_object = catalog_management_service.get_object(
                catalog_identifier='testString',
                object_identifier='testString'
            ).get_result()

            print(json.dumps(catalog_object, indent=2))

            # end-get_object

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_object_audit_example(self):
        """
        get_object_audit request example
        """
        try:
            print('\nget_object_audit() result:')
            # begin-get_object_audit

            audit_log = catalog_management_service.get_object_audit(
                catalog_identifier='testString',
                object_identifier='testString'
            ).get_result()

            print(json.dumps(audit_log, indent=2))

            # end-get_object_audit

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_account_publish_object_example(self):
        """
        account_publish_object request example
        """
        try:
            # begin-account_publish_object

            response = catalog_management_service.account_publish_object(
                catalog_identifier='testString',
                object_identifier='testString'
            )

            # end-account_publish_object
            print('\naccount_publish_object() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_shared_publish_object_example(self):
        """
        shared_publish_object request example
        """
        try:
            # begin-shared_publish_object

            response = catalog_management_service.shared_publish_object(
                catalog_identifier='testString',
                object_identifier='testString'
            )

            # end-shared_publish_object
            print('\nshared_publish_object() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_ibm_publish_object_example(self):
        """
        ibm_publish_object request example
        """
        try:
            # begin-ibm_publish_object

            response = catalog_management_service.ibm_publish_object(
                catalog_identifier='testString',
                object_identifier='testString'
            )

            # end-ibm_publish_object
            print('\nibm_publish_object() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_public_publish_object_example(self):
        """
        public_publish_object request example
        """
        try:
            # begin-public_publish_object

            response = catalog_management_service.public_publish_object(
                catalog_identifier='testString',
                object_identifier='testString'
            )

            # end-public_publish_object
            print('\npublic_publish_object() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_object_access_example(self):
        """
        create_object_access request example
        """
        try:
            # begin-create_object_access

            response = catalog_management_service.create_object_access(
                catalog_identifier='testString',
                object_identifier='testString',
                account_identifier='testString'
            )

            # end-create_object_access
            print('\ncreate_object_access() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_object_access_example(self):
        """
        get_object_access request example
        """
        try:
            print('\nget_object_access() result:')
            # begin-get_object_access

            object_access = catalog_management_service.get_object_access(
                catalog_identifier='testString',
                object_identifier='testString',
                account_identifier='testString'
            ).get_result()

            print(json.dumps(object_access, indent=2))

            # end-get_object_access

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_object_access_list_example(self):
        """
        get_object_access_list request example
        """
        try:
            print('\nget_object_access_list() result:')
            # begin-get_object_access_list

            object_access_list_result = catalog_management_service.get_object_access_list(
                catalog_identifier='testString',
                object_identifier='testString'
            ).get_result()

            print(json.dumps(object_access_list_result, indent=2))

            # end-get_object_access_list

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_object_access_list_example(self):
        """
        add_object_access_list request example
        """
        try:
            print('\nadd_object_access_list() result:')
            # begin-add_object_access_list

            access_list_bulk_response = catalog_management_service.add_object_access_list(
                catalog_identifier='testString',
                object_identifier='testString',
                accounts=['testString']
            ).get_result()

            print(json.dumps(access_list_bulk_response, indent=2))

            # end-add_object_access_list

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_offering_instance_example(self):
        """
        create_offering_instance request example
        """
        try:
            print('\ncreate_offering_instance() result:')
            # begin-create_offering_instance

            offering_instance = catalog_management_service.create_offering_instance(
                x_auth_refresh_token='testString'
            ).get_result()

            print(json.dumps(offering_instance, indent=2))

            # end-create_offering_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_offering_instance_example(self):
        """
        get_offering_instance request example
        """
        try:
            print('\nget_offering_instance() result:')
            # begin-get_offering_instance

            offering_instance = catalog_management_service.get_offering_instance(
                instance_identifier='testString'
            ).get_result()

            print(json.dumps(offering_instance, indent=2))

            # end-get_offering_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_put_offering_instance_example(self):
        """
        put_offering_instance request example
        """
        try:
            print('\nput_offering_instance() result:')
            # begin-put_offering_instance

            offering_instance = catalog_management_service.put_offering_instance(
                instance_identifier='testString',
                x_auth_refresh_token='testString'
            ).get_result()

            print(json.dumps(offering_instance, indent=2))

            # end-put_offering_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_version_example(self):
        """
        delete_version request example
        """
        try:
            # begin-delete_version

            response = catalog_management_service.delete_version(
                version_loc_id='testString'
            )

            # end-delete_version
            print('\ndelete_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_operators_example(self):
        """
        delete_operators request example
        """
        try:
            # begin-delete_operators

            response = catalog_management_service.delete_operators(
                x_auth_refresh_token='testString',
                cluster_id='testString',
                region='testString',
                version_locator_id='testString'
            )

            # end-delete_operators
            print('\ndelete_operators() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_offering_instance_example(self):
        """
        delete_offering_instance request example
        """
        try:
            # begin-delete_offering_instance

            response = catalog_management_service.delete_offering_instance(
                instance_identifier='testString',
                x_auth_refresh_token='testString'
            )

            # end-delete_offering_instance
            print('\ndelete_offering_instance() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_object_access_list_example(self):
        """
        delete_object_access_list request example
        """
        try:
            print('\ndelete_object_access_list() result:')
            # begin-delete_object_access_list

            access_list_bulk_response = catalog_management_service.delete_object_access_list(
                catalog_identifier='testString',
                object_identifier='testString',
                accounts=['testString']
            ).get_result()

            print(json.dumps(access_list_bulk_response, indent=2))

            # end-delete_object_access_list

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_object_access_example(self):
        """
        delete_object_access request example
        """
        try:
            # begin-delete_object_access

            response = catalog_management_service.delete_object_access(
                catalog_identifier='testString',
                object_identifier='testString',
                account_identifier='testString'
            )

            # end-delete_object_access
            print('\ndelete_object_access() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_object_example(self):
        """
        delete_object request example
        """
        try:
            # begin-delete_object

            response = catalog_management_service.delete_object(
                catalog_identifier='testString',
                object_identifier='testString'
            )

            # end-delete_object
            print('\ndelete_object() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_offering_example(self):
        """
        delete_offering request example
        """
        try:
            # begin-delete_offering

            response = catalog_management_service.delete_offering(
                catalog_identifier='testString',
                offering_id='testString'
            )

            # end-delete_offering
            print('\ndelete_offering() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_catalog_example(self):
        """
        delete_catalog request example
        """
        try:
            # begin-delete_catalog

            response = catalog_management_service.delete_catalog(
                catalog_identifier='testString'
            )

            # end-delete_catalog
            print('\ndelete_catalog() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: CatalogManagementV1
##############################################################################
