class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        
        total = 0

        i = 0
        while(i < len(nums)):

            bin_str = bin(i)[2:]

            if(bin_str.count('1') == k):
                total += nums[i]

            i += 1

        return total