def min_length_substring(s, t):
  # Write your code here
  idx_q = []
  from collections import Counter
  needed = Counter(t)
  min_length = float("inf")
  for i in range(len(s)):
    if s[i] in needed:
      idx_q.append((i, s[i]))
      needed[s[i]]=max(0, needed[s[i]]-1)
      if sum(needed.values())==0:#bad
        tup = idx_q.pop(0)
        min_length = min(min_length, i-tup[0]+1)
        needed[tup[1]]+=1
    print(needed)
  return min_length if min_length!=float("inf") else -1