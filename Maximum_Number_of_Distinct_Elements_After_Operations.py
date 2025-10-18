class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        
        nums.sort()
        _max = nums[0] - k
        nums[0] = _max
        ans = 1

        i = 1
        while(i < len(nums)):

            m = nums[i] - k
            M = nums[i] + k

            if(nums[i] - k <= _max):
                try_num = _max + 1
            else:
                try_num = nums[i] - k
            
            if(try_num >= m and try_num <= M):
                nums[i] = try_num
                _max = try_num
                ans += 1
            else:
                nums[i] = _max                

            i += 1

        return ans

nums = [89, 69, 98, 23, 55, 14, 87]
k = 47
obj = Solution()
result = obj.maxDistinctElements(nums, k)
print(result)
