"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AddEnvironmentVariableToContextRequestBody:
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""The value of the environment variable"""
    




@dataclasses.dataclass
class AddEnvironmentVariableToContextRequest:
    context_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'context-id', 'style': 'simple', 'explode': False }})
    r"""ID of the context (UUID)"""
    env_var_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'env-var-name', 'style': 'simple', 'explode': False }})
    r"""The name of the environment variable"""
    request_body: Optional[AddEnvironmentVariableToContextRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AddEnvironmentVariableToContextDefaultApplicationJSON:
    r"""Error response."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AddEnvironmentVariableToContext200ApplicationJSONMessageResponse:
    r"""message response"""
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""A human-readable message"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AddEnvironmentVariableToContext200ApplicationJSON1:
    context_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context_id') }})
    r"""ID of the context (UUID)"""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the environment variable was created."""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the environment variable was updated"""
    variable: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('variable') }})
    r"""The name of the environment variable"""
    




@dataclasses.dataclass
class AddEnvironmentVariableToContextResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    add_environment_variable_to_context_200_application_json_any_of: Optional[Any] = dataclasses.field(default=None)
    r"""The new environment variable"""
    add_environment_variable_to_context_default_application_json_object: Optional[AddEnvironmentVariableToContextDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

