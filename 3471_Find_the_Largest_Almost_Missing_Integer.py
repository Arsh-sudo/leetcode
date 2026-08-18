class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        ans = -1

        for x in set(nums):
            subarrays = 0

            for i in range(len(nums) - k + 1):
                if x in nums[i:i+k]:
                    subarrays += 1

            if subarrays == 1:
                ans = max(ans, x)

        return ans