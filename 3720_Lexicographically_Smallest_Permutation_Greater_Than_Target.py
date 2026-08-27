class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        n = len(s)

        for i in range(n):
            # Try to keep target[i]
            t = ord(target[i]) - ord('a')

            if cnt[t] > 0:
                cnt[t] -= 1
            else:
                # We cannot keep target[i].
                # Find the smallest character greater than target[i].
                for c in range(t + 1, 26):
                    if cnt[c] > 0:
                        cnt[c] -= 1

                        ans = target[:i] + chr(c + ord('a'))

                        # Fill remaining positions with smallest chars
                        for x in range(26):
                            ans += chr(x + ord('a')) * cnt[x]

                        return ans

                # No character greater than target[i].
                # We must backtrack.
                break

            # If this is the last position and we matched target exactly,
            # the result is not strictly greater, so no answer.
            if i == n - 1:
                break

        # We need to backtrack and make an earlier position larger.
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Try positions from right to left.
        for i in range(n - 1, -1, -1):
            t = ord(target[i]) - ord('a')

            # Restore characters used by target[0:i]
            # by rebuilding counts for this prefix.
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1

            possible = True

            for j in range(i):
                c = ord(target[j]) - ord('a')

                if cnt[c] == 0:
                    possible = False
                    break

                cnt[c] -= 1

            if not possible:
                continue

            # Find smallest available character > target[i]
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    ans = target[:i] + chr(c + ord('a'))

                    for x in range(26):
                        ans += chr(x + ord('a')) * cnt[x]

                    return ans

        return ""