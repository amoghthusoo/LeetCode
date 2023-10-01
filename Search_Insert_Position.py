class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        
        try:
            return nums.index(target)
        except:
            nums.append(target)
            nums.sort()
            return nums.index(target)



nums = [1,3,5,6]
target =  7
obj = Solution()
solution = obj.searchInsert(nums, target)
print(solution)
