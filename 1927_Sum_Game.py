class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0   # sum(left digits) - sum(right digits)
        cnt = 0    # count('?' in left) - count('?' in right)

        for i, ch in enumerate(num):
            if ch == '?':
                if i < half:
                    cnt += 1
                else:
                    cnt -= 1
            else:
                val = ord(ch) - ord('0')
                if i < half:
                    diff += val
                else:
                    diff -= val

        # If there is an odd number of '?', Alice makes the last move.
        # She can always choose a digit that makes the sums unequal.
        if cnt % 2 != 0:
            return True

        # Bob can force equality iff the required difference equals
        # the forced contribution from paired '?'s.
        return diff * 2 != -9 * cnt