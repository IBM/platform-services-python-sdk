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
Integration Tests for CatalogManagementV1
"""

import os

import pytest
from ibm_cloud_sdk_core import *

from ibm_platform_services.catalog_management_v1 import *

# Config file name
config_file = 'catalog_mgmt.env'

catalog_id = None
offering_id = None
object_id = None
version_locator_id = None
offering_instance_id = None
created_offering_ids = []
created_object_ids = []

kind_vpe = 'vpe'
kind_roks = 'roks'
kind_offering = 'offering'

repo_type_git_public = 'git_public'
object_name = 'object_created_by_python_sdk_5'
object_crn = 'crn:v1:bluemix:public:iam-global-endpoint:global:::endpoint:private.iam.cloud.ibm.com'
region_us_south = 'us-south'
namespace_python_sdk = 'python-sdk'
import_offering_zip_url = 'https://github.com/rhm-samples/node-red-operator/blob/master/node-red-operator/bundle/0.0' \
                          '.2/node-red-operator.v0.0.2.clusterserviceversion.yaml'

label_python_sdk = 'python-sdk'

bogus_revision = 'bogus-revision'
bogus_version_locator_id = 'bogus-version-locator-id'


class TestCatalogManagementV1():
    """
    Integration Test Class for CatalogManagementV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.catalog_management_service_authorized = CatalogManagementV1.new_instance(
            )
            assert cls.catalog_management_service_authorized is not None

            cls.catalog_management_service_not_authorized = CatalogManagementV1.new_instance(
                'NOT_AUTHORIZED'
            )
            assert cls.catalog_management_service_not_authorized is not None

            cls.config = read_external_sources(
                CatalogManagementV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.account_id = cls.config.get('ACCOUNT_ID')
            assert cls.account_id is not None

            cls.cluster_id = cls.config.get('CLUSTER_ID')
            assert cls.cluster_id is not None

            cls.git_auth_token = cls.config.get('GIT_TOKEN')
            assert cls.git_auth_token is not None

            cls.catalog_management_service_authorized.get_catalog_account()
            authenticator_authorized = cls.catalog_management_service_authorized.get_authenticator()
            token_manager_authorized = authenticator_authorized.token_manager
            cls.refresh_token_authorized = token_manager_authorized.request_token()['refresh_token']
            assert cls.refresh_token_authorized is not None

            cls.catalog_management_service_not_authorized.get_catalog_account()
            authenticator_unauthorized = cls.catalog_management_service_not_authorized.get_authenticator()
            token_manager_unauthorized = authenticator_unauthorized.token_manager
            cls.refresh_token_not_authorized = token_manager_unauthorized.request_token()['refresh_token']
            assert cls.refresh_token_not_authorized is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    ####
    # Create Catalog
    ####

    @needscredentials
    def test_create_catalog_returns_400_when_user_is_not_authorized(self):
        try:
            self.catalog_management_service_not_authorized.create_catalog(
                label=label_python_sdk,
                tags=['sdk', 'python'],
                owning_account=self.account_id,
                kind=kind_vpe,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_create_catalog_returns_400_when_backend_input_validation_fails(self):
        try:
            self.catalog_management_service_authorized.create_catalog(
                label=label_python_sdk,
                rev=bogus_revision,
                tags=['sdk', 'python'],
                owning_account=self.account_id,
                kind=kind_vpe,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_create_catalog(self):
        global catalog_id

        create_catalog_response = self.catalog_management_service_authorized.create_catalog(
            label=label_python_sdk,
            tags=['sdk', 'python'],
            kind=kind_vpe,
            owning_account=self.account_id,
        )
        assert create_catalog_response.get_status_code() == 201
        catalog = create_catalog_response.get_result()
        assert catalog is not None
        assert catalog['id'] is not None
        catalog_id = catalog['id']

    ####
    # Get Catalog
    ####

    @needscredentials
    def test_get_catalog_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None
        try:

            self.catalog_management_service_authorized.get_catalog(
                catalog_identifier='invalid-'+catalog_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_catalog_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        try:

            self.catalog_management_service_not_authorized.get_catalog(
                catalog_identifier=catalog_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_catalog(self):
        assert catalog_id is not None

        get_catalog_response = self.catalog_management_service_authorized.get_catalog(
            catalog_identifier=catalog_id,
        )

        assert get_catalog_response.get_status_code() == 200
        catalog = get_catalog_response.get_result()
        assert catalog is not None
        assert catalog['id'] == catalog_id

    ####
    # Replace Catalog
    ####

    @needscredentials
    def test_replace_catalog_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_not_authorized.replace_catalog(
                catalog_identifier=catalog_id,
                id=catalog_id,
                owning_account=self.account_id,
                kind=kind_vpe,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_replace_catalog_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.replace_catalog(
                catalog_identifier=catalog_id,
                id='invalid-'+catalog_id,
                owning_account=self.account_id,
                kind=kind_vpe,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_replace_catalog_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.replace_catalog(
                catalog_identifier='invalid-'+catalog_id,
                id='invalid-'+catalog_id,
                owning_account=self.account_id,
                kind=kind_vpe,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_replace_catalog(self):
        assert catalog_id is not None

        update_tags = ['python', 'sdk', 'update']
        replace_catalog_response = self.catalog_management_service_authorized.replace_catalog(
            catalog_identifier=catalog_id,
            id=catalog_id,
            tags=update_tags,
            owning_account=self.account_id,
            kind=kind_vpe,
        )

        assert replace_catalog_response.get_status_code() == 200
        catalog = replace_catalog_response.get_result()
        assert catalog is not None
        assert catalog['tags'] == update_tags

    ####
    # List Catalog
    ####

    @needscredentials
    def test_list_catalogs(self):
        assert catalog_id is not None

        list_catalogs_response = self.catalog_management_service_authorized.list_catalogs()

        assert list_catalogs_response.get_status_code() == 200
        catalog_search_result = list_catalogs_response.get_result()
        assert catalog_search_result is not None

        assert next((catalog for catalog in catalog_search_result['resources']
                     if catalog['id'] == catalog_id),
                    None) is not None

    ####
    # Create Offering
    ####

    @needscredentials
    def test_create_offering_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.create_offering(
                catalog_identifier='invalid-'+catalog_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_create_offering_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.create_offering(
                catalog_identifier=catalog_id,
                catalog_id=catalog_id,
                name='offering created by python sdk',
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_create_offering_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_not_authorized.create_offering(
                catalog_identifier=catalog_id,
                id=catalog_id,
                name='offering-created-by-python-sdk',
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_create_offering(self):
        global offering_id
        global created_offering_ids
        assert catalog_id is not None

        for i in range(2):
            create_offering_response = self.catalog_management_service_authorized.create_offering(
                catalog_identifier=catalog_id,
                label=label_python_sdk,
                name='offering-created-by-python-sdk-'+str(i),
            )

            assert create_offering_response.get_status_code() == 201
            offering = create_offering_response.get_result()

            assert offering is not None
            assert offering['id'] is not None
            print('offering id: '+offering['id'])
            if offering_id is None:
                offering_id = offering['id']

            created_offering_ids.append(offering['id'])

    ####
    # Get Offering
    ####

    @needscredentials
    def test_get_offering_returns_404_when_no_such_offering(self):
        assert offering_id is not None
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.get_offering(
                catalog_identifier=catalog_id,
                offering_id='invalid-'+offering_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_offering_returns_403_when_user_is_not_authorized(self):
        assert offering_id is not None
        assert catalog_id is not None

        try:
            self.catalog_management_service_not_authorized.get_offering(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_offering(self):
        assert offering_id is not None
        assert catalog_id is not None

        get_offering_response = self.catalog_management_service_authorized.get_offering(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
        )

        assert get_offering_response.get_status_code() == 200
        offering = get_offering_response.get_result()
        assert offering is not None
        assert offering['id'] == offering_id
        assert offering['catalog_id'] == catalog_id

    ####
    # Replace Offering
    ####

    @needscredentials
    def test_replace_offering_returns_404_when_no_such_offering(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.replace_offering(
                catalog_identifier=catalog_id,
                offering_id='invalid-'+offering_id,
                id='invalid-'+offering_id,
                name='updated-offering-name-by-python-sdk',
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_replace_offering_returns_400_backend_input_validation_fails(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.replace_offering(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                id=offering_id,
                name='updated offering name by python sdk',
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_replace_offering_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_not_authorized.replace_offering(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                id=offering_id,
                name='updated-offering-name-by-python-sdk',
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_replace_offering_returns_409_when_conflict_occurs(self):
        assert catalog_id is not None
        assert offering_id is not None

        # once the version related conflict is resolved this test requires a conflict case

        try:
            self.catalog_management_service_authorized.replace_offering(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                id=offering_id,
                name='updated-offering-name-by-python-sdk',
            )
        except ApiException as e:
            assert e.code == 409

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_replace_offering(self):
        assert catalog_id is not None
        assert offering_id is not None

        # update conflict on revisions

        updated_offering_name = 'updated-offering-by-python-sdk'
        replace_offering_response = self.catalog_management_service_authorized.replace_offering(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
            id=offering_id,
            name=updated_offering_name,
        )

        assert replace_offering_response.get_status_code() == 200
        offering = replace_offering_response.get_result()
        assert offering is not None
        assert offering['id'] == offering_id
        assert offering['catalog_id'] == catalog_id
        assert offering['name'] == updated_offering_name

    ####
    # Update Offering
    ####

    @needscredentials
    def test_update_offering(self):
        assert offering_id is not None
        assert catalog_id is not None

        # Get offering to use the rev
        get_offering_response = self.catalog_management_service_authorized.get_offering(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
        )

        assert get_offering_response.get_status_code() == 200
        offering = get_offering_response.get_result()
        assert offering is not None
        assert offering['id'] == offering_id
        assert offering['catalog_id'] == catalog_id

        update_offering_response = self.catalog_management_service_authorized.update_offering(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
            if_match='"'+offering['_rev']+'"',
            updates=[JsonPatchOperation(
                op="replace",
                path="/name",
                value="updated-offering-name-by-python-sdk-patch"
            )]
        )

        assert update_offering_response.get_status_code() == 200
        updatedOffering = update_offering_response.get_result()
        assert updatedOffering is not None
        assert updatedOffering['id'] == offering_id
        assert updatedOffering['catalog_id'] == catalog_id
        assert updatedOffering['name'] == "updated-offering-name-by-python-sdk-patch"

    @needscredentials
    def test_update_offering_returns_412_on_bad_request(self):
        assert offering_id is not None
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.update_offering(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                if_match='"bogus_rev"',
                updates=[JsonPatchOperation(
                    op="replace",
                    path="/name",
                    value="updated-offering-name-by-python-sdk-patch"
                )]
            )
        except ApiException as e:
            assert e.code == 412

    ####
    # List Offerings
    ####

    @needscredentials
    def test_list_offerings_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_not_authorized.list_offerings(
                catalog_identifier=catalog_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_list_offerings_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.list_offerings(
                catalog_identifier=catalog_id,
                digest=True,
                sort='bogus-sort-value'
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_list_offerings_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.list_offerings(
                catalog_identifier='invalid-'+catalog_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_list_offerings(self):
        assert catalog_id is not None

        limit = 1
        offset = 0
        amount_of_offerings = 0

        while offset > 0:
            list_offerings_response = self.catalog_management_service_authorized.list_offerings(
                catalog_identifier=catalog_id,
                limit=limit,
                offset=offset,
            )

            assert list_offerings_response.get_status_code() == 200
            offering_search_result = list_offerings_response.get_result()
            assert offering_search_result is not None

            offset_value = get_query_param(offering_search_result.next, 'offset')
            print('offset value: '+offset_value)

            if offset_value is None:
                offset = offset_value
            else:
                offset = 0

        print('Amount of offerings is: '+str(amount_of_offerings))

    ####
    # Import Offering
    ####

    @needscredentials
    def test_import_offering_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_not_authorized.import_offering(
                catalog_identifier=catalog_id,
                tags=['python', 'sdk'],
                target_kinds=[kind_vpe],
                zipurl=import_offering_zip_url,
                offering_id=offering_id,
                target_version='0.0.3',
                repo_type=repo_type_git_public,
                x_auth_token=self.git_auth_token,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_import_offering_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.import_offering(
                catalog_identifier=catalog_id,
                tags=['python', 'sdk'],
                target_kinds=['rocks'],
                zipurl=import_offering_zip_url,
                offering_id=offering_id,
                target_version='0.0.2-patch',
                repo_type=repo_type_git_public,
                x_auth_token=self.git_auth_token,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_import_offering_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.import_offering(
                catalog_identifier='invalid-'+catalog_id,
                tags=['python', 'sdk'],
                target_kinds=[kind_roks],
                zipurl=import_offering_zip_url,
                offering_id=offering_id,
                target_version='0.0.2',
                repo_type=repo_type_git_public,
                x_auth_token=self.git_auth_token,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_import_offering(self):
        global version_locator_id
        assert catalog_id is not None
        assert offering_id is not None

        import_offering_response = self.catalog_management_service_authorized.import_offering(
            catalog_identifier=catalog_id,
            tags=['python', 'sdk'],
            target_kinds=[kind_roks],
            zipurl=import_offering_zip_url,
            offering_id=offering_id,
            target_version='0.0.2',
            repo_type=repo_type_git_public,
            x_auth_token=self.git_auth_token,
        )

        assert import_offering_response.get_status_code() == 201
        offering = import_offering_response.get_result()
        assert offering is not None
        assert offering['kinds'][0]['versions'][0]['version_locator'] is not None
        version_locator_id = offering['kinds'][0]['versions'][0]['version_locator']

    @needscredentials
    def test_import_offering_returns_409_when_conflict_occurs(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.import_offering(
                catalog_identifier=catalog_id,
                tags=['python', 'sdk'],
                target_kinds=[kind_roks],
                zipurl=import_offering_zip_url,
                offering_id=offering_id,
                target_version='0.0.2',
                repo_type=repo_type_git_public,
                x_auth_token=self.git_auth_token,
            )

        except ApiException as e:
            assert e.code == 409

    ####
    # Reload Offering
    ####

    @needscredentials
    def test_reload_offering_returns_404_when_no_such_offering(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.reload_offering(
                catalog_identifier=catalog_id,
                offering_id='invalid-'+offering_id,
                target_version='0.0.2',
                target_kinds=kind_roks,
                zipurl=import_offering_zip_url,
                repo_type=repo_type_git_public,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_reload_offering_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_not_authorized.reload_offering(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                target_version='0.0.2',
                zipurl=import_offering_zip_url,
                target_kinds=kind_vpe,
                repo_type=repo_type_git_public,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_reload_offering(self):
        assert catalog_id is not None
        assert offering_id is not None

        #  Error: Could not find a kind with a target/format value of roks:operator for the current offering, Code: 400

        reload_offering_response = self.catalog_management_service_authorized.reload_offering(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
            target_version='0.0.2',
            target_kinds=kind_roks,
            zipurl=import_offering_zip_url,
            repo_type=repo_type_git_public,
        )

        assert reload_offering_response.get_status_code() == 201
        offering = reload_offering_response.get_result()
        assert offering is not None

    ####
    # Create Object
    ####

    @needscredentials
    def test_create_object_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None

        publish_object_model = {
            'permit_ibm_public_publish': True,
            'ibm_approved': True,
            'public_approved': True,
        }

        state_model = {
            'current': 'new',
        }

        try:
            self.catalog_management_service_authorized.create_object(
                catalog_identifier=catalog_id,
                catalog_id=catalog_id,
                name=object_name,
                crn=object_crn,
                parent_id='bogus region name',
                kind=kind_vpe,
                publish=publish_object_model,
                state=state_model,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_create_object_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None

        publish_object_model = {
            'permit_ibm_public_publish': True,
            'ibm_approved': True,
            'public_approved': True,
        }

        state_model = {
            'current': 'new',
        }

        try:
            self.catalog_management_service_not_authorized.create_object(
                catalog_identifier=catalog_id,
                catalog_id=catalog_id,
                name=object_name,
                crn=object_crn,
                parent_id=region_us_south,
                kind=kind_vpe,
                publish=publish_object_model,
                state=state_model,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_create_object_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None

        publish_object_model = {
            'permit_ibm_public_publish': True,
            'ibm_approved': True,
            'public_approved': True,
        }

        state_model = {
            'current': 'new',
        }

        try:
            self.catalog_management_service_authorized.create_object(
                catalog_identifier='invalid-'+catalog_id,
                catalog_id='invalid-'+catalog_id,
                name=object_name,
                crn=object_crn,
                parent_id=region_us_south,
                kind=kind_vpe,
                publish=publish_object_model,
                state=state_model,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_create_object(self):
        global object_id
        global created_object_ids
        assert catalog_id is not None

        for i in range(2):
            publish_object_model = {
                'permit_ibm_public_publish': True,
                'ibm_approved': True,
                'public_approved': True,
            }
            state_model = {
                'current': 'new',
            }

            name = object_name+'_'+str(i)
            create_object_response = self.catalog_management_service_authorized.create_object(
                catalog_identifier=catalog_id,
                catalog_id=catalog_id,
                name=name,
                crn=object_crn,
                parent_id=region_us_south,
                kind=kind_vpe,
                publish=publish_object_model,
                state=state_model,
            )

            assert create_object_response.get_status_code() == 201
            catalog_object = create_object_response.get_result()
            assert catalog_object is not None
            assert catalog_object['id'] is not None

            if object_id is None:
                object_id = catalog_object['id']

            created_object_ids.append(catalog_object['id'])

    ####
    # Get Offering Audit
    ####

    @needscredentials
    def test_get_offering_audit_returns_200_when_no_such_offerings(self):
        assert catalog_id is not None
        assert offering_id is not None

        get_offering_audit_response = self.catalog_management_service_authorized.get_offering_audit(
            catalog_identifier=catalog_id,
            offering_id='invalid-'+offering_id,
        )

        assert get_offering_audit_response.get_status_code() == 200

    @needscredentials
    def test_get_offering_audit_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_not_authorized.get_offering_audit(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_offering_audit(self):
        assert catalog_id is not None
        assert offering_id is not None

        get_offering_audit_response = self.catalog_management_service_authorized.get_offering_audit(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
        )

        assert get_offering_audit_response.get_status_code() == 200
        audit_log = get_offering_audit_response.get_result()
        assert audit_log is not None

    ####
    # Get Catalog Account
    ####

    @needscredentials
    def test_get_catalog_account(self):
        get_catalog_account_response = self.catalog_management_service_authorized.get_catalog_account()

        assert get_catalog_account_response.get_status_code() == 200
        account = get_catalog_account_response.get_result()
        assert account is not None
        assert account['id'] == self.account_id

    ####
    # Update Catalog Account
    ####

    @needscredentials
    def test_update_catalog_account_returns_400_when_no_such_account(self):

        try:
            self.catalog_management_service_authorized.update_catalog_account(
                id='invalid-'+self.account_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_update_catalog_account_returns_403_when_user_is_not_authorized(self):

        try:
            self.catalog_management_service_not_authorized.update_catalog_account(
                id=self.account_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_update_catalog_account_returns_400_when_backend_input_validation_fails(self):

        # user is not granted for this operation
        # a body with failing data comes here

        update_catalog_account_response = self.catalog_management_service_authorized.update_catalog_account(
            id=self.account_id,
            hide_ibm_cloud_catalog=True,
        )

        assert update_catalog_account_response.get_status_code() == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_update_catalog_account(self):

        # user is not granted for this operation
        # a body with failing data comes here

        update_catalog_account_response = self.catalog_management_service_authorized.update_catalog_account(
            id=self.account_id,
        )

        assert update_catalog_account_response.get_status_code() == 200
        assert update_catalog_account_response.get_result() is not None

    ####
    # Get Catalog Account Audit
    ####

    @needscredentials
    def test_get_catalog_account_audit_returns_403_when_user_is_not_authorized(self):
        try:
            self.catalog_management_service_not_authorized.get_catalog_account_audit()
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_catalog_account_audit(self):
        get_catalog_account_audit_response = self.catalog_management_service_authorized.get_catalog_account_audit()

        assert get_catalog_account_audit_response.get_status_code() == 200
        assert get_catalog_account_audit_response.get_result() is not None

    ####
    # Get Catalog Account Filters
    ####

    @needscredentials
    def test_get_catalog_account_filters_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_not_authorized.get_catalog_account_filters(
                catalog=catalog_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_catalog_account_filters_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.get_catalog_account_filters(
                catalog='invalid-'+catalog_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_catalog_account_filters(self):
        assert catalog_id is not None
        get_catalog_account_filters_response = self.catalog_management_service_authorized.get_catalog_account_filters(
            catalog=catalog_id,
        )

        assert get_catalog_account_filters_response.get_status_code() == 200
        accumulated_filters = get_catalog_account_filters_response.get_result()
        assert accumulated_filters is not None

    ####
    # Get Catalog Audit
    ####
    @needscredentials
    def test_get_catalog_audit_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.get_catalog_audit(
                catalog_identifier='invalid-'+catalog_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_catalog_audit_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_not_authorized.get_catalog_audit(
                catalog_identifier=catalog_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_catalog_audit(self):
        assert catalog_id is not None

        get_catalog_audit_response = self.catalog_management_service_authorized.get_catalog_audit(
            catalog_identifier=catalog_id,
        )

        assert get_catalog_audit_response.get_status_code() == 200
        audit_log = get_catalog_audit_response.get_result()
        assert audit_log is not None

    ####
    # Get Consumption Offerings
    ####

    @needscredentials
    def test_get_consumption_offerings_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_not_authorized.get_consumption_offerings(
                catalog=catalog_id,
                select='all',
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_consumption_offerings_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.get_consumption_offerings(
                catalog='invalid-'+catalog_id,
                select='all',
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_consumption_offerings(self):
        assert catalog_id is not None

        get_consumption_offerings_response = self.catalog_management_service_authorized.get_consumption_offerings(
            catalog=catalog_id,
            select='all',
        )

        assert get_consumption_offerings_response.get_status_code() == 200
        offering_search_result = get_consumption_offerings_response.get_result()
        assert offering_search_result is not None

    ####
    # Import Offering Version
    ####

    @needscredentials
    def test_import_offering_version_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.import_offering_version(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                target_kinds=['rocks'],
                zipurl=import_offering_zip_url,
                target_version='0.0.3',
                repo_type=repo_type_git_public,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_import_offering_version_returns_404_when_no_such_offerings(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.import_offering_version(
                catalog_identifier=catalog_id,
                offering_id='invalid-'+offering_id,
                target_kinds=[kind_roks],
                zipurl=import_offering_zip_url,
                target_version='0.0.3',
                repo_type=repo_type_git_public,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_import_offering_version_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_not_authorized.import_offering_version(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                target_kinds=[kind_roks],
                zipurl=import_offering_zip_url,
                target_version='0.0.3',
                repo_type=repo_type_git_public,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_import_offering_version(self):
        assert catalog_id is not None
        assert offering_id is not None

        import_offering_version_response = self.catalog_management_service_authorized.import_offering_version(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
            target_kinds=[kind_roks],
            zipurl=import_offering_zip_url,
            target_version='0.0.3',
            repo_type=repo_type_git_public,
        )

        assert import_offering_version_response.get_status_code() == 201
        offering = import_offering_version_response.get_result()
        assert offering is not None

    ####
    # Replace Offering Icon
    ####

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_replace_offering_icon_returns_404_when_no_such_offerings(self):
        assert catalog_id is not None
        assert offering_id is not None

        # this feature is disabled

        try:
            self.catalog_management_service_authorized.replace_offering_icon(
                catalog_identifier=catalog_id,
                offering_id='invalid-'+offering_id,
                file_name='filename.jpg',
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_replace_offering_icon_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        # this feature is disabled

        try:
            self.catalog_management_service_not_authorized.replace_offering_icon(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                file_name='filename.jpg',
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_replace_offering_icon(self):
        assert catalog_id is not None
        assert offering_id is not None

        # this feature is disabled

        replace_offering_icon_response = self.catalog_management_service_authorized.replace_offering_icon(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
            file_name='filename.jpg',
        )

        assert replace_offering_icon_response.get_status_code() == 200
        offering = replace_offering_icon_response.get_result()
        assert offering is not None

    ####
    # Update Offering IBM
    ####

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_update_offering_ibm_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None
        assert offering_id is not None

        # once the user is granted for this operation it can be executed

        try:
            self.catalog_management_service_authorized.update_offering_ibm(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                approval_type='bogus approval type',
                approved='true',
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_update_offering_ibm_returns_404_when_no_such_offerings(self):
        assert catalog_id is not None
        assert offering_id is not None

        # once the user is granted for this operation 404 can be squeezed out from the system, until then it is disabled

        try:
            self.catalog_management_service_authorized.update_offering_ibm(
                catalog_identifier=catalog_id,
                offering_id='invalid-'+offering_id,
                approval_type='allow_request',
                approved='true',
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_update_offering_ibm_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_not_authorized.update_offering_ibm(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                approval_type='allow_request',
                approved='true',
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_update_offering_ibm(self):
        assert catalog_id is not None
        assert offering_id is not None

        # once the user is granted for this operation it can be executed

        update_offering_ibm_response = self.catalog_management_service_authorized.update_offering_ibm(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
            approval_type='allow_request',
            approved='true',
        )

        assert update_offering_ibm_response.get_status_code() == 200
        approval_result = update_offering_ibm_response.get_result()
        assert approval_result is not None

    ####
    # Get Offering Updates
    ####

    @needscredentials
    def test_get_offering_updates_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.get_offering_updates(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                kind='rocks',
                version='0.0.2',
                cluster_id=self.cluster_id,
                region=region_us_south,
                x_auth_refresh_token=self.refresh_token_authorized,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_offering_updates_returns_404_when_no_such_offerings(self):
        assert catalog_id is not None
        assert offering_id is not None

        # it always complaining about offering types which is somehow related to create/import offerings
        # once this is resolved there is a chance we can squeeze a 404 out from the service

        try:
            self.catalog_management_service_authorized.get_offering_updates(
                catalog_identifier=catalog_id,
                offering_id='invalid-'+offering_id,
                version='0.0.2',
                kind=kind_vpe,
                cluster_id=self.cluster_id,
                region=region_us_south,
                namespace=namespace_python_sdk,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_offering_updates_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_not_authorized.get_offering_updates(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
                kind=kind_roks,
                version='0.0.2',
                cluster_id=self.cluster_id,
                region=region_us_south,
                namespace=namespace_python_sdk,
                x_auth_refresh_token=self.refresh_token_not_authorized,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_offering_updates(self):
        assert catalog_id is not None
        assert offering_id is not None

        # requires a special offering
        # Error: Could not find kind[roks] for offering

        get_offering_updates_response = self.catalog_management_service_authorized.get_offering_updates(
            catalog_identifier=catalog_id,
            offering_id=offering_id,
            kind=kind_roks,
            version='0.0.2',
            cluster_id=self.cluster_id,
            region=region_us_south,
            namespace=namespace_python_sdk,
        )

        assert get_offering_updates_response.get_status_code() == 200
        list_version_update_descriptor = get_offering_updates_response.get_result()
        assert list_version_update_descriptor is not None

    ####
    # Get Offering About
    ####

    @needscredentials
    def test_get_offering_about_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.get_offering_about(
                version_loc_id=bogus_version_locator_id,
            )

        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_get_offering_about_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.get_offering_about(
                version_loc_id='invalid-'+version_locator_id,
            )

        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_offering_about_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.get_offering_about(
                version_loc_id=version_locator_id,
            )

        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_offering_about(self):
        assert version_locator_id is not None

        get_offering_about_response = self.catalog_management_service_authorized.get_offering_about(
            version_loc_id=version_locator_id,
        )

        assert get_offering_about_response.get_status_code() == 200
        result = get_offering_about_response.get_result()
        assert result is not None

    ####
    # Get Offering License
    ####

    @needscredentials
    def test_get_offering_license_returns_400_when_backend_input_validation_fails(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.get_offering_license(
                version_loc_id=bogus_version_locator_id,
                license_id='license-id-is-needed',
            )

        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_get_offering_license_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.get_offering_license(
                version_loc_id='invalid-'+version_locator_id,
                license_id='license-id-is-needed',
            )

        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_offering_license_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.get_offering_license(
                version_loc_id=version_locator_id,
                license_id='license-id-is-needed',
            )

        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_offering_license(self):
        assert version_locator_id is not None

        get_offering_license_response = self.catalog_management_service_authorized.get_offering_license(
            version_loc_id=version_locator_id,
            license_id='license-id-is-needed',
        )

        assert get_offering_license_response.get_status_code() == 200
        result = get_offering_license_response.get_result()
        assert result is not None

    ####
    # Get Offering Container Images
    ####

    @needscredentials
    def test_get_offering_container_images_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.get_offering_container_images(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_get_offering_container_images_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.get_offering_container_images(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_offering_container_images_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.get_offering_container_images(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_offering_container_images(self):
        assert version_locator_id is not None

        get_offering_container_images_response = self.catalog_management_service_authorized.get_offering_container_images(
            version_loc_id=version_locator_id,
        )

        assert get_offering_container_images_response.get_status_code() == 200
        image_manifest = get_offering_container_images_response.get_result()
        assert image_manifest is not None

    ####
    # Deprecate Version
    ####

    @needscredentials
    def test_deprecate_version_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.deprecate_version(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_deprecate_version_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.deprecate_version(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_deprecate_version_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.deprecate_version(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_deprecate_version(self):
        assert version_locator_id is not None

        # the flow of different states
        #  Error: Cannot request the state deprecated from the current state new.

        deprecate_version_response = self.catalog_management_service_authorized.deprecate_version(
            version_loc_id=version_locator_id
        )

        assert deprecate_version_response.get_status_code() == 202

    ####
    # Account Publish Version
    ####

    @needscredentials
    def test_account_publish_version_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.account_publish_version(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_account_publish_version_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.account_publish_version(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_account_publish_version_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.account_publish_version(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_account_publish_version(self):
        assert version_locator_id is not None

        # the phases of different states is unknown
        #  Error: Cannot request the state account-published from the current state new.

        account_publish_version_response = self.catalog_management_service_authorized.account_publish_version(
            version_loc_id=version_locator_id,
        )

        assert account_publish_version_response.get_status_code() == 202

    ####
    # IBM Publish Version
    ####

    @needscredentials
    def test_ibm_publish_version_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.ibm_publish_version(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_ibm_publish_version_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.ibm_publish_version(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_ibm_publish_version_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.ibm_publish_version(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_ibm_publish_version(self):
        assert version_locator_id is not None

        # user is not allowed to publish

        ibm_publish_version_response = self.catalog_management_service_authorized.ibm_publish_version(
            version_loc_id=version_locator_id,
        )

        assert ibm_publish_version_response.get_status_code() == 202

    ####
    # Public Publish Version
    ####

    @needscredentials
    def test_public_publish_version_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.public_publish_version(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_public_publish_version_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.public_publish_version(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_public_publish_version_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.public_publish_version(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_public_publish_version(self):
        assert version_locator_id is not None

        # user is not granted

        public_publish_version_response = self.catalog_management_service_authorized.public_publish_version(
            version_loc_id=version_locator_id,
        )

        assert public_publish_version_response.get_status_code() == 202

    ####
    # Commit Version
    ####

    @needscredentials
    def test_commit_version_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.commit_version(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_commit_version_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.commit_version(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_commit_version_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.commit_version(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_commit_version(self):
        assert version_locator_id is not None

        # workflow of versions
        # Error: Could not find a working copy for the active version with id

        commit_version_response = self.catalog_management_service_authorized.commit_version(
            version_loc_id=version_locator_id,
        )

        assert commit_version_response.get_status_code() == 200

    ####
    # Copy Version
    ####

    @needscredentials
    def test_copy_version_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.copy_version(
                version_loc_id=version_locator_id,
                target_kinds=[kind_roks],
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_copy_version_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.copy_version(
                version_loc_id='invalid-'+version_locator_id,
                target_kinds=[kind_roks],
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_copy_version_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.copy_version(
                version_loc_id=bogus_version_locator_id,
                target_kinds=[kind_roks],
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_copy_version(self):
        assert version_locator_id is not None

        # Error: Only helm charts can be copied to a new target at this time.

        copy_version_response = self.catalog_management_service_authorized.copy_version(
            version_loc_id=version_locator_id,
            target_kinds=[kind_roks],
        )

        assert copy_version_response.get_status_code() == 200

    ####
    # Get Offering Working Copy
    ####

    @needscredentials
    def test_get_offering_working_copy_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.get_offering_working_copy(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_get_offering_working_copy_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.get_offering_working_copy(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_offering_working_copy_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.get_offering_working_copy(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_offering_working_copy(self):
        assert version_locator_id is not None

        # workflow problem
        # Error: Cannot create a working copy for version 60cb36c3-39fd-40ed-9887-6bc98aa7b7be.  The version
        # must be in a published state, deprecated state, or invalidated state to create a working copy

        get_offering_working_copy_response = self.catalog_management_service_authorized.get_offering_working_copy(
            version_loc_id=version_locator_id,
        )

        assert get_offering_working_copy_response.get_status_code() == 200
        version = get_offering_working_copy_response.get_result()
        assert version is not None

    ####
    # Get Version
    ####

    @needscredentials
    def test_get_version_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.get_version(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_get_version_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.get_version(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_version_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.get_version(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_version(self):
        assert version_locator_id is not None

        get_version_response = self.catalog_management_service_authorized.get_version(
            version_loc_id=version_locator_id,
        )

        assert get_version_response.get_status_code() == 200
        offering = get_version_response.get_result()
        assert offering is not None

    ####
    # Get Cluster
    ####

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_cluster_returns_403_when_user_is_not_authorized(self):

        # possibly this user doesn't have right to execute this operation

        try:
            self.catalog_management_service_not_authorized.get_cluster(
                cluster_id=self.cluster_id,
                region=region_us_south,
                x_auth_refresh_token=self.refresh_token_not_authorized,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_cluster_returns_404_when_no_such_cluster(self):

        try:
            self.catalog_management_service_authorized.get_cluster(
                cluster_id='invalid-'+self.cluster_id,
                region=region_us_south,
                x_auth_refresh_token=self.refresh_token_authorized,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_cluster(self):

        # possibly this user doesn't have right to get the cluster details
        # until it is not clear it is skipped
        # The specified cluster could not be found. If applicable, make sure that you target the correct account
        # and resource group."

        get_cluster_response = self.catalog_management_service_authorized.get_cluster(
            cluster_id=self.cluster_id,
            region=region_us_south,
            x_auth_refresh_token=self.refresh_token_authorized,
        )
        assert get_cluster_response.get_status_code() == 200
        cluster_info = get_cluster_response.get_result()
        assert cluster_info is not None

    ####
    # Get Namespaces
    ####

    @needscredentials
    def test_get_namespaces_returns_404_when_no_such_cluster(self):
        try:
            self.catalog_management_service_authorized.get_namespaces(
                cluster_id='invalid-'+self.cluster_id,
                region=region_us_south,
                x_auth_refresh_token=self.refresh_token_authorized,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_namespaces_returns_403_when_user_is_not_authorized(self):

        # possibly this user doesn't have right to get the cluster details
        # until it is not clear it is skipped
        # The specified cluster could not be found. If applicable, make sure that you target the correct account
        # and resource group."

        try:
            self.catalog_management_service_not_authorized.get_namespaces(
                cluster_id=self.cluster_id,
                region=region_us_south,
                x_auth_refresh_token=self.refresh_token_not_authorized,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_namespaces(self):

        # possibly this user doesn't have right to get the cluster details
        # until it is not clear it is skipped
        # The specified cluster could not be found. If applicable, make sure that you target the correct account
        # and resource group."

        get_namespaces_response = self.catalog_management_service_authorized.get_namespaces(
            cluster_id=self.cluster_id,
            region=region_us_south,
            x_auth_refresh_token=self.refresh_token_authorized,
        )

        assert get_namespaces_response.get_status_code() == 200
        namespace_search_result = get_namespaces_response.get_result()
        assert namespace_search_result is not None

    ####
    # Deploy Operators
    ####

    @needscredentials
    def test_deploy_operators_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.deploy_operators(
                x_auth_refresh_token=self.refresh_token_not_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                all_namespaces=True,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_deploy_operators_returns_404_when_no_such_cluster(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.deploy_operators(
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id='invalid-'+self.cluster_id,
                region=region_us_south,
                all_namespaces=True,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_deploy_operators_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.deploy_operators(
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                all_namespaces=True,
                version_locator_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_deploy_operators(self):
        assert version_locator_id is not None

        # possibly this user doesn't have right to get the cluster details
        # until it is not clear it is skipped
        # The specified cluster could not be found. If applicable, make sure that you target the correct account
        # and resource group."

        deploy_operators_response = self.catalog_management_service_authorized.deploy_operators(
            x_auth_refresh_token=self.refresh_token_authorized,
            cluster_id=self.cluster_id,
            region=region_us_south,
            all_namespaces=True,
            version_locator_id=version_locator_id,
        )

        assert deploy_operators_response.get_status_code() == 200
        list_operator_deploy_result = deploy_operators_response.get_result()
        assert list_operator_deploy_result is not None

    ####
    # List Operators
    ####

    @needscredentials
    def test_list_operators_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.list_operators(
                x_auth_refresh_token=self.refresh_token_not_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_list_operators_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.list_operators(
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_list_operators_returns_404_when_no_such_cluster(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.list_operators(
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id='invalid-'+self.cluster_id,
                region=region_us_south,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_list_operators(self):
        assert version_locator_id is not None

        # possibly this user doesn't have right to get the cluster details
        # until it is not clear it is skipped
        # The specified cluster could not be found. If applicable, make sure that you target the correct account
        # and resource group."

        list_operators_response = self.catalog_management_service_authorized.list_operators(
            x_auth_refresh_token=self.refresh_token_authorized,
            cluster_id=self.cluster_id,
            region=region_us_south,
            version_locator_id=version_locator_id,
        )

        assert list_operators_response.get_status_code() == 200
        list_operator_deploy_result = list_operators_response.get_result()
        assert list_operator_deploy_result is not None

    ####
    # Replace Operators
    ####

    @needscredentials
    def test_replace_operators_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.replace_operators(
                x_auth_refresh_token=self.refresh_token_not_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                all_namespaces=True,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_replace_operators_returns_404_when_no_such_cluster(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.replace_operators(
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id='invalid-'+self.cluster_id,
                region=region_us_south,
                all_namespaces=True,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_replace_operators_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.replace_operators(
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                all_namespaces=True,
                version_locator_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_replace_operators(self):
        assert version_locator_id is not None

        # possibly this user doesn't have right to get the cluster details
        # until it is not clear it is skipped
        # The specified cluster could not be found. If applicable, make sure that you target the correct account
        # and resource group."

        replace_operators_response = self.catalog_management_service_authorized.replace_operators(
            x_auth_refresh_token=self.refresh_token_authorized,
            cluster_id=self.cluster_id,
            region=region_us_south,
            all_namespaces=True,
            version_locator_id=version_locator_id,
        )

        assert replace_operators_response.get_status_code() == 200
        list_operator_deploy_result = replace_operators_response.get_result()
        assert list_operator_deploy_result is not None

    ####
    # Install Version
    ####

    @needscredentials
    def test_install_version_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.install_version(
                version_loc_id=version_locator_id,
                x_auth_refresh_token=self.refresh_token_not_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_install_version_returns_404_when_no_such_cluster(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.install_version(
                version_loc_id=version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id='invalid-'+self.cluster_id,
                region=region_us_south,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_install_version_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.install_version(
                version_loc_id=bogus_version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_install_version(self):
        assert version_locator_id is not None

        # possibly this user doesn't have right to get the cluster details
        # until it is not clear it is skipped
        # The specified cluster could not be found. If applicable, make sure that you target the correct account
        # and resource group."

        install_version_response = self.catalog_management_service_authorized.install_version(
            version_loc_id=version_locator_id,
            x_auth_refresh_token=self.refresh_token_authorized,
            cluster_id=self.cluster_id,
            region=region_us_south,
            version_locator_id=version_locator_id,
        )

        assert install_version_response.get_status_code() == 202

    ####
    # Preinstall Version
    ####

    @needscredentials
    def test_preinstall_version_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.preinstall_version(
                version_loc_id=version_locator_id,
                x_auth_refresh_token=self.refresh_token_not_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_preinstall_version_returns_404_when_no_such_cluster(self):

        # it requires a version where preinstall script is installed
        # but I don't know how to do it
        # once it is done possible to squeeze a 404 from the cluster

        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.preinstall_version(
                version_loc_id=version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id='invalid-'+self.cluster_id,
                region=region_us_south,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_preinstall_version_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.preinstall_version(
                version_loc_id=bogus_version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_preinstall_version(self):
        assert version_locator_id is not None

        # Error: Attempt to run pre-install script on a version that has no pre-install script specified

        preinstall_version_response = self.catalog_management_service_authorized.preinstall_version(
            version_loc_id=version_locator_id,
            x_auth_refresh_token=self.refresh_token_authorized,
            cluster_id=self.cluster_id,
            region=region_us_south,
            version_locator_id=version_locator_id,
        )

        assert preinstall_version_response.get_status_code() == 202

    ####
    # Get Preinstall
    ####

    @needscredentials
    def test_get_preinstall_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.get_preinstall(
                version_loc_id=version_locator_id,
                x_auth_refresh_token=self.refresh_token_not_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_preinstall_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.get_preinstall(
                version_loc_id='invalid-'+version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_preinstall_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.get_preinstall(
                version_loc_id=bogus_version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_preinstall(self):
        assert version_locator_id is not None

        # Error: Attempt to get pre-install status on a version that has no pre-install script

        get_preinstall_response = self.catalog_management_service_authorized.get_preinstall(
            version_loc_id=version_locator_id,
            x_auth_refresh_token=self.refresh_token_authorized,
            cluster_id=self.cluster_id,
            region=region_us_south,
        )

        assert get_preinstall_response.get_status_code() == 200
        install_status = get_preinstall_response.get_result()
        assert install_status is not None

    ####
    # Validate Install
    ####

    @needscredentials
    def test_validate_install_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.validate_install(
                version_loc_id=version_locator_id,
                x_auth_refresh_token=self.refresh_token_not_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_validate_install_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.validate_install(
                version_loc_id='invalid'+version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_validate_install_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.validate_install(
                version_loc_id=bogus_version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_validate_install(self):
        assert version_locator_id is not None

        # possibly this user doesn't have right to get the cluster details
        # until it is not clear it is skipped
        # The specified cluster could not be found. If applicable, make sure that you target the correct account
        # and resource group."

        validate_install_response = self.catalog_management_service_authorized.validate_install(
            version_loc_id=version_locator_id,
            x_auth_refresh_token=self.refresh_token_authorized,
            cluster_id=self.cluster_id,
            region=region_us_south,
            version_locator_id=version_locator_id,
        )

        assert validate_install_response.get_status_code() == 202

    ####
    # Get Validation Status
    ####

    @needscredentials
    def test_get_validation_status_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.get_validation_status(
                version_loc_id=version_locator_id,
                x_auth_refresh_token=self.refresh_token_not_authorized,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_validation_status_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.get_validation_status(
                version_loc_id='invalid-'+version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_validation_status_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.get_validation_status(
                version_loc_id=bogus_version_locator_id,
                x_auth_refresh_token=self.refresh_token_authorized,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_get_validation_status(self):
        assert version_locator_id is not None

        get_validation_status_response = self.catalog_management_service_authorized.get_validation_status(
            version_loc_id=version_locator_id,
            x_auth_refresh_token=self.refresh_token_authorized,
        )

        assert get_validation_status_response.get_status_code() == 200
        validation = get_validation_status_response.get_result()
        assert validation is not None

    ####
    # Get Override Values
    ####

    @needscredentials
    def test_get_override_values_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.get_override_values(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_override_values_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.get_override_values(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_override_values_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.get_override_values(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_override_values(self):

        # requires validation run before this operation

        assert version_locator_id is not None

        get_override_values_response = self.catalog_management_service_authorized.get_override_values(
            version_loc_id=version_locator_id,
        )

        assert get_override_values_response.get_status_code() == 200
        result = get_override_values_response.get_result()
        assert result is not None

    ####
    # Search Objects
    ####

    @needscredentials
    def test_search_objects_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.search_objects(
                query='',
                collapse=True,
                digest=True,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_search_objects_returns_200_when_user_is_not_authorized(self):

        search_objects_response = self.catalog_management_service_not_authorized.search_objects(
            query='name: '+object_name,
            collapse=True,
            digest=True,
        )

        assert search_objects_response.get_status_code() == 200
        object_search_result = search_objects_response.get_result()
        assert object_search_result is not None

    @needscredentials
    def test_search_objects(self):

        limit = 1
        offset = 0

        while offset > 0:
            search_objects_response = self.catalog_management_service_authorized.search_objects(
                query='name: object*',
                collapse=True,
                digest=True,
                limit=limit,
                offset=offset,
            )

            assert search_objects_response.get_status_code() == 200
            object_search_result = search_objects_response.get_result()
            assert object_search_result is not None
            offset_value = get_query_param(object_search_result.next, 'offset')
            if offset_value is not None:
                offset = offset_value
            else:
                offset = 0

    ####
    # List Objects
    ####

    @needscredentials
    def test_list_objects_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.list_objects(
                catalog_identifier=catalog_id,
                name=' ',
                sort=' '
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_list_objects_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_not_authorized.list_objects(
                catalog_identifier=catalog_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_list_objects(self):
        assert catalog_id is not None

        limit = 1
        offset = 0

        while offset > 0:
            list_objects_response = self.catalog_management_service_authorized.list_objects(
                catalog_identifier=catalog_id,
                limit=limit,
                offset=offset,
            )

            assert list_objects_response.get_status_code() == 200
            object_list_result = list_objects_response.get_result()
            assert object_list_result is not None
            offset_value = get_query_param(object_list_result.next, 'offset');
            if offset_value is not None:
                offset = offset_value
            else:
                offset = 0

    ####
    # Replace Object
    ####

    @needscredentials
    def test_replace_object_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.replace_object(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
                id=object_id,
                name='updated-object-name-created-by-python-sdk',
                parent_id=region_us_south,
                kind=kind_vpe,
                catalog_id=catalog_id,
                data={},
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_replace_object_returns_404_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.replace_object(
                catalog_identifier=catalog_id,
                object_identifier='invalid-'+object_id,
                id='invalid-'+object_id,
                name='updated-object-name-created-by-python-sdk',
                parent_id=region_us_south,
                kind=kind_vpe,
                catalog_id=catalog_id,
                data={},
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_replace_object_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.replace_object(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
                id=object_id,
                name='updated object name created by python sdk',
                parent_id=region_us_south,
                kind=kind_vpe,
                catalog_id=catalog_id,
                data={},
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_replace_object(self):

        # cannot change name of object, what can be changed?

        assert catalog_id is not None
        assert object_id is not None

        replace_object_response = self.catalog_management_service_authorized.replace_object(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
            id=object_id,
            name='updated-object-name-created-by-python-sdk',
            parent_id=region_us_south,
            kind=kind_vpe,
            catalog_id=catalog_id,
            data={},
        )

        assert replace_object_response.get_status_code() == 200
        catalog_object = replace_object_response.get_result()
        assert catalog_object is not None

    ####
    # Get Object
    ####

    @needscredentials
    def test_get_object_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.get_object(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_object_returns_404_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.get_object(
                catalog_identifier=catalog_id,
                object_identifier='invalid-'+object_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_get_object(self):
        assert catalog_id is not None
        assert object_id is not None

        get_object_response = self.catalog_management_service_authorized.get_object(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
        )

        assert get_object_response.get_status_code() == 200
        catalog_object = get_object_response.get_result()
        assert catalog_object is not None

    ####
    # Get Object Audit
    ####

    @needscredentials
    def test_get_object_audit_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.get_object_audit(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_object_audit_returns_200_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        get_object_audit_response = self.catalog_management_service_authorized.get_object_audit(
            catalog_identifier=catalog_id,
            object_identifier='invalid-'+object_id,
        )

        assert get_object_audit_response.get_status_code() == 200
        audit_log = get_object_audit_response.get_result()
        assert audit_log is not None

    @needscredentials
    def test_get_object_audit(self):
        assert catalog_id is not None
        assert object_id is not None

        get_object_audit_response = self.catalog_management_service_authorized.get_object_audit(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
        )

        assert get_object_audit_response.get_status_code() == 200
        audit_log = get_object_audit_response.get_result()
        assert audit_log is not None

    ####
    # Account Publish Object
    ####

    @needscredentials
    def test_account_publish_object_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.account_publish_object(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_account_publish_object_returns_404_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.account_publish_object(
                catalog_identifier=catalog_id,
                object_identifier='invalid-'+object_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_account_publish_object(self):
        assert catalog_id is not None
        assert object_id is not None

        account_publish_object_response = self.catalog_management_service_authorized.account_publish_object(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
        )

        assert account_publish_object_response.get_status_code() == 202

    ####
    # Shared Publish Object
    ####

    @needscredentials
    def test_shared_publish_object_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.shared_publish_object(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_shared_publish_object_returns_404_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.shared_publish_object(
                catalog_identifier=catalog_id,
                object_identifier='invalid-'+object_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_shared_publish_object(self):
        assert catalog_id is not None
        assert object_id is not None

        # Error: An invalid catalog object was provided

        shared_publish_object_response = self.catalog_management_service_authorized.shared_publish_object(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
        )

        assert shared_publish_object_response.get_status_code() == 202

    ####
    # IBM Publish Object
    ####

    @needscredentials
    def test_ibm_publish_object_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.ibm_publish_object(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_ibm_publish_object_returns_404_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.ibm_publish_object(
                catalog_identifier=catalog_id,
                object_identifier='invalid-'+object_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_ibm_publish_object(self):
        assert catalog_id is not None
        assert object_id is not None

        # Error: Object not approved to request publishing to IBM for

        ibm_publish_object_response = self.catalog_management_service_authorized.ibm_publish_object(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
        )

        assert ibm_publish_object_response.get_status_code() == 202

    ####
    # Public Publish Object
    ####

    @needscredentials
    def test_public_publish_object_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.public_publish_object(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_public_publish_object_returns_404_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.public_publish_object(
                catalog_identifier=catalog_id,
                object_identifier='invalid-'+object_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_public_publish_object(self):
        assert catalog_id is not None
        assert object_id is not None

        # Error: Object not approved to request publishing to IBM for

        public_publish_object_response = self.catalog_management_service_authorized.public_publish_object(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
        )

        assert public_publish_object_response.get_status_code() == 202

    ####
    # Create Object Access
    ####

    @needscredentials
    def test_create_object_access_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.create_object_access(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
                account_identifier=self.account_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_create_object_access_returns_404_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.create_object_access(
                catalog_identifier=catalog_id,
                object_identifier='invalid-'+object_id,
                account_identifier=self.account_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_create_object_access(self):
        assert catalog_id is not None
        assert object_id is not None

        create_object_access_response = self.catalog_management_service_authorized.create_object_access(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
            account_identifier=self.account_id,
        )

        assert create_object_access_response.get_status_code() == 201

    ####
    # Get Object Access List
    ####

    @needscredentials
    def test_get_object_access_list_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.get_object_access_list(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_object_access_list_returns_200_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        get_object_access_list_response = self.catalog_management_service_authorized.get_object_access_list(
            catalog_identifier=catalog_id,
            object_identifier='invalid-'+object_id,
        )

        assert get_object_access_list_response.get_status_code() == 200
        object_access_list_result = get_object_access_list_response.get_result()
        assert object_access_list_result is not None

    # pager
    @needscredentials
    def test_get_object_access_list(self):
        assert catalog_id is not None
        assert object_id is not None

        get_object_access_list_response = self.catalog_management_service_authorized.get_object_access_list(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
        )

        assert get_object_access_list_response.get_status_code() == 200
        object_access_list_result = get_object_access_list_response.get_result()
        assert object_access_list_result is not None

    ####
    # Get Object Access
    ####

    @needscredentials
    def test_get_object_access_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.get_object_access(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
                account_identifier=self.account_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_get_object_access_returns_404_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.get_object_access(
                catalog_identifier=catalog_id,
                object_identifier='invalid-'+object_id,
                account_identifier=self.account_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_object_access(self):
        assert catalog_id is not None
        assert object_id is not None

        #  Error: Error loading version with id: 6e263640-4805-471d-a30c-d7667325581c.
        #  e59ad442-d113-49e4-bcd4-5431990135fd: Error[404 Not Found]

        get_object_access_response = self.catalog_management_service_authorized.get_object_access(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
            account_identifier=self.account_id,
        )

        assert get_object_access_response.get_status_code() == 200
        object_access = get_object_access_response.get_result()
        assert object_access is not None

    ####
    # Add Object Access List
    ####

    @needscredentials
    def test_add_object_access_list_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.add_object_access_list(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
                accounts=[self.account_id],
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_add_object_access_list_returns_404_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.add_object_access_list(
                catalog_identifier=catalog_id,
                object_identifier='invalid-'+object_id,
                accounts=[self.account_id],
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_add_object_access_list(self):
        assert catalog_id is not None
        assert object_id is not None

        add_object_access_list_response = self.catalog_management_service_authorized.add_object_access_list(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
            accounts=[self.account_id],
        )

        assert add_object_access_list_response.get_status_code() == 201
        access_list_bulk_response = add_object_access_list_response.get_result()
        assert access_list_bulk_response is not None

    ####
    # Create Offering Instance
    ####

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_create_offering_instance_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None
        assert offering_id is not None

        # don't know what kind_format is needed here, vpe, helm and offering don't work

        try:
            self.catalog_management_service_authorized.create_offering_instance(
                x_auth_refresh_token=self.refresh_token_authorized,
                id=offering_id,
                catalog_id='invalid-'+catalog_id,
                offering_id=offering_id,
                kind_format=kind_vpe,
                version='0.0.2',
                cluster_id=self.cluster_id,
                cluster_region=region_us_south,
                cluster_all_namespaces=True,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_create_offering_instance_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        # don't know what kind_format is needed here, vpe, helm and offering don't work

        try:
            self.catalog_management_service_not_authorized.create_offering_instance(
                x_auth_refresh_token=self.refresh_token_authorized,
                id=offering_id,
                catalog_id=catalog_id,
                offering_id=offering_id,
                kind_format=kind_vpe,
                version='0.0.2',
                cluster_id=self.cluster_id,
                cluster_region=region_us_south,
                cluster_all_namespaces=True,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_create_offering_instance_returns_400_when_backend_input_validation_fails(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.create_offering_instance(
                x_auth_refresh_token=self.refresh_token_authorized,
                id=offering_id,
                catalog_id=catalog_id,
                offering_id=offering_id,
                kind_format='bogus kind',
                version='0.0.2',
                cluster_id=self.cluster_id,
                cluster_region=region_us_south,
                cluster_all_namespaces=True,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_create_offering_instance(self):
        global offering_instance_id

        assert catalog_id is not None
        assert offering_id is not None

        create_offering_instance_response = self.catalog_management_service_authorized.create_offering_instance(
            x_auth_refresh_token=self.refresh_token_authorized,
            id=offering_id,
            catalog_id=catalog_id,
            offering_id=offering_id,
            kind_format=kind_vpe,
            version='0.0.2',
            cluster_id=self.cluster_id,
            cluster_region=region_us_south,
            cluster_all_namespaces=True,
        )

        assert create_offering_instance_response.get_status_code() == 201
        offering_instance_id = create_offering_instance_response.get_result()
        assert offering_instance_id is not None
        assert offering_instance_id['id'] is not None
        offering_instance_id = offering_instance_id['id']

    ####
    # Get Offering Instance
    ####

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_offering_instance_returns_403_when_user_is_not_authorized(self):
        assert offering_instance_id is not None

        try:
            self.catalog_management_service_not_authorized.get_offering_instance(
                instance_identifier=offering_instance_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_offering_instance_returns_404_when_no_such_offering_instance(self):
        assert offering_instance_id is not None

        try:
            self.catalog_management_service_authorized.get_offering_instance(
                instance_identifier='invalid-'+offering_instance_id
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_get_offering_instance(self):
        assert offering_instance_id is not None

        get_offering_instance_response = self.catalog_management_service_authorized.get_offering_instance(
            instance_identifier=offering_instance_id,
        )

        assert get_offering_instance_response.get_status_code() == 200
        offering_instance = get_offering_instance_response.get_result()
        assert offering_instance is not None

    ####
    # Put Offering Instance
    ####

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_put_offering_instance_returns_403_when_user_is_not_authorized(self):
        assert offering_instance_id is not None
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_not_authorized.put_offering_instance(
                instance_identifier=offering_instance_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                id=offering_instance_id,
                catalog_id=catalog_id,
                offering_id=offering_id,
                kind_format=kind_vpe,
                version='0.0.3',
                cluster_id=self.cluster_id,
                cluster_region=region_us_south,
                cluster_all_namespaces=True,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_put_offering_instance_returns_404_when_no_such_catalog(self):
        assert offering_instance_id is not None
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.put_offering_instance(
                instance_identifier=offering_instance_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                id=offering_instance_id,
                catalog_id='invalid-'+catalog_id,
                offering_id=offering_id,
                kind_format=kind_vpe,
                version='0.0.3',
                cluster_id=self.cluster_id,
                cluster_region=region_us_south,
                cluster_all_namespaces=True,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_put_offering_instance_returns_400_when_backend_input_validation_fails(self):
        assert offering_instance_id is not None
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_authorized.put_offering_instance(
                instance_identifier=offering_instance_id,
                x_auth_refresh_token=self.refresh_token_authorized,
                id=offering_instance_id,
                catalog_id=catalog_id,
                offering_id=offering_id,
                kind_format='bogus kind',
                version='0.0.3',
                cluster_id=self.cluster_id,
                cluster_region=region_us_south,
                cluster_all_namespaces=True,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_put_offering_instance(self):
        assert offering_instance_id is not None
        assert catalog_id is not None
        assert offering_id is not None

        put_offering_instance_response = self.catalog_management_service_authorized.put_offering_instance(
            instance_identifier=offering_instance_id,
            x_auth_refresh_token=self.refresh_token_authorized,
            id=offering_instance_id,
            catalog_id=catalog_id,
            offering_id=offering_id,
            kind_format=kind_vpe,
            version='0.0.3',
            cluster_id=self.cluster_id,
            cluster_region=region_us_south,
            cluster_all_namespaces=True,
        )

        assert put_offering_instance_response.get_status_code() == 200
        offering_instance = put_offering_instance_response.get_result()
        assert offering_instance is not None

    ####
    # Delete Version
    ####

    @needscredentials
    def test_delete_version_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.delete_version(
                version_loc_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    def test_delete_version_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.delete_version(
                version_loc_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_delete_version_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.delete_version(
                version_loc_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_delete_version(self):
        assert version_locator_id is not None

        delete_version_response = self.catalog_management_service_authorized.delete_version(
            version_loc_id=version_locator_id,
        )

        assert delete_version_response.get_status_code() == 200

    ####
    # Delete Operators
    ####

    @needscredentials
    def test_delete_operators_returns_403_when_user_is_not_authorized(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_not_authorized.delete_operators(
                x_auth_refresh_token=self.refresh_token_not_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=version_locator_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_delete_operators_returns_404_when_no_such_version(self):
        assert version_locator_id is not None

        try:
            self.catalog_management_service_authorized.delete_operators(
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id='invalid-'+version_locator_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_delete_operators_returns_400_when_backend_input_validation_fails(self):

        try:
            self.catalog_management_service_authorized.delete_operators(
                x_auth_refresh_token=self.refresh_token_authorized,
                cluster_id=self.cluster_id,
                region=region_us_south,
                version_locator_id=bogus_version_locator_id,
            )
        except ApiException as e:
            assert e.code == 400

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_delete_operators(self):
        assert version_locator_id is not None

        # Error: Error loading version with id: fdeefb18-57aa-4390-a9e0-b66b551db803.
        # 2c187aa6-5009-4a2f-8f57-86533d2d3a18: Error[404 Not Found] -
        # Version not found: Catalog[fdeefb18-57aa-4390-a9e0-b66b551db803]:Version[2c187aa6-5009-4a2f-8f57-86533d2d3a18]

        delete_operators_response = self.catalog_management_service_authorized.delete_operators(
            x_auth_refresh_token=self.refresh_token_authorized,
            cluster_id=self.cluster_id,
            region=region_us_south,
            version_locator_id=version_locator_id,
        )

        assert delete_operators_response.get_status_code() == 200

    ####
    # Delete Offering Instance
    ####

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_delete_offering_instance_returns_403_when_user_is_not_authorized(self):
        assert offering_instance_id is not None

        try:
            self.catalog_management_service_not_authorized.delete_offering_instance(
                instance_identifier=offering_instance_id,
                x_auth_refresh_token=self.refresh_token_not_authorized,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_delete_offering_instance_returns_404_when_no_such_offering_instance(self):
        assert offering_instance_id is not None

        try:
            self.catalog_management_service_authorized.delete_offering_instance(
                instance_identifier='invalid-'+offering_instance_id,
                x_auth_refresh_token=self.refresh_token_authorized,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    @pytest.mark.skip(reason='Skipped by design')
    def test_delete_offering_instance(self):
        assert offering_instance_id is not None

        delete_offering_instance_response = self.catalog_management_service_authorized.delete_offering_instance(
            instance_identifier=offering_instance_id,
            x_auth_refresh_token=self.refresh_token_authorized,
        )

        assert delete_offering_instance_response.get_status_code() == 200

    ####
    # Delete Object Access List
    ####

    @needscredentials
    def test_delete_object_access_list_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.delete_object_access_list(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
                accounts=[self.account_id],
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_delete_object_access_list_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.delete_object_access_list(
                catalog_identifier='invalid-'+catalog_id,
                object_identifier=object_id,
                accounts=[self.account_id],
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_delete_object_access_list(self):
        assert catalog_id is not None
        assert object_id is not None

        delete_object_access_list_response = self.catalog_management_service_authorized.delete_object_access_list(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
            accounts=[self.account_id],
        )

        assert delete_object_access_list_response.get_status_code() == 200
        access_list_bulk_response = delete_object_access_list_response.get_result()
        assert access_list_bulk_response is not None

    ####
    # Delete Object Access
    ####

    @needscredentials
    def test_delete_object_access_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.delete_object_access(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
                account_identifier=self.account_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_delete_object_access_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_authorized.delete_object_access(
                catalog_identifier='invalid-'+catalog_id,
                object_identifier=object_id,
                account_identifier=self.account_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_delete_object_access(self):
        assert catalog_id is not None
        assert object_id is not None

        delete_object_access_response = self.catalog_management_service_authorized.delete_object_access(
            catalog_identifier=catalog_id,
            object_identifier=object_id,
            account_identifier=self.account_id,
        )

        assert delete_object_access_response.get_status_code() == 200

    ####
    # Delete Object
    ####

    @needscredentials
    def test_delete_object_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert object_id is not None

        try:
            self.catalog_management_service_not_authorized.delete_object(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_delete_object_returns_200_when_no_such_object(self):
        assert catalog_id is not None
        assert object_id is not None

        delete_object_response = self.catalog_management_service_authorized.delete_object(
            catalog_identifier=catalog_id,
            object_identifier='invalid-'+object_id,
        )

        assert delete_object_response.get_status_code() == 200

    @needscredentials
    def test_delete_object(self):
        assert catalog_id is not None
        assert object_id is not None

        for created_object_id in created_object_ids:
            delete_object_response = self.catalog_management_service_authorized.delete_object(
                catalog_identifier=catalog_id,
                object_identifier=created_object_id,
            )
            assert delete_object_response.get_status_code() == 200

    ####
    # Delete Offering
    ####

    @needscredentials
    def test_delete_offering_returns_200_when_no_such_offering(self):
        assert catalog_id is not None
        assert offering_id is not None

        delete_offering_response = self.catalog_management_service_authorized.delete_offering(
            catalog_identifier=catalog_id,
            offering_id='invalid-'+offering_id,
        )

        assert delete_offering_response.get_status_code() == 200

    @needscredentials
    def test_delete_offering_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None
        assert offering_id is not None

        try:
            self.catalog_management_service_not_authorized.delete_offering(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_delete_offering(self):
        assert catalog_id is not None
        assert offering_id is not None

        for i in created_offering_ids:
            delete_offering_response = self.catalog_management_service_authorized.delete_offering(
                catalog_identifier=catalog_id,
                offering_id=i,
            )
            assert delete_offering_response.get_status_code() == 200

    ####
    # Delete Catalog
    ####

    @needscredentials
    def test_delete_catalog_returns_404_when_no_such_catalog(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_authorized.delete_catalog(
                catalog_identifier='invalid-'+catalog_id,
            )
        except ApiException as e:
            assert e.code == 404

    @needscredentials
    def test_delete_catalog_returns_403_when_user_is_not_authorized(self):
        assert catalog_id is not None

        try:
            self.catalog_management_service_not_authorized.delete_catalog(
                catalog_identifier=catalog_id,
            )
        except ApiException as e:
            assert e.code == 403

    @needscredentials
    def test_delete_catalog(self):
        assert catalog_id is not None

        delete_catalog_response = self.catalog_management_service_authorized.delete_catalog(
            catalog_identifier=catalog_id,
        )

        assert delete_catalog_response.get_status_code() == 200

    @classmethod
    def teardown_class(cls):
        try:
            cls.catalog_management_service_authorized.delete_object(
                catalog_identifier=catalog_id,
                object_identifier=object_id,
            )
        except ApiException:
            print("Object is already deleted.")

        try:
            cls.catalog_management_service_authorized.delete_offering(
                catalog_identifier=catalog_id,
                offering_id=offering_id,
            )
        except ApiException:
            print("Offering is already deleted.")

        try:
            cls.catalog_management_service_authorized.delete_catalog(
                catalog_identifier=catalog_id,
            )
        except ApiException:
            print("Catalog is already deleted.")
