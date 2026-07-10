class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        # 1. Compress the graph to only unique values present in nums
        U = sorted(list(set(nums)))
        m = len(U)
        
        # Map each unique value to its new compressed index
        val_to_idx = {val: i for i, val in enumerate(U)}
        
        NUM_BITS = 18
        lift_right = [[0] * m for _ in range(NUM_BITS)]
        lift_left = [[0] * m for _ in range(NUM_BITS)]
        
        # 2. Optimized base cases using O(M) Two Pointers
        right_ptr = 0
        for i in range(m):
            # Move the right pointer as far right as maxDiff allows
            while right_ptr + 1 < m and U[right_ptr + 1] <= U[i] + maxDiff:
                right_ptr += 1
            lift_right[0][i] = right_ptr
            
        left_ptr = 0
        for i in range(m):
            # Move the left pointer as far left as maxDiff allows
            while U[left_ptr] < U[i] - maxDiff:
                left_ptr += 1
            lift_left[0][i] = left_ptr
            
        # 3. Build the Binary Lifting Tables
        for j in range(1, NUM_BITS):
            for i in range(m):
                lift_right[j][i] = lift_right[j-1][lift_right[j-1][i]]
                lift_left[j][i] = lift_left[j-1][lift_left[j-1][i]]
                
        # 4. Answer Queries in O(1) loop
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            x_val, y_val = nums[u], nums[v]
            if x_val == y_val:
                ans.append(1)
                continue
                
            curr_idx = val_to_idx[x_val]
            target_idx = val_to_idx[y_val]
            
            if curr_idx < target_idx:
                steps = 0
                for j in range(NUM_BITS - 1, -1, -1):
                    # Lift as far as possible without reaching or exceeding target
                    if lift_right[j][curr_idx] < target_idx:
                        curr_idx = lift_right[j][curr_idx]
                        steps += (1 << j)
                        
                # Take one final step
                curr_idx = lift_right[0][curr_idx]
                steps += 1
                
                ans.append(steps if curr_idx >= target_idx else -1)
            else:
                steps = 0
                for j in range(NUM_BITS - 1, -1, -1):
                    # Lift as far as possible without reaching or dropping below target
                    if lift_left[j][curr_idx] > target_idx:
                        curr_idx = lift_left[j][curr_idx]
                        steps += (1 << j)
                        
                # Take one final step
                curr_idx = lift_left[0][curr_idx]
                steps += 1
                
                ans.append(steps if curr_idx <= target_idx else -1)
                
        return ans