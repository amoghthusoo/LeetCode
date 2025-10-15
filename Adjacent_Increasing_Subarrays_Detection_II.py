class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        
        intr_arr = []
        cnt = 1
        for i in range(len(nums) - 1):

            if(nums[i] < nums[i + 1]):
                cnt += 1
            else:
                intr_arr.append(cnt)
                cnt = 1
        
        intr_arr.append(cnt)

        _max = intr_arr[0] // 2
        
        for i in range(1, len(intr_arr)):

            r1 = min(intr_arr[i - 1], intr_arr[i])
            r2 = intr_arr[i] // 2
            r = max(r1, r2)

            if(r > _max):
                _max = r
        
        return _max



nums = [-15,-13,4,7,0,2]

obj = Solution()
result = obj.maxIncreasingSubarrays(nums)
print(result)