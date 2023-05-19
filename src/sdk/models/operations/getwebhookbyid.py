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
class GetWebhookByIDRequest:
    
    webhook_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'webhook-id', 'style': 'simple', 'explode': False }})
    r"""ID of the webhook (UUID)"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWebhookByIDDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    
class GetWebhookByIDWebhookEvents(str, Enum):
    WORKFLOW_COMPLETED = 'workflow-completed'
    JOB_COMPLETED = 'job-completed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWebhookByIDWebhookScope:
    r"""The scope in which the relevant events that will trigger webhooks"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""ID of the scope being used (at the moment, only project ID is supported)"""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of the scope being used"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWebhookByIDWebhook:
    r"""A webhook"""
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created-at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the webhook was created."""
    events: list[GetWebhookByIDWebhookEvents] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    r"""Events that will trigger the webhook"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique ID of the webhook"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the webhook"""
    scope: GetWebhookByIDWebhookScope = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scope') }})
    r"""The scope in which the relevant events that will trigger webhooks"""
    signing_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signing-secret') }})
    r"""Masked value of the secret used to build an HMAC hash of the payload and passed as a header in the webhook request"""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated-at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the webhook was last updated."""
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)"""
    verify_tls: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verify-tls') }})
    r"""Whether to enforce TLS certificate verification when delivering the webhook"""
    

@dataclasses.dataclass
class GetWebhookByIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_webhook_by_id_default_application_json_object: Optional[GetWebhookByIDDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    webhook: Optional[GetWebhookByIDWebhook] = dataclasses.field(default=None)
    r"""A webhook"""
    