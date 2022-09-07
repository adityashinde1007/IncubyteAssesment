import unittest
from . stringtdd import StringCalculator

class simpletest(unittest.TestCase):

    def test_2_num_add(self):
        res = StringCalculator().add("1,2")
        self.assertEqual(res, 3)

    def test_blank_num_add(self):
        res = StringCalculator().add("")
        self.assertEqual(res, 0)

    def test_single_num_add(self):
        res = StringCalculator().add("4")
        self.assertEqual(res, 4)

if __name__ == '__main__':
    unittest.main()
