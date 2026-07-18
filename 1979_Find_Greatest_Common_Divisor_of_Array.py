from math import gcd

class Solution:
    def findGCD(self, nums):
        return gcd(min(nums), max(nums))