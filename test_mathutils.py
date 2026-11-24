import unittest

from mathutils import average, biggest, is_prime

class TestMathUtils(unittest.TestCase):

    # Tests for average()
    def test_average_normal(self):
        self.assertEqual(average([10, 20, 30, 40]), 25)

    def test_average_empty(self):
        self.assertEqual(average([]), 0)

    def test_average_single_element(self):
        self.assertEqual(average([50]), 50)

    # Tests for biggest()
    def test_biggest_normal(self):
        self.assertEqual(biggest([10, 50, 20, 80, 30]), 80)

    def test_biggest_empty(self):
        self.assertIsNone(biggest([]))

    def test_biggest_negative_numbers(self):
        self.assertEqual(biggest([-10, -5, -20]), -5)

    def test_biggest_single_element(self):
        self.assertEqual(biggest([25]), 25)

    # Tests for is_prime()
    def test_is_prime_true(self):
        self.assertTrue(is_prime(7))

    def test_is_prime_false(self):
        self.assertFalse(is_prime(9))

    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-5))


if __name__ == "__main__":
    unittest.main()
