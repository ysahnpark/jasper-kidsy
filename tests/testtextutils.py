__author__ = 'ysahn'

from textutils import segment_text
from semantic.numbers import NumberService
import unittest

class TestTextUtils(unittest.TestCase):

    def test_segment_text(self):
        text = 'aaa bbb cc dd'
        result = segment_text(text, 4)
        print(result)
        expected = ['aaa ', 'bbb ', 'cc ', 'dd']
        self.assertEqual(expected, result, '4s')

        result = segment_text(text, 6)
        print(result)
        expected = ['aaa ', 'bbb ', 'cc dd']
        self.assertEqual(expected, result, '5s')

        result = segment_text(text, 8)
        print(result)
        expected = ['aaa bbb ', 'cc dd']
        self.assertEqual(expected, result, '8s')
