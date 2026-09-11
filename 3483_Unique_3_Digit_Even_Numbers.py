from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        ans = 0

        # hundreds digit: cannot be 0
        for h in range(1, 10):
            if freq[h] == 0:
                continue
            freq[h] -= 1

            # tens digit
            for t in range(10):
                if freq[t] == 0:
                    continue
                freq[t] -= 1

                # units digit must be even
                for u in (0, 2, 4, 6, 8):
                    if freq[u] > 0:
                        ans += 1

                freq[t] += 1

            freq[h] += 1

        return ans