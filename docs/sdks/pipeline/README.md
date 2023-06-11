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
        api_key_header="",
    ),
)

req = operations.ContinuePipelineRequestBody(
    configuration='ad',
    continuation_key='eum',
    parameters={
        "necessitatibus": 'odit',
    },
)

res = s.pipeline.continue_pipeline(req)

if res.message_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ContinuePipelineRequestBody](../../models/operations/continuepipelinerequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ContinuePipelineResponse](../../models/operations/continuepipelineresponse.md)**


## get_pipeline_by_id

Returns a pipeline by the pipeline ID.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetPipelineByIDRequest(
    pipeline_id='516fe4c8-b711-4e5b-bfd2-ed028921cddc',
)

res = s.pipeline.get_pipeline_by_id(req)

if res.pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetPipelineByIDRequest](../../models/operations/getpipelinebyidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetPipelineByIDResponse](../../models/operations/getpipelinebyidresponse.md)**


## get_pipeline_by_number

Returns a pipeline by the pipeline number.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetPipelineByNumberRequest(
    pipeline_number='ea',
    project_slug='excepturi',
)

res = s.pipeline.get_pipeline_by_number(req)

if res.pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetPipelineByNumberRequest](../../models/operations/getpipelinebynumberrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetPipelineByNumberResponse](../../models/operations/getpipelinebynumberresponse.md)**


## get_pipeline_config_by_id

Returns a pipeline's configuration by ID.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetPipelineConfigByIDRequest(
    pipeline_id='2601fb57-6b0d-45f0-930c-5fbb25870532',
)

res = s.pipeline.get_pipeline_config_by_id(req)

if res.pipeline_config is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetPipelineConfigByIDRequest](../../models/operations/getpipelineconfigbyidrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetPipelineConfigByIDResponse](../../models/operations/getpipelineconfigbyidresponse.md)**


## list_my_pipelines

Returns a sequence of all pipelines for this project triggered by the user.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.ListMyPipelinesRequest(
    page_token='perferendis',
    project_slug='dolores',
)

res = s.pipeline.list_my_pipelines(req)

if res.pipeline_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListMyPipelinesRequest](../../models/operations/listmypipelinesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListMyPipelinesResponse](../../models/operations/listmypipelinesresponse.md)**


## list_pipelines

Returns all pipelines for the most recently built projects (max 250) you follow in an organization.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.ListPipelinesRequest(
    mine=False,
    org_slug='minus',
    page_token='quam',
)

res = s.pipeline.list_pipelines(req)

if res.pipeline_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListPipelinesRequest](../../models/operations/listpipelinesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListPipelinesResponse](../../models/operations/listpipelinesresponse.md)**


## list_pipelines_for_project

Returns all pipelines for this project.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.ListPipelinesForProjectRequest(
    branch='dolor',
    page_token='vero',
    project_slug='nostrum',
)

res = s.pipeline.list_pipelines_for_project(req)

if res.pipeline_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListPipelinesForProjectRequest](../../models/operations/listpipelinesforprojectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ListPipelinesForProjectResponse](../../models/operations/listpipelinesforprojectresponse.md)**


## list_workflows_by_pipeline_id

Returns a paginated list of workflows by pipeline ID.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.ListWorkflowsByPipelineIDRequest(
    page_token='hic',
    pipeline_id='e9b90c28-909b-43fe-89a8-d9cbf4863332',
)

res = s.pipeline.list_workflows_by_pipeline_id(req)

if res.workflow_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListWorkflowsByPipelineIDRequest](../../models/operations/listworkflowsbypipelineidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.ListWorkflowsByPipelineIDResponse](../../models/operations/listworkflowsbypipelineidresponse.md)**


## trigger_pipeline

Triggers a new pipeline on the project.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.TriggerPipelineRequest(
    request_body=operations.TriggerPipelineTriggerPipelineParameters(
        branch='feature/design-new-api',
        parameters={
            "hic": 'excepturi',
        },
        tag='v3.1.4159',
    ),
    project_slug='cum',
)

res = s.pipeline.trigger_pipeline(req)

if res.pipeline_creation is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.TriggerPipelineRequest](../../models/operations/triggerpipelinerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.TriggerPipelineResponse](../../models/operations/triggerpipelineresponse.md)**

