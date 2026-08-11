class Solution:
    def missingInteger(self, nums: list[int]) -> int:

        # Find sum of longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find smallest missing number >= total
        while total in nums:
            total += 1

        return total