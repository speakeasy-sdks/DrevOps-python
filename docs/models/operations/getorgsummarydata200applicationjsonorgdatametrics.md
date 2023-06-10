# GetOrgSummaryData200ApplicationJSONOrgDataMetrics

Metrics for a single org metrics.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `success_rate`                                                   | *float*                                                          | :heavy_check_mark:                                               | N/A                                                              |
| `throughput`                                                     | *float*                                                          | :heavy_check_mark:                                               | The average number of runs per day.                              |
| `total_credits_used`                                             | *int*                                                            | :heavy_check_mark:                                               | The total credits consumed over the current timeseries interval. |
| `total_duration_secs`                                            | *int*                                                            | :heavy_check_mark:                                               | Total duration, in seconds.                                      |
| `total_runs`                                                     | *int*                                                            | :heavy_check_mark:                                               | The total number of runs.                                        |