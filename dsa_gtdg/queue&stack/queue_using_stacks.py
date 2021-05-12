class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.revstack = []
    
    #O(n) spacetime
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack:
            self.stack.append(x)
        else:
            while self.stack:
                popped = self.stack.pop()
                self.revstack.append(popped)
            self.stack.append(x)
            while self.revstack:
                popped = self.revstack.pop()
                self.stack.append(popped)
            
    #O(1)sapcetime
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack)==0













# queue
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # O(1)time | O(n)space
    def push(self, x):
        self.s1.append(x)

    # O(n) amortized O(1) time, O(1)space
    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2



