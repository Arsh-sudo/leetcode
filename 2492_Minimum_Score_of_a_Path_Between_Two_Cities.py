from collections import deque

class Solution(object):
    def minScore(self, n, roads):
        graph = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        ans = float('inf')

        while q:
            u = q.popleft()

            for v, w in graph[u]:
                ans = min(ans, w)

                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        return ans