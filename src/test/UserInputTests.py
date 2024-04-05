import unittest
from unittest.mock import mock_open, patch
import src.main.UserInput as UI
import src.main.GUI as gui
import src.main.Value as val


class DynamicUserInput(unittest.TestCase):
    @patch("builtins.open")
    def test_name_exception(self, mock_open):
        name = UI.get_procedure_name()
        self.assertIsInstance(name, str)

    @patch("builtins.open")
    def test_plate_exception(self, mock_open):
        plate = UI.get_plate_type()
        self.assertIn(plate, {6, 96})

    @patch("builtins.open")
    def test_reservoir_exception(self, mock_open):
        tube = UI.get_reservoir_type()
        self.assertIn(tube, {"A", "B"})

    @patch("builtins.open")
    def test_tip_exception(self, mock_open):
        tip = UI.get_tip_type()
        self.assertIsInstance(tip, int)

    def test_gui(self):

        gui.run_procedure()



if __name__ == '__main__':
    unittest.main()