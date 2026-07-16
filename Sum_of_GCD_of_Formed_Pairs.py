from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        mxi = nums[0]
        prefixGcd = []
        for num in nums:
            if(num > mxi):
                mxi = num

            prefixGcd.append(gcd(num, mxi))
        
        prefixGcd.sort()

        i = 0
        j = len(prefixGcd) - 1
        
        ans = 0
        while(i < len(prefixGcd)//2):
            
            ans += gcd(prefixGcd[i], prefixGcd[j])
            
            i += 1
            j -= 1

        return ans        

nums = [2,6,4]
obj = Solution()
result = obj.gcdSum(nums)
print(result)