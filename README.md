<div align="center">
        <source srcset="https://user-images.githubusercontent.com/6267663/223574357-9a053550-02f9-49f1-b453-1b11db148d7b.svg" media="(prefers-color-scheme: dark)" width="500">
        <img src="https://user-images.githubusercontent.com/6267663/223574369-77805bfe-6d95-44e8-ac48-f9494101e1dc.svg" width="500">
    <h1>Python SDK</h1>
   <p>AI for everyone.</p>
   <a href="https://dev.writer.com/docs"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/writerai/writer-client-sdk-python/releases"><img src="https://img.shields.io/github/v/release/writerai/writer-client-sdk-python?sort=semver&style=for-the-badge" /></a>
  <a href="https://codespaces.new/writerai/writer-client-sdk-python.git/tree/main"><img src="https://github.com/codespaces/badge.svg" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install writerai
```
<!-- End SDK Installation -->

## Authentication

Writer authenticates your API requests using your account’s API keys. If you do not include your key when making an API request, or use one that is incorrect or outdated, Writer returns an error.

Your API keys are available in the account dashboard. We include randomly generated API keys in our code examples if you are not logged in. Replace these with your own or log in to see code examples populated with your own API keys.

<img width="1070" alt="writer-auth" src="https://user-images.githubusercontent.com/6267663/223578295-89087c24-c55a-48bf-b74a-5f057e21e14f.png">

If you cannot see your secret API keys in the Dashboard, this means you do not have access to them. Contact your Writer account owner and ask to be added to their team as a developer.

## SDK Example Usage
<!-- Start SDK Example Usage -->
### Example

```python
import writer

s = writer.Writer(
    api_key="",
    organization_id=850421,
)


res = s.billing.get_subscription_details()

if res.subscription_public_response_api is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [billing](docs/sdks/billing/README.md)

* [get_subscription_details](docs/sdks/billing/README.md#get_subscription_details) - Get your organization subscription details

### [ai_content_detector](docs/sdks/aicontentdetector/README.md)

* [detect](docs/sdks/aicontentdetector/README.md#detect) - Content detector api

### [content](docs/sdks/content/README.md)

* [check](docs/sdks/content/README.md#check) - Check your content against your preset styleguide.
* [correct](docs/sdks/content/README.md#correct) - Apply the style guide suggestions directly to your content.

### [co_write](docs/sdks/cowrite/README.md)

* [generate_content](docs/sdks/cowrite/README.md#generate_content) - Generate content using predefined templates
* [list_templates](docs/sdks/cowrite/README.md#list_templates) - Get a list of your existing CoWrite templates

### [files](docs/sdks/files/README.md)

* [delete](docs/sdks/files/README.md#delete) - Delete file
* [get](docs/sdks/files/README.md#get) - Get file
* [list](docs/sdks/files/README.md#list) - List files
* [upload](docs/sdks/files/README.md#upload) - Upload file

### [models](docs/sdks/models/README.md)

* [list](docs/sdks/models/README.md#list) - List available LLM models

### [completions](docs/sdks/completions/README.md)

* [create](docs/sdks/completions/README.md#create) - Create completion for LLM model
* [create_model_customization_completion](docs/sdks/completions/README.md#create_model_customization_completion) - Create completion for LLM customization model

### [model_customization](docs/sdks/modelcustomizationsdk/README.md)

* [create](docs/sdks/modelcustomizationsdk/README.md#create) - Create model customization
* [delete](docs/sdks/modelcustomizationsdk/README.md#delete) - Delete Model customization
* [get](docs/sdks/modelcustomizationsdk/README.md#get) - Get model customization
* [list](docs/sdks/modelcustomizationsdk/README.md#list) - List model customizations

### [download_the_customized_model](docs/sdks/downloadthecustomizedmodel/README.md)

* [fetch_file](docs/sdks/downloadthecustomizedmodel/README.md#fetch_file) - Download your fine-tuned model (available only for Palmyra Base and Palmyra Large)

### [document](docs/sdks/documentsdk/README.md)

* [get](docs/sdks/documentsdk/README.md#get) - Get document details
* [list](docs/sdks/documentsdk/README.md#list) - List team documents

### [snippet](docs/sdks/snippet/README.md)

* [delete](docs/sdks/snippet/README.md#delete) - Delete snippets
* [find](docs/sdks/snippet/README.md#find) - Find snippets
* [update](docs/sdks/snippet/README.md#update) - Update snippets

### [styleguide](docs/sdks/styleguide/README.md)

* [get](docs/sdks/styleguide/README.md#get) - Page details
* [list_pages](docs/sdks/styleguide/README.md#list_pages) - List your styleguide pages

### [terminology](docs/sdks/terminology/README.md)

* [add](docs/sdks/terminology/README.md#add) - Add terms
* [delete](docs/sdks/terminology/README.md#delete) - Delete terms
* [find](docs/sdks/terminology/README.md#find) - Find terms
* [update](docs/sdks/terminology/README.md#update) - Update terms

### [user](docs/sdks/user/README.md)

* [list](docs/sdks/user/README.md#list) - List users
<!-- End SDK Available Operations -->


<!-- Start Dev Containers -->
# Dev Containers
<div align="left">
    <a href="https://codespaces.new/writerai/writer-client-sdk-python.git/tree/main"><img src="https://github.com/codespaces/badge.svg" /></a>
    
</div>

Experience our SDK in an enhanced sandbox environment. Try it now in **GitHub Codespaces**!

* [Explore Dev Containers](.devcontainer/README.md)
<!-- End Dev Containers -->

<!-- Start Global Parameters -->
## Global Parameters

A parameter is configured globally. This parameter must be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `organizationId` to `99895` at SDK initialization and then you do not have to pass the same value on calls to operations like `detect`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameter is available. The required parameter must be set when you initialize the SDK client.

| Name | Type | Required | Description |
| ---- | ---- |:--------:| ----------- |
| organizationId | int | ✔️ | The organizationId parameter. |


### Example

```python
import writer

s = writer.Writer(
    api_key="",
    organization_id=496531,
)


res = s.ai_content_detector.detect(content_detector_request=writer.ContentDetectorRequest(
    input='string',
), organization_id=592237)

if res.classes is not None:
    # handle response
    pass
```
<!-- End Global Parameters -->



<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.FailResponseError | 400,401,403,404,500      | application/json         |
| models.SDKError          | 400-600                  | */*                      |

### Example

```python
import writer

s = writer.Writer(
    api_key="",
    organization_id=850421,
)


res = None
try:
    res = s.billing.get_subscription_details()
except (models.FailResponseError) as e:
    print(e) # handle exception

except (models.SDKError) as e:
    print(e) # handle exception


if res.subscription_public_response_api is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://enterprise-api.writer.com` | None |

#### Example

```python
import writer

s = writer.Writer(
    server_idx=0,
    api_key="",
    organization_id=850421,
)


res = s.billing.get_subscription_details()

if res.subscription_public_response_api is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import writer

s = writer.Writer(
    server_url="https://enterprise-api.writer.com",
    api_key="",
    organization_id=850421,
)


res = s.billing.get_subscription_details()

if res.subscription_public_response_api is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import writer
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = writer.Writer(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->

## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type      | Scheme    |
| --------- | --------- | --------- |
| `api_key` | apiKey    | API key   |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
import writer

s = writer.Writer(
    api_key="",
    organization_id=850421,
)


res = s.billing.get_subscription_details()

if res.subscription_public_response_api is not None:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
