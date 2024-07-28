class Solution:
    def minChanges(self, n: int, k: int) -> int:
        
        bin_str_n = bin(n)[2:]
        bin_str_k = bin(k)[2:]

        if(n > k):
            bin_str_k = bin_str_k.zfill(len(bin_str_n))
        elif(k > n):
            bin_str_n = bin_str_n.zfill(len(bin_str_k))

        count = 0

        i = 0
        while(i < len(bin_str_n)):

            if(bin_str_n[i] != bin_str_k[i]):

                if(bin_str_n[i] == '1'):
                    count += 1
                else:
                    return -1

            i += 1

        return count

n = 13
k = 4
obj = Solution()
out = obj.minChanges(n, k)
print(out)
