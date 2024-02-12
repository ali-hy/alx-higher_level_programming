#!/usr/bin/python3
"""Test for the Base class"""
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from models.base import Base


class BaseTest(unittest.TestCase):
    """Test cases for the Base class"""

    def test_exists(self):
        '''Check that the Base class exists and has docs'''
        self.assertIsNotNone(Base)
        self.assertGreater(len(Base.__doc__), 0)

    def test_id(self):
        '''Test the constructor's ability to generate id's'''
        l = [Base(), Base(12), Base(), Base(), Base(123)]
        self.assertListEqual([b.id for b in l], [1, 12, 2, 3, 123])


if __name__ == '__main__':
    unittest.main()
