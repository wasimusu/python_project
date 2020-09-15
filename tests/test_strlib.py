from python_project import strlib
import unittest


class StrlibTest(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(strlib.split("how are you?"), ["how", "are", "you?"])
        self.assertEqual(strlib.split("how are you?", ' '), ["how", "are", "you?"])
        self.assertEqual(strlib.split("how"), ["how"])
        self.assertEqual(strlib.split("apple,banana,orange", ','), ["apple", "banana", "orange"])

    def test_add_invalid_input(self):
        self.assertRaises(ValueError, strlib.split, "how are you", 1)
        self.assertRaises(ValueError, strlib.split, 123)
        self.assertRaises(ValueError, strlib.split, ["how are you?"])
        self.assertRaises(ValueError, strlib.split, {"hello": "how"})
