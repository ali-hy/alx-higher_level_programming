#!/usr/bin/python3
"""Test for the Rectangle class"""
import unittest
from unittest.mock import patch
import io
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_exists(self):
        '''Check that the Rectangle class exists and has docs'''
        self.assertIsNotNone(Rectangle)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertGreater(len(Rectangle.__doc__), 0)

    def test_id(self):
        '''test id values for Rectangle class (automatic and hardcoded)'''
        x = Rectangle(1, 2)
        self.assertTrue(hasattr(x, 'id'))

    def test_constructor(self):
        '''test that args passed to the constructor are set correctly'''
        r = Rectangle(4, 5, 0, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 1)

        r = Rectangle(6, 7)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)

    def test_validators(self):
        '''test for errors raised by number validators'''
        self.assertIsNone(Rectangle.assertIsInteger(1, 'num'))
        self.assertIsNone(Rectangle.assertIsNonNegativeInteger(1, 'num'))
        self.assertIsNone(Rectangle.assertIsPositiveInteger(1, 'num'))

        self.assertRaises(TypeError,
                          lambda: Rectangle.assertIsInteger(0.1, 'num'))
        self.assertRaises(TypeError,
                          lambda: Rectangle.assertIsNonNegativeInteger(
                              0.1, 'num'))
        self.assertRaises(TypeError,
                          lambda: Rectangle.assertIsPositiveInteger(
                              0.1, 'num'))
        self.assertRaises(ValueError,
                          lambda: Rectangle.assertIsPositiveInteger(
                              0, 'num'))
        self.assertRaises(ValueError,
                          lambda: Rectangle.assertIsNonNegativeInteger(
                              -1, 'num'))

    def test_widthHeightErrors(self):
        '''test for errors raised on invalid width and height input'''
        self.assertRaises(TypeError,
                          lambda: Rectangle(1.0, 1))
        self.assertRaises(ValueError,
                          lambda: Rectangle(0, 1))

        self.assertRaises(TypeError,
                          lambda: Rectangle(1, 1.0))
        self.assertRaises(ValueError,
                          lambda: Rectangle(1, 0))

    def test_xyErrors(self):
        '''test for errors raised on invalid x and y input'''
        self.assertRaises(TypeError,
                          lambda: Rectangle(1, 2, 1.0))
        self.assertRaises(ValueError,
                          lambda: Rectangle(1, 2, -1, 0))

        self.assertRaises(TypeError,
                          lambda: Rectangle(1, 2, 0, 1.0))
        self.assertRaises(ValueError,
                          lambda: Rectangle(1, 2, 0, -1))

    def test_area(self):
        '''test area function'''
        self.assertEqual(Rectangle(532, 245).area(), 532 * 245)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        '''test display function without x and y coordinates'''
        Rectangle(3, 4).display()
        expected = '###\n###\n###\n###\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_xy(self, mock_stdout):
        '''test display function with x and y coordinates'''
        Rectangle(3, 4, 3, 4).display()
        expected = '\n\n\n\n   ###\n   ###\n   ###\n   ###\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_str(self):
        '''test the __str__, str conversion function'''
        self.assertEqual(str(Rectangle(1, 8, 6, 2, 1000)),
                         f'[Rectangle] (1000) 6/2 - 1/8')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update(self, mock_stdout):
        r1 = Rectangle(10, 10, 10, 10, 10)
        print(r1)

        r1.update(height=1)
        print(r1)

        r1.update(args=[], width=1, x=2)
        print(r1)

        r1.update(y=1, width=2, x=3, id=89)
        print(r1)

        r1.update(x=1, height=2, y=3, width=4)
        print(r1)

        r1 = Rectangle(10, 10, 10, 10, 10)

        print(r1)

        r1.update(89)
        print(r1)

        r1.update(89, 2)
        print(r1)

        r1.update(89, 2, 3)
        print(r1)

        r1.update(89, 2, 3, 4, id=34, width=65)
        print(r1)

        r1.update(89, 2, 3, 4, 5)
        print(r1)

        self.assertEqual('[Rectangle] (10) 10/10 - 10/10\n'
                         + '[Rectangle] (10) 10/10 - 10/1\n'
                         + '[Rectangle] (10) 2/10 - 1/1\n'
                         + '[Rectangle] (89) 3/1 - 2/1\n'
                         + '[Rectangle] (89) 1/3 - 4/2\n'
                         + '[Rectangle] (10) 10/10 - 10/10\n'
                         + '[Rectangle] (89) 10/10 - 10/10\n'
                         + '[Rectangle] (89) 10/10 - 2/10\n'
                         + '[Rectangle] (89) 10/10 - 2/3\n'
                         + '[Rectangle] (89) 4/10 - 2/3\n'
                         + '[Rectangle] (89) 4/5 - 2/3\n',
                         mock_stdout.getvalue())

    def test_dictionary(self):
        r = Rectangle(3, 5, 6, 2, 94)
        self.assertIsInstance(r.to_dictionary(), dict)
        self.assertEqual(r.to_dictionary(), {
            'id': 94,
            'width': 3,
            'height': 5,
            'x': 6,
            'y': 2
        })

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create(self, mock_stdout):
        print(Rectangle.create(id=94))

        res = '[Rectangle] (94) 0/0 - 1/1\n'
        self.assertEqual(mock_stdout.getvalue(), res)


    def test_save(self):
        r1 = Rectangle(5, 6, 8, 4, 98)
        r2 = Rectangle(3, 5, 1, 5, 99)

        Rectangle.save_to_file([r1, r2])

        rlist = Rectangle.load_from_file()
        self.assertEqual(r1.__dict__, rlist[0].__dict__)
        self.assertEqual(r2.__dict__, rlist[1].__dict__)


if __name__ == '__main__':
    unittest.main()
