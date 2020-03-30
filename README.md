# IBM Cloud Platform Services Python SDK Version 0.3.0
[![Build Status](https://travis.ibm.com/ibmcloud/platform-services-python-sdk.svg?token=eW5FVD71iyte6tTby8gr&branch=master)](https://travis.ibm.com/ibmcloud/platform-services-python-sdk)

Python client library to interact with various [IBM Cloud Platform Service APIs](https://cloud.ibm.com/apidocs?category=platform_services).

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
[Enterprise Management](https://cloud.ibm.com/apidocs/enterprise-apis/enterprise) | EnterpriseManagementV1
[Enterprise Usage Reports](https://cloud.ibm.com/apidocs/enterprise-apis/resource-usage-reports) | EnterpriseUsagereportsV1
[Global Resource Catalog](https://cloud.ibm.com/apidocs/globalcatalog) | GlobalCatalogV1
[Global Search](https://cloud.ibm.com/apidocs/search) | GlobalSearchV2
[Global Tagging](https://cloud.ibm.com/apidocs/tagging) | GlobalTaggingV1
[IAM Access Groups](https://cloud.ibm.com/apidocs/iam-access-groups) | IamAccessGroupsV2
[IAM Identity Services](https://cloud.ibm.com/apidocs/iam-identity-token-api) | IamIdentityServicesV1
[IAM Policy Management](https://cloud.ibm.com/apidocs/iam-policy-management) | IamPolicyManagementV1
[Open Services Broker](https://cloud.ibm.com/apidocs/resource-controller/ibm-cloud-osb-api) | OpenServiceBrokerB1
[Resource Controller](https://cloud.ibm.com/apidocs/resource-controller) | ResourceControllerV2
[Resource Manager](https://cloud.ibm.com/apidocs/resource-controller/resource-manager) | ResourceManagerV2
[Usage Metering](https://cloud.ibm.com/apidocs/usage-metering) | UsageMeteringV4
[Usage Reports](https://cloud.ibm.com/apidocs/usage-metering) | UsageReportsV1
[User Management](https://cloud.ibm.com/apidocs/user-management) | UserManagementV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration?target=%2Fdeveloper%2Fwatson&

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.5 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "platform_services>=0.3.0"
```

or

```bash
easy_install --upgrade "platform_services>=0.3.0"
```

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md)

## Questions
If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question at [dW Answers](https://developer.ibm.com/answers/questions/ask/?topics=ibm-cloud) or
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.ibm.com/ibmcloud/platform-services-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING](CONTRIBUTING.md).

## License

The IBM Cloud Platform Services Python SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.ibm.com/ibmcloud/platform-services-python-sdk/blob/master/LICENSE).
