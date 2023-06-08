<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.AddEnvironmentVariableToContextRequest(
    request_body=operations.AddEnvironmentVariableToContextRequestBody(
        value='some-secret-value',
    ),
    context_id='89bd9d8d-69a6-474e-8f46-7cc8796ed151',
    env_var_name='deserunt',
)

res = s.context.add_environment_variable_to_context(req)

if res.add_environment_variable_to_context_200_application_json_any_of is not None:
    # handle response
```
<!-- End SDK Example Usage -->