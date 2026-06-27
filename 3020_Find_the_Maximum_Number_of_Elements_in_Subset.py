from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = 1

        # Handle x = 1 separately
        if 1 in cnt:
            if cnt[1] % 2 == 0:
                ans = max(ans, cnt[1] - 1)
            else:
                ans = max(ans, cnt[1])

        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while True:
                if cur not in cnt:
                    break

                if cnt[cur] == 1:
                    length += 1
                    ans = max(ans, length)
                    break

                nxt = cur * cur

                # Can't extend further, current becomes center
                if nxt not in cnt:
                    length += 1
                    ans = max(ans, length)
                    break

                # Use two copies as outer layer
                length += 2

                # Prevent unnecessary huge squaring
                if cur > 31623:
                    break

                cur = nxt

        return ans