from python_project import mathlib
import unittest


class MathlibTest(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(mathlib.add(1, 1), 2)
        self.assertEqual(mathlib.add(-1, 1), 0)
        self.assertEqual(mathlib.add(1, -1), 0)
        self.assertEqual(mathlib.add(0, 0), 0)

    def test_add_invalid_input(self):
        self.assertRaises(ValueError, mathlib.add, 1, '1')
        self.assertRaises(ValueError, mathlib.add, '1', '1')
        self.assertRaises(ValueError, mathlib.add, [1], '1')
        self.assertRaises(ValueError, mathlib.add, [1], 0)
        self.assertRaises(ValueError, mathlib.add, [1], [2])
