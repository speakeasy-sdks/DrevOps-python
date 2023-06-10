# GetJobDetailsJobDetailsMessages

Message from CircleCI execution platform.


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `message`                                                       | *str*                                                           | :heavy_check_mark:                                              | Information describing message.                                 |
| `reason`                                                        | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Value describing the reason for message to be added to the job. |
| `type`                                                          | *str*                                                           | :heavy_check_mark:                                              | Message type.                                                   |