from slack_bolt import Complete

from listeners.functions.utils import DINO_TYPES


def handle_dino_description(inputs: dict, complete: Complete):
    dino_name: str = inputs["name"]
    dino_type: str = inputs["characteristics"]["type"]
    dino_teeth_num: int = inputs["characteristics"]["teeth"]
    dino_colour: str = inputs["characteristics"]["colour"]

    complete(
        outputs={
            "description": [
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "emoji", "name": "egg"},
                                {
                                    "type": "text",
                                    "style": {"bold": True},
                                    "text": f" {dino_name.title()} ",
                                },
                                {"type": "emoji", "name": "chicken"},
                            ],
                        },
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": f"{DINO_TYPES[dino_type.lower()]} This specific "
                                    f"dinosaur has {dino_teeth_num} teeth and is {dino_colour}.",
                                }
                            ],
                        },
                    ],
                }
            ]
        }
    )
