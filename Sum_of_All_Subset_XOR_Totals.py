class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        total = 0

        i = 0
        while(i < int(2 ** len(nums))):
            
            bin_str = bin(i)[2:].zfill(len(nums))

            xor_result = 0
            j = 0
            while(j < len(nums)):

                if(bin_str[j] == '1'):
                    xor_result ^= nums[j]
                j += 1            
            
            total += xor_result
            
            i += 1

        return total


nums = [3,4,5,6,7,8]
obj = Solution()
out = obj.subsetXORSum(nums)
print(out)