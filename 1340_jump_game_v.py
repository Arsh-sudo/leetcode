from functools import lru_cache

class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:

        n = len(arr)

        @lru_cache(None)
        def dfs(i):

            best = 1

            # go right
            for j in range(i + 1, min(n, i + d + 1)):

                # blocked
                if arr[j] >= arr[i]:
                    break

                best = max(best, 1 + dfs(j))

            # go left
            for j in range(i - 1, max(-1, i - d - 1), -1):

                # blocked
                if arr[j] >= arr[i]:
                    break

                best = max(best, 1 + dfs(j))

            return best

        return max(dfs(i) for i in range(n))