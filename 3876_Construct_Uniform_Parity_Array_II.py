class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        has_odd = False
        has_even = False

        for x in nums1:
            if x % 2 == 0:
                has_even = True
            else:
                has_odd = True

        # Already uniform parity
        if not has_odd or not has_even:
            return True

        # Mixed parity: smallest value must be odd
        return min(nums1) % 2 == 1