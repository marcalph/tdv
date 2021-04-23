# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j 
# such that nums[i] == nums[j] and abs(i - j) <= k.

# O(n) time | O(k)space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm={}
        for i,v in enumerate(nums):
            if v in hm:
                return True
            hm[v] = hm.get(v,i)
            if len(hm)>k:
                del hm[nums[i-k]]
        return False

containsNearbyDuplicate([1,2,3,1],3)