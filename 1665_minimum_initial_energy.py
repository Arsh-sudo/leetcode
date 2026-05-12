class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:

        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:

            # If current energy is less than minimum,
            # add extra energy
            if current < minimum:
                energy += minimum - current
                current = minimum

            # perform task
            current -= actual

        return energy