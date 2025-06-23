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

    def convert_to_base_k(self, num, k):

        ans = ""

        while(num != 0):
            
            ans += str(num % k)
            num //= k
        
        return ans[-1 : : -1]


    def kMirror(self, k: int, n: int) -> int:
        
        count = 0
        ans = 0
        gen = self.get_palindrome()
        while(count != n):
            p = next(gen)
            p_base_k = self.convert_to_base_k(p, k)
            if(p_base_k == p_base_k[-1 : : -1]):
                ans += p
                count += 1

        return ans

k = 2
n = 30
obj = Solution()
result = obj.kMirror(k, n)
print(result)
