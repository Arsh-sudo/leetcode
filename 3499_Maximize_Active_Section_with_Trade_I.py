class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
        
        # Collect the lengths of all contiguous blocks of '0's
        zero_blocks = []
        current_zeros = 0
        
        for char in s:
            if char == '0':
                current_zeros += 1
            else:
                if current_zeros > 0:
                    zero_blocks.append(current_zeros)
                    current_zeros = 0
                    
        # Catch the last block of zeros if the string ends with '0'
        if current_zeros > 0:
            zero_blocks.append(current_zeros)
            
        # If there are less than 2 blocks of '0's, we can't perform a valid merge
        if len(zero_blocks) < 2:
            return total_ones
            
        # Find the maximum gain by merging two adjacent blocks of '0's
        max_gain = 0
        for i in range(len(zero_blocks) - 1):
            max_gain = max(max_gain, zero_blocks[i] + zero_blocks[i+1])
            
        return total_ones + max_gain