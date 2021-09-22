from python_project import split_string_add_nums
import unittest


class ComboTest(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(split_string_add_nums("1,1"), 2)
        self.assertEqual(split_string_add_nums("-1,1"), 0)
        self.assertEqual(split_string_add_nums("1,-1"), 0)
        self.assertEqual(split_string_add_nums("0,0"), 0)
        self.assertNotEqual(split_string_add_nums("0,2"), 0)
