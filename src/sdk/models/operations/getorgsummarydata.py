"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Any, Optional

class GetOrgSummaryDataReportingWindowEnum(str, Enum):
    r"""The time window used to calculate summary metrics."""
    LAST_7_DAYS = 'last-7-days'
    LAST_90_DAYS = 'last-90-days'
    LAST_24_HOURS = 'last-24-hours'
    LAST_30_DAYS = 'last-30-days'
    LAST_60_DAYS = 'last-60-days'


@dataclasses.dataclass
class GetOrgSummaryDataRequest:
    
    org_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org-slug', 'style': 'simple', 'explode': False }})
    r"""Org slug in the form `vcs-slug/org-name`. The `/` characters may be URL-escaped."""
    project_names: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'project-names', 'style': 'form', 'explode': True }})
    r"""List of project names."""
    reporting_window: Optional[GetOrgSummaryDataReportingWindowEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'reporting-window', 'style': 'form', 'explode': True }})
    r"""The time window used to calculate summary metrics."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrgSummaryDataDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrgSummaryData200ApplicationJSONOrgDataMetrics:
    r"""Metrics for a single org metrics."""
    
    success_rate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success_rate') }})
    throughput: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('throughput') }})
    r"""The average number of runs per day."""
    total_credits_used: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_credits_used') }})
    r"""The total credits consumed over the current timeseries interval."""
    total_duration_secs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_duration_secs') }})
    r"""Total duration, in seconds."""
    total_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_runs') }})
    r"""The total number of runs."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrgSummaryData200ApplicationJSONOrgDataTrends:
    r"""Trends for a single org."""
    
    success_rate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success_rate') }})
    r"""The trend value for the success rate."""
    throughput: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('throughput') }})
    r"""Trend value for the average number of runs per day."""
    total_credits_used: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_credits_used') }})
    r"""The trend value for total credits consumed."""
    total_duration_secs: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_duration_secs') }})
    r"""Trend value for total duration."""
    total_runs: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_runs') }})
    r"""The trend value for total number of runs."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrgSummaryData200ApplicationJSONOrgData:
    r"""Aggregated metrics for an org, with trends."""
    
    metrics: GetOrgSummaryData200ApplicationJSONOrgDataMetrics = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metrics') }})
    r"""Metrics for a single org metrics."""
    trends: GetOrgSummaryData200ApplicationJSONOrgDataTrends = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trends') }})
    r"""Trends for a single org."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrgSummaryData200ApplicationJSONOrgProjectDataMetrics:
    r"""Metrics for a single project, across all branches."""
    
    success_rate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success_rate') }})
    total_credits_used: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_credits_used') }})
    r"""The total credits consumed over the current timeseries interval."""
    total_duration_secs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_duration_secs') }})
    r"""Total duration, in seconds."""
    total_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_runs') }})
    r"""The total number of runs."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrgSummaryData200ApplicationJSONOrgProjectDataTrends:
    r"""Trends for a single project, across all branches."""
    
    success_rate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success_rate') }})
    r"""The trend value for the success rate."""
    total_credits_used: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_credits_used') }})
    r"""The trend value for total credits consumed."""
    total_duration_secs: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_duration_secs') }})
    r"""Trend value for total duration."""
    total_runs: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_runs') }})
    r"""The trend value for total number of runs."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrgSummaryData200ApplicationJSONOrgProjectData:
    
    metrics: GetOrgSummaryData200ApplicationJSONOrgProjectDataMetrics = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metrics') }})
    r"""Metrics for a single project, across all branches."""
    project_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_name') }})
    r"""The name of the project."""
    trends: GetOrgSummaryData200ApplicationJSONOrgProjectDataTrends = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trends') }})
    r"""Trends for a single project, across all branches."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetOrgSummaryData200ApplicationJSON:
    r"""Summary metrics with trends for the entire org, and for each project."""
    
    all_projects: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('all_projects') }})
    r"""A list of all the project names in the organization."""
    org_data: GetOrgSummaryData200ApplicationJSONOrgData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_data') }})
    r"""Aggregated metrics for an org, with trends."""
    org_project_data: list[GetOrgSummaryData200ApplicationJSONOrgProjectData] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_project_data') }})
    r"""Metrics for a single project, across all branches"""
    

@dataclasses.dataclass
class GetOrgSummaryDataResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_org_summary_data_200_application_json_object: Optional[GetOrgSummaryData200ApplicationJSON] = dataclasses.field(default=None)
    r"""summary metrics with trends for an entire org and it's projects."""
    get_org_summary_data_default_application_json_object: Optional[GetOrgSummaryDataDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    