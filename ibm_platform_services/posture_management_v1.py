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

# IBM OpenAPI SDK Code Generator Version: 99-SNAPSHOT-b414353e-20210324-135924
 
"""
With IBM Cloud® Security and Compliance Center, you can embed checks into your every day
workflows to help manage your current security and compliance posture. By monitoring for
risks, you can identify security vulnerabilities and quickly work to mitigate the impact.
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class PostureManagementV1(BaseService):
    """The Posture Management V1 service."""

    DEFAULT_SERVICE_URL = None
    DEFAULT_SERVICE_NAME = 'posture_management'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'PostureManagementV1':
        """
        Return a new client for the Posture Management service using the specified
               parameters and external configuration.
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
        Construct a new client for the Posture Management service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Scans
    #########################


    def create_validation(self,
        account_id: str,
        *,
        scope_id: str = None,
        profile_id: str = None,
        group_profile_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Initiate a validations scan.

        Validations scans determine a specified scope's adherence to regulatory controls
        by validating the configuration of the resources in your scope to the attached
        profile. To initiate a scan, you must have configured a collector, provided
        credentials, and completed both a fact collection and discovery scan. [Learn
        more](/docs/security-compliance?topic=security-compliance-schedule-scan).

        :param str account_id: Your IBM Cloud account ID.
        :param str scope_id: (optional) The unique ID of the scope.
        :param str profile_id: (optional) The unique ID of the profile.
        :param str group_profile_id: (optional) The ID of the profile group.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Result` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_validation')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id
        }

        data = {
            'scope_id': scope_id,
            'profile_id': profile_id,
            'group_profile_id': group_profile_id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/posture/v1/scans/validations'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Profiles
    #########################


    def list_profiles(self,
        account_id: str,
        *,
        name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List profiles.

        List all of the profiles that are available in your account. To view a specific
        profile, you can filter by name.

        :param str account_id: Your account ID.
        :param str name: (optional) The name of the profile.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfilesList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_profiles')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'name': name
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/posture/v1/profiles'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Scopes
    #########################


    def list_scopes(self,
        account_id: str,
        *,
        name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List scopes.

        List all of the scopes that are available in your account. To view a specific
        scope, you can filter by name.

        :param str account_id: Your IBM Cloud account ID.
        :param str name: (optional) The name of the scope.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ScopesList` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_scopes')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'name': name
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/posture/v1/scopes'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class ApplicabilityCriteria():
    """
    The criteria that defines how a profile applies.

    :attr List[str] environment: (optional) A list of environments that a profile
          can be applied to.
    :attr List[str] resource: (optional) A list of resources that a profile can be
          used with.
    :attr List[str] environment_category: (optional) The type of environment that a
          profile is able to be applied to.
    :attr List[str] resource_category: (optional) The type of resource that a
          profile is able to be applied to.
    :attr List[str] resource_type: (optional) The resource type that the profile
          applies to.
    :attr object software_details: (optional) The software that the profile applies
          to.
    :attr object os_details: (optional) The operatoring system that the profile
          applies to.
    :attr object additional_details: (optional) Any additional details about the
          profile.
    :attr dict environment_category_description: (optional) The type of environment
          that your scope is targeted to.
    :attr dict environment_description: (optional) The environment that your scope
          is targeted to.
    :attr dict resource_category_description: (optional) The type of resource that
          your scope is targeted to.
    :attr dict resource_type_description: (optional) A further classification of the
          type of resource that your scope is targeted to.
    :attr dict resource_description: (optional) The resource that is scanned as part
          of your scope.
    """

    def __init__(self,
                 *,
                 environment: List[str] = None,
                 resource: List[str] = None,
                 environment_category: List[str] = None,
                 resource_category: List[str] = None,
                 resource_type: List[str] = None,
                 software_details: object = None,
                 os_details: object = None,
                 additional_details: object = None,
                 environment_category_description: dict = None,
                 environment_description: dict = None,
                 resource_category_description: dict = None,
                 resource_type_description: dict = None,
                 resource_description: dict = None) -> None:
        """
        Initialize a ApplicabilityCriteria object.

        :param List[str] environment: (optional) A list of environments that a
               profile can be applied to.
        :param List[str] resource: (optional) A list of resources that a profile
               can be used with.
        :param List[str] environment_category: (optional) The type of environment
               that a profile is able to be applied to.
        :param List[str] resource_category: (optional) The type of resource that a
               profile is able to be applied to.
        :param List[str] resource_type: (optional) The resource type that the
               profile applies to.
        :param object software_details: (optional) The software that the profile
               applies to.
        :param object os_details: (optional) The operatoring system that the
               profile applies to.
        :param object additional_details: (optional) Any additional details about
               the profile.
        :param dict environment_category_description: (optional) The type of
               environment that your scope is targeted to.
        :param dict environment_description: (optional) The environment that your
               scope is targeted to.
        :param dict resource_category_description: (optional) The type of resource
               that your scope is targeted to.
        :param dict resource_type_description: (optional) A further classification
               of the type of resource that your scope is targeted to.
        :param dict resource_description: (optional) The resource that is scanned
               as part of your scope.
        """
        self.environment = environment
        self.resource = resource
        self.environment_category = environment_category
        self.resource_category = resource_category
        self.resource_type = resource_type
        self.software_details = software_details
        self.os_details = os_details
        self.additional_details = additional_details
        self.environment_category_description = environment_category_description
        self.environment_description = environment_description
        self.resource_category_description = resource_category_description
        self.resource_type_description = resource_type_description
        self.resource_description = resource_description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicabilityCriteria':
        """Initialize a ApplicabilityCriteria object from a json dictionary."""
        args = {}
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'resource' in _dict:
            args['resource'] = _dict.get('resource')
        if 'environment_category' in _dict:
            args['environment_category'] = _dict.get('environment_category')
        if 'resource_category' in _dict:
            args['resource_category'] = _dict.get('resource_category')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        if 'software_details' in _dict:
            args['software_details'] = _dict.get('software_details')
        if 'os_details' in _dict:
            args['os_details'] = _dict.get('os_details')
        if 'additional_details' in _dict:
            args['additional_details'] = _dict.get('additional_details')
        if 'environment_category_description' in _dict:
            args['environment_category_description'] = _dict.get('environment_category_description')
        if 'environment_description' in _dict:
            args['environment_description'] = _dict.get('environment_description')
        if 'resource_category_description' in _dict:
            args['resource_category_description'] = _dict.get('resource_category_description')
        if 'resource_type_description' in _dict:
            args['resource_type_description'] = _dict.get('resource_type_description')
        if 'resource_description' in _dict:
            args['resource_description'] = _dict.get('resource_description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicabilityCriteria object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'resource') and self.resource is not None:
            _dict['resource'] = self.resource
        if hasattr(self, 'environment_category') and self.environment_category is not None:
            _dict['environment_category'] = self.environment_category
        if hasattr(self, 'resource_category') and self.resource_category is not None:
            _dict['resource_category'] = self.resource_category
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'software_details') and self.software_details is not None:
            _dict['software_details'] = self.software_details
        if hasattr(self, 'os_details') and self.os_details is not None:
            _dict['os_details'] = self.os_details
        if hasattr(self, 'additional_details') and self.additional_details is not None:
            _dict['additional_details'] = self.additional_details
        if hasattr(self, 'environment_category_description') and self.environment_category_description is not None:
            _dict['environment_category_description'] = self.environment_category_description
        if hasattr(self, 'environment_description') and self.environment_description is not None:
            _dict['environment_description'] = self.environment_description
        if hasattr(self, 'resource_category_description') and self.resource_category_description is not None:
            _dict['resource_category_description'] = self.resource_category_description
        if hasattr(self, 'resource_type_description') and self.resource_type_description is not None:
            _dict['resource_type_description'] = self.resource_type_description
        if hasattr(self, 'resource_description') and self.resource_description is not None:
            _dict['resource_description'] = self.resource_description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApplicabilityCriteria object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApplicabilityCriteria') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApplicabilityCriteria') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Profile():
    """
    Profile.

    :attr str name: (optional) The name of the profile.
    :attr str description: (optional) A description of the profile.
    :attr int version: (optional) The version of the profile.
    :attr str created_by: (optional) The user who created the profile.
    :attr str modified_by: (optional) The user who last modified the profile.
    :attr str reason_for_delete: (optional) A reason that you want to delete a
          profile.
    :attr ApplicabilityCriteria applicability_criteria: (optional) The criteria that
          defines how a profile applies.
    :attr str profile_id: (optional) An auto-generated unique identifying number of
          the profile.
    :attr str base_profile: (optional) The base profile that the controls are pulled
          from.
    :attr str profile_type: (optional) The type of profile.
    :attr datetime created_time: (optional) The time that the profile was created in
          UTC.
    :attr datetime modified_time: (optional) The time that the profile was most
          recently modified in UTC.
    :attr bool enabled: (optional) The profile status. If the profile is enabled,
          the value is true. If the profile is disabled, the value is false.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 description: str = None,
                 version: int = None,
                 created_by: str = None,
                 modified_by: str = None,
                 reason_for_delete: str = None,
                 applicability_criteria: 'ApplicabilityCriteria' = None,
                 profile_id: str = None,
                 base_profile: str = None,
                 profile_type: str = None,
                 created_time: datetime = None,
                 modified_time: datetime = None,
                 enabled: bool = None) -> None:
        """
        Initialize a Profile object.

        :param str name: (optional) The name of the profile.
        :param str description: (optional) A description of the profile.
        :param int version: (optional) The version of the profile.
        :param str created_by: (optional) The user who created the profile.
        :param str modified_by: (optional) The user who last modified the profile.
        :param str reason_for_delete: (optional) A reason that you want to delete a
               profile.
        :param ApplicabilityCriteria applicability_criteria: (optional) The
               criteria that defines how a profile applies.
        :param str profile_id: (optional) An auto-generated unique identifying
               number of the profile.
        :param str base_profile: (optional) The base profile that the controls are
               pulled from.
        :param str profile_type: (optional) The type of profile.
        :param datetime created_time: (optional) The time that the profile was
               created in UTC.
        :param datetime modified_time: (optional) The time that the profile was
               most recently modified in UTC.
        :param bool enabled: (optional) The profile status. If the profile is
               enabled, the value is true. If the profile is disabled, the value is false.
        """
        self.name = name
        self.description = description
        self.version = version
        self.created_by = created_by
        self.modified_by = modified_by
        self.reason_for_delete = reason_for_delete
        self.applicability_criteria = applicability_criteria
        self.profile_id = profile_id
        self.base_profile = base_profile
        self.profile_type = profile_type
        self.created_time = created_time
        self.modified_time = modified_time
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Profile':
        """Initialize a Profile object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'modified_by' in _dict:
            args['modified_by'] = _dict.get('modified_by')
        if 'reason_for_delete' in _dict:
            args['reason_for_delete'] = _dict.get('reason_for_delete')
        if 'applicability_criteria' in _dict:
            args['applicability_criteria'] = ApplicabilityCriteria.from_dict(_dict.get('applicability_criteria'))
        if 'profile_id' in _dict:
            args['profile_id'] = _dict.get('profile_id')
        if 'base_profile' in _dict:
            args['base_profile'] = _dict.get('base_profile')
        if 'profile_type' in _dict:
            args['profile_type'] = _dict.get('profile_type')
        if 'created_time' in _dict:
            args['created_time'] = string_to_datetime(_dict.get('created_time'))
        if 'modified_time' in _dict:
            args['modified_time'] = string_to_datetime(_dict.get('modified_time'))
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Profile object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'modified_by') and self.modified_by is not None:
            _dict['modified_by'] = self.modified_by
        if hasattr(self, 'reason_for_delete') and self.reason_for_delete is not None:
            _dict['reason_for_delete'] = self.reason_for_delete
        if hasattr(self, 'applicability_criteria') and self.applicability_criteria is not None:
            _dict['applicability_criteria'] = self.applicability_criteria.to_dict()
        if hasattr(self, 'profile_id') and self.profile_id is not None:
            _dict['profile_id'] = self.profile_id
        if hasattr(self, 'base_profile') and self.base_profile is not None:
            _dict['base_profile'] = self.base_profile
        if hasattr(self, 'profile_type') and self.profile_type is not None:
            _dict['profile_type'] = self.profile_type
        if hasattr(self, 'created_time') and self.created_time is not None:
            _dict['created_time'] = datetime_to_string(self.created_time)
        if hasattr(self, 'modified_time') and self.modified_time is not None:
            _dict['modified_time'] = datetime_to_string(self.modified_time)
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Profile object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Profile') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Profile') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProfileTypeEnum(str, Enum):
        """
        The type of profile.
        """
        PREDEFINED = 'predefined'
        CUSTOM = 'custom'
        TEMPLATE_GROUP = 'template_group'


