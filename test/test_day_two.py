import unittest

import src.day_one as d1

test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


class TestDayOne(unittest.TestCase):
    def setUp(self):
        self.test_input = test_input

    def test_create_data(self):
        out = d1.create_data(self.test_input)
        self.assertEqual(out[0], "-68")
        self.assertEqual(out[-1], "-82")

    def test_day_one(self):
        out = d1.create_data(self.test_input)
        ans_one = d1.calc_part_a(out)
        self.assertEqual(ans_one, 3)

    def test_day_two(self):
        out = d1.create_data(self.test_input)
        ans_one = d1.calc_part_b(out)
        self.assertEqual(ans_one, 6)
