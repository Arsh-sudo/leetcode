class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)
        ans = 0
        start = 0

        # Try every possible center.
        for center in range(n):
            # Odd-length palindromes
            l = center
            r = center

            while l >= start and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    ans += 1
                    start = r + 1
                    break

                l -= 1
                r += 1

            if start > center:
                continue

            # Even-length palindromes
            l = center
            r = center + 1

            while l >= start and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    ans += 1
                    start = r + 1
                    break

                l -= 1
                r += 1

        return ans