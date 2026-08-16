from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]  # cnt[0], cnt[1], cnt[2] = residues modulo 3
        
        for stone in stones:
            cnt[stone % 3] += 1
        
        # If number of stones divisible by 3 is even:
        # Alice wins iff both residue 1 and residue 2 stones exist.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
        
        # If number of stones divisible by 3 is odd:
        # Alice wins iff the counts of residue 1 and residue 2 differ by more than 2.
        return abs(cnt[1] - cnt[2]) > 2