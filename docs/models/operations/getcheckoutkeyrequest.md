# GetCheckoutKeyRequest


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `fingerprint`                                                                                  | *str*                                                                                          | :heavy_check_mark:                                                                             | An SSH key fingerprint.                                                                        |
| `project_slug`                                                                                 | *str*                                                                                          | :heavy_check_mark:                                                                             | Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. |