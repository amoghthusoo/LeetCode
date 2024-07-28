class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        index_dict = {}

        for index, letter in enumerate(s):
            index_dict[letter] = index

        perm_diff = 0

        for index, letter in enumerate(t):
            perm_diff += abs(index - index_dict[letter])

        return perm_diff
        