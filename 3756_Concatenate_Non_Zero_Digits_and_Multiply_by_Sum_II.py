class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10 ** 9 + 7

        n = len(s)

        cnt = [0] * (n + 1)
        digitSum = [0] * (n + 1)

        digits = []

        for i, ch in enumerate(s):
            d = ord(ch) - 48
            digitSum[i + 1] = digitSum[i] + d
            cnt[i + 1] = cnt[i]
            if d:
                cnt[i + 1] += 1
                digits.append(d)

        m = len(digits)

        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        H = [0] * (m + 1)
        for i in range(m):
            H[i + 1] = (H[i] * 10 + digits[i]) % MOD

        ans = []

        for l, r in queries:
            L = cnt[l]
            R = cnt[r + 1]

            x = (H[R] - H[L] * pow10[R - L]) % MOD
            sm = digitSum[r + 1] - digitSum[l]

            ans.append((x * sm) % MOD)

        return ans