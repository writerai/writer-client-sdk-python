from __future__ import annotations
import dataclasses
from ..shared import failmessage as shared_failmessage
from ..shared import fulltermwithuser as shared_fulltermwithuser
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateTermsResponse:
    fails: Optional[list[shared_failmessage.FailMessage]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fails'), 'exclude': lambda f: f is None }})
    models: Optional[list[shared_fulltermwithuser.FullTermWithUser]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('models'), 'exclude': lambda f: f is None }})
    