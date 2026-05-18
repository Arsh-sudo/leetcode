from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:

        n = len(arr)

        if n == 1:
            return 0

        graph = defaultdict(list)

        # store indices for each value
        for i, val in enumerate(arr):
            graph[val].append(i)

        queue = deque([0])
        visited = set([0])

        steps = 0

        while queue:

            for _ in range(len(queue)):

                i = queue.popleft()

                # reached end
                if i == n - 1:
                    return steps

                neighbors = graph[arr[i]] + [i - 1, i + 1]

                for nxt in neighbors:

                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

                # IMPORTANT optimization
                graph[arr[i]].clear()

            steps += 1

        return -1