from bisect import bisect_right


class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration,
    ):

        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            s = [x for x, _ in rides]
            d = [y for _, y in rides]

            n = len(rides)

            pref = [0] * n
            pref[0] = d[0]

            for i in range(1, n):
                pref[i] = min(pref[i - 1], d[i])

            suff = [0] * n
            suff[-1] = s[-1] + d[-1]

            for i in range(n - 2, -1, -1):
                suff[i] = min(suff[i + 1], s[i] + d[i])

            return s, pref, suff

        ws, w_pref, w_suff = build(waterStartTime, waterDuration)
        ls, l_pref, l_suff = build(landStartTime, landDuration)

        ans = float("inf")

        # Land -> Water
        for start, dur in zip(landStartTime, landDuration):

            t = start + dur

            idx = bisect_right(ws, t) - 1

            if idx >= 0:
                ans = min(ans, t + w_pref[idx])

            if idx + 1 < len(ws):
                ans = min(ans, w_suff[idx + 1])

        # Water -> Land
        for start, dur in zip(waterStartTime, waterDuration):

            t = start + dur

            idx = bisect_right(ls, t) - 1

            if idx >= 0:
                ans = min(ans, t + l_pref[idx])

            if idx + 1 < len(ls):
                ans = min(ans, l_suff[idx + 1])

        return ans