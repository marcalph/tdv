# Given an integer array nums, 
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.
def containsDuplicate(self, nums: List[int]) -> bool:
        viewed = set()
        for i in nums:
            if i in viewed:
                return True
            viewed.add(i)
        return False