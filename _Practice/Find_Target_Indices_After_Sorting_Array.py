class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        ansList = []

        nums.sort()

        i = 0
        while (i < len(nums)):

            if (nums[i] == target):
                ansList.append(i)

            i +=1 

        return ansList