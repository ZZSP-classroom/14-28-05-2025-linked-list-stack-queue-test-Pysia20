import unittest
from browser_history import *

class tests(unittest.TestCase):
    def test_push(self):
        sys = Stack()
        sys.push("url")
        self.assertEqual(sys.peek()[0], "url")
    
    def test_pop(self):
        sys = Stack()
        sys.push("url")
        sys.push("url2")
        sys.pop()
        self.assertEqual(sys.peek()[0], "url")
    
    def test_peek(self):
        sys = Stack()
        sys.push("url")
        sys.push("url2")
        self.assertEqual(sys.peek()[1], "url2")


if __name__ == '__main__':
    unittest.main()