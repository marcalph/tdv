#O(n) spacetime
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = len(T)*[0]
        stack = []
        for idx in range(len(T)-1,-1,-1):
            while stack and T[idx]>=stack[-1][0]:
                stack.pop()
            if stack and T[idx]<stack[-1][0]:
                offset = stack[-1][1]-idx
                res[idx]=(offset)
            stack.append((T[idx],idx))
        return (res)
            
            