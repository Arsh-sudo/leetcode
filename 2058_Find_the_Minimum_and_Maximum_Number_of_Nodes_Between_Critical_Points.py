class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        # Need at least 3 nodes
        if curr is None or curr.next is None:
            return [-1, -1]

        first = -1
        prev_critical = -1
        min_dist = float('inf')

        pos = 1

        while curr.next:
            next_node = curr.next

            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - prev_critical)

                prev_critical = pos

            prev = curr
            curr = next_node
            pos += 1

        # Fewer than 2 critical points
        if first == -1 or first == prev_critical:
            return [-1, -1]

        max_dist = prev_critical - first

        return [min_dist, max_dist]