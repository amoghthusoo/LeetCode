class Solution:

    def is_prime(self, n):

        if(n == 1):
            return False

        if(n == 2):
            return True

        i = 2
        while(i < n):
            
            if(n % i == 0):
                return False
            
            i += 1
        
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:

        ans = 0

        i = left
        while(i <= right):

            bin_str = bin(i)[2 : ]
            set_bits = bin_str.count("1")

            if(self.is_prime(set_bits)):
                ans += 1

            i += 1
        
        return ans

left = 6
right = 10
obj = Solution()
result = obj.countPrimeSetBits(left, right)
print(result)