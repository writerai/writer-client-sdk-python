from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import metadata as shared_metadata
from ..shared import usage as shared_usage
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from writer import utils

class SubscriptionPublicResponseAPIProductNameEnum(str, Enum):
    FREE = "free"
    PRO = "pro"
    TEAM = "team"
    ENTERPRISE = "enterprise"
    LEGACY = "legacy"

class SubscriptionPublicResponseAPIStatusEnum(str, Enum):
    TRIALING = "trialing"
    ACTIVE = "active"
    PAST_DUE = "past_due"
    INCOMPLETE = "incomplete"
    INCOMPLETE_EXPIRED = "incomplete_expired"
    UNPAID = "unpaid"
    CANCELED = "canceled"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionPublicResponseAPI:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    meta: shared_metadata.MetaData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta') }})
    product_name: SubscriptionPublicResponseAPIProductNameEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productName') }})
    seats: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seats') }})
    status: SubscriptionPublicResponseAPIStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    subscription_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscriptionId') }})
    usage: shared_usage.Usage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage') }})
    