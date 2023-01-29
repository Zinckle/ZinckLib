import unittest
from src.ZinckLib import numberToText


class NumberToTextTestCases(unittest.TestCase):

    def test_zero(self):
        result = numberToText(0)
        self.assertEqual(result, "zero")

    def test_invalidType(self):
        with self.assertRaises(TypeError):
            numberToText("a")


if __name__ == '__main__':
    unittest.main()
