# brute force sort and handpick median O(nlogn), O(n)
# keep sorted >> insertion sort + binary search O(n), spacetime
# double heaps O(logn), O(n)

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
		self.lo = []
		self.hi = []
		self.len = 0
		import heapq
		
    def insert(self, number):
        # Write your code here.
		import heapq
		self.len +=1
		heapq.heappush(self.lo, -number)
		k = heapq.heappop(self.lo)
		heapq.heappush(self.hi, -k)
		if len(self.lo)<len(self.hi):
			heapq.heappush(self.lo, -self.hi[0])
			heapq.heappop(self.hi)
		if self.len%2==1:
			self.median = -self.lo[0]
		else:
			print(self.len)
			self.median = (self.hi[0]-self.lo[0])/2
		print(self.lo)
		print(self.hi)
		
    def getMedian(self):
        return self.median