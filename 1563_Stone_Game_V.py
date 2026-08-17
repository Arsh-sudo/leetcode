from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        pref = [0] * (n + 1)
        for i, v in enumerate(stoneValue):
            pref[i + 1] = pref[i] + v

        # dp[i][j] = max score obtainable from stoneValue[i..j]
        dp = [[0] * n for _ in range(n)]

        # left_best[i][k] = max over m in [i, k] of dp[i][m] + sum(i, m)
        left_best = [[0] * n for _ in range(n)]

        # right_best[j][p] = max over x in [p, j] of dp[x][j] + sum(x, j)
        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = pref[j + 1] - pref[i]

                best = 0

                # Case 1: left sum < right sum, keep left part
                # 2 * (pref[m + 1] - pref[i]) < total
                limit = pref[i] + (total - 1) // 2
                pos = bisect_right(pref, limit)
                m_end = pos - 2
                if m_end >= i:
                    best = max(best, left_best[i][m_end])

                # Case 2: left sum > right sum, keep right part
                # 2 * (pref[p] - pref[i]) > total, where p = m + 1
                lower = pref[i] + total // 2 + 1
                p = bisect_left(pref, lower)
                if p <= j:
                    best = max(best, right_best[j][p])

                # Case 3: left sum == right sum
                if total % 2 == 0:
                    target = pref[i] + total // 2
                    p = bisect_left(pref, target)
                    if p <= j and pref[p] == target:
                        m = p - 1
                        best = max(
                            best,
                            total // 2 + max(dp[i][m], dp[p][j])
                        )

                dp[i][j] = best

                # Update range-max structures for future intervals
                cur = best + total
                left_best[i][j] = max(left_best[i][j - 1], cur)
                right_best[j][i] = max(right_best[j][i + 1], cur)

        return dp[0][n - 1]