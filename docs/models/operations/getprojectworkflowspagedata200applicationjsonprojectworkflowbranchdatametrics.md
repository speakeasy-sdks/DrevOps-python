# GetProjectWorkflowsPageData200ApplicationJSONProjectWorkflowBranchDataMetrics

Metrics aggregated across a workflow or branchfor a project.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `p95_duration_secs`                                              | *float*                                                          | :heavy_check_mark:                                               | The 95th percentile duration among a group of workflow runs.     |
| `success_rate`                                                   | *float*                                                          | :heavy_check_mark:                                               | N/A                                                              |
| `total_credits_used`                                             | *int*                                                            | :heavy_check_mark:                                               | The total credits consumed over the current timeseries interval. |
| `total_runs`                                                     | *int*                                                            | :heavy_check_mark:                                               | The total number of runs.                                        |