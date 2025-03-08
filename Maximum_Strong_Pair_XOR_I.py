class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        out = -1

        i = 0
        while(i < len(nums)):

            j = 0
            while(j < len(nums)):

                if(abs(nums[i] - nums[j]) <= min(nums[i], nums[j])):

                    xor = nums[i] ^ nums[j]
                    if(xor > out):
                        out = xor

                j += 1
            i += 1

        return out