#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)

    def test_max_integer_errors(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4])
        with self.assertRaises(TypeError):
            max_integer(1234)

if __name__ == '__main__':
    unittest.main()
