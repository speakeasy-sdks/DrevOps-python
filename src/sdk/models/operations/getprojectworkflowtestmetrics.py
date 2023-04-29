"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclasses.dataclass
class GetProjectWorkflowTestMetricsRequest:
    
    project_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project-slug', 'style': 'simple', 'explode': False }})
    r"""Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped."""
    workflow_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workflow-name', 'style': 'simple', 'explode': False }})
    r"""The name of the workflow."""
    all_branches: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'all-branches', 'style': 'form', 'explode': True }})
    r"""Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter."""
    branch: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'branch', 'style': 'form', 'explode': True }})
    r"""The name of a vcs branch. If not passed we will scope the API call to the default branch."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowTestMetricsDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowTestMetrics200ApplicationJSONMostFailedTests:
    
    classname: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classname') }})
    r"""The class the test belongs to."""
    failed_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_runs') }})
    r"""The number of times the test failed"""
    file: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file') }})
    r"""The file the test belongs to."""
    flaky: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flaky') }})
    r"""Whether the test is flaky."""
    job_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job_name') }})
    r"""The name of the job."""
    p95_duration: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p95_duration') }})
    r"""The 95th percentile duration, in seconds, among a group of test runs."""
    source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    r"""The source of the test."""
    test_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test_name') }})
    r"""The name of the test."""
    total_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_runs') }})
    r"""The total number of times the test was run."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowTestMetrics200ApplicationJSONSlowestTests:
    
    classname: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classname') }})
    r"""The class the test belongs to."""
    failed_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_runs') }})
    r"""The number of times the test failed"""
    file: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file') }})
    r"""The file the test belongs to."""
    flaky: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flaky') }})
    r"""Whether the test is flaky."""
    job_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job_name') }})
    r"""The name of the job."""
    p95_duration: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p95_duration') }})
    r"""The 95th percentile duration, in seconds, among a group of test runs."""
    source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    r"""The source of the test."""
    test_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test_name') }})
    r"""The name of the test."""
    total_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_runs') }})
    r"""The total number of times the test was run."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowTestMetrics200ApplicationJSONTestRunsTestCounts:
    r"""Test counts for a given pipeline number"""
    
    error: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    r"""The number of tests with the error status"""
    failure: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failure') }})
    r"""The number of tests with the failure status"""
    skipped: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skipped') }})
    r"""The number of tests with the skipped status"""
    success: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success') }})
    r"""The number of tests with the success status"""
    total: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    r"""The total number of tests"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowTestMetrics200ApplicationJSONTestRuns:
    
    pipeline_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_number') }})
    r"""The number of the pipeline associated with the provided test counts"""
    success_rate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success_rate') }})
    r"""The success rate calculated from test counts"""
    test_counts: GetProjectWorkflowTestMetrics200ApplicationJSONTestRunsTestCounts = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test_counts') }})
    r"""Test counts for a given pipeline number"""
    workflow_id: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow_id') }})
    r"""The ID of the workflow associated with the provided test counts"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectWorkflowTestMetrics200ApplicationJSON:
    r"""Project level test metrics response"""
    
    average_test_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('average_test_count') }})
    r"""The average number of tests executed per run"""
    most_failed_tests: list[GetProjectWorkflowTestMetrics200ApplicationJSONMostFailedTests] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('most_failed_tests') }})
    r"""Metrics for the most frequently failing tests"""
    most_failed_tests_extra: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('most_failed_tests_extra') }})
    r"""The number of tests with the same success rate being omitted from most_failed_tests"""
    slowest_tests: list[GetProjectWorkflowTestMetrics200ApplicationJSONSlowestTests] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slowest_tests') }})
    r"""Metrics for the slowest running tests"""
    slowest_tests_extra: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slowest_tests_extra') }})
    r"""The number of tests with the same duration rate being omitted from slowest_tests"""
    test_runs: list[GetProjectWorkflowTestMetrics200ApplicationJSONTestRuns] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test_runs') }})
    r"""Test counts grouped by pipeline number and workflow id"""
    total_test_runs: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_test_runs') }})
    r"""The total number of test runs"""
    

@dataclasses.dataclass
class GetProjectWorkflowTestMetricsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_project_workflow_test_metrics_200_application_json_object: Optional[GetProjectWorkflowTestMetrics200ApplicationJSON] = dataclasses.field(default=None)
    r"""A list of test metrics by workflow"""
    get_project_workflow_test_metrics_default_application_json_object: Optional[GetProjectWorkflowTestMetricsDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    