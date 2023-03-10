from __future__ import annotations
import dataclasses
from ..shared import failmessage as shared_failmessage
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FailResponse:
    extras: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extras') }})
    tpe: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tpe') }})
    errors: Optional[list[shared_failmessage.FailMessage]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    