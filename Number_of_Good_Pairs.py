class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        
        count = 0

        i = 0
        while (i < len(nums)):

            j = i + 1
            while (j < len(nums)):

                if (nums[i] == nums[j]):
                    count += 1
                
                j += 1

            i += 1

        return count 



nums = [1,2,3]
obj = Solution()
solution = obj. numIdenticalPairs(nums)
print(solution)