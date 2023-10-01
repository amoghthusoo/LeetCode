from collections import Counter
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        
        occDict = Counter(nums)

        for occurence in occDict.values():
            if(occurence % 2 != 0):
                return False
            
        else:
            return True

nums = [1,2,3,4]
obj = Solution()
solution = obj.divideArray(nums)
print(solution)