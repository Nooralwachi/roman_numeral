import unittest
from roman_numeral import roman_numeral

class Testword(unittest.TestCase):
    def test_roman_numeral(self):
        self.assertEqual(roman_numeral('XXXVI'),36)
        self.assertEqual(roman_numeral('XXVII'),27)
        self.assertEqual(roman_numeral('XIII'),13)
        self.assertEqual(roman_numeral('XIX'),19)
        self.assertEqual(roman_numeral('IV'),4)
        self.assertEqual(roman_numeral('IX'),9)
        self.assertEqual(roman_numeral('CCIC'),299)
        self.assertEqual(roman_numeral('DM'),500)
        self.assertEqual(roman_numeral('VM'),995)
        self.assertEqual(roman_numeral('XIVC'),86)
        self.assertEqual(roman_numeral('MCM'),1900)
        self.assertEqual(roman_numeral('MM'),2000)
        self.assertEqual(roman_numeral('MMXXI'),2021)

unittest.main()
