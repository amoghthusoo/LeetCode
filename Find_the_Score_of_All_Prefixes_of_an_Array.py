class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:

        max_dict = dict()
        _max = float("-inf")
        for i, num in enumerate(nums):
            max_dict[i] = _max = max(_max, nums[i])

        conver = []
        for i in range(len(nums)):
            conver.append(nums[i] + max_dict[i])

        ans = []
        cumm_sum = 0
        for i in range(len(conver)):

            cumm_sum += conver[i]
            ans.append(cumm_sum)

        return ans

nums = [2,3,7,5,10]
obj = Solution()
result = obj.findPrefixScore(nums)
print(result)
