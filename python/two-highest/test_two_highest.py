from unittest import TestCase

from two_highest import two_highest


class TestTwoHighest(TestCase):

    def test_fib(self):
        self.assertEqual(two_highest([1, 2, 3, 4, 5]), (5, 4))
        self.assertEqual(two_highest([2, 4, 12, 10, 8]), (12, 10))
        self.assertEqual(two_highest([-10, -5, 0, -2, -3]), (0, -2))
