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
        api_key_header="",
    ),
)

req = operations.CreateWebhookRequestBody(
    events=[
        operations.CreateWebhookRequestBodyEvents.JOB_COMPLETED,
        operations.CreateWebhookRequestBodyEvents.JOB_COMPLETED,
    ],
    name='Nathaniel Ryan',
    scope=operations.CreateWebhookRequestBodyScope(
        id='6146c3e2-50fb-4008-842e-141aac366c8d',
        type=operations.CreateWebhookRequestBodyScopeType.PROJECT,
    ),
    signing_secret='nulla',
    url='voluptas',
    verify_tls=False,
)

res = s.webhook.create_webhook(req)

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateWebhookRequestBody](../../models/operations/createwebhookrequestbody.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateWebhookResponse](../../models/operations/createwebhookresponse.md)**


## delete_webhook

Delete a webhook

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.DeleteWebhookRequest(
    webhook_id='b1442907-4747-478a-bbd4-66d28c10ab3c',
)

res = s.webhook.delete_webhook(req)

if res.message_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteWebhookRequest](../../models/operations/deletewebhookrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DeleteWebhookResponse](../../models/operations/deletewebhookresponse.md)**


## get_webhook_by_id

Get a webhook by id.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetWebhookByIDRequest(
    webhook_id='dca42519-04e5-423c-be0b-c7178e4796f2',
)

res = s.webhook.get_webhook_by_id(req)

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetWebhookByIDRequest](../../models/operations/getwebhookbyidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetWebhookByIDResponse](../../models/operations/getwebhookbyidresponse.md)**


## get_webhooks

Get a list of webhook that match the given scope-type and scope-id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetWebhooksRequest(
    scope_id='a70c6882-82aa-4482-962f-222e9817ee17',
    scope_type=operations.GetWebhooksScopeType.PROJECT,
)

res = s.webhook.get_webhooks(req)

if res.get_webhooks_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetWebhooksRequest](../../models/operations/getwebhooksrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetWebhooksResponse](../../models/operations/getwebhooksresponse.md)**


## update_webhook

Update a webhook

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.UpdateWebhookRequest(
    request_body=operations.UpdateWebhookRequestBody(
        events=[
            operations.UpdateWebhookRequestBodyEvents.JOB_COMPLETED,
            operations.UpdateWebhookRequestBodyEvents.JOB_COMPLETED,
            operations.UpdateWebhookRequestBodyEvents.WORKFLOW_COMPLETED,
            operations.UpdateWebhookRequestBodyEvents.WORKFLOW_COMPLETED,
        ],
        name='Cecil Pollich',
        signing_secret='occaecati',
        url='minima',
        verify_tls=False,
    ),
    webhook_id='bc0ab3c2-0c4f-4378-9fd8-71f99dd2efd1',
)

res = s.webhook.update_webhook(req)

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateWebhookRequest](../../models/operations/updatewebhookrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateWebhookResponse](../../models/operations/updatewebhookresponse.md)**

