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

profile_id = None
profile_etag = None

claimRule_id = None
claimRule_etag = None

link_id = None

account_settings_etag = None


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

            print('\ncreate_api_key() result:')
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

            print('\nlist_api_keys() result:')
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

            print('\nget_api_keys_details() result:')
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

            print('\nget_api_key() result:')
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

            print('\nupdate_api_key() result:')
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

            # end-lock_api_key
            print('\nlock_api_key() response status code: ', response.get_status_code())

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

            # end-unlock_api_key
            print('\nunlock_api_key() response status code: ', response.get_status_code())


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

            # end-delete_api_key
            print('\ndelete_api_key() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_service_id_example(self):
        """
        create_service_id request example
        """
        try:
            global account_id, serviceid_name, svc_id

            print('\ncreate_service_id() result:')
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

            print('\nget_service_id() result:')
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

            print('\nlist_service_ids() result:')
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

            print('\nupdate_service_id() result:')
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

            # end-lock_service_id
            print('\nlock_service_id() response status code: ', response.get_status_code())

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

            # end-unlock_service_id
            print('\nunlock_service_id() response status code: ', response.get_status_code())

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

            # end-delete_service_id
            print('\ndelete_service_id() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_create_profile_example(self):
        """
        create_profile request example
        """
        try:
            global profile_id
            print('\ncreate_profile() result:')
            # begin-create_profile

            profile = iam_identity_service.create_profile(
                name="example profile",
                description="example profile",
                account_id=account_id
            ).get_result()

            profile_id = profile['id']

            print(json.dumps(profile, indent=2))

            # end-create_profile

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_get_profile_example(self):
        """
        get_profile request example
        """
        try:
            global profile_id, profile_etag

            print('\nget_profile() result:')
            # begin-get_profile

            response = iam_identity_service.get_profile(
                profile_id=profile_id
            )

            profile_etag = response.get_headers()['Etag']
            profile = response.get_result()

            print(json.dumps(profile, indent=2))

            # end-get_profile

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_list_profile_example(self):
        """
        list_profiles request example
        """
        try:
            global account_id

            print('\nlist_profiles() result:')
            # begin-list_profiles

            profile_list = iam_identity_service.list_profile(
                account_id=account_id,
                include_history=True
            ).get_result()

            print(json.dumps(profile_list, indent=2))

            # end-list_profiles

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_update_profile_example(self):
        """
        update_profile request example
        """
        try:
            global profile_id, profile_etag

            print('\nupdate_profile() result:')
            # begin-update_profile

            profile = iam_identity_service.update_profile(
                profile_id=profile_id,
                if_match=profile_etag,
                description='This is an updated description'
            ).get_result()

            print(json.dumps(profile, indent=2))

            # end-update_profile

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_create_claim_rule_example(self):
        """
        create_claim_rule request example
        """
        try:
            global claimRule_id, profile_id
            print('\ncreate_claim_rule() result:')
            # begin-create_claim_rule

            profile_claim_rule_conditions_model = {}
            profile_claim_rule_conditions_model['claim'] = 'blueGroups'
            profile_claim_rule_conditions_model['operator'] = 'EQUALS'
            profile_claim_rule_conditions_model['value'] = '\"cloud-docs-dev\"'

            claimRule = iam_identity_service.create_claim_rule(
                profile_id = profile_id,
                type = 'Profile-SAML',
                realm_name = 'https://w3id.sso.ibm.com/auth/sps/samlidp2/saml20',
                expiration = 43200,
                conditions = [profile_claim_rule_conditions_model]
           ).get_result()

            claimRule_id = claimRule['id']

            print(json.dumps(claimRule, indent=2))

            # end-create_claim_rule

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_get_claim_rule_example(self):
        """
        get_claim_rule request example
        """
        try:
            global profile_id, claimRule_id, claimRule_etag

            print('\nget_claim_rule() result:')
            # begin-get_claim_rule

            response = iam_identity_service.get_claim_rule(
                profile_id= profile_id,
                rule_id= claimRule_id
            )

            claimRule_etag = response.get_headers()['Etag']
            claimRule = response.get_result()

            print(json.dumps(claimRule, indent=2))

            # end-get_claim_rule

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_list_claim_rules_example(self):
        """
        list_claim_rules request example
        """
        try:
            global profile_id

            print('\nlist_claim_rules() result:')
            # begin-list_claim_rules

            claimRule_list = iam_identity_service.list_claim_rules(
                profile_id=profile_id,
            ).get_result()

            print(json.dumps(claimRule_list, indent=2))

            # end-list_claim_rules

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_claim_rule_example(self):
        """
        update_claim_rule request example
        """
        try:
            global claimRule_id, claimRule_etag, profile_id

            print('\nupdate_claim_rule() result:')
            # begin-update_claim_rule

            profile_claim_rule_conditions_model = {}
            profile_claim_rule_conditions_model['claim'] = 'blueGroups'
            profile_claim_rule_conditions_model['operator'] = 'EQUALS'
            profile_claim_rule_conditions_model['value'] = '\"Europe_Group\"'

            claimRule = iam_identity_service.update_claim_rule(
                profile_id = profile_id,
                rule_id = claimRule_id,
                if_match = claimRule_etag,
                expiration = 33200,
                conditions = [profile_claim_rule_conditions_model],
                type = 'Profile-SAML',
                realm_name = 'https://w3id.sso.ibm.com/auth/sps/samlidp2/saml20',
            ).get_result()

            print(json.dumps(claimRule, indent=2))

            # end-update_claim_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_claim_rule_example(self):
        """
        delete_claim_rule request example
        """
        try:
            global profile_id, claimRule_id

            # begin-delete_claim_rule

            response = iam_identity_service.delete_claim_rule(profile_id=profile_id, rule_id=claimRule_id)

            # end-delete_claim_rule
            print('\ndelete_claimRule() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_create_link_example(self):
        """
        create_link request example
        """
        try:
            global profile_id, link_id
            print('\ncreate_link() result:')
            # begin-create_link

            CreateProfileLinkRequestLink = {}
            CreateProfileLinkRequestLink['crn'] = 'crn:v1:staging:public:iam-identity::a/18e3020749ce4744b0b472466d61fdb4::computeresource:Fake-Compute-Resource'
            CreateProfileLinkRequestLink['namespace'] = 'default'
            CreateProfileLinkRequestLink['name'] = 'nice name'

            link = iam_identity_service.create_link(
                profile_id = profile_id,
                name = 'nice link',
                cr_type = 'ROKS_SA',
                link = CreateProfileLinkRequestLink
            ).get_result()

            link_id = link['id']

            print(json.dumps(link, indent=2))

            # end-create_link

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_get_link_example(self):
        """
        get_link request example
        """
        try:
            global profile_id, link_id

            print('\nget_link() result:')
            # begin-get_link

            response = iam_identity_service.get_link(
                profile_id= profile_id,
                link_id= link_id
            )

            link = response.get_result()

            print(json.dumps(link, indent=2))

            # end-get_link

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_list_link_example(self):
        """
        list_links request example
        """
        try:
            global profile_id

            print('\nlist_links() result:')
            # begin-list_links

            link_list = iam_identity_service.list_link(
                profile_id=profile_id,
            ).get_result()

            print(json.dumps(link_list, indent=2))

            # end-list_links

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_delete_link_example(self):
        """
        delete_link request example
        """
        try:
            global profile_id, link_id

            # begin-delete_link

            response = iam_identity_service.delete_link(profile_id=profile_id, link_id=link_id)

            # end-delete_link
            print('\ndelete_link() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_delete_profile_example(self):
        """
        delete_profile request example
        """
        try:
            global profile_id

            # begin-delete_profile

            response = iam_identity_service.delete_profile(profile_id=profile_id)

            # end-delete_profile
            print('\ndelete_profile() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_account_settings_example(self):
        """
        get_account_settings request example
        """
        try:
            global account_settings_etag

            print('\nget_account_settings() result:')
            # begin-getAccountSettings

            response = iam_identity_service.get_account_settings(
                account_id=account_id
            )
            settings = response.get_result()
            account_settings_etag = response.get_headers()['Etag']

            print(json.dumps(settings, indent=2))

            # end-getAccountSettings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_account_settings_example(self):
        """
        update_account_settings request example
        """
        try:
            global account_settings_etag

            print('\nupdate_account_settings() result:')
            # begin-updateAccountSettings

            account_settings_response = iam_identity_service.update_account_settings(
                account_id=account_id,
                if_match=account_settings_etag,
                restrict_create_service_id="NOT_RESTRICTED",
                restrict_create_platform_apikey="NOT_RESTRICTED",
                mfa="NONE",
                session_expiration_in_seconds="86400",
                session_invalidation_in_seconds="7200",
            ).get_result()

            print(json.dumps(account_settings_response, indent=2))

            # end-updateAccountSettings

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: IamIdentityV1
##############################################################################
