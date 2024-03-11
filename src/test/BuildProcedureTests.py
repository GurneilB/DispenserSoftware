import unittest
from unittest.mock import mock_open, patch
import src.main.UserInput as UI
import src.main.BuildProcedure as bp
import numpy as np

array1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
array1inv = [3, 6, 9, 8, 5, 2, 1, 4, 7]


class ProcedureTests(unittest.TestCase):
    def testSnake(self):
        snaked = bp.build_snake(array1)

        self.assertEqual(snaked, array1inv)
