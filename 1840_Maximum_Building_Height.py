class Solution:
    def maxBuilding(self, n, restrictions):
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])

        restrictions.sort()

        m = len(restrictions)

        # forward pass
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + dist
            )

        # backward pass
        for i in range(m - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + dist
            )

        ans = 0

        for i in range(m - 1):
            x1, h1 = restrictions[i]
            x2, h2 = restrictions[i + 1]

            dist = x2 - x1

            ans = max(
                ans,
                (h1 + h2 + dist) // 2
            )

        return ans