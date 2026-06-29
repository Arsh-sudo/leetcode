class Solution(object):
    def numOfStrings(self, patterns, word):
        ans = 0

        for p in patterns:
            if p in word:
                ans += 1

        return ans