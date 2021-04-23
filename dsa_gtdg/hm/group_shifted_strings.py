# MEDIUM
# We can shift a string by shifting each of its letters to its successive letter.

# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.

# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.



class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hm = {}
        for s in strings:
            diff = "".join([str((ord(i)-ord(j))%26) for i,j in zip(s,s[1:])]) #copy       
            hm[diff]=hm.get(diff,[])+[s]
        return hm.values()