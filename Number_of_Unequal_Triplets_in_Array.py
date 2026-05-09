class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        
        ans = 0
        i = 0
        while(i < len(nums) - 2):
            
            j = i + 1
            while(j < len(nums) - 1):

                k = j + 1
                while(k < len(nums)):

                    if(nums[i] != nums[j] and nums[j] != nums[k] and nums[k] != nums[i]):
                        ans += 1

                    k += 1
                j += 1
            i += 1
        
        return ans
    