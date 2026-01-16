class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None for _ in range(n + 2)]
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        
        self.stream[idKey] = value
        
        if(idKey != self.ptr):
            return []
        else:
            ans = []
            while(self.stream[self.ptr] != None):
                ans.append(self.stream[self.ptr])
                self.ptr += 1
                
            return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)