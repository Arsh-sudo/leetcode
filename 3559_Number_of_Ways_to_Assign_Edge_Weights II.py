from collections import deque

class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7

        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = (n + 1).bit_length()

        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            node = q.popleft()

            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    depth[nxt] = depth[node] + 1
                    parent[0][nxt] = node
                    q.append(nxt)

        for k in range(1, LOG):
            for node in range(1, n + 1):
                parent[k][node] = parent[k - 1][parent[k - 1][node]]

        def lca(u, v):

            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        ans = []

        for u, v in queries:

            w = lca(u, v)

            d = depth[u] + depth[v] - 2 * depth[w]

            if d == 0:
                ans.append(0)
            else:
                ans.append(pow(2, d - 1, MOD))

        return ans