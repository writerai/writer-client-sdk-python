"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .termupdate import TermUpdate
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from writer import utils

class UpdateTermsRequestFailHandling(str, Enum):
    ACCUMULATE = 'accumulate'
    VALIDATE = 'validate'
    SKIP = 'skip'
    VALIDATE_ONLY = 'validateOnly'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateTermsRequest:
    fail_handling: Optional[UpdateTermsRequestFailHandling] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failHandling'), 'exclude': lambda f: f is None }})
    models: Optional[List[TermUpdate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('models'), 'exclude': lambda f: f is None }})
    
