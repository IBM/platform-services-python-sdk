[![Build Status](https://travis-ci.com/IBM/platform-services-python-sdk.svg?branch=main)](https://travis-ci.com/IBM/platform-services-python-sdk)
[![Release](https://img.shields.io/github/v/release/IBM/platform-services-python-sdk)](https://github.com/IBM/platform-services-python-sdk/releases/latest)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ibm-platform-services)](https://pypi.org/project/ibm-platform-services/)
[![PyPI](https://img.shields.io/pypi/v/ibm-platform-services)](https://pypi.org/project/ibm-platform-services/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ibm-platform-services)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![codecov](https://codecov.io/gh/IBM/platform-services-python-sdk/branch/main/graph/badge.svg)](https://codecov.io/gh/IBM/platform-services-python-sdk)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

# IBM Cloud Platform Services Python SDK Version 0.17.12

Python client library to interact with various 
[IBM Cloud Platform Service APIs](https://cloud.ibm.com/docs?tab=api-docs&category=platform_services).

Disclaimer: this SDK is being released initially as a **pre-release** version.
Changes might occur which impact applications that use this SDK.

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

Service Name | Imported Class Name
--- | --- 
[Case Management](https://cloud.ibm.com/apidocs/case-management) | CaseManagementV1
[Catalog Management](https://cloud.ibm.com/apidocs/resource-catalog/private-catalog) | CatalogManagementV1
[Configuration Governance](https://cloud.ibm.com/apidocs/security-compliance/config) | ConfigurationGovernanceV1
[Enterprise Billing Units](https://cloud.ibm.com/apidocs/enterprise-apis/billing-unit) | EnterpriseBillingUnitsV1
[Enterprise Management](https://cloud.ibm.com/apidocs/enterprise-apis/enterprise) | EnterpriseManagementV1
[Enterprise Usage Reports](https://cloud.ibm.com/apidocs/enterprise-apis/resource-usage-reports) | EnterpriseUsageReportsV1
[Global Catalog](https://cloud.ibm.com/apidocs/resource-catalog/global-catalog) | GlobalCatalogV1
[Global Search](https://cloud.ibm.com/apidocs/search) | GlobalSearchV2
[Global Tagging](https://cloud.ibm.com/apidocs/tagging) | GlobalTaggingV1
[IAM Access Groups](https://cloud.ibm.com/apidocs/iam-access-groups) | IamAccessGroupsV2
[IAM Identity Service](https://cloud.ibm.com/apidocs/iam-identity-token-api) | IamIdentityV1
[IAM Policy Management](https://cloud.ibm.com/apidocs/iam-policy-management) | IamPolicyManagementV1
[Open Service Broker](https://cloud.ibm.com/apidocs/resource-controller/ibm-cloud-osb-api) | OpenServiceBrokerV1
[Resource Controller](https://cloud.ibm.com/apidocs/resource-controller/resource-controller) | ResourceControllerV2
[Resource Manager](https://cloud.ibm.com/apidocs/resource-controller/resource-manager) | ResourceManagerV2
[Usage Metering](https://cloud.ibm.com/apidocs/usage-metering) | UsageMeteringV4
[Usage Reports](https://cloud.ibm.com/apidocs/metering-reporting) | UsageReportsV4
[User Management](https://cloud.ibm.com/apidocs/user-management) | UserManagementV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.6 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibm-platform-services>=0.17.12"
```

or

```bash
easy_install --upgrade "ibm-platform-services>=0.17.12"
```

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
