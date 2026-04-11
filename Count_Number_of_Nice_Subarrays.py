class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:

        for i, e in enumerate(nums):
            if(e % 2 == 0):
                nums[i] = 0
            else:
                nums[i] = 1

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

nums = [1,1,2,1,1]
k = 3 
obj = Solution()
result = obj.numberOfSubarrays(nums, k)
print(result)
