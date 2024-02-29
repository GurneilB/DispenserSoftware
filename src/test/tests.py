import unittest
from unittest.mock import mock_open, patch
import src.main.Exceptions as E
import src.main.UserInput as UI
class TestName(unittest.TestCase):
    @patch("builtins.open")
    def test_name_exception(self, mock_open):
        name = UI.get_procedure_name()
        self.assertIsInstance(name, str)

    @patch("builtins.open")
    def test_plate_exception(self, mock_open):
        plate = E.Exception_plate()
        self.assertIn(plate, {6, 96})

    @patch("builtins.open")
    def test_reservoir_exception(self, mock_open):
        tube = E.Exception_reservoir()
        self.assertIn(tube, {"A","B"})

    @patch("builtins.open")
    def test_tip_exception(self, mock_open):
        tip = E.Exception_tip()
        self.assertIsInstance(tip, int)


if __name__ == '__main__':
    unittest.main()

