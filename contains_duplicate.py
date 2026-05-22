class Solution:
    def containsDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        else:
            return True