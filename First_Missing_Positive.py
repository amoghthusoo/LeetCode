class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        trackDict = {}

        for num in nums:
            if(num > 0 and num not in trackDict):
                trackDict[num] = None
        
        for i in range(1, 2 ** 31):
            if(i not in trackDict):
                return i
            


nums = [7,8,9,11,12]
obj = Solution()
out = obj.firstMissingPositive(nums)
print(out)