# ListEnvVarsResponse


## Fields

| Field                                                                                                                         | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                                | *str*                                                                                                                         | :heavy_check_mark:                                                                                                            | N/A                                                                                                                           |
| `environment_variable_list_response`                                                                                          | [Optional[ListEnvVarsEnvironmentVariableListResponse]](../../models/operations/listenvvarsenvironmentvariablelistresponse.md) | :heavy_minus_sign:                                                                                                            | A sequence of environment variables.                                                                                          |
| `status_code`                                                                                                                 | *int*                                                                                                                         | :heavy_check_mark:                                                                                                            | N/A                                                                                                                           |
| `raw_response`                                                                                                                | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                         | :heavy_minus_sign:                                                                                                            | N/A                                                                                                                           |
| `list_env_vars_default_application_json_object`                                                                               | [Optional[ListEnvVarsDefaultApplicationJSON]](../../models/operations/listenvvarsdefaultapplicationjson.md)                   | :heavy_minus_sign:                                                                                                            | Error response.                                                                                                               |