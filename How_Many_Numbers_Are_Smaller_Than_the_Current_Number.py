class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        
        ansList = []

        i = 0
        while (i < len(nums)):

            count = 0
            j = 0
            while(j < len(nums)):

                if nums[j] < nums[i]:
                    count += 1

                j += 1
            
            ansList.append(count)
            i += 1

        return ansList

nums = [7,7,7,7]
obj = Solution()
solution = obj.smallerNumbersThanCurrent(nums)
print(solution)