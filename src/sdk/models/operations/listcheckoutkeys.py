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
class ListCheckoutKeysRequest:
    project_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project-slug', 'style': 'simple', 'explode': False }})
    r"""Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListCheckoutKeysDefaultApplicationJSON:
    r"""Error response."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    


class ListCheckoutKeysCheckoutKeyListResponseCheckoutKeyCheckoutKeyType(str, Enum):
    r"""The type of checkout key. This may be either `deploy-key` or `github-user-key`."""
    DEPLOY_KEY = 'deploy-key'
    GITHUB_USER_KEY = 'github-user-key'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListCheckoutKeysCheckoutKeyListResponseCheckoutKey:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created-at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time the checkout key was created."""
    fingerprint: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fingerprint') }})
    r"""An SSH key fingerprint."""
    preferred: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preferred') }})
    r"""A boolean value that indicates if this key is preferred."""
    public_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public-key') }})
    r"""A public SSH key."""
    type: ListCheckoutKeysCheckoutKeyListResponseCheckoutKeyCheckoutKeyType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of checkout key. This may be either `deploy-key` or `github-user-key`."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListCheckoutKeysCheckoutKeyListResponse:
    r"""A sequence of checkout keys."""
    items: list[ListCheckoutKeysCheckoutKeyListResponseCheckoutKey] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    next_page_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page_token') }})
    r"""A token to pass as a `page-token` query parameter to return the next page of results."""
    




@dataclasses.dataclass
class ListCheckoutKeysResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    checkout_key_list_response: Optional[ListCheckoutKeysCheckoutKeyListResponse] = dataclasses.field(default=None)
    r"""A sequence of checkout keys."""
    list_checkout_keys_default_application_json_object: Optional[ListCheckoutKeysDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

