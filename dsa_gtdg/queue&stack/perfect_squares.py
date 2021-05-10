#O(n^(h/2)) time, n^.5 number of perfect squares
#O(n^.5) space for perfect squares
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_sq  =[i**2 for i in range(1, int(n**.5)+1)][::-1]        
        q = {n}
        subs=1
        while q:
            nextq = set()
            for remain in q:
                for sq in perfect_sq:
                    new_val = remain - sq
                    if new_val<0:
                        continue
                    elif new_val==0:
                        return subs
                    else:
                        nextq.add(new_val)
            q = nextq
            subs+=1
            