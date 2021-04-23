# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".


# O(m) time | O(m+n)space
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        js = set(jewels)
        cnt = 0
        for st in stones:
            if st in js:
                cnt+=1
        return cnt
        