class ProfilesList():
    """
    A list of profiles.

    :attr List[Profile] profiles: (optional) Profiles.
    """

    def __init__(self,
                 *,
                 profiles: List['Profile'] = None) -> None:
        """
        Initialize a ProfilesList object.

        :param List[Profile] profiles: (optional) Profiles.
        """
        self.profiles = profiles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfilesList':
        """Initialize a ProfilesList object from a json dictionary."""
        args = {}
        if 'profiles' in _dict:
            args['profiles'] = [Profile.from_dict(x) for x in _dict.get('profiles')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfilesList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'profiles') and self.profiles is not None:
            _dict['profiles'] = [x.to_dict() for x in self.profiles]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfilesList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfilesList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfilesList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Result():
    """
    Result.

    :attr bool result: (optional) Result.
    :attr str message: (optional) A message is returned.
    """

    def __init__(self,
                 *,
                 result: bool = None,
                 message: str = None) -> None:
        """
        Initialize a Result object.

        :param bool result: (optional) Result.
        :param str message: (optional) A message is returned.
        """
        self.result = result
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Result':
        """Initialize a Result object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = _dict.get('result')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Result object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Result object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Result') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Result') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Scan():
    """
    Scan.

    :attr str scan_id: (optional) An auto-generated unique identifier for the scan.
    :attr str discover_id: (optional) An auto-generated unique identifier for
          discovery.
    :attr str status: (optional) The status of the collector as it completes a scan.
    :attr str status_message: (optional) The current status of the collector.
    """

    def __init__(self,
                 *,
                 scan_id: str = None,
                 discover_id: str = None,
                 status: str = None,
                 status_message: str = None) -> None:
        """
        Initialize a Scan object.

        :param str scan_id: (optional) An auto-generated unique identifier for the
               scan.
        :param str discover_id: (optional) An auto-generated unique identifier for
               discovery.
        :param str status: (optional) The status of the collector as it completes a
               scan.
        :param str status_message: (optional) The current status of the collector.
        """
        self.scan_id = scan_id
        self.discover_id = discover_id
        self.status = status
        self.status_message = status_message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Scan':
        """Initialize a Scan object from a json dictionary."""
        args = {}
        if 'scan_id' in _dict:
            args['scan_id'] = _dict.get('scan_id')
        if 'discover_id' in _dict:
            args['discover_id'] = _dict.get('discover_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'status_message' in _dict:
            args['status_message'] = _dict.get('status_message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Scan object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scan_id') and self.scan_id is not None:
            _dict['scan_id'] = self.scan_id
        if hasattr(self, 'discover_id') and self.discover_id is not None:
            _dict['discover_id'] = self.discover_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'status_message') and self.status_message is not None:
            _dict['status_message'] = self.status_message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Scan object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Scan') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Scan') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the collector as it completes a scan.
        """
        PENDING = 'pending'
        DISCOVERY_STARTED = 'discovery_started'
        DISCOVERY_COMPLETED = 'discovery_completed'
        ERROR_IN_DISCOVERY = 'error_in_discovery'
        GATEWAY_ABORTED = 'gateway_aborted'
        CONTROLLER_ABORTED = 'controller_aborted'
        NOT_ACCEPTED = 'not_accepted'
        WAITING_FOR_REFINE = 'waiting_for_refine'
        VALIDATION_STARTED = 'validation_started'
        VALIDATION_COMPLETED = 'validation_completed'
        SENT_TO_COLLECTOR = 'sent_to_collector'
        DISCOVERY_IN_PROGRESS = 'discovery_in_progress'
        VALIDATION_IN_PROGRESS = 'validation_in_progress'
        ERROR_IN_VALIDATION = 'error_in_validation'
        DISCOVERY_RESULT_POSTED_WITH_ERROR = 'discovery_result_posted_with_error'
        DISCOVERY_RESULT_POSTED_NO_ERROR = 'discovery_result_posted_no_error'
        VALIDATION_RESULT_POSTED_WITH_ERROR = 'validation_result_posted_with_error'
        VALIDATION_RESULT_POSTED_NO_ERROR = 'validation_result_posted_no_error'
        FACT_COLLECTION_STARTED = 'fact_collection_started'
        FACT_COLLECTION_IN_PROGRESS = 'fact_collection_in_progress'
        FACT_COLLECTION_COMPLETED = 'fact_collection_completed'
        ERROR_IN_FACT_COLLECTION = 'error_in_fact_collection'
        FACT_VALIDATION_STARTED = 'fact_validation_started'
        FACT_VALIDATION_IN_PROGRESS = 'fact_validation_in_progress'
        FACT_VALIDATION_COMPLETED = 'fact_validation_completed'
        ERROR_IN_FACT_VALIDATION = 'error_in_fact_validation'
        ABORT_TASK_REQUEST_RECEIVED = 'abort_task_request_received'
        ERROR_IN_ABORT_TASK_REQUEST = 'error_in_abort_task_request'
        ABORT_TASK_REQUEST_COMPLETED = 'abort_task_request_completed'
        USER_ABORTED = 'user_aborted'
        ABORT_TASK_REQUEST_FAILED = 'abort_task_request_failed'
        REMEDIATION_STARTED = 'remediation_started'
        REMEDIATION_IN_PROGRESS = 'remediation_in_progress'
        ERROR_IN_REMEDIATION = 'error_in_remediation'
        REMEDIATION_COMPLETED = 'remediation_completed'
        INVENTORY_STARTED = 'inventory_started'
        INVENTORY_IN_PROGRESS = 'inventory_in_progress'
        INVENTORY_COMPLETED = 'inventory_completed'
        ERROR_IN_INVENTORY = 'error_in_inventory'
        INVENTORY_COMPLETED_WITH_ERROR = 'inventory_completed_with_error'


