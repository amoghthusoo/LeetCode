class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        
        xor = 0
        for e in derived:
            xor ^= e

        if(xor):
            return False
        else:
            return True

derived = [1,0]
solution = Solution()
result = solution.doesValidArrayExist(derived)
print(result)