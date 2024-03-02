import unittest
from unittest.mock import mock_open, patch
import src.main.UserInput as UI

class ProcedureTests(unittest.TestCase):
    @patch("builtins.open")
    def test_aspiration(self):
        name = UI.get_procedure_name()
        self.assertIsInstance(name, str)