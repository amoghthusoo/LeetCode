class Solution:
    def createTargetArray(self, nums: list, index: list) -> list:
        
        ansList = []

        i = 0
        while (i < len(nums)):
            
            ansList.insert(index[i], nums[i])
            
            i += 1

        return ansList



nums = [1]
index = [0]
obj = Solution()
solution = obj.createTargetArray(nums, index)
print(solution)
