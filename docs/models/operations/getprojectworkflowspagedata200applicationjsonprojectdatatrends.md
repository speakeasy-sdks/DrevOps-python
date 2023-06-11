# GetProjectWorkflowsPageData200ApplicationJSONProjectDataTrends

Metric trends aggregated across all workflows and branches for a project.


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `success_rate`                                      | *float*                                             | :heavy_check_mark:                                  | The trend value for the success rate.               |
| `throughput`                                        | *float*                                             | :heavy_check_mark:                                  | Trend value for the average number of runs per day. |
| `total_credits_used`                                | *float*                                             | :heavy_check_mark:                                  | The trend value for total credits consumed.         |
| `total_duration_secs`                               | *float*                                             | :heavy_check_mark:                                  | Trend value for total duration.                     |
| `total_runs`                                        | *float*                                             | :heavy_check_mark:                                  | The trend value for total number of runs.           |