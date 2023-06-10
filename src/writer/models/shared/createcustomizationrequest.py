"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import hyperparameters as shared_hyperparameters
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateCustomizationRequest:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    training_dataset_file_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trainingDatasetFileId') }})
    additional_hyper_parameters: Optional[shared_hyperparameters.HyperParameters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalHyperParameters'), 'exclude': lambda f: f is None }})
    batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batchSize'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    epochs: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('epochs'), 'exclude': lambda f: f is None }})
    learning_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('learningRate'), 'exclude': lambda f: f is None }})
    prompt_template: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptTemplate'), 'exclude': lambda f: f is None }})
    validation_dataset_file_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validationDatasetFileId'), 'exclude': lambda f: f is None }})
    

