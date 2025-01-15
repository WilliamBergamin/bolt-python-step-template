import logging
from typing import Dict, List

from slack_bolt import Ack, Complete

from .utils import DINO_TYPES, OptionField, OptionSelect


def get_dino_type_options(types: Dict[str, str]) -> List[OptionSelect]:
    return [
        {"text": {"text": type.title(), "type": "plain_text"}, "value": type.lower()}
        for type in types.keys()
    ]


def handle_get_dino_characteristics(
    ack: Ack,
    complete: Complete,
    logger: logging.Logger,
):
    try:
        options: List[OptionField] = [
            {
                "text": {"text": "Type", "type": "plain_text"},
                "key": "type",
                "type": "string",
                "options": get_dino_type_options(DINO_TYPES),
                "is_required": True,
            },
            {
                "text": {"text": "Number of teeth", "type": "plain_text"},
                "key": "teeth",
                "type": "integer",
                "is_required": True,
            },
            {
                "text": {"text": "What colour is it", "type": "plain_text"},
                "key": "colour",
                "type": "string",
                "is_required": True,
            },
        ]

        complete(outputs={"options": options})
    finally:
        ack()
        logger.info("Acknowledged!")
