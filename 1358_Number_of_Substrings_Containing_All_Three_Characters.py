class Solution(object):
    def numberOfSubstrings(self, s):
        cnt = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0
        n = len(s)

        for right in range(n):
            cnt[s[right]] += 1

            while cnt['a'] > 0 and cnt['b'] > 0 and cnt['c'] > 0:
                ans += n - right
                cnt[s[left]] -= 1
                left += 1

        return ans