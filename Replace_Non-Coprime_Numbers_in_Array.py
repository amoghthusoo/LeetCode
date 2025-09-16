from collections import deque
from math import gcd, lcm
class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        
        stack = deque([nums[0]])

        i = 1
        while(i < len(nums)):

            if(gcd(stack[-1], nums[i]) == 1):
                stack.append(nums[i])
            
            else:
                stack.append(lcm(stack.pop(), nums[i]))

                while(len(stack) > 1 and gcd(stack[-1], stack[-2]) != 1):
                    stack.append(lcm(stack.pop(), stack.pop()))

            i += 1
        
        return list(stack)
    
nums = [6,4,3,2,7,6,2]
obj = Solution()
result = obj.replaceNonCoprimes(nums)
print(result)