import unittest
import time
from calculator import add, multiply

class TestPerformance(unittest.TestCase):
    def test_add_performance(self):
        numbers = list(range(1, 101))
        start = time.time()
        result = add(numbers)
        elapsed = time.time() - start
        self.assertEqual(result, sum(numbers))
        self.assertLessEqual(elapsed, 0.5)

    def test_multiply_performance(self):
        numbers = [2] * 100
        expected = 2**100
        start = time.time()
        result = multiply(numbers)
        elapsed = time.time() - start
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed, 0.5)

if __name__ == "__main__":
    unittest.main()
