from math import log2
class Solution:
    def smallestNumber(self, n: int) -> int:
        return int(2 ** (int(log2(n)) + 1) - 1)