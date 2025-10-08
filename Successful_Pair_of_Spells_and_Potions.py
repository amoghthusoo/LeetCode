from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        
        potions.sort()
        return [len(potions) - bisect_left(potions, success / spell) for spell in spells]

spells = [3,1,2]
potions = [8,5,8]
success = 16
obj = Solution()
result = obj.successfulPairs(spells, potions, success)
print(result)