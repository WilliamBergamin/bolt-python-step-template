import logging
from unittest import mock

from listeners.functions import get_dino_characteristics
from listeners.functions.utils import OptionSelect

test_logger = logging.getLogger(__name__)


class TestGetDinoNames:
    test_dino_options: OptionSelect = {
        "text": {"text": "Dinosaur", "type": "plain_text"},
        "value": "dinosaur",
    }

    def test_fetch_dinosaur_names(self):
        actual = get_dino_characteristics.get_dino_type_options({"dinosaur": "this is a dinosaur"})
        expected = [self.test_dino_options]
        assert actual == expected

    def test_handle_get_dino_names(self):
        fake_ack = mock.Mock()
        fake_complete = mock.Mock()
        get_dino_characteristics.get_dino_type_options = mock.Mock(
            return_value=[self.test_dino_options]
        )

        get_dino_characteristics.handle_get_dino_characteristics(
            fake_ack, fake_complete, test_logger
        )

        fake_ack.assert_called_once()
        fake_complete.assert_called_once()
        _, kwargs = fake_complete.call_args
        assert len(kwargs["outputs"]["options"]) == 3
