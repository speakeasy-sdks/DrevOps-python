# pipeline

### Available Operations

* [continue_pipeline](#continue_pipeline) - Continue a pipeline
* [get_pipeline_by_id](#get_pipeline_by_id) - Get a pipeline by ID
* [get_pipeline_by_number](#get_pipeline_by_number) - Get a pipeline by pipeline number
* [get_pipeline_config_by_id](#get_pipeline_config_by_id) - Get a pipeline's configuration
* [list_my_pipelines](#list_my_pipelines) - Get your pipelines
* [list_pipelines](#list_pipelines) - Get a list of pipelines
* [list_pipelines_for_project](#list_pipelines_for_project) - Get all pipelines
* [list_workflows_by_pipeline_id](#list_workflows_by_pipeline_id) - Get a pipeline's workflows
* [trigger_pipeline](#trigger_pipeline) - Trigger a new pipeline

## continue_pipeline

Continue a pipeline from the setup phase.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ContinuePipelineRequestBody(
    configuration="praesentium",
    continuation_key="natus",
    parameters={
        "sunt": "quo",
    },
)

res = s.pipeline.continue_pipeline(req)

if res.message_response is not None:
    # handle response
```

## get_pipeline_by_id

Returns a pipeline by the pipeline ID.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPipelineByIDRequest(
    pipeline_id="ddc69260-1fb5-476b-8d5f-0d30c5fbb258",
)

res = s.pipeline.get_pipeline_by_id(req)

if res.pipeline is not None:
    # handle response
```

## get_pipeline_by_number

Returns a pipeline by the pipeline number.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPipelineByNumberRequest(
    pipeline_number="dignissimos",
    project_slug="eaque",
)

res = s.pipeline.get_pipeline_by_number(req)

if res.pipeline is not None:
    # handle response
```

## get_pipeline_config_by_id

Returns a pipeline's configuration by ID.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPipelineConfigByIDRequest(
    pipeline_id="53202c73-d5fe-49b9-8c28-909b3fe49a8d",
)

res = s.pipeline.get_pipeline_config_by_id(req)

if res.pipeline_config is not None:
    # handle response
```

## list_my_pipelines

Returns a sequence of all pipelines for this project triggered by the user.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListMyPipelinesRequest(
    page_token="provident",
    project_slug="nobis",
)

res = s.pipeline.list_my_pipelines(req)

if res.pipeline_list_response is not None:
    # handle response
```

## list_pipelines

Returns all pipelines for the most recently built projects (max 250) you follow in an organization.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListPipelinesRequest(
    mine=False,
    org_slug="libero",
    page_token="delectus",
)

res = s.pipeline.list_pipelines(req)

if res.pipeline_list_response is not None:
    # handle response
```

## list_pipelines_for_project

Returns all pipelines for this project.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListPipelinesForProjectRequest(
    branch="quaerat",
    page_token="quos",
    project_slug="aliquid",
)

res = s.pipeline.list_pipelines_for_project(req)

if res.pipeline_list_response is not None:
    # handle response
```

## list_workflows_by_pipeline_id

Returns a paginated list of workflows by pipeline ID.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListWorkflowsByPipelineIDRequest(
    page_token="dolorem",
    pipeline_id="3323f9b7-7f3a-4410-8674-ebf69280d1ba",
)

res = s.pipeline.list_workflows_by_pipeline_id(req)

if res.workflow_list_response is not None:
    # handle response
```

## trigger_pipeline

Triggers a new pipeline on the project.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.TriggerPipelineRequest(
    request_body=operations.TriggerPipelineTriggerPipelineParameters(
        branch="feature/design-new-api",
        parameters={
            "voluptate": "dolorum",
            "deleniti": "omnis",
        },
        tag="v3.1.4159",
    ),
    project_slug="necessitatibus",
)

res = s.pipeline.trigger_pipeline(req)

if res.pipeline_creation is not None:
    # handle response
```
