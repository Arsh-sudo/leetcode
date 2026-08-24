class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        total = sum(stones)
        dp = total

        for i in range(n - 2, 0, -1):
            total -= stones[i + 1]
            dp = max(dp, total - dp)

        return dp