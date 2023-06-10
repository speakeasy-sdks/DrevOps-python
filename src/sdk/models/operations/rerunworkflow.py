"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RerunWorkflowRerunWorkflowParameters:
    r"""The information you can supply when rerunning a workflow."""
    enable_ssh: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_ssh'), 'exclude': lambda f: f is None }})
    r"""Whether to enable SSH access for the triggering user on the newly-rerun job. Requires the jobs parameter to be used and so is mutually exclusive with the from_failed parameter."""
    from_failed: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_failed'), 'exclude': lambda f: f is None }})
    r"""Whether to rerun the workflow from the failed job. Mutually exclusive with the jobs parameter."""
    jobs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobs'), 'exclude': lambda f: f is None }})
    r"""A list of job IDs to rerun."""
    sparse_tree: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sparse_tree'), 'exclude': lambda f: f is None }})
    r"""Completes rerun using sparse trees logic, an optimization for workflows that have disconnected subgraphs. Requires jobs parameter and so is mutually exclusive with the from_failed parameter."""
    




@dataclasses.dataclass
class RerunWorkflowRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The unique ID of the workflow."""
    request_body: Optional[RerunWorkflowRerunWorkflowParameters] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RerunWorkflowDefaultApplicationJSON:
    r"""Error response."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RerunWorkflow202ApplicationJSON:
    r"""A response to rerunning a workflow"""
    workflow_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow_id') }})
    r"""The ID of the newly-created workflow."""
    




@dataclasses.dataclass
class RerunWorkflowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    rerun_workflow_202_application_json_object: Optional[RerunWorkflow202ApplicationJSON] = dataclasses.field(default=None)
    r"""A confirmation message."""
    rerun_workflow_default_application_json_object: Optional[RerunWorkflowDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    

