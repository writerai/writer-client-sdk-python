"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from writer import utils

class TermExampleCreateType(str, Enum):
    GOOD = 'good'
    BAD = 'bad'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TermExampleCreate:
    example: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('example') }})
    type: TermExampleCreateType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    

