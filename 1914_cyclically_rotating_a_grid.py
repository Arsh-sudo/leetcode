class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:

        m = len(grid)
        n = len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):

            elements = []

            top = layer
            left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            # top row
            for j in range(left, right + 1):
                elements.append(grid[top][j])

            # right column
            for i in range(top + 1, bottom):
                elements.append(grid[i][right])

            # bottom row
            for j in range(right, left - 1, -1):
                elements.append(grid[bottom][j])

            # left column
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])

            # rotate
            rot = k % len(elements)
            elements = elements[rot:] + elements[:rot]

            idx = 0

            # place top row
            for j in range(left, right + 1):
                grid[top][j] = elements[idx]
                idx += 1

            # place right column
            for i in range(top + 1, bottom):
                grid[i][right] = elements[idx]
                idx += 1

            # place bottom row
            for j in range(right, left - 1, -1):
                grid[bottom][j] = elements[idx]
                idx += 1

            # place left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = elements[idx]
                idx += 1

        return grid