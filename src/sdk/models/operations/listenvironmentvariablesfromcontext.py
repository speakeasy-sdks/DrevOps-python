"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class ListEnvironmentVariablesFromContextRequest:
    
    context_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'context-id', 'style': 'simple', 'explode': False }})
    r"""ID of the context (UUID)"""
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page-token', 'style': 'form', 'explode': True }})
    r"""A token to retrieve the next page of results."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListEnvironmentVariablesFromContextDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListEnvironmentVariablesFromContext200ApplicationJSONItems:
    
    context_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context_id') }})
    r"""ID of the context (UUID)"""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the environment variable was created."""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the environment variable was updated"""
    variable: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('variable') }})
    r"""The name of the environment variable"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListEnvironmentVariablesFromContext200ApplicationJSON:
    r"""A paginated list of environment variables"""
    
    items: list[ListEnvironmentVariablesFromContext200ApplicationJSONItems] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    next_page_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page_token') }})
    r"""A token to pass as a `page-token` query parameter to return the next page of results."""
    

@dataclasses.dataclass
class ListEnvironmentVariablesFromContextResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_environment_variables_from_context_200_application_json_object: Optional[ListEnvironmentVariablesFromContext200ApplicationJSON] = dataclasses.field(default=None)
    r"""A paginated list of environment variables"""
    list_environment_variables_from_context_default_application_json_object: Optional[ListEnvironmentVariablesFromContextDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    