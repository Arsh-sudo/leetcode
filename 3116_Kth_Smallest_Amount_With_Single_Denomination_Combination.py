from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):

        m = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << m):
                cur_lcm = 1
                bits = 0

                for i in range(m):
                    if mask & (1 << i):
                        cur_lcm = lcm(cur_lcm, coins[i])

                        if cur_lcm > x:
                            break

                        bits += 1

                else:
                    ways = x // cur_lcm

                    if bits % 2 == 1:
                        total += ways
                    else:
                        total -= ways

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left