"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..errors import failmessage as errors_failmessage
from dataclasses_json import Undefined, dataclass_json
from typing import Any, List, Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FailResponse(Exception):
    extras: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extras') }})
    tpe: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tpe') }})
    errors: Optional[List[errors_failmessage.FailMessage]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
