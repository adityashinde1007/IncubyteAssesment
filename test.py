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

    def test_mult_num_add(self):
        res = StringCalculator().add("3,6,1")
        self.assertEqual(res, 3 + 6 + 1)

    def test_third_step(self):
        res = StringCalculator().add("3,6,1,c")
        self.assertEqual(res, 3 + 6 + 1 + 3)

    def test_third_2_step(self):
        res = StringCalculator().add("b,z,1,c")
        self.assertEqual(res, 2 + 26 + 1 + 3)

    def test_third_3_step(self):
        res = StringCalculator().add("1,2,a,c")
        self.assertEqual(res, 7)

    def test_negative_step(self):
        with self.assertRaises(Exception) as e:
            StringCalculator().add("1,2,-3,a,c")
        print(e.exception)

    def test_negative_2_step(self):
        with self.assertRaises(Exception) as e:
            StringCalculator().add("-9,3,4")
        print(e.exception)

    def test_multiple_negative_step(self):
        with self.assertRaises(Exception) as e:
            StringCalculator().add("-9,3,-4,a")
        print(e.exception)

    def test_multiple_negative_2_step(self):
        with self.assertRaises(Exception) as e:
            StringCalculator().add("-10,-76,34,-22,z")
        print(e.exception)

    def test_greater_than_1000_step(self):
        res = StringCalculator().add("1003,2000,a,c")
        self.assertEqual(res, 4)


if __name__ == '__main__':
    unittest.main()
