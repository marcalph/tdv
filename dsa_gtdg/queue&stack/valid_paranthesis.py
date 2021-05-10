
#O(n) spacetime
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"]":"[", ")":"(", "}":"{"}
        for char in s:
            if char in ["(","[", "{"]:
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                if stack[-1]==mapping[char]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
                