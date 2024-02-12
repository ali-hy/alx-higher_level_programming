#!/usr/bin/python3
"""Test for the Square class"""
import unittest
from unittest.mock import patch
import io
from models.square import Square


class SquareTest(unittest.TestCase):
    """Test cases for the Square class"""

    def test_exists(self):
        '''Check that the Square class exists and has docs'''
        self.assertIsNotNone(Square)
        self.assertIsNotNone(Square.__doc__)
        self.assertGreater(len(Square.__doc__), 0)

    def test_id(self):
        '''test id values for Square class (automatic and hardcoded)'''
        x = Square(1, 2)
        self.assertTrue(hasattr(x, 'id'))

    def test_constructor(self):
        '''test that args passed to the constructor are set correctly'''
        r = Square(4, 5, 6, 1)
        self.assertEqual(r.size, 4)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

        r = Square(6)
        self.assertEqual(r.size, 6)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_sizeErrors(self):
        '''test for errors raised on invalid size input'''
        self.assertRaises(TypeError,
                          lambda: Square(1.0))
        self.assertRaises(ValueError,
                          lambda: Square(0, 1))

    def test_xyErrors(self):
        '''test for errors raised on invalid x and y input'''
        self.assertRaises(TypeError,
                          lambda: Square(1, 1.0))
        self.assertRaises(ValueError,
                          lambda: Square(1, -1, 0))

        self.assertRaises(TypeError,
                          lambda: Square(1, 0, 1.0))
        self.assertRaises(ValueError,
                          lambda: Square(1, 0, -1))

    def test_area(self):
        '''test area function'''
        self.assertEqual(Square(532).area(), 532 * 532)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        '''test display function without x and y coordinates'''
        Square(3).display()
        expected = '###\n###\n###\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_xy(self, mock_stdout):
        '''test display function with x and y coordinates'''
        Square(3, 4, 3, 4).display()
        expected = '\n\n\n    ###\n    ###\n    ###\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_str(self):
        '''test the __str__, str conversion function'''
        self.assertEqual(str(Square(1, 8, 6, 1000)),
                         f'[Square] (1000) 8/6 - 1')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update(self, mock_stdout):
        '''test update method'''
        r1 = Square(10, 10, 10, 10)
        print(r1)

        r1.update(size=1)
        print(r1)

        r1.update(size=1, x=2)
        print(r1)

        r1.update(y=1, size=2, x=3, id=89)
        print(r1)

        r1.update(x=1, size=2, y=3)
        print(r1)

        r1 = Square(10, 10, 10, 10)
        print(r1)

        r1.update(89)
        print(r1)

        r1.update(89, 2)
        print(r1)

        r1.update(89, 2, 3)
        print(r1)

        r1.update(89, 2, 3, 4)
        print(r1)

        self.assertEqual('[Square] (10) 10/10 - 10\n'
                         + '[Square] (10) 10/10 - 1\n'
                         + '[Square] (10) 2/10 - 1\n'
                         + '[Square] (89) 3/1 - 2\n'
                         + '[Square] (89) 1/3 - 2\n'
                         + '[Square] (10) 10/10 - 10\n'
                         + '[Square] (89) 10/10 - 10\n'
                         + '[Square] (89) 10/10 - 2\n'
                         + '[Square] (89) 3/10 - 2\n'
                         + '[Square] (89) 3/4 - 2\n', mock_stdout.getvalue())

    def test_dictionary(self):
        '''test to_dictionary method'''
        r = Square(3, 6, 2, 94)
        self.assertIsInstance(r.to_dictionary(), dict)
        self.assertEqual(r.to_dictionary(), {
            'id': 94,
            'size': 3,
            'x': 6,
            'y': 2
        })


if __name__ == '__main__':
    unittest.main()
