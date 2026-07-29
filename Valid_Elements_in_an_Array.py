class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:

        if(len(nums) == 1):
            return nums

        max_left = dict()
        max_right = dict()

        _max = float("-inf")
        i = 0
        while(i < len(nums)):

            max_left[i] = _max = max(_max, nums[i])
            i += 1

        _max = float("-inf")
        i = len(nums) - 1
        while(i >= 0):

            max_right[i] = _max = max(_max, nums[i])
            i -= 1

        ans = [nums[0]]
        i = 1
        while(i < len(nums) - 1):

            if(nums[i] > max_left[i - 1] or nums[i] > max_right[i + 1]):
                ans.append(nums[i])

            i += 1

        ans.append(nums[-1])
        return ans

nums = [7,3,2,6]
obj = Solution()
result = obj.findValidElements(nums)
print(result)