import unittest
from main import wordsToNumber

class TestWordsToNumber(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(wordsToNumber(["one"]), 1)
        self.assertEqual(wordsToNumber(["five"]), 5)

    def test_two_digits(self):
        self.assertEqual(wordsToNumber(["twenty", "one"]), 21)
        self.assertEqual(wordsToNumber(["thirty", "five"]), 35)

    def test_hundreds(self):
        self.assertEqual(wordsToNumber(["one", "hundred"]), 100)
        self.assertEqual(wordsToNumber(["two", "hundred", "thirty", "four"]), 234)

    def test_thousands(self):
        self.assertEqual(wordsToNumber(["one", "thousand"]), 1000)
        self.assertEqual(wordsToNumber(["three", "thousand", "two", "hundred", "ten"]), 3210)

    def test_millions(self):
        self.assertEqual(wordsToNumber(["one", "million"]), 1000000)
        self.assertEqual(wordsToNumber(["two", "million", "three", "hundred", "forty", "five", "thousand", "six", "hundred", "seventy", "eight"]), 2345678)

    def test_edge_cases(self):
        self.assertEqual(wordsToNumber([]), 0)
        self.assertEqual(wordsToNumber(["zero"]), 0)

if __name__ == '__main__':
    unittest.main()