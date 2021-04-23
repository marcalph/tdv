
# Given a string s, return the first non-repeating character 
# and return its index. 
# If it does not exist, return -1.

# O(n) time | O(1) space not O(n) number of char is bounded 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        viewed = {}
        pos = {}
        for i, char in enumerate(s):
            pos[char]=i
            viewed[char]=viewed.get(char,0)+1
            
        kmin = min(viewed, key=viewed.get)
        
        if viewed[kmin]==1:
            return pos[kmin]
        else:
            return -1