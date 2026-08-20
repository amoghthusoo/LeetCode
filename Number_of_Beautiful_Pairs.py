from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:

        ans = 0
        i = 0
        while(i < len(nums)):

            j = i + 1
            while(j < len(nums)):

                d1 = int(str(nums[i])[0])
                d2 = int(str(nums[j])[-1])

                if(gcd(d1, d2) == 1):
                    ans += 1


                j += 1
            i += 1

        return ans

