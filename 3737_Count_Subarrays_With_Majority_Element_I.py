class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        ans = 0

        for i in range(n):
            s = 0

            for j in range(i, n):
                if nums[j] == target:
                    s += 1
                else:
                    s -= 1

                if s > 0:
                    ans += 1

        return ans