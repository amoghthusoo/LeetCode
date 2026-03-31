class Skiplist:

    def __init__(self):
        self.sl = {}

    def search(self, target: int) -> bool:
        
        if(target in self.sl):
            return True
        return False

    def add(self, num: int) -> None:
        
        if(num not in self.sl):
            self.sl[num] = 1
        else:
            self.sl[num] += 1

    def erase(self, num: int) -> bool:
        
        if(num not in self.sl):
            return False
        
        if(self.sl[num] > 1):
            self.sl[num] -= 1
        else:
            self.sl.pop(num)
        
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)