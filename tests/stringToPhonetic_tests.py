import unittest
from ZinckLib import stringToPhonetic


class StringToPhoneticTestCases(unittest.TestCase):

    def test_empty(self):
        result = stringToPhonetic("")
        self.assertEqual(result, [])

    def test_invalidType(self):
        with self.assertRaises(TypeError):
            stringToPhonetic(1)


if __name__ == '__main__':
    unittest.main()
