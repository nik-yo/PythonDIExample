from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase, DataClassJsonMixin
from os import path

@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class SomeConfig:
  some_key: str


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class Config(DataClassJsonMixin):
  some_config: SomeConfig

def load_config(file: str) -> Config:
  with open(file, 'r') as f:
    return Config.from_json(f.read())