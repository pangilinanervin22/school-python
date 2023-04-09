import unittest
# import the is_prime function

from sample import isEven


class TestPrime(unittest.TestCase):
    def test_two(self):
        self.assertEqual(isEven(2), True)

    def test_five(self):
        self.assertEqual(isEven(5), False)

    def test_nine(self):
        self.assertEqual(isEven(0), True)

    def test_eleven(self):
        self.assertEqual(isEven(11), True)


if __name__ == '__main__':
    unittest.main()
