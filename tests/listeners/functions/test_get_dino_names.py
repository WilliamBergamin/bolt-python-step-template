import logging
from unittest import mock

from listeners.functions import get_dino_names

test_logger = logging.getLogger(__name__)


class TestGetDinoNames:
    test_data_path = "tests/db/fake_dinosaur_names.csv"

    def test_fetch_dinosaur_names(self):
        actual = get_dino_names.fetch_dinosaur_names(filter="", data_path=self.test_data_path)
        expected = ["Aerodracon", "Astromimus", "Bill", "Brontoventrix", "Caeliraptor"]
        assert actual == expected

    def test_fetch_dinosaur_names_filter(self):
        actual = get_dino_names.fetch_dinosaur_names(filter="b", data_path=self.test_data_path)
        assert actual == ["Bill", "Brontoventrix"]

        actual = get_dino_names.fetch_dinosaur_names(filter="bi", data_path=self.test_data_path)
        assert actual == ["Bill"]

    def test_handle_get_dino_names(self):
        fake_ack = mock.Mock()
        fake_complete = mock.Mock()
        get_dino_names.fetch_dinosaur_names = mock.Mock(return_value=[])

        get_dino_names.handle_get_dino_names(fake_ack, {"query": ""}, fake_complete, test_logger)

        fake_ack.assert_called_once()
        fake_complete.assert_called_once_with(outputs={"options": []})

    def test_handle_get_dino_names_crop_length(self):
        fake_ack = mock.Mock()
        fake_complete = mock.Mock()
        test_dino_names = ["dinosaur"] * 1002
        get_dino_names.fetch_dinosaur_names = mock.Mock(return_value=test_dino_names)

        get_dino_names.handle_get_dino_names(fake_ack, {"query": ""}, fake_complete, test_logger)

        fake_ack.assert_called_once()
        fake_complete.assert_called_once()
        _, kwargs = fake_complete.call_args
        assert len(kwargs["outputs"]["options"]) == 1000
