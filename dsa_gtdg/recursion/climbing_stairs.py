#O(n) spacetime
class Solution:
    def climbStairs(self, n: int) -> int:
        mem={}
        def helper(i, n, mem):
            if i>n:
                return 0
            if n == i:
                return 1
            if i in mem:       
                return mem[i]
            else:
                mem[i] = helper(i+1,n, mem)+helper(i+2,n,mem)
                return mem[i]
        return helper(0,n, mem)