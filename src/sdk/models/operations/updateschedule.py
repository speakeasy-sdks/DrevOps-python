"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Any, Optional

class UpdateScheduleUpdateScheduleParametersAttributionActorEnum(str, Enum):
    r"""The attribution-actor of the scheduled pipeline."""
    CURRENT = 'current'
    SYSTEM = 'system'

class UpdateScheduleUpdateScheduleParametersTimetableDaysOfWeekEnum(str, Enum):
    r"""Day in a week, in three letters format"""
    TUE = 'TUE'
    SAT = 'SAT'
    SUN = 'SUN'
    MON = 'MON'
    THU = 'THU'
    WED = 'WED'
    FRI = 'FRI'

class UpdateScheduleUpdateScheduleParametersTimetableMonthsEnum(str, Enum):
    r"""Month, in three letters format."""
    MAR = 'MAR'
    NOV = 'NOV'
    DEC = 'DEC'
    JUN = 'JUN'
    MAY = 'MAY'
    OCT = 'OCT'
    FEB = 'FEB'
    APR = 'APR'
    SEP = 'SEP'
    AUG = 'AUG'
    JAN = 'JAN'
    JUL = 'JUL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateScheduleUpdateScheduleParametersTimetable:
    r"""Timetable that specifies when a schedule triggers."""
    
    days_of_month: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-month'), 'exclude': lambda f: f is None }})
    r"""Days in a month in which the schedule triggers. This is mutually exclusive with days in a week."""
    days_of_week: Optional[list[UpdateScheduleUpdateScheduleParametersTimetableDaysOfWeekEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-week'), 'exclude': lambda f: f is None }})
    r"""Days in a week in which the schedule triggers."""
    hours_of_day: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hours-of-day'), 'exclude': lambda f: f is None }})
    r"""Hours in a day in which the schedule triggers."""
    months: Optional[list[UpdateScheduleUpdateScheduleParametersTimetableMonthsEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('months'), 'exclude': lambda f: f is None }})
    r"""Months in which the schedule triggers."""
    per_hour: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per-hour'), 'exclude': lambda f: f is None }})
    r"""Number of times a schedule triggers per hour, value must be between 1 and 60"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateScheduleUpdateScheduleParameters:
    r"""The parameters for an update schedule request"""
    
    attribution_actor: Optional[UpdateScheduleUpdateScheduleParametersAttributionActorEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attribution-actor'), 'exclude': lambda f: f is None }})
    r"""The attribution-actor of the scheduled pipeline."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the schedule."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the schedule."""
    parameters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters'), 'exclude': lambda f: f is None }})
    r"""Pipeline parameters represented as key-value pairs. Must contain branch or tag."""
    timetable: Optional[UpdateScheduleUpdateScheduleParametersTimetable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timetable'), 'exclude': lambda f: f is None }})
    r"""Timetable that specifies when a schedule triggers."""
    

@dataclasses.dataclass
class UpdateScheduleRequest:
    
    schedule_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'schedule-id', 'style': 'simple', 'explode': False }})
    r"""The unique ID of the schedule."""
    request_body: Optional[UpdateScheduleUpdateScheduleParameters] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateScheduleDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateScheduleScheduleUser:
    r"""The attribution actor who will run the scheduled pipeline."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique ID of the user."""
    login: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('login') }})
    r"""The login information for the user on the VCS."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the user."""
    
class UpdateScheduleScheduleTimetable2DaysOfWeekEnum(str, Enum):
    r"""Day in a week, in three letters format"""
    TUE = 'TUE'
    SAT = 'SAT'
    SUN = 'SUN'
    MON = 'MON'
    THU = 'THU'
    WED = 'WED'
    FRI = 'FRI'

class UpdateScheduleScheduleTimetable2MonthsEnum(str, Enum):
    r"""Month, in three letters format."""
    MAR = 'MAR'
    NOV = 'NOV'
    DEC = 'DEC'
    JUN = 'JUN'
    MAY = 'MAY'
    OCT = 'OCT'
    FEB = 'FEB'
    APR = 'APR'
    SEP = 'SEP'
    AUG = 'AUG'
    JAN = 'JAN'
    JUL = 'JUL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateScheduleScheduleTimetable2:
    r"""Timetable that specifies when a schedule triggers."""
    
    days_of_month: list[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-month') }})
    r"""Days in a month in which the schedule triggers. This is mutually exclusive with days in a week."""
    hours_of_day: list[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hours-of-day') }})
    r"""Hours in a day in which the schedule triggers."""
    per_hour: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per-hour') }})
    r"""Number of times a schedule triggers per hour, value must be between 1 and 60"""
    days_of_week: Optional[list[UpdateScheduleScheduleTimetable2DaysOfWeekEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-week'), 'exclude': lambda f: f is None }})
    r"""Days in a week in which the schedule triggers."""
    months: Optional[list[UpdateScheduleScheduleTimetable2MonthsEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('months'), 'exclude': lambda f: f is None }})
    r"""Months in which the schedule triggers."""
    
class UpdateScheduleScheduleTimetable1DaysOfWeekEnum(str, Enum):
    r"""Day in a week, in three letters format"""
    TUE = 'TUE'
    SAT = 'SAT'
    SUN = 'SUN'
    MON = 'MON'
    THU = 'THU'
    WED = 'WED'
    FRI = 'FRI'

class UpdateScheduleScheduleTimetable1MonthsEnum(str, Enum):
    r"""Month, in three letters format."""
    MAR = 'MAR'
    NOV = 'NOV'
    DEC = 'DEC'
    JUN = 'JUN'
    MAY = 'MAY'
    OCT = 'OCT'
    FEB = 'FEB'
    APR = 'APR'
    SEP = 'SEP'
    AUG = 'AUG'
    JAN = 'JAN'
    JUL = 'JUL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateScheduleScheduleTimetable1:
    r"""Timetable that specifies when a schedule triggers."""
    
    days_of_week: list[UpdateScheduleScheduleTimetable1DaysOfWeekEnum] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-week') }})
    r"""Days in a week in which the schedule triggers."""
    hours_of_day: list[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hours-of-day') }})
    r"""Hours in a day in which the schedule triggers."""
    per_hour: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per-hour') }})
    r"""Number of times a schedule triggers per hour, value must be between 1 and 60"""
    days_of_month: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-month'), 'exclude': lambda f: f is None }})
    r"""Days in a month in which the schedule triggers. This is mutually exclusive with days in a week."""
    months: Optional[list[UpdateScheduleScheduleTimetable1MonthsEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('months'), 'exclude': lambda f: f is None }})
    r"""Months in which the schedule triggers."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateScheduleSchedule:
    r"""A schedule response"""
    
    actor: UpdateScheduleScheduleUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actor') }})
    r"""The attribution actor who will run the scheduled pipeline."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created-at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the pipeline was created."""
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Description of the schedule."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique ID of the schedule."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the schedule."""
    parameters: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters') }})
    r"""Pipeline parameters represented as key-value pairs. Must contain branch or tag."""
    project_slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project-slug') }})
    r"""The project-slug for the schedule"""
    timetable: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timetable') }})
    r"""Timetable that specifies when a schedule triggers."""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated-at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the pipeline was last updated."""
    

@dataclasses.dataclass
class UpdateScheduleResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schedule: Optional[UpdateScheduleSchedule] = dataclasses.field(default=None)
    r"""A schedule object."""
    update_schedule_default_application_json_object: Optional[UpdateScheduleDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    