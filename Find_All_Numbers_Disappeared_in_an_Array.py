class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        
        ansArray = []

        for i in range(1, len(nums) + 1):

            if (i not in nums):
                ansArray.append(i)
        
        return ansArray

nums = []
obj = Solution()
solution = obj.findDisappearedNumbers(nums)
print(solution)
