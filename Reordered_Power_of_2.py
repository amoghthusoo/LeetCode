from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        i = 0
        while(True):

            target = str(int(2 ** i))
            n_str = str(n)

            if(len(n_str) == len(target) and Counter(target) == Counter(n_str)):
                return True

            if(len(target) > len(n_str)):
                return False
            
            i += 1

n = 822
obj = Solution()
result = obj.reorderedPowerOf2(n)
print(result)