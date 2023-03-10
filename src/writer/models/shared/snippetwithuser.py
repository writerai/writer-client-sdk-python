from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import snippettagv2 as shared_snippettagv2
from ..shared import terminologyuser as shared_terminologyuser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SnippetWithUser:
    created_user: shared_terminologyuser.TerminologyUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdUser') }})
    creation_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creationTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    modification_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modificationTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    modified_user: shared_terminologyuser.TerminologyUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedUser') }})
    snippet: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('snippet') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    shortcut: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shortcut'), 'exclude': lambda f: f is None }})
    tags: Optional[list[shared_snippettagv2.SnippetTagV2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    