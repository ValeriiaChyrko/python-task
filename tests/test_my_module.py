import unittest
from src.my_module import greet, is_even

class TestMyModule(unittest.TestCase):

    def test_greet_passed(self):
        self.assertEqual(greet("Ivan"), "Hello, Ivan!")
        self.assertEqual(greet("Maria"), "Hello, Maria!")

    def test_is_even_passed(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-1))
        self.assertTrue(is_even(-2))

    def test_greet_failed(self):
        self.assertEqual(greet("Maria"), "Hello, Ivan!")

if __name__ == '__main__':
    unittest.main()