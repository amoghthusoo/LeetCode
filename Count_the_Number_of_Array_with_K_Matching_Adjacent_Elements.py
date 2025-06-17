from math import comb
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        
        return (m * comb(n - 1, k) * (m - 1) ** (n - k - 1)) % (10 ** 9 + 7)