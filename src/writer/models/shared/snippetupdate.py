from __future__ import annotations
import dataclasses
from ..shared import snippettagv2 as shared_snippettagv2
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SnippetUpdate:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    snippet: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('snippet') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    shortcut: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shortcut'), 'exclude': lambda f: f is None }})
    tags: Optional[list[shared_snippettagv2.SnippetTagV2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    