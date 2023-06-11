# project

### Available Operations

* [create_checkout_key](#create_checkout_key) - Create a new checkout key
* [create_env_var](#create_env_var) - Create an environment variable
* [delete_checkout_key](#delete_checkout_key) - Delete a checkout key
* [delete_env_var](#delete_env_var) - Delete an environment variable
* [get_checkout_key](#get_checkout_key) - Get a checkout key
* [get_env_var](#get_env_var) - Get a masked environment variable
* [get_project_by_slug](#get_project_by_slug) - Get a project
* [list_checkout_keys](#list_checkout_keys) - Get all checkout keys
* [list_env_vars](#list_env_vars) - List all environment variables

## create_checkout_key

Creates a new checkout key. This API request is only usable with a user API token.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.CreateCheckoutKeyRequest(
    request_body=operations.CreateCheckoutKeyCheckoutKeyInput(
        type=operations.CreateCheckoutKeyCheckoutKeyInputCheckoutKeyInputType.DEPLOY_KEY,
    ),
    project_slug='voluptate',
)

res = s.project.create_checkout_key(req)

if res.checkout_key is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateCheckoutKeyRequest](../../models/operations/createcheckoutkeyrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateCheckoutKeyResponse](../../models/operations/createcheckoutkeyresponse.md)**


## create_env_var

Creates a new environment variable.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.CreateEnvVarRequest(
    request_body=operations.CreateEnvVarEnvironmentVariablePair(
        name='foo',
        value='xxxx1234',
    ),
    project_slug='dignissimos',
)

res = s.project.create_env_var(req)

if res.environment_variable_pair is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateEnvVarRequest](../../models/operations/createenvvarrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateEnvVarResponse](../../models/operations/createenvvarresponse.md)**


## delete_checkout_key

Deletes the checkout key.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.DeleteCheckoutKeyRequest(
    fingerprint='reiciendis',
    project_slug='amet',
)

res = s.project.delete_checkout_key(req)

if res.message_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteCheckoutKeyRequest](../../models/operations/deletecheckoutkeyrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteCheckoutKeyResponse](../../models/operations/deletecheckoutkeyresponse.md)**


## delete_env_var

Deletes the environment variable named :name.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.DeleteEnvVarRequest(
    name='Mr. Bradley Bogan',
    project_slug='odio',
)

res = s.project.delete_env_var(req)

if res.message_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteEnvVarRequest](../../models/operations/deleteenvvarrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteEnvVarResponse](../../models/operations/deleteenvvarresponse.md)**


## get_checkout_key

Returns an individual checkout key.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetCheckoutKeyRequest(
    fingerprint='quaerat',
    project_slug='accusamus',
)

res = s.project.get_checkout_key(req)

if res.checkout_key is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCheckoutKeyRequest](../../models/operations/getcheckoutkeyrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetCheckoutKeyResponse](../../models/operations/getcheckoutkeyresponse.md)**


## get_env_var

Returns the masked value of environment variable :name.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetEnvVarRequest(
    name='Jan Hodkiewicz',
    project_slug='atque',
)

res = s.project.get_env_var(req)

if res.environment_variable_pair is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetEnvVarRequest](../../models/operations/getenvvarrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetEnvVarResponse](../../models/operations/getenvvarresponse.md)**


## get_project_by_slug

Retrieves a project by project slug.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetProjectBySlugRequest(
    project_slug='sit',
)

res = s.project.get_project_by_slug(req)

if res.project is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetProjectBySlugRequest](../../models/operations/getprojectbyslugrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetProjectBySlugResponse](../../models/operations/getprojectbyslugresponse.md)**


## list_checkout_keys

Returns a sequence of checkout keys for `:project`.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.ListCheckoutKeysRequest(
    project_slug='fugiat',
)

res = s.project.list_checkout_keys(req)

if res.checkout_key_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCheckoutKeysRequest](../../models/operations/listcheckoutkeysrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListCheckoutKeysResponse](../../models/operations/listcheckoutkeysresponse.md)**


## list_env_vars

Returns four 'x' characters, in addition to the last four ASCII characters of the value, consistent with the display of environment variable values on the CircleCI website.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.ListEnvVarsRequest(
    project_slug='ab',
)

res = s.project.list_env_vars(req)

if res.environment_variable_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListEnvVarsRequest](../../models/operations/listenvvarsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListEnvVarsResponse](../../models/operations/listenvvarsresponse.md)**

