from math import factorial as fact
import sys
sys.set_int_max_str_digits(100000)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        inter_out = str(fact(n))
        
        out = 0
        i = len(inter_out) - 1
        while(inter_out[i] == '0'):

            if(inter_out[i] == '0'):
                out += 1

            i -= 1

        return out

n = 100
obj = Solution()
out = obj.trailingZeroes(n)
print(out)