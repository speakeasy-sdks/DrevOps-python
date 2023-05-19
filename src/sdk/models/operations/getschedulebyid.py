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


@dataclasses.dataclass
class GetScheduleByIDRequest:
    
    schedule_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'schedule-id', 'style': 'simple', 'explode': False }})
    r"""The unique ID of the schedule."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduleByIDDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduleByIDScheduleUser:
    r"""The attribution actor who will run the scheduled pipeline."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique ID of the user."""
    login: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('login') }})
    r"""The login information for the user on the VCS."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the user."""
    
class GetScheduleByIDScheduleTimetable2DaysOfWeek(str, Enum):
    r"""Day in a week, in three letters format"""
    TUE = 'TUE'
    SAT = 'SAT'
    SUN = 'SUN'
    MON = 'MON'
    THU = 'THU'
    WED = 'WED'
    FRI = 'FRI'

class GetScheduleByIDScheduleTimetable2Months(str, Enum):
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
class GetScheduleByIDScheduleTimetable2:
    r"""Timetable that specifies when a schedule triggers."""
    
    days_of_month: list[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-month') }})
    r"""Days in a month in which the schedule triggers. This is mutually exclusive with days in a week."""
    hours_of_day: list[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hours-of-day') }})
    r"""Hours in a day in which the schedule triggers."""
    per_hour: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per-hour') }})
    r"""Number of times a schedule triggers per hour, value must be between 1 and 60"""
    days_of_week: Optional[list[GetScheduleByIDScheduleTimetable2DaysOfWeek]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-week'), 'exclude': lambda f: f is None }})
    r"""Days in a week in which the schedule triggers."""
    months: Optional[list[GetScheduleByIDScheduleTimetable2Months]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('months'), 'exclude': lambda f: f is None }})
    r"""Months in which the schedule triggers."""
    
class GetScheduleByIDScheduleTimetable1DaysOfWeek(str, Enum):
    r"""Day in a week, in three letters format"""
    TUE = 'TUE'
    SAT = 'SAT'
    SUN = 'SUN'
    MON = 'MON'
    THU = 'THU'
    WED = 'WED'
    FRI = 'FRI'

class GetScheduleByIDScheduleTimetable1Months(str, Enum):
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
class GetScheduleByIDScheduleTimetable1:
    r"""Timetable that specifies when a schedule triggers."""
    
    days_of_week: list[GetScheduleByIDScheduleTimetable1DaysOfWeek] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-week') }})
    r"""Days in a week in which the schedule triggers."""
    hours_of_day: list[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hours-of-day') }})
    r"""Hours in a day in which the schedule triggers."""
    per_hour: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per-hour') }})
    r"""Number of times a schedule triggers per hour, value must be between 1 and 60"""
    days_of_month: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days-of-month'), 'exclude': lambda f: f is None }})
    r"""Days in a month in which the schedule triggers. This is mutually exclusive with days in a week."""
    months: Optional[list[GetScheduleByIDScheduleTimetable1Months]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('months'), 'exclude': lambda f: f is None }})
    r"""Months in which the schedule triggers."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetScheduleByIDSchedule:
    r"""A schedule response"""
    
    actor: GetScheduleByIDScheduleUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actor') }})
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
class GetScheduleByIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_schedule_by_id_default_application_json_object: Optional[GetScheduleByIDDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schedule: Optional[GetScheduleByIDSchedule] = dataclasses.field(default=None)
    r"""A schedule object."""
    