class Solution:
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i]:
                continue

            stack = [i]
            visited[i] = True
            nodes = []
            edge_count = 0

            while stack:
                u = stack.pop()
                nodes.append(u)
                edge_count += len(graph[u])

                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)

            size = len(nodes)
            edge_count //= 2

            if edge_count == size * (size - 1) // 2:
                ans += 1

        return ans