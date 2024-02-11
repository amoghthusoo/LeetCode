#NOT SOLVED
class Solution:
    def countDigitOne(self, n: int) -> int:

        counter = 0
        
        i = 1
        while (i <= n):
            
            try:
                counter += str(i).count("1")
            except:
                pass

            i += 1

        return counter

n = 13
obj = Solution()
solution = obj.countDigitOne(n)
print(solution)