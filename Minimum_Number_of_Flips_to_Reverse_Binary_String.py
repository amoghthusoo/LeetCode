class Solution:
    def minimumFlips(self, n: int) -> int:
        
        bin_str = bin(n)[2 : ]
        reserve_str = bin_str[-1::-1]

        ans = 0
        i = 0
        while(i < len(bin_str)):

            if(bin_str[i] != reserve_str[i]):
                ans += 1

            i += 1
        
        return ans