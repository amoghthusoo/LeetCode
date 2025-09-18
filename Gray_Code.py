class Solution:
    def grayCode(self, n: int) -> list[int]:
        
        ans = []

        for i in range(2 ** n):

            bin_str = bin(i)[2 : ].zfill(n)        

            gray_str = ""
            gray_str += bin_str[0]

            j = 0
            while(j < n - 1):

                gray_str += str(int(bin_str[j]) ^ int(bin_str[j + 1]))

                j += 1
            
            ans.append(int(gray_str, 2))
        
        return ans

n = 16
obj = Solution()
result = obj.grayCode(n)
print(result)