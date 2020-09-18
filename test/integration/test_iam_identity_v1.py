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

"""
Integration Tests for IamIdentityV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_platform_services.iam_identity_v1 import *

# Config file name
config_file = 'iam_identity.env'

class TestIamIdentityV1():
    """
    Integration Test Class for IamIdentityV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.iam_identity_service = IamIdentityV1.new_instance(
                )
            assert cls.iam_identity_service is not None

            cls.config = read_external_sources(
                IamIdentityV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_api_keys(self):

        list_api_keys_response = self.iam_identity_service.list_api_keys(
            account_id='testString',
            iam_id='testString',
            pagesize=38,
            pagetoken='testString',
            scope='entity',
            type='user',
            sort='testString',
            order='asc',
            include_history=True
        )

        assert list_api_keys_response.get_status_code() == 200
        api_key_list = list_api_keys_response.get_result()
        assert api_key_list is not None

    @needscredentials
    def test_create_api_key(self):

        create_api_key_response = self.iam_identity_service.create_api_key(
            name='testString',
            iam_id='testString',
            description='testString',
            account_id='testString',
            apikey='testString',
            store_value=True,
            entity_lock='testString'
        )

        assert create_api_key_response.get_status_code() == 201
        api_key = create_api_key_response.get_result()
        assert api_key is not None

    @needscredentials
    def test_get_api_keys_details(self):

        get_api_keys_details_response = self.iam_identity_service.get_api_keys_details(
            iam_api_key='testString',
            include_history=True
        )

        assert get_api_keys_details_response.get_status_code() == 200
        api_key = get_api_keys_details_response.get_result()
        assert api_key is not None

    @needscredentials
    def test_get_api_key(self):

        get_api_key_response = self.iam_identity_service.get_api_key(
            id='testString',
            include_history=True
        )

        assert get_api_key_response.get_status_code() == 200
        api_key = get_api_key_response.get_result()
        assert api_key is not None

    @needscredentials
    def test_update_api_key(self):

        update_api_key_response = self.iam_identity_service.update_api_key(
            id='testString',
            if_match='testString',
            name='testString',
            description='testString'
        )

        assert update_api_key_response.get_status_code() == 200
        api_key = update_api_key_response.get_result()
        assert api_key is not None

    @needscredentials
    def test_lock_api_key(self):

        lock_api_key_response = self.iam_identity_service.lock_api_key(
            id='testString'
        )

        assert lock_api_key_response.get_status_code() == 200

    @needscredentials
    def test_list_service_ids(self):

        list_service_ids_response = self.iam_identity_service.list_service_ids(
            account_id='testString',
            name='testString',
            pagesize=38,
            pagetoken='testString',
            sort='testString',
            order='asc',
            include_history=True
        )

        assert list_service_ids_response.get_status_code() == 200
        service_id_list = list_service_ids_response.get_result()
        assert service_id_list is not None

    @needscredentials
    def test_create_service_id(self):

        # Construct a dict representation of a CreateApiKeyRequest model
        create_api_key_request_model = {
            'name': 'testString',
            'description': 'testString',
            'iam_id': 'testString',
            'account_id': 'testString',
            'apikey': 'testString',
            'store_value': True
        }

        create_service_id_response = self.iam_identity_service.create_service_id(
            account_id='testString',
            name='testString',
            description='testString',
            unique_instance_crns=['testString'],
            apikey=create_api_key_request_model,
            entity_lock='testString'
        )

        assert create_service_id_response.get_status_code() == 201
        service_id = create_service_id_response.get_result()
        assert service_id is not None

    @needscredentials
    def test_get_service_id(self):

        get_service_id_response = self.iam_identity_service.get_service_id(
            id='testString',
            include_history=True
        )

        assert get_service_id_response.get_status_code() == 200
        service_id = get_service_id_response.get_result()
        assert service_id is not None

    @needscredentials
    def test_update_service_id(self):

        update_service_id_response = self.iam_identity_service.update_service_id(
            id='testString',
            if_match='testString',
            name='testString',
            description='testString',
            unique_instance_crns=['testString']
        )

        assert update_service_id_response.get_status_code() == 200
        service_id = update_service_id_response.get_result()
        assert service_id is not None

    @needscredentials
    def test_lock_service_id(self):

        lock_service_id_response = self.iam_identity_service.lock_service_id(
            id='testString'
        )

        assert lock_service_id_response.get_status_code() == 200
        service_id = lock_service_id_response.get_result()
        assert service_id is not None

    @needscredentials
    def test_unlock_service_id(self):

        unlock_service_id_response = self.iam_identity_service.unlock_service_id(
            id='testString'
        )

        assert unlock_service_id_response.get_status_code() == 200
        service_id = unlock_service_id_response.get_result()
        assert service_id is not None

    @needscredentials
    def test_unlock_api_key(self):

        unlock_api_key_response = self.iam_identity_service.unlock_api_key(
            id='testString'
        )

        assert unlock_api_key_response.get_status_code() == 200

    @needscredentials
    def test_delete_service_id(self):

        delete_service_id_response = self.iam_identity_service.delete_service_id(
            id='testString'
        )

        assert delete_service_id_response.get_status_code() == 204

    @needscredentials
    def test_delete_api_key(self):

        delete_api_key_response = self.iam_identity_service.delete_api_key(
            id='testString'
        )

        assert delete_api_key_response.get_status_code() == 204

