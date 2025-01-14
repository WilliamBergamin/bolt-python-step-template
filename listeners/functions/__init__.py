from slack_bolt import App

from .get_dino_names import handle_get_dino_names


def register(app: App):
    app.function("get-dino-names", auto_acknowledge=False)(handle_get_dino_names)
