from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import approvedtermextension as shared_approvedtermextension
from ..shared import fulllinkedterm as shared_fulllinkedterm
from ..shared import termexample as shared_termexample
from ..shared import terminologyuser as shared_terminologyuser
from ..shared import termmistake as shared_termmistake
from ..shared import termtagresponse as shared_termtagresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional
from writer import utils

class FullTermWithUserPosEnum(str, Enum):
    NOUN = "noun"
    VERB = "verb"
    ADVERB = "adverb"
    ADJECTIVE = "adjective"

class FullTermWithUserTypeEnum(str, Enum):
    APPROVED = "approved"
    BANNED = "banned"
    PENDING = "pending"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FullTermWithUser:
    case_sensitive: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caseSensitive') }})
    created_user: shared_terminologyuser.TerminologyUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdUser') }})
    creation_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creationTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    highlight: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highlight') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    modification_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modificationTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    modified_user: shared_terminologyuser.TerminologyUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedUser') }})
    term: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('term') }})
    term_bank_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('termBankId') }})
    type: FullTermWithUserTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    approved_term_extension: Optional[shared_approvedtermextension.ApprovedTermExtension] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approvedTermExtension'), 'exclude': lambda f: f is None }})
    backlinked_terms: Optional[list[shared_fulllinkedterm.FullLinkedTerm]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('backlinkedTerms'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    examples: Optional[list[shared_termexample.TermExample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('examples'), 'exclude': lambda f: f is None }})
    linked_terms: Optional[list[shared_fulllinkedterm.FullLinkedTerm]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('linkedTerms'), 'exclude': lambda f: f is None }})
    mistakes: Optional[list[shared_termmistake.TermMistake]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mistakes'), 'exclude': lambda f: f is None }})
    pos: Optional[FullTermWithUserPosEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pos'), 'exclude': lambda f: f is None }})
    tags: Optional[list[shared_termtagresponse.TermTagResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    