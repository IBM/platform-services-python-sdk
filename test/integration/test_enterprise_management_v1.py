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
Integration Tests for EnterpriseManagementV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_platform_services.enterprise_management_v1 import *

# Config file name
config_file = 'enterprise_management_v1.env'

class TestEnterpriseManagementV1():
    """
    Integration Test Class for EnterpriseManagementV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.enterprise_management_service = EnterpriseManagementV1.new_instance(
                )
            assert cls.enterprise_management_service is not None

            cls.config = read_external_sources(
                EnterpriseManagementV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_account_group(self):

        create_account_group_response = self.enterprise_management_service.create_account_group(
            parent='testString',
            name='testString',
            primary_contact_iam_id='testString'
        )

        assert create_account_group_response.get_status_code() == 201
        create_account_group_response = create_account_group_response.get_result()
        assert create_account_group_response is not None

    @needscredentials
    def test_list_account_groups(self):

        list_account_groups_response = self.enterprise_management_service.list_account_groups(
            enterprise_id='testString',
            parent_account_group_id='testString',
            next_docid='testString',
            parent='testString',
            limit=38
        )

        assert list_account_groups_response.get_status_code() == 200
        list_account_groups_response = list_account_groups_response.get_result()
        assert list_account_groups_response is not None

    @needscredentials
    def test_get_account_group(self):

        get_account_group_response = self.enterprise_management_service.get_account_group(
            account_group_id='testString'
        )

        assert get_account_group_response.get_status_code() == 200
        account_group = get_account_group_response.get_result()
        assert account_group is not None

    @needscredentials
    def test_update_account_group(self):

        update_account_group_response = self.enterprise_management_service.update_account_group(
            account_group_id='testString',
            name='testString',
            primary_contact_iam_id='testString'
        )

        assert update_account_group_response.get_status_code() == 204

    @needscredentials
    def test_import_account_to_enterprise(self):

        import_account_to_enterprise_response = self.enterprise_management_service.import_account_to_enterprise(
            enterprise_id='testString',
            account_id='testString',
            parent='testString',
            billing_unit_id='testString'
        )

        assert import_account_to_enterprise_response.get_status_code() == 202

    @needscredentials
    def test_create_account(self):

        create_account_response = self.enterprise_management_service.create_account(
            parent='testString',
            name='testString',
            owner_iam_id='testString'
        )

        assert create_account_response.get_status_code() == 201
        create_account_response = create_account_response.get_result()
        assert create_account_response is not None

    @needscredentials
    def test_list_accounts(self):

        list_accounts_response = self.enterprise_management_service.list_accounts(
            enterprise_id='testString',
            account_group_id='testString',
            next_docid='testString',
            parent='testString',
            limit=38
        )

        assert list_accounts_response.get_status_code() == 200
        list_accounts_response = list_accounts_response.get_result()
        assert list_accounts_response is not None

    @needscredentials
    def test_get_account(self):

        get_account_response = self.enterprise_management_service.get_account(
            account_id='testString'
        )

        assert get_account_response.get_status_code() == 200
        account = get_account_response.get_result()
        assert account is not None

    @needscredentials
    def test_update_account(self):

        update_account_response = self.enterprise_management_service.update_account(
            account_id='testString',
            parent='testString'
        )

        assert update_account_response.get_status_code() == 204

    @needscredentials
    def test_create_enterprise(self):

        create_enterprise_response = self.enterprise_management_service.create_enterprise(
            source_account_id='testString',
            name='testString',
            primary_contact_iam_id='testString',
            domain='testString'
        )

        assert create_enterprise_response.get_status_code() == 202
        create_enterprise_response = create_enterprise_response.get_result()
        assert create_enterprise_response is not None

    @needscredentials
    def test_list_enterprises(self):

        list_enterprises_response = self.enterprise_management_service.list_enterprises(
            enterprise_account_id='testString',
            account_group_id='testString',
            account_id='testString',
            next_docid='testString',
            limit=38
        )

        assert list_enterprises_response.get_status_code() == 200
        list_enterprises_response = list_enterprises_response.get_result()
        assert list_enterprises_response is not None

    @needscredentials
    def test_get_enterprise(self):

        get_enterprise_response = self.enterprise_management_service.get_enterprise(
            enterprise_id='testString'
        )

        assert get_enterprise_response.get_status_code() == 200
        enterprise = get_enterprise_response.get_result()
        assert enterprise is not None

    @needscredentials
    def test_update_enterprise(self):

        update_enterprise_response = self.enterprise_management_service.update_enterprise(
            enterprise_id='testString',
            name='testString',
            domain='testString',
            primary_contact_iam_id='testString'
        )

        assert update_enterprise_response.get_status_code() == 204

