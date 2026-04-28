class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        prefix_prod = []
        prod = 1

        for i, e in enumerate(nums):
            prod *= e
            prefix_prod.append(prod) 

        suffix_prod = []

        i = len(nums) - 1
        prod = 1
        while(i >= 0):

            prod *= nums[i]
            suffix_prod.append(prod)

            i -= 1

        suffix_prod.reverse()

        ans = []
        ans.append(suffix_prod[1])

        i = 1
        while(i < len(nums) - 1):
            
            ans.append(prefix_prod[i - 1] * suffix_prod[i + 1])
            i += 1

        ans.append(prefix_prod[-2])

        return ans


nums = [-1,1,0,-3,3]
obj = Solution()
result = obj.productExceptSelf(nums)
print(result)