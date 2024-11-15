import unittest

from lesson1.hello import greet


class HelloWorldTest(unittest.TestCase):
    def test_greet(self) -> None:
        self.assertEqual("Hello, world!", greet("world"))
        self.assertEqual("Hello, Alice!", greet("Alice"))
