class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):

            # Add nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # If nums[right] occurs more than k times,
            # shrink the window from the left
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            # Current window is valid
            ans = max(ans, right - left + 1)

        return ans