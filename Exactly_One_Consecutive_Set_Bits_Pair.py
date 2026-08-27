class Solution:
    def consecutiveSetBits(self, n: int) -> bool:

        if(n < 2):
            return False
        
        bin_str = bin(n)[2:]

        i = 0
        j = 1

        cnt = 0
        while(j < len(bin_str)):
            if(bin_str[i] == bin_str[j] == "1"):
                cnt += 1

            i += 1
            j += 1

        if(cnt == 1):
            return True

        return False

