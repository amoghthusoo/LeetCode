class Solution:
    def countBits(self, n: int) -> list[int]:

        if(n == 0):
            return [0]
        
        ans = [None for _ in range(n + 1)]

        ans[0] = 0
        ans[1] = 1

        if(n % 2 == 0):
            last_index = n // 2
        else:
            last_index = (n - 1)//2

        for i in range(1, last_index + 1):

            try:
                ans[i * 2] = ans[i]
                ans[i * 2 + 1] = ans[i] + 1
            except:
                pass
        
        return ans

n = 0
obj = Solution()
result = obj.countBits(n)
print(result)
