from math import prod
class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        if(prod(nums) > 0):
            return prod(nums)
        
        product_list = []
        i = 0
        while(i < len(nums)):
            j = i
            while(j < len(nums)):
                product_list.append(prod(nums[i : j + 1]))
                j += 1
            i += 1
        
        return max(product_list)



nums = [2,3,-2,4]
obj = Solution()
out = obj.maxProduct(nums)
print(out)

# print(prod(nums))