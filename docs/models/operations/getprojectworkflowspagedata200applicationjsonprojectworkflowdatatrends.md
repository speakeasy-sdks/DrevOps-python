# GetProjectWorkflowsPageData200ApplicationJSONProjectWorkflowDataTrends

Trends aggregated across a workflow or branch for a project.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `p95_duration_secs`                                          | *float*                                                      | :heavy_check_mark:                                           | The 95th percentile duration among a group of workflow runs. |
| `success_rate`                                               | *float*                                                      | :heavy_check_mark:                                           | The trend value for the success rate.                        |
| `total_credits_used`                                         | *float*                                                      | :heavy_check_mark:                                           | The trend value for total credits consumed.                  |
| `total_runs`                                                 | *float*                                                      | :heavy_check_mark:                                           | The trend value for total number of runs.                    |