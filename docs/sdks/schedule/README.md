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
        api_key_header="",
    ),
)

req = operations.CreateScheduleRequest(
    request_body=operations.CreateScheduleCreateScheduleParameters(
        attribution_actor=operations.CreateScheduleCreateScheduleParametersAttributionActor.CURRENT,
        description='soluta',
        name='Ted Kling',
        parameters={
            "necessitatibus": 'distinctio',
            "asperiores": 'nihil',
            "ipsum": 'voluptate',
        },
        timetable=operations.CreateScheduleCreateScheduleParametersTimetable2(
            days_of_month=[
                263322,
                137220,
                20651,
                229219,
            ],
            days_of_week=[
                operations.CreateScheduleCreateScheduleParametersTimetable2DaysOfWeek.FRI,
                operations.CreateScheduleCreateScheduleParametersTimetable2DaysOfWeek.SUN,
                operations.CreateScheduleCreateScheduleParametersTimetable2DaysOfWeek.FRI,
                operations.CreateScheduleCreateScheduleParametersTimetable2DaysOfWeek.SUN,
            ],
            hours_of_day=[
                588317,
                324683,
                831049,
            ],
            months=[
                operations.CreateScheduleCreateScheduleParametersTimetable2Months.APR,
                operations.CreateScheduleCreateScheduleParametersTimetable2Months.MAR,
                operations.CreateScheduleCreateScheduleParametersTimetable2Months.JAN,
            ],
            per_hour=311860,
        ),
    ),
    project_slug='tempora',
)

res = s.schedule.create_schedule(req)

if res.schedule is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateScheduleRequest](../../models/operations/createschedulerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateScheduleResponse](../../models/operations/createscheduleresponse.md)**


## delete_schedule_by_id

Deletes the schedule by id.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.DeleteScheduleByIDRequest(
    schedule_id='6ce2af7a-73cf-43be-853f-870b326b5a73',
)

res = s.schedule.delete_schedule_by_id(req)

if res.message_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteScheduleByIDRequest](../../models/operations/deleteschedulebyidrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.DeleteScheduleByIDResponse](../../models/operations/deleteschedulebyidresponse.md)**


## get_schedule_by_id

Get a schedule by id.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.GetScheduleByIDRequest(
    schedule_id='429cdb1a-8422-4bb6-b9d2-322715bf0cbb',
)

res = s.schedule.get_schedule_by_id(req)

if res.schedule is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetScheduleByIDRequest](../../models/operations/getschedulebyidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetScheduleByIDResponse](../../models/operations/getschedulebyidresponse.md)**


## list_schedules_for_project

Returns all schedules for this project.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.ListSchedulesForProjectRequest(
    page_token='et',
    project_slug='saepe',
)

res = s.schedule.list_schedules_for_project(req)

if res.list_schedules_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListSchedulesForProjectRequest](../../models/operations/listschedulesforprojectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ListSchedulesForProjectResponse](../../models/operations/listschedulesforprojectresponse.md)**


## update_schedule

Updates a schedule and returns the updated schedule.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        api_key_header="",
    ),
)

req = operations.UpdateScheduleRequest(
    request_body=operations.UpdateScheduleUpdateScheduleParameters(
        attribution_actor=operations.UpdateScheduleUpdateScheduleParametersAttributionActor.CURRENT,
        description='ipsum',
        name='Gayle Lueilwitz',
        parameters={
            "delectus": 'dolorem',
        },
        timetable=operations.UpdateScheduleUpdateScheduleParametersTimetable(
            days_of_month=[
                286915,
                240829,
            ],
            days_of_week=[
                operations.UpdateScheduleUpdateScheduleParametersTimetableDaysOfWeek.TUE,
                operations.UpdateScheduleUpdateScheduleParametersTimetableDaysOfWeek.TUE,
                operations.UpdateScheduleUpdateScheduleParametersTimetableDaysOfWeek.TUE,
            ],
            hours_of_day=[
                929530,
                9240,
                669917,
            ],
            months=[
                operations.UpdateScheduleUpdateScheduleParametersTimetableMonths.AUG,
                operations.UpdateScheduleUpdateScheduleParametersTimetableMonths.JUL,
                operations.UpdateScheduleUpdateScheduleParametersTimetableMonths.JUN,
                operations.UpdateScheduleUpdateScheduleParametersTimetableMonths.SEP,
            ],
            per_hour=586410,
        ),
    ),
    schedule_id='21879fce-953f-473e-b7fb-c7abd74dd39c',
)

res = s.schedule.update_schedule(req)

if res.schedule is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateScheduleRequest](../../models/operations/updateschedulerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateScheduleResponse](../../models/operations/updatescheduleresponse.md)**

