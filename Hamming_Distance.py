class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        
        if (x > y):
            y_bin = y_bin.zfill(len(x_bin))
        else:
            x_bin = x_bin.zfill(len(y_bin))

        count = 0

        i = 0
        while (i < len(x_bin)):

            if (x_bin[i] != y_bin[i]):
                count += 1

            i += 1

        return count        

x = 1
y = 4
obj = Solution()
solution = obj.hammingDistance(x, y)
print(solution)