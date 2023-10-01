class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        remainder_arr = []

        while (n != 0):

            remainder_arr.append(n % k)
            n //= k

        return sum(remainder_arr)


n = 10
k = 10
obj = Solution()
solution = obj.sumBase(n, k)
print(solution)

# 77.1 %