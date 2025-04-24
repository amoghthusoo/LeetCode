class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:

        distinct_count = len(set(nums))
        count = 0
        for i in range(len(nums)):
            temp = set()
            for j in range(i, len(nums)):
                
                temp.add(nums[j])
                if(len(temp) == distinct_count):
                    count += 1

        return count



nums = nums = [5,5,5,5]
solution = Solution()
result = solution.countCompleteSubarrays(nums)
print(result)