class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        
        freq_dict = {0 : 1}
        
        ans = 0
        cs = 0
        for num in nums:
            cs += num

            if((cs - k) in freq_dict):
                ans += freq_dict[cs - k]


            if(cs not in freq_dict):
                freq_dict[cs] = 1
            else:
                freq_dict[cs] += 1
        
        return ans

nums = [1,2,3]
k = 3
obj = Solution()
result = obj.subarraySum(nums, k)
print(result)