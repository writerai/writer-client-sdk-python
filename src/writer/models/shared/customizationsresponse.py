from __future__ import annotations
import dataclasses
from ..shared import modelcustomization as shared_modelcustomization
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomizationsResponse:
    customizations: Optional[list[shared_modelcustomization.ModelCustomization]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customizations'), 'exclude': lambda f: f is None }})
    