import heapq

class Solution(object):
    # Changed the function name here to match what LeetCode expects
    def maxTotalValue(self, nums, k):
        n = len(nums)
        max_log = n.bit_length()
        
        # Initialize Sparse Tables
        st_min = [[0] * n for _ in range(max_log)]
        st_max = [[0] * n for _ in range(max_log)]
        
        st_min[0] = list(nums)
        st_max[0] = list(nums)
        
        # Populate the Sparse Tables
        for j in range(1, max_log):
            step = 1 << (j - 1)
            row_min_prev = st_min[j - 1]
            row_max_prev = st_max[j - 1]
            row_min_curr = st_min[j]
            row_max_curr = st_max[j]
            
            for i in range(n - (1 << j) + 1):
                a = row_min_prev[i]
                b = row_min_prev[i + step]
                row_min_curr[i] = a if a < b else b
                
                c = row_max_prev[i]
                d = row_max_prev[i + step]
                row_max_curr[i] = c if c > d else d
                
        # Helper to query Sparse Tables
        def get_val(L, R):
            length = R - L + 1
            j = length.bit_length() - 1
            idx_b = R - (1 << j) + 1
            
            a = st_min[j][L]
            b = st_min[j][idx_b]
            mn = a if a < b else b
            
            c = st_max[j][L]
            d = st_max[j][idx_b]
            mx = c if c > d else d
            
            return mx - mn

        # Initialize Max-Heap
        heap = []
        for L in range(n):
            val = get_val(L, n - 1)
            heap.append((-val, L, n - 1))
            
        heapq.heapify(heap)
        
        # Extract top K subarray values
        total_value = 0
        for _ in range(k):
            neg_val, L, R = heapq.heappop(heap)
            total_value -= neg_val
            
            if R > L:
                next_val = get_val(L, R - 1)
                heapq.heappush(heap, (-next_val, L, R - 1))
                
        return total_value