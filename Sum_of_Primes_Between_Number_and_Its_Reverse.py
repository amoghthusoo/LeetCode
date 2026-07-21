class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:

        def is_prime(num):

            if(num == 1):
                return False

            i = 2
            n = num ** 0.5
            while(i <= n):

                if(num % i == 0):
                    return False

                i += 1
            
            return True
        
        reversed_num = int(str(n)[-1::-1])
        low = min(n, reversed_num)
        high = max(n, reversed_num)

        ans = 0
        for num in range(low, high + 1):
            if(is_prime(num)):
                ans += num

        return ans

n = 10
obj = Solution()
result = obj.sumOfPrimesInRange(n)
print(result)