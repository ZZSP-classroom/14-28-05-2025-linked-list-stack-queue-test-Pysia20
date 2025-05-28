import unittest
from library_reservation import *

class tests(unittest.TestCase):
    def test_enqueue(self):
        sys = Queue()
        sys.enqueue("on","test")
        self.assertEqual(sys.peek()[0].user_name, "on")
    
    def test_dequeue(self):
        sys = Queue()
        sys.enqueue("on","test")
        sys.enqueue("on2","test2")
        sys.dequeue()
        self.assertEqual(sys.peek()[0].user_name, "on2")
    
    def test_peek(self):
        sys = Queue()
        sys.enqueue("on","test")
        sys.enqueue("on2","test2")
        self.assertEqual(sys.peek()[1].user_name, "on2")


if __name__ == '__main__':
    unittest.main()