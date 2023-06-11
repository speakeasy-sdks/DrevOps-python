# ListMyPipelinesRequest


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `page_token`                                                                                   | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | A token to retrieve the next page of results.                                                  |
| `project_slug`                                                                                 | *str*                                                                                          | :heavy_check_mark:                                                                             | Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. |