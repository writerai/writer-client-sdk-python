from __future__ import annotations
import dataclasses
from ..shared import completiongenerationchoice as shared_completiongenerationchoice
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompletionResponse:
    choices: Optional[list[shared_completiongenerationchoice.CompletionGenerationChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('choices'), 'exclude': lambda f: f is None }})
    