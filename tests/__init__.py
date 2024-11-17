import unittest
from src import greet, is_even

class TestMyModule(unittest.TestCase):

    def test_greet_passed(self):
        self.assertEqual(greet("Іван"), "Привіт, Іван!")
        self.assertEqual(greet("Марія"), "Привіт, Марія!")

    def test_is_even_passed(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-1))
        self.assertTrue(is_even(-2))

    def test_greet_failed(self):
        self.assertEqual(greet("Марія"), "Привіт, Іван!")

if __name__ == '__main__':
    unittest.main()