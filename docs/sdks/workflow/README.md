# workflow

### Available Operations

* [approve_pending_approval_job_by_id](#approve_pending_approval_job_by_id) - Approve a job
* [cancel_workflow](#cancel_workflow) - Cancel a workflow
* [get_workflow_by_id](#get_workflow_by_id) - Get a workflow
* [list_workflow_jobs](#list_workflow_jobs) - Get a workflow's jobs
* [rerun_workflow](#rerun_workflow) - Rerun a workflow

## approve_pending_approval_job_by_id

Approves a pending approval job in a workflow.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.ApprovePendingApprovalJobByIDRequest(
    approval_request_id='21aa6f1e-674b-4db0-8f15-756082d68ea1',
    id='9f1d1705-1339-4d08-886a-1840394c2607',
)

res = s.workflow.approve_pending_approval_job_by_id(req)

if res.message_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.ApprovePendingApprovalJobByIDRequest](../../models/operations/approvependingapprovaljobbyidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.ApprovePendingApprovalJobByIDResponse](../../models/operations/approvependingapprovaljobbyidresponse.md)**


## cancel_workflow

Cancels a running workflow.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.CancelWorkflowRequest(
    id='1f93f5f0-642d-4ac7-af51-5cc413aa63aa',
)

res = s.workflow.cancel_workflow(req)

if res.message_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CancelWorkflowRequest](../../models/operations/cancelworkflowrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CancelWorkflowResponse](../../models/operations/cancelworkflowresponse.md)**


## get_workflow_by_id

Returns summary fields of a workflow by ID.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetWorkflowByIDRequest(
    id='e8d67864-dbb6-475f-95e6-0b375ed4f6fb',
)

res = s.workflow.get_workflow_by_id(req)

if res.workflow is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetWorkflowByIDRequest](../../models/operations/getworkflowbyidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetWorkflowByIDResponse](../../models/operations/getworkflowbyidresponse.md)**


## list_workflow_jobs

Returns a sequence of jobs for a workflow.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.ListWorkflowJobsRequest(
    id='ee41f333-17fe-435b-a0eb-1ea426555ba3',
)

res = s.workflow.list_workflow_jobs(req)

if res.workflow_job_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListWorkflowJobsRequest](../../models/operations/listworkflowjobsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListWorkflowJobsResponse](../../models/operations/listworkflowjobsresponse.md)**


## rerun_workflow

Reruns a workflow.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.RerunWorkflowRequest(
    request_body=operations.RerunWorkflowRerunWorkflowParameters(
        enable_ssh=False,
        from_failed=False,
        jobs=[
            '28744ed5-3b88-4f3a-8d8f-5c0b2f2fb7b1',
            '94a276b2-6916-4fe1-b08f-4294e3698f44',
            '7f603e8b-445e-480c-a55e-fd20e457e185',
            '8b6a89fb-e3a5-4aa8-a482-4d0ab4075088',
        ],
        sparse_tree=False,
    ),
    id='e5186206-5e90-44f3-b119-4b8abf603a79',
)

res = s.workflow.rerun_workflow(req)

if res.rerun_workflow_202_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RerunWorkflowRequest](../../models/operations/rerunworkflowrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RerunWorkflowResponse](../../models/operations/rerunworkflowresponse.md)**

