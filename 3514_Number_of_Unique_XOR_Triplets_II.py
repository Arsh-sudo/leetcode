import itertools

class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        # Step 1: Keep only unique numbers to minimize operations
        unique_nums = set(nums)
        
        # Step 2: Generate all unique XOR values of any two elements (pairs)
        # combinations_with_replacement allows elements to be XORed with themselves
        pairs_xor = {
            a ^ b 
            for a, b in itertools.combinations_with_replacement(unique_nums, 2)
        }
        
        # Step 3: Generate all unique XOR values of any three elements (triplets)
        # by XORing the paired results with every unique element
        triplets_xor = {
            p ^ c 
            for p in pairs_xor 
            for c in unique_nums
        }
        
        # Return the total count of unique triplet values
        return len(triplets_xor)