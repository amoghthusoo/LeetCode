class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        
        def get_range(num):

            num = list(str(num))
            _min = min(num)
            _max = max(num)

            return int(_max) - int(_min)

        range_dict = dict()
        for num in nums:
            range_dict[num] = get_range(num)
        
        max_range = max(range_dict.values())

        ans = 0
        for num in nums:
            if(range_dict[num] == max_range):
                ans += num

        return ans

nums = [5724,111,350]
obj = Solution()
result = obj.maxDigitRange(nums)
print(result)