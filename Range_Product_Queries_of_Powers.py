class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        
        n = bin(n)[2 : ]
        powers = []

        i = len(n) - 1
        while(i >= 0):
            
            if(n[i] == "1"):
                powers.append(2 ** (len(n) - i - 1))
            i -= 1
        
        ans = []
        mod = 10 ** 9 + 7
        for query in queries:
            
            product = 1
            i = query[0]
            while(i <= query[1]):
                product = (product * powers[i]) % mod
                i += 1
            
            ans.append(product)

        return ans
    
n = 15
queries = [[0,1],[2,2],[0,3]]
obj = Solution()
result = obj.productQueries(n, queries)
print(result)