import unittest
from my_calculator import my_adder

class TestMyAdder(unittest.TestCase):
    def test_my_adder(self):
        self.assertEqual(my_adder(1, 2), 3)
