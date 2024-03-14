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
import time
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
# IAM_IDENTITY_IAM_ID_MEMBER=<IAM ID of a user belonging to the account but different to the one above>
# IAM_IDENTITY_ENTERPRISE_ACCOUNT_ID=<AccountID of the enterprise account>
# IAM_IDENTITY_ENTERPRISE_SUBACCOUNT_ID=<AccountID of an account in the enterprise>
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

# config property values
account_id = None
iam_id = None
iam_id_member = None
apikey = None
enterprise_account_id = None
enterprise_subaccount_id = None

apikey_id = None
apikey_etag = None

svc_id = None
svc_id_etag = None

profile_id = None
profile_etag = None
profile_identity_etag = None

claimRule_id = None
claimRule_etag = None

link_id = None

account_settings_etag = None

report_reference_mfa = None

profile_template_id = None
profile_template_version = None
profile_template_etag = None
profile_template_assignment_id = None
profile_template_assignment_etag = None

account_settings_template_id = None
account_settings_template_version = None
account_settings_template_etag = None
account_settings_template_assignment_id = None
account_settings_template_assignment_etag = None


##############################################################################
# Start of Examples for Service: IamIdentityV1
##############################################################################
# region
class TestIamIdentityV1Examples:
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

            global iam_id_member
            iam_id_member = config['IAM_ID_MEMBER']

            global apikey
            apikey = config['APIKEY']

            global enterprise_account_id
            enterprise_account_id = config['ENTERPRISE_ACCOUNT_ID']

            global enterprise_subaccount_id
            enterprise_subaccount_id = config['ENTERPRISE_SUBACCOUNT_ID']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @classmethod
    def isFinished(cls, status):
        return "succeeded" == status.lower() or "failed" == status.lower()

    @classmethod
    def waitUntilTrustedProfileAssignmentFinished(cls, service, assignmentId):
        finished = False
        for x in range(20):
            try:
                response = service.get_trusted_profile_assignment(assignment_id=assignmentId)
                assignment = response.get_result()
                finished = cls.isFinished(assignment['status'])
                if finished:
                    global profile_template_assignment_etag
                    profile_template_assignment_etag = response.get_headers()['Etag']
                    profile_template_assignment_etag is not None
                    break
            except ApiException as e:
                if e.code == 404:
                    finished = True
                    break
            time.sleep(10)
        assert finished == True

    @classmethod
    def waitUntilAccountSettingsAssignmentFinished(cls, service, assignmentId):
        finished = False
        for x in range(20):
            try:
                response = service.get_account_settings_assignment(assignment_id=assignmentId)
                assignment = response.get_result()
                finished = cls.isFinished(assignment['status'])
                if finished:
                    global account_settings_template_assignment_etag
                    account_settings_template_assignment_etag = response.get_headers()['Etag']
                    account_settings_template_assignment_etag is not None
                    break
            except ApiException as e:
                if e.code == 404:
                    finished = True
                    break
            time.sleep(10)
        assert finished == True

    @needscredentials
    def test_create_api_key_example(self):
        """
        create_api_key request example
        """
        try:
            print('\ncreate_api_key() result:')
            # begin-create_api_key

            api_key = iam_identity_service.create_api_key(name=apikey_name, iam_id=iam_id).get_result()
            print(json.dumps(api_key, indent=2))

            # end-create_api_key

            global apikey_id
            apikey_id = api_key['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_api_keys_example(self):
        """
        list_api_keys request example
        """
        try:
            print('\nlist_api_keys() result:')
            # begin-list_api_keys

            api_key_list = iam_identity_service.list_api_keys(
                account_id=account_id, iam_id=iam_id, include_history=True
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
            print('\nget_api_keys_details() result:')
            # begin-get_api_keys_details

            api_key = iam_identity_service.get_api_keys_details(iam_api_key=apikey).get_result()
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
            print('\nget_api_key() result:')
            # begin-get_api_key

            response = iam_identity_service.get_api_key(
                id=apikey_id,
                include_activity=True,
            )
            api_key = response.get_result()
            print(json.dumps(api_key, indent=2))

            # end-get_api_key

            global apikey_etag
            apikey_etag = response.get_headers()['Etag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_api_key_example(self):
        """
        update_api_key request example
        """
        try:
            print('\nupdate_api_key() result:')
            # begin-update_api_key

            api_key = iam_identity_service.update_api_key(
                id=apikey_id, if_match=apikey_etag, description='This is an updated description'
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
            # begin-unlock_api_key

            response = iam_identity_service.unlock_api_key(id=apikey_id)

            # end-unlock_api_key

            print('\nunlock_api_key() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_disable_api_key_example(self):
        """
        disable_api_key request example
        """
        try:
            # begin-disable_api_key

            response = iam_identity_service.disable_api_key(id=apikey_id)

            # end-disable_api_key
            print('\nlock_api_key() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_enable_api_key_example(self):
        """
        enable_api_key request example
        """
        try:
            # begin-enable_api_key

            response = iam_identity_service.enable_api_key(id=apikey_id)

            # end-enable_api_key

            print('\nunlock_api_key() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_api_key_example(self):
        """
        delete_api_key request example
        """
        try:
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
            print('\ncreate_service_id() result:')
            # begin-create_service_id

            service_id = iam_identity_service.create_service_id(
                account_id=account_id, name=serviceid_name, description='Example ServiceId'
            ).get_result()
            print(json.dumps(service_id, indent=2))

            # end-create_service_id

            global svc_id
            svc_id = service_id['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_service_id_example(self):
        """
        get_service_id request example
        """
        try:
            print('\nget_service_id() result:')
            # begin-get_service_id

            response = iam_identity_service.get_service_id(
                id=svc_id,
                include_history=True,
                include_activity=True,
            )
            service_id = response.get_result()
            print(json.dumps(service_id, indent=2))

            # end-get_service_id

            global svc_id_etag
            svc_id_etag = response.get_headers()['Etag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_service_ids_example(self):
        """
        list_service_ids request example
        """
        try:
            print('\nlist_service_ids() result:')
            # begin-list_service_ids

            service_id_list = iam_identity_service.list_service_ids(
                account_id=account_id, name=serviceid_name
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
            print('\nupdate_service_id() result:')
            # begin-update_service_id

            service_id = iam_identity_service.update_service_id(
                id=svc_id, if_match=svc_id_etag, description='This is an updated description'
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
            print('\ncreate_profile() result:')
            # begin-create_profile

            profile = iam_identity_service.create_profile(
                name="example profile", description="example profile", account_id=account_id
            ).get_result()
            print(json.dumps(profile, indent=2))

            # end-create_profile

            global profile_id
            profile_id = profile['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_profile_example(self):
        """
        get_profile request example
        """
        try:
            print('\nget_profile() result:')
            # begin-get_profile

            response = iam_identity_service.get_profile(
                profile_id=profile_id,
                include_activity=True,
            )
            profile = response.get_result()
            print(json.dumps(profile, indent=2))

            # end-get_profile
            global profile_etag
            profile_etag = response.get_headers()['Etag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_profiles_example(self):
        """
        list_profiles request example
        """
        try:
            print('\nlist_profiles() result:')
            # begin-list_profiles

            profile_list = iam_identity_service.list_profiles(account_id=account_id, include_history=True).get_result()
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
            print('\nupdate_profile() result:')
            # begin-update_profile

            profile = iam_identity_service.update_profile(
                profile_id=profile_id, if_match=profile_etag, description='This is an updated description'
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
            print('\ncreate_claim_rule() result:')
            # begin-create_claim_rule

            profile_claim_rule_conditions_model = {}
            profile_claim_rule_conditions_model['claim'] = 'blueGroups'
            profile_claim_rule_conditions_model['operator'] = 'EQUALS'
            profile_claim_rule_conditions_model['value'] = '\"cloud-docs-dev\"'
            claimRule = iam_identity_service.create_claim_rule(
                profile_id=profile_id,
                type='Profile-SAML',
                realm_name='https://sdk.test.realm/1234',
                expiration=43200,
                conditions=[profile_claim_rule_conditions_model],
            ).get_result()
            print(json.dumps(claimRule, indent=2))

            # end-create_claim_rule

            global claimRule_id
            claimRule_id = claimRule['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_claim_rule_example(self):
        """
        get_claim_rule request example
        """
        try:
            print('\nget_claim_rule() result:')
            # begin-get_claim_rule

            response = iam_identity_service.get_claim_rule(profile_id=profile_id, rule_id=claimRule_id)
            claimRule = response.get_result()
            print(json.dumps(claimRule, indent=2))

            # end-get_claim_rule

            global claimRule_etag
            claimRule_etag = response.get_headers()['Etag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_claim_rules_example(self):
        """
        list_claim_rules request example
        """
        try:
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
            print('\nupdate_claim_rule() result:')
            # begin-update_claim_rule

            profile_claim_rule_conditions_model = {}
            profile_claim_rule_conditions_model['claim'] = 'blueGroups'
            profile_claim_rule_conditions_model['operator'] = 'EQUALS'
            profile_claim_rule_conditions_model['value'] = '\"Europe_Group\"'
            claimRule = iam_identity_service.update_claim_rule(
                profile_id=profile_id,
                rule_id=claimRule_id,
                if_match=claimRule_etag,
                expiration=33200,
                conditions=[profile_claim_rule_conditions_model],
                type='Profile-SAML',
                realm_name='https://sdk.test.realm/1234',
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
            print('\ncreate_link() result:')
            # begin-create_link

            CreateProfileLinkRequestLink = {}
            CreateProfileLinkRequestLink['crn'] = (
                'crn:v1:staging:public:iam-identity::a/' + account_id + '::computeresource:Fake-Compute-Resource'
            )
            CreateProfileLinkRequestLink['namespace'] = 'default'
            CreateProfileLinkRequestLink['name'] = 'nice name'
            link = iam_identity_service.create_link(
                profile_id=profile_id, name='nice link', cr_type='ROKS_SA', link=CreateProfileLinkRequestLink
            ).get_result()
            print(json.dumps(link, indent=2))

            # end-create_link

            global link_id
            link_id = link['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_link_example(self):
        """
        get_link request example
        """
        try:
            print('\nget_link() result:')
            # begin-get_link

            response = iam_identity_service.get_link(profile_id=profile_id, link_id=link_id)
            link = response.get_result()
            print(json.dumps(link, indent=2))

            # end-get_link

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_links_example(self):
        """
        list_links request example
        """
        try:
            print('\nlist_links() result:')
            # begin-list_links

            link_list = iam_identity_service.list_links(
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
            # begin-delete_link

            response = iam_identity_service.delete_link(profile_id=profile_id, link_id=link_id)

            # end-delete_link
            print('\ndelete_link() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_profile_identities(self):
        """
        get_profile_identities request example
        """
        try:
            # begin-get_profile_identities

            response = iam_identity_service.get_profile_identities(profile_id=profile_id)

            # end-get_profile_identities

            print('\nget_profile_identities() response status code: ', response.get_status_code())
            global profile_identity_etag
            profile_identity_etag = response.get_headers()['Etag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_profile_identities(self):
        """
        set_profile_identities request example
        """
        try:
            # begin-set_profile_identities
            accounts = [account_id]
            profileIdentity = ProfileIdentityRequest(
                identifier=iam_id, accounts=accounts, type="user", description="Identity description"
            )
            profile_identities_input = [profileIdentity]
            response = iam_identity_service.set_profile_identities(
                profile_id=profile_id, if_match=profile_identity_etag, identities=profile_identities_input
            )
            # end-set_profile_identities

            print('\nset_profile_identities() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_profile_identity(self):
        """
        set_profile_identity request example
        """
        try:
            # begin-set_profile_identity

            accounts = [account_id]
            response = iam_identity_service.set_profile_identity(
                profile_id=profile_id,
                identity_type="user",
                identifier=iam_id_member,
                type="user",
                accounts=accounts,
                description="Identity description",
            )

            # end-set_profile_identity

            print('\nset_profile_identities() response status code: ', response.get_status_code())
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_profile_identity(self):
        """
        get_profile_identity request example
        """
        try:
            # begin-get_profile_identity

            response = iam_identity_service.get_profile_identity(
                profile_id=profile_id, identity_type="user", identifier_id=iam_id_member
            )

            # end-get_profile_identity

            print('\nget_profile_identities() response status code: ', response.get_status_code())
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_profile_identity(self):
        """
        delete_profile_identity request example
        """
        try:
            # begin-delete_profile_identity

            response = iam_identity_service.delete_profile_identity(
                profile_id=profile_id, identity_type="user", identifier_id=iam_id_member
            )

            # end-delete_profile_identity

            print('\ndelete_profile_identity() response status code: ', response.get_status_code())
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_profile_example(self):
        """
        delete_profile request example
        """
        try:
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
            print('\nget_account_settings() result:')
            # begin-getAccountSettings

            response = iam_identity_service.get_account_settings(account_id=account_id)
            settings = response.get_result()
            print(json.dumps(settings, indent=2))

            # end-getAccountSettings

            global account_settings_etag
            account_settings_etag = response.get_headers()['Etag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_account_settings_example(self):
        """
        update_account_settings request example
        """
        try:
            print('\nupdate_account_settings() result:')
            # begin-updateAccountSettings

            account_settings_user_mfa = {}
            account_settings_user_mfa['iam_id'] = iam_id_member
            account_settings_user_mfa['mfa'] = 'NONE'
            account_settings_response = iam_identity_service.update_account_settings(
                account_id=account_id,
                if_match=account_settings_etag,
                restrict_create_service_id="NOT_RESTRICTED",
                restrict_create_platform_apikey="NOT_RESTRICTED",
                mfa="NONE",
                user_mfa=[account_settings_user_mfa],
                session_expiration_in_seconds="86400",
                session_invalidation_in_seconds="7200",
                max_sessions_per_identity='10',
                system_access_token_expiration_in_seconds='3600',
                system_refresh_token_expiration_in_seconds='259200',
            ).get_result()
            print(json.dumps(account_settings_response, indent=2))

            # end-updateAccountSettings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_report(self):
        """
        create_report request example
        """
        try:
            print('\ncreate_report() result:')
            # begin-create_report

            create_report_response = iam_identity_service.create_report(
                account_id=account_id,
                type="inactive",
                duration="120",
            ).get_result()
            print(json.dumps(create_report_response, indent=2))

            # end-create_report

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_report(self):
        """
        get_report request example
        """
        try:
            print('\nget_report() result:')
            # begin-get_report

            get_report_response = iam_identity_service.get_report(
                account_id=account_id, reference="latest"
            ).get_result()
            print(json.dumps(get_report_response, indent=2))

            # end-get_report

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_mfa_report(self):
        """
        create_mfa_report request example
        """
        try:
            print('\ncreate_mfa_report() result:')
            # begin-create_mfa_report

            create_report_response = iam_identity_service.create_mfa_report(
                account_id=account_id, type="mfa_status"
            ).get_result()
            print(json.dumps(create_report_response, indent=2))

            # end-create_mfa_report
            global report_reference_mfa
            report_reference_mfa = create_report_response['reference']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_mfa_report(self):
        """
        get_mfa_report request example
        """
        try:
            print('\nget_mfa_report() result:')
            # begin-get_mfa_report

            get_report_response = iam_identity_service.get_mfa_report(
                account_id=account_id, reference=report_reference_mfa
            ).get_result()
            print(json.dumps(get_report_response, indent=2))

            # end-get_mfa_report

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_mfa_status(self):
        """
        get_mfa_status request example
        """
        try:
            print('\nget_mfa_status() result:')
            # begin-get_mfa_status

            get_mfa_status_response = iam_identity_service.get_mfa_status(
                account_id=account_id, iam_id=iam_id
            ).get_result()
            print(json.dumps(get_mfa_status_response, indent=2))

            # end-get_mfa_status

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_profile_template(self):
        """
        create_profile_template request example
        """
        try:
            print('\ncreate_profile_template() result:')
            # begin-create_profile_template

            profile_claim_rule_conditions = {}
            profile_claim_rule_conditions['claim'] = 'blueGroups'
            profile_claim_rule_conditions['operator'] = 'EQUALS'
            profile_claim_rule_conditions['value'] = '\"cloud-docs-dev\"'

            profile_claim_rule = {}
            profile_claim_rule['name'] = 'My Rule'
            profile_claim_rule['realm_name'] = 'https://sdk.test.realm/1234'
            profile_claim_rule['type'] = 'Profile-SAML'
            profile_claim_rule['expiration'] = 43200
            profile_claim_rule['conditions'] = [profile_claim_rule_conditions]

            profile = {}
            profile['name'] = 'Profile-From-Example-Template'
            profile['description'] = 'Trusted profile created from a template'
            profile['rules'] = [profile_claim_rule]

            create_response = iam_identity_service.create_profile_template(
                name='Example-Profile-Template',
                description='IAM enterprise trusted profile template example',
                account_id=enterprise_account_id,
                profile=profile,
            )
            profile_template = create_response.get_result()
            print('\ncreate_profile_template() response: ', json.dumps(profile_template, indent=2))

            # end-create_profile_template
            global profile_template_id
            profile_template_id = profile_template['id']
            global profile_template_version
            profile_template_version = profile_template['version']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_profile_template(self):
        """
        get_profile_template request example
        """
        try:
            print('\nget_profile_template() result:')
            # begin-get_profile_template_version

            get_response = iam_identity_service.get_profile_template_version(
                template_id=profile_template_id, version=str(profile_template_version)
            )
            profile_template = get_response.get_result()
            print('\nget_profile_template response: ', json.dumps(profile_template, indent=2))

            # end-get_profile_template_version

            global profile_template_etag
            profile_template_etag = get_response.get_headers()['Etag']
            profile_template_etag is not None
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_profile_templates(self):
        """
        list_profile_templates request example
        """
        try:
            print('\nlist_profile_templates() result:')
            # begin-list_profile_templates

            list_response = iam_identity_service.list_profile_templates(account_id=enterprise_account_id)
            profile_template_list = list_response.get_result()
            print('\nlist_profile_templates response: ', json.dumps(profile_template_list, indent=2))

            # end-list_profile_templates
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_profile_template(self):
        """
        update_profile_template request example
        """
        try:
            print('\nupdate_profile_template() result:')
            global profile_template_etag
            # begin-update_profile_template_version

            update_response = iam_identity_service.update_profile_template_version(
                account_id=enterprise_account_id,
                template_id=profile_template_id,
                version=str(profile_template_version),
                if_match=profile_template_etag,
                name='Example-Profile-Template',
                description='IAM enterprise trusted profile template example - updated',
            )
            profile_template = update_response.get_result()
            print('\nupdate_profile_template() response: ', json.dumps(profile_template, indent=2))

            # end-update_profile_template_version

            profile_template_etag = update_response.get_headers()['Etag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_assign_profile_template(self):
        """
        commit_profile_template request example
        """
        try:
            print('\nupdate_profile_template() result:')
            # begin-commit_profile_template

            commit_response = iam_identity_service.commit_profile_template(
                template_id=profile_template_id, version=str(profile_template_version)
            )

            # end-commit_profile_template

            """
            create_trusted_profile_assignment request example
            """
            # begin-create_trusted_profile_assignment

            assign_response = iam_identity_service.create_trusted_profile_assignment(
                template_id=profile_template_id,
                template_version=profile_template_version,
                target_type='Account',
                target=enterprise_subaccount_id,
            )
            assignment = assign_response.get_result()
            print('\ncreate_trusted_profile_assignment() response: ', json.dumps(assignment, indent=2))

            # end-create_trusted_profile_assignment

            global profile_template_assignment_id
            profile_template_assignment_id = assignment['id']
            global profile_template_assignment_etag
            profile_template_assignment_etag = assign_response.get_headers()['Etag']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_trusted_profile_assignment(self):
        """
        get_trusted_profile_assignment request example
        """
        try:
            print('\nget_trusted_profile_assignment() result:')
            # begin-get_trusted_profile_assignment

            response = iam_identity_service.get_trusted_profile_assignment(assignment_id=profile_template_assignment_id)
            assignment = response.get_result()
            print('\nget_trusted_profile_assignment() response: ', json.dumps(assignment, indent=2))

            # end-get_trusted_profile_assignment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_profile_template_assignments(self):
        """
        list_profile_template_assignments request example
        """
        try:
            print('\nlist_profile_template_assignments() result:')
            # begin-list_trusted_profile_assignments

            list_response = iam_identity_service.list_trusted_profile_assignments(
                account_id=enterprise_account_id, template_id=profile_template_id
            )
            assignment_list = list_response.get_result()
            print('\nlist_trusted_profile_assignments() response: ', json.dumps(assignment_list, indent=2))

            # end-list_trusted_profile_assignments
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_new_profile_template_version(self):
        """
        create_profile_template_version request example
        """
        try:
            print('\ncreate_profile_template_version() result:')
            # begin-create_profile_template_version

            profile_claim_rule_conditions = {}
            profile_claim_rule_conditions['claim'] = 'blueGroups'
            profile_claim_rule_conditions['operator'] = 'EQUALS'
            profile_claim_rule_conditions['value'] = '\"cloud-docs-dev\"'

            profile_claim_rule = {}
            profile_claim_rule['name'] = 'My Rule'
            profile_claim_rule['realm_name'] = 'https://sdk.test.realm/1234'
            profile_claim_rule['type'] = 'Profile-SAML'
            profile_claim_rule['expiration'] = 43200
            profile_claim_rule['conditions'] = [profile_claim_rule_conditions]

            profile_identity = {}
            profile_identity['identifier'] = iam_id
            profile_identity['accounts'] = [enterprise_account_id]
            profile_identity['type'] = 'user'
            profile_identity['description'] = 'Identity description'

            profile = {}
            profile['name'] = 'Profile-From-Example-Template'
            profile['description'] = 'Trusted profile created from a template - new version'
            profile['rules'] = [profile_claim_rule]
            profile['identities'] = [profile_identity]

            create_response = iam_identity_service.create_profile_template_version(
                template_id=profile_template_id,
                name='Example-Profile-Template',
                description='IAM enterprise trusted profile template example - new version',
                account_id=enterprise_account_id,
                profile=profile,
            )
            profile_template = create_response.get_result()
            print('\ncreate_profile_template_version() response: ', json.dumps(profile_template, indent=2))

            # end-create_profile_template_version
            global profile_template_version
            profile_template_version = profile_template['version']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_latest_profile_template_version(self):
        """
        get_latest_profile_template_version request example
        """
        try:
            print('\nget_latest_profile_template_version() result:')
            # begin-get_latest_profile_template_version

            get_response = iam_identity_service.get_latest_profile_template_version(template_id=profile_template_id)

            profile_template = get_response.get_result()
            print('\nget_latest_profile_template_version response: ', json.dumps(profile_template, indent=2))

            # end-get_latest_profile_template_version
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_profile_template_versions(self):
        """
        list_profile_template_versions request example
        """
        try:
            print('\nlist_profile_template_versions() result:')
            # begin-list_versions_of_profile_template

            list_response = iam_identity_service.list_versions_of_profile_template(template_id=profile_template_id)
            profile_template_list = list_response.get_result()
            print('\nlist_profile_template_versions response: ', json.dumps(profile_template_list, indent=2))

            # end-list_versions_of_profile_template
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_profile_template_assignment(self):
        """
        update_trusted_profile_assignment request example
        """
        try:
            print('\nupdate_trusted_profile_assignment() result:')
            commit_response = iam_identity_service.commit_profile_template(
                template_id=profile_template_id, version=str(profile_template_version)
            )
            self.waitUntilTrustedProfileAssignmentFinished(iam_identity_service, profile_template_assignment_id)
            global profile_template_assignment_etag
            # begin-update_trusted_profile_assignment

            assign_response = iam_identity_service.update_trusted_profile_assignment(
                assignment_id=profile_template_assignment_id,
                template_version=profile_template_version,
                if_match=profile_template_assignment_etag,
            )
            assignment = assign_response.get_result()
            print('\nupdate_profile_template_assignment response: ', json.dumps(assignment, indent=2))

            # end-update_trusted_profile_assignment

            profile_template_assignment_etag = assign_response.get_headers()['Etag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_profile_template_assignment(self):
        """
        delete_trusted_profile_assignment request example
        """
        try:
            print('\ndelete_trusted_profile_assignment() result:')
            self.waitUntilTrustedProfileAssignmentFinished(iam_identity_service, profile_template_assignment_id)
            # begin-delete_trusted_profile_assignment

            delete_response = iam_identity_service.delete_trusted_profile_assignment(
                assignment_id=profile_template_assignment_id
            )

            # end-delete_trusted_profile_assignment
            self.waitUntilTrustedProfileAssignmentFinished(iam_identity_service, profile_template_assignment_id)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_profile_template_version(self):
        """
        delete_profile_template_version request example
        """
        try:
            print('\ndelete_profile_template_version() result:')
            # begin-delete_profile_template_version

            delete_response = iam_identity_service.delete_profile_template_version(
                template_id=profile_template_id, version='1'
            )

            # end-delete_profile_template_version
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_profile_template(self):
        """
        delete_all_versions_of_profile_template request example
        """
        try:
            print('\ndelete_all_versions_of_profile_template() result:')
            self.waitUntilTrustedProfileAssignmentFinished(iam_identity_service, profile_template_assignment_id)
            # begin-delete_all_versions_of_profile_template

            delete_response = iam_identity_service.delete_all_versions_of_profile_template(
                template_id=profile_template_id
            )

            # end-delete_all_versions_of_profile_template
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_account_settings_template(self):
        """
        create_account_settings_template request example
        """
        try:
            print('\ncreate_account_settings_template() result:')
            # begin-create_account_settings_template

            account_settings = {}
            account_settings['mfa'] = 'LEVEL1'
            account_settings['system_access_token_expiration_in_seconds'] = 3000

            create_response = iam_identity_service.create_account_settings_template(
                name='Example-Account-Settings-Template',
                description='IAM enterprise account settings template example',
                account_id=enterprise_account_id,
                account_settings=account_settings,
            )
            account_settings_template = create_response.get_result()
            print('\ncreate_account_settings_template() response: ', json.dumps(account_settings_template, indent=2))

            # end-create_account_settings_template
            global account_settings_template_id
            global account_settings_template_version
            account_settings_template_id = account_settings_template['id']
            account_settings_template_version = account_settings_template['version']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_account_settings_template(self):
        """
        get_account_settings_template_version request example
        """
        try:
            print('\nget_account_settings_template_version() result:')
            # begin-get_account_settings_template_version

            get_response = iam_identity_service.get_account_settings_template_version(
                template_id=account_settings_template_id, version=str(account_settings_template_version)
            )

            account_settings_template = get_response.get_result()
            print('\nget_account_settings_template response: ', json.dumps(account_settings_template, indent=2))

            # end-get_account_settings_template_version

            global account_settings_template_etag
            account_settings_template_etag = get_response.get_headers()['Etag']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_account_settings_templates(self):
        """
        list_account_settings_templates request example
        """
        try:
            print('\nlist_account_settings_templates() result:')
            # begin-list_account_settings_templates

            list_response = iam_identity_service.list_account_settings_templates(account_id=enterprise_account_id)
            account_settings_template_list = list_response.get_result()
            print('\nlist_account_settings_templates response: ', json.dumps(account_settings_template_list, indent=2))

            # end-list_account_settings_templates
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_account_settings_template(self):
        """
        update_account_settings_template_version request example
        """
        try:
            print('\nupdate_account_settings_template_version() result:')
            global account_settings_template_etag
            # begin-update_account_settings_template_version

            account_settings = {}
            account_settings['mfa'] = 'LEVEL1'
            account_settings['system_access_token_expiration_in_seconds'] = 3000

            update_response = iam_identity_service.update_account_settings_template_version(
                account_id=enterprise_account_id,
                template_id=account_settings_template_id,
                version=str(account_settings_template_version),
                if_match=account_settings_template_etag,
                name='Example-Account-Settings-Template',
                description='IAM enterprise account settings template example - updated',
                account_settings=account_settings,
            )
            account_settings_template = update_response.get_result()
            print('\nupdate_account_settings_template() response: ', json.dumps(account_settings_template, indent=2))

            # end-update_account_settings_template_version
            account_settings_template_etag = update_response.get_headers()['Etag']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_assign_account_settings_template(self):
        """
        commit_account_settings_template request example
        """
        try:
            print('\ncommit_account_settings_template() result:')
            # begin-commit_account_settings_template

            commit_response = iam_identity_service.commit_account_settings_template(
                template_id=account_settings_template_id, version=str(account_settings_template_version)
            )

            # end-commit_account_settings_template

            """
            create_account_settings_assignment request example
            """
            print('\ncreate_account_settings_assignment() result:')
            # begin-create_account_settings_assignment

            assign_response = iam_identity_service.create_account_settings_assignment(
                template_id=account_settings_template_id,
                template_version=account_settings_template_version,
                target_type='Account',
                target=enterprise_subaccount_id,
            )
            assignment = assign_response.get_result()
            print('\ncreate_account_settings_assignment() response: ', json.dumps(assignment, indent=2))

            # end-create_account_settings_assignment

            global account_settings_template_assignment_id
            account_settings_template_assignment_id = assignment['id']
            global account_settings_template_assignment_etag
            account_settings_template_assignment_etag = assign_response.get_headers()['Etag']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_account_settings_template_assignments(self):
        """
        list_account_settings_assignments request example
        """
        try:
            print('\nlist_account_settings_assignments() result:')
            # begin-list_account_settings_assignments

            list_response = iam_identity_service.list_account_settings_assignments(
                account_id=enterprise_account_id, template_id=account_settings_template_id
            )
            assignment_list = list_response.get_result()
            print('\ncreate_account_settings_assignment() response: ', json.dumps(assignment_list, indent=2))

            # end-list_account_settings_assignments
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_latest_account_settings_template_version(self):
        """
        get_account_settings_assignment request example
        """
        try:
            print('\nget_account_settings_assignment() result:')
            # begin-get_account_settings_assignment

            response = iam_identity_service.get_account_settings_assignment(
                assignment_id=account_settings_template_assignment_id
            )
            assignment = response.get_result()
            print('\nget_latest_account_settings_template_version response: ', json.dumps(assignment, indent=2))

            # end-get_account_settings_assignment
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_new_account_settings_template_version(self):
        """
        create_account_settings_template_version request example
        """
        try:
            print('\ncreate_account_settings_template_version() result:')
            # begin-create_account_settings_template_version

            account_settings = {}
            account_settings['mfa'] = 'LEVEL1'
            account_settings['system_access_token_expiration_in_seconds'] = 2600
            account_settings['restrict_create_platform_apikey'] = 'RESTRICTED'
            account_settings['restrict_create_service_id'] = 'RESTRICTED'

            create_response = iam_identity_service.create_account_settings_template_version(
                template_id=account_settings_template_id,
                name='Example-Account-Settings-Template',
                description='IAM enterprise account settings template example - new version',
                account_id=enterprise_account_id,
                account_settings=account_settings,
            )
            account_settings_template = create_response.get_result()
            print(
                '\ncreate_account_settings_template_version() response: ',
                json.dumps(account_settings_template, indent=2),
            )

            # end-create_account_settings_template_version

            global account_settings_template_version
            account_settings_template_version = account_settings_template['version']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_latest_account_settings_template_version(self):
        """
        get_latest_account_settings_template_version request example
        """
        try:
            print('\nget_latest_account_settings_template_version() result:')
            # begin-get_latest_account_settings_template_version

            get_response = iam_identity_service.get_latest_account_settings_template_version(
                template_id=account_settings_template_id
            )
            account_settings_template = get_response.get_result()
            print(
                '\nget_latest_account_settings_template_version response: ',
                json.dumps(account_settings_template, indent=2),
            )

            # end-get_latest_account_settings_template_version
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_account_settings_template_versions(self):
        """
        list_versions_of_account_settings_template request example
        """
        try:
            print('\nlist_versions_of_account_settings_template() result:')
            # begin-list_versions_of_account_settings_template

            list_response = iam_identity_service.list_versions_of_account_settings_template(
                template_id=account_settings_template_id
            )
            account_settings_template_list = list_response.get_result()
            print(
                '\nlist_account_settings_template_versions response: ',
                json.dumps(account_settings_template_list, indent=2),
            )

            # end-list_versions_of_account_settings_template
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_account_settings_template_assignment(self):
        """
        update_account_settings_assignment request example
        """
        try:
            print('\nupdate_account_settings_assignment() result:')
            commit_response = iam_identity_service.commit_account_settings_template(
                template_id=account_settings_template_id, version=str(account_settings_template_version)
            )

            self.waitUntilAccountSettingsAssignmentFinished(
                iam_identity_service, account_settings_template_assignment_id
            )
            global account_settings_template_assignment_etag
            # begin-update_account_settings_assignment

            assign_response = iam_identity_service.update_account_settings_assignment(
                assignment_id=account_settings_template_assignment_id,
                template_version=account_settings_template_version,
                if_match=account_settings_template_assignment_etag,
            )
            assignment = assign_response.get_result()
            print('\nupdate_account_settings_template_assignment response: ', json.dumps(assignment, indent=2))

            # end-update_account_settings_assignment
            account_settings_template_assignment_etag = assign_response.get_headers()['Etag']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_account_settings_template_assignment(self):
        """
        delete_account_settings_assignment request example
        """
        try:
            print('\ndelete_account_settings_assignment() result:')
            self.waitUntilAccountSettingsAssignmentFinished(
                iam_identity_service, account_settings_template_assignment_id
            )

            # begin-delete_account_settings_assignment

            delete_response = iam_identity_service.delete_account_settings_assignment(
                assignment_id=account_settings_template_assignment_id
            )

            # end-delete_account_settings_assignment
            self.waitUntilAccountSettingsAssignmentFinished(
                iam_identity_service, account_settings_template_assignment_id
            )
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_account_settings_template_version(self):
        """
        delete_account_settings_template_version request example
        """
        try:
            print('\ndelete_account_settings_template_version() result:')
            # begin-delete_account_settings_template_version

            delete_response = iam_identity_service.delete_account_settings_template_version(
                template_id=account_settings_template_id, version='1'
            )

            # end-delete_account_settings_template_version
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_account_settings_template(self):
        """
        delete_all_versions_of_account_settings_template request example
        """
        try:
            print('\ndelete_all_versions_of_account_settings_template() result:')

            self.waitUntilAccountSettingsAssignmentFinished(
                iam_identity_service, account_settings_template_assignment_id
            )

            # begin-delete_all_versions_of_account_settings_template

            delete_response = iam_identity_service.delete_all_versions_of_account_settings_template(
                template_id=account_settings_template_id
            )

            # end-delete_all_versions_of_account_settings_template
        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: IamIdentityV1
##############################################################################
