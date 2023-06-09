"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional



@dataclasses.dataclass
class DeleteWebhookRequest:
    webhook_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'webhook-id', 'style': 'simple', 'explode': False }})
    r"""ID of the webhook (UUID)"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteWebhookDefaultApplicationJSON:
    r"""Error response."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteWebhookMessageResponse:
    r"""message response"""
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""A human-readable message"""
    




@dataclasses.dataclass
class DeleteWebhookResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_webhook_default_application_json_object: Optional[DeleteWebhookDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    message_response: Optional[DeleteWebhookMessageResponse] = dataclasses.field(default=None)
    r"""A confirmation message"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

