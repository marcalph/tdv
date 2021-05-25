
class Solution:
    def fib(self, n: int) -> int:
        mem = {}
        def helper(n , mem):
            if n < 2:
                return n
            if n not in mem:
                mem[n] = helper(n-1, mem)+helper(n-2, mem)    
            return mem[n]
        return helper(n, mem)