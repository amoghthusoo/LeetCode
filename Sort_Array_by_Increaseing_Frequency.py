from collections import Counter
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        
        occDict = dict(Counter(nums))
        
        i = 0
        while(i < len(nums) - 1):

            j = 0
            while(j < len(nums) - 1 - i):
                
                if(occDict[nums[j]] > occDict[nums[j + 1]]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

                if(occDict[nums[j]] == occDict[nums[j + 1]]):

                    if(nums[j] < nums[j + 1]):
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]                
                
                j += 1
            i += 1

        return nums


nums = [-1,1,-6,4,5,-6,1,4,1]
obj = Solution()
out = obj.frequencySort(nums)
print(out)