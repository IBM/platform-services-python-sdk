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
Examples for IamIdentityV1
"""

import json
import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.iam_identity_v1 import *

#
# This file provides an example of how to use the IAM Identity service.
#
# The following configuration properties are assumed to be defined:
#
# IAM_IDENTITY_URL=<service url>
# IAM_IDENTITY_AUTHTYPE=iam
# IAM_IDENTITY_AUTH_URL=<IAM Token Service url>
# IAM_IDENTITY_APIKEY=<IAM APIKEY for the User>
# IAM_IDENTITY_ACCOUNT_ID=<AccountID which is unique to the User>
# IAM_IDENTITY_IAM_ID=<IAM ID which is unique to the User account>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'iam_identity.env'

iam_identity_service = None

config = None

apikey_name = 'Example-ApiKey'
serviceid_name = 'Example-ServiceId'

account_id = None
iam_id = None
apikey = None

apikey_id = None
apikey_etag = None
svc_id = None
svc_id_etag = None


##############################################################################
# Start of Examples for Service: IamIdentityV1
##############################################################################
# region
class TestIamIdentityV1Examples():
    """
    Example Test Class for IamIdentityV1
    """

    @classmethod
    def setup_class(cls):
        global iam_identity_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            iam_identity_service = IamIdentityV1.new_instance()

            # end-common
            assert iam_identity_service is not None

            # Load the configuration
            global config
            config = read_external_sources(IamIdentityV1.DEFAULT_SERVICE_NAME)

            global account_id
            account_id = config['ACCOUNT_ID']

            global iam_id
            iam_id = config['IAM_ID']

            global apikey
            apikey = config['APIKEY']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_api_key_example(self):
        """
        create_api_key request example
        """
        try:
            global apikey_name, iam_id, apikey_id

            # begin-create_api_key

            api_key = iam_identity_service.create_api_key(
                name=apikey_name,
                iam_id=iam_id
            ).get_result()

            apikey_id = api_key['id']

            print(json.dumps(api_key, indent=2))

            # end-create_api_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_api_keys_example(self):
        """
        list_api_keys request example
        """
        try:
            global account_id, iam_id

            # begin-list_api_keys

            api_key_list = iam_identity_service.list_api_keys(
                account_id=account_id,
                iam_id=iam_id,
                include_history=True
            ).get_result()

            print(json.dumps(api_key_list, indent=2))

            # end-list_api_keys

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_api_keys_details_example(self):
        """
        get_api_keys_details request example
        """
        try:
            global apikey

            # begin-get_api_keys_details

            api_key = iam_identity_service.get_api_keys_details(
                iam_api_key=apikey
            ).get_result()

            print(json.dumps(api_key, indent=2))

            # end-get_api_keys_details

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_api_key_example(self):
        """
        get_api_key request example
        """
        try:
            global apikey_id, apikey_etag
            # begin-get_api_key

            response = iam_identity_service.get_api_key(
                id=apikey_id
            )

            apikey_etag = response.get_headers()['Etag']
            api_key = response.get_result()

            print(json.dumps(api_key, indent=2))

            # end-get_api_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_api_key_example(self):
        """
        update_api_key request example
        """
        try:
            global apikey_id, apikey_etag
            # begin-update_api_key

            api_key = iam_identity_service.update_api_key(
                id=apikey_id,
                if_match=apikey_etag,
                description='This is an updated description'
            ).get_result()

            print(json.dumps(api_key, indent=2))

            # end-update_api_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_lock_api_key_example(self):
        """
        lock_api_key request example
        """
        try:
            global apikey_id
            # begin-lock_api_key

            response = iam_identity_service.lock_api_key(id=apikey_id)

            print(response)

            # end-lock_api_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_unlock_api_key_example(self):
        """
        unlock_api_key request example
        """
        try:
            global apikey_id
            # begin-unlock_api_key

            response = iam_identity_service.unlock_api_key(id=apikey_id)

            print(response)

            # end-unlock_api_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_api_key_example(self):
        """
        delete_api_key request example
        """
        try:
            global apikey_id

            # begin-delete_api_key

            response = iam_identity_service.delete_api_key(id=apikey_id)

            print(response)

            # end-delete_api_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_service_id_example(self):
        """
        create_service_id request example
        """
        try:
            global account_id, serviceid_name, svc_id
            # begin-create_service_id

            service_id = iam_identity_service.create_service_id(
                account_id=account_id,
                name=serviceid_name,
                description='Example ServiceId'
            ).get_result()

            svc_id = service_id['id']

            print(json.dumps(service_id, indent=2))

            # end-create_service_id
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_service_id_example(self):
        """
        get_service_id request example
        """
        try:
            global svc_id, svc_id_etag
            # begin-get_service_id

            response = iam_identity_service.get_service_id(
                id=svc_id
            )

            svc_id_etag = response.get_headers()['Etag']
            service_id = response.get_result()

            print(json.dumps(service_id, indent=2))

            # end-get_service_id

            serviceIDEtag = service_id['entity_tag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_service_ids_example(self):
        """
        list_service_ids request example
        """
        try:
            global account_id, serviceid_name
            # begin-list_service_ids

            service_id_list = iam_identity_service.list_service_ids(
                account_id=account_id,
                name=serviceid_name
            ).get_result()

            print(json.dumps(service_id_list, indent=2))

            # end-list_service_ids

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_service_id_example(self):
        """
        update_service_id request example
        """
        try:
            global svc_id, svc_id_etag
            # begin-update_service_id

            service_id = iam_identity_service.update_service_id(
                id=svc_id,
                if_match=svc_id_etag,
                description='This is an updated description'
            ).get_result()

            print(json.dumps(service_id, indent=2))

            # end-update_service_id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_lock_service_id_example(self):
        """
        lock_service_id request example
        """
        try:
            global svc_id
            # begin-lock_service_id

            response = iam_identity_service.lock_service_id(id=svc_id)

            print(response)

            # end-lock_service_id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_unlock_service_id_example(self):
        """
        unlock_service_id request example
        """
        try:
            global svc_id

            # begin-unlock_service_id

            response = iam_identity_service.unlock_service_id(id=svc_id)

            print(response)

            # end-unlock_service_id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_service_id_example(self):
        """
        delete_service_id request example
        """
        try:
            global svc_id

            # begin-delete_service_id

            response = iam_identity_service.delete_service_id(id=svc_id)

            print(response)

            # end-delete_service_id

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: IamIdentityV1
##############################################################################
