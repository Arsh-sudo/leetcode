from collections import deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:

        n = len(arr)

        queue = deque([start])
        visited = set([start])

        while queue:

            i = queue.popleft()

            if arr[i] == 0:
                return True

            for nxt in (i + arr[i], i - arr[i]):

                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return False