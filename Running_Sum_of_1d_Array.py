class Solution:
    def runningSum(self, nums: list) -> list:
        
        ansList = []
        total = 0

        for element in nums:
            total += element
            ansList.append(total)

        return ansList

nums = [3,1,2,10,1]
obj = Solution()
solution = obj.runningSum(nums)
print(solution)