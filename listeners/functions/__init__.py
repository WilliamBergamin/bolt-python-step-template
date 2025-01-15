from slack_bolt import App

from .dino_description import handle_dino_description
from .get_dino_characteristics import handle_get_dino_characteristics
from .get_dino_names import handle_get_dino_names


def register(app: App):
    app.function("get-dino-names", auto_acknowledge=False)(handle_get_dino_names)
    app.function("get-dino-characteristics", auto_acknowledge=False)(
        handle_get_dino_characteristics
    )
    app.function("dino-description")(handle_dino_description)
