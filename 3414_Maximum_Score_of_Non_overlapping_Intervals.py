class Solution:
    def maximumWeight(self, intervals):
        from bisect import bisect_right

        intervals = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        n = len(intervals)

        memo = {}

        def dp(i, k):
            if i == n or k == 0:
                return 0, ()

            if (i, k) in memo:
                return memo[(i, k)]

            # Option 1: skip current interval
            skip_score, skip_ids = dp(i + 1, k)

            # Option 2: take current interval
            l, r, w, original_index = intervals[i]

            # First interval with start > r
            j = bisect_right(intervals, (r, float('inf')))

            next_score, next_ids = dp(j, k - 1)

            take_score = w + next_score
            take_ids = tuple(sorted((original_index,) + next_ids))

            if take_score > skip_score:
                result = (take_score, take_ids)

            elif take_score < skip_score:
                result = (skip_score, skip_ids)

            else:
                if take_ids < skip_ids:
                    result = (take_score, take_ids)
                else:
                    result = (skip_score, skip_ids)

            memo[(i, k)] = result
            return result

        return list(dp(0, 4)[1])