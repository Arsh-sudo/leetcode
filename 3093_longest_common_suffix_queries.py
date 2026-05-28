class TrieNode:
    def __init__(self):
        self.children = {}
        self.best = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):

        root = TrieNode()

        # function to choose better index
        def better(i, j):

            if j == -1:
                return i

            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return i

            if len(wordsContainer[i]) > len(wordsContainer[j]):
                return j

            return min(i, j)

        # build trie
        for i, word in enumerate(wordsContainer):

            rev = word[::-1]

            node = root
            node.best = better(i, node.best)

            for ch in rev:

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                node.best = better(i, node.best)

        ans = []

        # process queries
        for word in wordsQuery:

            rev = word[::-1]

            node = root

            for ch in rev:

                if ch not in node.children:
                    break

                node = node.children[ch]

            ans.append(node.best)

        return ans