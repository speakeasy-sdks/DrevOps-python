# ListPipelinesRequest


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `mine`                                        | *Optional[bool]*                              | :heavy_minus_sign:                            | Only include entries created by your user.    |
| `org_slug`                                    | *Optional[str]*                               | :heavy_minus_sign:                            | Org slug in the form `vcs-slug/org-name`      |
| `page_token`                                  | *Optional[str]*                               | :heavy_minus_sign:                            | A token to retrieve the next page of results. |