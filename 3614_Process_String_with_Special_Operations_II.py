class Solution:
    def processStr(self, s, k):
        LIMIT = 10**15

        n = len(s)
        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = min(LIMIT, cur + 1)

            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)

            elif ch == '#':
                lengths[i + 1] = min(LIMIT, cur * 2)

            else:  # '%'
                lengths[i + 1] = cur

        if k >= lengths[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            if 'a' <= ch <= 'z':
                if k == lengths[i]:
                    return ch

            elif ch == '#':
                prev_len = lengths[i]
                if prev_len:
                    k %= prev_len

            elif ch == '%':
                L = lengths[i]
                k = L - 1 - k

            else:  # '*'
                pass

        return '.'