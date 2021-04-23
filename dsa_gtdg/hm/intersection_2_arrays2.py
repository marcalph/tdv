# Given two integer arrays nums1 and nums2, 
# return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays 
# and you may return the result in any order.


# 0(l2) time, O(l1) where l1<l2

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        res = []
        if len(nums1)>len(num2):
            nums1, nums2 = nums2, nums1
        for n in nums1:
            hm[n] = hm.get(n, 0) + 1
        for n in nums2:
            if n in hm:
                hm[n]= hm.get(n, 0) - 1
                if hm[n]>-1:
                    res.append(n)
        return res
# if sorted arrays O(n+m)time | O(n+m)
# i, j = 0, 0
# for i in smol:
#     if i<j:
#         i++
#     elif j<i:
#         j++
#     else:
#         res.append(i)
#         i++
#         j++



