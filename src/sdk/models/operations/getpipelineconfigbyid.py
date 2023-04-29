"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetPipelineConfigByIDRequest:
    
    pipeline_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pipeline-id', 'style': 'simple', 'explode': False }})
    r"""The unique ID of the pipeline."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPipelineConfigByIDDefaultApplicationJSON:
    r"""Error response."""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPipelineConfigByIDPipelineConfig:
    r"""The configuration strings for the pipeline."""
    
    compiled: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compiled') }})
    r"""The compiled configuration for the pipeline, after all orb expansion has been performed. If there were errors processing the pipeline's configuration, then this field may be empty."""
    source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    r"""The source configuration for the pipeline, before any config compilation has been performed. If there is no config, then this field will be empty."""
    compiled_setup_config: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compiled-setup-config'), 'exclude': lambda f: f is None }})
    r"""The compiled setup configuration for the pipeline, after all orb expansion has been performed. If there were errors processing the pipeline's setup workflows, then this field may be empty."""
    setup_config: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('setup-config'), 'exclude': lambda f: f is None }})
    r"""The setup configuration for the pipeline used for Setup Workflows. If there were errors processing the pipeline's configuration or if setup workflows are not enabled, then this field should not exist"""
    

@dataclasses.dataclass
class GetPipelineConfigByIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_pipeline_config_by_id_default_application_json_object: Optional[GetPipelineConfigByIDDefaultApplicationJSON] = dataclasses.field(default=None)
    r"""Error response."""
    pipeline_config: Optional[GetPipelineConfigByIDPipelineConfig] = dataclasses.field(default=None)
    r"""The configuration strings for the pipeline."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    