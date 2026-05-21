class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:

        prefixes = set()

        # store all prefixes from arr1
        for num in arr1:

            s = str(num)

            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        longest = 0

        # check prefixes in arr2
        for num in arr2:

            s = str(num)

            for i in range(1, len(s) + 1):

                if s[:i] in prefixes:
                    longest = max(longest, i)

        return longest