from collections import deque

class Solution:
    def get_palindrome(self):

        queue = deque()

        num_len = 1
        i = 1
        while(True):

            num_str = str(i)

            if(len(num_str) == num_len + 1):
                num_len += 1

                while(len(queue) != 0):
                    yield int(queue.popleft())
            

            left_part = num_str[0 : -1]
            right_part = left_part[-1 : : -1]
            palindrome = left_part + num_str[-1] + right_part
            
            yield int(palindrome)

            right_part = num_str[-1 : : -1]
            palindrome = num_str + right_part
            queue.append(int(palindrome))

            i += 1

    def is_prime(self, n):

        if(n == 1):
            return False

        i = 2
        while(i <= n ** 0.5):

            if(n % i == 0):
                return False
            
            i += 1
        
        return True

    def primePalindrome(self, n: int) -> int:
        
        gen = self.get_palindrome()
        while(True):
            p = next(gen)

            if(p >= n and self.is_prime(p)):
                return p
            

from time import time
s = time()
n = 1
obj = Solution()
result = obj.primePalindrome(n)
print(result)
e = time()
print(e - s)
