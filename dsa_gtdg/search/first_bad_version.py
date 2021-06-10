# find fisrt bad version
# binary search template 2 
# looking to evaluate something on the right of pointer
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 and isBadVersion(n):
            return n

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid 
            else:
                left = mid +1

        return left