from __future__ import annotations
import dataclasses
from ..shared import completiongenerationchoicelogprobs as shared_completiongenerationchoicelogprobs
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompletionGenerationChoice:
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text') }})
    logprobs: Optional[shared_completiongenerationchoicelogprobs.CompletionGenerationChoiceLogprobs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logprobs'), 'exclude': lambda f: f is None }})
    