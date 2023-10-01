class Solution:
    def arithmeticTriplets(self, nums: list, diff: int) -> int:
        
        count = 0

        i = 0
        while (i < len(nums) - 2):

            j = i + 1
            while (j < len(nums) - 1):

                k = j + 1
                while (k < len(nums)):

                    if (nums[j] - nums[i] == diff and nums[k] - nums[j] == diff):
                        count += 1

                    k += 1                
                j += 1
            i += 1
            
        return count

nums = [4,5,6,7,8,9]
diff = 2
obj = Solution()
solution = obj.arithmeticTriplets(nums, diff)
print(solution)


