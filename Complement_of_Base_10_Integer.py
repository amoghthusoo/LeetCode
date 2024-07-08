class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        bin_str = bin(n)[2:]

        comp_bin_str = ""

        i = 0
        while(i < len(bin_str)):
            
            if(bin_str[i] == "0"):
                comp_bin_str += "1"
            else:
                comp_bin_str += "0"
            
            i += 1

        out_num = int(comp_bin_str, 2)

        return out_num

n = 5
obj = Solution()
out = obj.bitwiseComplement(n)
print(out)