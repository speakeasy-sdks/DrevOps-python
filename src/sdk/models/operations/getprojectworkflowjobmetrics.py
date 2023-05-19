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
from typing import Optional

class GetProjectWorkflowJobMetricsReportingWindow(str, Enum):
    r"""The time window used to calculate summary metrics."""
    LAST_7_DAYS = 'last-7-days'
    LAST_90_DAYS = 'last-90-days'
    LAST_24_HOURS = 'last-24-hours'
    LAST_30_DAYS = 'last-30-days'
    LAST_60_DAYS = 'last-60-days'


@dataclasses.dataclass
class GetProjectWorkflowJobMetricsRequest:
    
    project_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project-slug', 'style': 'simple', 'explode': False }})
    r"""Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped."""
    workflow_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workflow-name', 'style': 'simple', 'explode': False }})
    r"""The name of the workflow."""
    all_branches: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'all-branches', 'style': 'form', 'explode': True }})
    r"""Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter."""
    branch: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'branch', 'style': 'form', 'explode': True }})
    r"""The name of a vcs branch. If not passed we will scope the API call to the default branch."""
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page-token', 'style': 'form', 'explode': True }})
    r"""A token to retrieve the next page of results."""
    reporting_window: Optional[GetProjectWorkflowJobMetricsReportingWindow] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'reporting-window', 'style': 'form', 'explode': True }})
    r"""The time window used to calculate summary metrics."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowJobMetricsDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowJobMetrics200ApplicationJSONItemsMetricsDurationMetrics:
    r"""Metrics relating to the duration of runs for a workflow job."""
    
    max: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max') }})
    r"""The max duration, in seconds, among a group of runs."""
    mean: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mean') }})
    r"""The mean duration, in seconds, among a group of runs."""
    median: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('median') }})
    r"""The median duration, in seconds, among a group of runs."""
    min: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('min') }})
    r"""The minimum duration, in seconds, among a group of runs."""
    p95: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p95') }})
    r"""The 95th percentile duration, in seconds, among a group of runs."""
    standard_deviation: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('standard_deviation') }})
    r"""The standard deviation, in seconds, among a group of runs."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowJobMetrics200ApplicationJSONItemsMetrics:
    r"""Metrics relating to a workflow job's runs."""
    
    duration_metrics: GetProjectWorkflowJobMetrics200ApplicationJSONItemsMetricsDurationMetrics = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration_metrics') }})
    r"""Metrics relating to the duration of runs for a workflow job."""
    failed_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_runs') }})
    r"""The number of failed runs."""
    success_rate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success_rate') }})
    successful_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('successful_runs') }})
    r"""The number of successful runs."""
    throughput: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('throughput') }})
    r"""The average number of runs per day."""
    total_credits_used: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_credits_used') }})
    r"""The total credits consumed by the job in the aggregation window. Note that Insights is not a real time financial reporting tool and should not be used for credit reporting."""
    total_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_runs') }})
    r"""The total number of runs."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowJobMetrics200ApplicationJSONItems:
    
    metrics: GetProjectWorkflowJobMetrics200ApplicationJSONItemsMetrics = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metrics') }})
    r"""Metrics relating to a workflow job's runs."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the job."""
    window_end: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('window_end'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The end of the aggregation window for job metrics."""
    window_start: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('window_start'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The start of the aggregation window for job metrics."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowJobMetrics200ApplicationJSON:
    r"""Paginated workflow job summary metrics."""
    
    items: list[GetProjectWorkflowJobMetrics200ApplicationJSONItems] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    r"""Job summary metrics."""
    next_page_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page_token') }})
    r"""A token to pass as a `page-token` query parameter to return the next page of results."""
    

@dataclasses.dataclass
class GetProjectWorkflowJobMetricsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_project_workflow_job_metrics_200_application_json_object: Optional[GetProjectWorkflowJobMetrics200ApplicationJSON] = dataclasses.field(default=None)
    r"""A paginated list of summary metrics by workflow job."""
    get_project_workflow_job_metrics_default_application_json_object: Optional[GetProjectWorkflowJobMetricsDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    