from unittest.mock import Mock

from slack_bolt import Complete

from listeners.functions import dino_description


class TestGetDinoNames:
    test_dino_types = {"dinosaur": "this is a dinosaur"}

    def test_handle_get_dino_names(self):
        fake_complete = Mock(Complete)
        fake_inputs = {
            "name": "bill",
            "characteristics": {"type": "dinosaur", "teeth": 3, "colour": "blue"},
        }
        dino_description.DINO_TYPES = self.test_dino_types

        dino_description.handle_dino_description(fake_inputs, fake_complete)

        fake_complete.assert_called_once()
        _, kwargs = fake_complete.call_args
        assert "description" in kwargs["outputs"]
        assert isinstance(kwargs["outputs"]["description"], list)
