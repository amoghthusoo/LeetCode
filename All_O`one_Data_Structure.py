class AllOne:

    def __init__(self):
        self.str_count = {}
        self.count_str = {}

    def inc(self, key: str) -> None:
        
        if(key not in self.str_count):
            self.str_count[key] = 1

            if(1 not in self.count_str):
                self.count_str[1] = {key}
            else:
                self.count_str[1].add(key)

        else:
            self.str_count[key] += 1

            new_freq = self.str_count[key]
            old_freq = new_freq - 1
            if(new_freq not in self.count_str):
                self.count_str[new_freq] = {key}
            else:
                self.count_str[new_freq].add(key)

            self.count_str[old_freq].remove(key)
            if(len(self.count_str[old_freq]) == 0):
                self.count_str.pop(old_freq)
        
    def dec(self, key: str) -> None:
        
        if(self.str_count[key] > 1):
            self.str_count[key] -= 1

            new_freq = self.str_count[key]
            old_freq = new_freq + 1

            if(new_freq not in self.count_str):
                self.count_str[new_freq] = {key}
            else:
                self.count_str[new_freq].add(key)
            
            self.count_str[old_freq].remove(key)

            if(len(self.count_str[old_freq]) == 0):
                self.count_str.pop(old_freq)

        else:
            self.str_count.pop(key)

            self.count_str[1].remove(key)

            if(len(self.count_str[1]) == 0):
                self.count_str.pop(1)


    def getMaxKey(self) -> str:
        try:
            return next(iter(self.count_str[max(self.count_str)])) 
        except:
            return ""

    def getMinKey(self) -> str:
        try:
            return next(iter(self.count_str[min(self.count_str)])) 
        except:
            return ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()