class Solution:
    def findMin(self, nums: list[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            # minimum is in right half
            if nums[mid] > nums[right]:
                left = mid + 1

            # minimum is in left half including mid
            elif nums[mid] < nums[right]:
                right = mid

            # duplicates -> shrink safely
            else:
                right -= 1

        return nums[left]