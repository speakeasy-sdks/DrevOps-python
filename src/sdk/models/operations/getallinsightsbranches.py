"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclasses.dataclass
class GetAllInsightsBranchesRequest:
    
    project_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project-slug', 'style': 'simple', 'explode': False }})
    r"""Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped."""
    workflow_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workflow-name', 'style': 'form', 'explode': True }})
    r"""The name of a workflow. If not passed we will scope the API call to the project."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAllInsightsBranchesDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetAllInsightsBranchesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_all_insights_branches_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""A list of branches for a project"""
    get_all_insights_branches_default_application_json_object: Optional[GetAllInsightsBranchesDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    