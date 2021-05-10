#O(n) spacetime
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opstack = []
        res = 0
        if len(tokens)==1:
            return int(tokens[0])
        for t in tokens:
            if t not in ["+","-","/","*"]:
                opstack.append(t)
            else:
                a = opstack.pop()
                b = opstack.pop()
                res=int(eval(b+t+a))
                opstack.append(str(res))
        return (res)
            
        