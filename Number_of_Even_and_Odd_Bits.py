class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        
        n_bin = bin(n)[2 : ]

        n_bin = list(n_bin)
        n_bin.reverse()

        even = 0
        odd = 0

        i = 0
        while(i < len(n_bin)):

            if(n_bin[i] == '1'):

                if(i % 2 == 0):
                    even += 1
                else:
                    odd += 1

            i += 1
        
        return [even, odd]

n = 2
obj = Solution()
solution = obj.evenOddBit(n)
print(solution)