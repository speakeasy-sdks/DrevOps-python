# GetProjectWorkflowTestMetrics200ApplicationJSONSlowestTests


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `classname`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | The class the test belongs to.                                        |
| `failed_runs`                                                         | *int*                                                                 | :heavy_check_mark:                                                    | The number of times the test failed                                   |
| `file`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | The file the test belongs to.                                         |
| `flaky`                                                               | *bool*                                                                | :heavy_check_mark:                                                    | Whether the test is flaky.                                            |
| `job_name`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | The name of the job.                                                  |
| `p95_duration`                                                        | *float*                                                               | :heavy_check_mark:                                                    | The 95th percentile duration, in seconds, among a group of test runs. |
| `source`                                                              | *str*                                                                 | :heavy_check_mark:                                                    | The source of the test.                                               |
| `test_name`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | The name of the test.                                                 |
| `total_runs`                                                          | *int*                                                                 | :heavy_check_mark:                                                    | The total number of times the test was run.                           |