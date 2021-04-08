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
config_file = 'enterprise_management.env'

first_example_account_group_name = 'Example Account Group'
first_updated_example_account_group_name = 'Updated Example Account Group'
second_example_account_group_name = 'Second Example Account Group'
example_account_name = 'Example Account Name'
updated_enterprise_name = 'Updated Enterprise Name'
result_per_page = 1

example_account_id = None
first_example_account_group_id = None
second_example_account_group_id = None

class TestEnterpriseManagementV1():
    """
    Integration Test Class for EnterpriseManagementV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.enterprise_management_service = EnterpriseManagementV1.new_instance()
            assert cls.enterprise_management_service is not None

            cls.config = read_external_sources(
                EnterpriseManagementV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.enterprise_id = cls.config['ENTERPRISE_ID']
            cls.account_id = cls.config['ACCOUNT_ID']
            cls.account_iam_id = cls.config['ACCOUNT_IAM_ID']

            assert cls.enterprise_id is not None
            assert cls.account_id is not None
            assert cls.account_iam_id is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_account_group(self):
        global first_example_account_group_id, second_example_account_group_id

        parent = 'crn:v1:bluemix:public:enterprise::a/' + self.account_id + '::enterprise:' + self.enterprise_id

        create_first_example_account_group_response = self.enterprise_management_service.create_account_group(
            parent=parent,
            name=first_example_account_group_name,
            primary_contact_iam_id=self.account_iam_id,
        )

        assert create_first_example_account_group_response.get_status_code() == 201
        create_first_example_account_group_response = create_first_example_account_group_response.get_result()
        assert create_first_example_account_group_response is not None

        first_example_account_group_id = create_first_example_account_group_response.get('account_group_id')

        create_second_example_account_group_response = self.enterprise_management_service.create_account_group(
            parent=parent,
            name=second_example_account_group_name,
            primary_contact_iam_id=self.account_iam_id,
        )

        assert create_second_example_account_group_response.get_status_code() == 201
        create_second_example_account_group_response = create_second_example_account_group_response.get_result()
        assert create_second_example_account_group_response is not None

        second_example_account_group_id = create_second_example_account_group_response.get('account_group_id')

    @needscredentials
    def test_list_account_groups(self):

        list_account_groups_response = self.enterprise_management_service.list_account_groups(
            enterprise_id=self.enterprise_id,
        )

        assert list_account_groups_response.get_status_code() == 200
        list_account_groups_response = list_account_groups_response.get_result()
        assert list_account_groups_response is not None

    @needscredentials
    def test_list_account_groups_with_pagination(self):

        results_count = 0
        doc_id = None

        while True:
            list_account_groups_response = self.enterprise_management_service.list_account_groups(
                enterprise_id=self.enterprise_id,
                limit=result_per_page,
                next_docid=doc_id,
            )

            assert list_account_groups_response.get_status_code() == 200
            list_account_groups_response = list_account_groups_response.get_result()
            assert list_account_groups_response is not None

            results_count += 1

            next_url = list_account_groups_response.get('next_url')
            if next_url is None:
                break

            doc_id = get_query_param(next_url, 'next_docid')

        print(f'\nlist_account_groups() returned a total of {results_count} account groups.')

    @needscredentials
    def test_get_account_group(self):
        assert first_example_account_group_id is not None

        get_account_group_response = self.enterprise_management_service.get_account_group(
            account_group_id=first_example_account_group_id,
        )

        assert get_account_group_response.get_status_code() == 200
        account_group = get_account_group_response.get_result()
        assert account_group is not None

    @needscredentials
    def test_update_account_group(self):
        assert first_example_account_group_id is not None

        update_account_group_response = self.enterprise_management_service.update_account_group(
            account_group_id=first_example_account_group_id,
            name=first_example_account_group_name,
            primary_contact_iam_id=self.account_iam_id,
        )

        assert update_account_group_response.get_status_code() == 204

    @needscredentials
    def test_create_account(self):
        global example_account_id

        assert first_example_account_group_id is not None

        parent = 'crn:v1:bluemix:public:enterprise::a/' + self.account_id + '::account-group:' + first_example_account_group_id

        create_account_response = self.enterprise_management_service.create_account(
            parent=parent,
            name=example_account_name,
            owner_iam_id=self.account_iam_id,
        )

        assert create_account_response.get_status_code() == 202
        create_account_response = create_account_response.get_result()
        assert create_account_response is not None

        example_account_id = create_account_response.get('account_id')

    @needscredentials
    def test_list_accounts(self):

        list_accounts_response = self.enterprise_management_service.list_accounts(
            enterprise_id=self.enterprise_id,
        )

        assert list_accounts_response.get_status_code() == 200
        list_accounts_response = list_accounts_response.get_result()
        assert list_accounts_response is not None

    @needscredentials
    def test_list_accounts_with_pagination(self):

        results_count = 0
        doc_id = None

        while True:
            list_accounts_response = self.enterprise_management_service.list_accounts(
                enterprise_id=self.enterprise_id,
                limit=result_per_page,
                next_docid=doc_id,
            )

            assert list_accounts_response.get_status_code() == 200
            list_accounts_response = list_accounts_response.get_result()
            assert list_accounts_response is not None

            results_count += 1

            next_url = list_accounts_response.get('next_url')
            if next_url is None:
                break

            doc_id = get_query_param(next_url, 'next_docid')

        print(f'\nlist_accounts() returned a total of {results_count} accounts.')

    @needscredentials
    def test_get_account(self):
        assert example_account_id is not None

        get_account_response = self.enterprise_management_service.get_account(
            account_id=example_account_id,
        )

        assert get_account_response.get_status_code() == 200
        account = get_account_response.get_result()
        assert account is not None

    @needscredentials
    def test_update_account(self):
        assert example_account_id is not None
        assert second_example_account_group_id is not None

        new_parent = 'crn:v1:bluemix:public:enterprise::a/' + self.account_id + '::account-group:' + second_example_account_group_id

        update_account_response = self.enterprise_management_service.update_account(
            account_id=example_account_id,
            parent=new_parent,
        )

        assert update_account_response.get_status_code() == 202

    @needscredentials
    def test_list_enterprises(self):

        list_enterprises_response = self.enterprise_management_service.list_enterprises(
            account_id=self.account_id,
        )

        assert list_enterprises_response.get_status_code() == 200
        list_enterprises_response = list_enterprises_response.get_result()
        assert list_enterprises_response is not None

    @needscredentials
    def test_get_enterprise(self):

        get_enterprise_response = self.enterprise_management_service.get_enterprise(
            enterprise_id=self.enterprise_id,
        )

        assert get_enterprise_response.get_status_code() == 200
        enterprise = get_enterprise_response.get_result()
        assert enterprise is not None

    @needscredentials
    def test_update_enterprise(self):

        update_enterprise_response = self.enterprise_management_service.update_enterprise(
            enterprise_id=self.enterprise_id,
            name=updated_enterprise_name,
            primary_contact_iam_id=self.account_iam_id,
        )

        assert update_enterprise_response.get_status_code() == 204

