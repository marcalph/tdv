# MEDIUM
# Given an array of strings strs, 
# group the anagrams together. 
# You can return the answer in any order.

# O(nl*log(l)) time| O(nl) space, l length of string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        print(strs)
        for s in strs:
            hm["".join(sorted(s))]=hm.get("".join(sorted(s)), [])+[s]
            
        return hm.values()
# could group by letter count
#results in O(nl) spacetime