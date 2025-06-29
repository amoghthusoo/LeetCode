from math import pow
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:

        ans = 0        
        nums.sort()
        mod_val = int(10 ** 9 + 7)

        i = 0
        j = len(nums) - 1

        while(i <= j):

            if(nums[i] + nums[j] <= target):
                ans = (ans + pow(2, j - i, mod_val)) % mod_val
                i += 1
            else:
                j -= 1
        
        return ans

nums = [2,3,3,4,6,7]
target = 12
obj = Solution()
result = obj.numSubseq(nums, target)
print(result)        