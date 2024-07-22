class Solution:

    def getNoInDifferentBase(self, n, base):
        
        num_str = ""

        while(n != 0):

            num_str += str(n % base)
            n //= base

        num_str = num_str[-1 : : -1]

        return num_str

    def isStrictlyPalindromic(self, n: int) -> bool:
        
        base = 2
        while(base <= n - 2):

            converter_no = self.getNoInDifferentBase(n, base)

            if(converter_no != converter_no[-1: :-1]):
                return False

            base += 1
        
        return True

n = 5
obj = Solution()
out = obj.isStrictlyPalindromic(n)
# print(out)