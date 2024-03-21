import src.main.UserInput as UI
import numpy as np


class OutOfRangeError(Exception):
    def __init__(self, value, minimum, maximum):
        self.value = value
        self.minimum = minimum
        self.maximum = maximum
        message = f"Please enter a volume between [{minimum}, {maximum}]. {value} is out of the range. "
        super().__init__(message)
