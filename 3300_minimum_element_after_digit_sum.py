class Solution:
    def minElement(self, nums: list[int]) -> int:

        def digit_sum(num):

            total = 0

            while num:

                total += num % 10
                num //= 10

            return total

        return min(digit_sum(num) for num in nums)