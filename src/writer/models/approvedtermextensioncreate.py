"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ApprovedTermExtensionCreate:
    capitalize: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('capitalize') }})
    fix_case: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fixCase') }})
    fix_common_mistakes: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fixCommonMistakes') }})
    

