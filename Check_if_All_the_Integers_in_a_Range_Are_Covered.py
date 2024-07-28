class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        
        range_set = set()

        for r in ranges:
            range_set = range_set.union(range(r[0], r[1] + 1))

        given_range = set(range(left, right + 1))

        if(range_set.intersection(given_range) == given_range):
            return True
        else:
            return False