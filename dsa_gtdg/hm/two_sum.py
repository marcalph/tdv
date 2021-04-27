

# O(n) time | O(n) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed = {}
        for i, v in enumerate(nums):
            if target - v in viewed:
                return viewed[target-v], i
            viewed[v]=i

# other approach w/ l,r pointers w/ sort
# O(nlog(n)) time | O(1) space
