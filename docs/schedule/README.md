# schedule

### Available Operations

* [create_schedule](#create_schedule) - Create a schedule
* [delete_schedule_by_id](#delete_schedule_by_id) - Delete a schedule
* [get_schedule_by_id](#get_schedule_by_id) - Get a schedule
* [list_schedules_for_project](#list_schedules_for_project) - Get all schedules
* [update_schedule](#update_schedule) - Update a schedule

## create_schedule

Creates a schedule and returns the created schedule.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateScheduleRequest(
    request_body=operations.CreateScheduleCreateScheduleParameters(
        attribution_actor="current",
        description="similique",
        name="Cristina Hahn",
        parameters={
            "officiis": "qui",
            "dolorum": "a",
            "esse": "harum",
            "iusto": "ipsum",
        },
        timetable=operations.CreateScheduleCreateScheduleParametersTimetable2(
            days_of_month=[
                229442,
                730856,
                880298,
                253941,
            ],
            days_of_week=[
                "SAT",
                "FRI",
            ],
            hours_of_day=[
                471752,
                25662,
                711584,
            ],
            months=[
                "NOV",
            ],
            per_hour=424685,
        ),
    ),
    project_slug="libero",
)

res = s.schedule.create_schedule(req)

if res.schedule is not None:
    # handle response
```

## delete_schedule_by_id

Deletes the schedule by id.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteScheduleByIDRequest(
    schedule_id="5a73429c-db1a-4842-abb6-79d2322715bf",
)

res = s.schedule.delete_schedule_by_id(req)

if res.message_response is not None:
    # handle response
```

## get_schedule_by_id

Get a schedule by id.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetScheduleByIDRequest(
    schedule_id="0cbb1e31-b8b9-40f3-843a-1108e0adcf4b",
)

res = s.schedule.get_schedule_by_id(req)

if res.schedule is not None:
    # handle response
```

## list_schedules_for_project

Returns all schedules for this project.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListSchedulesForProjectRequest(
    page_token="cupiditate",
    project_slug="qui",
)

res = s.schedule.list_schedules_for_project(req)

if res.list_schedules_for_project_200_application_json_object is not None:
    # handle response
```

## update_schedule

Updates a schedule and returns the updated schedule.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateScheduleRequest(
    request_body=operations.UpdateScheduleUpdateScheduleParameters(
        attribution_actor="current",
        description="quae",
        name="Darren McClure",
        parameters={
            "omnis": "quis",
            "ipsum": "delectus",
            "voluptate": "consectetur",
            "vero": "tenetur",
        },
        timetable=operations.UpdateScheduleUpdateScheduleParametersTimetable(
            days_of_month=[
                941378,
                715561,
            ],
            days_of_week=[
                "MON",
                "THU",
                "THU",
                "FRI",
            ],
            hours_of_day=[
                293020,
                844550,
            ],
            months=[
                "DEC",
                "APR",
                "AUG",
                "MAR",
            ],
            per_hour=974259,
        ),
    ),
    schedule_id="5d2cff7c-70a4-4562-ad43-6813f16d9f5f",
)

res = s.schedule.update_schedule(req)

if res.schedule is not None:
    # handle response
```
