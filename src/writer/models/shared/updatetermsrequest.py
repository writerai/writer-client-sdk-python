from __future__ import annotations
import dataclasses
from ..shared import termupdate as shared_termupdate
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from writer import utils

class UpdateTermsRequestFailHandlingEnum(str, Enum):
    ACCUMULATE = "accumulate"
    VALIDATE = "validate"
    SKIP = "skip"
    VALIDATE_ONLY = "validateOnly"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateTermsRequest:
    fail_handling: Optional[UpdateTermsRequestFailHandlingEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failHandling'), 'exclude': lambda f: f is None }})
    models: Optional[list[shared_termupdate.TermUpdate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('models'), 'exclude': lambda f: f is None }})
    