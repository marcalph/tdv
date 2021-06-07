#min heap construction w/ array
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

	# O(n)!! because every sift is not equal those from the bottom 
	# takes O(1)
    def buildHeap(self, array):
        # Write your code here.
		last_parent = self.get_parent_idx(len(array)-1)
        for idx in reversed(range(last_parent+1)):
			self.siftDown(idx, array)
		return array
		
	def has_parent(self, index):
		return index > 0
	
	def is_left_child(self, index):
		# left is uneven
		return index%2 == 1
	
	def is_right_child(self, index):
		# right is even
		return index%2 == 0
	
	def get_parent_idx(self, index):
		return (index-1)//2

	
	def has_left_child(self, index, heap):
		return len(heap)-1 >= 2*index+1
	
	def has_right_child(self, index, heap):
		return len(heap)-1 >= 2*index+2
	
	def get_left_child_idx(self, index):
		return 2*index+1
	
	def get_right_child_idx(self, index):
		return 2*index+2
	
	#O(log n)
    def siftDown(self, index, heap):
        # Write your code here.
		left_child = self.get_left_child_idx(index)
		while left_child <= len(heap)-1:
			right_child = self.get_right_child_idx(index) if self.has_right_child(index, heap) else -1
        	if right_child != -1 and heap[left_child]>heap[right_child]:
				swap_index = right_child
			else:
				swap_index = left_child
			if heap[swap_index] < heap[index]:
				heap[index], heap[swap_index] =  heap[swap_index], heap[index]
				index = swap_index
				left_child = self.get_left_child_idx(index)
			else:
				return
			
	#O(log n)	
    def siftUp(self):
        # Write your code here.
        cur = len(self.heap)-1
		while self.has_parent(cur) and self.heap[self.get_parent_idx(cur)] > self.heap[cur]:
			parent_idx = self.get_parent_idx(cur)
			self.heap[parent_idx], self.heap[cur] =  self.heap[cur], self.heap[parent_idx]
			cur = parent_idx
		
    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.heap[len(self.heap)-1], self.heap[0] = self.heap[0], self.heap[len(self.heap)-1]
		removed = self.heap.pop()
		self.siftDown(0, self.heap)
		return removed

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
		self.siftUp()