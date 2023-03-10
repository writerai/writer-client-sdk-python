from __future__ import annotations
import dataclasses
from ..shared import usageitem as shared_usageitem
from dataclasses_json import Undefined, dataclass_json
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Usage:
    co_write_words: shared_usageitem.UsageItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('coWriteWords') }})
    team: shared_usageitem.UsageItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('team') }})
    user: shared_usageitem.UsageItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    words: shared_usageitem.UsageItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('words') }})
    