class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # 1. Remove both from the front
        option1 = right + 1

        # 2. Remove both from the back
        option2 = n - left

        # 3. Remove one from front and the other from back
        option3 = left + 1 + n - right

        return min(option1, option2, option3)