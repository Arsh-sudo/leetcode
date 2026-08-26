class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # We have exactly k ones.
            if ones == k:
                # Remove unnecessary leading zeros.
                while left <= right and s[left] == '0':
                    left += 1

                candidate = s[left:right + 1]

                if (not best or
                    len(candidate) < len(best) or
                    (len(candidate) == len(best) and candidate < best)):
                    best = candidate

                # Move past the first 1 so we can find
                # the next group of k ones.
                left += 1
                ones -= 1

                # Skip zeros after the removed 1.
                while left <= right and s[left] == '0':
                    left += 1

        return best