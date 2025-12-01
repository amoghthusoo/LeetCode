class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        n = str(n)[-1::-1]
        ans = ""
        
        count = 0
        for d in n:
            ans += d
            count += 1
            if(count == 3):
                ans += "."
                count = 0
        
        ans = ans.rstrip(".")
        ans = ans[-1::-1]
        return ans

n = 987
obj = Solution()
result = obj.thousandSeparator(n)
print(result)