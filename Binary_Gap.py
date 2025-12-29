class Solution:
    def binaryGap(self, n: int) -> int:
        
        bin_str = bin(n)[2 : ]
        pos_arr = []
        
        for (i, d) in enumerate(bin_str):
            if(d == "1"):
                pos_arr.append(i)
        
        max_diff = 0
        i = 1
        while(i < len(pos_arr)):

            temp_diff = pos_arr[i] - pos_arr[i - 1]
            if(temp_diff > max_diff):
                max_diff = temp_diff
            i += 1
        
        return max_diff

n = 22
obj = Solution()
result = obj.binaryGap(n)
print(result)
