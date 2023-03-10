from __future__ import annotations
import dataclasses
from ..shared import approvedtermextension as shared_approvedtermextension
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from writer import utils

class FullLinkedTermPosEnum(str, Enum):
    NOUN = "noun"
    VERB = "verb"
    ADVERB = "adverb"
    ADJECTIVE = "adjective"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FullLinkedTerm:
    case_sensitive: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caseSensitive') }})
    linked_term_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('linkedTermId') }})
    term: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('term') }})
    term_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('termId') }})
    approved_term_extension: Optional[shared_approvedtermextension.ApprovedTermExtension] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approvedTermExtension'), 'exclude': lambda f: f is None }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    pos: Optional[FullLinkedTermPosEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pos'), 'exclude': lambda f: f is None }})
    