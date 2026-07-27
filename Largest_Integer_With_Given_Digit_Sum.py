class Solution:
    def largestInteger(self, n: int, s: int) -> int:

        def digit_sum(n):

            total = 0
            for digit in str(n):
                total += int(digit)
            return total

        n = int(10 ** n) - 1
        while(n >= 0):

            if(digit_sum(n) == s):
                return n

            n -= 1

        return -1
            