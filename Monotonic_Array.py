class Solution:
    def isMonotonic(self, nums: list) -> bool:
        
        incTemp = [element for element in nums]
        incTemp.sort()
        decTemp = [element for element in nums]
        decTemp.sort()
        decTemp.reverse()

        if (nums == incTemp):
            return True
        elif (nums == decTemp):
            return True
        else:
            return False
        


nums = [1,3,2]
obj = Solution()
solution = obj.isMonotonic(nums)
print(solution)