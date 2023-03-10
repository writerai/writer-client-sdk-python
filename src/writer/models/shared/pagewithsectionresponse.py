from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import sectioninfo as shared_sectioninfo
from ..shared import simpleuser as shared_simpleuser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional
from writer import utils

class PageWithSectionResponseStatusEnum(str, Enum):
    LIVE = "live"
    OFFLINE = "offline"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PageWithSectionResponse:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    order: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order') }})
    status: PageWithSectionResponseStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})
    section: Optional[shared_sectioninfo.SectionInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('section'), 'exclude': lambda f: f is None }})
    updated_by: Optional[shared_simpleuser.SimpleUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedBy'), 'exclude': lambda f: f is None }})
    