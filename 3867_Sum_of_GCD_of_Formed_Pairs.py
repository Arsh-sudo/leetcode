from math import gcd

class Solution:
    def gcdSum(self, nums):
        arr = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            arr.append(gcd(x, mx))

        arr.sort()

        ans = 0
        i, j = 0, len(arr) - 1

        while i < j:
            ans += gcd(arr[i], arr[j])
            i += 1
            j -= 1

        return ans