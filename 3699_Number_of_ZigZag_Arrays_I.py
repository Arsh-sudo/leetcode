class Solution:
    def zigZagArrays(self, n, l, r):
        MOD = 1000000007

        m = r - l + 1

        if n == 1:
            return m

        up = [0] * (m + 1)
        down = [0] * (m + 1)

        # length = 2
        for v in range(1, m + 1):
            up[v] = v - 1
            down[v] = m - v

        for _ in range(3, n + 1):

            pref_down = [0] * (m + 1)
            for v in range(1, m + 1):
                pref_down[v] = (pref_down[v - 1] + down[v]) % MOD

            pref_up = [0] * (m + 1)
            for v in range(1, m + 1):
                pref_up[v] = (pref_up[v - 1] + up[v]) % MOD

            total_up = pref_up[m]

            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            for v in range(1, m + 1):
                new_up[v] = pref_down[v - 1]
                new_down[v] = (total_up - pref_up[v]) % MOD

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD