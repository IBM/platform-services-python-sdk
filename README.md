[![Build Status](https://github.com/IBM/platform-services-python-sdk/actions/workflows/build.yaml/badge.svg)](https://github.com/IBM/platform-services-python-sdk/actions/workflows/build.yaml)
[![Release](https://img.shields.io/github/v/release/IBM/platform-services-python-sdk)](https://github.com/IBM/platform-services-python-sdk/releases/latest)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ibm-platform-services)](https://pypi.org/project/ibm-platform-services/)
[![PyPI](https://img.shields.io/pypi/v/ibm-platform-services)](https://pypi.org/project/ibm-platform-services/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ibm-platform-services)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
[![CLA assistant](https://cla-assistant.io/readme/badge/IBM/platform-services-python-sdk)](https://cla-assistant.io/IBM/platform-services-python-sdk)


# IBM Cloud Platform Services Python SDK Version 0.68.1

Python client library to interact with various 
[IBM Cloud Platform Service APIs](https://cloud.ibm.com/docs?tab=api-docs&category=platform_services).

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud Platform Services Python SDK allows developers to programmatically interact with the following 
IBM Cloud services:

Service Name | Module Name | Service Class Name
--- | --- | ---
[Case Management](https://cloud.ibm.com/apidocs/case-management?code=python) | case_management_v1 | CaseManagementV1
[Catalog Management](https://cloud.ibm.com/apidocs/resource-catalog/private-catalog?code=python) | catalog_management_v1 | CatalogManagementV1
[Context Based Restrictions](https://cloud.ibm.com/apidocs/context-based-restrictions?code=python) | context_based_restrictions_v1 | ContextBasedRestrictionsV1
[Enterprise Billing Units](https://cloud.ibm.com/apidocs/enterprise-apis/billing-unit?code=python) | enterprise_billing_units_v1 | EnterpriseBillingUnitsV1
[Enterprise Management](https://cloud.ibm.com/apidocs/enterprise-apis/enterprise?code=python) | enterprise_management_v1 | EnterpriseManagementV1
[Enterprise Usage Reports](https://cloud.ibm.com/apidocs/enterprise-apis/resource-usage-reports?code=python) | enterprise_usage_reports_v1 | EnterpriseUsageReportsV1
[Global Catalog](https://cloud.ibm.com/apidocs/resource-catalog/global-catalog?code=python) | global_catalog_v1 | GlobalCatalogV1
[Global Search](https://cloud.ibm.com/apidocs/search?code=python) | global_search_v2 | GlobalSearchV2
[Global Tagging](https://cloud.ibm.com/apidocs/tagging?code=python) | global_tagging_v1 | GlobalTaggingV1
[IAM Access Groups](https://cloud.ibm.com/apidocs/iam-access-groups?code=python) | iam_access_groups_v2 | IamAccessGroupsV2
[IAM Identity Service](https://cloud.ibm.com/apidocs/iam-identity-token-api?code=python) | iam_identity_v1 | IamIdentityV1
[IAM Policy Management](https://cloud.ibm.com/apidocs/iam-policy-management?code=python) | iam_policy_management_v1 | IamPolicyManagementV1
[IBM Cloud Shell](https://cloud.ibm.com/apidocs/cloudshell?code=python) | ibm_cloud_shell_v1 | IbmCloudShellV1
[Open Service Broker](https://cloud.ibm.com/apidocs/resource-controller/ibm-cloud-osb-api?code=python) | open_service_broker_v1 | OpenServiceBrokerV1
[Partner Management APIs](https://cloud.ibm.com/apidocs/partner-apis/partner?code=python) | partner_management_v1 | PartnerManagementV1
[Resource Controller](https://cloud.ibm.com/apidocs/resource-controller/resource-controller?code=python) | resource_controller_v2 | ResourceControllerV2
[Resource Manager](https://cloud.ibm.com/apidocs/resource-controller/resource-manager?code=python) | resource_manager_v2 | ResourceManagerV2
[Usage Metering](https://cloud.ibm.com/apidocs/usage-metering?code=python) | usage_metering_v4 | UsageMeteringV4
[Usage Reports](https://cloud.ibm.com/apidocs/metering-reporting?code=python) | usage_reports_v4 | UsageReportsV4
[User Management](https://cloud.ibm.com/apidocs/user-management?code=python) | user_management_v1 | UserManagementV1

The following services have been relocated to a different SDK project.
Please consult the documentation for each service to determine the new location:

Service Name | Module Name | Service Class Name
--- | --- | ---
[Configuration Governance](https://cloud.ibm.com/apidocs/security-compliance/config?code=python) | configuration_governance_v1 | ConfigurationGovernanceV1
[Posture Management](https://cloud.ibm.com/apidocs/security-compliance/posture?code=python) | posture_management_v1 | PostureManagementV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.9 or above.

## Installation

To install, use `pip`:

```bash
python -m pip install --upgrade ibm-platform-services
```

Then in your code, you can import the appropriate service like this:
```
from ibm_platform_services.<service-module-name> import *
```
where `<service-module-name>` is the service's module name from the table above

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

## Questions
If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question at
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/platform-services-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](https://github.com/IBM/platform-services-python-sdk/blob/main/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.com/IBM/platform-services-python-sdk/blob/main/LICENSE).
