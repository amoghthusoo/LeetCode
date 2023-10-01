class Solution:
    def countPairs(self, nums: list, k: int) -> int:
        
        count = 0

        i = 0
        while (i < len(nums)):

            j = i + 1
            while (j < len(nums)):

                if (nums[i] == nums[j] and (i * j) % k == 0):
                    count += 1
                

                j += 1

            i += 1

        return count

nums = [1,2,3,4]
k = 1
obj = Solution()
solution = obj.countPairs(nums, k)
print(solution)