class Solution:
    def maximumProduct(self, nums: list) -> int:
        
        nums.sort()

        posAns1 = nums[-1] * nums[-2] * nums[-3]
        posAns2 = nums[-1] * nums[0] * nums[1]

        if (posAns1 >= posAns2):
            return posAns1
        else:
            return posAns2

nums = [-1,-2,-3]
obj = Solution()
solution = obj.maximumProduct(nums)
print(solution)