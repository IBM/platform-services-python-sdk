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
Examples for EnterpriseManagementV1
"""

from abc import abstractclassmethod
from inspect import isframe
import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.enterprise_management_v1 import *

#
# This file provides an example of how to use the Enterprise Management service.
#
# The following configuration properties are assumed to be defined:
# ENTERPRISE_MANAGEMENT_URL=<service base url>
# ENTERPRISE_MANAGEMENT_AUTH_TYPE=iam
# ENTERPRISE_MANAGEMENT_APIKEY=<IAM apikey>
# ENTERPRISE_MANAGEMENT_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
# ENTERPRISE_MANAGEMENT_ENTERPRISE_ID=<ID of the enterprise>
# ENTERPRISE_MANAGEMENT_ACCOUNT_ID=<enterprise account ID>
# ENTERPRISE_MANAGEMENT_ACCOUNT_IAM_ID=<IAM ID of the enterprise account>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'enterprise_management.env'

enterprise_management_service = None

config = None

enterprise_id = None
enterprise_account_id = None
enterprise_account_iam_id = None

account_id = None
account_group_id = None
new_parent_account_group_id = None


##############################################################################
# Start of Examples for Service: EnterpriseManagementV1
##############################################################################
# region
class TestEnterpriseManagementV1Examples():
    """
    Example Test Class for EnterpriseManagementV1
    """

    @classmethod
    def setup_class(cls):
        global enterprise_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            enterprise_management_service = EnterpriseManagementV1.new_instance()

            # end-common
            assert enterprise_management_service is not None

            # Load the configuration
            global config
            config = read_external_sources(EnterpriseManagementV1.DEFAULT_SERVICE_NAME)

            global enterprise_id
            enterprise_id = config['ENTERPRISE_ID']

            global enterprise_account_id
            enterprise_account_id = config['ACCOUNT_ID']

            global enterprise_account_iam_id
            enterprise_account_iam_id = config['ACCOUNT_IAM_ID']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_account_group_example(self):
        """
        create_account_group request example
        """
        assert enterprise_id is not None
        assert enterprise_account_id is not None
        assert enterprise_account_iam_id is not None

        print('\ncreate_account_group() result:')

        try:
            parent_crn = 'crn:v1:bluemix:public:enterprise::a/' + enterprise_account_id + '::enterprise:' + enterprise_id

            # begin-create_account_group

            create_account_group_response = enterprise_management_service.create_account_group(
                parent=parent_crn,
                name='Example Account Group',
                primary_contact_iam_id=enterprise_account_iam_id,
            ).get_result()

            print(json.dumps(create_account_group_response, indent=2))

            # end-create_account_group

            global account_group_id
            account_group_id = create_account_group_response.get('account_group_id')

            create_parent_account_group_response = enterprise_management_service.create_account_group(
                parent=parent_crn,
                name='New Parent Account Group',
                primary_contact_iam_id=enterprise_account_iam_id,
            )

            global new_parent_account_group_id
            new_parent_account_group_id = create_parent_account_group_response.get('account_group_id')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_account_groups_example(self):
        """
        list_account_groups request example
        """
        assert enterprise_id is not None

        print('\nlist_account_groups() result:')

        try:
            # begin-list_account_groups

            list_account_groups_response = enterprise_management_service.list_account_groups(
                enterprise_id=enterprise_id,
            ).get_result()

            print(json.dumps(list_account_groups_response, indent=2))

            # end-list_account_groups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_account_group_example(self):
        """
        get_account_group request example
        """
        assert account_group_id is not None

        print('\nget_account_group() result:')

        try:
            # begin-get_account_group

            account_group = enterprise_management_service.get_account_group(
                account_group_id=account_group_id,
            ).get_result()

            print(json.dumps(account_group, indent=2))

            # end-get_account_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_account_group_example(self):
        """
        update_account_group request example
        """
        assert account_group_id is not None

        print('\nupdate_account_group() result:')

        try:
            # begin-update_account_group

            response = enterprise_management_service.update_account_group(
                account_group_id=account_group_id,
                name='Updated Account Group',
                primary_contact_iam_id=enterprise_account_iam_id,
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_account_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_account_example(self):
        """
        create_account request example
        """
        assert account_group_id is not None

        print('\ncreate_account() result:')

        try:
            parent_crn = 'crn:v1:bluemix:public:enterprise::a/' + enterprise_account_id + '::account-group:' + account_group_id

            # begin-create_account

            create_account_response = enterprise_management_service.create_account(
                parent=parent_crn,
                name='Example Account',
                owner_iam_id=enterprise_account_iam_id,
            ).get_result()

            print(json.dumps(create_account_response, indent=2))

            # end-create_account

            global account_id
            account_id = create_account_response.get('account_id')

        except ApiException as e:
            pytest.fail(str(e))

    @pytest.mark.skip(reason='Skip by design.')
    @needscredentials
    def test_import_account_to_enterprise_example(self):
        """
        import_account_to_enterprise request example
        """
        print('\nimport_account_to_enterprise() result:')

        try:
            account_id = 'standalone_account_id'

            # begin-import_account_to_enterprise

            response = enterprise_management_service.import_account_to_enterprise(
                enterprise_id=enterprise_id,
                account_id=account_id,
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-import_account_to_enterprise

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_accounts_example(self):
        """
        list_accounts request example
        """
        assert enterprise_id is not None

        print('\nlist_accounts() result:')

        try:
            # begin-list_accounts

            list_accounts_response = enterprise_management_service.list_accounts(
                enterprise_id=enterprise_id,
            ).get_result()

            print(json.dumps(list_accounts_response, indent=2))

            # end-list_accounts

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_account_example(self):
        """
        get_account request example
        """
        assert account_id is not None

        print('\nget_account() result:')

        try:
            # begin-get_account

            account = enterprise_management_service.get_account(
                account_id=account_id,
            ).get_result()

            print(json.dumps(account, indent=2))

            # end-get_account

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_account_example(self):
        """
        update_account request example
        """
        assert account_id is not None
        assert new_parent_account_group_id is not None

        print('\nupdate_account() result:')

        try:
            new_parent_crn = 'crn:v1:bluemix:public:enterprise::a/' + enterprise_account_id + '::account-group:' + new_parent_account_group_id

            # begin-update_account

            response = enterprise_management_service.update_account(
                account_id=account_id,
                parent=new_parent_crn,
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_account

        except ApiException as e:
            pytest.fail(str(e))

    @pytest.mark.skip(reason='Skip by design.')
    @needscredentials
    def test_create_enterprise_example(self):
        """
        create_enterprise request example
        """

        print('\ncreate_enterprise() result:')

        try:
            account_id = 'standalone_account_id'
            contact_iam_id = 'standalone_account_iam_id'

            # begin-create_enterprise

            create_enterprise_response = enterprise_management_service.create_enterprise(
                source_account_id=account_id,
                name='Example Enterprise',
                primary_contact_iam_id=contact_iam_id,
            ).get_result()

            print(json.dumps(create_enterprise_response, indent=2))

            # end-create_enterprise

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_enterprises_example(self):
        """
        list_enterprises request example
        """
        assert enterprise_account_id is not None

        print('\nlist_enterprises() result:')

        try:
            # begin-list_enterprises

            list_enterprises_response = enterprise_management_service.list_enterprises(
                account_id=enterprise_account_id,
            ).get_result()

            print(json.dumps(list_enterprises_response, indent=2))

            # end-list_enterprises

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_enterprise_example(self):
        """
        get_enterprise request example
        """
        assert enterprise_id is not None

        print('\nget_enterprise() result:')

        try:
            # begin-get_enterprise

            enterprise = enterprise_management_service.get_enterprise(
                enterprise_id=enterprise_id
            ).get_result()

            print(json.dumps(enterprise, indent=2))

            # end-get_enterprise

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_enterprise_example(self):
        """
        update_enterprise request example
        """
        assert enterprise_id is not None
        assert enterprise_account_iam_id is not None

        print('\nupdate_enterprise() result:')

        try:
            # begin-update_enterprise

            response = enterprise_management_service.update_enterprise(
                enterprise_id=enterprise_id,
                name='Updated Example Enterprise',
                primary_contact_iam_id=enterprise_account_iam_id,
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_enterprise

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: EnterpriseManagementV1
##############################################################################
