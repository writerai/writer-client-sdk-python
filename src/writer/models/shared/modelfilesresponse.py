from __future__ import annotations
import dataclasses
from ..shared import modelfile as shared_modelfile
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelFilesResponse:
    files: Optional[list[shared_modelfile.ModelFile]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files'), 'exclude': lambda f: f is None }})
    