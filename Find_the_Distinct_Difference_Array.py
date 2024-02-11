from collections import Counter
class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        

        outList = list()
        i = 0
        while (i < len(nums)):
            
            outList.append(len(dict(Counter(nums[0 : i + 1])).keys()) - len(dict(Counter(nums[i + 1 :])).keys()))
            i += 1

        return outList

nums = [1,2,3,4,5]
obj = Solution()
solution = obj.distinctDifferenceArray(nums)
print(solution)