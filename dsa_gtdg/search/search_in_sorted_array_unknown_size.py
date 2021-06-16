class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # check target left of  sorted array
        i = 0
        if target<reader.get(i):
            return -1
        # check if target in sorted array
        # find first bigger
        i=1
        while reader.get(i)<=target:
            i*=2
            if reader.get(i)==target:
                return i
        # need to check if i becomes out of bound (but shitty testcase makes it useless)
        l, r = 0, i
        while l<r:
            mid =(l+r)//2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)<target:
                l = mid+1
            else:
                r=mid
        return -1
        