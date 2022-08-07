import unittest

import Ex_2_FizzBuzz.fizzbuzz as fizzbuzz


class TestFizBuzz(unittest.TestCase):


    # def test_canCallFizzBuzz(self):
    #     fizzbuzz.fizz_buzz(1)

    def checkValWithExpected(self, val, expected):
        ret = fizzbuzz.fizz_buzz(val)
        self.assertEqual(ret, expected)

    def test_callFizzBuzzReturns1WhenPassed1(self):
        # self.assertEqual(fizzbuzz.fizz_buzz(1), "1")
        self.checkValWithExpected(1, "1")

    def test_callFizzBuzzReturns2WhenPassed2(self):
        # self.assertEqual(fizzbuzz.fizz_buzz(2), "2")
        self.checkValWithExpected(2, "2")

    def test_callFizzBuzzReturnsFizzWhenPassed3(self):
        self.checkValWithExpected(3, "Fizz")

    def test_callFizzBuzzReturnsBuzzWhenPassed5(self):
        self.checkValWithExpected(5, "Buzz")

    def test_callFizzBuzzReturnsFizzWhenPassedMultipleOf3(self):
        self.checkValWithExpected(6, "Fizz")

    def test_callFizzBuzzReturnsBuzzWhenPassedMultipleOf5(self):
        self.checkValWithExpected(10, "Buzz")

    def test_callFizzBuzzReturnsFizzBuzzWhenPassed15(self):
        self.checkValWithExpected(15, "FizzBuzz")