from __future__ import annotations
import dataclasses
from ..shared import contentissue as shared_contentissue
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProcessedContent:
    issues: Optional[list[shared_contentissue.ContentIssue]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issues'), 'exclude': lambda f: f is None }})
    