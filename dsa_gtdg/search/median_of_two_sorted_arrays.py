class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # lets always consider smaller array as array 1
        if len(nums1)> len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        if m > n :
            return self.findMedianSortedArrays(nums2, nums1)
        k = (m + n - 1) // 2
        l = 0
        r = m #min(m, k)
        #start binarysearch
        while l < r:
            midNums1 = (l + r) // 2
            midNums2 = k - midNums1
            if nums1[midNums1] < nums2[midNums2]:
                l = midNums1+1
            else:
                r = midNums1
        # after binary search, we almost get the median because it must be between
        # these 4 numbers: A[l-1], A[l], B[k-l], and B[k-l+1] 
    
        # if (n+m) is odd, the median is the larger one between A[l-1] and B[k-l].
        # and there are some corner cases we need to take care of.
        a = max(nums1[l-1] if l > 0  else float('-inf'), nums2[k-l] if k-l >= 0 else float('-inf'))
        if (m + n) %2  == 1:
            return a
        b = min(nums1[l] if l < m else float('inf'), nums2[k-l+1] if k-l+1 < n else float('inf'))
        return (a+b)/2.0