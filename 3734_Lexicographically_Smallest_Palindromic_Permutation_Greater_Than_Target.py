class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # A palindrome can have at most one character with odd frequency
        if sum(v & 1 for v in cnt) > 1:
            return ""

        # Characters used in the left half
        half = [v // 2 for v in cnt]

        # Middle character if n is odd
        mid = None
        if n & 1:
            for i in range(26):
                if cnt[i] & 1:
                    mid = chr(97 + i)
                    break

        def build(left: str) -> str:
            return left + (mid if mid is not None else "") + left[::-1]

        m = n // 2
        pref = target[:m]

        def count_of(t: str):
            c = [0] * 26
            for ch in t:
                c[ord(ch) - 97] += 1
            return c

        # Case 1: left half equals target prefix.
        # If this palindrome is already greater than target, it is optimal.
        if count_of(pref) == half:
            cand = build(pref)
            if cand > target:
                return cand

        # Case 2: find the smallest valid left half > target prefix.
        def next_greater(left_target: str):
            x = left_target

            # Try the rightmost possible position where we can put a larger char
            for i in range(len(x) - 1, -1, -1):
                rem = half[:]
                ok = True

                # Match x[:i] exactly
                for j in range(i):
                    idx = ord(x[j]) - 97
                    if rem[idx] == 0:
                        ok = False
                        break
                    rem[idx] -= 1

                if not ok:
                    continue

                # Put the smallest possible char > x[i]
                start = ord(x[i]) - 97 + 1
                chosen = -1
                for ch in range(start, 26):
                    if rem[ch] > 0:
                        chosen = ch
                        rem[ch] -= 1
                        break

                if chosen == -1:
                    continue

                # Fill the rest with smallest remaining characters
                res = [x[:i], chr(97 + chosen)]
                for ch in range(26):
                    if rem[ch]:
                        res.append(chr(97 + ch) * rem[ch])

                return "".join(res)

            return None

        left = next_greater(pref)
        if left is None:
            return ""

        return build(left)