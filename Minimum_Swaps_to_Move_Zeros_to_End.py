class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        
        zero_count = nums.count(0)

        ans = 0
        i = len(nums) - 1
        for _ in range(zero_count):
            if(nums[i] != 0):
                ans += 1
            i -= 1
        
        return ans
