# O(n log n), O(1)
"""
Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the worst possible penalty for a given input."""
def getTotalTime(arr):
  # Write your code here
  arr.sort()
  run_pen = 0
  cur_pen = 0
  while len(arr)>1:
    cur_pen = arr.pop()+arr.pop()
    arr.append(cur_pen)
    run_pen+=cur_pen
  return run_pen

#O(n log n), O(n)
def getTotalTime(arr):
  # Write your code here
  heap = [-1*a for a in arr]
  heapq.heapify(heap)       # O(n)
  cur_pen = 0               # current penalty
  run_pen = 0               # running penalty
  while len(heap)>1:        # O(n)
    cur_pen = heapq.heappop(heap) + heapq.heappop(heap) 
    heapq.heappush(heap, cur_pen)
    run_pen-=cur_pen
  return run_pen

