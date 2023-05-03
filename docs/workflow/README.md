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
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ApprovePendingApprovalJobByIDRequest(
    approval_request_id='a19f1d17-0513-439d-8808-6a1840394c26',
    id='071f93f5-f064-42da-87af-515cc413aa63',
)

res = s.workflow.approve_pending_approval_job_by_id(req)

if res.message_response is not None:
    # handle response
```

## cancel_workflow

Cancels a running workflow.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CancelWorkflowRequest(
    id='aae8d678-64db-4b67-9fd5-e60b375ed4f6',
)

res = s.workflow.cancel_workflow(req)

if res.message_response is not None:
    # handle response
```

## get_workflow_by_id

Returns summary fields of a workflow by ID.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetWorkflowByIDRequest(
    id='fbee41f3-3317-4fe3-9b60-eb1ea426555b',
)

res = s.workflow.get_workflow_by_id(req)

if res.workflow is not None:
    # handle response
```

## list_workflow_jobs

Returns a sequence of jobs for a workflow.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListWorkflowJobsRequest(
    id='a3c28744-ed53-4b88-b3a8-d8f5c0b2f2fb',
)

res = s.workflow.list_workflow_jobs(req)

if res.workflow_job_list_response is not None:
    # handle response
```

## rerun_workflow

Reruns a workflow.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.RerunWorkflowRequest(
    request_body=operations.RerunWorkflowRerunWorkflowParameters(
        enable_ssh=False,
        from_failed=False,
        jobs=[
            'b194a276-b269-416f-a1f0-8f4294e3698f',
            '447f603e-8b44-45e8-8ca5-5efd20e457e1',
        ],
        sparse_tree=False,
    ),
    id='858b6a89-fbe3-4a5a-a8e4-824d0ab40750',
)

res = s.workflow.rerun_workflow(req)

if res.rerun_workflow_202_application_json_object is not None:
    # handle response
```
