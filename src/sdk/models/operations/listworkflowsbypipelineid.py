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


@dataclasses.dataclass
class ListWorkflowsByPipelineIDRequest:
    
    pipeline_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pipeline-id', 'style': 'simple', 'explode': False }})
    r"""The unique ID of the pipeline."""
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page-token', 'style': 'form', 'explode': True }})
    r"""A token to retrieve the next page of results."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListWorkflowsByPipelineIDDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    
class ListWorkflowsByPipelineIDWorkflowListResponseWorkflowStatus(str, Enum):
    r"""The current status of the workflow."""
    SUCCESS = 'success'
    RUNNING = 'running'
    NOT_RUN = 'not_run'
    FAILED = 'failed'
    ERROR = 'error'
    FAILING = 'failing'
    ON_HOLD = 'on_hold'
    CANCELED = 'canceled'
    UNAUTHORIZED = 'unauthorized'

class ListWorkflowsByPipelineIDWorkflowListResponseWorkflowTag(str, Enum):
    r"""Tag used for the workflow"""
    SETUP = 'setup'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListWorkflowsByPipelineIDWorkflowListResponseWorkflow:
    r"""A workflow"""
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the workflow was created."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique ID of the workflow."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the workflow."""
    pipeline_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_id') }})
    r"""The ID of the pipeline this workflow belongs to."""
    pipeline_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_number') }})
    r"""The number of the pipeline this workflow belongs to."""
    project_slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_slug') }})
    r"""The project-slug for the pipeline this workflow belongs to."""
    started_by: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('started_by') }})
    status: ListWorkflowsByPipelineIDWorkflowListResponseWorkflowStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The current status of the workflow."""
    stopped_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stopped_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the workflow stopped."""
    canceled_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canceled_by'), 'exclude': lambda f: f is None }})
    errored_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errored_by'), 'exclude': lambda f: f is None }})
    tag: Optional[ListWorkflowsByPipelineIDWorkflowListResponseWorkflowTag] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag'), 'exclude': lambda f: f is None }})
    r"""Tag used for the workflow"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListWorkflowsByPipelineIDWorkflowListResponse:
    r"""A list of workflows and associated pagination token."""
    
    items: list[ListWorkflowsByPipelineIDWorkflowListResponseWorkflow] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    r"""A list of workflows."""
    next_page_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page_token') }})
    r"""A token to pass as a `page-token` query parameter to return the next page of results."""
    

@dataclasses.dataclass
class ListWorkflowsByPipelineIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_workflows_by_pipeline_id_default_application_json_object: Optional[ListWorkflowsByPipelineIDDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    workflow_list_response: Optional[ListWorkflowsByPipelineIDWorkflowListResponse] = dataclasses.field(default=None)
    r"""A paginated list of workflow objects."""
    