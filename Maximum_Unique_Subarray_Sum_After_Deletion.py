class Solution:
    def maxSum(self, nums: list[int]) -> int:
        
        nums = set(nums)

        max_element = max(nums)
        if(max_element < 0):
            return max_element
        
        ans = 0
        it = iter(nums)
        for num in it:
            if(num >= 0):
                ans += num
        
        return ans


nums = [1,2,3,4,5]
obj = Solution()
result = obj.maxSum(nums)
print(result)