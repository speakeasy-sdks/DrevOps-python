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
class ListMyPipelinesRequest:
    
    project_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project-slug', 'style': 'simple', 'explode': False }})
    r"""Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped."""
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page-token', 'style': 'form', 'explode': True }})
    r"""A token to retrieve the next page of results."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListMyPipelinesDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    
class ListMyPipelinesPipelineListResponsePipelineErrorsTypeEnum(str, Enum):
    r"""The type of error."""
    CONFIG = 'config'
    CONFIG_FETCH = 'config-fetch'
    TIMEOUT = 'timeout'
    PERMISSION = 'permission'
    OTHER = 'other'
    PLAN = 'plan'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListMyPipelinesPipelineListResponsePipelineErrors:
    r"""An error with a type and message."""
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""A human-readable error message."""
    type: ListMyPipelinesPipelineListResponsePipelineErrorsTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of error."""
    
class ListMyPipelinesPipelineListResponsePipelineStateEnum(str, Enum):
    r"""The current state of the pipeline."""
    CREATED = 'created'
    ERRORED = 'errored'
    SETUP_PENDING = 'setup-pending'
    SETUP = 'setup'
    PENDING = 'pending'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListMyPipelinesPipelineListResponsePipelineTriggerActor:
    r"""The user who triggered the Pipeline."""
    
    avatar_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avatar_url') }})
    r"""URL to the user's avatar on the VCS"""
    login: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('login') }})
    r"""The login information for the user on the VCS."""
    
class ListMyPipelinesPipelineListResponsePipelineTriggerTypeEnum(str, Enum):
    r"""The type of trigger."""
    SCHEDULED_PIPELINE = 'scheduled_pipeline'
    EXPLICIT = 'explicit'
    API = 'api'
    WEBHOOK = 'webhook'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListMyPipelinesPipelineListResponsePipelineTrigger:
    r"""A summary of the trigger."""
    
    actor: ListMyPipelinesPipelineListResponsePipelineTriggerActor = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actor') }})
    r"""The user who triggered the Pipeline."""
    received_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('received_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the trigger was received."""
    type: ListMyPipelinesPipelineListResponsePipelineTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of trigger."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListMyPipelinesPipelineListResponsePipelineVcsCommit:
    r"""The latest commit in the pipeline."""
    
    body: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('body') }})
    r"""The body of the commit message."""
    subject: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subject') }})
    r"""The subject of the commit message."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListMyPipelinesPipelineListResponsePipelineVcs:
    r"""VCS information for the pipeline."""
    
    origin_repository_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origin_repository_url') }})
    r"""URL for the repository where the trigger originated. For fork-PR pipelines, this is the URL to the fork. For other pipelines the `origin_` and `target_repository_url`s will be the same."""
    provider_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider_name') }})
    r"""Name of the VCS provider (e.g. GitHub, Bitbucket)."""
    revision: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revision') }})
    r"""The code revision the pipeline ran."""
    target_repository_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_repository_url') }})
    r"""URL for the repository the trigger targets (i.e. the repository where the PR will be merged). For fork-PR pipelines, this is the URL to the parent repo. For other pipelines, the `origin_` and `target_repository_url`s will be the same."""
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    r"""The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only)."""
    commit: Optional[ListMyPipelinesPipelineListResponsePipelineVcsCommit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commit'), 'exclude': lambda f: f is None }})
    r"""The latest commit in the pipeline."""
    review_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('review_id'), 'exclude': lambda f: f is None }})
    r"""The code review id."""
    review_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('review_url'), 'exclude': lambda f: f is None }})
    r"""The code review URL."""
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag'), 'exclude': lambda f: f is None }})
    r"""The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListMyPipelinesPipelineListResponsePipeline:
    r"""A pipeline response."""
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the pipeline was created."""
    errors: list[ListMyPipelinesPipelineListResponsePipelineErrors] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors') }})
    r"""A sequence of errors that have occurred within the pipeline."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique ID of the pipeline."""
    number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number') }})
    r"""The number of the pipeline."""
    project_slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_slug') }})
    r"""The project-slug for the pipeline."""
    state: ListMyPipelinesPipelineListResponsePipelineStateEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    r"""The current state of the pipeline."""
    trigger: ListMyPipelinesPipelineListResponsePipelineTrigger = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trigger') }})
    r"""A summary of the trigger."""
    trigger_parameters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trigger_parameters'), 'exclude': lambda f: f is None }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date and time the pipeline was last updated."""
    vcs: Optional[ListMyPipelinesPipelineListResponsePipelineVcs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vcs'), 'exclude': lambda f: f is None }})
    r"""VCS information for the pipeline."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListMyPipelinesPipelineListResponse:
    r"""List of pipelines"""
    
    items: list[ListMyPipelinesPipelineListResponsePipeline] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    next_page_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page_token') }})
    r"""A token to pass as a `page-token` query parameter to return the next page of results."""
    

@dataclasses.dataclass
class ListMyPipelinesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_my_pipelines_default_application_json_object: Optional[ListMyPipelinesDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    pipeline_list_response: Optional[ListMyPipelinesPipelineListResponse] = dataclasses.field(default=None)
    r"""A sequence of pipelines."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    