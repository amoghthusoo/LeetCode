from collections import Counter
class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        
        nums = list(dict(Counter(nums)).keys())
        counter = 0

        i = 1
        while (i < len(nums) - 1):

            if (    ((nums[i] > nums[i - 1]) and (nums[i] > nums[i + 1])) or 
                    ((nums[i] < nums[i - 1]) and (nums[i] < nums[i + 1]))
                ):
                counter += 1

            i += 1

        return counter

nums = [6,6,5,5,4,1]
obj = Solution()
solution = obj.countHillValley(nums)
print(solution)