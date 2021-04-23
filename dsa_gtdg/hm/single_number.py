# Given a non-empty array of integers nums,
# every element appears twice except for one. 
# Find that single one.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        viewed = {}
        for i in nums:
            viewed[i] = viewed.get(i, 0)+1
        return min(viewed, key=viewed.get)

# O(n) time | O(n) space as above w/ hashmap
#############
# see math
# bit manipulation

