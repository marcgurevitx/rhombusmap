import unittest

from rhombusmap import RhombusMap


class RhombusMapTest(unittest.TestCase):
    def test_basic(self):
        rm = RhombusMap(diagonal=7)
        self.assertEqual(rm[0, 0], None)
        rm[0, 0] = "hello"
        self.assertEqual(rm[0, 0], "hello")

    def test_wrap(self):
        rm = RhombusMap(diagonal=7)
        self.assertEqual(rm[0, 0], None)
        rm[2, -1] = "hello"
        self.assertEqual(rm[2, -1], "hello")
        self.assertEqual(rm[-1, 3], "hello")
        self.assertEqual(rm[3, 6], "hello")
        self.assertEqual(rm[6, 2], "hello")
        self.assertEqual(rm[5, -5], "hello")
        self.assertEqual(rm[9, -2], "hello")

    def test_wrap_ccw(self):
        rm = RhombusMap(diagonal=7, wrap_cw=False)
        self.assertEqual(rm[0, 0], None)
        rm[2, -1] = "hello"
        self.assertEqual(rm[2, -1], "hello")
        self.assertEqual(rm[-2, 2], "hello")
        self.assertEqual(rm[1, 6], "hello")
        self.assertEqual(rm[5, 3], "hello")
        self.assertEqual(rm[6, -4], "hello")
        self.assertEqual(rm[9, 0], "hello")
