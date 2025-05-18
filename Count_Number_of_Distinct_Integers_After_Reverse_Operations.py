class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        
        int_set = set()
        for num in nums:
            int_set.add(num)
            int_set.add(int(str(num)[-1::-1]))

        return len(int_set)

nums = [2,2,2]
solution = Solution()
result = solution.countDistinctIntegers(nums)
print(result)