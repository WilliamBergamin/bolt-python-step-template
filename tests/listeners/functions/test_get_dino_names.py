from listeners.functions.get_dino_names import fetch_dinosaur_names


class TestGetDinoNames:
    test_data_path = "tests/db/fake_dinosaur_names.csv"

    def test_fetch_dinosaur_names(self):
        actual = fetch_dinosaur_names(filter="", data_path=self.test_data_path)
        expected = ["Aerodracon", "Astromimus", "Bill", "Brontoventrix", "Caeliraptor"]
        assert actual == expected

    def test_fetch_dinosaur_names_filter(self):
        actual = fetch_dinosaur_names(filter="b", data_path=self.test_data_path)
        assert actual == ["Bill", "Brontoventrix"]

        actual = fetch_dinosaur_names(filter="bi", data_path=self.test_data_path)
        assert actual == ["Bill"]
