class Ticket:
    def __init__(self,id,desc) -> None:
        self.ticket_id = id
        self.issue_description = desc
    
class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self,id,desc):
        self.stack.append(Ticket(id,desc))
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack

class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self,x):
        self.queue.append(x)
    
    def dequeue(self,stack:Stack):
        x = self.queue.pop()
        stack.push(x.ticket_id,x.issue_description)
    
    def peek(self):
        return self.queue