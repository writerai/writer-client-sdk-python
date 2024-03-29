"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .failmessage import FailMessage
from dataclasses_json import Undefined, dataclass_json
from typing import Any, List, Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FailResponse(Exception):
    r"""Bad Request"""
    extras: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extras') }})
    tpe: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tpe') }})
    errors: Optional[List[FailMessage]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))
