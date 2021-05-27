from collections import Counter


# two sum pb
# O(nlogn) w/ sort or O(n) w/ hashmap
def numberOfWays(arr, k):
 	# Write your code here
  nways = 0
  arr.sort()
  l, r = 0, len(arr)-1
  cnt = Counter(arr)
  while l<r:
    candidate_pair = arr[l]+arr[r]
    if candidate_pair == k:
      print(cnt)
      if arr[l]==arr[r] and cnt[arr[l]]>2:
        nways += cnt[arr[l]]*(cnt[arr[l]]-1)/2
        break
      else:
        nways+=1
        l+=1
        r-=1
    elif candidate_pair > k:
      r-=1
    else:
      l+=1
  return nways
  