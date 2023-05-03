<div align="center">
        <source srcset="https://user-images.githubusercontent.com/6267663/223574357-9a053550-02f9-49f1-b453-1b11db148d7b.svg" media="(prefers-color-scheme: dark)" width="500">
        <img src="https://user-images.githubusercontent.com/6267663/223574369-77805bfe-6d95-44e8-ac48-f9494101e1dc.svg" width="500">
    <h1>Python SDK</h1>
   <p>AI for everyone.</p>
   <a href="https://dev.writer.com/docs"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/writerai/writer-client-sdk-python/releases"><img src="https://img.shields.io/github/v/release/writerai/writer-client-sdk-python?sort=semver&style=for-the-badge" /></a>
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
```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=548814,
)


req = operations.DetectContentRequest(
    content_detector_request=shared.ContentDetectorRequest(
        input='provident',
    ),
)

res = s.ai_content_detector.detect(req)

if res.content_detector_responses is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [ai_content_detector](docs/aicontentdetector/README.md)

* [detect](docs/aicontentdetector/README.md#detect) - Content detector api

### [billing](docs/billing/README.md)

* [get_subscription_details](docs/billing/README.md#get_subscription_details) - Get your organization subscription details

### [co_write](docs/cowrite/README.md)

* [generate_content](docs/cowrite/README.md#generate_content) - Generate content using predefined templates
* [list_templates](docs/cowrite/README.md#list_templates) - Get a list of your existing CoWrite templates

### [completions](docs/completions/README.md)

* [create](docs/completions/README.md#create) - Create completion for LLM model
* [create_model_customization_completion](docs/completions/README.md#create_model_customization_completion) - Create completion for LLM customization model

### [content](docs/content/README.md)

* [check](docs/content/README.md#check) - Check your content against your preset styleguide.
* [correct](docs/content/README.md#correct) - Apply the style guide suggestions directly to your content.

### [download_the_customized_model](docs/downloadthecustomizedmodel/README.md)

* [fetch_file](docs/downloadthecustomizedmodel/README.md#fetch_file) - Download your fine-tuned model (available only for Palmyra Base and Palmyra Large)

### [files](docs/files/README.md)

* [delete](docs/files/README.md#delete) - Delete file
* [get](docs/files/README.md#get) - Get file
* [list](docs/files/README.md#list) - List files
* [upload](docs/files/README.md#upload) - Upload file

### [model_customization](docs/modelcustomization/README.md)

* [create](docs/modelcustomization/README.md#create) - Create model customization
* [delete](docs/modelcustomization/README.md#delete) - Delete Model customization
* [get](docs/modelcustomization/README.md#get) - Get model customization
* [list](docs/modelcustomization/README.md#list) - List model customizations

### [models](docs/models/README.md)

* [list](docs/models/README.md#list) - List available LLM models

### [snippet](docs/snippet/README.md)

* [delete](docs/snippet/README.md#delete) - Delete snippets
* [find](docs/snippet/README.md#find) - Find snippets
* [update](docs/snippet/README.md#update) - Update snippets

### [styleguide](docs/styleguide/README.md)

* [get](docs/styleguide/README.md#get) - Page details
* [list_pages](docs/styleguide/README.md#list_pages) - List your styleguide pages

### [terminology](docs/terminology/README.md)

* [add](docs/terminology/README.md#add) - Add terms
* [delete](docs/terminology/README.md#delete) - Delete terms
* [find](docs/terminology/README.md#find) - Find terms
* [update](docs/terminology/README.md#update) - Update terms

### [user](docs/user/README.md)

* [list](docs/user/README.md#list) - List users
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
