"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ContinuePipelineRequestBody:
    configuration: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    r"""A configuration string for the pipeline."""
    continuation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('continuation-key') }})
    r"""A pipeline continuation key."""
    parameters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters'), 'exclude': lambda f: f is None }})
    r"""An object containing pipeline parameters and their values."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ContinuePipelineDefaultApplicationJSON:
    r"""Error response."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ContinuePipelineMessageResponse:
    r"""message response"""
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""A human-readable message"""
    




@dataclasses.dataclass
class ContinuePipelineResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    continue_pipeline_default_application_json_object: Optional[ContinuePipelineDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    message_response: Optional[ContinuePipelineMessageResponse] = dataclasses.field(default=None)
    r"""A confirmation message."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

