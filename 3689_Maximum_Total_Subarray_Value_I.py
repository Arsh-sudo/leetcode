class Solution:
    def maxTotalValue(self, nums, k):
        return k * (max(nums) - min(nums))