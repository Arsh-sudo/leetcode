from collections import Counter
from math import factorial
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = {}
        mid = ""
        m = 0

        for c in sorted(freq):
            half[c] = freq[c] // 2
            m += half[c]
            if freq[c] & 1:
                mid = c

        # factorials
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        def ways(cnt):
            rem = sum(cnt.values())
            ans = 1
            for c in cnt.values():
                if c:
                    ans *= comb(rem, c)
                    if ans >= k:
                        return k
                    rem -= c
            return ans

        if ways(half) < k:
            return ""

        left = []

        for _ in range(m):
            for c in sorted(half):
                if half[c] == 0:
                    continue

                half[c] -= 1
                w = ways(half)

                if w >= k:
                    left.append(c)
                    break

                k -= w
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]