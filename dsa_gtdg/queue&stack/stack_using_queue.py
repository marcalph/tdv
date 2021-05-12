class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.queue: # if queue is empty
            self.queue.append(x)
        else:
            self.queue.append(x)
            for _ in range(len(self.queue)-1):
                popped = self.queue.pop(0)
                self.queue.append(popped)
            print(self.queue)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop(0)
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue)==0
        
