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
        api_key_header="",
    ),
)

req = operations.CancelJobRequest(
    job_number='ullam',
    project_slug='provident',
)

res = s.job.cancel_job(req)

if res.message_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.CancelJobRequest](../../models/operations/canceljobrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CancelJobResponse](../../models/operations/canceljobresponse.md)**


## get_job_artifacts

Returns a job's artifacts.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetJobArtifactsRequest(
    job_number='quos',
    project_slug='sint',
)

res = s.job.get_job_artifacts(req)

if res.artifact_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetJobArtifactsRequest](../../models/operations/getjobartifactsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetJobArtifactsResponse](../../models/operations/getjobartifactsresponse.md)**


## get_job_details

Returns job details.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetJobDetailsRequest(
    job_number='accusantium',
    project_slug='mollitia',
)

res = s.job.get_job_details(req)

if res.job_details is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetJobDetailsRequest](../../models/operations/getjobdetailsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetJobDetailsResponse](../../models/operations/getjobdetailsresponse.md)**


## get_tests

Get test metadata for a build. In the rare case where there is more than 250MB of test data on the job, no results will be returned.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetTestsRequest(
    job_number='reiciendis',
    project_slug='mollitia',
)

res = s.job.get_tests(req)

if res.tests_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetTestsRequest](../../models/operations/gettestsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetTestsResponse](../../models/operations/gettestsresponse.md)**

