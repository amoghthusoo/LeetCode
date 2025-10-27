class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        
        freq_dict = {0 : 1}

        ans = 0
        cs = 0
        for num in nums:
            cs += num

            if((cs - goal) in freq_dict):
                ans += freq_dict[cs - goal]

            if(cs not in freq_dict):
                freq_dict[cs] = 1
            else:
                freq_dict[cs] += 1
        
        return ans
