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
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateCheckoutKeyRequest(
    request_body=operations.CreateCheckoutKeyCheckoutKeyInput(
        type=operations.CreateCheckoutKeyCheckoutKeyInputCheckoutKeyInputType.DEPLOY_KEY,
    ),
    project_slug='distinctio',
)

res = s.project.create_checkout_key(req)

if res.checkout_key is not None:
    # handle response
```

## create_env_var

Creates a new environment variable.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateEnvVarRequest(
    request_body=operations.CreateEnvVarEnvironmentVariablePair(
        name='foo',
        value='xxxx1234',
    ),
    project_slug='asperiores',
)

res = s.project.create_env_var(req)

if res.environment_variable_pair is not None:
    # handle response
```

## delete_checkout_key

Deletes the checkout key.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DeleteCheckoutKeyRequest(
    fingerprint='nihil',
    project_slug='ipsum',
)

res = s.project.delete_checkout_key(req)

if res.message_response is not None:
    # handle response
```

## delete_env_var

Deletes the environment variable named :name.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DeleteEnvVarRequest(
    name='Alberta Ullrich',
    project_slug='perferendis',
)

res = s.project.delete_env_var(req)

if res.message_response is not None:
    # handle response
```

## get_checkout_key

Returns an individual checkout key.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetCheckoutKeyRequest(
    fingerprint='amet',
    project_slug='optio',
)

res = s.project.get_checkout_key(req)

if res.checkout_key is not None:
    # handle response
```

## get_env_var

Returns the masked value of environment variable :name.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetEnvVarRequest(
    name='Tommy Turner',
    project_slug='provident',
)

res = s.project.get_env_var(req)

if res.environment_variable_pair is not None:
    # handle response
```

## get_project_by_slug

Retrieves a project by project slug.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetProjectBySlugRequest(
    project_slug='minima',
)

res = s.project.get_project_by_slug(req)

if res.project is not None:
    # handle response
```

## list_checkout_keys

Returns a sequence of checkout keys for `:project`.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListCheckoutKeysRequest(
    project_slug='repellendus',
)

res = s.project.list_checkout_keys(req)

if res.checkout_key_list_response is not None:
    # handle response
```

## list_env_vars

Returns four 'x' characters, in addition to the last four ASCII characters of the value, consistent with the display of environment variable values on the CircleCI website.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListEnvVarsRequest(
    project_slug='totam',
)

res = s.project.list_env_vars(req)

if res.environment_variable_list_response is not None:
    # handle response
```
