from __future__ import annotations
import dataclasses
from ..shared import approvedtermextensioncreate as shared_approvedtermextensioncreate
from ..shared import linkedtermcreate as shared_linkedtermcreate
from ..shared import termexamplecreate as shared_termexamplecreate
from ..shared import termmistakecreate as shared_termmistakecreate
from ..shared import termtagcreate as shared_termtagcreate
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from writer import utils

class TermCreatePosEnum(str, Enum):
    NOUN = "noun"
    VERB = "verb"
    ADVERB = "adverb"
    ADJECTIVE = "adjective"

class TermCreateTypeEnum(str, Enum):
    APPROVED = "approved"
    BANNED = "banned"
    PENDING = "pending"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TermCreate:
    case_sensitive: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caseSensitive') }})
    term: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('term') }})
    type: TermCreateTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    approved_term_extension: Optional[shared_approvedtermextensioncreate.ApprovedTermExtensionCreate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approvedTermExtension'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    examples: Optional[list[shared_termexamplecreate.TermExampleCreate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('examples'), 'exclude': lambda f: f is None }})
    highlight: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highlight'), 'exclude': lambda f: f is None }})
    linked_terms: Optional[list[shared_linkedtermcreate.LinkedTermCreate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('linkedTerms'), 'exclude': lambda f: f is None }})
    mistakes: Optional[list[shared_termmistakecreate.TermMistakeCreate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mistakes'), 'exclude': lambda f: f is None }})
    pos: Optional[TermCreatePosEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pos'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    tags: Optional[list[shared_termtagcreate.TermTagCreate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    