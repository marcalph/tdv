
# O(n), O(1)
# number of contiguous sub arr
# think left+right
def count_subarrays(arr):
  # Write your code here
  curmax = float("-inf")
  prev = None
  n = len(arr)
  
  left = [1] * n
  right = []
  for i in range(1, n):
    curmax = max(curmax, arr[i])
    if arr[i]==curmax:
      left[i]=i+1
    elif arr[i]>=arr[i-1]:
      left[i]+=left[i-1]
    else:
      pass
  
  right = [1] * n
  curmax = float("-inf")
  for i in range(-2,-n-1,-1):
    curmax = max(arr[i], curmax)
    if arr[i]==curmax:
      right[i]=abs(i)
    elif arr[i]>arr[i+1]:
      right[i]+=right[i+1]
    else:
      pass