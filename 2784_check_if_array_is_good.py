class Solution:
    def isGood(self, nums: list[int]) -> bool:

        nums.sort()

        n = nums[-1]

        expected = list(range(1, n + 1)) + [n]

        return nums == expected