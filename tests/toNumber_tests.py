import unittest
from ZinckLib import toNumber


class ToNumbersTestCases(unittest.TestCase):

    def test_empty(self):
        result = toNumber("")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()