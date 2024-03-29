from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
    
        occDict = dict(Counter(nums))
        
        maxFreq = 0
        for key, value in occDict.items():
            
            if(value > maxFreq):
                maxFreq = value

        count = 0
        for key, value in occDict.items():
            
            if(value == maxFreq):
                count += maxFreq

        return count
    
nums = [1,2,3,4,5]
obj = Solution()
out = obj.maxFrequencyElements(nums)
print(out)