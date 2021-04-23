# MEDIUM not good
# Given a string s, find the length of the longest substring without repeating characters.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # todo
        # keep track of max length
        hm = {}
        l,maxlen = 0,0 #left pointer, current max length
        for r, c in enumerate(s): #right pointer, char
        
            if c in hm:
                l=max(hm[c]+1,l)
            
            maxlen = max(maxlen,r-l+1)
            hm[c]=r
            
        return maxlen
            