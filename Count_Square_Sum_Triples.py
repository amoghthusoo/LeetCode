class Solution:
    def countTriples(self, n: int) -> int:

        count = 0
        i = 1
        while(i <= n):

            j = 1
            while(j <= n):

                k = 1
                while(k <= n):

                    if(i ** 2 + j ** 2 == k ** 2):
                        count += 1

                    k += 1

                j += 1

            i += 1
            
        return count
        
n = 250
obj = Solution()
out = obj.countTriples(n)
print(out)