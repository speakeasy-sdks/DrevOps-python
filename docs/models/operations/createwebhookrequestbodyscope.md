# CreateWebhookRequestBodyScope

The scope in which the relevant events that will trigger webhooks


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `id`                                                                                              | *str*                                                                                             | :heavy_check_mark:                                                                                | ID of the scope being used (at the moment, only project ID is supported)                          |
| `type`                                                                                            | [CreateWebhookRequestBodyScopeType](../../models/operations/createwebhookrequestbodyscopetype.md) | :heavy_check_mark:                                                                                | Type of the scope being used                                                                      |