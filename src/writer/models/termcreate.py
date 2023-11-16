"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .approvedtermextensioncreate import ApprovedTermExtensionCreate
from .linkedtermcreate import LinkedTermCreate
from .termexamplecreate import TermExampleCreate
from .termmistakecreate import TermMistakeCreate
from .termtagcreate import TermTagCreate
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from writer import utils

class TermCreatePos(str, Enum):
    NOUN = 'noun'
    VERB = 'verb'
    ADVERB = 'adverb'
    ADJECTIVE = 'adjective'

class TermCreateType(str, Enum):
    APPROVED = 'approved'
    BANNED = 'banned'
    PENDING = 'pending'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TermCreate:
    case_sensitive: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caseSensitive') }})
    term: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('term') }})
    type: TermCreateType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    approved_term_extension: Optional[ApprovedTermExtensionCreate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approvedTermExtension'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    examples: Optional[List[TermExampleCreate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('examples'), 'exclude': lambda f: f is None }})
    highlight: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highlight'), 'exclude': lambda f: f is None }})
    linked_terms: Optional[List[LinkedTermCreate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('linkedTerms'), 'exclude': lambda f: f is None }})
    mistakes: Optional[List[TermMistakeCreate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mistakes'), 'exclude': lambda f: f is None }})
    pos: Optional[TermCreatePos] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pos'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    tags: Optional[List[TermTagCreate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    
