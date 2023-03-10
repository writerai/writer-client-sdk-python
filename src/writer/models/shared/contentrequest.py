from __future__ import annotations
import dataclasses
from ..shared import contentsettings as shared_contentsettings
from dataclasses_json import Undefined, dataclass_json
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ContentRequest:
    content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    settings: shared_contentsettings.ContentSettings = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settings') }})
    