#O(1) time, O(size) space
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.size=size
        self.window_sum=0
        self.count=0

    def next(self, val: int) -> float:
        self.count+=1
        self.values.append(val)
        tail = self.values.pop(0) if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / len(self.values)
