# AddEnvironmentVariableToContext200ApplicationJSON1


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `context_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | ID of the context (UUID)                                             |                                                                      |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The date and time the environment variable was created.              | 2015-09-21T17:29:21.042Z                                             |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The date and time the environment variable was updated               | 2015-09-21T17:29:21.042Z                                             |
| `variable`                                                           | *str*                                                                | :heavy_check_mark:                                                   | The name of the environment variable                                 | POSTGRES_USER                                                        |