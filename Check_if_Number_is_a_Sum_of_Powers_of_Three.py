class Solution:

    def convert_to_base_3_reversed(self, n):
        
        out_str = ""
        while(n != 0):
            out_str += str(n % 3)
            n //= 3
        
        return out_str

    def checkPowersOfThree(self, n: int) -> bool:

        if("2" in self.convert_to_base_3_reversed(n)):
            return False
        else:
            return True

n = 21
solution = Solution()
result = solution.checkPowersOfThree(n)
print(result)