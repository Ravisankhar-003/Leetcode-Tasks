class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            partner = target - num
            if partner in seen:
                return [seen[partner], i]
            seen[num] = i
