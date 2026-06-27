from collections import Counter
class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        
        occr_dict = Counter(nums)
        if(1 in occr_dict):
            cnt = occr_dict[1]
            if(cnt % 2 == 0):
                ans = cnt - 1
            else:
                ans = cnt
        else:
            ans = float("-inf")

        occr_dict.pop(1, None)

        for num, freq in occr_dict.items():

            cnt = 1
            k = 1
            while(occr_dict.get(num ** k, 0) >= 2):
                k *= 2
                cnt += 1

            
            if(occr_dict.get(num ** k, 0) == 1):
                ans = max(ans, 2 * cnt - 1)
            else:
                ans = max(ans, 2 * (cnt - 1) - 1)
        
        return ans
    
                
nums = [5,4,1,2,2]
obj = Solution()
result = obj.maximumLength(nums)
print(result)