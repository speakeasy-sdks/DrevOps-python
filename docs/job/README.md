# job

### Available Operations

* [cancel_job](#cancel_job) - Cancel job
* [get_job_artifacts](#get_job_artifacts) - Get a job's artifacts
* [get_job_details](#get_job_details) - Get job details
* [get_tests](#get_tests) - Get test metadata

## cancel_job

Cancel job with a given job number.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CancelJobRequest(
    job_number="nihil",
    project_slug="repellat",
)

res = s.job.cancel_job(req)

if res.message_response is not None:
    # handle response
```

## get_job_artifacts

Returns a job's artifacts.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetJobArtifactsRequest(
    job_number="quibusdam",
    project_slug="sed",
)

res = s.job.get_job_artifacts(req)

if res.artifact_list_response is not None:
    # handle response
```

## get_job_details

Returns job details.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetJobDetailsRequest(
    job_number="saepe",
    project_slug="pariatur",
)

res = s.job.get_job_details(req)

if res.job_details is not None:
    # handle response
```

## get_tests

Get test metadata for a build. In the rare case where there is more than 250MB of test data on the job, no results will be returned.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetTestsRequest(
    job_number="accusantium",
    project_slug="consequuntur",
)

res = s.job.get_tests(req)

if res.tests_response is not None:
    # handle response
```
