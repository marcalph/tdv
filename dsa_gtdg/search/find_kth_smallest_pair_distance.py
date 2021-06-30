class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(n - 1)]
        heapify(heap)

        for _ in range(k):
            d, root, nei = heappop(heap)
            if nei + 1 < n:
                heappush(heap, (nums[nei + 1] - nums[root], root, nei + 1))

        return d

    
#O(k log n+n log n)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        def enough(distance):
            count, slow, fast = 0,0,0
            while slow<len(nums):
                while fast<len(nums) and nums[fast]-nums[slow]<=distance:
                    fast+=1
                count+=fast-slow-1
                slow+=1
            return count>=k
        
        l,r=0, nums[-1]-nums[0]
        while l<r:
            mid = l+r>>1
            if enough(mid):
                r=mid
            else:
                l=mid+1
        return l