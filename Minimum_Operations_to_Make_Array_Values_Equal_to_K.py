class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        
        for num in nums:
            if(num < k):
                return -1
        

        nums = list(set(nums))
        ans = 0
        for num in nums:
            if(num > k):
                ans += 1
        return ans
