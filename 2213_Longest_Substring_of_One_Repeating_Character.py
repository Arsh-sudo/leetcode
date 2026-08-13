class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:

        n = len(s)

        # Each node stores:
        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]

            prefix = a[2]
            suffix = b[3]

            best = max(a[4], b[4])

            # If the two parts have the same character
            if a[1] == b[0]:

                # Substring crossing the boundary
                best = max(best, a[3] + b[2])

                # If the ENTIRE left segment has one character,
                # its prefix can extend into the right segment.
                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                # If the ENTIRE right segment has one character,
                # its suffix can extend into the left segment.
                if b[3] == b[5]:
                    suffix = a[3] + b[5]

            return [
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                a[5] + b[5]
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = [
                    s[l],   # left character
                    s[l],   # right character
                    1,      # prefix
                    1,      # suffix
                    1,      # best
                    1       # length
                ]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = [
                    ch, ch, 1, 1, 1, 1
                ]
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build the initial tree
        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):

            # Change s[idx]
            update(1, 0, n - 1, idx, ch)

            # tree[1][4] = longest repeating substring
            ans.append(tree[1][4])

        return ans