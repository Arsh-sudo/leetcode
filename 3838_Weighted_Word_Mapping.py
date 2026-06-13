class Solution:
    def mapWordWeights(self, words, weights):
        ans = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            rem = total % 26

            ans.append(chr(ord('z') - rem))

        return "".join(ans)