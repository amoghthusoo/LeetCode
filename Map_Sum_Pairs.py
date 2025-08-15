class MapSum:

    def __init__(self):
        self.map = dict()        

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        
        total = 0
        for key, vals in self.map.items():
            try:
                if(key.index(prefix) == 0):
                    total += vals
            except:
                pass
            
        return total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)