import unittest
from calculator import add, multiply

class TestCorrectness(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add([1, 2, 3]), 6)

    def test_multiply(self):
        self.assertEqual(multiply([2, 3, 4]), 24)

if __name__ == "__main__":
    unittest.main()
