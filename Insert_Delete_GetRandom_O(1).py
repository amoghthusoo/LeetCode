import random as rd

class RandomizedSet:

    def __init__(self):
        
        self.num_dict = {}

    def insert(self, val: int) -> bool:
        
        if(val not in self.num_dict):
            self.num_dict[val] = None
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        
        if(val in self.num_dict):
            self.num_dict.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        
        return rd.choice(list(self.num_dict.keys()))