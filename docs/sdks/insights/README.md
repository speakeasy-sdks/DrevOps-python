# insights

### Available Operations

* [get_all_insights_branches](#get_all_insights_branches) - Get all branches for a project
* [get_flaky_tests](#get_flaky_tests) - Get flaky tests for a project
* [get_job_timeseries](#get_job_timeseries) - Job timeseries data
* [get_org_summary_data](#get_org_summary_data) - Get summary metrics with trends for the entire org, and for each project.
* [get_project_workflow_job_metrics](#get_project_workflow_job_metrics) - Get summary metrics for a project workflow's jobs.
* [get_project_workflow_metrics](#get_project_workflow_metrics) - Get summary metrics for a project's workflows
* [get_project_workflow_runs](#get_project_workflow_runs) - Get recent runs of a workflow
* [get_project_workflow_test_metrics](#get_project_workflow_test_metrics) - Get test metrics for a project's workflows
* [get_project_workflows_page_data](#get_project_workflows_page_data) - Get summary metrics and trends for a project across it's workflows and branches
* [get_workflow_summary](#get_workflow_summary) - Get metrics and trends for workflows

## get_all_insights_branches

Get a list of all branches for a specified project. The list will only contain branches currently available within Insights. The maximum number of branches returned by this endpoint is 5,000.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetAllInsightsBranchesRequest(
    project_slug='accusamus',
    workflow_name='non',
)

res = s.insights.get_all_insights_branches(req)

if res.get_all_insights_branches_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAllInsightsBranchesRequest](../../models/operations/getallinsightsbranchesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetAllInsightsBranchesResponse](../../models/operations/getallinsightsbranchesresponse.md)**


## get_flaky_tests

Get a list of flaky tests for a given project. Flaky tests are branch agnostic. 
             A flaky test is a test that passed and failed in the same commit.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetFlakyTestsRequest(
    project_slug='occaecati',
)

res = s.insights.get_flaky_tests(req)

if res.get_flaky_tests_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetFlakyTestsRequest](../../models/operations/getflakytestsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetFlakyTestsResponse](../../models/operations/getflakytestsresponse.md)**


## get_job_timeseries

Get timeseries data for all jobs within a workflow.

### Example Usage

```python
import sdk
import dateutil.parser
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetJobTimeseriesRequest(
    branch='enim',
    end_date=dateutil.parser.isoparse('2020-02-08T20:51:42.354Z'),
    granularity=operations.GetJobTimeseriesGranularity.HOURLY,
    project_slug='provident',
    start_date=dateutil.parser.isoparse('2021-09-06T10:36:33.442Z'),
    workflow_name='blanditiis',
)

res = s.insights.get_job_timeseries(req)

if res.get_job_timeseries_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetJobTimeseriesRequest](../../models/operations/getjobtimeseriesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetJobTimeseriesResponse](../../models/operations/getjobtimeseriesresponse.md)**


## get_org_summary_data

Gets aggregated summary metrics with trends for the entire org. 
              Also gets aggregated metrics and trends for each project belonging to the org.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetOrgSummaryDataRequest(
    org_slug='deleniti',
    project_names=operations.GetOrgSummaryDataProjectNames(),
    reporting_window=operations.GetOrgSummaryDataReportingWindow.LAST_60_DAYS,
)

res = s.insights.get_org_summary_data(req)

if res.get_org_summary_data_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetOrgSummaryDataRequest](../../models/operations/getorgsummarydatarequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetOrgSummaryDataResponse](../../models/operations/getorgsummarydataresponse.md)**


## get_project_workflow_job_metrics

Get summary metrics for a project workflow's jobs. Job runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetProjectWorkflowJobMetricsRequest(
    all_branches=False,
    branch='amet',
    page_token='deserunt',
    project_slug='nisi',
    reporting_window=operations.GetProjectWorkflowJobMetricsReportingWindow.LAST_24_HOURS,
    workflow_name='natus',
)

res = s.insights.get_project_workflow_job_metrics(req)

if res.get_project_workflow_job_metrics_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetProjectWorkflowJobMetricsRequest](../../models/operations/getprojectworkflowjobmetricsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetProjectWorkflowJobMetricsResponse](../../models/operations/getprojectworkflowjobmetricsresponse.md)**


## get_project_workflow_metrics

Get summary metrics for a project's workflows.  Workflow runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours.  Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetProjectWorkflowMetricsRequest(
    all_branches=False,
    branch='omnis',
    page_token='molestiae',
    project_slug='perferendis',
    reporting_window=operations.GetProjectWorkflowMetricsReportingWindow.LAST_24_HOURS,
)

res = s.insights.get_project_workflow_metrics(req)

if res.get_project_workflow_metrics_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetProjectWorkflowMetricsRequest](../../models/operations/getprojectworkflowmetricsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetProjectWorkflowMetricsResponse](../../models/operations/getprojectworkflowmetricsresponse.md)**


## get_project_workflow_runs

Get recent runs of a workflow. Runs going back at most 90 days are returned. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

### Example Usage

```python
import sdk
import dateutil.parser
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetProjectWorkflowRunsRequest(
    all_branches=False,
    branch='magnam',
    end_date=dateutil.parser.isoparse('2021-09-06T01:45:34.248Z'),
    page_token='labore',
    project_slug='labore',
    start_date=dateutil.parser.isoparse('2022-05-20T10:11:05.115Z'),
    workflow_name='nobis',
)

res = s.insights.get_project_workflow_runs(req)

if res.get_project_workflow_runs_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetProjectWorkflowRunsRequest](../../models/operations/getprojectworkflowrunsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetProjectWorkflowRunsResponse](../../models/operations/getprojectworkflowrunsresponse.md)**


## get_project_workflow_test_metrics

Get test metrics for a project's workflows. Currently tests metrics are calculated based on 10 most recent workflow runs.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetProjectWorkflowTestMetricsRequest(
    all_branches=False,
    branch='eum',
    project_slug='vero',
    workflow_name='aspernatur',
)

res = s.insights.get_project_workflow_test_metrics(req)

if res.get_project_workflow_test_metrics_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetProjectWorkflowTestMetricsRequest](../../models/operations/getprojectworkflowtestmetricsrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetProjectWorkflowTestMetricsResponse](../../models/operations/getprojectworkflowtestmetricsresponse.md)**


## get_project_workflows_page_data

Get summary metrics and trends for a project at workflow and branch level. 
             Workflow runs going back at most 90 days are included in the aggregation window. 
             Trends are only supported upto last 30 days. 
             Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetProjectWorkflowsPageDataRequest(
    branches=operations.GetProjectWorkflowsPageDataBranches(),
    project_slug='architecto',
    reporting_window=operations.GetProjectWorkflowsPageDataReportingWindow.LAST_90_DAYS,
    workflow_names=operations.GetProjectWorkflowsPageDataWorkflowNames(),
)

res = s.insights.get_project_workflows_page_data(req)

if res.get_project_workflows_page_data_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetProjectWorkflowsPageDataRequest](../../models/operations/getprojectworkflowspagedatarequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetProjectWorkflowsPageDataResponse](../../models/operations/getprojectworkflowspagedataresponse.md)**


## get_workflow_summary

Get the metrics and trends for a particular workflow on a single branch or all branches

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetWorkflowSummaryRequest(
    all_branches=False,
    branches=operations.GetWorkflowSummaryBranches(),
    project_slug='et',
    workflow_name='excepturi',
)

res = s.insights.get_workflow_summary(req)

if res.get_workflow_summary_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetWorkflowSummaryRequest](../../models/operations/getworkflowsummaryrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetWorkflowSummaryResponse](../../models/operations/getworkflowsummaryresponse.md)**

