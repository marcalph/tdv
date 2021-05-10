
#O(n*l) n size of nums array; l range of cursum
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(index=0, cursum=0):          
            key = (index, cursum)
            
            if index == len(nums):                    
                return 1 if cursum == target else 0
            if key not in memo:
                memo[key] = dfs(index+1, cursum + nums[index]) + dfs(index+1, cursum - nums[index])                    
                        
            return memo[key]                                                             
                
        return dfs()