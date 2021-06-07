import math
# Add any extra import statements you may need here
def bin_search(arr, value):
  l, r = 0, len(arr)-1
  while l<r:
    mid = (l+r)//2
    if arr[mid]>=value:
      r = mid
    elif arr[mid]<value:
      l = mid+1
  return l

# Add any helper functions you may need here


def getMilestoneDays(revenues, milestones):
  print(revenues)
  
  cursum = 0
  for i in range(len(revenues)):
    cursum += revenues[i]
    revenues[i] = cursum 
  print(revenues)
  print(milestones)
  
  res = []
  for m in milestones:
    res.append(bin_search(revenues,m)+1)
  
  print(res)
  return res