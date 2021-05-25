# O(logn) spacetime
def myPow(self, x: float, n: int) -> float:
    mem = {-1: 1/x, 0: 1, 1: x}
    def helper(x, n, mem):
        # base case
        if n in mem:
            return mem[n]
        else:
            if n<0:
                mem[n] =  helper(x, n//2, mem) * helper(x, (n+1)//2, mem)
            else:
                mem[n] = helper(x, n//2, mem) * helper(x, n//2, mem) * helper(x,n-n//2-n//2, mem)
            return mem[n]
    return helper(x, n, mem)