# brute force sort and handpick median O(nlogn), O(n)
# keep sorted >> insertion sort + binary search O(n), spacetime
# double heaps O(logn), O(n)
def findMedian(arr):
  # Write your code here
  lo = []
  hi = []
  res = []
  import heapq
  
  for i in range(len(arr)):
    heapq.heappush(lo, -arr[i])
    k = heapq.heappop(lo)
    heapq.heappush(hi, -k)
    if len(lo)<len(hi):
      heapq.heappush(lo, -hi[0])
      heapq.heappop(hi)
    print(i, lo, hi)
    if i%2==0:
      res.append(-lo[0])
    else:
      res.append((hi[0]-lo[0])//2)  
  return res