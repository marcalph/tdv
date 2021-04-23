#!/usr/bin/python
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s 
# can be replaced to get t.

# All occurrences of a character must be replaced with another
# character while preserving the order of characters.
# No two characters may map to the same character, 
# but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t) or len(set(s))!=len(set(t)):
            return False
        hm = {}
        teststring = []
        for cs, ct in zip(s,t):
            if cs in hm and hm[cs]!=ct:
                return False
            else:
                hm[cs]=ct
        return True

s = Solution()
"""
Input: s = "egg", t = "add"
Output: true
"""
print(s.isIsomorphic("egg", "add"))  
"""
Input: s = "foo", t = "bar"
Output: false
"""
print(s.isIsomorphic("foo", "bar"))  
"""
Input: s = "paper", t = "title"
Output: true
"""
print(s.isIsomorphic("paper", "title"))    