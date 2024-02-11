import numpy as np
class Solution:
    def construct2DArray(self, original: list, m: int, n: int) -> list:
        
        arr1 = np.array(original)

        try:
            return arr1.reshape(m, n)
        except:
            return []

original = [1,2]
m = 1
n = 1
obj = Solution()
solution = obj.construct2DArray(original, m, n)
print(solution)