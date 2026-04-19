from collections import deque
from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):

        combs = combinations(sorted(characters), combinationLength)
        self.dq = deque()
        for comb in combs:
            self.dq.append("".join(comb))

    def next(self) -> str:
        return self.dq.popleft()

    def hasNext(self) -> bool:
        if(self.dq):
            return True
        else:
            return False


# Your CombinationIterator object will be instantiated and called as such:
characters = "abc"
combinationLength = 2
obj = CombinationIterator(characters, combinationLength)
param_1 = obj.next()
param_2 = obj.hasNext()