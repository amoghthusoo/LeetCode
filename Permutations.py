from itertools import permutations
class Solution:
    def permute(self, nums: list) -> list:
        
        allComb = list(permutations(nums))
        permuteList = []

        for i in allComb:
            permuteList.append(list(i))        

        return permuteList


nums = [1,2,3]
obj = Solution()
solution = obj.permute(nums)
print(solution)