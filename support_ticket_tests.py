import unittest
from support_ticket import *

class tests(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1,"desc")
        self.assertEqual(stack.peek()[0].issue_description, "desc")
    
    def test_pop(self):
        stack = Stack()
        stack.push(1,"desc")
        stack.push(2,"desc2")
        self.assertEqual(stack.pop().issue_description, "desc2")
    
    def test_enqueue(self):
        stack = Stack()
        stack.push(1,"desc")
        stack.push(2,"desc2")
        queue = Queue()
        queue.enqueue(stack.pop())
        self.assertEqual(queue.peek()[0].issue_description, "desc2")
    
    def test_dequeue(self):
        stack = Stack()
        stack.push(1,"desc")
        stack.push(2,"desc2")
        queue = Queue()
        queue.enqueue(stack.pop())
        queue.enqueue(stack.pop())
        queue.dequeue(stack)
        self.assertEqual(stack.peek()[0].issue_description, "desc")



if __name__ == '__main__':
    unittest.main()