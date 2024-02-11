class Solution:
    def targetIndices(self, nums: list, target: int) -> list:
        
        ansList = []

        nums.sort()

        i = 0
        while (i < len(nums)):

            if (nums[i] == target):
                ansList.append(i)

            i +=1 

        return ansList

nums = [1,2,5,2,3]
target = 5
obj = Solution()
solution = obj.targetIndices(nums, target)
print(solution)