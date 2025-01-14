import csv
import json
import logging
import re
from typing import List

from slack_bolt import Ack, Complete

from .utils import OptionSelect


def fetch_dinosaur_names(filter="", data_path="db/dinosaur_names.csv"):
    matcher = re.compile(filter, re.I)
    dino_names = []
    with open(data_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=" ")
        dino_names = [row for row in reader if matcher.match(row)]
    return sorted(dino_names)


def handle_get_dino_names(
    ack: Ack,
    payload: dict,
    inputs: dict,
    complete: Complete,
    logger: logging.Logger,
):
    try:
        logger.info(f"Payload: {json.dumps(payload, indent=2)}")
        query = inputs["query"]

        dino_names = fetch_dinosaur_names(filter=query)
        options: List[OptionSelect] = [
            {
                "text": {"text": dino_name, "type": "plain_text"},
                "value": dino_names,
            }
            for dino_name in dino_names[:1000]
        ]

        complete(outputs={"options": options})
    finally:
        ack()
        logger.info("Acknowledged!")
