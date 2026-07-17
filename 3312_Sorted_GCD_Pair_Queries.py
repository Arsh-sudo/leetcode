from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        MAX = max(nums)

        freq = [0] * (MAX + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (MAX + 1)
        for d in range(1, MAX + 1):
            s = 0
            for m in range(d, MAX + 1, d):
                s += freq[m]
            cnt[d] = s * (s - 1) // 2

        exact = [0] * (MAX + 1)
        for d in range(MAX, 0, -1):
            exact[d] = cnt[d]
            for m in range(d * 2, MAX + 1, d):
                exact[d] -= exact[m]

        vals = []
        pref = []

        cur = 0
        for g in range(1, MAX + 1):
            if exact[g]:
                cur += exact[g]
                vals.append(g)
                pref.append(cur)

        ans = []
        for q in queries:
            ans.append(vals[bisect_right(pref, q)])

        return ans