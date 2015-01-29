__author__ = 'ysahn'

from text2num import text2num
from semantic.numbers import NumberService
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_get_a_story(self):
        numservice = NumberService()
        result  = numservice.parse("11")

        print(result)

        self.assertEqual( 1 , text2num("one"))
        self.assertEqual( 12 , text2num("twelve"))
        self.assertEqual( 72 , text2num("seventy two"))
        self.assertEqual( 300 , text2num("three hundred"))
        self.assertEqual( 1200 , text2num("twelve hundred"))
        self.assertEqual( 12304 , text2num("twelve thousand three hundred four"))
        self.assertEqual( 6000000 , text2num("six million"))
        self.assertEqual( 6400005 , text2num("six million four hundred thousand five"))
        self.assertEqual( 123456789012 , text2num("one hundred twenty three billion four hundred fifty six million seven hundred eighty nine thousand twelve"))
        self.assertEqual( 4000000000000000000000000000000000 , text2num("four decillion"))