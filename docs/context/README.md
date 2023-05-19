# context

### Available Operations

* [add_environment_variable_to_context](#add_environment_variable_to_context) - Add or update an environment variable
* [create_context](#create_context) - Create a new context
* [delete_context](#delete_context) - Delete a context
* [delete_environment_variable_from_context](#delete_environment_variable_from_context) - Remove an environment variable
* [get_context](#get_context) - Get a context
* [list_contexts](#list_contexts) - List contexts
* [list_environment_variables_from_context](#list_environment_variables_from_context) - List environment variables

## add_environment_variable_to_context

Create or update an environment variable within a context. Returns information about the environment variable, not including its value.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.AddEnvironmentVariableToContextRequest(
    request_body=operations.AddEnvironmentVariableToContextRequestBody(
        value='some-secret-value',
    ),
    context_id='05dfc2dd-f7cc-478c-a1ba-928fc816742c',
    env_var_name='cum',
)

res = s.context.add_environment_variable_to_context(req)

if res.add_environment_variable_to_context_200_application_json_any_of is not None:
    # handle response
```

## create_context

Create a new context

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateContextRequestBody(
    name='Edna Mante II',
    owner=operations.CreateContextRequestBodyOwner2(
        slug='sed',
        type=operations.CreateContextRequestBodyOwner2Type.ORGANIZATION,
    ),
)

res = s.context.create_context(req)

if res.context is not None:
    # handle response
```

## delete_context

Delete a context

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DeleteContextRequest(
    context_id='9396fea7-596e-4b10-baaa-2352c5955907',
)

res = s.context.delete_context(req)

if res.message_response is not None:
    # handle response
```

## delete_environment_variable_from_context

Delete an environment variable from a context.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DeleteEnvironmentVariableFromContextRequest(
    context_id='aff1a3a2-fa94-4677-b925-1aa52c3f5ad0',
    env_var_name='quasi',
)

res = s.context.delete_environment_variable_from_context(req)

if res.message_response is not None:
    # handle response
```

## get_context

Returns basic information about a context.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetContextRequest(
    context_id='9da1ffe7-8f09-47b0-874f-15471b5e6e13',
)

res = s.context.get_context(req)

if res.context is not None:
    # handle response
```

## list_contexts

List all contexts for an owner.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListContextsRequest(
    owner_id='b99d488e-1e91-4e45-8ad2-abd44269802d',
    owner_slug='ipsam',
    owner_type=operations.ListContextsOwnerType.ACCOUNT,
    page_token='fugit',
)

res = s.context.list_contexts(req)

if res.list_contexts_200_application_json_object is not None:
    # handle response
```

## list_environment_variables_from_context

List information about environment variables in a context, not including their values.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListEnvironmentVariablesFromContextRequest(
    context_id='a94bb4f6-3c96-49e9-a3ef-a77dfb14cd66',
    page_token='laborum',
)

res = s.context.list_environment_variables_from_context(req)

if res.list_environment_variables_from_context_200_application_json_object is not None:
    # handle response
```
