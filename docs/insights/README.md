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
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAllInsightsBranchesRequest(
    project_slug="accusamus",
    workflow_name="non",
)

res = s.insights.get_all_insights_branches(req)

if res.get_all_insights_branches_200_application_json_any is not None:
    # handle response
```

## get_flaky_tests

Get a list of flaky tests for a given project. Flaky tests are branch agnostic. 
             A flaky test is a test that passed and failed in the same commit.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetFlakyTestsRequest(
    project_slug="occaecati",
)

res = s.insights.get_flaky_tests(req)

if res.get_flaky_tests_200_application_json_object is not None:
    # handle response
```

## get_job_timeseries

Get timeseries data for all jobs within a workflow.

### Example Usage

```python
import sdk
import dateutil.parser
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetJobTimeseriesRequest(
    branch="enim",
    end_date=dateutil.parser.isoparse('2020-02-08T20:51:42.354Z'),
    granularity="hourly",
    project_slug="provident",
    start_date=dateutil.parser.isoparse('2021-09-06T10:36:33.442Z'),
    workflow_name="blanditiis",
)

res = s.insights.get_job_timeseries(req)

if res.get_job_timeseries_200_application_json_object is not None:
    # handle response
```

## get_org_summary_data

Gets aggregated summary metrics with trends for the entire org. 
              Also gets aggregated metrics and trends for each project belonging to the org.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetOrgSummaryDataRequest(
    org_slug="deleniti",
    project_names={
        "amet": "deserunt",
        "nisi": "vel",
        "natus": "omnis",
        "molestiae": "perferendis",
    },
    reporting_window="last-24-hours",
)

res = s.insights.get_org_summary_data(req)

if res.get_org_summary_data_200_application_json_object is not None:
    # handle response
```

## get_project_workflow_job_metrics

Get summary metrics for a project workflow's jobs. Job runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetProjectWorkflowJobMetricsRequest(
    all_branches=False,
    branch="magnam",
    page_token="distinctio",
    project_slug="id",
    reporting_window="last-90-days",
    workflow_name="labore",
)

res = s.insights.get_project_workflow_job_metrics(req)

if res.get_project_workflow_job_metrics_200_application_json_object is not None:
    # handle response
```

## get_project_workflow_metrics

Get summary metrics for a project's workflows.  Workflow runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours.  Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetProjectWorkflowMetricsRequest(
    all_branches=False,
    branch="suscipit",
    page_token="natus",
    project_slug="nobis",
    reporting_window="last-24-hours",
)

res = s.insights.get_project_workflow_metrics(req)

if res.get_project_workflow_metrics_200_application_json_object is not None:
    # handle response
```

## get_project_workflow_runs

Get recent runs of a workflow. Runs going back at most 90 days are returned. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

### Example Usage

```python
import sdk
import dateutil.parser
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetProjectWorkflowRunsRequest(
    all_branches=False,
    branch="vero",
    end_date=dateutil.parser.isoparse('2022-11-24T10:55:00.183Z'),
    page_token="magnam",
    project_slug="et",
    start_date=dateutil.parser.isoparse('2022-04-17T13:06:08.135Z'),
    workflow_name="provident",
)

res = s.insights.get_project_workflow_runs(req)

if res.get_project_workflow_runs_200_application_json_object is not None:
    # handle response
```

## get_project_workflow_test_metrics

Get test metrics for a project's workflows. Currently tests metrics are calculated based on 10 most recent workflow runs.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetProjectWorkflowTestMetricsRequest(
    all_branches=False,
    branch="quos",
    project_slug="sint",
    workflow_name="accusantium",
)

res = s.insights.get_project_workflow_test_metrics(req)

if res.get_project_workflow_test_metrics_200_application_json_object is not None:
    # handle response
```

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
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetProjectWorkflowsPageDataRequest(
    branches={
        "reiciendis": "mollitia",
        "ad": "eum",
        "dolor": "necessitatibus",
    },
    project_slug="odit",
    reporting_window="last-90-days",
    workflow_names={
        "iure": "doloribus",
    },
)

res = s.insights.get_project_workflows_page_data(req)

if res.get_project_workflows_page_data_200_application_json_object is not None:
    # handle response
```

## get_workflow_summary

Get the metrics and trends for a particular workflow on a single branch or all branches

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetWorkflowSummaryRequest(
    all_branches=False,
    branches={
        "eius": "maxime",
        "deleniti": "facilis",
        "in": "architecto",
        "architecto": "repudiandae",
    },
    project_slug="ullam",
    workflow_name="expedita",
)

res = s.insights.get_workflow_summary(req)

if res.get_workflow_summary_200_application_json_object is not None:
    # handle response
```
