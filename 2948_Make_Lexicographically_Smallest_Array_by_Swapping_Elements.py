class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)

        # (value, original_index)
        pairs = sorted((x, i) for i, x in enumerate(nums))

        ans = [0] * n

        start = 0

        while start < n:
            end = start

            # Find one connected group in sorted value order.
            while (
                end + 1 < n
                and pairs[end + 1][0] - pairs[end][0] <= limit
            ):
                end += 1

            # Original indices in this group
            indices = [pairs[i][1] for i in range(start, end + 1)]
            indices.sort()

            # Values are already sorted because pairs is sorted.
            for j, idx in enumerate(indices):
                ans[idx] = pairs[start + j][0]

            start = end + 1

        return ans