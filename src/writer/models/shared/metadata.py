from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from writer import utils

class MetaDataTierEnum(str, Enum):
    ENTERPRISE_1 = "enterprise-1"
    ENTERPRISE_2 = "enterprise-2"
    ENTERPRISE_3 = "enterprise-3"
    ENTERPRISE_4 = "enterprise-4"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MetaData:
    portal: dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('portal') }})
    reporting: dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reporting') }})
    snippets_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('snippetsCount') }})
    sso_access: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssoAccess') }})
    styleguide: dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('styleguide') }})
    team_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('teamCount') }})
    terms_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('termsCount') }})
    tier: Optional[MetaDataTierEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tier'), 'exclude': lambda f: f is None }})
    