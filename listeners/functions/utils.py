from typing import List, NotRequired, TypedDict


class Text(TypedDict):
    type: str
    text: str


class Items(TypedDict):
    type: str


class OptionSelect(TypedDict):
    text: Text
    value: str


class OptionField(TypedDict):
    text: Text
    key: str
    type: str
    is_required: NotRequired[bool]
    options: NotRequired[List[OptionSelect]]
    items: NotRequired[Items]
