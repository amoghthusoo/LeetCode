from copy import deepcopy

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        original = [i for i in range(n)]

        prev = deepcopy(original)
        next = deepcopy(original)

        ans = 0
        while(True):

            for i in range(len(original)):
                
                if(i % 2 == 0):
                    next[i] = prev[i // 2]
                else:
                    next[i] = prev[len(original) // 2 + (i - 1) // 2]
            
            ans += 1

            if(next == original):
                return ans
            
            prev = deepcopy(next)

n = 4
obj = Solution()
result = obj.reinitializePermutation(n)
print(result)