import random as rd
from copy import deepcopy

class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.nums_copy = deepcopy(self.nums)

    def reset(self) -> list[int]:
        return self.nums

    def shuffle(self) -> list[int]:
        
        temp = []
        while(len(self.nums_copy) != 0): 
            temp.append(self.nums_copy.pop(rd.randrange(len(self.nums_copy))))

        self.nums_copy = deepcopy(temp)
        return temp