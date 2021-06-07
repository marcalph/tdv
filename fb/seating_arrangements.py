
def minOverallAwkwardness(arr):
  # Write your code here
  arr.sort()
  q = deque([arr[-1]])
  for i in range(len(arr)-1,0,-1):
    if i%2==0:
      q.appendleft(arr[i])
    else:
      q.append(arr[i])
  print(q)
  
  diff = abs(q[-1]-q[0])
  for i in range(1, len(arr)): # bad
    diff = max(diff, abs(q[i]-q[i-1]))
  return diff