class Solution:
    def countKDifference(self, nums: list, k: int) -> int:
        
        count = 0
        i = 0
        while (i < len(nums) - 1):

            j = i + 1
            while (j < len(nums)):

                if (abs(nums[i] - nums[j]) == k):
                    count += 1

                j += 1
            i += 1

        return count

nums = [3,2,1,5,4]
k = 2
obj = Solution()
solution = obj.countKDifference(nums, k)
print(solution)