class Solution:

    def check_strictly_increasing(self, arr):

        for i in range(len(arr) - 1):

            if(arr[i] >= arr[i + 1]):
                return False
        
        return True

    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        

        for i in range(len(nums) - 2 * k + 1):

            if(self.check_strictly_increasing(nums[i : i + k]) and self.check_strictly_increasing(nums[i + k : i + 2 * k])):
                return True
        
        return False


nums = [-15,19]
k = 1
obj = Solution()
result = obj.hasIncreasingSubarrays(nums, k)
print(result)
