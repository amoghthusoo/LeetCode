class Solution:
    
    def get_product(self, n):

        n = list(str(n))

        prod = 1
        for d in n:
            prod *= int(d)
        
        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        
        while(self.get_product(n) % t != 0):
            n += 1
        
        return n


n = 10
t = 2
obj = Solution()
result = obj.smallestNumber(n, t)
print(result)