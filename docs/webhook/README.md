# webhook

### Available Operations

* [create_webhook](#create_webhook) - Create a webhook
* [delete_webhook](#delete_webhook) - Delete a webhook
* [get_webhook_by_id](#get_webhook_by_id) - Get a webhook
* [get_webhooks](#get_webhooks) - List webhooks
* [update_webhook](#update_webhook) - Update a webhook

## create_webhook

Create a webhook

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateWebhookRequestBody(
    events=[
        operations.CreateWebhookRequestBodyEvents.WORKFLOW_COMPLETED,
    ],
    name='Vicky Lynch',
    scope=operations.CreateWebhookRequestBodyScope(
        id='6b144290-7474-4778-a7bd-466d28c10ab3',
        type=operations.CreateWebhookRequestBodyScopeType.PROJECT,
    ),
    signing_secret='quo',
    url='illum',
    verify_tls=False,
)

res = s.webhook.create_webhook(req)

if res.webhook is not None:
    # handle response
```

## delete_webhook

Delete a webhook

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DeleteWebhookRequest(
    webhook_id='ca425190-4e52-43c7-a0bc-7178e4796f2a',
)

res = s.webhook.delete_webhook(req)

if res.message_response is not None:
    # handle response
```

## get_webhook_by_id

Get a webhook by id.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetWebhookByIDRequest(
    webhook_id='70c68828-2aa4-4825-a2f2-22e9817ee17c',
)

res = s.webhook.get_webhook_by_id(req)

if res.webhook is not None:
    # handle response
```

## get_webhooks

Get a list of webhook that match the given scope-type and scope-id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetWebhooksRequest(
    scope_id='be61e6b7-b95b-4c0a-b3c2-0c4f3789fd87',
    scope_type=operations.GetWebhooksScopeType.PROJECT,
)

res = s.webhook.get_webhooks(req)

if res.get_webhooks_200_application_json_object is not None:
    # handle response
```

## update_webhook

Update a webhook

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UpdateWebhookRequest(
    request_body=operations.UpdateWebhookRequestBody(
        events=[
            operations.UpdateWebhookRequestBodyEvents.JOB_COMPLETED,
        ],
        name='Kirk Stracke',
        signing_secret='eveniet',
        url='asperiores',
        verify_tls=False,
    ),
    webhook_id='d121aa6f-1e67-44bd-b04f-15756082d68e',
)

res = s.webhook.update_webhook(req)

if res.webhook is not None:
    # handle response
```
