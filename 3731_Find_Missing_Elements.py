class Solution:
    def findMissingElements(self, nums):
        s = set(nums)
        mn, mx = min(nums), max(nums)

        ans = []
        for x in range(mn, mx + 1):
            if x not in s:
                ans.append(x)

        return ans