class Scope():
    """
    Scope.

    :attr str description: (optional) A detailed description of the scope.
    :attr str created_by: (optional) The user who created the scope.
    :attr str modified_by: (optional) The user who most recently modified the scope.
    :attr str scope_id: (optional) An auto-generated unique identifier for the
          scope.
    :attr str name: (optional) A unique name for your scope.
    :attr bool enabled: (optional) Indicates whether scope is enabled/disabled.
    :attr str environment_type: (optional) The environment that the scope is
          targeted to.
    :attr datetime created_time: (optional) The time that the scope was created in
          UTC.
    :attr datetime modified_time: (optional) The time that the scope was last
          modified in UTC.
    :attr str last_scan_type: (optional) The last type of scan that was run on the
          scope.
    :attr str last_scan_type_description: (optional) A description of the last scan
          type.
    :attr datetime last_scan_status_updated_time: (optional) The last time that a
          scan status for a scope was updated in UTC.
    :attr List[str] collectors_id: (optional) The unique IDs of the collectors that
          are attached to the scope.
    :attr List[Scan] scans: (optional) A list of the scans that have been run on the
          scope.
    """

    def __init__(self,
                 *,
                 description: str = None,
                 created_by: str = None,
                 modified_by: str = None,
                 scope_id: str = None,
                 name: str = None,
                 enabled: bool = None,
                 environment_type: str = None,
                 created_time: datetime = None,
                 modified_time: datetime = None,
                 last_scan_type: str = None,
                 last_scan_type_description: str = None,
                 last_scan_status_updated_time: datetime = None,
                 collectors_id: List[str] = None,
                 scans: List['Scan'] = None) -> None:
        """
        Initialize a Scope object.

        :param str description: (optional) A detailed description of the scope.
        :param str created_by: (optional) The user who created the scope.
        :param str modified_by: (optional) The user who most recently modified the
               scope.
        :param str scope_id: (optional) An auto-generated unique identifier for the
               scope.
        :param str name: (optional) A unique name for your scope.
        :param bool enabled: (optional) Indicates whether scope is
               enabled/disabled.
        :param str environment_type: (optional) The environment that the scope is
               targeted to.
        :param datetime created_time: (optional) The time that the scope was
               created in UTC.
        :param datetime modified_time: (optional) The time that the scope was last
               modified in UTC.
        :param str last_scan_type: (optional) The last type of scan that was run on
               the scope.
        :param str last_scan_type_description: (optional) A description of the last
               scan type.
        :param datetime last_scan_status_updated_time: (optional) The last time
               that a scan status for a scope was updated in UTC.
        :param List[str] collectors_id: (optional) The unique IDs of the collectors
               that are attached to the scope.
        :param List[Scan] scans: (optional) A list of the scans that have been run
               on the scope.
        """
        self.description = description
        self.created_by = created_by
        self.modified_by = modified_by
        self.scope_id = scope_id
        self.name = name
        self.enabled = enabled
        self.environment_type = environment_type
        self.created_time = created_time
        self.modified_time = modified_time
        self.last_scan_type = last_scan_type
        self.last_scan_type_description = last_scan_type_description
        self.last_scan_status_updated_time = last_scan_status_updated_time
        self.collectors_id = collectors_id
        self.scans = scans

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Scope':
        """Initialize a Scope object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'modified_by' in _dict:
            args['modified_by'] = _dict.get('modified_by')
        if 'scope_id' in _dict:
            args['scope_id'] = _dict.get('scope_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'environment_type' in _dict:
            args['environment_type'] = _dict.get('environment_type')
        if 'created_time' in _dict:
            args['created_time'] = string_to_datetime(_dict.get('created_time'))
        if 'modified_time' in _dict:
            args['modified_time'] = string_to_datetime(_dict.get('modified_time'))
        if 'last_scan_type' in _dict:
            args['last_scan_type'] = _dict.get('last_scan_type')
        if 'last_scan_type_description' in _dict:
            args['last_scan_type_description'] = _dict.get('last_scan_type_description')
        if 'last_scan_status_updated_time' in _dict:
            args['last_scan_status_updated_time'] = string_to_datetime(_dict.get('last_scan_status_updated_time'))
        if 'collectors_id' in _dict:
            args['collectors_id'] = _dict.get('collectors_id')
        if 'scans' in _dict:
            args['scans'] = [Scan.from_dict(x) for x in _dict.get('scans')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Scope object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'modified_by') and self.modified_by is not None:
            _dict['modified_by'] = self.modified_by
        if hasattr(self, 'scope_id') and self.scope_id is not None:
            _dict['scope_id'] = self.scope_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'environment_type') and self.environment_type is not None:
            _dict['environment_type'] = self.environment_type
        if hasattr(self, 'created_time') and self.created_time is not None:
            _dict['created_time'] = datetime_to_string(self.created_time)
        if hasattr(self, 'modified_time') and self.modified_time is not None:
            _dict['modified_time'] = datetime_to_string(self.modified_time)
        if hasattr(self, 'last_scan_type') and self.last_scan_type is not None:
            _dict['last_scan_type'] = self.last_scan_type
        if hasattr(self, 'last_scan_type_description') and self.last_scan_type_description is not None:
            _dict['last_scan_type_description'] = self.last_scan_type_description
        if hasattr(self, 'last_scan_status_updated_time') and self.last_scan_status_updated_time is not None:
            _dict['last_scan_status_updated_time'] = datetime_to_string(self.last_scan_status_updated_time)
        if hasattr(self, 'collectors_id') and self.collectors_id is not None:
            _dict['collectors_id'] = self.collectors_id
        if hasattr(self, 'scans') and self.scans is not None:
            _dict['scans'] = [x.to_dict() for x in self.scans]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Scope object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Scope') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Scope') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class EnvironmentTypeEnum(str, Enum):
        """
        The environment that the scope is targeted to.
        """
        IBM = 'ibm'
        AWS = 'aws'
        AZURE = 'azure'
        ON_PREMISE = 'on_premise'
        HOSTED = 'hosted'
        SERVICES = 'services'
        OPENSTACK = 'openstack'
        GCP = 'gcp'


    class LastScanTypeEnum(str, Enum):
        """
        The last type of scan that was run on the scope.
        """
        DISCOVERY = 'discovery'
        VALIDATION = 'validation'
        FACT_COLLECTION = 'fact_collection'
        FACT_VALIDATION = 'fact_validation'
        INVENTORY = 'inventory'
        REMEDIATION = 'remediation'
        ABORT_TASKS = 'abort_tasks'
        EVIDENCE = 'evidence'
        SCRIPT = 'script'


class ScopesList():
    """
    Scopes list.

    :attr List[Scope] scopes: (optional) Scopes.
    """

    def __init__(self,
                 *,
                 scopes: List['Scope'] = None) -> None:
        """
        Initialize a ScopesList object.

        :param List[Scope] scopes: (optional) Scopes.
        """
        self.scopes = scopes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopesList':
        """Initialize a ScopesList object from a json dictionary."""
        args = {}
        if 'scopes' in _dict:
            args['scopes'] = [Scope.from_dict(x) for x in _dict.get('scopes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopesList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scopes') and self.scopes is not None:
            _dict['scopes'] = [x.to_dict() for x in self.scopes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ScopesList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopesList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopesList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
