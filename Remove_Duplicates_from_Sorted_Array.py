class Solution:
    def removeDuplicates(self, nums: list) -> int | list:
        for element in nums:
            if (nums.count(element) != 1):
                for index in range(0, nums.count(element) - 1):
                    del(nums[nums.index(element)])
        
        return len(nums), nums



input = [0,0,1,1,1,2,2,3,3,4]
obj = Solution()
solution, nums = obj.removeDuplicates(input)
print(solution, nums)