def foursum(nums, target):
    def kSum(nums, target, k):
        if len(nums)==0 or nums[0] * k > target or target > nums[-1] * k:
            return []
        
        # no k==1
        if k==2:
            return twoSum(nums, target)
        
        res = []
        for i in range(len(nums)):
            if i==0 or nums[i-1] != nums[i]:  # we want different numbers
                for _,candidates in enumerate(kSum(nums[i+1:], target-nums[i], k-1)):
                    res.append([nums[i]]+candidates)
        return res
    
    def twoSum(nums, target):
        res = []
        s = set()
        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
            s.add(nums[i])
        return res
    
    nums.sort()
    return kSum(nums, target, 4)


print(foursum([1,0-1,0-2,2], 0))