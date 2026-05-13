class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:

        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):

            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            total = a + b

            # default: 2 moves
            diff[2] += 2

            # one move range starts
            diff[low] -= 1

            # zero move at exact sum
            diff[total] -= 1
            diff[total + 1] += 1

            # back to two moves
            diff[high + 1] += 1

        ans = float('inf')
        current = 0

        for s in range(2, 2 * limit + 1):

            current += diff[s]
            ans = min(ans, current)

        return ans