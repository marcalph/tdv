# search in rotated sorted array
# binary search in two pass
# O(log n )spacetime
# could be done in one pass
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #first locate the min
        def find_min(nums):
            l, r = 0, len(nums)-1
            if nums[l]<nums[r]:
                return 0
            
            while l<=r:
                mid = (l+r)//2
                if  nums[mid]>nums[mid+1]:
                    return mid+1
                if nums[mid]>=nums[l]: #left of mid is sorted
                    l = mid+1
                else:
                    r = mid-1
            
        
        def search(l, r):
            while l<=r:
                mid = (l+r)//2
                if  target == nums[mid]:
                    return mid
                if  target > nums[mid]: #left of mid is sorted
                    l = mid+1
                else:
                    r = mid-1
            return -1
        
        
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        min_idx = find_min(nums)
        print(min_idx)
        
        if nums[min_idx]==target:
            return min_idx

        
        if min_idx == 0:
            return search(0, len(nums) - 1)
        if target<nums[0]:
            print("h")
            return search(min_idx, len(nums)-1)
        else:
            print("g")
            return search(0, min_idx-1)
        
        