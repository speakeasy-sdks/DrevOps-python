# CircleCi

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/DrevOps-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.AddEnvironmentVariableToContextRequest(
    request_body=operations.AddEnvironmentVariableToContextRequestBody(
        value='some-secret-value',
    ),
    context_id='89bd9d8d-69a6-474e-8f46-7cc8796ed151',
    env_var_name='deserunt',
)

res = s.context.add_environment_variable_to_context(req)

if res.add_environment_variable_to_context_200_application_json_any_of is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [context](docs/sdks/context/README.md)

* [add_environment_variable_to_context](docs/sdks/context/README.md#add_environment_variable_to_context) - Add or update an environment variable
* [create_context](docs/sdks/context/README.md#create_context) - Create a new context
* [delete_context](docs/sdks/context/README.md#delete_context) - Delete a context
* [delete_environment_variable_from_context](docs/sdks/context/README.md#delete_environment_variable_from_context) - Remove an environment variable
* [get_context](docs/sdks/context/README.md#get_context) - Get a context
* [list_contexts](docs/sdks/context/README.md#list_contexts) - List contexts
* [list_environment_variables_from_context](docs/sdks/context/README.md#list_environment_variables_from_context) - List environment variables

### [insights](docs/sdks/insights/README.md)

* [get_all_insights_branches](docs/sdks/insights/README.md#get_all_insights_branches) - Get all branches for a project
* [get_flaky_tests](docs/sdks/insights/README.md#get_flaky_tests) - Get flaky tests for a project
* [get_job_timeseries](docs/sdks/insights/README.md#get_job_timeseries) - Job timeseries data
* [get_org_summary_data](docs/sdks/insights/README.md#get_org_summary_data) - Get summary metrics with trends for the entire org, and for each project.
* [get_project_workflow_job_metrics](docs/sdks/insights/README.md#get_project_workflow_job_metrics) - Get summary metrics for a project workflow's jobs.
* [get_project_workflow_metrics](docs/sdks/insights/README.md#get_project_workflow_metrics) - Get summary metrics for a project's workflows
* [get_project_workflow_runs](docs/sdks/insights/README.md#get_project_workflow_runs) - Get recent runs of a workflow
* [get_project_workflow_test_metrics](docs/sdks/insights/README.md#get_project_workflow_test_metrics) - Get test metrics for a project's workflows
* [get_project_workflows_page_data](docs/sdks/insights/README.md#get_project_workflows_page_data) - Get summary metrics and trends for a project across it's workflows and branches
* [get_workflow_summary](docs/sdks/insights/README.md#get_workflow_summary) - Get metrics and trends for workflows

### [job](docs/sdks/job/README.md)

* [cancel_job](docs/sdks/job/README.md#cancel_job) - Cancel job
* [get_job_artifacts](docs/sdks/job/README.md#get_job_artifacts) - Get a job's artifacts
* [get_job_details](docs/sdks/job/README.md#get_job_details) - Get job details
* [get_tests](docs/sdks/job/README.md#get_tests) - Get test metadata

### [pipeline](docs/sdks/pipeline/README.md)

* [continue_pipeline](docs/sdks/pipeline/README.md#continue_pipeline) - Continue a pipeline
* [get_pipeline_by_id](docs/sdks/pipeline/README.md#get_pipeline_by_id) - Get a pipeline by ID
* [get_pipeline_by_number](docs/sdks/pipeline/README.md#get_pipeline_by_number) - Get a pipeline by pipeline number
* [get_pipeline_config_by_id](docs/sdks/pipeline/README.md#get_pipeline_config_by_id) - Get a pipeline's configuration
* [list_my_pipelines](docs/sdks/pipeline/README.md#list_my_pipelines) - Get your pipelines
* [list_pipelines](docs/sdks/pipeline/README.md#list_pipelines) - Get a list of pipelines
* [list_pipelines_for_project](docs/sdks/pipeline/README.md#list_pipelines_for_project) - Get all pipelines
* [list_workflows_by_pipeline_id](docs/sdks/pipeline/README.md#list_workflows_by_pipeline_id) - Get a pipeline's workflows
* [trigger_pipeline](docs/sdks/pipeline/README.md#trigger_pipeline) - Trigger a new pipeline

### [project](docs/sdks/project/README.md)

* [create_checkout_key](docs/sdks/project/README.md#create_checkout_key) - Create a new checkout key
* [create_env_var](docs/sdks/project/README.md#create_env_var) - Create an environment variable
* [delete_checkout_key](docs/sdks/project/README.md#delete_checkout_key) - Delete a checkout key
* [delete_env_var](docs/sdks/project/README.md#delete_env_var) - Delete an environment variable
* [get_checkout_key](docs/sdks/project/README.md#get_checkout_key) - Get a checkout key
* [get_env_var](docs/sdks/project/README.md#get_env_var) - Get a masked environment variable
* [get_project_by_slug](docs/sdks/project/README.md#get_project_by_slug) - Get a project
* [list_checkout_keys](docs/sdks/project/README.md#list_checkout_keys) - Get all checkout keys
* [list_env_vars](docs/sdks/project/README.md#list_env_vars) - List all environment variables

### [schedule](docs/sdks/schedule/README.md)

* [create_schedule](docs/sdks/schedule/README.md#create_schedule) - Create a schedule
* [delete_schedule_by_id](docs/sdks/schedule/README.md#delete_schedule_by_id) - Delete a schedule
* [get_schedule_by_id](docs/sdks/schedule/README.md#get_schedule_by_id) - Get a schedule
* [list_schedules_for_project](docs/sdks/schedule/README.md#list_schedules_for_project) - Get all schedules
* [update_schedule](docs/sdks/schedule/README.md#update_schedule) - Update a schedule

### [user](docs/sdks/user/README.md)

* [get_collaborations](docs/sdks/user/README.md#get_collaborations) - Collaborations
* [get_current_user](docs/sdks/user/README.md#get_current_user) - User Information
* [get_user](docs/sdks/user/README.md#get_user) - User Information

### [webhook](docs/sdks/webhook/README.md)

* [create_webhook](docs/sdks/webhook/README.md#create_webhook) - Create a webhook
* [delete_webhook](docs/sdks/webhook/README.md#delete_webhook) - Delete a webhook
* [get_webhook_by_id](docs/sdks/webhook/README.md#get_webhook_by_id) - Get a webhook
* [get_webhooks](docs/sdks/webhook/README.md#get_webhooks) - List webhooks
* [update_webhook](docs/sdks/webhook/README.md#update_webhook) - Update a webhook

### [workflow](docs/sdks/workflow/README.md)

* [approve_pending_approval_job_by_id](docs/sdks/workflow/README.md#approve_pending_approval_job_by_id) - Approve a job
* [cancel_workflow](docs/sdks/workflow/README.md#cancel_workflow) - Cancel a workflow
* [get_workflow_by_id](docs/sdks/workflow/README.md#get_workflow_by_id) - Get a workflow
* [list_workflow_jobs](docs/sdks/workflow/README.md#list_workflow_jobs) - Get a workflow's jobs
* [rerun_workflow](docs/sdks/workflow/README.md#rerun_workflow) - Rerun a workflow
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
