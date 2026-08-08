from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # positions of each character in word1
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(word1):
            pos[ord(ch) - 97].append(i)
        
        # prefIdx[t] = earliest index chosen for word2[t] in an exact match
        # of the prefix word2[:t+1].
        prefIdx = [-1] * m
        cur = -1
        exact_full = True
        
        for t, ch in enumerate(word2):
            lst = pos[ord(ch) - 97]
            k = bisect_right(lst, cur)
            if k == len(lst):
                exact_full = False
                break
            prefIdx[t] = lst[k]
            cur = lst[k]
        
        # latestStart[t] = maximum possible first index of an exact match
        # of the suffix word2[t:].
        latestStart = [-1] * (m + 1)
        latestStart[m] = n
        cur = n
        
        for t in range(m - 1, -1, -1):
            lst = pos[ord(word2[t]) - 97]
            k = bisect_left(lst, cur) - 1
            if k < 0:
                break
            cur = lst[k]
            latestStart[t] = cur
        
        # Segment tree storing bitmask of characters in each segment.
        size = 1
        while size < n:
            size <<= 1
        
        tree = [0] * (2 * size)
        for i, ch in enumerate(word1):
            tree[size + i] = 1 << (ord(ch) - 97)
        
        for i in range(size - 1, 0, -1):
            tree[i] = tree[i << 1] | tree[i << 1 | 1]
        
        full_mask = (1 << 26) - 1
        
        def first_not(l: int, r: int, banned_char: str) -> int:
            """Smallest index in [l, r] whose character is not banned_char."""
            allowed = full_mask ^ (1 << (ord(banned_char) - 97))
            stack = [(1, 0, size - 1)]
            
            while stack:
                node, nl, nr = stack.pop()
                if nr < l or r < nl or not (tree[node] & allowed):
                    continue
                if nl == nr:
                    return nl
                
                mid = (nl + nr) >> 1
                stack.append((node << 1 | 1, mid + 1, nr))
                stack.append((node << 1, nl, mid))
            
            return -1
        
        best_p = -1
        best_i = -1
        
        # Try every possible mismatch position p in word2.
        for p in range(m):
            if p > 0 and prefIdx[p - 1] == -1:
                break
            
            q = p + 1
            if latestStart[q] == -1:
                continue
            
            left = 0 if p == 0 else prefIdx[p - 1] + 1
            right = latestStart[q] - 1
            
            if left > right:
                continue
            
            i = first_not(left, right, word2[p])
            if i == -1:
                continue
            
            if best_p == -1:
                best_p = p
                best_i = i
            else:
                # Compare candidate p with current best candidate.
                exact_at_best = prefIdx[best_p]
                if best_i > exact_at_best:
                    best_p = p
                    best_i = i
        
        # Exact match candidate.
        if exact_full:
            if best_p != -1:
                exact_at_best = prefIdx[best_p]
                if best_i < exact_at_best:
                    return self._build_answer(
                        word1, word2, pos, prefIdx, best_p, best_i
                    )
            return prefIdx[:m]
        
        if best_p == -1:
            return []
        
        return self._build_answer(
            word1, word2, pos, prefIdx, best_p, best_i
        )
    
    def _build_answer(
        self,
        word1: str,
        word2: str,
        pos: List[List[int]],
        prefIdx: List[int],
        p: int,
        mismatch_index: int
    ) -> List[int]:
        """Build the lexicographically smallest sequence for mismatch position p."""
        ans = prefIdx[:p]
        ans.append(mismatch_index)
        
        cur = mismatch_index
        for t in range(p + 1, len(word2)):
            lst = pos[ord(word2[t]) - 97]
            k = bisect_right(lst, cur)
            cur = lst[k]
            ans.append(cur)
        
        return ans