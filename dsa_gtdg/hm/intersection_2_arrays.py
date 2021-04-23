# Given two integer arrays nums1 and nums2, 
# return an array of their intersection. 
# Each element in the result must be unique and 
# you may return the result in any order.

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)