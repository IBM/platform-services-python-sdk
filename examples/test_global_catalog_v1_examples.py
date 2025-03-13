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
Examples for GlobalCatalogV1
"""

import os
import io
import uuid
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.global_catalog_v1 import *

#
# This file provides an example of how to use the Global Catalog service.
#
# The following configuration properties are assumed to be defined:
#
# GLOBAL_CATALOG_URL=<service url>
# GLOBAL_CATALOG_AUTH_TYPE=iam
# GLOBAL_CATALOG_APIKEY=<IAM apikey>
# GLOBAL_CATALOG_AUTH_URL=<IAM token service URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'global_catalog.env'

global_catalog_service = None

catalog_entry_id = None


##############################################################################
# Start of Examples for Service: GlobalCatalogV1
##############################################################################
# region
class TestGlobalCatalogV1Examples:
    """
    Example Test Class for GlobalCatalogV1
    """

    @classmethod
    def setup_class(cls):
        global global_catalog_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            global_catalog_service = GlobalCatalogV1.new_instance()

            # end-common
            assert global_catalog_service is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_catalog_entry_example(self):
        """
        create_catalog_entry request example
        """
        global catalog_entry_id

        try:
            print('\ncreate_catalog_entry() result:')
            # begin-create_catalog_entry

            overview_model_EN = {
                'display_name': 'Example Web Starter',
                'description': 'Use the Example service in your applications',
                'long_description': 'This is a starter that helps you use the Example service within your applications.',
            }
            image_model = {
                'image': 'https://somehost.com/examplewebstarter/cachedIcon/large/0',
                'small_image': 'https://somehost.com/examplewebstarter/cachedIcon/small/0',
                'medium_image': 'https://somehost.com/examplewebstarter/cachedIcon/medium/0',
                'feature_image': 'https://somehost.com/examplewebstarter/cachedIcon/large/0',
            }
            provider_model = {
                'email': 'info@examplestarter.com',
                'name': 'Example Starter Co., Inc.',
                'contact': 'Example Starter Developer Relations',
                'support_email': 'support@examplestarter.com',
                'phone': '800-555-1234',
            }
            metadata_model = {
                'version': '1.0.0',
            }
            catalog_entry_id = str(uuid.uuid4())

            catalog_entry = global_catalog_service.create_catalog_entry(
                name='exampleWebStarter123',
                kind=CatalogEntry.KindEnum.TEMPLATE,
                overview_ui={'en': overview_model_EN},
                images=image_model,
                disabled=False,
                tags=['example-tag-1', 'example-tag-2'],
                provider=provider_model,
                id=catalog_entry_id,
                active=True,
                metadata=metadata_model,
            ).get_result()

            print(json.dumps(catalog_entry, indent=2))

            # end-create_catalog_entry

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_catalog_entry_example(self):
        """
        get_catalog_entry request example
        """
        assert catalog_entry_id is not None

        try:
            print('\nget_catalog_entry() result:')
            # begin-get_catalog_entry

            catalog_entry = global_catalog_service.get_catalog_entry(
                id=catalog_entry_id,
                complete=True,
            ).get_result()

            print(json.dumps(catalog_entry, indent=2))

            # end-get_catalog_entry

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_catalog_entry_example(self):
        """
        update_catalog_entry request example
        """
        assert catalog_entry_id is not None

        try:
            print('\nupdate_catalog_entry() result:')
            # begin-update_catalog_entry

            catalog_entry = global_catalog_service.get_catalog_entry(
                id=catalog_entry_id,
                complete=True,
            ).get_result()

            overview_model_EN = {
                'display_name': 'Example Web Starter V2',
                'description': 'Use the Example V2 service in your applications',
                'long_description': 'This is a starter that helps you use the Example V2 service within your applications.',
            }
            image_model = {
                'image': 'https://somehost.com/examplewebstarter/cachedIcon/large/0',
                'small_image': 'https://somehost.com/examplewebstarter/cachedIcon/small/0',
                'medium_image': 'https://somehost.com/examplewebstarter/cachedIcon/medium/0',
                'feature_image': 'https://somehost.com/examplewebstarter/cachedIcon/large/0',
            }
            provider_model = {
                'email': 'info@examplestarter.com',
                'name': 'Example Starter Co., Inc.',
                'contact': 'Example Starter Developer Relations',
                'support_email': 'support@examplestarter.com',
                'phone': '800-555-1234',
            }
            metadata_model = {
                'version': '2.0.0',
            }

            catalog_entry = global_catalog_service.update_catalog_entry(
                id=catalog_entry_id,
                name='exampleWebStarter123',
                kind=CatalogEntry.KindEnum.TEMPLATE,
                overview_ui={
                    'en': overview_model_EN,
                },
                images=image_model,
                disabled=False,
                tags=['example-tag-1', 'example-tag-2', 'new-example-tag-3'],
                provider=provider_model,
                active=True,
                metadata=metadata_model,
                url=catalog_entry['url'],
            ).get_result()

            print(json.dumps(catalog_entry, indent=2))

            # end-update_catalog_entry

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_catalog_entries_example(self):
        """
        list_catalog_entries request example
        """
        try:
            print('\nlist_catalog_entries() result:')
            # begin-list_catalog_entries

            entry_search_result = global_catalog_service.list_catalog_entries(
                offset=0,
                limit=10,
                q='kind:template tag:example-tag-1',
                complete=True,
            ).get_result()

            print(json.dumps(entry_search_result, indent=2))

            # end-list_catalog_entries

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_child_objects_example(self):
        """
        get_child_objects request example
        """
        assert catalog_entry_id is not None

        try:
            print('\nget_child_objects() result:')
            # begin-get_child_objects

            entry_search_result = global_catalog_service.get_child_objects(
                id=catalog_entry_id,
                kind='*',
                offset=0,
                limit=10,
                complete=True,
            ).get_result()

            print(json.dumps(entry_search_result, indent=2))

            # end-get_child_objects

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_restore_catalog_entry_example(self):
        """
        restore_catalog_entry request example
        """
        assert catalog_entry_id is not None

        try:
            # begin-restore_catalog_entry

            response = global_catalog_service.restore_catalog_entry(
                id=catalog_entry_id,
            )

            # end-restore_catalog_entry

            print('\nrestore_catalog_entry() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_visibility_example(self):
        """
        get_visibility request example
        """
        assert catalog_entry_id is not None

        try:
            print('\nget_visibility() result:')
            # begin-get_visibility

            visibility = global_catalog_service.get_visibility(
                id=catalog_entry_id,
            ).get_result()

            print(json.dumps(visibility, indent=2))

            # end-get_visibility

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_visibility_example(self):
        """
        update_visibility request example
        """
        assert catalog_entry_id is not None

        try:
            # begin-update_visibility

            response = global_catalog_service.update_visibility(
                id=catalog_entry_id,
                extendable=False,
            )

            # end-update_visibility

            print('\nupdate_visibility() response status code: ', response.get_status_code())

        except ApiException as e:
            print('update_visibility() returned the following error: {0}'.format(str(e.message)))

    @needscredentials
    def test_get_pricing_example(self):
        """
        get_pricing request example
        """
        assert catalog_entry_id is not None

        try:
            print('\nget_pricing() result:')
            # begin-get_pricing

            pricing_get = global_catalog_service.get_pricing(
                id=catalog_entry_id,
            ).get_result()

            print(json.dumps(pricing_get, indent=2))

            # end-get_pricing

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_audit_logs_example(self):
        """
        get_audit_logs request example
        """
        assert catalog_entry_id is not None

        try:
            print('\nget_audit_logs() result:')
            # begin-get_audit_logs

            audit_search_result = global_catalog_service.get_audit_logs(
                id=catalog_entry_id,
                offset=0,
                limit=10,
            ).get_result()

            print(json.dumps(audit_search_result, indent=2))

            # end-get_audit_logs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_upload_artifact_example(self):
        """
        upload_artifact request example
        """
        assert catalog_entry_id is not None

        try:
            # begin-upload_artifact

            artifact_contents = io.BytesIO(b'This is an example artifact associated with a catalog entry.')

            response = global_catalog_service.upload_artifact(
                object_id=catalog_entry_id,
                artifact_id='artifact.txt',
                artifact=artifact_contents,
                content_type='text/plain',
            )

            # end-upload_artifact

            print('\nupload_artifact() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_artifact_example(self):
        """
        get_artifact request example
        """
        assert catalog_entry_id is not None

        try:
            print('\nget_artifact() result:')
            # begin-get_artifact

            response = global_catalog_service.get_artifact(
                object_id=catalog_entry_id,
                artifact_id='artifact.txt',
            )

            content_type = response.get_headers().get('content-type')
            result = response.get_result()
            print(result)

            # end-get_artifact

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_artifacts_example(self):
        """
        list_artifacts request example
        """
        assert catalog_entry_id is not None

        try:
            print('\nlist_artifacts() result:')
            # begin-list_artifacts

            artifacts = global_catalog_service.list_artifacts(object_id=catalog_entry_id).get_result()

            print(json.dumps(artifacts, indent=2))

            # end-list_artifacts

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_artifact_example(self):
        """
        delete_artifact request example
        """
        assert catalog_entry_id is not None

        try:
            # begin-delete_artifact

            response = global_catalog_service.delete_artifact(
                object_id=catalog_entry_id,
                artifact_id='artifact.txt',
            )

            # end-delete_artifact

            print('\ndelete_artifact() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_catalog_entry_example(self):
        """
        delete_catalog_entry request example
        """
        assert catalog_entry_id is not None

        try:
            # begin-delete_catalog_entry

            response = global_catalog_service.delete_catalog_entry(id=catalog_entry_id)

            # end-delete_catalog_entry

            print('\ndelete_catalog_entry() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: GlobalCatalogV1
##############################################################################
