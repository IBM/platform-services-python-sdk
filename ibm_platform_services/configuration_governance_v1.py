# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 99-SNAPSHOT-c6db7f4a-20210114-141015
 
"""
API specification for the Configuration Governance service.
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class ConfigurationGovernanceV1(BaseService):
    """The Configuration Governance V1 service."""

    DEFAULT_SERVICE_URL = 'https://compliance.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'configuration_governance'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ConfigurationGovernanceV1':
        """
        Return a new client for the Configuration Governance service using the
               specified parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Configuration Governance service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Rules
    #########################


    def create_rules(self,
        rules: List['CreateRuleRequest'],
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create rules.

        Creates one or more rules that you can use to govern the way that IBM Cloud
        resources can be provisioned and configured.
        A successful `POST /config/rules` request defines a rule based on the target,
        conditions, and enforcement actions that you specify. The response returns the ID
        value for your rule, along with other metadata.

        :param List[CreateRuleRequest] rules: A list of rules to be created.
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateRulesResponse` object
        """

        if rules is None:
            raise ValueError('rules must be provided')
        rules = [convert_model(x) for x in rules]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_rules')
        headers.update(sdk_headers)

        data = {
            'rules': rules
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/config/v1/rules'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_rules(self,
        account_id: str,
        *,
        transaction_id: str = None,
        attached: bool = None,
        labels: str = None,
        scopes: str = None,
        limit: int = None,
        offset: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List rules.

        Retrieves a list of the rules that are available in your account.

        :param str account_id: Your IBM Cloud account ID.
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param bool attached: (optional) Retrieves a list of rules that have scope
               attachments.
        :param str labels: (optional) Retrieves a list of rules that match the
               labels that you specify.
        :param str scopes: (optional) Retrieves a list of rules that match the
               scope ID that you specify.
        :param int limit: (optional) The number of resources to retrieve. By
               default, list operations return the first 100 items. To retrieve a
               different set of items, use `limit` with `offset` to page through your
               available resources.
               **Usage:** If you have 20 rules, and you want to retrieve only the first 5
               rules, use `../rules?account_id={account_id}&limit=5`.
        :param int offset: (optional) The number of resources to skip. By
               specifying `offset`, you retrieve a subset of resources that starts with
               the `offset` value. Use `offset` with `limit` to page through your
               available resources.
               **Usage:** If you have 100 rules, and you want to retrieve rules 26 through
               50, use `../rules?account_id={account_id}&offset=25&limit=5`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RuleList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_rules')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'attached': attached,
            'labels': labels,
            'scopes': scopes,
            'limit': limit,
            'offset': offset
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/config/v1/rules'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_rule(self,
        rule_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a rule.

        Retrieves an existing rule and its details.

        :param str rule_id: The UUID that uniquely identifies the rule.
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/config/v1/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_rule(self,
        rule_id: str,
        if_match: str,
        name: str,
        description: str,
        target: 'TargetResource',
        required_config: 'RuleRequiredConfig',
        enforcement_actions: List['EnforcementAction'],
        *,
        account_id: str = None,
        rule_type: str = None,
        labels: List[str] = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a rule.

        Updates an existing rule based on the properties that you specify.

        :param str rule_id: The UUID that uniquely identifies the rule.
        :param str if_match: Compares a supplied `Etag` value with the version that
               is stored for the requested resource. If the values match, the server
               allows the request method to continue.
               To find the `Etag` value, run a GET request on the resource that you want
               to modify, and check the response headers.
        :param str name: A human-readable alias to assign to your rule.
        :param str description: An extended description of your rule.
        :param TargetResource target: The properties that describe the resource
               that you want to target
               with the rule.
        :param RuleRequiredConfig required_config:
        :param List[EnforcementAction] enforcement_actions: The actions that the
               service must run on your behalf when a request to create or modify the
               target resource does not comply with your conditions.
        :param str account_id: (optional) Your IBM Cloud account ID.
        :param str rule_type: (optional) The type of rule. Rules that you create
               are `user_defined`.
        :param List[str] labels: (optional) Labels that you can use to group and
               search for similar rules, such as those that help you to meet a specific
               organization guideline.
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if description is None:
            raise ValueError('description must be provided')
        if target is None:
            raise ValueError('target must be provided')
        if required_config is None:
            raise ValueError('required_config must be provided')
        if enforcement_actions is None:
            raise ValueError('enforcement_actions must be provided')
        target = convert_model(target)
        required_config = convert_model(required_config)
        enforcement_actions = [convert_model(x) for x in enforcement_actions]
        headers = {
            'If-Match': if_match,
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_rule')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'target': target,
            'required_config': required_config,
            'enforcement_actions': enforcement_actions,
            'account_id': account_id,
            'rule_type': rule_type,
            'labels': labels
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/config/v1/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_rule(self,
        rule_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a rule.

        Deletes an existing rule.

        :param str rule_id: The UUID that uniquely identifies the rule.
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/config/v1/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_attachments(self,
        rule_id: str,
        attachments: List['AttachmentRequest'],
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create attachments.

        Creates one or more scope attachments for an existing rule.
        You can attach an existing rule to a scope, such as a specific IBM Cloud account,
        to start evaluating the rule for compliance. A successful
        `POST /config/v1/rules/{rule_id}/attachments` returns the ID value for the
        attachment, along with other metadata.

        :param str rule_id: The UUID that uniquely identifies the rule.
        :param List[AttachmentRequest] attachments:
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateAttachmentsResponse` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if attachments is None:
            raise ValueError('attachments must be provided')
        attachments = [convert_model(x) for x in attachments]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_attachments')
        headers.update(sdk_headers)

        data = {
            'attachments': attachments
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/config/v1/rules/{rule_id}/attachments'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_attachments(self,
        rule_id: str,
        *,
        transaction_id: str = None,
        limit: int = None,
        offset: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List attachments.

        Retrieves a list of scope attachments that are associated with the specified rule.

        :param str rule_id: The UUID that uniquely identifies the rule.
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param int limit: (optional) The number of resources to retrieve. By
               default, list operations return the first 100 items. To retrieve a
               different set of items, use `limit` with `offset` to page through your
               available resources.
               **Usage:** If you have 20 rules, and you want to retrieve only the first 5
               rules, use `../rules?account_id={account_id}&limit=5`.
        :param int offset: (optional) The number of resources to skip. By
               specifying `offset`, you retrieve a subset of resources that starts with
               the `offset` value. Use `offset` with `limit` to page through your
               available resources.
               **Usage:** If you have 100 rules, and you want to retrieve rules 26 through
               50, use `../rules?account_id={account_id}&offset=25&limit=5`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentList` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_attachments')
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'offset': offset
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/config/v1/rules/{rule_id}/attachments'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_attachment(self,
        rule_id: str,
        attachment_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get an attachment.

        Retrieves an existing scope attachment for a rule.

        :param str rule_id: The UUID that uniquely identifies the rule.
        :param str attachment_id: The UUID that uniquely identifies the attachment.
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Attachment` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if attachment_id is None:
            raise ValueError('attachment_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_attachment')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id', 'attachment_id']
        path_param_values = self.encode_path_vars(rule_id, attachment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/config/v1/rules/{rule_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_attachment(self,
        rule_id: str,
        attachment_id: str,
        if_match: str,
        account_id: str,
        included_scope: 'RuleScope',
        *,
        excluded_scopes: List['RuleScope'] = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update an attachment.

        Updates an existing scope attachment based on the properties that you specify.

        :param str rule_id: The UUID that uniquely identifies the rule.
        :param str attachment_id: The UUID that uniquely identifies the attachment.
        :param str if_match: Compares a supplied `Etag` value with the version that
               is stored for the requested resource. If the values match, the server
               allows the request method to continue.
               To find the `Etag` value, run a GET request on the resource that you want
               to modify, and check the response headers.
        :param str account_id: Your IBM Cloud account ID.
        :param RuleScope included_scope: The extent at which the rule can be
               attached across your accounts.
        :param List[RuleScope] excluded_scopes: (optional) The extent at which the
               rule can be excluded from the included scope.
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Attachment` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if attachment_id is None:
            raise ValueError('attachment_id must be provided')
        if if_match is None:
            raise ValueError('if_match must be provided')
        if account_id is None:
            raise ValueError('account_id must be provided')
        if included_scope is None:
            raise ValueError('included_scope must be provided')
        included_scope = convert_model(included_scope)
        if excluded_scopes is not None:
            excluded_scopes = [convert_model(x) for x in excluded_scopes]
        headers = {
            'If-Match': if_match,
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_attachment')
        headers.update(sdk_headers)

        data = {
            'account_id': account_id,
            'included_scope': included_scope,
            'excluded_scopes': excluded_scopes
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id', 'attachment_id']
        path_param_values = self.encode_path_vars(rule_id, attachment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/config/v1/rules/{rule_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_attachment(self,
        rule_id: str,
        attachment_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an attachment.

        Deletes an existing scope attachment.

        :param str rule_id: The UUID that uniquely identifies the rule.
        :param str attachment_id: The UUID that uniquely identifies the attachment.
        :param str transaction_id: (optional) The unique identifier that is used to
               trace an entire request. If you omit this field, the service generates and
               sends a transaction ID as a response header of the request. In the case of
               an error, the transaction ID is set in the `trace` field of the response
               body.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `Transaction-Id` with each request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if attachment_id is None:
            raise ValueError('attachment_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_attachment')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['rule_id', 'attachment_id']
        path_param_values = self.encode_path_vars(rule_id, attachment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/config/v1/rules/{rule_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class Attachment():
    """
    The scopes to attach to the rule.

    :attr str attachment_id: The UUID that uniquely identifies the attachment.
    :attr str rule_id: The UUID that uniquely identifies the rule.
    :attr str account_id: Your IBM Cloud account ID.
    :attr RuleScope included_scope: The extent at which the rule can be attached
          across your accounts.
    :attr List[RuleScope] excluded_scopes: (optional) The extent at which the rule
          can be excluded from the included scope.
    """

    def __init__(self,
                 attachment_id: str,
                 rule_id: str,
                 account_id: str,
                 included_scope: 'RuleScope',
                 *,
                 excluded_scopes: List['RuleScope'] = None) -> None:
        """
        Initialize a Attachment object.

        :param str attachment_id: The UUID that uniquely identifies the attachment.
        :param str rule_id: The UUID that uniquely identifies the rule.
        :param str account_id: Your IBM Cloud account ID.
        :param RuleScope included_scope: The extent at which the rule can be
               attached across your accounts.
        :param List[RuleScope] excluded_scopes: (optional) The extent at which the
               rule can be excluded from the included scope.
        """
        self.attachment_id = attachment_id
        self.rule_id = rule_id
        self.account_id = account_id
        self.included_scope = included_scope
        self.excluded_scopes = excluded_scopes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Attachment':
        """Initialize a Attachment object from a json dictionary."""
        args = {}
        if 'attachment_id' in _dict:
            args['attachment_id'] = _dict.get('attachment_id')
        else:
            raise ValueError('Required property \'attachment_id\' not present in Attachment JSON')
        if 'rule_id' in _dict:
            args['rule_id'] = _dict.get('rule_id')
        else:
            raise ValueError('Required property \'rule_id\' not present in Attachment JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in Attachment JSON')
        if 'included_scope' in _dict:
            args['included_scope'] = RuleScope.from_dict(_dict.get('included_scope'))
        else:
            raise ValueError('Required property \'included_scope\' not present in Attachment JSON')
        if 'excluded_scopes' in _dict:
            args['excluded_scopes'] = [RuleScope.from_dict(x) for x in _dict.get('excluded_scopes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Attachment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attachment_id') and self.attachment_id is not None:
            _dict['attachment_id'] = self.attachment_id
        if hasattr(self, 'rule_id') and self.rule_id is not None:
            _dict['rule_id'] = self.rule_id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'included_scope') and self.included_scope is not None:
            _dict['included_scope'] = self.included_scope.to_dict()
        if hasattr(self, 'excluded_scopes') and self.excluded_scopes is not None:
            _dict['excluded_scopes'] = [x.to_dict() for x in self.excluded_scopes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Attachment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Attachment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Attachment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AttachmentList():
    """
    A list of attachments.

    :attr int offset: The requested offset for the returned items.
    :attr int limit: The requested limit for the returned items.
    :attr int total_count: The total number of available items.
    :attr Link first: The first page of available items.
    :attr Link last: The last page of available items.
    :attr List[Attachment] attachments:
    """

    def __init__(self,
                 offset: int,
                 limit: int,
                 total_count: int,
                 first: 'Link',
                 last: 'Link',
                 attachments: List['Attachment']) -> None:
        """
        Initialize a AttachmentList object.

        :param int offset: The requested offset for the returned items.
        :param int limit: The requested limit for the returned items.
        :param int total_count: The total number of available items.
        :param Link first: The first page of available items.
        :param Link last: The last page of available items.
        :param List[Attachment] attachments:
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.last = last
        self.attachments = attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentList':
        """Initialize a AttachmentList object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in AttachmentList JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in AttachmentList JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in AttachmentList JSON')
        if 'first' in _dict:
            args['first'] = Link.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in AttachmentList JSON')
        if 'last' in _dict:
            args['last'] = Link.from_dict(_dict.get('last'))
        else:
            raise ValueError('Required property \'last\' not present in AttachmentList JSON')
        if 'attachments' in _dict:
            args['attachments'] = [Attachment.from_dict(x) for x in _dict.get('attachments')]
        else:
            raise ValueError('Required property \'attachments\' not present in AttachmentList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'attachments') and self.attachments is not None:
            _dict['attachments'] = [x.to_dict() for x in self.attachments]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AttachmentRequest():
    """
    The scopes to attach to the rule.

    :attr str account_id: Your IBM Cloud account ID.
    :attr RuleScope included_scope: The extent at which the rule can be attached
          across your accounts.
    :attr List[RuleScope] excluded_scopes: (optional) The extent at which the rule
          can be excluded from the included scope.
    """

    def __init__(self,
                 account_id: str,
                 included_scope: 'RuleScope',
                 *,
                 excluded_scopes: List['RuleScope'] = None) -> None:
        """
        Initialize a AttachmentRequest object.

        :param str account_id: Your IBM Cloud account ID.
        :param RuleScope included_scope: The extent at which the rule can be
               attached across your accounts.
        :param List[RuleScope] excluded_scopes: (optional) The extent at which the
               rule can be excluded from the included scope.
        """
        self.account_id = account_id
        self.included_scope = included_scope
        self.excluded_scopes = excluded_scopes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentRequest':
        """Initialize a AttachmentRequest object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in AttachmentRequest JSON')
        if 'included_scope' in _dict:
            args['included_scope'] = RuleScope.from_dict(_dict.get('included_scope'))
        else:
            raise ValueError('Required property \'included_scope\' not present in AttachmentRequest JSON')
        if 'excluded_scopes' in _dict:
            args['excluded_scopes'] = [RuleScope.from_dict(x) for x in _dict.get('excluded_scopes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'included_scope') and self.included_scope is not None:
            _dict['included_scope'] = self.included_scope.to_dict()
        if hasattr(self, 'excluded_scopes') and self.excluded_scopes is not None:
            _dict['excluded_scopes'] = [x.to_dict() for x in self.excluded_scopes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreateAttachmentsResponse():
    """
    CreateAttachmentsResponse.

    :attr List[Attachment] attachments:
    """

    def __init__(self,
                 attachments: List['Attachment']) -> None:
        """
        Initialize a CreateAttachmentsResponse object.

        :param List[Attachment] attachments:
        """
        self.attachments = attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateAttachmentsResponse':
        """Initialize a CreateAttachmentsResponse object from a json dictionary."""
        args = {}
        if 'attachments' in _dict:
            args['attachments'] = [Attachment.from_dict(x) for x in _dict.get('attachments')]
        else:
            raise ValueError('Required property \'attachments\' not present in CreateAttachmentsResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateAttachmentsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attachments') and self.attachments is not None:
            _dict['attachments'] = [x.to_dict() for x in self.attachments]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateAttachmentsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateAttachmentsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateAttachmentsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreateRuleRequest():
    """
    A rule to be created.

    :attr str request_id: (optional) A field that you can use in bulk operations to
          store a custom identifier for an individual request. If you omit this field, the
          service generates and sends a `request_id` string for each new rule. The
          generated string corresponds with the numerical order of the rules request
          array. For example, `"request_id": "1"`, `"request_id": "2"`.
          **Note:** To help with debugging logs, it is strongly recommended that you
          generate and supply a `request_id` with each request.
    :attr RuleRequest rule: User-settable properties associated with a rule to be
          created or updated.
    """

    def __init__(self,
                 rule: 'RuleRequest',
                 *,
                 request_id: str = None) -> None:
        """
        Initialize a CreateRuleRequest object.

        :param RuleRequest rule: User-settable properties associated with a rule to
               be created or updated.
        :param str request_id: (optional) A field that you can use in bulk
               operations to store a custom identifier for an individual request. If you
               omit this field, the service generates and sends a `request_id` string for
               each new rule. The generated string corresponds with the numerical order of
               the rules request array. For example, `"request_id": "1"`, `"request_id":
               "2"`.
               **Note:** To help with debugging logs, it is strongly recommended that you
               generate and supply a `request_id` with each request.
        """
        self.request_id = request_id
        self.rule = rule

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateRuleRequest':
        """Initialize a CreateRuleRequest object from a json dictionary."""
        args = {}
        if 'request_id' in _dict:
            args['request_id'] = _dict.get('request_id')
        if 'rule' in _dict:
            args['rule'] = RuleRequest.from_dict(_dict.get('rule'))
        else:
            raise ValueError('Required property \'rule\' not present in CreateRuleRequest JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateRuleRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request_id') and self.request_id is not None:
            _dict['request_id'] = self.request_id
        if hasattr(self, 'rule') and self.rule is not None:
            _dict['rule'] = self.rule.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateRuleRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateRuleRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateRuleRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreateRuleResponse():
    """
    Response information for a rule request.
    If the 'status_code' property indicates success, the 'request_id' and 'rule'
    properties will be present.   If the 'status_code' property indicates an error, the
    'request_id', 'errors', and 'trace' fields will be present.

    :attr str request_id: (optional) The identifier that is used to correlate an
          individual request.
          To assist with debugging, you can use this ID to identify and inspect only one
          request that was made as part of a bulk operation.
    :attr int status_code: (optional) The HTTP response status code.
    :attr Rule rule: (optional) Information about a newly-created rule.
          This field will be present for a successful request.
    :attr List[RuleResponseError] errors: (optional) The error contents of the
          multi-status response.
          This field will be present for a failed rule request.
    :attr str trace: (optional) The UUID that uniquely identifies the request.
          This field will be present for a failed rule request.
    """

    def __init__(self,
                 *,
                 request_id: str = None,
                 status_code: int = None,
                 rule: 'Rule' = None,
                 errors: List['RuleResponseError'] = None,
                 trace: str = None) -> None:
        """
        Initialize a CreateRuleResponse object.

        :param str request_id: (optional) The identifier that is used to correlate
               an individual request.
               To assist with debugging, you can use this ID to identify and inspect only
               one request that was made as part of a bulk operation.
        :param int status_code: (optional) The HTTP response status code.
        :param Rule rule: (optional) Information about a newly-created rule.
               This field will be present for a successful request.
        :param List[RuleResponseError] errors: (optional) The error contents of the
               multi-status response.
               This field will be present for a failed rule request.
        :param str trace: (optional) The UUID that uniquely identifies the request.
               This field will be present for a failed rule request.
        """
        self.request_id = request_id
        self.status_code = status_code
        self.rule = rule
        self.errors = errors
        self.trace = trace

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateRuleResponse':
        """Initialize a CreateRuleResponse object from a json dictionary."""
        args = {}
        if 'request_id' in _dict:
            args['request_id'] = _dict.get('request_id')
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        if 'rule' in _dict:
            args['rule'] = Rule.from_dict(_dict.get('rule'))
        if 'errors' in _dict:
            args['errors'] = [RuleResponseError.from_dict(x) for x in _dict.get('errors')]
        if 'trace' in _dict:
            args['trace'] = _dict.get('trace')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateRuleResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request_id') and self.request_id is not None:
            _dict['request_id'] = self.request_id
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        if hasattr(self, 'rule') and self.rule is not None:
            _dict['rule'] = self.rule.to_dict()
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateRuleResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateRuleResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateRuleResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreateRulesResponse():
    """
    The response associated with a request to create one or more rules.

    :attr List[CreateRuleResponse] rules: An array of rule responses.
    """

    def __init__(self,
                 rules: List['CreateRuleResponse']) -> None:
        """
        Initialize a CreateRulesResponse object.

        :param List[CreateRuleResponse] rules: An array of rule responses.
        """
        self.rules = rules

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateRulesResponse':
        """Initialize a CreateRulesResponse object from a json dictionary."""
        args = {}
        if 'rules' in _dict:
            args['rules'] = [CreateRuleResponse.from_dict(x) for x in _dict.get('rules')]
        else:
            raise ValueError('Required property \'rules\' not present in CreateRulesResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateRulesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rules') and self.rules is not None:
            _dict['rules'] = [x.to_dict() for x in self.rules]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateRulesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateRulesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateRulesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class EnforcementAction():
    """
    EnforcementAction.

    :attr str action: To block a request from completing, use `disallow`. To log the
          request to Activity Tracker with LogDNA, use `audit_log`.
    """

    def __init__(self,
                 action: str) -> None:
        """
        Initialize a EnforcementAction object.

        :param str action: To block a request from completing, use `disallow`. To
               log the request to Activity Tracker with LogDNA, use `audit_log`.
        """
        self.action = action

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnforcementAction':
        """Initialize a EnforcementAction object from a json dictionary."""
        args = {}
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError('Required property \'action\' not present in EnforcementAction JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnforcementAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnforcementAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnforcementAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnforcementAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ActionEnum(str, Enum):
        """
        To block a request from completing, use `disallow`. To log the request to Activity
        Tracker with LogDNA, use `audit_log`.
        """
        AUDIT_LOG = 'audit_log'
        DISALLOW = 'disallow'


class Link():
    """
    A link that is used to paginate through available resources.

    :attr str href: The URL for the first, previous, next, or last page of
          resources.
    """

    def __init__(self,
                 href: str) -> None:
        """
        Initialize a Link object.

        :param str href: The URL for the first, previous, next, or last page of
               resources.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Link':
        """Initialize a Link object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in Link JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Link object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Link object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Link') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Link') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Rule():
    """
    Properties associated with a rule, including both user-settable and server-populated
    properties.

    :attr str account_id: (optional) Your IBM Cloud account ID.
    :attr str name: A human-readable alias to assign to your rule.
    :attr str description: An extended description of your rule.
    :attr str rule_type: (optional) The type of rule. Rules that you create are
          `user_defined`.
    :attr TargetResource target: The properties that describe the resource that you
          want to target
          with the rule.
    :attr RuleRequiredConfig required_config:
    :attr List[EnforcementAction] enforcement_actions: The actions that the service
          must run on your behalf when a request to create or modify the target resource
          does not comply with your conditions.
    :attr List[str] labels: (optional) Labels that you can use to group and search
          for similar rules, such as those that help you to meet a specific organization
          guideline.
    :attr str rule_id: (optional) The UUID that uniquely identifies the rule.
    :attr datetime creation_date: (optional) The date the resource was created.
    :attr str created_by: (optional) The unique identifier for the user or
          application that created the resource.
    :attr datetime modification_date: (optional) The date the resource was last
          modified.
    :attr str modified_by: (optional) The unique identifier for the user or
          application that last modified the resource.
    :attr int number_of_attachments: (optional) The number of scope attachments that
          are associated with the rule.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 target: 'TargetResource',
                 required_config: 'RuleRequiredConfig',
                 enforcement_actions: List['EnforcementAction'],
                 *,
                 account_id: str = None,
                 rule_type: str = None,
                 labels: List[str] = None,
                 rule_id: str = None,
                 creation_date: datetime = None,
                 created_by: str = None,
                 modification_date: datetime = None,
                 modified_by: str = None,
                 number_of_attachments: int = None) -> None:
        """
        Initialize a Rule object.

        :param str name: A human-readable alias to assign to your rule.
        :param str description: An extended description of your rule.
        :param TargetResource target: The properties that describe the resource
               that you want to target
               with the rule.
        :param RuleRequiredConfig required_config:
        :param List[EnforcementAction] enforcement_actions: The actions that the
               service must run on your behalf when a request to create or modify the
               target resource does not comply with your conditions.
        :param str account_id: (optional) Your IBM Cloud account ID.
        :param str rule_type: (optional) The type of rule. Rules that you create
               are `user_defined`.
        :param List[str] labels: (optional) Labels that you can use to group and
               search for similar rules, such as those that help you to meet a specific
               organization guideline.
        """
        self.account_id = account_id
        self.name = name
        self.description = description
        self.rule_type = rule_type
        self.target = target
        self.required_config = required_config
        self.enforcement_actions = enforcement_actions
        self.labels = labels
        self.rule_id = rule_id
        self.creation_date = creation_date
        self.created_by = created_by
        self.modification_date = modification_date
        self.modified_by = modified_by
        self.number_of_attachments = number_of_attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Rule':
        """Initialize a Rule object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Rule JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in Rule JSON')
        if 'rule_type' in _dict:
            args['rule_type'] = _dict.get('rule_type')
        if 'target' in _dict:
            args['target'] = TargetResource.from_dict(_dict.get('target'))
        else:
            raise ValueError('Required property \'target\' not present in Rule JSON')
        if 'required_config' in _dict:
            args['required_config'] = _dict.get('required_config')
        else:
            raise ValueError('Required property \'required_config\' not present in Rule JSON')
        if 'enforcement_actions' in _dict:
            args['enforcement_actions'] = [EnforcementAction.from_dict(x) for x in _dict.get('enforcement_actions')]
        else:
            raise ValueError('Required property \'enforcement_actions\' not present in Rule JSON')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        if 'rule_id' in _dict:
            args['rule_id'] = _dict.get('rule_id')
        if 'creation_date' in _dict:
            args['creation_date'] = string_to_datetime(_dict.get('creation_date'))
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'modification_date' in _dict:
            args['modification_date'] = string_to_datetime(_dict.get('modification_date'))
        if 'modified_by' in _dict:
            args['modified_by'] = _dict.get('modified_by')
        if 'number_of_attachments' in _dict:
            args['number_of_attachments'] = _dict.get('number_of_attachments')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Rule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'rule_type') and self.rule_type is not None:
            _dict['rule_type'] = self.rule_type
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target.to_dict()
        if hasattr(self, 'required_config') and self.required_config is not None:
            if isinstance(self.required_config, dict):
                _dict['required_config'] = self.required_config
            else:
                _dict['required_config'] = self.required_config.to_dict()
        if hasattr(self, 'enforcement_actions') and self.enforcement_actions is not None:
            _dict['enforcement_actions'] = [x.to_dict() for x in self.enforcement_actions]
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        if hasattr(self, 'rule_id') and getattr(self, 'rule_id') is not None:
            _dict['rule_id'] = getattr(self, 'rule_id')
        if hasattr(self, 'creation_date') and getattr(self, 'creation_date') is not None:
            _dict['creation_date'] = datetime_to_string(getattr(self, 'creation_date'))
        if hasattr(self, 'created_by') and getattr(self, 'created_by') is not None:
            _dict['created_by'] = getattr(self, 'created_by')
        if hasattr(self, 'modification_date') and getattr(self, 'modification_date') is not None:
            _dict['modification_date'] = datetime_to_string(getattr(self, 'modification_date'))
        if hasattr(self, 'modified_by') and getattr(self, 'modified_by') is not None:
            _dict['modified_by'] = getattr(self, 'modified_by')
        if hasattr(self, 'number_of_attachments') and getattr(self, 'number_of_attachments') is not None:
            _dict['number_of_attachments'] = getattr(self, 'number_of_attachments')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Rule object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Rule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Rule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class RuleTypeEnum(str, Enum):
        """
        The type of rule. Rules that you create are `user_defined`.
        """
        USER_DEFINED = 'user_defined'


class RuleCondition():
    """
    RuleCondition.

    """

    def __init__(self) -> None:
        """
        Initialize a RuleCondition object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['RuleConditionSingleProperty', 'RuleConditionOrLvl2', 'RuleConditionAndLvl2']))
        raise Exception(msg)

class RuleList():
    """
    A list of rules.

    :attr int offset: The requested offset for the returned items.
    :attr int limit: The requested limit for the returned items.
    :attr int total_count: The total number of available items.
    :attr Link first: The first page of available items.
    :attr Link last: The last page of available items.
    :attr List[Rule] rules: An array of rules.
    """

    def __init__(self,
                 offset: int,
                 limit: int,
                 total_count: int,
                 first: 'Link',
                 last: 'Link',
                 rules: List['Rule']) -> None:
        """
        Initialize a RuleList object.

        :param int offset: The requested offset for the returned items.
        :param int limit: The requested limit for the returned items.
        :param int total_count: The total number of available items.
        :param Link first: The first page of available items.
        :param Link last: The last page of available items.
        :param List[Rule] rules: An array of rules.
        """
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.last = last
        self.rules = rules

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleList':
        """Initialize a RuleList object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in RuleList JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in RuleList JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in RuleList JSON')
        if 'first' in _dict:
            args['first'] = Link.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in RuleList JSON')
        if 'last' in _dict:
            args['last'] = Link.from_dict(_dict.get('last'))
        else:
            raise ValueError('Required property \'last\' not present in RuleList JSON')
        if 'rules' in _dict:
            args['rules'] = [Rule.from_dict(x) for x in _dict.get('rules')]
        else:
            raise ValueError('Required property \'rules\' not present in RuleList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'rules') and self.rules is not None:
            _dict['rules'] = [x.to_dict() for x in self.rules]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RuleRequest():
    """
    User-settable properties associated with a rule to be created or updated.

    :attr str account_id: (optional) Your IBM Cloud account ID.
    :attr str name: A human-readable alias to assign to your rule.
    :attr str description: An extended description of your rule.
    :attr str rule_type: (optional) The type of rule. Rules that you create are
          `user_defined`.
    :attr TargetResource target: The properties that describe the resource that you
          want to target
          with the rule.
    :attr RuleRequiredConfig required_config:
    :attr List[EnforcementAction] enforcement_actions: The actions that the service
          must run on your behalf when a request to create or modify the target resource
          does not comply with your conditions.
    :attr List[str] labels: (optional) Labels that you can use to group and search
          for similar rules, such as those that help you to meet a specific organization
          guideline.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 target: 'TargetResource',
                 required_config: 'RuleRequiredConfig',
                 enforcement_actions: List['EnforcementAction'],
                 *,
                 account_id: str = None,
                 rule_type: str = None,
                 labels: List[str] = None) -> None:
        """
        Initialize a RuleRequest object.

        :param str name: A human-readable alias to assign to your rule.
        :param str description: An extended description of your rule.
        :param TargetResource target: The properties that describe the resource
               that you want to target
               with the rule.
        :param RuleRequiredConfig required_config:
        :param List[EnforcementAction] enforcement_actions: The actions that the
               service must run on your behalf when a request to create or modify the
               target resource does not comply with your conditions.
        :param str account_id: (optional) Your IBM Cloud account ID.
        :param str rule_type: (optional) The type of rule. Rules that you create
               are `user_defined`.
        :param List[str] labels: (optional) Labels that you can use to group and
               search for similar rules, such as those that help you to meet a specific
               organization guideline.
        """
        self.account_id = account_id
        self.name = name
        self.description = description
        self.rule_type = rule_type
        self.target = target
        self.required_config = required_config
        self.enforcement_actions = enforcement_actions
        self.labels = labels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleRequest':
        """Initialize a RuleRequest object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in RuleRequest JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in RuleRequest JSON')
        if 'rule_type' in _dict:
            args['rule_type'] = _dict.get('rule_type')
        if 'target' in _dict:
            args['target'] = TargetResource.from_dict(_dict.get('target'))
        else:
            raise ValueError('Required property \'target\' not present in RuleRequest JSON')
        if 'required_config' in _dict:
            args['required_config'] = _dict.get('required_config')
        else:
            raise ValueError('Required property \'required_config\' not present in RuleRequest JSON')
        if 'enforcement_actions' in _dict:
            args['enforcement_actions'] = [EnforcementAction.from_dict(x) for x in _dict.get('enforcement_actions')]
        else:
            raise ValueError('Required property \'enforcement_actions\' not present in RuleRequest JSON')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'rule_type') and self.rule_type is not None:
            _dict['rule_type'] = self.rule_type
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target.to_dict()
        if hasattr(self, 'required_config') and self.required_config is not None:
            if isinstance(self.required_config, dict):
                _dict['required_config'] = self.required_config
            else:
                _dict['required_config'] = self.required_config.to_dict()
        if hasattr(self, 'enforcement_actions') and self.enforcement_actions is not None:
            _dict['enforcement_actions'] = [x.to_dict() for x in self.enforcement_actions]
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class RuleTypeEnum(str, Enum):
        """
        The type of rule. Rules that you create are `user_defined`.
        """
        USER_DEFINED = 'user_defined'


class RuleRequiredConfig():
    """
    RuleRequiredConfig.

    """

    def __init__(self) -> None:
        """
        Initialize a RuleRequiredConfig object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['RuleRequiredConfigSingleProperty', 'RuleRequiredConfigMultipleProperties']))
        raise Exception(msg)

class RuleResponseError():
    """
    RuleResponseError.

    :attr str code: Specifies the problem that caused the error.
    :attr str message: Describes the problem.
    """

    def __init__(self,
                 code: str,
                 message: str) -> None:
        """
        Initialize a RuleResponseError object.

        :param str code: Specifies the problem that caused the error.
        :param str message: Describes the problem.
        """
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleResponseError':
        """Initialize a RuleResponseError object from a json dictionary."""
        args = {}
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        else:
            raise ValueError('Required property \'code\' not present in RuleResponseError JSON')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError('Required property \'message\' not present in RuleResponseError JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleResponseError object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleResponseError object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleResponseError') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleResponseError') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RuleScope():
    """
    The extent at which the rule can be attached across your accounts.

    :attr str note: (optional) A short description or alias to assign to the scope.
    :attr str scope_id: The ID of the scope, such as an enterprise, account, or
          account group, that you want to evaluate.
    :attr str scope_type: The type of scope that you want to evaluate.
    """

    def __init__(self,
                 scope_id: str,
                 scope_type: str,
                 *,
                 note: str = None) -> None:
        """
        Initialize a RuleScope object.

        :param str scope_id: The ID of the scope, such as an enterprise, account,
               or account group, that you want to evaluate.
        :param str scope_type: The type of scope that you want to evaluate.
        :param str note: (optional) A short description or alias to assign to the
               scope.
        """
        self.note = note
        self.scope_id = scope_id
        self.scope_type = scope_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleScope':
        """Initialize a RuleScope object from a json dictionary."""
        args = {}
        if 'note' in _dict:
            args['note'] = _dict.get('note')
        if 'scope_id' in _dict:
            args['scope_id'] = _dict.get('scope_id')
        else:
            raise ValueError('Required property \'scope_id\' not present in RuleScope JSON')
        if 'scope_type' in _dict:
            args['scope_type'] = _dict.get('scope_type')
        else:
            raise ValueError('Required property \'scope_type\' not present in RuleScope JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleScope object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'note') and self.note is not None:
            _dict['note'] = self.note
        if hasattr(self, 'scope_id') and self.scope_id is not None:
            _dict['scope_id'] = self.scope_id
        if hasattr(self, 'scope_type') and self.scope_type is not None:
            _dict['scope_type'] = self.scope_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleScope object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleScope') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleScope') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ScopeTypeEnum(str, Enum):
        """
        The type of scope that you want to evaluate.
        """
        ENTERPRISE = 'enterprise'
        ENTERPRISE_ACCOUNT_GROUP = 'enterprise.account_group'
        ENTERPRISE_ACCOUNT = 'enterprise.account'
        ACCOUNT = 'account'
        ACCOUNT_RESOURCE_GROUP = 'account.resource_group'


class RuleSingleProperty():
    """
    The requirement that must be met to determine the resource's level of compliance in
    accordance with the rule.
    To apply a single property check, define a configuration property and the desired
    value that you want to check against.

    :attr str description: (optional)
    :attr str property: A resource configuration variable that describes the
          property that you want to apply to the target resource.
          Available options depend on the target service and resource.
    :attr str operator: The way in which the `property` field is compared to its
          value.
          There are three types of operators: string, numeric, and boolean.
    :attr str value: (optional) The way in which you want your property to be
          applied.
          Value options differ depending on the rule that you configure. If you use a
          boolean operator, you do not need to input a value.
    """

    def __init__(self,
                 property: str,
                 operator: str,
                 *,
                 description: str = None,
                 value: str = None) -> None:
        """
        Initialize a RuleSingleProperty object.

        :param str property: A resource configuration variable that describes the
               property that you want to apply to the target resource.
               Available options depend on the target service and resource.
        :param str operator: The way in which the `property` field is compared to
               its value.
               There are three types of operators: string, numeric, and boolean.
        :param str description: (optional)
        :param str value: (optional) The way in which you want your property to be
               applied.
               Value options differ depending on the rule that you configure. If you use a
               boolean operator, you do not need to input a value.
        """
        self.description = description
        self.property = property
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleSingleProperty':
        """Initialize a RuleSingleProperty object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'property' in _dict:
            args['property'] = _dict.get('property')
        else:
            raise ValueError('Required property \'property\' not present in RuleSingleProperty JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in RuleSingleProperty JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleSingleProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'property') and self.property is not None:
            _dict['property'] = self.property
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleSingleProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleSingleProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleSingleProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The way in which the `property` field is compared to its value.
        There are three types of operators: string, numeric, and boolean.
        """
        IS_TRUE = 'is_true'
        IS_FALSE = 'is_false'
        IS_EMPTY = 'is_empty'
        IS_NOT_EMPTY = 'is_not_empty'
        STRING_EQUALS = 'string_equals'
        STRING_NOT_EQUALS = 'string_not_equals'
        STRING_MATCH = 'string_match'
        STRING_NOT_MATCH = 'string_not_match'
        NUM_EQUALS = 'num_equals'
        NUM_NOT_EQUALS = 'num_not_equals'
        NUM_LESS_THAN = 'num_less_than'
        NUM_LESS_THAN_EQUALS = 'num_less_than_equals'
        NUM_GREATER_THAN = 'num_greater_than'
        NUM_GREATER_THAN_EQUALS = 'num_greater_than_equals'
        IPS_IN_RANGE = 'ips_in_range'
        STRINGS_IN_LIST = 'strings_in_list'


class RuleTargetAttribute():
    """
    The attributes that are associated with a rule target.

    :attr str name:
    :attr str operator: The way in which the `name` field is compared to its value.
          There are three types of operators: string, numeric, and boolean.
    :attr str value: (optional) The way in which you want your property to be
          applied.
          Value options differ depending on the rule that you configure. If you use a
          boolean operator, you do not need to input a value.
    """

    def __init__(self,
                 name: str,
                 operator: str,
                 *,
                 value: str = None) -> None:
        """
        Initialize a RuleTargetAttribute object.

        :param str name:
        :param str operator: The way in which the `name` field is compared to its
               value.
               There are three types of operators: string, numeric, and boolean.
        :param str value: (optional) The way in which you want your property to be
               applied.
               Value options differ depending on the rule that you configure. If you use a
               boolean operator, you do not need to input a value.
        """
        self.name = name
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleTargetAttribute':
        """Initialize a RuleTargetAttribute object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in RuleTargetAttribute JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in RuleTargetAttribute JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleTargetAttribute object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleTargetAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleTargetAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleTargetAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The way in which the `name` field is compared to its value.
        There are three types of operators: string, numeric, and boolean.
        """
        STRING_EQUALS = 'string_equals'
        STRING_NOT_EQUALS = 'string_not_equals'
        STRING_MATCH = 'string_match'
        STRING_NOT_MATCH = 'string_not_match'
        NUM_EQUALS = 'num_equals'
        NUM_NOT_EQUALS = 'num_not_equals'
        NUM_LESS_THAN = 'num_less_than'
        NUM_LESS_THAN_EQUALS = 'num_less_than_equals'
        NUM_GREATER_THAN = 'num_greater_than'
        NUM_GREATER_THAN_EQUALS = 'num_greater_than_equals'
        IS_EMPTY = 'is_empty'
        IS_NOT_EMPTY = 'is_not_empty'
        IS_TRUE = 'is_true'
        IS_FALSE = 'is_false'
        IPS_IN_RANGE = 'ips_in_range'
        STRINGS_IN_LIST = 'strings_in_list'


class TargetResource():
    """
    The properties that describe the resource that you want to target with the rule.

    :attr str service_name: The programmatic name of the IBM Cloud service that you
          want to target with the rule.
    :attr str resource_kind: The type of resource that you want to target.
    :attr List[RuleTargetAttribute] additional_target_attributes: (optional) An
          extra qualifier for the resource kind. When you include additional attributes,
          only the resources that match the definition are included in the rule.
    """

    def __init__(self,
                 service_name: str,
                 resource_kind: str,
                 *,
                 additional_target_attributes: List['RuleTargetAttribute'] = None) -> None:
        """
        Initialize a TargetResource object.

        :param str service_name: The programmatic name of the IBM Cloud service
               that you want to target with the rule.
        :param str resource_kind: The type of resource that you want to target.
        :param List[RuleTargetAttribute] additional_target_attributes: (optional)
               An extra qualifier for the resource kind. When you include additional
               attributes, only the resources that match the definition are included in
               the rule.
        """
        self.service_name = service_name
        self.resource_kind = resource_kind
        self.additional_target_attributes = additional_target_attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetResource':
        """Initialize a TargetResource object from a json dictionary."""
        args = {}
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        else:
            raise ValueError('Required property \'service_name\' not present in TargetResource JSON')
        if 'resource_kind' in _dict:
            args['resource_kind'] = _dict.get('resource_kind')
        else:
            raise ValueError('Required property \'resource_kind\' not present in TargetResource JSON')
        if 'additional_target_attributes' in _dict:
            args['additional_target_attributes'] = [RuleTargetAttribute.from_dict(x) for x in _dict.get('additional_target_attributes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'resource_kind') and self.resource_kind is not None:
            _dict['resource_kind'] = self.resource_kind
        if hasattr(self, 'additional_target_attributes') and self.additional_target_attributes is not None:
            _dict['additional_target_attributes'] = [x.to_dict() for x in self.additional_target_attributes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TargetResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TargetResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TargetResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RuleConditionAndLvl2(RuleCondition):
    """
    A condition with the `and` logical operator.

    :attr str description: (optional)
    :attr List[RuleSingleProperty] and_:
    """

    def __init__(self,
                 and_: List['RuleSingleProperty'],
                 *,
                 description: str = None) -> None:
        """
        Initialize a RuleConditionAndLvl2 object.

        :param List[RuleSingleProperty] and_:
        :param str description: (optional)
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.and_ = and_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleConditionAndLvl2':
        """Initialize a RuleConditionAndLvl2 object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'and' in _dict:
            args['and_'] = [RuleSingleProperty.from_dict(x) for x in _dict.get('and')]
        else:
            raise ValueError('Required property \'and\' not present in RuleConditionAndLvl2 JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleConditionAndLvl2 object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'and_') and self.and_ is not None:
            _dict['and'] = [x.to_dict() for x in self.and_]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleConditionAndLvl2 object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleConditionAndLvl2') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleConditionAndLvl2') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RuleConditionOrLvl2(RuleCondition):
    """
    A condition with the `or` logical operator.

    :attr str description: (optional)
    :attr List[RuleSingleProperty] or_:
    """

    def __init__(self,
                 or_: List['RuleSingleProperty'],
                 *,
                 description: str = None) -> None:
        """
        Initialize a RuleConditionOrLvl2 object.

        :param List[RuleSingleProperty] or_:
        :param str description: (optional)
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.or_ = or_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleConditionOrLvl2':
        """Initialize a RuleConditionOrLvl2 object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'or' in _dict:
            args['or_'] = [RuleSingleProperty.from_dict(x) for x in _dict.get('or')]
        else:
            raise ValueError('Required property \'or\' not present in RuleConditionOrLvl2 JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleConditionOrLvl2 object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'or_') and self.or_ is not None:
            _dict['or'] = [x.to_dict() for x in self.or_]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleConditionOrLvl2 object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleConditionOrLvl2') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleConditionOrLvl2') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RuleConditionSingleProperty(RuleCondition):
    """
    The requirement that must be met to determine the resource's level of compliance in
    accordance with the rule.
    To apply a single property check, define a configuration property and the desired
    value that you want to check against.

    :attr str description: (optional)
    :attr str property: A resource configuration variable that describes the
          property that you want to apply to the target resource.
          Available options depend on the target service and resource.
    :attr str operator: The way in which the `property` field is compared to its
          value.
          There are three types of operators: string, numeric, and boolean.
    :attr str value: (optional) The way in which you want your property to be
          applied.
          Value options differ depending on the rule that you configure. If you use a
          boolean operator, you do not need to input a value.
    """

    def __init__(self,
                 property: str,
                 operator: str,
                 *,
                 description: str = None,
                 value: str = None) -> None:
        """
        Initialize a RuleConditionSingleProperty object.

        :param str property: A resource configuration variable that describes the
               property that you want to apply to the target resource.
               Available options depend on the target service and resource.
        :param str operator: The way in which the `property` field is compared to
               its value.
               There are three types of operators: string, numeric, and boolean.
        :param str description: (optional)
        :param str value: (optional) The way in which you want your property to be
               applied.
               Value options differ depending on the rule that you configure. If you use a
               boolean operator, you do not need to input a value.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.property = property
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleConditionSingleProperty':
        """Initialize a RuleConditionSingleProperty object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'property' in _dict:
            args['property'] = _dict.get('property')
        else:
            raise ValueError('Required property \'property\' not present in RuleConditionSingleProperty JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in RuleConditionSingleProperty JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleConditionSingleProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'property') and self.property is not None:
            _dict['property'] = self.property
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleConditionSingleProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleConditionSingleProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleConditionSingleProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The way in which the `property` field is compared to its value.
        There are three types of operators: string, numeric, and boolean.
        """
        IS_TRUE = 'is_true'
        IS_FALSE = 'is_false'
        IS_EMPTY = 'is_empty'
        IS_NOT_EMPTY = 'is_not_empty'
        STRING_EQUALS = 'string_equals'
        STRING_NOT_EQUALS = 'string_not_equals'
        STRING_MATCH = 'string_match'
        STRING_NOT_MATCH = 'string_not_match'
        NUM_EQUALS = 'num_equals'
        NUM_NOT_EQUALS = 'num_not_equals'
        NUM_LESS_THAN = 'num_less_than'
        NUM_LESS_THAN_EQUALS = 'num_less_than_equals'
        NUM_GREATER_THAN = 'num_greater_than'
        NUM_GREATER_THAN_EQUALS = 'num_greater_than_equals'
        IPS_IN_RANGE = 'ips_in_range'
        STRINGS_IN_LIST = 'strings_in_list'


class RuleRequiredConfigMultipleProperties(RuleRequiredConfig):
    """
    The requirements that must be met to determine the resource's level of compliance in
    accordance with the rule.
    Use logical operators (`and`/`or`) to define multiple property checks and conditions.
    To define requirements for a rule, list one or more property check objects in the
    `and` array. To add conditions to a property check, use `or`.

    """

    def __init__(self) -> None:
        """
        Initialize a RuleRequiredConfigMultipleProperties object.

        """
        # pylint: disable=super-init-not-called
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['RuleRequiredConfigMultiplePropertiesConditionOr', 'RuleRequiredConfigMultiplePropertiesConditionAnd']))
        raise Exception(msg)

class RuleRequiredConfigSingleProperty(RuleRequiredConfig):
    """
    The requirement that must be met to determine the resource's level of compliance in
    accordance with the rule.
    To apply a single property check, define a configuration property and the desired
    value that you want to check against.

    :attr str description: (optional)
    :attr str property: A resource configuration variable that describes the
          property that you want to apply to the target resource.
          Available options depend on the target service and resource.
    :attr str operator: The way in which the `property` field is compared to its
          value.
          There are three types of operators: string, numeric, and boolean.
    :attr str value: (optional) The way in which you want your property to be
          applied.
          Value options differ depending on the rule that you configure. If you use a
          boolean operator, you do not need to input a value.
    """

    def __init__(self,
                 property: str,
                 operator: str,
                 *,
                 description: str = None,
                 value: str = None) -> None:
        """
        Initialize a RuleRequiredConfigSingleProperty object.

        :param str property: A resource configuration variable that describes the
               property that you want to apply to the target resource.
               Available options depend on the target service and resource.
        :param str operator: The way in which the `property` field is compared to
               its value.
               There are three types of operators: string, numeric, and boolean.
        :param str description: (optional)
        :param str value: (optional) The way in which you want your property to be
               applied.
               Value options differ depending on the rule that you configure. If you use a
               boolean operator, you do not need to input a value.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.property = property
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleRequiredConfigSingleProperty':
        """Initialize a RuleRequiredConfigSingleProperty object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'property' in _dict:
            args['property'] = _dict.get('property')
        else:
            raise ValueError('Required property \'property\' not present in RuleRequiredConfigSingleProperty JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in RuleRequiredConfigSingleProperty JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleRequiredConfigSingleProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'property') and self.property is not None:
            _dict['property'] = self.property
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleRequiredConfigSingleProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleRequiredConfigSingleProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleRequiredConfigSingleProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The way in which the `property` field is compared to its value.
        There are three types of operators: string, numeric, and boolean.
        """
        IS_TRUE = 'is_true'
        IS_FALSE = 'is_false'
        IS_EMPTY = 'is_empty'
        IS_NOT_EMPTY = 'is_not_empty'
        STRING_EQUALS = 'string_equals'
        STRING_NOT_EQUALS = 'string_not_equals'
        STRING_MATCH = 'string_match'
        STRING_NOT_MATCH = 'string_not_match'
        NUM_EQUALS = 'num_equals'
        NUM_NOT_EQUALS = 'num_not_equals'
        NUM_LESS_THAN = 'num_less_than'
        NUM_LESS_THAN_EQUALS = 'num_less_than_equals'
        NUM_GREATER_THAN = 'num_greater_than'
        NUM_GREATER_THAN_EQUALS = 'num_greater_than_equals'
        IPS_IN_RANGE = 'ips_in_range'
        STRINGS_IN_LIST = 'strings_in_list'


class RuleRequiredConfigMultiplePropertiesConditionAnd(RuleRequiredConfigMultipleProperties):
    """
    A condition with the `and` logical operator.

    :attr str description: (optional)
    :attr List[RuleCondition] and_:
    """

    def __init__(self,
                 and_: List['RuleCondition'],
                 *,
                 description: str = None) -> None:
        """
        Initialize a RuleRequiredConfigMultiplePropertiesConditionAnd object.

        :param List[RuleCondition] and_:
        :param str description: (optional)
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.and_ = and_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleRequiredConfigMultiplePropertiesConditionAnd':
        """Initialize a RuleRequiredConfigMultiplePropertiesConditionAnd object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'and' in _dict:
            args['and_'] = _dict.get('and')
        else:
            raise ValueError('Required property \'and\' not present in RuleRequiredConfigMultiplePropertiesConditionAnd JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleRequiredConfigMultiplePropertiesConditionAnd object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'and_') and self.and_ is not None:
            and_list = []
            for x in self.and_:
                if isinstance(x, dict):
                    and_list.append(x)
                else:
                    and_list.append(x.to_dict())
            _dict['and'] = and_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleRequiredConfigMultiplePropertiesConditionAnd object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleRequiredConfigMultiplePropertiesConditionAnd') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleRequiredConfigMultiplePropertiesConditionAnd') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RuleRequiredConfigMultiplePropertiesConditionOr(RuleRequiredConfigMultipleProperties):
    """
    A condition with the `or` logical operator.

    :attr str description: (optional)
    :attr List[RuleCondition] or_:
    """

    def __init__(self,
                 or_: List['RuleCondition'],
                 *,
                 description: str = None) -> None:
        """
        Initialize a RuleRequiredConfigMultiplePropertiesConditionOr object.

        :param List[RuleCondition] or_:
        :param str description: (optional)
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.or_ = or_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleRequiredConfigMultiplePropertiesConditionOr':
        """Initialize a RuleRequiredConfigMultiplePropertiesConditionOr object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'or' in _dict:
            args['or_'] = _dict.get('or')
        else:
            raise ValueError('Required property \'or\' not present in RuleRequiredConfigMultiplePropertiesConditionOr JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleRequiredConfigMultiplePropertiesConditionOr object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'or_') and self.or_ is not None:
            or_list = []
            for x in self.or_:
                if isinstance(x, dict):
                    or_list.append(x)
                else:
                    or_list.append(x.to_dict())
            _dict['or'] = or_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleRequiredConfigMultiplePropertiesConditionOr object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleRequiredConfigMultiplePropertiesConditionOr') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleRequiredConfigMultiplePropertiesConditionOr') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
