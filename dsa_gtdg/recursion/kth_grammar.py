#O(logk) spacetime
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n, k):
            # base case
            if n==1:
                return 0
            #recurrence
            else:
                if k<=2**(n-2):
                    return helper(n-1, k)
                else:
                    return 1-helper(n-1, k-2**(n-2))
        
        return helper(n,k)