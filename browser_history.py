class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self,x):
        self.stack.append(x)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack

