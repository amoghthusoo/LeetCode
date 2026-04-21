class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums_set = set(nums)

        ans = 0
        for num in nums_set:
            if(num-1 not in nums_set):
                i = num
                cnt = 0
                while(i in nums_set):
                    cnt += 1
                    i += 1
                ans = max(ans, cnt)
                
        return ans
    


nums = [1,2,6,7,8]
obj = Solution()
result = obj.longestConsecutive(nums)
print(result)