from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Number each litter cell
        litter_id = {}
        start = None
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        # All litter already collected
        if litter_count == 0:
            return 0

        target = (1 << litter_count) - 1

        # State = (row, col, remaining_energy, mask)
        q = deque()
        q.append((start[0], start[1], energy, 0))

        visited = set()
        visited.add((start[0], start[1], energy, 0))

        moves = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Need energy to make the move
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if (nr, nc) in litter_id:
                        bit = litter_id[(nr, nc)]
                        nmask |= (1 << bit)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    # All litter collected
                    if nmask == target:
                        return moves + 1

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1