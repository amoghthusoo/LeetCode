class Solution:
    def findTheArrayConcVal(self, nums: list) -> int:
        
        concatenation_value = 0

        while (len(nums) != 0):

            if (len(nums) != 1):

                concatenation_value += int(str(nums[0]) + str(nums[-1]))
                del(nums[0])
                del(nums[-1])
            
            else:
                concatenation_value += nums[0]
                del(nums[0])

        
        return concatenation_value

nums = [5,14,13,8,12]
obj = Solution()
solution = obj.findTheArrayConcVal(nums)
print(solution)