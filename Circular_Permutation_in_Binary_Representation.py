class Solution:
    
    def find_gray(self, n):

        bin_str = bin(n)[2 : ]
        gray_str = bin_str[0]
        for i in range(len(bin_str) - 1):
            gray_str += str(int(bin_str[i]) ^ int(bin_str[i + 1]))
        
        return int(gray_str, 2)


    def circularPermutation(self, n: int, start: int) -> list[int]:
        
        gray_arr = []
        for i in range(2 ** n):
            gray_arr.append(self.find_gray(i))
        
        right_part = []
        i = 0
        while(gray_arr[i] != start):
            right_part.append(gray_arr[i])
            i += 1
        
        left_part = gray_arr[i : ]

        return left_part + right_part

n = 2
start = 3
obj = Solution()
result = obj.circularPermutation(n, start)
print(result)