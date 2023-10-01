class Solution:
    def countPairs(self, nums: list, target: int) -> int:
        
        count = 0
        i = 0
        while (i < len(nums)):

            j = i + 1
            while (j < len(nums)):

                if (nums[i] + nums[j] < target):
                    count += 1

                j += 1

            i += 1

        return count 

nums = [-6,2,5,-2,-7,-1,3]
target = -2
obj = Solution()
solution = obj.countPairs(nums, target)
print(solution)