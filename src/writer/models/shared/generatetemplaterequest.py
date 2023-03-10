from __future__ import annotations
import dataclasses
from ..shared import magicrequestinput as shared_magicrequestinput
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateTemplateRequest:
    template_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('templateId') }})
    inputs: Optional[list[shared_magicrequestinput.MagicRequestInput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inputs'), 'exclude': lambda f: f is None }})
    