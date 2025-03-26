class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        
        count  = 0
        piles.sort()
        n = len(piles) // 3

        i = -2
        for _ in range(n):
            count += piles[i]
            i -= 2

        return count
        