# O(n) spacetime
def are_they_equal(array_a, array_b):
  # Write your code here
  from collections import Counter
  cnt = Counter(array_a)
  for n in array_b:
    if n in cnt:
      if cnt[n]<0:
        return False
      cnt[n]-=1
    else:
      return False
  return True

