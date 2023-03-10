from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompletionGenerationChoiceLogprobs:
    text_offset: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('textOffset'), 'exclude': lambda f: f is None }})
    token_logprobs: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tokenLogprobs'), 'exclude': lambda f: f is None }})
    tokens: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tokens'), 'exclude': lambda f: f is None }})
    top_logprobs: Optional[list[dict[str, str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topLogprobs'), 'exclude': lambda f: f is None }})
    