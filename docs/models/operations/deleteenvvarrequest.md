# DeleteEnvVarRequest


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `name`                                                                                         | *str*                                                                                          | :heavy_check_mark:                                                                             | The name of the environment variable.                                                          |
| `project_slug`                                                                                 | *str*                                                                                          | :heavy_check_mark:                                                                             | Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. |