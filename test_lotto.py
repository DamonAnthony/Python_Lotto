# Damon Anthony Class 1

from unittest import TestCase
from lotto_func import *


class TestLotto(TestCase):

    def test_generate_lotto_num(self):
        lotto_numbers = generate_lotto_num()

        self.assertEqual(len(lotto_numbers), 6, "Should be six")

        self.assertGreater(lotto_numbers[5], lotto_numbers[0], "Should be true, list sorted in ascending order")

    def test_checking_matches(self):

        self.assertEqual(checking_matches([1, 2, 3], [3, 4, 5]), 1, "Should be 1")

        self.assertEqual(checking_matches([11, 22, 33], [11, 22, 33]), 3, "Should be 3")

        self.assertEqual(checking_matches([11, 25, 37, 67], [13, 23, 43, 63]), 0, "Should be 0")

    def test_prize_check(self):

        self.assertEqual(prize_check(5), 8584.00, "should be 8584.00")

        self.assertEqual(prize_check(3), 100.50, "Should be 100.50")
