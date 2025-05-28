class User:
    def __init__(self,user_name,book_title) -> None:
        self.user_name = user_name
        self.book_title = book_title

class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self,user_name,book_title):
        self.queue.append(User(user_name,book_title))
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue
    